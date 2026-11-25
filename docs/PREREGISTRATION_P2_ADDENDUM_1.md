# Pre-registration P2, addendum 1: registration commit and researcher declaration

**Date:** 2026-11-25. This addendum changes nothing in the hypothesis, criteria
or falsifiers of `docs/PREREGISTRATION_P2.md`. It identifies the registration
commit and records the researcher's declaration of previously seen data
(section 2, exclusion rule; section 7, step 1). It is committed **before** any
search for P2 data is run.

## 1. Registration commit

- **Commit:** `55b8f8dfe73b4843b1b47a35158efce194002959` ("Register
  pre-registration P2"), merged to `main` via PR #1 (`80bc8a0`).
- **Commit timestamp:** 2026-11-08T15:06:34+00:00.
- No `p2-registered` tag exists. The commit hash is the authoritative identifier.
- **Frozen inputs re-checked 2026-11-25:** all eight files listed in section 6 of
  the registration still match their registered SHA-256 hashes.

## 2. Researcher declaration (previously seen data)

Collected 2026-11-25 by the assistant, by direct question.

1. **Insulating-crystal heat-capacity data seen outside the repository:** yes,
   vaguely; the researcher cannot recall specifics (material, source or date).
2. **Old E3 corpus.** The 2026-08-02 corpus file list
   (`audits/2026-08-02_initial/raw/all_files.txt.gz`) contains a
   `debye_test_data.json` in five copies (`E3_Project/data/validation/`,
   `E3_Project_REBUILT/data/validation/`, `E3_CURRENT_PRODUCTION/data/validation/`,
   `github_repos/E3_Project/data/validation/`, `E3_DAVP_Pipeline/`). Its
   contents were **not opened** by the assistant. It is **presumed seen** by the
   researcher.
3. **Shen (1965), UCRL-16117, Part II (CrBr3):** not seen; only the niobium
   figures were viewed. (CrBr3 is magnetic and would fail inclusion criterion 3
   in any case.)
4. **Repository contents:** no insulating-crystal heat-capacity data are held in
   this repository (`reference/`, `data/provenance/`, `data/raw/` hold
   aluminium, niobium and lead material only).

## 3. Exclusion rules adopted for screening

Because item 1 is non-specific:

- **E-a.** Any dataset whose source is, or traces back to,
  `debye_test_data.json` in the old corpus is excluded.
- **E-b.** When the qualifying list is presented, the researcher is shown only
  the reference (authors, journal, year, title) of each candidate, never its
  data, and declares for each whether it is recognised. Recognised candidates
  are excluded and the decision is recorded in the screening addendum, before
  any data are opened.
- **E-c.** The assistant's own training prior (declared in the registration's
  blindness statement) does not count as having seen a specific dataset, but
  any specific result the assistant sees during screening is entered in the
  exposure log.

## 4. Next

Blind, methods-only screening (section 7, step 2). Its result, the qualifying
list and the exposure log go in `docs/PREREGISTRATION_P2_ADDENDUM_2.md`.
