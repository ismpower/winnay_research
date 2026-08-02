#!/usr/bin/env python3
"""Is the GW150914 derivation actually independent of the observation?"""
import math

hbar = 1.054571817e-34
c = 299792458.0
G = 6.67430e-11
k_B = 1.380649e-23
M_sun = 1.98847e30

print("Test: does kappa_GW = 3/(R_s * T_H) depend on the black hole mass at all?\n")
print(f"{'M (M_sun)':>12} {'R_s (m)':>14} {'T_H (K)':>14} {'kappa':>14}")
for n in [1, 5, 62, 100, 1e6, 1e9]:
    M = n * M_sun
    R_s = 2 * G * M / c**2
    T_H = hbar * c**3 / (8 * math.pi * G * M * k_B)
    print(f"{n:>12g} {R_s:>14.4e} {T_H:>14.4e} {3/(R_s*T_H):>14.4f}")

print("\nAlgebra:")
print("  R_s * T_H = (2GM/c^2) * (hbar c^3 / (8 pi G M k_B))")
print("            = 2 hbar c / (8 pi k_B)")
print("            = hbar c / (4 pi k_B)      <- M cancels exactly")
print("  => kappa_GW = 3 / (hbar c/(4 pi k_B)) = 12 pi k_B/(hbar c)")
print()
print("  l_P * T_P = sqrt(hbar G/c^3) * sqrt(hbar c^5/G)/k_B = hbar c / k_B")
print("  => kappa_Planck = 3 k_B/(hbar c)")
print()
kappa_gw = 12 * math.pi * k_B / (hbar * c)
kappa_pl = 3 * k_B / (hbar * c)
print(f"  kappa_GW closed form     = {kappa_gw:.4f}")
print(f"  kappa_Planck closed form = {kappa_pl:.4f}")
print(f"  exact ratio = 12pi/3 = 4pi = {kappa_gw/kappa_pl:.10f}")
print()
print("CONCLUSION: the two 'independent' derivations are the SAME expression")
print("differing by a factor of exactly 4*pi. The GW150914 calculation contains")
print("no observational information -- the mass cancels identically.")
