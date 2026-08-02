# Bruno / E3 — Full Corpus Audit

**Date:** 2026-08-02
**Corpus:** `/home/winnay/Documents/Codex/E3_Engine` — 41 GB · 308,033 files · 18,575 directories
**Working set:** 613 unique-content authored files (572 after normalizing line endings)
**Method:** shell inventory → grep sweeps → mechanical extraction → independent recomputation
**Supersedes:** `AUDIT.md` (Phase 3 only) and `CLEAN_WORKSPACE/BRUNO_CONSTANT_FINAL_ANALYSIS.md` (see §1.3)

Every numeric claim below was recomputed from a stated formula. No comment,
docstring, or README assertion was taken on trust.

---

## Executive summary

Five findings, in order of consequence.

1. **The governing equation is dimensionally inconsistent.** `β_B = A/V = 3/R = κ·T`
   has m⁻¹ on the left and a dimensionless quantity on the right. κ therefore
   tracks the length unit — 164.6 in centimetres, 16,463 in metres, 16.5 million
   in kilometres. **No κ value is determinate until this is fixed.** Everything
   below is conditional on it.

2. **The GW150914 "independent validation" cannot be independent.** `R_s · T_H`
   reduces to `ħc/(4πk_B)` — the mass cancels identically. Verified across six
   decades of black-hole mass: κ = 16463.3245 every time, to ten significant
   figures. The calculation contains zero observational content.

3. **κ = 1366 is an artifact of a 12× arithmetic error** and does not survive its
   correction. **κ = 1313 is the only value in the corpus reproducible from its
   stated formula** (computes to 1310.11, +0.22%).

4. **The production engine never used either value.** 32 files across
   `E3_CURRENT_PRODUCTION`, `CLEAN_WORKSPACE`, and `E3_Project` carry
   `self.bruno_constant = 1.23456789e-23` — a keyboard-walk placeholder, baked
   into serialized model JSON.

5. **67% of authored files are byte-identical duplicates**, and one entire tree
   (`Entropy-Collapse-Research-main`, 111 `.py` files) is **hollow — every file
   zero bytes**.

6. **The only pipeline ever run against real observational data (204 real
   LIGO events) used neither audited κ candidate.** It chains an
   admitted-empirical `1e23` strain-to-temperature scale factor to
   κ = 0.001005 — a value imported from an unrelated context — producing
   collapse-point counts with no stated derivation. See §6.

---

## 1. Constant-by-constant table

### 1.1 Defined constants — exact by definition, not recomputable

Since the 2019 SI redefinition these *define* the metre, kilogram and kelvin.
A "disagreement" is a rounded transcription, not a physics error.

| Symbol | Repo value | Files | Independent | Verdict |
|---|---|---:|---|---|
| `c` | `299792458` | 57 | 299792458 m/s (exact) | ✅ exact |
| `c` | `2.99792458e8` | 6 | — | ✅ equivalent |
| `c` | `3.0e8` / `3e8` | **40** | — | ⚠️ **+0.069%** |
| `k_B` | `1.380649e-23` | 79 | 1.380649e-23 J/K (exact) | ✅ exact |
| `k_B` | `1.381e-23` | 1 | — | ⚠️ +0.025% |
| `h` | `6.62607015e-34` | 19 | 6.62607015e-34 J·s (exact) | ✅ exact |
| `hbar` | `1.054571817e-34` | 45 | h/2π = 1.054571818e-34 | ✅ exact |
| `hbar` | `1.0545718e-34` | 10 | — | ✅ rounding |

> `c = 3.0e8` in **40 files** is the only one large enough to matter. Acceptable
> for order-of-magnitude work; **not** for any result quoted to four significant
> figures — which includes every κ figure in this corpus.

### 1.2 Measured constants — checked against CODATA 2018 / IAU

| Symbol | Repo value | Files | Independent | Verdict |
|---|---|---:|---|---|
| `G` | `6.67430e-11` | 87 | 6.67430(15)e-11 | ✅ exact |
| `G` | `6.67e-11` | 1 | — | ⚠️ −0.064% |
| `M_sun` | `1.98847e30` | 18 | 1.98847e30 (IAU) | ✅ exact |
| `M_sun` | `1.9885e30` | 3 | — | ✅ rounding |
| `M_sun` | `1.989e30` | 6 | — | ⚠️ +0.027% |
| `m_p` | `1.67262192369e-27` | 1 | CODATA 2018 | ✅ exact |
| `m_p` | `1.6726219e-27` | 2 | — | ✅ rounding |
| `m_e` | `9.1093837015e-31` | 2 | CODATA 2018 | ✅ exact |
| `sigma_SB` | `5.670374419e-8` | 11 | CODATA 2018 | ✅ exact |

### 1.3 Derived quantities — recomputed from formula

| Quantity | Formula | Independent | Repo | Verdict |
|---|---|---|---|---|
| `l_P` | √(ħG/c³) | 1.616255024e-35 m | `1.616255e-35` (36 files) | ✅ |
| `m_P` | √(ħc/G) | 2.176434e-8 kg | `2.17651e-8` (15 files) | ⚠️ stale |
| `T_P` | √(ħc⁵/G)/k_B | 1.416784e32 K | `1.416808e32` (7 files) | ⚠️ stale |
| `R_s` | 2GM/c² (62 M☉) | 183,107 m | `183000` | ✅ −0.06% |
| `T_H` | ħc³/(8πGMk_B) | **9.9517e-10 K** | `1.2e-8 K` | ❌ **+1106%** |
| `S_BH` | k_Bc³A/(4Għ) | **5.567e57 J/K** | `7.0095e54` | ❌ **−99.87%** |

**Three mismatched masses.** The corpus pairs quantities computed for different
objects:

| Recorded value | Object it actually describes |
|---|---|
| `R_s = 183,000 m` | 62 M☉ ✅ |
| `T_H = 1.2e-8 K` | **5.14 M☉** |
| `S_bh = 7.0095e54` | **2.20 M☉** |

### 1.4 κ — all six values

Framework's own definition: `β_B = A/V = 3/R = κ·T`

| Value | Files | Route | Independent | Verdict |
|---|---:|---|---|---|
| **1313** | 19 | 3/(l_P·T_P) = 3k_B/(ħc) | **1310.11** | ✅ **+0.22% — reproducible** |
| 1366 | 22 | 3/(R_s·T_H), bad T_H | 16463.32 | ❌ **−91.7%** — error artifact |
| 0.001005 | 6 | "Chajar Constant" | — | ⚠️ **dimensionless multiplier**, different quantity |
| 1340e-6 | 1 | "laboratory κ_lab" | — | ⚠️ units K⁻¹s⁻¹; **no derivation exists** |
| 1.23456789e-23 | **32** | none | — | ❌ **placeholder** |
| 1.0e-23 | 1 | toy model | — | ⚠️ unrelated |

**The two routes are the same expression.**

```
κ_Planck = 3k_B/(ħc)    = 1310.11
κ_GW     = 12πk_B/(ħc)  = 16463.32
ratio    = 4π           = 12.5663706144   (exact, not fitted)
```

`R_s · T_H = ħc/(4πk_B)` — mass cancels. Confirmed numerically for
M = 1, 5, 62, 100, 10⁶, 10⁹ M☉: identical to ten significant figures.

**Why `BRUNO_CONSTANT_FINAL_ANALYSIS.md` is wrong.** It declares κ = 1366
"DEFINITIVE" and orders 1313 removed as "superseded," reasoning the GW route is
"MOST RELIABLE" because it uses "direct observational data from LIGO." Inverted
on every point: the GW route uses no observational data, its value rests on a 12×
error, and the route it dismisses is the one that reproduces. **Retract, don't
edit.**

### 1.5 κ = 0.001005 is not a rival value

Found in context (`Entropy Collapse Test 1.9.py:46-48`):

```python
k_chajar = 0.001005  # Chajar Constant: entropy tangency threshold
T_tangent = T_planck * k_chajar
```

Used as a **dimensionless multiplier of Planck temperature**, not a K⁻¹ quantity.
It is a different physical thing sharing a name. Not comparable to 1313/1366 and
should never have been counted against them.

### 1.6 Three CODATA vintages coexist

The Planck literals sit just outside what G's uncertainty permits (u_r = 2.2e-5,
halved under a square root). Too systematic for rounding — it dates them:

| Literal | Repo | Matches |
|---|---|---|
| `l_P = 1.616255e-35` | exact | **CODATA 2018** |
| `m_P = 2.17651e-8` | exact | **CODATA 2010** |
| `T_P = 1.416808e32` | exact | **CODATA 2014** |

Numerically harmless (~2e-5). Useful as a **lineage fingerprint** — more reliable
than directory names, which §3 shows cannot be trusted.

### 1.7 Mislabelled variable

| File:line | Name | Holds | Should hold |
|---|---|---|---|
| `Planck_Scale_Entropy.py:7` (+6 copies) | `t_planck` | 1.416808e32 (Planck **temperature**) | 5.391e-44 s (Planck **time**) |

Off by 2.6×10⁷⁵ if consumed as a time. Note `sim_results/bruno_universe.py`
defines `PLANCK_TIME = 5.39e-44` correctly — the two conventions coexist.

---

## 2. Equation modification log

From the `suspicious_modifications` sweep (361 lines / 19 files), plus equation
defects surfaced during Phase 4. Each recomputed.

### M-1 · Hawking temperature multiplied by dimensionless entropy

**Files (7):** `Entropy Temperature Fix.py` in `bruno-framework-clean/organized_research/thermodynamics/`, `github_repos/Entropy-Collapse-Research/Scripts/`, `Entropy-Collapse-Research/Scripts/Archive/`, `E3_Project_OLD_MESSY/archive/legacy_scripts/archive/`, and 3 copies under `CLEAN_WORKSPACE/archived_research/`

```python
T_H_eq = sp.Eq(T_H, (hbar * c**3) / (8 * pi * G * M) * (S_BH / k_B))  # Adjusted scaling
```

| | Value (62 M☉) |
|---|---|
| Standard `ħc³/(8πGMk_B)` | 9.9517e-10 K |
| As written | 5.5402e+48 |
| **Ratio** | **5.567e57** |

`S_BH/k_B` is the *dimensionless* entropy, order 10⁸⁰. Multiplying a temperature
by it is not a scaling correction. The comment "Adjusted scaling" documents no
justification. ❌ **Invalid.**

### M-2 · Bekenstein-Hawking entropy missing the factor of 4

**File:** `Entropy Blackhole Model.py:16-17` (+ copies)

```python
# Bekenstein-Hawking entropy equation for a black hole (corrected formula)
S_BH_eq = sp.Eq(S_BH, (k_B * 4 * pi * sp.Pow(r_s, 2)) / (hbar * G / c**3))
```

| | Value (62 M☉) |
|---|---|
| Standard `k_Bc³A/(4Għ)` | 5.5670e57 |
| As written | 2.2268e58 |
| **Ratio** | **exactly 4.0000** |

The `/4` in `A/4` was dropped. The comment claims "corrected formula." ❌ **4× too high.**

### M-3 · Hawking temperature missing k_B

**File:** `github_repos/Entropy-Collapse-Research/Scripts/Hawking Radiation Comparison.py`

```python
T_H_standard = [(hbar * c**3) / (8 * pi * G * M) for M in mass_values]   # no k_B
```

Returns **joules, not kelvin** — off by 1/k_B = 7.24×10²². Same file sets
`c = 3.0e8`, then adds `f_S = 1.66345592659651e-36` to the already-wrong
quantity. ❌ **Invalid.**

### M-4 · Bekenstein-Hawking entropy misassembled

**File:** `github_repos/Entropy-Collapse-Research/Scripts/Gw150914 Entropy Test.py`

```python
S = (4 * pi * G * A) / (hbar * c * kB)     # correct: k_B*c**3*A/(4*G*hbar)
```

G in the wrong position, k_B inverted. Standard 5.567e57 vs coded 8.096e50 —
**seven orders of magnitude low**, in the script computing entropy for the very
event underpinning κ = 1366. ❌ **Invalid.**

### M-5 · Undocumented additive correction `f_S`

**Files:** 2, under `github_repos/Entropy-Collapse-Research/Scripts/`

```python
f_S = 1.66345592659651e-36  # Previously computed entropy contribution
```

Added to both `T_H` and `r_s` — quantities with different dimensions. No
derivation anywhere in the corpus. ⚠️ **Not recomputable; provenance absent.**

### M-6 · Benign

`quality_flags.append(f"purity_adjusted_{purity}%")` — 15 hits, materials-parser
string label. Not an equation. ✅ No action.

---

## 3. Duplicate / orphan file map

### 3.1 Disposition of all 2,408 authored files

| Class | Count | Definition |
|---|---:|---|
| Canonical (live) | 145 | Best copy, current tree, referenced or documentary |
| Superseded | 69 | Best copy but under `archive/`, `legacy/`, `rev*/`, `phase*/` |
| **Orphan** | **399** | Unique content, imported by nothing |
| Duplicate | 1,622 | Byte-identical to a canonical copy |
| Empty | 173 | Zero bytes |
| **Total** | **2,408** | reconciles exactly; 5/5 spot-checks re-verified |

Unique contents: **613** exact-byte → **572** ignoring line endings (42 files are
CRLF/LF twins). **Deduplication must normalize line endings first** or it
preserves 42 needless copies.

### 3.2 Corpus bulk is not authored content

| Path | Contents |
|---|---|
| `E3_DAVP_Pipeline/davp_env` | 29,117 `.py` · 29,115 `.pyc` · 18,474 `.h` |
| `Bruno_Entropy_Project/bruno_env` | 13,039 `.py` · 14,422 `.pyc` · 9,213 `.h` |
| `Bruno_Entropy_Project/datasets` | 94,443 `.json` |

**42,156 of 43,790 `.py` files (96%) are third-party library code.** Delete both
virtualenvs; rebuild from `requirements.txt`. Recovers ~40 GB.

### 3.3 The hollow tree

| Tree | `.py` | empty |
|---|---:|---:|
| **`Entropy-Collapse-Research-main`** | 111 | **111** |
| `github_repos/Entropy-Collapse-Research` | 111 | 0 |
| `Entropy-Collapse-Research` | 134 | 0 |
| `bruno-framework-clean` | 114 | 0 |

Every file zero bytes — structure intact, content absent. Almost certainly a
failed clone. **441 zero-byte files** corpus-wide. **Delete; nothing is lost.**

### 3.4 Apparent drift is mostly the hollow tree

Of 233 directory pairs with ≥60% filename overlap, 72 disagreed on content:

| Cause | Pairs |
|---|---:|
| One side has empty files | 59 |
| **Genuine content drift** | **13** |

The corpus is *more* redundant than raw numbers suggest. Real forks:

- `Bruno_Entropy_Project/scripts/utilities` vs 5 trees — 8 shared, **0 identical**
- `bruno_core` in both `bruno-collapse-*` backups vs `E3_Project_OLD_MESSY` — 7 shared, 2 diverged
- Three-way fork of `scr/` **inside** `bruno-unified-rev1` alone

### 3.5 Filenames with divergent content

**77 filenames** carry more than one non-empty implementation. Worst:

| Filename | Versions | Copies | Empty | Trees |
|---|---:|---:|---:|---:|
| `README.md` | 27 | 65 | 2 | 17 |
| `data_pipeline.md` | 4 | 15 | 0 | 4 |
| `bruno_threshold.py` | 3 | 23 | 9 | 12 |
| `__init__.py` | 3 | 20 | 1 | 9 |
| `registry_logger.py` | 3 | 19 | 0 | 8 |
| `fluence_engine.py` | 2 | 23 | 9 | 12 |
| `utils.py` | 2 | 21 | 9 | 8 |

**`bruno_threshold.py` in full** — the case you flagged:

| Content | Copies | Where |
|---|---:|---|
| `02890648` (CRLF) | 9 | `E3_CURRENT_PRODUCTION`, `E3_Project`, `E3_Project_REBUILT`, `bruno-simulator-RESTRUCTURED`, `archived_research`×2, `OLD_MESSY`, `github_repos`×2 |
| `88c535c4` (LF) | 4 | `bruno-fluence-app`, `bruno-framework-clean`, `bruno-new-dataset`, `bruno-real-analyzer` |
| `4e0907a7` | **1** | `github_repos/bruno-collapse-unified/bruno_core_unified/theory/` |
| empty | 9 | `Bruno_Entropy_Project`, `CLEAN_WORKSPACE/*`×5, `github_repos/*`×2 |

First two differ **only in line endings**. The lone outlier adds:

```python
# Bruno Constant - Final experimentally validated value
BRUNO_CONSTANT_KAPPA = 1340e-6  # K⁻¹s⁻¹ (1340 ± 60 × 10⁻⁶)
```

The only named module-level κ binding in the corpus, self-described as "final" —
directly contradicting `BRUNO_CONSTANT_FINAL_ANALYSIS.md`, which calls the same
value erroneous and orders it deleted. **Two documents, each claiming finality,
each rejecting the other.**

### 3.6 Directory names are unreliable

`CLEAN_`, `Final`, `CURRENT_PRODUCTION`, `latest` label trees that are in several
cases *older* than what they claim to supersede. **124 directories** carry
version/duplication naming, nested recursively —
`CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/` contains its own
`legacy_import/dupe_archive_final/`. All classification above uses content hashes,
never names.

---

## 4. Recommended canonical source going forward

### 4.1 Constants — create one module, delete the rest

**No file in the corpus is currently fit to be canonical for constants.** The
best-populated trees carry the `1.23456789e-23` placeholder. Create:

**`e3_core/constants.py`** — single source of truth:

```python
"""Physical constants. CODATA 2018 / IAU nominal. Single source of truth.
Do not redefine these anywhere else in the codebase."""
C       = 299792458.0          # m/s        exact (2019 SI)
H       = 6.62607015e-34       # J*s        exact (2019 SI)
HBAR    = H / (2 * math.pi)    # J*s        derived
K_B     = 1.380649e-23         # J/K        exact (2019 SI)
G       = 6.67430e-11          # m^3/kg/s^2 CODATA 2018
M_SUN   = 1.98847e30           # kg         IAU nominal
SIGMA_SB= 5.670374419e-8       # W/m^2/K^4  CODATA 2018
L_PLANCK    = math.sqrt(HBAR * G / C**3)      # derive, never hardcode
M_PLANCK    = math.sqrt(HBAR * C / G)
T_PLANCK    = math.sqrt(HBAR * C**5 / G) / K_B
TIME_PLANCK = math.sqrt(HBAR * G / C**5)      # NOT T_PLANCK -- see §1.7
```

Derive Planck units rather than hardcoding — it eliminates the three-vintage
problem (§1.6) and the `t_planck` mislabel (§1.7) permanently.

**κ is deliberately absent.** It cannot be defined until §5.1 is resolved.

| Action | Target |
|---|---|
| Delete | all 32 `bruno_constant = 1.23456789e-23` sites |
| Delete | `BRUNO_CONSTANT_KAPPA = 1340e-6` (unverifiable) |
| Rename | `kappa = 0.001005` → `CHAJAR_TANGENCY` (different quantity, §1.5) |
| Replace | all 40 `c = 3.0e8` with import from `constants` |

### 4.2 Equations — one implementation each

| Equation | Canonical form | Retire |
|---|---|---|
| Hawking temperature | `T_H = HBAR*C**3/(8*pi*G*M*K_B)` | M-1, M-3 |
| Bekenstein-Hawking entropy | `S = K_B*C**3*A/(4*G*HBAR)` | M-2, M-4 |
| Schwarzschild radius | `R_s = 2*G*M/C**2` | none — already clean, 1 literal / 24 files ✅ |
| Horizon area | `A = 16*pi*(G*M/C**2)**2` | — |

Recommended home: **`e3_core/blackhole.py`**, importing only from
`e3_core/constants.py`.

### 4.3 Trees to keep

| Component | Keep | Delete |
|---|---|---|
| Engine core | `E3_CURRENT_PRODUCTION/e3_engine/` | 10 identical copies |
| Notebooks | `notebooks/` | `notebooks/archive/`, per-project copies |
| Research history | `CLEAN_WORKSPACE/archived_research/` (**one** of backup/unified) | the other 845-file clone |
| Papers | `bruno-framework-clean/Entropy_Hypothesis_History/` | 14 copies of `quantum_entropy.tex` |
| Environments | none — `requirements.txt` | `davp_env`, `bruno_env` (~40 GB) |
| — | — | `Entropy-Collapse-Research-main` (hollow) |

**Order of operations:** normalize line endings → dedupe by hash → delete hollow
tree and virtualenvs → introduce `constants.py` → migrate call sites.

---

## 5. Known gaps — follow-up manual pass required

### 5.1 The blocking question (not a gap — a prerequisite)

`β_B = A/V = 3/R = κ·T` cannot balance dimensionally. **No κ value means anything
until this is resolved.** Options: β_B is not dimensionless; `3/R` carries a
hidden length scale; or κ is not K⁻¹. The corpus does not say which. Everything
in §4.1 concerning κ is blocked on this.

### 5.2 Constants under unconventional names — value-first sweep

A keyword sweep cannot find a constant named something unexpected. I re-swept by
**value** (any `NAME = <literal>` within 0.05% of a known constant, name
ignored). Findings beyond the Phase 2 alias list:

| Constant | Alias found | Files |
|---|---|---:|
| `a_rad` (radiation density) | `a_rad`, **`a`** | 5, 3 |
| Planck mass | `planck_mass` | 3 |
| Planck time | `PLANCK_TIME` | 1 |
| Avogadro | `NA` | 2 |
| M☉ | `solar_mass_kg` | 1 |
| Parsec | `pc_to_m` | 1 |
| Elementary charge / eV | `e` | 2 |

Coverage was better than feared — no *new* contradictions. But `a` and `e` as
single letters confirm the sweep's blind spot is real.

### 5.3 Not covered — genuine gaps

| Gap | Why it matters | Suggested pass |
|---|---|---|
| **Constants in `.dat` / `.csv`** | 43,955 `.dat` + 1,884 `.csv` never swept | Sample headers for embedded parameters |
| **`Bruno_Entropy_Project/datasets`** | 94,443 JSON excluded as bulk data | Check whether any encode model parameters, as `e3_universal_thermal_model_v2_*.json` did |
| **Computed-not-assigned constants** | `kappa = 3/(l_P*T_P)` has no literal; assignment-based extraction misses it | AST parse rather than regex |
| **In-notebook execution outputs** | κ may appear in stored cell *outputs*, not source | Parse `outputs[].text` in 263 `.ipynb` |
| **LaTeX-only equations** | 47 unique `.tex` files; sweep caught assignments, not `\begin{equation}` bodies | Manual read of the 5 `Bruno_model_sim*.tex` |
| **The 16 `.git` histories** | Could date the 1366→1313 transition definitively | `git log -S 1366` per repo |
| **`f_S = 1.66e-36`** | Undocumented, applied to two different dimensions | Locate original derivation or delete |
| **`κ_lab = 1340 ± 60 × 10⁻⁶`** | Only claimed *measurement* in the corpus; no method recorded | Source lies outside this corpus |

### 5.4 Methodological caveats

- **Duplicate inflation.** Wide sweeps (§2) ran over all non-noise files, not the
  613-file unique set. Raw line counts overstate by ~4×; distinct-file and
  unique-content columns are the reliable ones.
- **Empty files distort name-based comparison.** 441 zero-byte files made 59 of
  72 directory pairs look "drifted" when one side simply had no content.
- **One correction to an earlier pass.** I initially reported "no named `KAPPA`
  constant exists" — the pattern required a trailing underscore and missed suffix
  forms. Case-sensitive re-sweep found `KAPPA = 1366` (2 files) and
  `BRUNO_CONSTANT_KAPPA = 1340e-6` (1 file).
- **Directory names are not evidence.** See §3.6.

---

## 6. Addendum — the only pipeline run against real observational data used neither audited κ candidate

Found via `Bruno-Unified-Research` (a separate bundle covering
`bruno-collapse-unified` + `bruno-collapse-simulator`, ~1.3 GB uncompressed,
545 MB zipped). 91% of its authored code (472/518 files) is byte-identical to
what's already covered above; this section documents the part that wasn't.

### 6.1 What was found

`bruno-collapse-simulator/notebooks/e3_core/nb04_gw_corrmap.ipynb` and
`nb05_GW_Batch_AutoRun.ipynb` are the only code in either corpus that was run
against real gravitational-wave strain data — 204 real LIGO events (150914,
190413, 190421, 200114, and 200 others), producing
`bruno_collapse_summary.csv` and one `*_bruno_betaB.png` plot per event.

The computation:

```python
kappa = 0.001005  # Entropy collapse threshold factor (dimensionless)

# NOTE: The 1e23 scale factor is empirical; refine based on future calibration
T_h1 = cp.abs(strain_h1) * 1e23
T_l1 = cp.abs(strain_l1) * 1e23

beta_h1 = kappa * T_h1   # β_B = κ × T
beta_l1 = kappa * T_l1
# collapse flagged wherever β_B >= 1
```

Sample notebook output: *"β_B computed for both detectors using kappa =
0.001005 — H1 collapse points detected: 16378, L1 collapse points detected:
16378."*

### 6.2 Why this doesn't hold up

Two chained, undeclared scale factors, neither derived:

1. **`1e23` strain-to-temperature conversion.** Raw GW strain is a
   dimensionless ratio, O(10⁻²¹). Multiplying by `1e23` produces a number in
   a temperature-like range, but the notebook's own comment admits it is
   *empirical* and awaiting *future calibration* — i.e., chosen to land in a
   plausible-looking range, not derived from physics.
2. **`kappa = 0.001005`.** This is the value documented in §1.5 above as the
   "Chajar Constant" — a dimensionless Planck-temperature tangency multiplier
   from an unrelated origin file (`Bruno Constant.py`,
   `Entropy-Collapse-Research` repo). Nothing in either notebook derives or
   justifies applying it to gravitational-wave strain. It is neither of the
   two values (1313, 1366) that received all prior scrutiny.

The reported collapse counts (e.g. 16,378) are therefore the number of time
samples where `κ × (|strain| × 1e23) ≥ 1` — a threshold crossing of a product
of two unexplained numbers, not a physical measurement. It carries the
precision and framing of a detection count without the derivation to support
that framing.

### 6.3 Why this outranks the 1313/1366 dispute in one respect

Findings 1–5 concern which candidate κ value, if any, is defensible. This
finding shows that the one place the framework was actually run against real
observational data used **none of the audited candidates** — a third,
unrelated value, chained to an admittedly-empirical scale factor. Any claim
that the framework has been "tested against real GW events" should be read
as: tested using this pipeline, with this undocumented scaling, not as
validation of κ = 1313 or 1366.

### 6.4 Recommendation

- Do not cite `bruno_collapse_summary.csv` or the 204 `*_bruno_betaB.png`
  plots as validation evidence until both the `1e23` conversion and the
  choice of κ = 0.001005 in this context have a stated derivation.
- If revisited, treat as a new derivation task, not a bug fix — there is no
  "correct" version of this calculation on file anywhere in either corpus;
  the scale factor is admitted-empirical from the start.

---

## Reproduction

Scripts and machine-generated tables in
`/tmp/claude-1000/-home-winnay-Documents-Codex-E3-Engine/da6cb24a-56a3-46f8-afb7-5ecfd53a1646/scratchpad/`
and `/tmp/audit/`. **Both are session-scratch and will not survive a reboot —
copy them into the repo if this audit needs to be re-runnable.**

| Script | Produces |
|---|---|
| `extract.py` | `constants_inventory.tsv` (689 rows), `equations_inventory.tsv` (121), `kappa_hits.tsv` (151) |
| `verify.py` | Both κ derivations from CODATA 2018 |
| `verify2.py` | Mass-independence proof of the GW route |
| `classify.py` | `cls_canonical.txt`, `cls_superseded.txt`, `cls_orphan.txt`, `cls_duplicate.tsv` |
| `value_table.py` | `/tmp/audit/VALUE_TABLE.md` |
| `phase4.py` | `/tmp/audit/FOLDER_AUDIT.md` |
| `phase5_recompute.py` | `/tmp/audit/RECOMPUTE.txt` |
| `gap_check.py` | `/tmp/audit/GAP_CHECK.txt` |

```
python3 extract.py && python3 verify.py && python3 verify2.py \
  && python3 classify.py && python3 value_table.py \
  && python3 phase4.py && python3 phase5_recompute.py && python3 gap_check.py
```

No file was deleted, moved, or modified in producing this audit. All deletions
recommended above are **recommendations only**.
