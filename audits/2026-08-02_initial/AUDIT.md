# E3 / Bruno Constant Corpus Audit

**Date:** 2026-08-02
**Scope:** `/home/winnay/Documents/Codex/E3_Engine` — 41 GB, 308,033 files, 18,575 directories
**Method:** mechanical extraction over a deduplicated 613-file working set; no bulk file reading
**Reproduce:** `extract.py`, `verify.py`, `verify2.py`, `classify.py` (see [Artifacts](#artifacts))

---

## Executive summary

Three findings, in order of importance.

### 1. The GW150914 "independent validation" is not independent. It cannot be.

The derivation is κ = 3/(R_s · T_H), using the Schwarzschild radius and Hawking
temperature of the GW150914 remnant. Substituting the standard formulas:

```
R_s · T_H = (2GM/c²) · (ħc³ / (8πGMk_B)) = ħc / (4πk_B)
```

**The mass cancels identically.** R_s · T_H is the same number for a 1 M☉ black
hole, a 62 M☉ black hole, and a 10⁹ M☉ black hole — verified numerically across
six decades of mass in `verify2.py`, all returning κ = 16463.3245 to ten
significant figures.

The calculation therefore contains **zero observational content**. Plugging in
LIGO's measured remnant mass is arithmetically irrelevant; any mass gives the
same answer. This is not a data-quality problem that better measurements would
fix — the quantity being computed is a combination of ħ, c, and k_B wearing a
black hole as a costume.

### 2. κ = 1366 exists only because of an arithmetic error.

The notes record T_H = 1.2 × 10⁻⁸ K for a 62 M☉ remnant. The correct value is:

```
T_H = ħc³/(8πGMk_B) = 9.9517 × 10⁻¹⁰ K
```

The recorded value is **12.06× too high**. It propagates directly into κ:

| Quantity | Using claimed T_H | Using correct T_H |
|---|---|---|
| κ = 3/(R_s·T_H) | **1366.1 K⁻¹** | **16463.3 K⁻¹** |

Correcting the temperature does not repair the derivation — it moves κ to 16463,
which agrees with nothing else in the corpus. **κ = 1366 is an artifact of the
error and does not survive its correction.**

*Probable origin:* T_H = 1.2 × 10⁻⁸ K is the Hawking temperature of a **5.14 M☉**
black hole (`verify.py`). At M = 5 M☉ the formula returns 1.234 × 10⁻⁸ K. The
figure appears to be a temperature computed for a ~5 M☉ object, paired with a
Schwarzschild radius computed for the 62 M☉ GW150914 remnant — two different
black holes combined in one equation.

### 3. The authoritative document reaches the wrong conclusion, and reverses the correct one.

`CLEAN_WORKSPACE/BRUNO_CONSTANT_FINAL_ANALYSIS.md` declares κ = 1366 K⁻¹
"DEFINITIVE" and instructs that κ = 1313 be removed as a "Theoretical Planck
value, superseded" (lines 82–97). Its stated reason is that the GW150914 route is
"MOST RELIABLE" because it uses "direct observational data from LIGO" (lines
66–71).

That reasoning is exactly inverted:

- The GW150914 route uses **no** observational data — the mass cancels (Finding 1).
- Its numerical value depends on an error 12× in size (Finding 2).
- The Planck route it dismisses is the one that **reproduces**: κ = 3/(l_P·T_P)
  = 3k_B/(ħc) = **1310.11 K⁻¹**, within 0.22% of the recorded 1313
  (`verify.py`). The residual is consistent with rounding in intermediate steps.

The two derivations are the same expression differing by exactly 4π:

```
κ_Planck = 3k_B/(ħc)        = 1310.11
κ_GW     = 12πk_B/(ħc)      = 16463.32
ratio    = 4π               = 12.5663706144  (exact, not fitted)
```

**Recommendation:** κ = 1313 (properly 1310.11) is the only value in the corpus
that is reproducible from its stated definition. `BRUNO_CONSTANT_FINAL_ANALYSIS.md`
should be retracted, not merely corrected — its central claim is backwards.

### Caveat that outranks all of the above

`test_bruno_constant.py:115-139` already records a dimensional inconsistency, and
it is correct:

```
β_B = A/V = 3/R = κ·T
[3/R] = length⁻¹        [κ·T] = K⁻¹·K = dimensionless
```

These cannot be equal. Because the equation is dimensionally unbalanced, κ's
numerical value **depends on the length unit chosen**. Computing R_s in kilometres
instead of metres changes κ by a factor of 1000 (`verify.py`). "κ = 1310 K⁻¹" is
therefore not a determinate physical claim — it is 1310 *per metre-kelvin*, and
the choice of metre is doing unacknowledged work.

Selecting 1313 over 1366 is thus the right call **within** the framework's own
terms, but it does not rescue the framework. The dimensional defect must be
resolved before any κ value means anything.

---

## Constants inventory

689 constant assignments extracted from 613 unique files. Values below are
clustered per symbol; file:line citations are in `constants_inventory.tsv`.

### Standard physical constants — consistent

| Symbol | Value | Files | CODATA 2018 | Verdict |
|---|---|---|---|---|
| `G` | 6.67430e-11 | 87 | 6.67430e-11 | ✅ exact |
| `G` | 6.67e-11 | 1 | — | ⚠️ low precision, 1 file |
| `c` | 299792458 | 57 | 299792458 | ✅ exact |
| `c` | 2.99792458e8 | 6 | — | ✅ equivalent |
| `c` | 3.0e8 / 3e8 | 40 | — | ⚠️ 0.07% approximation |
| `k_B` | 1.380649e-23 | 79 | 1.380649e-23 | ✅ exact |
| `k_B` | 1.381e-23 | 1 | — | ⚠️ rounded |
| `hbar` | 1.054571817e-34 | 45 | 1.054571817e-34 | ✅ exact |
| `hbar` | 1.0545718e-34 | 10 | — | ✅ rounded, harmless |
| `h` | 6.62607015e-34 | 19 | 6.62607015e-34 | ✅ exact |
| `M_sun` | 1.98847e30 | 18 | 1.98847e30 | ✅ current |
| `M_sun` | 1.989e30 / 1.9885e30 | 9 | — | ⚠️ older value, 0.03% |
| `sigma_SB` | 5.670374419e-8 | 11 | 5.670374419e-8 | ✅ exact |
| `l_planck` | 1.616255e-35 | 6 | 1.616255e-35 | ✅ exact |
| `m_e` | 9.1093837015e-31 | 2 | 9.1093837015e-31 | ✅ exact |
| `m_p` | 1.67262192369e-27 | 1 | 1.67262192369e-27 | ✅ exact |
| `m_p` | 1.6726219e-27 | 2 | — | ✅ rounded |

**No standard constant disagrees beyond rounding.** The `3.0e8` approximation for
`c` in 40 files is the only one large enough to matter (0.07%), and only where
precision claims exceed three significant figures.

### κ — the contested symbol

| Value | Files | Meaning | Status |
|---|---|---|---|
| **1313** | 19 | Planck route, 3/(l_P·T_P) | ✅ reproducible (computes to 1310.11) |
| **1366** | 22 | GW150914 route | ❌ artifact of 12× T_H error |
| 0.001005 | 6 | "GW strain κ" | ⚠️ different quantity, same name |
| 1340e-6 | 1 | "laboratory κ_lab", units K⁻¹s⁻¹ | ⚠️ different units, unresolved |
| 1.0e-23 | 1 | toy emergent-gravity model | ⚠️ unrelated use |

Six values spanning ~26 orders of magnitude share one symbol. At minimum,
`0.001005`, `1340e-6`, and `1.0e-23` are **different physical quantities** that
should never have been named κ. `BRUNO_CONSTANT_FINAL_ANALYSIS.md:45-60`
identifies the units problem with `κ_lab` correctly.

### Files asserting both 1313 and 1366

Four notebooks assign **both** values, 1366 at early cell lines and 1313 later:

| File | 1366 at lines | 1313 at lines |
|---|---|---|
| `notebooks/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb` | 5, 45, 57, 118, 166 | 182, 244, 419 |
| `notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb` | 14, 63, 80, 152, 213 | 233, 310, 525 |
| `notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb` | 14, 63, 80, 152, 213 | 233, 310, 525 |
| `notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb` | 10, 54, 68, 130, 179 | 197, 260, 438 |

The ordering is consistent: **1366 always precedes 1313 within a file.** This is a
mid-notebook revision, not two competing camps. Any run of these notebooks
produces results from whichever definition executed last — results computed in
early cells use 1366, later cells use 1313, and **no notebook is internally
consistent**.

### Mislabelled variables

| File:line | Symbol | Value | Problem |
|---|---|---|---|
| `bruno-framework-clean/Scripts/Planck_Scale_Entropy.py:7` | `t_planck` | 1.416808e32 | This is the Planck **temperature** (1.417e32 K), not the Planck **time** (5.39e-44 s). Off by 76 orders of magnitude if used as a time. |

### Extraction false positives (documented, not defects)

The regex captured single-letter variables reused for unrelated purposes. Not
physics errors:

- `c = 33.3`, `c = 12.01`, `c = 2.55` — column indices / atomic masses in
  materials parsers (`comprehensive_e3_parser.py` and 6 duplicates)
- `h = 1.008`, `h = 0.18`, `h = 11.11` — hydrogen atomic mass, step sizes
- `sigma_SB = 0.01` — Gaussian width in
  `notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb`

---

## Disagreement register

| # | Conflict | Evidence | Verdict | Confidence |
|---|---|---|---|---|
| 1 | κ = 1313 vs 1366 | `verify.py`, `verify2.py` | **1313** (=1310.11). 1366 is an error artifact. | High — algebraic, not statistical |
| 2 | T_H = 1.2e-8 K vs 9.95e-10 K | `verify.py` | Recorded value 12.06× too high; matches a 5.14 M☉ object, not 62 M☉ | High |
| 3 | GW150914 = "independent validation" | `verify2.py` | **False.** Mass cancels; no observational content | Certain — exact cancellation |
| 4 | β_B = 3/R = κ·T | `test_bruno_constant.py:115` | Dimensionally inconsistent; κ unit-dependent | Certain |
| 5 | κ_lab units K⁻¹s⁻¹ vs K⁻¹ | `BRUNO_CONSTANT_FINAL_ANALYSIS.md:45` | Unresolved — no derivation found in corpus | Low — insufficient evidence |
| 6 | κ = 0.001005 ("GW strain") | 6 files | Different quantity sharing a name; not comparable to 1313/1366 | Medium |
| 7 | `t_planck` = 1.417e32 | `Planck_Scale_Entropy.py:7` | Planck temperature mislabelled as time | High |

---

## File disposition

All 2,408 core authored files (`.py`, `.ipynb`, `.md`, `.tex`), classified. Totals
reconcile exactly; 5/5 random duplicate assertions re-verified by `md5sum`.

| Class | Count | Definition |
|---|---|---|
| **Canonical (live)** | 145 | Best copy, in a current tree, referenced or documentary |
| **Superseded** | 69 | Best copy but in an `archive/`, `legacy/`, `rev*/`, `phase*/` path |
| **Orphan** | 399 | Unique content, imported by nothing, in no current tree |
| **Duplicate** | 1,622 | Byte-identical to a canonical copy |
| **Empty** | 173 | Zero bytes |
| **Total** | **2,408** | |

- Unique contents: **613** (145 + 69 + 399)
- **67% of core files are byte-identical duplicates.** Deleting them recovers
  3.4 MB of source and removes 1,622 opportunities for the versions to drift.
- **399 orphans** is the dominant category — most unique work in this corpus is
  referenced by nothing.

Full listings: `cls_canonical.txt`, `cls_superseded.txt`, `cls_orphan.txt`,
`cls_duplicate.tsv`.

### Corpus shape

The 41 GB is almost entirely non-authored content:

| Path | Contents |
|---|---|
| `E3_DAVP_Pipeline/davp_env` | 29,117 `.py`, 29,115 `.pyc`, 18,474 `.h` — vendored virtualenv |
| `Bruno_Entropy_Project/bruno_env` | 13,039 `.py`, 14,422 `.pyc`, 9,213 `.h` — vendored virtualenv |
| `Bruno_Entropy_Project/datasets` | 94,443 `.json` — dataset dump |

**42,156 of 43,790 `.py` files (96%) are third-party library code.** Both
virtualenvs should be deleted and rebuilt from a `requirements.txt`.

**124 directories** carry version/duplication naming (`rev1`, `rework1-5`,
`phase1-3`, `Archive`, `Final`, `legacy_import`, `dupe_archive_cleanup/_dedup/_final`,
`New folder`, `OLD_MESSY`, `RESTRUCTURED`, `CURRENT_PRODUCTION`, `CLEAN_*`).
Nesting is recursive — `CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/`
contains its own `legacy_import/dupe_archive_final/`.

⚠️ **Directory names are not reliable here.** `CLEAN_`, `Final`, and
`CURRENT_PRODUCTION` label trees that are in several cases older than what they
supersede. The classification above uses content hashes and path structure, not
names — treat any name-based intuition about which tree is current as unverified.

### Recommended canonical trees

One survivor per component. **Recommendations only — nothing has been deleted.**

| Component | Keep | Drop |
|---|---|---|
| Engine core | `E3_CURRENT_PRODUCTION/e3_engine/` | 10 identical copies in `E3_Project`, `E3_Project_REBUILT`, `CLEAN_WORKSPACE`, `github_repos` |
| Notebooks | `notebooks/` | `notebooks/archive/`, `Bruno_Entropy_Project/notebooks/`, per-project copies |
| Research history | `CLEAN_WORKSPACE/archived_research/` (one copy) | `bruno-collapse-backup` vs `bruno-collapse-unified` — two 845-file `.git` clones of the same tree |
| Papers | `bruno-framework-clean/Entropy_Hypothesis_History/` | 14 further copies of `quantum_entropy.tex` |
| Environments | none — rebuild from requirements | `davp_env`, `bruno_env` (~40 GB) |

---

## Open questions the corpus cannot settle

1. **What is β_B actually meant to be?** Until the dimensional inconsistency in
   `β_B = A/V = 3/R = κ·T` is resolved, no κ value is well-defined. This is the
   blocking question; everything else is downstream.
2. **Is there a real derivation of κ = 1313, or is 3/(l_P·T_P) a post-hoc fit?**
   The expression reduces to 3k_B/(ħc) — the "3" is unexplained anywhere in the
   corpus. Where does it come from?
3. **What is κ_lab = 1340 ± 60 × 10⁻⁶ K⁻¹s⁻¹?** No derivation or experimental
   method appears anywhere. Its units differ from every other κ. If this is a
   real measurement, its source is outside this corpus.
4. **Is κ = 0.001005 ("GW strain κ") related to the others at all,** or is it an
   unrelated quantity that inherited the name?
5. **Which materials dataset backs the "100+ materials" validation claim** in
   `BRUNO_CONSTANT_FINAL_ANALYSIS.md:90`? Given Finding 1, whatever it validated
   was not a black-hole-derived constant.

---

## Artifacts

Reproduction scripts and machine-generated tables:
`/tmp/claude-1000/-home-winnay-Documents-Codex-E3-Engine/da6cb24a-56a3-46f8-afb7-5ecfd53a1646/scratchpad/`

| File | Purpose |
|---|---|
| `extract.py` | Phase 2 extraction over the 613-file set |
| `verify.py` | Recomputes both κ derivations from CODATA 2018 |
| `verify2.py` | Demonstrates mass-independence of the GW route |
| `classify.py` | File classification |
| `constants_inventory.tsv` | 689 rows: file, line, symbol, literal, expression |
| `equations_inventory.tsv` | 121 rows: file, line, symbol, RHS |
| `kappa_hits.tsv` | 151 rows: every 1313/1366 occurrence with context |
| `cls_*.txt` / `cls_duplicate.tsv` | File disposition listings |
| `unique_core.txt` | The 613-file deduplicated working set |

**Reproduce:** `python3 extract.py && python3 verify.py && python3 verify2.py && python3 classify.py`

Every claim above carries a `file:line` citation or a named script. No file was
deleted, moved, or modified in producing this audit.
