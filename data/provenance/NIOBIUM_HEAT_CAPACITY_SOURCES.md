# Niobium heat-capacity sources

## NBS Circular 519

- Title: *Low Temperature Physics: Proceedings of the Second Biennial Conference*
- Publisher: United States Department of Commerce, National Bureau of Standards
- Series: National Bureau of Standards Circular 519
- Local raw file: `data/raw/niobium_heat_capacity/nist_circular_519/NBS_Circular_519_Low_Temperature_Physics.pdf`
- SHA-256: `482e4a41aec8f63dc42de40bc1e6d8e4a0662dd181d83cac9a7517789909d193`
- Relevant contribution: A. Brown, M. W. Zemansky, and H. A. Boorse,
  "Specific Heat of Niobium at Various Temperatures," printed pages 99-101
  (PDF pages 107-109).

The contribution documents the calorimeter, the sample, low-temperature
relations, and preliminary helium-temperature findings. It does **not** print
the final 2.5-11 K numerical data. It therefore serves as authoritative
methodological provenance, not as the numerical crossover source.

## Final Physical Review article

- A. Brown, M. W. Zemansky, and H. A. Boorse, *The Superconducting and Normal
  Heat Capacities of Niobium*, Physical Review 92, 52-58 (1953)
- DOI: `10.1103/PhysRev.92.52`
- Reported range: 2.5-11 K
- Reported zero-field transition: `8.70 +/- 0.10 K`

The APS abstract is accessible, but the full PDF requires subscription
authorization. Direct APS PDF endpoints returned HTTP 403 on 2026-08-26, and
the in-app APS page displayed "Authorization Required." No table has been
transcribed or reconstructed from the abstract.

## Acceptance boundary

Graph digitization must remain explicitly labeled presentation-derived and
cannot be promoted to confirmed tabular reference data. A graphical bracket
may be used as a cue if its construction and uncertainty are recorded.

## Shen 1965 open thesis

- Y. L. Shen, *I. Low Temperature Heat Capacities of Vanadium, Niobium and
  Tantalum; II. Low Temperature Heat Capacity of Ferromagnetic Chromic
  Tribromide*, Ph.D. thesis, UCRL-16117 (1965)
- Official record: `https://escholarship.org/uc/item/0t19k8j8`
- Local raw file:
  `data/raw/niobium_heat_capacity/shen_1965/Shen_1965_UCRL_16117.pdf`
- SHA-256:
  `fd508c1c913953952347a9885173f5b994d7df59da36153924c7c32265336b3b`
- File size: `4,013,075 bytes`; 101 PDF pages
- Relevant figures: Fig. 9 on PDF page 32, Fig. 10 on PDF page 33, and Fig. 11
  on PDF page 35.

Figure 11 supports a conservative presentation-derived crossover bracket.
The audit and reproducible calculation are in
`reference/superconductivity/comparison_material/analysis/SHEN_NIOBIUM_CROSSOVER.md`
and `scripts/analyze_niobium_shen_crossover.py`. No point-by-point niobium
calorimetry table is claimed.
