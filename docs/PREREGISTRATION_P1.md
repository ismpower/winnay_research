# Pre-registration P1: lattice-capacity crossing in superconducting aluminium

**Status: REGISTERED, 2026-11-07.** The researcher confirmed R1, R2 and R3 on
2026-11-07. The registration time is the timestamp of the commit tagged
`p1-registered` on branch `claude/dreamy-mccarthy-yhsr5i`. **This file is not
edited after registration.** Corrections go in dated addendum files
(`docs/PREREGISTRATION_P1_ADDENDUM_<n>.md`), which may not change the
hypothesis, the criteria or the falsifiers.

**Blindness statement.** Up to the time this draft was written, no aluminium
heat-capacity dataset other than Phillips (1959) has been searched for, opened
or analysed in this project. Phillips (1959) motivated P1 and is therefore
excluded from testing it.

Code: `e3_core/prediction_p1.py` (tested in `e3_core/tests/test_prediction_p1.py`).
Numbers: `scripts/p1_prediction_table.py` writes `docs/p1_prediction_table.json`.
Framework decisions: `docs/TASK7_OPTIONS.md`, section 6.

---

## 1. Hypothesis

With `sigma_crit = k_B/a^2` (`a = n^(-1/3)`) and active entropy `S_act`
(TASK7_OPTIONS 6.2), E3 asserts that `eta_S = 1` marks a physical change of
state. In a zero-field bulk aluminium superconductor, `eta_S = 1` occurs where
the active entropy per atom equals the threshold

```text
s_th = a * (A/V)                 (equals 3a/R for a sphere)
```

**Registered claim P1.** Below the crossing temperature `T*` defined by
`S_act(T*)/(N k_B) = f * s_th`, the measured heat capacity exceeds the no-E3
baseline. `f` is the unknown O(1) prefactor of `sigma_crit`.

- **[confirmed R1, 2026-11-07]** The sign is an **excess** of heat capacity below `T*`, as in
  the anomaly that motivated P1. E3 has not yet derived this sign; registering
  it is a researcher choice.

## 2. Data selection (point 1)

Data are chosen by these criteria, fixed now, not by naming datasets.

**Inclusion (all required):**

1. Elemental aluminium, nominal purity of at least 99.99%.
2. Bulk sample: every dimension at least 10 um.
3. Superconducting-state heat capacity measured in zero applied field, with
   residual or trapped field at most 1 mT, stated or bounded by the authors.
   (Reason: at 30 mT nuclear Zeeman entropy becomes comparable to `s_th`; see
   section 5.)
4. Numerical point values (a table or a data file), not values read off a plot,
   with stated relative uncertainty per point or per temperature range.
5. Addenda (sample holder, thermometer, heater) subtracted and the correction
   stated.
6. Sample geometry reported well enough to compute `A/V` within 20%.
7. Normal-state `gamma`, `Tc` and Debye temperature reported by the same study,
   or measured on the same sample.
8. Temperature window covering `[0.8 T*(0.25), 1.1 T*(4)]` for that sample's
   own predicted band (section 3).

**Exclusion:**

- Phillips (1959) and any dataset already viewed by the researcher before
  registration (to be declared in the addendum).
- Thin films and nanostructures (excluded by inclusion criterion 2).
- Measurements with exchange gas present at the measured temperatures (surface
  adsorption confound, section 4).

**Procedure:**

- Candidate studies are screened only on their methods sections: sample,
  purity, geometry, field, window and uncertainties. Their heat-capacity results
  are not viewed during screening.
- The list of qualifying datasets is committed as
  `docs/PREREGISTRATION_P1_ADDENDUM_1.md` before any of them is analysed.
- **Every qualifying dataset is analysed. None may be dropped after its
  results are seen.**

## 3. Prediction and observable (point 2)

**Baseline (no E3).** `C_base(T) = C_BCS(T; gamma, Tc) + (12 pi^4/5) R (T/Theta_D)^3`,
using weak-coupling BCS (`e3_core.bcs`) with each sample's own `gamma`, `Tc` and
`Theta_D`.

**Observable: departure temperature `T_dep`** (`prediction_p1.departure_temperature`).
Sort the points by temperature. A point is in excess if
`(C - C_base)/C_base > 3 u`, where `u` is its stated relative uncertainty.
`T_dep` is the highest measured temperature such that it and every point below
it are in excess, with at least two such points. The true onset lies in the
bracket `[T_dep, T_next]`, where `T_next` is the next measured point above.

**Single-sample prediction.** `T_dep` bracket overlaps the band
`[T*(0.25), T*(4)]`, computed from that sample's own `a`, `A/V`, `gamma`, `Tc`
and `Theta_D`.

Illustrative bands (Phillips parameters, varying only the size):

| A/V relative to Phillips sphere | Equivalent sphere radius | T*(0.25) | T*(1) | T*(4) |
|---|---|---|---|---|
| 0.1 | 0.266 m | 0.090 K | 0.137 K | 0.171 K |
| 1 | 2.66 cm | 0.161 K | 0.191 K | 0.225 K |
| 10 | 2.66 mm | 0.213 K | 0.253 K | 0.309 K |
| 100 | 0.266 mm | 0.288 K | 0.361 K | 0.481 K |
| 1000 | 26.6 um | 0.433 K | 0.608 K | 0.955 K |

**Two-sample prediction (prefactor-free).** For two qualifying samples whose
`A/V` differ by a factor of at least 4, the unknown `f` cancels:
`S_act,1(T1)/s_th,1 = S_act,2(T2)/s_th,2`. Given sample 1's bracket, the
predicted bracket for sample 2 is `partner_crossing_temperature` applied to each
end. Example: a Phillips-size sample departing at 0.1914 K implies 0.2254 K for a
sample with 4 times the `A/V`.

- **[confirmed R3, 2026-11-07]** Significance threshold `3 u`, and the prefactor band
  `f` from 0.25 to 4.

## 4. Falsification and support criteria (point 3)

P1 is **falsified** by any of:

- **F1 (absent).** A qualifying dataset, with `u <= 0.2` at every point below
  `T*(0.25)`, shows no departure (`T_dep` undefined) down to `0.8 T*(0.25)`.
- **F2 (misplaced).** The `T_dep` bracket of a qualifying dataset lies entirely
  outside `[T*(0.25), T*(4)]`.
- **F3 (no size scaling).** For a qualifying pair with an `A/V` ratio of at least
  4, sample 2's bracket does not overlap the bracket predicted from sample 1.
- **F4 (surface explanation).** The excess heat capacity per unit surface area,
  `(C - C_base) * (V/A)`, plotted against T coincides within uncertainties
  across samples of different `A/V`. A surface-localised contribution (oxide,
  adsorbed films) predicts exactly that collapse, and it would explain the size
  scaling without E3.

- **[confirmed R2, 2026-11-07]** F1 assumes that the E3 excess, if real, is large enough to be
  seen at `3 u <= 0.6`, i.e. at least about 60% of the baseline. E3 does not
  predict the size of the effect. Without this assumption an absent excess
  cannot falsify P1. A smaller assumed size requires smaller `u` in inclusion
  criterion 4.

P1 is **supported, not proven,** if every qualifying dataset satisfies the
single-sample prediction, at least one pair satisfies the two-sample prediction,
and F4 does not hold. Standard explanations (impurity contributions, trapped
normal regions, strong-coupling corrections to the baseline) must then still be
examined before any stronger claim.

## 5. Caveats resolved or bounded (point 4)

| Caveat | Status |
|---|---|
| Nuclear-spin entropy treated as frozen | **Bounded by calculation.** Al-27 has `I = 5/2` and `mu = +3.6415069 mu_N` (KAERI, LBL nuclear moments table), with `mu_N = e hbar/(2 m_p)` computed from the reference constants. The dipolar field estimate `mu_0 mu/(4 pi a^3)` is 0.11 mT. At 0.1 K the nuclear active entropy (C/2 in the high-temperature regime) is below 1e-4 of `s_th` at 0.11 mT and below 2e-3 at 1 mT, and it shifts `T*` by less than 0.1% (tested). At 30 mT it becomes comparable to `s_th`, hence inclusion criterion 3. **Not bounded:** nuclear quadrupole splitting at impurities or strained sites (zero by symmetry in a perfect cubic lattice). |
| Prefactor of `sigma_crit` | Not derived. Covered by the registered band `f` = 0.25-4 (real Al crystal faces give 0.79-0.92). Cancels exactly in the two-sample test F3. |
| Low-temperature model below the window | Each sample's own weak-coupling BCS + Debye baseline. Inclusion criterion 8 ensures that the window reaches below the band. |
| Post-hoc origin | Phillips (1959) is excluded. Only new, blindly selected data count. |
| Surface confound | Exchange-gas exclusion plus falsifier F4. |
| How x, y and z combine away from the black-hole point | Not needed for P1; remains open (plan task 7). |

## 6. Frozen inputs (SHA-256 at registration)

The analysis of qualifying data must use these exact files. If any hash
differs, the difference must be explained in an addendum before results are
reported.

| File | SHA-256 |
|---|---|
| `e3_core/prediction_p1.py` | `5d1d68fa152471f7eb1ed2bb9a3724ad461f5d5ef4c26b7534b723feba9651d5` |
| `e3_core/bcs.py` | `fb3778260c9b61212f2a6f905e5c142378b5b69a4795c981b1010e584f92ec93` |
| `e3_core/constants.py` | `be9de8f89b9c6b0d2c377c20b959826aee45fad2c3f8807c8dba1a3019659798` |
| `e3_core/scales.py` | `e25a96c8bfb8ae16359ab0dd97b935b5db9590b180c4aa97d029bbfcd852fc1f` |
| `e3_core/geometry.py` | `4683d9962bcd41218c45f17a4383b3d534f532b810738738d8770643f836d235` |
| `e3_core/tests/test_prediction_p1.py` | `eac9c15d05dc8e61c9b1df8e764faa08d0551f24f671e041d583aba9583b49c5` |
| `scripts/p1_prediction_table.py` | `6b74072555664bf14beb0b09b7c5b3aa081aff46a5d8bf19eac72572e0a6fc9c` |
| `docs/p1_prediction_table.json` | `039a30339d1c2b8c371c001314a7c007c09d8984f0b31f769371ad085d3aee91` |
| `docs/task7_candidate_scales.json` | `aff8e0b2fdb47cdf49146b7d438c2e1da1236e5df93ff6996f99f7b32ee9ead3` |

Check with `sha256sum <file>`. At registration all 80 tests in `e3_core/tests`
passed, and `scripts/p1_prediction_table.py` reproduced its JSON byte for byte.

## 7. Next steps after registration

1. Screen candidate studies on their methods sections only (section 2,
   Procedure) and commit `docs/PREREGISTRATION_P1_ADDENDUM_1.md` listing the
   qualifying datasets and declaring any dataset the researcher has already
   seen.
2. Only then extract the data and compute `T_dep` with the frozen code.

