# P1 measurement design: three aluminium samples differing only in A/V

**Status:** design proposal, 2026-11-08. It is not part of the registration and
does not change P1. Data from this experiment count for P1 only if they meet the
registered inclusion criteria (`docs/PREREGISTRATION_P1.md`, section 2) and are
listed in an addendum before analysis.

Numbers: `scripts/p1_measurement_design.py` writes `docs/p1_measurement_design.json`,
using the frozen P1 code (`e3_core/prediction_p1.py`, `bcs.py`, `constants.py`)
unchanged. Planning values for `gamma`, `Tc` and `Theta_D` are Phillips (1959). The
registered analysis must use the values measured on these samples.

## 1. Idea

Three pieces of the same aluminium, treated identically, differing only in their
surface-to-volume ratio `A/V`. P1 predicts that the departure temperature rises
with `A/V` by an amount fixed without any free prefactor (falsifier F3). A
surface-localised artefact predicts that the excess heat capacity per unit area
is the same for all three (falsifier F4). Three samples spanning a factor of 54
in `A/V` separate these cleanly.

## 2. Samples

All three are cut from **one lot** of aluminium of at least 99.999% purity, by a
low-damage method (for example spark erosion), then **annealed together** and
**etched together**, so that bulk purity, strain and surface oxide are the same.

| Sample | Shape | Mass | A/V | Ratio to S1 |
|---|---|---|---|---|
| S1 | cube 4 x 4 x 4 mm | 172.8 mg | 1500 m^-1 | 1 |
| S2 | plate 10 x 10 x 0.25 mm | 67.5 mg | 8400 m^-1 | 5.6 |
| S3 | foil 10 x 10 x 0.025 mm | 6.75 mg | 80400 m^-1 | 53.6 |

Every dimension is at least 10 um (criterion 2), and both pair ratios exceed the
registered minimum of 4 for F3. Dimensions must be measured, so that `A/V` is known
within 20% (criterion 6). The thermal contact patch should cover at most a few
percent of the surface and be the same fraction for all three samples.

Each sample is one piece. Stacked foils are not allowed: whether a stack counts
as one system or several for `A` has not been decided.

## 3. Predictions (planning values)

| Sample | T*(0.25) | T*(1) | T*(4) | Required window (0.8 T*(0.25) to 1.1 T*(4)) |
|---|---|---|---|---|
| S1 | 0.220 K | 0.263 K | 0.324 K | 0.176-0.356 K |
| S2 | 0.276 K | 0.343 K | 0.450 K | 0.221-0.494 K |
| S3 | 0.403 K | 0.555 K | 0.845 K | 0.323-0.929 K |

**Prefactor-free (F3).** Whatever the prefactor, if S1 departs at `T1`, S2 and S3
must depart at the partner temperatures given by
`prediction_p1.partner_crossing_temperature`. For example, at f = 1, S1 at 0.263 K
implies S2 at 0.343 K and S3 at 0.555 K. The smallest predicted S1-S2 shift over
the band is 0.055 K. The S1-S3 shift is at least 0.18 K.

## 4. Measurement requirements

| Item | Requirement | Reason |
|---|---|---|
| Temperature range | 0.15 K to 1.3 K for every sample | covers all windows, plus Tc |
| Point spacing | at most 14 mK between 0.15 and 0.95 K | a quarter of the smallest F3 shift |
| Uncertainty | target at most 5% per point; registered limit at most 20% below T*(0.25) | F1 needs at most 20% |
| Field, superconducting runs | at most 1 mT, measured in situ (for example with a fluxgate) or bounded by shielding (mu-metal plus a superconducting shield); cool through Tc inside the shield | criterion 3; nuclear term at most 2.3e-4 of the baseline |
| Normal-state run | 20 mT (about twice Hc(0)), from 0.1 K to 1.3 K, for `gamma` and `Theta_D` | nuclear Zeeman term at most 0.2% of `gamma T` at 0.1 K |
| Tc | from the zero-field transition of each sample | criterion 7 |
| Addenda | measured separately, same run conditions, reported with the data | criterion 5 |
| Exchange gas | none at the measured temperatures | exclusion rule |
| Data | numerical table per sample: T, C, u, addenda subtracted | criterion 4 |
| Instrument | the same calorimeter and thermometer calibration for all three | the comparison is relative |

**Heat capacities to resolve** (baseline, planning values):

| Sample | At window bottom | At T*(1) | At window top |
|---|---|---|---|
| S1 | 6.2e-9 J/K | 1.5e-7 J/K | 7.9e-7 J/K |
| S2 | 1.7e-8 J/K | 2.6e-7 J/K | 1.1e-6 J/K |
| S3 | 1.9e-8 J/K | 1.6e-7 J/K | 6.1e-7 J/K |

## 5. Blinding

1. The person operating the calorimeter receives coded sample labels and does
   not see the predicted temperatures.
2. Raw data, dimensions and addenda are deposited in the repository, and listed
   in a P1 addendum, before any analysis.
3. The analysis uses the frozen code; its SHA-256 hashes are checked first
   (registration, section 6).

## 6. Auxiliary control (exploratory, not a registered falsifier)

**S2-ox:** the same geometry as S2, with a deliberately thicker anodic oxide. P1
predicts the same departure temperature as S2, since `A/V` and `a` are unchanged.
A surface-oxide artefact predicts a larger excess in S2-ox. Its result is reported
as exploratory only.

## 7. Feasibility questions for the laboratory

1. **Resolution at the lowest temperatures.** S1 needs about 6e-9 J/K resolved
   to 5% near 0.18 K. The addenda there must be small enough, or S1 made larger.
   A larger S1 lowers its predicted temperatures and its heat capacity per mole,
   so it is not automatically easier.
2. **Internal equilibrium.** Deep in the superconducting state, electronic heat
   conduction is frozen out. The internal thermal time of the 4 mm cube may
   become long compared with the external relaxation time (the "tau2 effect").
   The lab must show that tau2/tau1 is small over the window, or use an adiabatic
   method.
3. **The thin foil.** S3 is fragile and has the largest oxide fraction. Mounting
   it without strain and with a reproducible contact is the practical challenge.

## 8. Decisions for the researcher

- The sample sizes above are a proposal. Changing them changes the predicted
  bands, which must then be recomputed with the script before measurement.
- Which laboratory, or which collaboration, will measure.
