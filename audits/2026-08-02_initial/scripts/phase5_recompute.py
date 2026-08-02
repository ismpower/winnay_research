#!/usr/bin/env python3
"""Phase 5 — independent recomputation of every disputed constant.

Each block states the formula explicitly, computes from first principles,
then reports which repo value(s) match. No comment or docstring claim is
taken on trust.
"""
import math

# ---------------------------------------------------------------- references
# 2019 SI: exact by definition (not measurable, not recomputable).
c_SI    = 299792458.0            # m/s      exact
h_SI    = 6.62607015e-34         # J*s      exact
kB_SI   = 1.380649e-23           # J/K      exact
# Measured:
G_CODATA  = 6.67430e-11          # m^3/kg/s^2  CODATA 2018, u_r = 2.2e-5
Msun_IAU  = 1.98847e30           # kg          IAU nominal
mp_CODATA = 1.67262192369e-27    # kg          CODATA 2018
me_CODATA = 9.1093837015e-31     # kg          CODATA 2018

hbar = h_SI / (2 * math.pi)
G, kB, c, Msun = G_CODATA, kB_SI, c_SI, Msun_IAU

W = 78
def head(t):
    print("\n" + "=" * W + f"\n{t}\n" + "=" * W)

def verdict(name, computed, candidates, unit=""):
    """candidates: list of (repo_value, where)."""
    print(f"  independent result : {computed:.10g} {unit}")
    print(f"  {'repo value':>22} {'rel. error':>14}   verdict")
    for val, where in candidates:
        rel = (val - computed) / computed if computed else float("nan")
        if abs(rel) < 1e-9:      v = "EXACT MATCH"
        elif abs(rel) < 1e-4:    v = "match (rounding)"
        elif abs(rel) < 1e-2:    v = "LOW PRECISION"
        else:                    v = "*** MISMATCH ***"
        print(f"  {val:>22.10g} {rel:>+13.4%}   {v}   [{where}]")

# ---------------------------------------------------------------------------
head("CATEGORY A — SI-defined exact. Not recomputable; checked vs definition.")
print("""  Since the 2019 SI redefinition, c, h and k_B are fixed numerical
  values that DEFINE the metre, kilogram and kelvin. There is no
  experiment or formula that yields them; a 'disagreement' here is
  simply a rounded transcription.""")

print("\n-- c  (defined exactly as 299 792 458 m/s)")
verdict("c", c_SI, [(299792458.0, "57 files"), (3.0e8, "40 files"),
                    (2.99792458e8, "6 files")], "m/s")

print("\n-- k_B  (defined exactly as 1.380649e-23 J/K)")
verdict("k_B", kB_SI, [(1.380649e-23, "79 files"), (1.381e-23, "1 file")], "J/K")

print("\n-- hbar = h/(2*pi), h defined exactly")
verdict("hbar", hbar, [(1.054571817e-34, "45 files"),
                       (1.0545718e-34, "10 files")], "J*s")

# ---------------------------------------------------------------------------
head("CATEGORY B — measured. Checked against CODATA 2018 / IAU.")
print("\n-- G  (CODATA 2018: 6.67430(15)e-11, rel. unc. 2.2e-5)")
verdict("G", G_CODATA, [(6.67430e-11, "87 files"), (6.67e-11, "1 file")], "m^3/kg/s^2")

print("\n-- M_sun  (IAU nominal 1.98847e30 kg)")
verdict("M_sun", Msun_IAU, [(1.98847e30, "18 files"), (1.9885e30, "3 files"),
                            (1.989e30, "6 files")], "kg")

print("\n-- m_p  (CODATA 2018)")
verdict("m_p", mp_CODATA, [(1.67262192369e-27, "1 file"),
                           (1.6726219e-27, "2 files")], "kg")

# ---------------------------------------------------------------------------
head("CATEGORY C — derived. Recomputed from formula.")

print("\n-- Planck length:   l_P = sqrt(hbar*G/c^3)")
l_P = math.sqrt(hbar * G / c**3)
verdict("l_P", l_P, [(1.616255e-35, "36 files")], "m")

print("\n-- Planck mass:     m_P = sqrt(hbar*c/G)")
m_P = math.sqrt(hbar * c / G)
verdict("m_P", m_P, [(2.17651e-8, "15 files")], "kg")

print("\n-- Planck temperature: T_P = sqrt(hbar*c^5/G)/k_B")
T_P = math.sqrt(hbar * c**5 / G) / kB
verdict("T_P", T_P, [(1.416808e32, "7 files, named t_planck")], "K")

print("\n-- Planck TIME (what the name 't_planck' should hold):")
print("     t_P = sqrt(hbar*G/c^5)")
t_P = math.sqrt(hbar * G / c**5)
print(f"  independent result : {t_P:.10g} s")
print(f"  value stored under that name : 1.416808e+32")
print(f"  ratio = {1.416808e32/t_P:.4g}  -> the variable holds a TEMPERATURE,")
print(f"  not a time. Misuse as a time is wrong by ~76 orders of magnitude.")

# ---------------------------------------------------------------------------
head("CATEGORY D — the GW150914 chain.")
M = 62 * Msun

print("\n-- Schwarzschild radius:  R_s = 2*G*M/c^2   (M = 62 M_sun)")
R_s = 2 * G * M / c**2
verdict("R_s", R_s, [(183000.0, "Bruno Constant Note.txt")], "m")

print("\n-- Hawking temperature:   T_H = hbar*c^3/(8*pi*G*M*k_B)")
T_H = hbar * c**3 / (8 * math.pi * G * M * kB)
verdict("T_H", T_H, [(1.2e-8, "Bruno Constant Note.txt / FINAL_ANALYSIS")], "K")
print(f"  -> implied mass for T_H = 1.2e-8 K : "
      f"{hbar*c**3/(8*math.pi*G*1.2e-8*kB)/Msun:.2f} M_sun (not 62)")

print("\n-- Bekenstein-Hawking entropy: S = k_B*c^3*A/(4*G*hbar),  A = 16*pi*(GM/c^2)^2")
A = 16 * math.pi * (G * M / c**2)**2
S_BH = kB * c**3 * A / (4 * G * hbar)
S_repo_formula = (4 * math.pi * G * A) / (hbar * c * kB)   # as coded in repo
verdict("S_BH", S_BH, [(7.009474410896821e54, "Entropy Collapse Test 1.8/1.9/2.1"),
                       (S_repo_formula, "as coded in Gw150914 Entropy Test.py")], "J/K")
M_implied = math.sqrt(7.009474410896821e54 * hbar * c / (4 * math.pi * G * kB))
print(f"  -> mass implied by S = 7.0095e54 (via S = 4*pi*G*M^2*k_B/(hbar*c)) : "
      f"{M_implied/Msun:.3f} M_sun")

# ---------------------------------------------------------------------------
head("CATEGORY E — kappa, all five values.")
print("""  Formula asserted by the framework:  beta_B = A/V = 3/R = kappa * T
  Two derivations appear in the corpus.""")

print("\n-- Planck route:  kappa = 3/(l_P * T_P)   [reduces to 3*k_B/(hbar*c)]")
k_planck = 3 / (l_P * T_P)
verdict("kappa", k_planck, [(1313.0, "19 files"), (1366.0, "22 files")], "K^-1")

print("\n-- GW route:      kappa = 3/(R_s * T_H)   [reduces to 12*pi*k_B/(hbar*c)]")
k_gw = 3 / (R_s * T_H)
verdict("kappa", k_gw, [(1366.0, "22 files"), (1313.0, "19 files")], "K^-1")
print(f"  NOTE: R_s*T_H = hbar*c/(4*pi*k_B) -- mass cancels. Ratio to Planck")
print(f"  route = {k_gw/k_planck:.10f} = 4*pi exactly. Not an independent check.")

print("\n-- kappa = 0.001005  ('Chajar Constant', tangency threshold)")
print("     Used as: T_tangent = T_planck * 0.001005  -> DIMENSIONLESS multiplier.")
print("     Not a K^-1 quantity. No formula in corpus derives it.")
print(f"     T_planck * 0.001005 = {T_P*0.001005:.6g} K")
print("     VERDICT: different physical quantity sharing the name. Not comparable.")

print("\n-- kappa = 1340e-6 K^-1 s^-1  ('laboratory', BRUNO_CONSTANT_KAPPA)")
print("     Units carry s^-1, inconsistent with beta_B = kappa*T.")
print("     No derivation or experimental method anywhere in corpus.")
print("     VERDICT: NOT RECOMPUTABLE -- no formula given. Unverifiable.")

print("\n-- kappa = 1.23456789e-23  (engine / parser trees, 32 files)")
print("     Digit sequence 1-2-3-4-5-6-7-8-9. No formula, no units.")
print("     VERDICT: PLACEHOLDER. Not a physical value.")

print("\n-- f_S = 1.66345592659651e-36  ('previously computed entropy contribution')")
print("     Added to T_H and to r_s in two scripts. No derivation in corpus.")
print("     VERDICT: NOT RECOMPUTABLE -- provenance absent.")

# ---------------------------------------------------------------------------
head("CATEGORY F — dimensional consistency of the governing equation.")
print("""  beta_B = A/V = 3/R = kappa*T
    [3/R]     = m^-1
    [kappa*T] = K^-1 * K = dimensionless
  m^-1 != dimensionless  ->  the equation cannot balance.""")
print(f"  Consequence: kappa's value tracks the length unit.")
for unit, scale in [("metre", 1.0), ("kilometre", 1e3), ("centimetre", 1e-2)]:
    print(f"    R in {unit:<10s}: kappa = {3/((R_s/scale)*T_H):>14.4f} K^-1")
print("  No unit choice is privileged by the framework, so no value is determinate.")
