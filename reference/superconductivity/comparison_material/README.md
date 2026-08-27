# Superconductivity comparison material

Primary-source material selected for the first E3 superconductivity
reproduction. Retrieved 2026-08-26. Files are preserved without modification;
their SHA-256 checksums are recorded in `SOURCE_MANIFEST.json`.

## Primary aluminium experiment

- Norman E. Phillips, *Heat Capacity of Aluminum between 0.1 K and 4.0 K*,
  Physical Review 114, 676 (1959).
- DOI: https://doi.org/10.1103/PhysRev.114.676
- Local PDF: `papers/Phillips_1959_aluminum_heat_capacity.pdf`
- NIMS curve: `data/MSP151067.dat`
- Visually checked Table II transcription: `data/Phillips_1959_Table_II.tsv`

This is the primary reproduction source. The paper states which measurements
represent the normal and superconducting conditions; the NIMS curve supplies
the tabulated values used for computation. Neither source should be silently
used to fill a blank in the other.

The Table II transcription preserves printed column groups and source order.
Those groups describe the table layout and must not be assumed to identify
experimental runs unless the paper explicitly establishes that mapping.

## Niobium transport/coherence comparison

- A. I. Gubin et al., *Dependence of magnetic penetration depth on the
  thickness of superconducting Nb thin films*, Physical Review B 72, 064503
  (2005).
- DOI and publisher page: https://doi.org/10.1103/PhysRevB.72.064503
- Local PDF: `papers/Gubin_et_al_2005_niobium_thin_films.pdf`

## Niobium calorimetry comparison

- Y. L. Shen, *Low Temperature Heat Capacities of Vanadium, Niobium and
  Tantalum*, UCRL-16117 (1965).
- Official record: https://escholarship.org/uc/item/0t19k8j8
- Preserved raw PDF:
  `../../../data/raw/niobium_heat_capacity/shen_1965/Shen_1965_UCRL_16117.pdf`
- Figure-derived audit: `analysis/SHEN_NIOBIUM_CROSSOVER.md`

The thesis contains graphical rather than tabular niobium observations. Its
Figure 11 supports a conservative crossover bracket, which remains explicitly
presentation-derived and does not have the status of a tabulated measurement.

## Lead thermodynamic comparisons

- D. L. Decker, D. E. Mapother, and R. W. Shaw, *Critical Field Measurements
  on Superconducting Lead Isotopes*, Physical Review 112, 1888 (1958).
- DOI and publisher page: https://doi.org/10.1103/PhysRev.112.1888
- Local PDF: `papers/Decker_et_al_1958_lead_critical_field.pdf`

- N. Suresh and J. L. Tallon, *Thermodynamic properties of Pb determined from
  pressure-dependent critical-field measurements*, Physical Review B 75,
  174502 (2007).
- DOI and publisher page: https://doi.org/10.1103/PhysRevB.75.174502
- Author preprint: https://arxiv.org/abs/0704.2077
- Local PDF: `papers/Suresh_Tallon_2007_lead_thermodynamics.pdf`

## Evidence rule

Downloading a paper does not validate a numerical claim. Values become
`cross_checked` only after the relevant table, figure, sample condition, units,
and uncertainty have been compared against the NIMS record and recorded in a
separate audit.
