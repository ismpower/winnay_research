#!/usr/bin/env python3
"""Phase 3 verification: recompute both kappa derivations from CODATA 2018."""
import math

hbar = 1.054571817e-34
c = 299792458.0
G = 6.67430e-11
k_B = 1.380649e-23
M_sun = 1.98847e30

print("== Planck-unit derivation (claimed kappa = 1313) ==")
l_P = math.sqrt(hbar * G / c**3)
T_P = math.sqrt(hbar * c**5 / G) / k_B
kappa_planck = 3 / (l_P * T_P)
print(f"  l_P            = {l_P:.6e} m")
print(f"  T_P            = {T_P:.6e} K")
print(f"  kappa = 3/(l_P*T_P) = {kappa_planck:.2f} K^-1   (claimed 1313)")
print(f"  relative error vs 1313 = {(kappa_planck-1313)/1313*100:+.2f}%")

print("\n== GW150914 derivation (claimed kappa = 1366) ==")
M = 62 * M_sun
R_s = 2 * G * M / c**2
T_H = hbar * c**3 / (8 * math.pi * G * M * k_B)
print(f"  M              = 62 M_sun = {M:.4e} kg")
print(f"  R_s (computed) = {R_s:.0f} m        (claimed 183000 m)")
print(f"  T_H (computed) = {T_H:.4e} K     (claimed 1.2e-8 K)")
print(f"  T_H ratio claimed/correct = {1.2e-8/T_H:.2f}x")
print(f"  4*pi = {4*math.pi:.3f}  (for comparison)")

kappa_claimed = 3 / (183000 * 1.2e-8)
kappa_correct = 3 / (R_s * T_H)
print(f"  kappa using CLAIMED T_H  = {kappa_claimed:.1f} K^-1   <- origin of 1366")
print(f"  kappa using CORRECT T_H  = {kappa_correct:.1f} K^-1")
print(f"  inflation factor = {kappa_correct/kappa_claimed:.2f}x")

print("\n== What mass would actually give T_H = 1.2e-8 K? ==")
M_implied = hbar * c**3 / (8 * math.pi * G * 1.2e-8 * k_B)
print(f"  M_implied      = {M_implied/M_sun:.2f} M_sun  (vs the 62 M_sun used for R)")

print("\n== Consistency of the two derivations ==")
print(f"  Planck route : {kappa_planck:.1f} K^-1")
print(f"  GW route (corrected): {kappa_correct:.1f} K^-1")
print(f"  ratio = {kappa_correct/kappa_planck:.2f}x  -> agreement? "
      f"{'YES' if abs(kappa_correct/kappa_planck - 1) < 0.05 else 'NO'}")

print("\n== Dimensional check of beta_B = A/V = 3/R ==")
print("  [3/R] = 1/length ; [kappa*T] = K^-1 * K = dimensionless")
print("  -> 1/length != dimensionless : equation is dimensionally INCONSISTENT")
print("  kappa's fitted value therefore depends on the length unit chosen (m vs km vs ...)")
R_km = R_s / 1000.0
print(f"  e.g. using km instead of m: kappa = {3/(R_km*T_H):.1f} K^-1 "
      f"({3/(R_km*T_H)/kappa_correct:.0f}x different)")
