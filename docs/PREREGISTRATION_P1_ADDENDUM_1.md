# Pre-registration P1, addendum 1: data screening

**Date:** 2026-11-08. This addendum applies section 2 of the registered
`docs/PREREGISTRATION_P1.md` (registration commit `39896da`, see addendum 0). It
does not change the hypothesis, the criteria or the falsifiers.

## Outcome

**No qualifying dataset was found.** P1 cannot be tested on the literature
screened so far. It needs either qualifying data from a wider search or a new
measurement designed to the registered criteria.

## Procedure

- Screening was done by the assistant at the researcher's request.
- Candidates were found with three neutrally worded web searches (2026-11-08).
- Each candidate was read by a separate agent instructed to report only the
  methods checklist (purity, geometry, field, temperature window, data format,
  uncertainties, addenda, gamma/Tc/Debye reported yes or no, exchange gas,
  method), and no values, fits, theory comparisons or conclusions.
- Bot checks on publisher sites were not circumvented.

## Candidates

| # | Study | Decision | Reason (registered criterion) |
|---|---|---|---|
| — | Phillips, Phys. Rev. 114, 676 (1959) | excluded | motivated P1 (exclusion rule) |
| C1 | Vector-magnet relaxation calorimetry, arXiv cond-mat/0311587 (6N polycrystalline Al, 3.9 x 3.9 x 1.9 mm, 77.9 mg) | **fails** | 4: figures only, no table or data file; 4: no per-point or per-range uncertainty; 3: residual field from a persistent-mode superconducting magnet neither stated nor bounded |
| C2 | Z. Naturforsch. A 18 (1963), DOI 10.1515/zna-1963-0205 | **not screened** | publisher returned a bot check; the title indicates measurements near the transition, which would fail 8, but this was not verified |
| C3 | Hopkins thesis, Univ. of Illinois (99.995% single-crystal sphere) | fails | 8: data range 1.06-1.19 K (from the search listing) does not reach the predicted band |
| C4 | Phys. Rev. 76, 1324 (1949), "Some properties of superconductors below 1 K. II. Aluminum and zinc" | **not screened** | publisher (APS) returned a bot check; the search listing describes it as a magnetic-threshold study, which would not be calorimetry, but this was not verified |
| C5 | Noise-thermometry calorimetry, arXiv 2407.01434 | fails | no aluminium sample (Al used only as a heat switch) |
| C6 | Keesom (1937), Al heat capacity 1.1-20 K | fails | 8: above Tc |
| C7 | Al nuclear demagnetization stage, arXiv 2404.19352 | fails | 3: measured in applied field (nuclear refrigeration) |
| C8 | Al critical field report, DTIC AD0645738 | fails | not calorimetry |

## Exposure log (results seen during screening)

Blinding was imperfect. Search-engine summaries, which the assistant saw
directly, contained these result statements:

1. Phillips (1959): the excess over the exponential at the lowest temperatures
   (already known; Phillips is excluded).
2. C1: summary-level thermodynamic parameters, and a statement that its aluminium
   data agree with BCS "across the range". C1 does not qualify, so this does not
   affect any test.
3. C7: a statement of excess heat capacity at low B/T in aluminium in applied
   field. C7 does not qualify (criterion 3).

No result from any screened paper's full text reached the assistant.

## Coverage limits

This screen is not exhaustive: three searches, eight candidates, and two papers
not accessible. Paywalled and pre-digital literature (journals of the 1950s-1970s,
theses, conference proceedings) is under-represented. Before concluding that no
literature test of P1 exists, a wider search should be done, preferably by
someone with library access, using the same methods-only rule.

## Still required before any analysis

- **Researcher declaration:** any aluminium heat-capacity dataset other than
  Phillips (1959) that the researcher has already seen. Requested 2026-11-08;
  to be recorded in the next addendum.
