#!/usr/bin/env python3
"""Extract targeted Git provenance for high-value Bruno/E3 artifacts.

This intentionally avoids a corpus-wide Git walk: the legacy folder contains
copied and nested repositories whose wrapper histories add cost without adding
authorship evidence.
"""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path

LEGACY = Path("/home/winnay/Documents/Codex/E3_Engine")
OUT = Path(__file__).resolve().parent.parent / "data" / "git_events.csv"

QUERIES = [
    (
        "Entropy-Collapse-Research",
        [
            "Scripts/Entropy Collapse Test/Bruno Constant.py",
            "Scripts/Entropy Collapse Test/Entropy Collapse Test 1.5.py",
            "Figures/Figures Datas/Figure_Waves_Timeline.csv",
            "Entropy_Hypothesis_History/Hypothesis/LaTeX TimeStamp.png",
            "Entropy_Hypothesis_History/Hypothesis/Entropy_Project_Summary_UPDATED.TeX",
        ],
    ),
    (
        "Bruno_Entropy_Project",
        [
            "data/notes/Bruno Constant Note.txt",
            "data/registry/bruno_events_registry.csv",
            "notebooks/Bruno_timeline_analysis.ipynb",
            "notebooks/Fluence_Model_Comparison.ipynb",
        ],
    ),
    (
        "CLEAN_WORKSPACE/archived_research/bruno-collapse-unified",
        [
            "docs/theory/bruno_constant_derivation.json",
            "scripts/legacy_import/Final/Bruno_Constant_Extraction.py",
        ],
    ),
    (
        "E3_CURRENT_PRODUCTION",
        [
            "README.md",
            "e3_engine",
            "bruno_framework",
            "external/mdqt-sim/laser-cooling-2019",
        ],
    ),
]


def history(repo: Path, paths: list[str]) -> list[dict]:
    command = [
        "git", "-C", str(repo), "log", "--all", "--reverse",
        "--date=iso-strict", "--format=@@%H%x09%aI%x09%s", "--name-only", "--",
        *paths,
    ]
    proc = subprocess.run(command, check=True, capture_output=True, text=True)
    current = None
    events = []
    for line in proc.stdout.splitlines():
        if line.startswith("@@"):
            commit, date, subject = line[2:].split("\t", 2)
            current = (commit, date, subject)
        elif line.strip() and current:
            commit, date, subject = current
            events.append({
                "repository": repo.relative_to(LEGACY).as_posix(),
                "path": line.strip(),
                "commit": commit,
                "author_date": date,
                "subject": subject,
            })
    return events


def main() -> None:
    rows = []
    for repo_rel, paths in QUERIES:
        rows.extend(history(LEGACY / repo_rel, paths))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["repository", "path", "commit", "author_date", "subject"],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} targeted Git events to {OUT}")


if __name__ == "__main__":
    main()

