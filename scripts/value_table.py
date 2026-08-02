#!/usr/bin/env python3
"""Phase 3: build /tmp/audit/VALUE_TABLE.md from the Phase 2 grep output only.

Reads ONLY /tmp/audit/*.txt (match line +/-2 context already captured).
Never opens a source file. Appends section by section.
"""
import os
import re
from collections import defaultdict

AUD = "/tmp/audit"
OUT = os.path.join(AUD, "VALUE_TABLE.md")
SP = "/tmp/claude-1000/-home-winnay-Documents-Codex-E3-Engine/da6cb24a-56a3-46f8-afb7-5ecfd53a1646/scratchpad"

EXT = r"(?:py|ipynb|md|tex|txt|js|html?|ya?ml|json|cfg|ini|sh|rst|toml)"
LINE = re.compile(r"^(?P<path>.+?\." + EXT + r")[:-](?P<line>\d+)[:-](?P<body>.*)$")
NUM = r"[-+]?(?:\d+\.?\d*(?:[eE][-+]?\d+)?|\.\d+(?:[eE][-+]?\d+)?)"

# audit file -> (target symbol regex, display name)
TARGETS = [
    ("kappa.txt",                 r"kappa",                            "kappa"),
    ("bruno_constant.txt",        r"kappa|bruno_?constant|BRUNO_?CONSTANT", "kappa / bruno_constant"),
    ("t_hawking_values.txt",      r"T_H|T_hawking|T_hawk",             "T_H"),
    ("r_schwarzschild_values.txt", r"r_s|R_s|R_schwarzschild|R_sch",   "R_s"),
    ("schwarzschild.txt",         r"r_s|R_s|R_schwarzschild|R_sch",    "R_s (wide sweep)"),
    ("planck_units.txt",          r"[lLtT]_planck|[TtlL]_P|planck_\w+", "Planck units"),
    ("relaxation.txt",            r"tau|relaxation_time",              "tau / relaxation_time"),
    ("hawking.txt",               r"T_H|T_hawking|T_hawk",             "T_H (wide sweep)"),
]

# path -> content hash, to tell real divergence from copy-paste
HASH = {}
try:
    with open(os.path.join(SP, "core_hashes.txt")) as fh:
        for ln in fh:
            h, _, p = ln.rstrip("\n").partition("  ")
            HASH[p] = h
except OSError:
    pass


def branch(path):
    """Top two path components -- the 'phase'/'branch' identity."""
    parts = path.lstrip("./").split("/")
    return "/".join(parts[:2]) if len(parts) > 1 else parts[0]


def parse(fname, symre):
    """Yield (symbol, value, path, lineno) from a grep -C2 output file."""
    assign = re.compile(r"\b(" + symre + r")\b\s*=\s*\(?\s*(" + NUM + r")\b")
    seen = set()
    path = os.path.join(AUD, fname)
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8", errors="replace") as fh:
        for raw in fh:
            m = LINE.match(raw.rstrip("\n"))
            if not m:
                continue
            body = m.group("body")
            if len(body) > 400:
                continue
            for a in assign.finditer(body):
                key = (a.group(1), a.group(2), m.group("path"), m.group("line"))
                if key not in seen:
                    seen.add(key)
                    yield key


def section(fh, fname, symre, label):
    rows = list(parse(fname, symre))
    fh.write(f"\n## `{fname}` — {label}\n\n")
    if not rows:
        fh.write("_No numeric assignments matched._\n")
        return
    groups = defaultdict(list)
    for sym, val, path, lineno in rows:
        groups[val].append((sym, path, lineno))

    fh.write(f"{len(rows)} assignment sites, "
             f"{len({r[2] for r in rows})} distinct files, "
             f"{len(groups)} distinct values.\n\n")
    fh.write("| Value | Sites | Files | Unique contents | Branches |\n")
    fh.write("|---|---:|---:|---:|---|\n")

    order = sorted(groups.items(), key=lambda kv: -len({x[1] for x in kv[1]}))
    for val, items in order:
        files = {x[1] for x in items}
        hashes = {HASH.get(f) for f in files if HASH.get(f)}
        brs = sorted({branch(f) for f in files})
        shown = ", ".join(f"`{b}`" for b in brs[:4])
        if len(brs) > 4:
            shown += f" +{len(brs)-4} more"
        uniq = str(len(hashes)) if hashes else "—"
        fh.write(f"| `{val}` | {len(items)} | {len(files)} | {uniq} | {shown} |\n")

    # Per-value detail: which branch used what.
    fh.write("\n<details><summary>Branch breakdown</summary>\n\n")
    for val, items in order:
        fh.write(f"\n**`{val}`**\n\n")
        bybr = defaultdict(set)
        for sym, path, lineno in items:
            bybr[branch(path)].add(f"{path}:{lineno}")
        for b in sorted(bybr):
            locs = sorted(bybr[b])
            fh.write(f"- `{b}` — {len(locs)} site(s)\n")
            for loc in locs[:6]:
                fh.write(f"  - `{loc}`\n")
            if len(locs) > 6:
                fh.write(f"  - _…{len(locs)-6} more_\n")
    fh.write("\n</details>\n")


def main():
    with open(OUT, "w") as fh:
        fh.write("# Value Table — grouped by value, not by file\n\n")
        fh.write("Built from `/tmp/audit/*.txt` (Phase 2 grep output) only. "
                 "No source file was opened.\n\n")
        fh.write("**Reading the columns.** *Sites* counts assignment "
                 "occurrences. *Files* counts distinct paths. *Unique contents* "
                 "counts distinct md5s among those paths — if Files is 8 but "
                 "Unique contents is 1, that is one file copied 8 times, not "
                 "eight independent decisions. *Branches* are top-two path "
                 "components, the unit at which a rebuild/session diverged.\n")
    for fname, symre, label in TARGETS:
        with open(OUT, "a") as fh:
            section(fh, fname, symre, label)
        print(f"appended {fname}")


if __name__ == "__main__":
    main()
