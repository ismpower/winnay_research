# Pre-registration P2, addendum 2: first blinded data screening

**Date:** 2026-11-25. This addendum applies section 2 of the registered
`docs/PREREGISTRATION_P2.md` (registration commit `55b8f8d`, see addendum 1). It
does not change the hypothesis, the criteria or the falsifiers.

## Outcome

**No qualifying dataset was found.** One candidate, Barucci et al. (2001) on
TeO2, passes every check possible from public records, but its full text is
closed access and could not be screened. P2 cannot be tested on the literature
screened so far.

## Procedure

- Screening was done by the assistant at the researcher's request, after the
  researcher's declaration was committed (addendum 1, commit `5ad8207`).
- **Discovery:** one agent ran 22 neutrally worded web searches and returned
  bibliographic identity, access status and methods-level reasons only. Queries
  are listed in the section "Search queries" below.
- **Rule-based triage (no data):**
  - *Nuclear rule (criterion 2)*, from the material alone.
  - *Reach versus size (criteria 4 and 8)*: `scripts/p2_screening_triage.py`
    computes, with the frozen `predicted_band`, the largest equivalent cube edge
    `L_eq = 6/(A/V)` for which a stated lowest temperature still reaches
    `0.8 T*(0.25)`. Handbook planning values are used. Criterion 4 (every
    dimension at least 0.1 mm) allows `L_eq` down to about 0.3 mm (thin plate).
    A floor needing `L_eq` below that cannot qualify whatever the sample.
- **Methods-only reading:** three further agents read only sample, apparatus and
  method sections or public bibliographic records, and answered the inclusion
  checklist. They were told to report no values, fits or conclusions.
- Bot checks and paywalls were not circumvented.

## Triage numbers (`scripts/p2_screening_triage.py`)

| Candidate | Material | Stated floor | Largest `L_eq` served |
|---|---|---|---|
| C1 Barucci 2001 | TeO2 | 0.06 K | 136 mm |
| C2 White 1990 | TeO2 | 0.6 K | 0.14 mm |
| C3 Keesom & Seidel 1959 | Si / Ge | 1.2 K / 0.5 K | 0.42 mm / 1.2 mm |
| C6 Gusev 2015 | Ge | 2.5 K | 0.011 mm |
| C9 CaWO4 1968 | CaWO4 | 5 K | 0.009 mm |
| C10 ZnSe 1975 | ZnSe | 2 K | 0.011 mm |
| C13 Scales 1958 | LiF / KI | 2 K | 0.10 mm / 0.014 mm |
| C11 KCl 1953 (if floor 1 K) | KCl | 1 K | 0.04 mm |

## Candidates

| # | Study | Decision | Reason (registered criterion) |
|---|---|---|---|
| C1 | Barucci, Brofferio, Giuliani, Gottardi, Peroni, Ventura, J. Low Temp. Phys. 123, 303 (2001), DOI 10.1023/A:1017555615150 (TeO2) | **not screened** | closed access (Unpaywall closed, no repository file). From public records: relaxation calorimetry to 60 mK, so the range suits samples up to about 13 cm; single crystal, dimensions, table, uncertainties, field, addenda and exchange gas not verifiable |
| C2 | White, Collocott, Collins, J. Phys.: Condens. Matter 2, 7715 (1990), DOI 10.1088/0953-8984/2/37/015 (TeO2) | fails | 8 with 4: heat capacity from 0.6 K, which needs `L_eq` of at most 0.14 mm |
| C3 | Keesom & Seidel, Phys. Rev. 113, 33 (1959), DOI 10.1103/PhysRev.113.33 (Si, Ge) | **not screened**, likely fails | paywalled. Public record: doped and degenerate n-type samples (fail 1); floors need `L_eq` at most 0.42 mm (Si) or 1.2 mm (Ge) (8) |
| C4 | Bryant & Keesom, Phys. Rev. 124, 698 (1961), DOI 10.1103/PhysRev.124.698 (Ge) | fails | 1: doped, degenerate n-type ingots (from public abstract) |
| C5 | Li2MoO4 bolometer pre-study, arXiv 2505.01961 (2025) | fails | 2: Li-7 (I = 3/2, 92.5%) and Mo-95 (I = 5/2, 15.9%) on non-cubic sites (trigonal) |
| C6 | Gusev et al., Phys. Solid State 57, 1917 (2015), DOI 10.1134/S1063783415090097 (Ge-76) | fails | 8 with 4: range 2.5-15 K |
| C7 | H. Abe (NMIJ/AIST), Teion Kogaku 50, 314 (2015), DOI 10.2221/jcsj.50.314 (FZ Si) | fails | 8: measured 30-350 K; 9: He exchange gas in the cell |
| C8 | Li2MoO4 crystal growth, Solid State Sciences 65, 41 (2017), HAL hal-01554702 | fails | 2: as C5 |
| C9 | CaWO4 low-temperature thermal properties (1968) | fails | 8 with 4: from 5 K |
| C10 | Heat capacities of ZnS, ZnSe, CdTe below 25 K (1975) | fails | 8 with 4: from about 2 K |
| C11 | Keesom & Pearlman, Phys. Rev. 91, 1354 (1953), DOI 10.1103/PhysRev.91.1354 (KCl) | **not screened**, likely fails | paywalled; floor not stated publicly; a 1 K floor would need `L_eq` of at most 0.04 mm |
| C12 | Kirkham & Yates, Cryogenics 8, 381 (1968), DOI 10.1016/0011-2275(68)90009-X (KCl, RbCl) | **not screened** | paywalled; no range in any public record |
| C13 | W. W. Scales, Phys. Rev. 112, 49 (1958), DOI 10.1103/PhysRev.112.49 (LiF, KI) | fails | 8 with 4: range 2-7 K |
| C14 | ZnWO4 single crystal, Russ. J. Phys. Chem. A (2024) | fails | 2: Zn-67 (I = 5/2, 4.1%) on a non-cubic (monoclinic) site; also 8 (from 2.6 K) |
| C15 | Laborde et al., Phys. Rev. B 41, 9721 (1990) | fails | 1: Pd2Si, metallic |

Found but not listed as candidates by the discovery agent: diamond studies by
Desnoyers & Morrison (1958), Burk & Friedberg (1958) and DeSorbo (1953) start at
11-20 K (fail 8); Si isotope crystals, arXiv cond-mat/0412264, 20-75 K (fail 8);
Berg & Morrison (1957), alkali halides from 2.8 K (fail 8).

## Exposure log

**Assistant (analysis side):** saw bibliographic identity, materials, stated
temperature ranges, sample descriptions and access status only. No result from
any candidate reached the assistant.

**Agents (screening side):** search-engine summaries and page renderings showed
result content to the agents, which withheld it. Recorded by kind only:

1. C1 Barucci 2001: abstract statements about the fit form, a Debye temperature
   derived from the heat-capacity data, and its comparison with elastic-constant
   values; later CUORE review statements about Debye-law behaviour.
2. C2 White 1990: abstract statements of the fit form, fit range and Debye
   temperature; thermal-expansion results.
3. C7 Abe 2015: certified Si values and uncertainties (50-350 K), a sapphire
   check plot. Outside every P2 window.
4. C13 Scales 1958: a Debye temperature for one material and statements about the
   temperature dependence. C13 fails criterion 8.
5. C3, C4, C9, C10, C11, the diamond papers and Berg & Morrison: the discovery
   agent marked these exposed through search summaries, content unspecified.

The C1 exposure does not concern the predicted band directly, but it means a
Debye temperature fitted to C1's own data is known to the screening agent.
Criterion 7 already forbids using it: C1's baseline must come from elastic
constants or sound velocities, or from the registered fit window.

## Coverage limits

Twenty-two web searches; detector-crystal literature (CUORE, CRESST, CUPID,
EDELWEISS, SuperCDMS) is under-represented beyond what the searches reached.
The pre-1980 Phys. Rev. literature is paywalled from here. Theses and
collaboration technical notes, where sub-kelvin crystal calorimetry is most
likely to be tabulated, were not searched systematically.

## Still required

1. **C1 full text.** Obtain Barucci et al. (2001) through library access or from
   the authors. A methods-only reader then answers criteria 1-9. If it
   qualifies, the researcher is shown its reference only and declares whether it
   is recognised (addendum 1, rule E-b) before any data are opened.
2. **Wider search**, preferably with library access, using
   `docs/P1_SEARCH_BRIEF.md` adapted to P2's criteria, extended to detector
   collaboration theses and technical notes.
3. Optionally, C3, C11 and C12 full texts, to close them formally.
