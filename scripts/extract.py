#!/usr/bin/env python3
"""Phase 2: mechanical constant/equation extraction over the unique-file working set.

Reads only the deduplicated file list. Emits TSVs; prints nothing but counts.
"""
import json
import os
import re
import sys

SP = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/winnay/Documents/Codex/E3_Engine"

# Symbols we care about, normalized to a canonical name.
SYMBOL_ALIASES = {
    "g": "G", "g_const": "G", "gconst": "G", "grav": "G", "g_newton": "G",
    "c": "c", "c_light": "c", "speed_of_light": "c", "clight": "c",
    "hbar": "hbar", "h_bar": "hbar", "hbar_const": "hbar",
    "h": "h", "h_planck": "h", "planck": "h",
    "k_b": "k_B", "kb": "k_B", "k_boltzmann": "k_B", "boltzmann": "k_B",
    "m_sun": "M_sun", "msun": "M_sun", "solar_mass": "M_sun", "m_solar": "M_sun",
    "sigma": "sigma_SB", "sigma_sb": "sigma_SB", "stefan_boltzmann": "sigma_SB",
    "kappa": "kappa", "kappa_b": "kappa", "k_bruno": "kappa",
    "bruno_constant": "kappa", "bruno_const": "kappa", "brunoconstant": "kappa",
    "bruno": "kappa", "kappa_bruno": "kappa", "b_const": "kappa",
    "t_h": "T_H", "t_hawking": "T_H", "temp_hawking": "T_H", "t_hawk": "T_H",
    "s_bh": "S_BH", "s_hawking": "S_BH", "entropy_bh": "S_BH",
    "alpha": "alpha", "beta": "beta", "eta": "eta", "gamma": "gamma",
    "m_p": "m_p", "m_e": "m_e", "l_p": "l_planck", "l_planck": "l_planck",
    "t_p": "t_planck", "t_planck": "t_planck", "m_planck": "m_planck",
    "r_s": "r_s", "schwarzschild_radius": "r_s", "rs": "r_s",
}

NUM = r"[-+]?(?:\d+\.?\d*(?:[eE][-+]?\d+)?|\.\d+(?:[eE][-+]?\d+)?)"
ASSIGN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*([^=].*?)\s*(?:#.*)?$")
DICTENT = re.compile(r"""["']([A-Za-z_][A-Za-z0-9_]*)["']\s*:\s*(""" + NUM + r")\b")
PURE_NUM = re.compile(r"^\(?\s*(" + NUM + r")\s*\)?$")
KAPPA_LIT = re.compile(r"\b(1313(?:\.\d+)?|1366(?:\.\d+)?)\b")


def canon(name):
    return SYMBOL_ALIASES.get(name.lower())


def iter_lines(path):
    """Yield (lineno, text). Notebooks are flattened to their source cells."""
    if path.endswith(".ipynb"):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                nb = json.load(fh)
        except Exception:
            return
        n = 0
        for cell in nb.get("cells", []):
            src = cell.get("source", [])
            if isinstance(src, str):
                src = src.splitlines(True)
            for line in src:
                n += 1
                yield n, line.rstrip("\n")
        return
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for n, line in enumerate(fh, 1):
                yield n, line.rstrip("\n")
    except Exception:
        return


def main():
    with open(os.path.join(SP, "unique_core.txt")) as fh:
        files = [ln.strip() for ln in fh if ln.strip()]

    consts = []   # file, line, symbol, literal, expr
    equations = []  # file, line, symbol, rhs
    kappa_hits = []  # file, line, literal, context

    for rel in files:
        path = os.path.join(ROOT, rel[2:] if rel.startswith("./") else rel)
        for n, line in iter_lines(path):
            if len(line) > 600:
                continue
            for m in KAPPA_LIT.finditer(line):
                kappa_hits.append((rel, n, m.group(1), line.strip()[:220]))

            m = ASSIGN.match(line)
            if m:
                name, rhs = m.group(1), m.group(2).strip()
                sym = canon(name)
                pn = PURE_NUM.match(rhs)
                if pn:
                    if sym or re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
                        consts.append((rel, n, sym or name, pn.group(1), rhs[:200]))
                elif sym and rhs:
                    equations.append((rel, n, sym, rhs[:300]))

            for dm in DICTENT.finditer(line):
                sym = canon(dm.group(1))
                if sym:
                    consts.append((rel, n, sym, dm.group(2), line.strip()[:200]))

    def dump(name, rows, header):
        with open(os.path.join(SP, name), "w") as fh:
            fh.write("\t".join(header) + "\n")
            for r in rows:
                fh.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")
        return len(rows)

    a = dump("constants_inventory.tsv", consts,
             ["file", "line", "symbol", "literal", "expr"])
    b = dump("equations_inventory.tsv", equations,
             ["file", "line", "symbol", "rhs"])
    c = dump("kappa_hits.tsv", kappa_hits,
             ["file", "line", "literal", "context"])
    print(f"files_scanned\t{len(files)}")
    print(f"constants_rows\t{a}")
    print(f"equations_rows\t{b}")
    print(f"kappa_hit_rows\t{c}")


if __name__ == "__main__":
    main()
