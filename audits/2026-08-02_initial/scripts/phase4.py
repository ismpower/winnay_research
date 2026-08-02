#!/usr/bin/env python3
"""Phase 4: folder-level duplicate/orphan detection by filename, not content.

Finds (a) filenames recurring across trees with DIVERGENT contents -- the
"silently replaced" case -- and (b) directory pairs that are near-identical
by filename set.
"""
import os
from collections import defaultdict

SP = os.path.dirname(os.path.abspath(__file__))
OUT = "/tmp/audit/FOLDER_AUDIT.md"
EMPTY = "d41d8cd98f00b204e9800998ecf8427e"

paths = {}
with open(os.path.join(SP, "core_hashes.txt")) as fh:
    for ln in fh:
        h, _, p = ln.rstrip("\n").partition("  ")
        paths[p] = h

# (a) same basename, multiple distinct non-empty hashes
byname = defaultdict(lambda: defaultdict(list))
for p, h in paths.items():
    byname[os.path.basename(p)][h].append(p)

divergent = []
for name, hs in byname.items():
    nonempty = {h: ps for h, ps in hs.items() if h != EMPTY}
    if len(nonempty) > 1:
        divergent.append((name, hs, nonempty))
divergent.sort(key=lambda x: (-len(x[2]), -sum(len(v) for v in x[1].values())))

# (b) directory filename-set similarity
dirs = defaultdict(set)
for p in paths:
    dirs[os.path.dirname(p)].add(os.path.basename(p))
dirs = {d: s for d, s in dirs.items() if len(s) >= 4}

pairs = []
keys = sorted(dirs)
for i, a in enumerate(keys):
    for b in keys[i + 1:]:
        sa, sb = dirs[a], dirs[b]
        inter = len(sa & sb)
        if inter < 4:
            continue
        j = inter / len(sa | sb)
        if j >= 0.6:
            ident = sum(1 for n in (sa & sb)
                        if paths.get(f"{a}/{n}") == paths.get(f"{b}/{n}"))
            pairs.append((j, a, b, inter, ident, len(sa), len(sb)))
pairs.sort(reverse=True)

with open(OUT, "w") as fh:
    fh.write("# Folder-Level Audit — filename recurrence and parallel trees\n\n")
    fh.write("Compares folder names and file-name sets, not contents. "
             "Content hashes are used only to say whether same-named files "
             "actually agree.\n\n")

    fh.write(f"## A. Same filename, divergent content ({len(divergent)} filenames)\n\n")
    fh.write("These are the silent-replacement risks: one name, more than one "
             "non-empty implementation. Ordered by number of competing versions.\n\n")
    fh.write("| Filename | Versions | Copies | Empty | Spread |\n|---|---:|---:|---:|---|\n")
    for name, hs, ne in divergent[:40]:
        tot = sum(len(v) for v in hs.values())
        nempty = len(hs.get(EMPTY, []))
        trees = {p.lstrip("./").split("/")[0] for v in hs.values() for p in v}
        fh.write(f"| `{name}` | {len(ne)} | {tot} | {nempty} | {len(trees)} trees |\n")

    fh.write("\n<details><summary>Per-version locations (top 20)</summary>\n\n")
    for name, hs, ne in divergent[:20]:
        fh.write(f"\n### `{name}`\n\n")
        for h, ps in sorted(hs.items(), key=lambda kv: -len(kv[1])):
            tag = "**EMPTY**" if h == EMPTY else f"`{h[:8]}`"
            fh.write(f"- {tag} — {len(ps)} copy(ies)\n")
            for p in sorted(ps)[:8]:
                fh.write(f"  - `{p}`\n")
            if len(ps) > 8:
                fh.write(f"  - _…{len(ps)-8} more_\n")
    fh.write("\n</details>\n")

    fh.write(f"\n## B. Near-identical directories ({len(pairs)} pairs, Jaccard >= 0.6)\n\n")
    fh.write("`Shared` = filenames in both. `Identical` = of those, how many have "
             "the same content. A pair with Shared >> Identical is two trees that "
             "*look* like copies but have drifted.\n\n")
    fh.write("| Jaccard | Dir A | Dir B | Shared | Identical |\n|---:|---|---|---:|---:|\n")
    for j, a, b, inter, ident, na, nb in pairs[:45]:
        flag = " ⚠️" if ident < inter else ""
        fh.write(f"| {j:.2f} | `{a}` | `{b}` | {inter} | {ident}{flag} |\n")

print(f"divergent filenames: {len(divergent)}")
print(f"near-identical dir pairs: {len(pairs)}")
drifted = [p for p in pairs if p[4] < p[3]]
print(f"  of which DRIFTED (shared > identical): {len(drifted)}")
print(f"filenames that are empty in >=1 place: "
      f"{sum(1 for n, hs, _ in byname.items() if EMPTY in hs)}")
