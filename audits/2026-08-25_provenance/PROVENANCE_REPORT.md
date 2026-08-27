# Bruno/E3 provenance reconstruction

**Audit date:** 2026-08-25  
**Legacy corpus:** `/home/winnay/Documents/Codex/E3_Engine`  
**Purpose:** recover the idea's chronology, not revalidate every scientific claim

## Bottom line

The surviving evidence does **not** show one Bruno constant extracted from
SN/GRB/neutrino observations and then cleanly converted to a laser-cooling
scale. It shows several different quantities being given the same name during
successive research phases:

1. a saturation/decay parameter `k` scanned over `0.001` to `0.1`;
2. a dimensionless `0.001005` "tangency" multiplier;
3. a cosmic fluence trigger fixed at `1e-5 J/m²`;
4. a Planck-geometry coefficient near `1313` (recomputed as `1310.11`);
5. a faulty GW150914 coefficient `1366`;
6. an undocumented laboratory value `(1340 ± 60)×10^-6 K^-1 s^-1`;
7. placeholder constants embedded in later engine files.

The original intuition is recoverable. The numerical lineage is not yet one
continuous derivation.

## Evidence hierarchy

Dates below have different authority:

1. Git author dates from authored repositories;
2. the internal figure-development CSV created with the original drop;
3. filesystem modification times, used only as supporting evidence;
4. folder names such as `phase1`, `Final`, or `Rebuilt`, which are not dates.

The earliest surviving authored Git repository is
`Entropy-Collapse-Research`, initially committed 2025-03-26 and populated by a
"New Repo first drop" on 2025-03-27. Its internal figure timeline records work
from 2025-03-23 onward.

## Reconstructed timeline

### 1. March 23–25, 2025 — entropy-first and saturation phase

The internal `Figure_Waves_Timeline.csv` records:

- March 23: entropy-gradient, saturation, horizon, and predictive models;
- March 24: correlation tests and `Entropy Collapse Test 1.5`–`1.6`;
- March 25: `Figure_64`, labeled "Chajar Constant", followed by Test 2.2.

The master summary states the originating proposition as:

> Entropy is the fundamental descriptor of structure, not temperature.

Its early equations use `k` as an exponential decay/saturation rate:

`S(tau) = S_inf (1 - exp(-k tau))`.

That `k` is not the later `3/(R T)` coefficient. Its dimensions depend on the
definition and units of `tau`.

### 2. March 25 — `0.001005` tangency multiplier

`Scripts/Entropy Collapse Test/Bruno Constant.py` defines:

```python
k_chajar = 0.001005
T_tangent = T_planck * k_chajar
```

This makes `0.001005` a dimensionless multiplier of Planck temperature. The
script does not fit it from SN, GRB, neutrino, or laser data.

The plot behind Figure 64 is also circular as a temperature validation:

```python
flux = a_rad * T**4
entropy_temp = (flux / a_rad)**0.25
```

The second line algebraically returns the input `T`. The displayed agreement is
therefore an identity, not an independent empirical recovery of temperature.

### 3. March 25–27 — lab work is proposed, not yet performed

The master summary's future-work section says:

> Use lab-scale data (e.g., from doppler cooling or superconductors) to
> calibrate and test k values.

This is decisive provenance: in the earliest surviving theory record, Doppler
cooling is a future validation target, not the source of the initial constant.

The same summary calls the Roman input "real flux data", but the committed
filename is `...sim-ultradeep-mocks.csv`: a simulated mock catalog. Its role
must not be described as direct observational validation.

### 4. April 11–13 — cosmic fluence and multimessenger notebook phase

The `Bruno_Entropy_Project` initial commit introduces large notebooks and
registries for supernovae, BATSE GRBs, IceCube candidates, and fluence studies.
The notebooks contain rich saved output—up to 28–29 embedded plots in the two
largest lineages—which explains why they functioned like visual lab books.

Their operative Bruno trigger is:

`fluence >= 1e-5 J/m²`.

The surviving documentation labels this the Bruno fluence threshold but does
not derive it from the earlier `0.001005` multiplier, the later `1313`
coefficient, or a detector sensitivity model. It is presently a chosen event
classification threshold.

The notebooks repeatedly classify and crossmatch events using this same fixed
cut. Those event matches therefore cannot independently estimate the cut unless
a separate fitting step is recovered.

### 5. April 11 — Planck and GW coefficients assembled into one note

`data/notes/Bruno Constant Note.txt` contains mutually incompatible historical
sections and thresholds (`1 K`, `1,000,000 K`, and approximately `7.61e-4 K`).
It should be treated as a concatenated evolution log, not a single derivation.

It derives:

`kappa = 3/(l_P T_P)`, reported as `1313 K^-1`.

The correct unit from the written equation is `m^-1 K^-1`, and recomputation
gives approximately `1310.11 m^-1 K^-1`.

The same note later derives `1366` from GW150914 using an incorrect Hawking
temperature. The initial audit showed that correction gives `16463.32
m^-1 K^-1`, and that the black-hole mass cancels. It is a formula identity, not
observational calibration.

### 6. May 18–June 6 — unified packaging

The `bruno-collapse-unified` repository imports the April project and adds
theory outlines and extraction utilities. The extraction script computes:

`(Entropy/Volume)/(Entropy/Area) = Area/Volume`.

Entropy cancels. It also generates temperature as `10**row_index`. Consequently
its Bruno-versus-temperature plot is neither an entropy extraction nor a
temperature measurement.

### 7. July 29–August 1 — E3 and MDQT phase

`E3_CURRENT_PRODUCTION` begins on 2025-07-29. Commits on July 30–31 describe the
DAVP pipeline and MDQT integration. The laser-cooling code under
`external/mdqt-sim/laser-cooling-2019` is an external simulation codebase; its
presence does not itself establish that a Bruno coefficient was extracted from
its outputs.

The existing corpus audit found that the production engine did not consistently
consume `1313` or `1366`; many serialized models instead contain the obvious
placeholder `1.23456789e-23`.

### 8. August 2025 — LLM reconstruction and constant promotion

`COHERENT_E3_PROJECT_PLAN.md` declares `(1340 ± 60)×10^-6 K^-1 s^-1` the final
experimentally validated value but gives no experiment, source file, fit, or
derivation. `COMPLETE_SESSION_ARCHIVE.md` later describes an LLM-led replacement
of that value with `1366`, explicitly calling the former value's derivation
unclear.

This is documentation propagation, not experimental provenance. Neither value
should be restored to the clean engine as a validated universal constant.

## Image and notebook findings

- `Figure_61.png` plots temperatures generated by a prescribed logarithmic
  range against the fixed Planck temperature; it is a model visualization.
- `Figure_64.png` adds benchmark lines and the preselected `0.001005` Planck
  multiplier; it does not visually demonstrate a fitted tangency.
- `LaTeX TimeStamp.png` is valuable provenance: it shows source files dated
  March 25–27, consistent with the internal timeline and Git import.
- `Bruno_timeline_analysis.ipynb` and `Fluence_Model_Comparison.ipynb` are the
  richest surviving visual lab books, but exact hashes show they were copied
  across many later trees.

## What survives scientifically

The following is the cleanest recoverable hypothesis:

1. entropy capacity may be associated with a boundary area;
2. an equivalent volumetric density then scales with `A/V = 3/R` for a sphere;
3. temperature can change when energy is redistributed between internal,
   motional, radiative, and environmental channels;
4. a proposed transition should be expressed as a dimensionless capacity ratio,
   then tested against data not used to define it.

What does **not** yet survive is a universal numerical bridge from cosmic-event
data to laser cooling.

## Recommended restart target

Do not begin by selecting one legacy value. Reconstruct a single transparent
dimensionless observable:

`eta_S = S_system / S_boundary_capacity`.

For each candidate dataset, record raw measured fields, conversions, inferred
quantities, uncertainties, and whether the event was used for discovery or
validation. The cosmic-to-lab bridge must then be a stated similarity law, not
a numerical resize.

The first reproduction notebook should use one early dataset only and must be
paired with plain Python plus tests. It should reproduce the input data and
standard physics before calculating any E3 quantity.

## Audit limitations

- Generated `datasets/` trees and bundled raw external model collections were
  excluded from this provenance parser; they are not authored chronology.
- The corpus root Git repository was excluded because it is a wrapper around
  nested repositories.
- Filesystem mtimes can reflect copying. They are never used alone to claim
  authorship dates.
- The two private repositories noted in the initial audit remain unavailable.

