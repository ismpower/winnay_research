#!/usr/bin/env python3
"""Build a reproducible provenance inventory for the Bruno/E3 legacy corpus.

The legacy tree is read-only. All outputs are written beside this script under
../data. The parser favors evidence preservation over choosing a canonical copy.
"""

from __future__ import annotations

import bisect
import csv
import hashlib
import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

LEGACY_ROOT = Path("/home/winnay/Documents/Codex/E3_Engine")
AUDIT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = AUDIT_ROOT / "data"

SKIP_DIRS = {
    ".git", ".venv", "__pycache__", "node_modules", "bruno_env", "davp_env",
    "site-packages", ".ipynb_checkpoints", "datasets",
    "snfluxes-public-master", "snewpy-models-presn-master",
    "sne-1990-1999-master", "sne-2000-2004-master", "sne-2005-2009-master",
    "sne-2010-2014-master", "Kato_2017", "Patton_2017", "Yoshida_2016",
}

TEXT_EXTS = {
    ".py", ".md", ".txt", ".rst", ".tex", ".json", ".csv", ".tsv",
    ".ipynb", ".yaml", ".yml", ".toml", ".ini", ".m", ".cpp", ".h",
}
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".svg", ".pdf", ".gif", ".tif", ".tiff"}

CATEGORIES = {
    "core_geometry": re.compile(
        r"bruno constant|brunoestimate|beta[_ ]?b|β[_ ]?b|kappa|κ|"
        r"\bA\s*/\s*V\b|\b3\s*/\s*R\b|surface.?project|volumetric entropy|entropy",
        re.I,
    ),
    "cosmic_events": re.compile(
        r"supernova|\bSN\s*\d|\bSNe\b|gamma.?ray|\bGRB\b|neutrino|icecube|"
        r"BATSE|GW150914|LIGO|Betelgeuse|fluence",
        re.I,
    ),
    "laser_lab": re.compile(
        r"laser.?cool|supercool|MDQT|magneto.?optical|Doppler.?cool|plasma",
        re.I,
    ),
    "horizon_entropy": re.compile(
        r"event horizon|apparent horizon|trapping horizon|Schwarzschild|"
        r"Bekenstein|Hawking|holograph|entropy.?bound|black.?hole",
        re.I,
    ),
    "engine": re.compile(r"\bE3\b|E3[_ -]?Engine|bruno[_ -]?engine|collapse[_ -]?tracker", re.I),
}

DATE_PATTERNS = [
    re.compile(r"\b(19\d{2}|20\d{2})[-_/](0?[1-9]|1[0-2])[-_/]([0-2]?\d|3[01])\b"),
    re.compile(r"\b([0-2]?\d|3[01])[-_/](0?[1-9]|1[0-2])[-_/](19\d{2}|20\d{2})\b"),
    re.compile(
        r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
        r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
        r"Dec(?:ember)?)\s+\d{1,2},?\s+(?:19|20)\d{2}\b",
        re.I,
    ),
]

CLAIM_PATTERNS = {
    "kappa_literal": re.compile(
        r"(?i)(?:kappa|κ|bruno(?:[_ ]constant)?)[^\n]{0,80}?"
        r"(?:=|≈|~|:)[^\n]{0,20}?([-+]?\d+(?:\.\d+)?(?:\s*[eE×x*]\s*[-+]?\d+)?)"
    ),
    "temperature_threshold": re.compile(
        r"(?i)(?:T[_ ]?(?:collapse|critical)|collapse temperature|threshold)"
        r"[^\n]{0,80}?([-+]?\d+(?:\.\d+)?(?:\s*[eE×x*^]\s*[-+]?\d+)?)\s*K\b"
    ),
    "fluence_threshold": re.compile(
        r"(?i)(?:fluence[^\n]{0,30}?threshold|threshold[^\n]{0,30}?fluence)"
        r"[^\n]{0,50}?([-+]?\d+(?:\.\d+)?(?:\s*[eE×x*^]\s*[-+]?\d+)?)\s*J\s*/?\s*m(?:\^?2|²)"
    ),
    "area_volume": re.compile(r"(?i)(?:A\s*/\s*V|area\s*/\s*volume|3\s*/\s*[Rr])"),
    "entropy_density_ratio": re.compile(r"(?i)s_?3D\s*/\s*s_?2D|s_?volume\s*/\s*s_?surface"),
    "synthetic_temperature": re.compile(r"(?i)temperature[^\n]{0,80}(?:10\s*\*\*|10\s*\^)"),
    "planck_route": re.compile(r"(?i)3\s*/\s*\(?\s*l_?P\s*[·*]\s*T_?P|3\s*k_?B\s*/\s*\(?\s*(?:hbar|ℏ)\s*[·*]\s*c"),
    "black_hole_route": re.compile(r"(?i)3\s*/\s*\(?\s*R_?s\s*[·*]\s*T_?H|12\s*(?:pi|π)\s*k_?B"),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def safe_text(path: Path, limit: int = 8_000_000) -> str:
    try:
        if path.stat().st_size > limit:
            return ""
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def notebook_text_and_meta(path: Path) -> tuple[str, dict]:
    meta = {
        "code_cells": 0,
        "markdown_cells": 0,
        "outputs": 0,
        "embedded_images": 0,
        "execution_counts": [],
        "kernel": "",
    }
    try:
        nb = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return "", meta
    chunks = []
    meta["kernel"] = nb.get("metadata", {}).get("kernelspec", {}).get("display_name", "")
    for cell in nb.get("cells", []):
        ctype = cell.get("cell_type", "")
        if ctype == "code":
            meta["code_cells"] += 1
            if cell.get("execution_count") is not None:
                meta["execution_counts"].append(cell["execution_count"])
        elif ctype == "markdown":
            meta["markdown_cells"] += 1
        src = cell.get("source", [])
        chunks.append(src if isinstance(src, str) else "".join(src))
        for output in cell.get("outputs", []):
            meta["outputs"] += 1
            data = output.get("data", {})
            for mime in ("image/png", "image/jpeg", "image/svg+xml"):
                if mime in data:
                    meta["embedded_images"] += 1
            text = output.get("text", [])
            if text:
                chunks.append(text if isinstance(text, str) else "".join(text))
            plain = data.get("text/plain", [])
            if plain:
                chunks.append(plain if isinstance(plain, str) else "".join(plain))
    return "\n".join(chunks), meta


def embedded_dates(text: str) -> list[str]:
    found = []
    for pattern in DATE_PATTERNS:
        found.extend(m.group(0) for m in pattern.finditer(text[:2_000_000]))
    return sorted(set(found))[:30]


def categories_for(path_text: str, content: str) -> list[str]:
    haystack = path_text + "\n" + content[:2_000_000]
    return [name for name, pattern in CATEGORIES.items() if pattern.search(haystack)]


def write_csv(name: str, rows: list[dict], fields: list[str]) -> None:
    with (DATA_DIR / name).open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def discover_git_roots() -> list[Path]:
    roots = []
    for current, dirs, _files in os.walk(LEGACY_ROOT):
        if ".git" in dirs:
            roots.append(Path(current))
            dirs.remove(".git")
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    # The corpus root is a wrapper snapshot containing many nested repositories;
    # its history is both expensive and less authoritative than those projects.
    return sorted((p for p in roots if p != LEGACY_ROOT), key=lambda p: (len(p.parts), str(p)))


def git_history(git_root: Path) -> dict[str, dict]:
    cmd = [
        "git", "-C", str(git_root), "log", "--all", "--reverse",
        "--date=iso-strict", "--format=@@%H%x09%aI%x09%cI%x09%s", "--name-only",
    ]
    try:
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
    except (subprocess.SubprocessError, OSError):
        return {}
    result: dict[str, dict] = {}
    current = None
    for line in proc.stdout.splitlines():
        if line.startswith("@@"):
            parts = line[2:].split("\t", 3)
            if len(parts) == 4:
                current = {"commit": parts[0], "author_date": parts[1], "commit_date": parts[2], "subject": parts[3]}
            continue
        rel = line.strip()
        if not rel or current is None:
            continue
        entry = result.setdefault(rel, {"first": current.copy(), "last": current.copy(), "touches": 0})
        entry["last"] = current.copy()
        entry["touches"] += 1
    return result


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    artifacts = []
    notebooks = []
    media = []
    claims = []
    hashes: dict[str, list[dict]] = defaultdict(list)

    for current, dirs, files in os.walk(LEGACY_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            path = Path(current) / filename
            ext = path.suffix.lower()
            if ext not in TEXT_EXTS | MEDIA_EXTS:
                continue
            rel = path.relative_to(LEGACY_ROOT).as_posix()
            if ext in MEDIA_EXTS and not categories_for(rel, ""):
                continue
            try:
                raw = path.read_bytes()
                stat = path.stat()
            except OSError:
                continue
            digest = sha256_bytes(raw)
            text = ""
            nbmeta = None
            if ext == ".ipynb":
                text, nbmeta = notebook_text_and_meta(path)
            elif ext in TEXT_EXTS:
                text = raw.decode("utf-8", errors="replace") if len(raw) <= 8_000_000 else ""
            cats = categories_for(rel, text)
            if not cats:
                continue
            row = {
                "path": rel,
                "extension": ext,
                "size_bytes": stat.st_size,
                "mtime_utc": iso_mtime(path),
                "sha256": digest,
                "categories": ";".join(cats),
                "embedded_dates": ";".join(embedded_dates(text)),
            }
            artifacts.append(row)
            hashes[digest].append(row)

            if nbmeta is not None:
                notebooks.append({
                    "path": rel,
                    "sha256": digest,
                    "mtime_utc": row["mtime_utc"],
                    "categories": row["categories"],
                    "code_cells": nbmeta["code_cells"],
                    "markdown_cells": nbmeta["markdown_cells"],
                    "outputs": nbmeta["outputs"],
                    "embedded_images": nbmeta["embedded_images"],
                    "execution_count_min": min(nbmeta["execution_counts"], default=""),
                    "execution_count_max": max(nbmeta["execution_counts"], default=""),
                    "kernel": nbmeta["kernel"],
                    "embedded_dates": row["embedded_dates"],
                })

            if ext in MEDIA_EXTS:
                media.append({
                    "path": rel,
                    "extension": ext,
                    "size_bytes": stat.st_size,
                    "mtime_utc": row["mtime_utc"],
                    "sha256": digest,
                    "categories_from_path": row["categories"],
                    "stem": path.stem,
                })

            if text:
                claim_text = text[:4_000_000]
                line_starts = [0]
                line_starts.extend(match.end() for match in re.finditer("\n", claim_text))
                for claim_type, pattern in CLAIM_PATTERNS.items():
                    for match in pattern.finditer(claim_text):
                        line_index = bisect.bisect_right(line_starts, match.start()) - 1
                        line = line_index + 1
                        start = line_starts[line_index]
                        end_pos = claim_text.find("\n", match.end())
                        end = len(claim_text) if end_pos < 0 else end_pos
                        context = re.sub(r"\s+", " ", claim_text[start:end]).strip()[:500]
                        claims.append({
                            "path": rel,
                            "line": line,
                            "claim_type": claim_type,
                            "value": match.group(1) if match.lastindex else "",
                            "context": context,
                            "sha256": digest,
                        })

    content_groups = []
    for digest, rows in hashes.items():
        if len(rows) < 2:
            continue
        ordered = sorted(rows, key=lambda r: (r["mtime_utc"], r["path"]))
        for index, row in enumerate(ordered):
            content_groups.append({
                "sha256": digest,
                "copies": len(rows),
                "candidate_order": index + 1,
                "path": row["path"],
                "mtime_utc": row["mtime_utc"],
            })

    print(
        f"content inventory: {len(artifacts)} artifacts, {len(notebooks)} notebooks, "
        f"{len(media)} media, {len(claims)} claims",
        flush=True,
    )

    git_events = []
    git_roots = discover_git_roots() if os.environ.get("PROVENANCE_FULL_GIT") == "1" else []
    artifact_paths = {row["path"] for row in artifacts}
    for root in git_roots:
        history = git_history(root)
        prefix = root.relative_to(LEGACY_ROOT).as_posix()
        for repo_rel, event in history.items():
            corpus_rel = f"{prefix}/{repo_rel}" if prefix != "." else repo_rel
            if corpus_rel not in artifact_paths:
                continue
            git_events.append({
                "path": corpus_rel,
                "git_root": prefix,
                "first_commit": event["first"]["commit"],
                "first_author_date": event["first"]["author_date"],
                "first_subject": event["first"]["subject"],
                "last_commit": event["last"]["commit"],
                "last_author_date": event["last"]["author_date"],
                "last_subject": event["last"]["subject"],
                "touches": event["touches"],
            })

    artifacts.sort(key=lambda r: r["path"])
    notebooks.sort(key=lambda r: r["path"])
    media.sort(key=lambda r: r["path"])
    claims.sort(key=lambda r: (r["path"], r["line"], r["claim_type"]))
    git_events.sort(key=lambda r: (r["first_author_date"], r["path"]))

    write_csv("artifacts.csv", artifacts, [
        "path", "extension", "size_bytes", "mtime_utc", "sha256", "categories", "embedded_dates",
    ])
    write_csv("content_groups.csv", content_groups, [
        "sha256", "copies", "candidate_order", "path", "mtime_utc",
    ])
    write_csv("notebooks.csv", notebooks, [
        "path", "sha256", "mtime_utc", "categories", "code_cells", "markdown_cells",
        "outputs", "embedded_images", "execution_count_min", "execution_count_max", "kernel", "embedded_dates",
    ])
    write_csv("media.csv", media, [
        "path", "extension", "size_bytes", "mtime_utc", "sha256", "categories_from_path", "stem",
    ])
    write_csv("claims.csv", claims, [
        "path", "line", "claim_type", "value", "context", "sha256",
    ])
    write_csv("git_events.csv", git_events, [
        "path", "git_root", "first_commit", "first_author_date", "first_subject",
        "last_commit", "last_author_date", "last_subject", "touches",
    ])

    summary = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "legacy_root": str(LEGACY_ROOT),
        "artifact_count": len(artifacts),
        "notebook_count": len(notebooks),
        "media_count": len(media),
        "claim_count": len(claims),
        "duplicate_content_groups": sum(1 for rows in hashes.values() if len(rows) > 1),
        "git_roots_scanned": [str(p.relative_to(LEGACY_ROOT)) for p in git_roots],
        "git_event_count": len(git_events),
        "skipped_directories": sorted(SKIP_DIRS),
    }
    (DATA_DIR / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
