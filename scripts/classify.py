#!/usr/bin/env python3
"""Phase 4: classify every core file as canonical / duplicate / superseded / orphan."""
import os
import re
import sys
from collections import defaultdict

SP = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/winnay/Documents/Codex/E3_Engine"

# Lower rank = more likely to be the surviving canonical copy.
TREE_RANK = [
    ("E3_CURRENT_PRODUCTION", 0), ("CLEAN_WORKSPACE", 1), ("E3_Project", 2),
    ("notebooks", 2), ("Bruno_Entropy_Project", 3), ("bruno-framework-clean", 3),
    ("E3_Project_REBUILT", 4), ("bruno-simulator-RESTRUCTURED", 4),
    ("bruno-simulator-latest", 5), ("Entropy-Collapse-Research", 5),
    ("github_repos", 6), ("Entropy-Collapse-Research-main", 6),
    ("E3_Project_OLD_MESSY", 8),
]
STALE = re.compile(r"(archive|archived|legacy|backup|dupe_|old|_bak|New folder|"
                   r"phase[123]|rev[0-9]|rework|checkpoint)", re.I)


def rank(path):
    top = path.split("/")[1] if path.startswith("./") and "/" in path[2:] else ""
    base = 7
    for name, r in TREE_RANK:
        if top == name:
            base = r
            break
    if STALE.search(path):
        base += 10
    return (base, path.count("/"), len(path))


def main():
    groups = defaultdict(list)
    with open(os.path.join(SP, "core_hashes.txt")) as fh:
        for line in fh:
            h, _, p = line.rstrip("\n").partition("  ")
            groups[h].append(p)

    empty_hash = "d41d8cd98f00b204e9800998ecf8427e"
    canonical, duplicate = {}, []
    for h, paths in groups.items():
        if h == empty_hash:
            continue
        best = sorted(paths, key=rank)[0]
        canonical[h] = best
        for p in paths:
            if p != best:
                duplicate.append((p, best))

    # Build import graph over canonical files to find orphans.
    canon_paths = set(canonical.values())
    modnames = defaultdict(set)
    for p in canon_paths:
        if p.endswith(".py"):
            modnames[os.path.basename(p)[:-3]].add(p)
    stems = {os.path.splitext(os.path.basename(p))[0] for p in canon_paths}

    referenced = set()
    imp = re.compile(r"^\s*(?:from|import)\s+([A-Za-z_][\w.]*)", re.M)
    tex = re.compile(r"\\(?:input|include)\{([^}]+)\}")
    for p in canon_paths:
        fp = os.path.join(ROOT, p[2:])
        try:
            with open(fp, encoding="utf-8", errors="replace") as fh:
                txt = fh.read()
        except Exception:
            continue
        for m in imp.finditer(txt):
            head = m.group(1).split(".")[0]
            if head in modnames:
                referenced |= modnames[head]
        for m in tex.finditer(txt):
            b = os.path.splitext(os.path.basename(m.group(1)))[0]
            for q in canon_paths:
                if os.path.splitext(os.path.basename(q))[0] == b:
                    referenced.add(q)

    superseded, orphan, live = [], [], []
    for p in sorted(canon_paths):
        if STALE.search(p):
            superseded.append(p)
        elif p in referenced or p.endswith((".md", ".tex", ".ipynb")):
            live.append(p)
        else:
            orphan.append(p)

    def w(name, rows):
        with open(os.path.join(SP, name), "w") as fh:
            for r in rows:
                fh.write(("\t".join(r) if isinstance(r, tuple) else r) + "\n")
        return len(rows)

    n_live = w("cls_canonical.txt", live)
    n_sup = w("cls_superseded.txt", superseded)
    n_orph = w("cls_orphan.txt", orphan)
    n_dup = w("cls_duplicate.tsv", duplicate)
    n_empty = len(groups.get(empty_hash, []))

    print(f"canonical (live)   {n_live}")
    print(f"superseded         {n_sup}")
    print(f"orphan             {n_orph}")
    print(f"  unique subtotal  {n_live + n_sup + n_orph}")
    print(f"duplicate copies   {n_dup}")
    print(f"empty files        {n_empty}")
    print(f"TOTAL              {n_live + n_sup + n_orph + n_dup + n_empty}")


if __name__ == "__main__":
    main()
