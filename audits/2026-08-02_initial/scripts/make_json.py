#!/usr/bin/env python3
"""Convert audit TSV/text artifacts into structured JSON."""
import json
import os
from collections import defaultdict

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW, DATA = os.path.join(D, "raw"), os.path.join(D, "data")
os.makedirs(DATA, exist_ok=True)
EMPTY = "d41d8cd98f00b204e9800998ecf8427e"


def tsv(name):
    p = os.path.join(RAW, name)
    with open(p, encoding="utf-8", errors="replace") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        return [dict(zip(hdr, ln.rstrip("\n").split("\t"))) for ln in fh if ln.strip()]


def dump(name, obj):
    p = os.path.join(DATA, name)
    with open(p, "w") as fh:
        json.dump(obj, fh, indent=2)
    print(f"  {name:34s} {os.path.getsize(p):>9,} bytes")


print("writing JSON:")
dump("constants_inventory.json", tsv("constants_inventory.tsv"))
dump("equations_inventory.json", tsv("equations_inventory.tsv"))
dump("kappa_hits.json", tsv("kappa_hits.tsv"))

# ---- file classification -------------------------------------------------
def lines(n):
    p = os.path.join(RAW, n)
    return [l.strip() for l in open(p)] if os.path.exists(p) else []

dup = []
for ln in lines("cls_duplicate.tsv"):
    if "\t" in ln:
        a, b = ln.split("\t", 1)
        dup.append({"duplicate": a, "canonical_copy": b})

dump("file_classification.json", {
    "canonical": lines("cls_canonical.txt"),
    "superseded": lines("cls_superseded.txt"),
    "orphan": lines("cls_orphan.txt"),
    "duplicate": dup,
})

# ---- duplicate groups ----------------------------------------------------
groups = defaultdict(list)
for ln in open(os.path.join(RAW, "core_hashes.txt")):
    h, _, p = ln.rstrip("\n").partition("  ")
    groups[h].append(p)

nocr = defaultdict(list)
for ln in open(os.path.join(RAW, "core_hashes_nocr.txt")):
    h, _, p = ln.rstrip("\n").partition("  ")
    nocr[h].append(p)

dump("duplicate_groups.json", {
    "note": "md5 -> every path with that exact content. The all-zero-length "
            "group is the 173 empty files.",
    "empty_file_hash": EMPTY,
    "groups": {h: sorted(ps) for h, ps in sorted(groups.items(),
                                                 key=lambda kv: -len(kv[1]))},
})

# ---- corpus manifest -----------------------------------------------------
dump("manifest.json", {
    "corpus_root": "/home/winnay/Documents/Codex/E3_Engine",
    "audited": "2026-08-02",
    "size_bytes_approx": 41 * 1024**3,
    "totals": {"files": 308033, "directories": 18575},
    "extensions_top": {"json": 117604, "dat": 45156, "pyc": 44129, "py": 43790,
                       "h": 27701, "pyi": 3186, "csv": 2044, "ipynb": 368,
                       "md": 299, "tex": 266},
    "excluded_as_noise": {
        "E3_DAVP_Pipeline/davp_env": {"py": 29117, "pyc": 29115, "h": 18474},
        "Bruno_Entropy_Project/bruno_env": {"py": 13039, "pyc": 14422, "h": 9213},
        "Bruno_Entropy_Project/datasets": {"json": 94443},
        "git_dirs": 16, "zero_byte_files": 441},
    "third_party_share_of_py": "42156 / 43790 = 96%",
    "authored_core_files": {"total": 2408, "py": 1631, "ipynb": 263,
                            "md": 251, "tex": 138},
    "unique_contents": {"exact_bytes": len(groups),
                        "ignoring_line_endings": len(nocr),
                        "crlf_lf_twins": len(groups) - len(nocr)},
    "classification": {"canonical": 145, "superseded": 69, "orphan": 399,
                       "duplicate": 1622, "empty": 173},
    "version_named_directories": 124,
})
print("done")
