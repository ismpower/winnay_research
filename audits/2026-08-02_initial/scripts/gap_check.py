#!/usr/bin/env python3
"""Section 5 gap analysis + modification verification.

(a) Verify the two 'modified' equations numerically.
(b) Find physical constants hiding under unconventional variable names, by
    matching VALUE rather than name -- the blind spot of a keyword sweep.
"""
import json
import math
import os
import re
from collections import defaultdict

SP = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/winnay/Documents/Codex/E3_Engine"

hbar, c, G, kB, Msun = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.380649e-23, 1.98847e30

print("=" * 78)
print("(a) MODIFICATION VERIFICATION")
print("=" * 78)
M = 62 * Msun
r_s = 2 * G * M / c**2
A = 4 * math.pi * r_s**2

S_std = kB * c**3 * A / (4 * G * hbar)
S_mod = (kB * 4 * math.pi * r_s**2) / (hbar * G / c**3)
print("\n'Bekenstein-Hawking entropy equation ... (corrected formula)'")
print("  as written : S = k_B*4*pi*r_s^2 / (hbar*G/c^3)")
print("  standard   : S = k_B*c^3*A/(4*G*hbar),  A = 4*pi*r_s^2")
print(f"  standard   = {S_std:.6e}")
print(f"  as written = {S_mod:.6e}")
print(f"  ratio      = {S_mod/S_std:.4f}   <- the /4 of 'A/4' was dropped")

T_std = hbar * c**3 / (8 * math.pi * G * M * kB)
T_mod = (hbar * c**3) / (8 * math.pi * G * M) * (S_std / kB)
print("\n'T_H_eq = (hbar*c**3)/(8*pi*G*M) * (S_BH/k_B)   # Adjusted scaling'")
print(f"  standard T_H = {T_std:.6e} K")
print(f"  as written   = {T_mod:.6e}")
print(f"  ratio        = {T_mod/T_std:.4e}")
print("  The factor S_BH/k_B is the DIMENSIONLESS entropy (~1e80). Multiplying a")
print("  temperature by it is not a scaling correction; it is a unit-less")
print("  quantity of order 10^80 applied to a physical observable.")

print("\n" + "=" * 78)
print("(b) VALUE-FIRST SWEEP -- constants under unconventional names")
print("=" * 78)

KNOWN = {
    "c (speed of light)": 299792458.0, "G (Newton)": 6.67430e-11,
    "hbar": 1.054571817e-34, "h (Planck)": 6.62607015e-34,
    "k_B (Boltzmann)": 1.380649e-23, "M_sun": 1.98847e30,
    "sigma_SB": 5.670374419e-8, "l_Planck": 1.616255e-35,
    "m_Planck": 2.176434e-8, "T_Planck": 1.416784e32,
    "t_Planck": 5.391247e-44, "m_p": 1.67262192369e-27,
    "m_e": 9.1093837015e-31, "a_rad": 7.565723e-16,
    "R_gas": 8.314462618, "N_A": 6.02214076e23, "e (charge)": 1.602176634e-19,
    "eV": 1.602176634e-19, "pc (parsec)": 3.0856775814913673e16,
    "AU": 1.495978707e11, "L_sun": 3.828e26, "R_sun": 6.957e8,
}
EXPECTED = {  # names already covered by the Phase 2 keyword sweep
    "c", "c_light", "speed_of_light", "clight", "g", "g_const", "gconst",
    "hbar", "h_bar", "h", "h_planck", "planck", "k_b", "kb", "k_boltzmann",
    "boltzmann", "m_sun", "msun", "solar_mass", "m_solar", "sigma", "sigma_sb",
    "stefan_boltzmann", "l_p", "l_planck", "m_planck", "t_p", "t_planck",
    "m_p", "m_e", "kappa", "bruno_constant", "t_h", "t_hawking", "s_bh",
    "r_s", "rs", "schwarzschild_radius", "alpha", "beta", "eta", "gamma",
}
NUM = r"[-+]?(?:\d+\.?\d*(?:[eE][-+]?\d+)?|\.\d+(?:[eE][-+]?\d+)?)"
ASSIGN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\(?\s*(" + NUM + r")\s*\)?\s*(?:#.*)?$")


def lines(path):
    if path.endswith(".ipynb"):
        try:
            nb = json.load(open(path, encoding="utf-8", errors="replace"))
        except Exception:
            return
        for cell in nb.get("cells", []):
            src = cell.get("source", [])
            if isinstance(src, str):
                src = src.splitlines()
            for ln in src:
                yield ln.rstrip("\n")
        return
    try:
        for ln in open(path, encoding="utf-8", errors="replace"):
            yield ln.rstrip("\n")
    except Exception:
        return


hits = defaultdict(lambda: defaultdict(set))
for rel in [l.strip() for l in open(os.path.join(SP, "unique_core.txt")) if l.strip()]:
    p = os.path.join(ROOT, rel[2:])
    for ln in lines(p):
        m = ASSIGN.match(ln)
        if not m:
            continue
        name, val = m.group(1), m.group(2)
        if name.lower() in EXPECTED:
            continue
        try:
            v = float(val)
        except ValueError:
            continue
        if v == 0:
            continue
        for label, ref in KNOWN.items():
            if abs(v - ref) / ref < 5e-4:
                hits[label][name].add(rel)

if not hits:
    print("\n  none found")
for label in sorted(hits):
    print(f"\n  {label}")
    for name in sorted(hits[label], key=lambda n: -len(hits[label][n])):
        fs = hits[label][name]
        print(f"    `{name}`  in {len(fs)} file(s)   e.g. {sorted(fs)[0]}")
