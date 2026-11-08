# P1 literature search brief (for the researcher)

**Purpose:** find existing aluminium heat-capacity data that could test the
registered prediction P1, without seeing their results first. Anything found
goes into a P1 addendum **before** anyone looks at the data.

## 1. Before you start

- **Declare what you have already seen.** List every aluminium heat-capacity
  dataset or plot, other than Phillips (1959), that you remember seeing,
  even vaguely. Those are excluded from testing P1.
- **Keep a log** (section 5) from the first search on.

## 2. How to read without seeing results

1. Do **not** read abstracts, conclusions or figure captions. They usually state
   the results.
2. Go straight to the **experimental / sample / apparatus** section.
3. When a page shows a heat-capacity plot or table of values, **look away or
   scroll past**. You only need to know whether a table exists, not what is in it.
4. If you see a result by accident, keep going, but write it down in the log.
   An honest exposure log keeps the test valid.

## 3. Where and what to search

**Search terms** (combine freely):
`aluminum` / `aluminium`, `specific heat` / `heat capacity`, `superconducting`
/ `superconductor`, `low temperature`, `below 1 K`, `millikelvin`,
`adiabatic demagnetization`, `dilution refrigerator`, `calorimetry`.

**Where to look:**

| Source | Years most likely | Notes |
|---|---|---|
| Physical Review / Phys. Rev. B | 1950-1985 | APS; needs library access |
| Z. Naturforsch. A | 1955-1975 | includes the unscreened 1963 paper (below) |
| J. Low Temp. Phys. | 1969 onwards | Springer |
| Cryogenics | 1960 onwards | Elsevier |
| Physica, Phys. Lett., Proc. Roy. Soc. A | 1950-1980 | |
| Sov. Phys. JETP (English translation) | 1955-1980 | |
| Theses (ProQuest, university repositories) | any | often hold full data tables |
| OSTI, NBS/NIST technical reports | any | government lab calorimetry |

**Start with the two candidates already found but not readable from here:**

- Z. Naturforsch. A 18 (1963), "Specific Heat of Aluminum Near its
  Superconductive Transition Point", DOI 10.1515/zna-1963-0205
- Phys. Rev. 76, 1324 (1949), "Some Properties of Superconductors below 1 K.
  II. Aluminum and Zinc"

**Already screened, no need to repeat:** arXiv cond-mat/0311587, arXiv 2407.01434,
arXiv 2404.19352, the Hopkins thesis (Illinois), Keesom (1937), DTIC AD0645738
(see `docs/PREREGISTRATION_P1_ADDENDUM_1.md`).

## 4. Checklist for each candidate

A paper qualifies only if **every** answer is yes.

| # | Question | Where to find it |
|---|---|---|
| 1 | Elemental aluminium, purity at least 99.99%? | sample section |
| 2 | Bulk sample, every dimension at least 10 um (no films or powders)? | sample section |
| 3 | Superconducting-state data in **zero** applied field, with leftover field stated or bounded at no more than 1 mT? | apparatus section |
| 4 | Numbers given as a table or data file (not only a plot), with uncertainties? | check that a table **exists**; do not read it |
| 5 | Addenda (holder, thermometer) subtracted, and the correction described? | method section |
| 6 | Sample dimensions or shape and mass given, so surface/volume can be computed? | sample section |
| 7 | Normal-state gamma, Tc and Debye temperature reported for the same sample? | yes/no only |
| 8 | Data reach down to about 0.15-0.2 K (depends on sample size)? | the stated temperature range |
| — | No exchange gas during the low-temperature measurements? | apparatus section |

If you are unsure about item 8, note the stated range and the sample size. The
exact window is computed from them later.

## 5. What to send back

For each paper looked at, one row:

| Reference (authors, journal, year, DOI) | Answers to 1-8 + exchange gas (yes / no / not stated) | Sample size and stated temperature range | How far you read | Results seen by accident (or "none") |
|---|---|---|---|---|

Plus your declaration from section 1. These go into
`docs/PREREGISTRATION_P1_ADDENDUM_2.md`, and only then is any qualifying dataset
opened and analysed with the frozen code.
