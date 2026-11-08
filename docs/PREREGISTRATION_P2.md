# Pre-registration P2: lattice-capacity crossing in insulating single crystals

**Status: DRAFT, not registered.** It becomes registered when the researcher
confirms the items marked **[confirm]** and the confirming commit is pushed. That
commit's timestamp is the registration time. After registration this file is
never edited. Corrections go in dated addenda.

**Blindness statement.**

- No dataset has been searched for, opened or analysed for P2.
- The assistant that drafted P2 holds a general prior from its training: that
  high-quality crystalline insulators follow the Debye T^3 law closely at low
  temperature. This prior is stated here so that it cannot be mistaken for a
  test, and so that P2's criteria are not shaped around it.
- The researcher declares previously seen data in addendum 1.

Code: `e3_core/prediction_p2.py` (tested in `e3_core/tests/test_prediction_p2.py`).
Numbers: `scripts/p2_prediction_table.py` writes `docs/p2_prediction_table.json`
(illustrative inputs only). Framework: `docs/TASK7_OPTIONS.md` section 6, as used
by the registered P1.

---

## 1. Hypothesis

P2 applies the same framework as P1: `sigma_crit = k_B/a^2` with `a = n^(-1/3)`
(all atoms counted), and active entropy `S_act` (TASK7_OPTIONS 6.2). In an
electrically insulating crystal at `T < Theta_D/50`, the active entropy is the
phonon entropy, `S_act/(N k_B) = (4 pi^4/5)(T/Theta_D)^3`. So `eta_S = 1` at

```text
T* = Theta_D * (5 f a (A/V) / (4 pi^4))^(1/3)
```

with no superconductivity model involved. `f` is the unknown prefactor; through
the cube root, f = 0.25 to 4 changes `T*` only by factors of 0.63 to 1.59.

**Registered claim P2.** Below `T*`, the measured heat capacity exceeds the
Debye baseline `C = A T^3`.

- **[confirm R1-P2]** The sign is an **excess** below `T*`, the same as P1.
- **[confirm R4-P2] Scope commitment.** Phonon entropy is part of `S_act` in
  the registered P1 as well (about 32% at the aluminium crossing). P2 therefore
  tests the same framework, not a new one. **A falsification of P2 counts
  against the lattice-capacity framework as registered.** It cannot be escaped
  afterwards by declaring phonons inactive, because that would also change P1's
  frozen prediction.

## 2. Data selection

**Inclusion (all required):**

1. Electrically insulating **single crystal** (no glasses, no polycrystals:
   grain boundaries are internal surfaces whose role in `A` is undecided), with
   no free-carrier term at the measured temperatures (intrinsic, or doping
   stated low enough for carrier freeze-out).
2. **Nuclear rule:** no nuclide with natural abundance of at least 1% and spin
   `I >= 1` on a lattice site of non-cubic symmetry. (Reason: its quadrupole
   heat capacity can rival the phonon term. Si, Ge, diamond, TeO2 and CaWO4
   pass; sapphire, through Al-27, does not.)
3. No intentional paramagnetic dopant; applied field at most 1 mT.
4. Every dimension at least 0.1 mm; sample geometry reported well enough to give
   `A/V` within 20%.
5. Numerical point values (a table or a data file), with stated relative
   uncertainty per point or per range.
6. Addenda subtracted and the correction stated.
7. **Baseline coefficient from an independent source**, either:
   (a) `Theta_D` from sound velocities or elastic constants
   (`debye_temperature_from_sound_velocities`); or
   (b) a fit of `C/T^3 = A + B T^2` to the same dataset **only** within the
   registered window `[1.5 T*(4), Theta_D/50]` (`registered_fit_window`), using
   `fit_low_temperature_coefficients`.
   Never a fit that includes the predicted band.
8. Temperature window covering `[0.8 T*(0.25), 1.1 T*(4)]`, plus the fit window
   if option (b) is used.
9. No exchange gas at the measured temperatures.

**Exclusion:** any dataset the researcher has already seen (declared in
addendum 1).

**Procedure:** as in P1. Studies are screened on their methods only
(`docs/P1_SEARCH_BRIEF.md` applies, extended to detector-crystal calorimetry).
The qualifying list is committed as an addendum before analysis, and every
qualifying dataset is analysed.

## 3. Prediction and observable

**Baseline (no E3):** `C_base = A T^3`, with `A` from inclusion criterion 7.

**Observable:** the departure temperature `T_dep`, using the same rule and code
as P1 (`prediction_p1.departure_temperature`): the highest measured temperature
such that it and every point below it exceed the baseline by more than `3u`. The
bracket is `[T_dep, T_next]`.

**Single-sample prediction:** the `T_dep` bracket overlaps
`[T*(0.25), T*(4)]`, computed from that crystal's own `a`, `A/V` and `Theta_D`.

Illustrative scale (approximate handbook inputs; cubes):

| Crystal | 1 mm | 1 cm | 5 cm |
|---|---|---|---|
| Si | 1.12-2.82 K | 0.52-1.31 K | 0.30-0.77 K |
| Ge | 0.66-1.66 K | 0.31-0.77 K | 0.18-0.45 K |
| diamond | 3.36-8.48 K | 1.56-3.94 K | 0.91-2.30 K |
| TeO2 | 0.39-0.97 K | 0.18-0.45 K | 0.11-0.26 K |

**Two-sample prediction (prefactor-free):** for two qualifying crystals of the
same material whose `A/V` differ by a factor of at least 8,
`T2 = Theta2 (T1/Theta1)(s_th2/s_th1)^(1/3)` (`partner_crossing_temperature`),
whatever `f` is. (The ratio is 8 rather than 4 because the cube root halves the
shift.)

- **[confirm R3-P2]** Significance threshold `3u`, prefactor band 0.25-4, pair
  ratio at least 8.

## 4. Falsification and support

P2 is **falsified** by any of:

- **F1 (absent).** A qualifying dataset with `u <= 0.2` at every point below
  `T*(0.25)` shows no departure down to `0.8 T*(0.25)`.
- **F2 (misplaced).** A `T_dep` bracket lies entirely outside `[T*(0.25), T*(4)]`.
- **F3 (no size scaling).** For a qualifying pair, sample 2's bracket does not
  overlap the bracket predicted from sample 1.
- **F4 (surface explanation).** The excess per unit area, `(C - C_base)(V/A)`,
  coincides within uncertainties across crystals of different `A/V`.

- **[confirm R2-P2]** F1 assumes the E3 excess, if real, is at least about 60% of
  the baseline (seen at `3u <= 0.6`), the same assumption as P1.

**Supported, not proven,** if every qualifying dataset meets the single-sample
prediction, at least one pair meets the two-sample prediction, and F4 does not
hold. Defect two-level systems and residual impurities must then still be
examined.

## 5. Caveats

| Caveat | Treatment |
|---|---|
| Debye `T^3` validity | Used only below `Theta_D/50` (code-enforced); dispersion handled by the `B T^2` term in the fit window |
| Baseline circularity | Criterion 7: `Theta_D` independent of the predicted band |
| Nuclear quadrupole heat capacity | Nuclear rule (criterion 2) |
| Defect two-level systems | Single crystals only; examined before any support claim |
| Grain boundaries as surfaces | Excluded (single crystals) |
| Assistant's prior | Declared in the blindness statement |
