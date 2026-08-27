# Candidate audit for the first E3 superconductivity reproduction

**Audited:** 2026-08-26  
**Scope:** the 71 elemental observations in `elemental_observations.tsv`  
**Evidence status:** reported in NIMS SuperCon Ver.240322; original papers not
yet independently checked

This audit ranks usefulness for the proposed experiment by the presence of
relevant recorded observables. It does not assign a physics score, average a
measurement, fill a blank, or infer an unreported value.

## Primary candidate: aluminium, NIMS data number 151067

NIMS identifies the source as:

- reference number: `PR1140676`
- title: *Heat capacities of aluminum between 0.1 K and 4.0 K*
- author: N. E. Phillips
- journal: *Physical Review* 114 (1959) 676
- reported midpoint and recommended transition temperature: `1.163 K`
- electronic specific-heat coefficient: `1.35 mJ/mol.K2`
- Debye temperature: `427.7 K`, derivation field `SP-heat`
- preparation comment: `annealed in vac (450C,48h)`
- associated specific-heat graph identifier: `MSP151067`

The associated raw NIMS file `dat/MSP151067.dat` contains 85 tabulated points:

| Magnetic field | Temperature range in file | Points | Recorded ordinate |
|---:|---:|---:|---|
| 0 gauss | 0.236–1.981 K | 48 | heat capacity in mJ/mol.K |
| 300 gauss | 0.103–1.194 K | 37 | heat capacity in mJ/mol.K |

This is the strongest first candidate because it supplies temperature-dependent
heat capacity under two recorded magnetic-field conditions. It can support a
direct comparison of `C/T` and a partial entropy-difference integral over their
shared measured temperature interval.

### Boundary on the first calculation

The two series do not both extend to zero temperature and do not cover identical
temperature ranges. Therefore a full integral from `0 K` requires an explicit
low-temperature extrapolation or an additional source. Such an extrapolation is
a model-dependent analysis step, not measured NIMS data, and must be labeled as
such. The first result should report both:

1. an integral restricted to the overlapping measured interval; and
2. any extrapolated integral separately, with the assumed functional form and
   sensitivity to that assumption.

The interpretation of the `0` and `300 gauss` series must also be checked against
the original paper before labeling either series normal or superconducting.

## Secondary candidate: niobium thin-film series

NIMS records six rows (`152558` through `152563`, inclusive) from reference
`P072064503`:

- title: *Dependence of magnetic penetration depth on the thickness of
  superconducting Nb thin films*
- journal: *Physical Review B* 72 (2005) 064503
- preparation: DC magnetron sputtering in Ar on Si(100), recorded deposition
  rate `2 nm/s`
- transition width: `0.1 K` for every listed row

| NIMS number | Tc (K) | Penetration depth (A) | Normal resistivity (uOhm.cm) |
|---:|---:|---:|---:|
| 152558 | 7.13 | 2174 | 16.1 |
| 152559 | 7.95 | 1361 | 11.8 |
| 152560 | 8.81 | 1191 | 10.3 |
| 152561 | 9.09 | 1008 | 5.37 |
| 152562 | 9.47 | 872 | 4.48 |
| 152563 | 9.71 | 772 | 3.75 |

These values are transcribed verbatim from NIMS. The dataset does not populate
the retained `sample` field with film thickness, despite thickness appearing in
the paper title. The original paper is therefore required before treating
thickness as the controlled variable or fitting any relation.

This series is valuable after the aluminium thermodynamic reproduction because
it connects a coherence-scale observable (penetration depth) with transport and
transition measurements across related samples.

## Supporting candidates

### Lead

Lead has complementary thermodynamic records rather than one self-contained
record:

- `150030`: `Tc = 7.175 K`, specific-heat jump `53 mJ/mol.K`, and recorded
  critical-field values from `PR1121888`.
- `150037`: `Tc = 7.186 K`, `gamma = 3.47 mJ/mol.K2`, from `P075174502`.
- `150038`: `Tc = 7.17 K`, `gamma = 3.13 mJ/mol.K2`, Debye temperature
  `96.3 K`, from `PR0881182`.

Lead is a useful cross-check once the three original sources are inspected. The
values must not be combined as if they describe one sample.

### Mercury

Record `111526` contains `Tc = 4.16 K`, `gamma = 1.79 mJ/mol.K2`, Debye
temperature `71.9 K`, and critical-field values. NIMS identifies the paper as
*Specific heat of mercury and thallium between 0.35 and 4.2 K* (`PR135A0631`).
No associated heat-capacity curve was identified in the supplied `data.zip`.

### Tin

The selected tin records primarily supply transition temperatures, isotope
comparisons, and some critical-field values. They do not contain an associated
heat-capacity series in the retained NIMS fields, so tin is not the best first
entropy candidate from this dataset alone.

## Decision

1. Reproduce the aluminium heat-capacity curves from `MSP151067.dat` without
   extrapolation.
2. Obtain and inspect the Phillips paper before assigning physical-state labels
   to the field series.
3. Define the shared measured integration interval and calculate the partial
   integral of the recorded heat-capacity difference divided by temperature.
4. Keep interpolation and numerical-integration uncertainty separate from
   experimental uncertainty; the latter is not supplied in the NIMS data file.
5. Use the niobium thin-film series only as the second, transport/coherence test.
