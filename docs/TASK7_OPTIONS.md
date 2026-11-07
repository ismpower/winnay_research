# Task 7 options: reference length L_0 and boundary capacity sigma_crit

**Status:** options for the researcher's decision, 2026-11-07. **Nothing here is chosen.**
Numbers come from `scripts/task7_candidate_scales.py` (output:
`docs/task7_candidate_scales.json`). Identities are tested in
`e3_core/tests/test_scales.py` and `e3_core/tests/test_constants.py`.

## 0. What is already fixed

- `beta_geom = A/V = 3/R` has units `m^-1`. A temperature coefficient
  `kappa_T` has units `m^-1 K^-1` (task 1).
- A dimensionless criterion needs either a declared length `L_0`
  (`beta_tilde = 3 L_0/R`) or a declared surface capacity `sigma_crit`
  (`eta_S = S/(sigma_crit A)`).
- Symbols follow `docs/NOTATION.md`.

## 1. Two results that narrow the choice

**R1. A "Planck" normalization is the thermal photon length in disguise.**
Any condition `R T = const` calibrated at the Planck point `(l_P, T_P)` has
`const = l_P T_P = hbar c/k_B`, for every value of `G` (tested). So:

```text
legacy Planck route   beta_geom = kappa_T^Pl T   <=>  R = hbar c/(k_B T)        =: lambda_gamma(T)
legacy Hawking route  beta_geom = kappa_T^GW T   <=>  R = lambda_gamma(T)/(4 pi)
```

`lambda_gamma(T)` is the reduced thermal photon length (2.29 mm at 1 K,
0.84 mm at the CMB temperature, 7.6 um at 300 K). It is not the Wien peak
wavelength, which is larger by `2 pi/4.965 = 1.2655`.

The Hawking-route condition is exactly the relation `R_s T_H = hbar c/(4 pi k_B)`,
which every Schwarzschild black hole satisfies. But the condition contains no
mass. It is therefore **necessary but not sufficient** for a horizon: a 1 K
object with radius 0.18 mm satisfies it without being a black hole. Identifying
collapse also needs the mass condition `R = 2GM/c^2` (the compactness
`beta_horizon` of H-001).

**R2. A surface capacity fixes eta_S only up to its numerical prefactor.**
For `sigma_crit = c k_B/l^2`, the prefactor `c` moves the `eta_S = 1` point.
The Bekenstein-Hawking value has `c = 1/4` with `l = l_P`, fixed by a derivation.
Any other prefactor must also come from an argument. Choosing it so that
`eta_S = 1` lands on a feature in the data is fitting, not prediction.

## 2. Candidate reference lengths L_0

| | `L_0` | `beta_tilde = 1` means | Standard physics already says | What E3 would have to add |
|---|---|---|---|---|
| A | `lambda_gamma(T) = hbar c/(k_B T)` | system as small as a thermal photon length; equivalent to the legacy Planck route (R1) | below this size the blackbody mode count departs from the continuum (Weyl) limit, a known finite-size effect | a predicted effect beyond standard cavity electrodynamics |
| B | `lambda_dB = h/sqrt(2 pi m k_B T)` | system as small as a particle's thermal wavelength | quantum confinement; in a gas the relevant condition is `n lambda_dB^3 = 2.612` (BEC), with known finite-size shifts | a departure from standard degenerate-gas theory |
| C | correlation or coherence length `xi` | system size reaches `xi` | finite-size scaling of phase transitions; for superconducting grains, loss of superconductivity when level spacing approaches the gap | a universal coefficient across materials not given by finite-size scaling |
| D | `R_s = 2GM/c^2` (mass dependent) | horizon formation (`beta_horizon = 1`) | general relativity: exactly the horizon condition | nothing new by itself; useful as the mass condition that R1 shows is missing |

A and D together reproduce the black-hole case exactly: `R = R_s` and
`R T = hbar c/(4 pi k_B)` are both true for every Schwarzschild hole.
`lambda_dB/lambda_gamma = sqrt(2 pi k_B T/(m c^2))`, which is much less than 1
for any non-relativistic particle (tested), so A and B describe very different
regimes.

## 3. Candidate boundary capacities sigma_crit

`eta_S = S_system/(sigma_crit A)` for three reference systems:

| `sigma_crit` | 10 solar-mass black hole | blackbody cavity, R = 1 cm, 1 K | Phillips Al sample, 1 K (normal electrons) |
|---|---|---|---|
| (i) `k_B/(4 l_P^2) = 1.32e46 J K^-1 m^-2` (Bekenstein-Hawking) | **1** (exactly, any mass) | 2.5e-64 | 9.1e-47 |
| (ii) `k_B/lambda_gamma(T)^2` (one `k_B` per thermal photon area) | 1.3e80 | 1.28 | 4.5e17 |
| (iii) `k_B/a^2`, `a` = mean atomic spacing (one `k_B` per surface site) | not defined | not defined | 5.6e3 |

Observations:

- **No single sigma_crit puts both black holes and laboratory matter near
  eta_S = 1.** (i) saturates only for horizons; (ii) and (iii) give black-hole
  values far above 1. A cross-regime law would need either a
  temperature/length-dependent capacity with a stated rule, or a different
  observable.
- (i) is untestable in the laboratory: lab values are 1e-64 to 1e-46.
- (ii) applied to a photon gas gives `eta_S = (4 pi^2/135) R/lambda_gamma`, which
  equals 1 at `R = 3.42 lambda_gamma` (tested). So for radiation, (ii) and L_0
  option A mark the same size scale up to an O(1) factor. For condensed matter
  `eta_S` is far above 1 at all accessible temperatures, so (ii) predicts no
  laboratory crossing.
- (iii) has `eta_S = 1` exactly when the entropy per atom equals `3a/R` (tested;
  about `2.9e-8 k_B` for the Phillips sample). That is the point where bulk
  entropy falls to one `k_B` per surface site.

### 3.1 Option (iii) in aluminium: a post-hoc coincidence to treat with care

In normal-state aluminium, (iii) reaches `eta_S = 1` only at 0.18 mK. Below
`Tc = 1.163 K` in zero field, however, the sample is superconducting and its
electronic entropy falls exponentially. Using weak-coupling BCS electrons plus
Debye phonons (`e3_core.bcs`, Debye 427.7 K from the paper), the crossing is at
**0.191 K**. Varying the factor `f` (sigma prefactor times A/V relative to a
sphere):

| f | 0.1 | 0.25 | 0.5 | 1 | 2 | 4 | 10 |
|---|---|---|---|---|---|---|---|
| T at eta_S = 1 (K) | 0.137 | 0.161 | 0.176 | 0.191 | 0.208 | 0.225 | 0.253 |

Phillips reported his lowest superconducting point, near 0.17 K, at about four
times the exponential extrapolation, and argued that the excess exceeded his
estimated errors (`ALUMINUM_CROSSOVER.md`). The crossing lands in the same
region for any `f` between 0.25 and 4.

This must **not** be read as evidence:

1. It was found after the anomaly was known, while several capacities were
   being compared (look-elsewhere effect).
2. It holds only if `S_system` excludes nuclear-spin entropy. Al-27 has spin 5/2,
   whose entropy `k_B ln 6` per atom is fully disordered at 0.2 K and is
   6.2e7 times the threshold. Including it puts `eta_S` far above 1 at every
   accessible temperature.
3. Phonons are 32% of the counted entropy at the crossing, so the result also
   depends on the Debye model at these temperatures.
4. Phillips' lowest points carry precision of up to about 20% and a 15% addenda
   correction.
5. Standard explanations of excess low-temperature heat capacity in
   superconductors, such as impurity or nuclear contributions or trapped
   normal regions, have not been examined here.

What would make it a real test: the threshold scales as `a/R`, so for
geometrically similar samples `f = R_reference/R_sample`. **E3 option (iii)
predicts that the anomaly temperature shifts with sample size**: up to about
0.25 K for a sample ten times smaller, down to about 0.14 K for one ten times
larger. A per-mole effect such as impurities would not shift this way. This is
a falsifiable prediction, but it is only a candidate for task 9 if (iii) is
chosen on its own merits first.

## 4. Decisions needed from the researcher

1. **L_0:** A, B, C, D, or a combination? R1 shows that the legacy routes amount
   to A. A horizon criterion also needs D.
2. **sigma_crit and its prefactor:** (i), (ii), (iii) or another, with the
   argument that fixes the prefactor stated before any comparison with data.
3. **Which entropy is S_system?** Electronic, phonon, nuclear spin, or total?
   Option (iii) changes from "never crosses" to "crosses at 0.19 K" depending
   on this choice alone.
4. **One law across regimes, or regime-specific?** Section 3 shows that no
   single fixed capacity covers black holes and laboratory matter.
5. **Then task 9:** pre-register one prediction (for example the
   size-dependence test in 3.1, if (iii) is chosen) before analysing new data.

## 5. Researcher responses (2026-11-07)

Recorded as given; nothing below is yet a final choice.

1. **L_0:** "a combination". Which options combine has not been specified.
   (A + D reproduces the black-hole case exactly; see section 2.)
2. **sigma_crit:** agreed that sigma_crit and its prefactor must be fixed by an
   argument, not fitted. No capacity chosen yet.
3. **S_system:** "none of the named". In the researcher's model, electrons
   "come far after" and nuclear spin is an emergent phenomenon of the rise of
   entropy. S_system is therefore intended to be more fundamental than any
   particle species, and is not yet operationally defined.
4. **Scope:** a constant must apply in every regime, but only within the
   observable universe ("in our universe"). Anything beyond it is speculation.

### Consequences (mathematical, not choices)

- **3 needs a measurement rule before eta_S can be evaluated.** The species-free
  quantity that experiments can measure is the calorimetric entropy,
  `S(T) = S(T_0) + int_{T_0}^{T} C/T' dT'`, which counts every degree of
  freedom without naming it. An absolute value of S needs a reference, either
  the third law (integrating down through nuclear ordering at microkelvin
  temperatures) or a model.
- **With total entropy the aluminium coincidence of section 3.1 disappears.**
  Total entropy at 0.2 K includes the nuclear-spin term `k_B ln 6` per atom,
  6.2e7 times the lattice threshold, so eta_S stays far above 1. Section 3.1
  survives only under an S that leaves out degrees of freedom that are fully
  disordered and unchanging, for example "the entropy that changes over the
  measured range". That would be a definition to argue for, not one to adopt
  because it produces the coincidence.
- **Scope 4 still includes black holes and laboratory matter**, since both are
  in our universe. Section 3 shows that no single fixed sigma_crit puts both
  near eta_S = 1, so a law of this form needs sigma_crit to vary with a stated
  rule (and that rule then carries the physics), or a different observable.

