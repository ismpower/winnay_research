# E3 / Bruno Constant — Audit 2026

Independent audit of the physics-framework corpus at
`/home/winnay/Documents/Codex/E3_Engine` — 41 GB, 308,033 files, 18,575
directories, accumulated across many GPT and Gemini sessions.

**Completed 2026-08-02. Read-only: nothing in the corpus was modified, moved, or
deleted.** All deletions named below are recommendations.

---

## What was asked

Inventory every physical constant, derived value, and version of each core
equation across the entire corpus; flag every disagreement; and identify which
files and folders are duplicates, orphans, or superseded.

Two problems were known going in: κ appeared as both **1313** and **1366** with
no resolution, and a claimed "independent validation" from GW150914 relied on a
Hawking temperature that looked roughly 12× too high.

Both are now resolved. The second is worse than it looked.

---

## Headline results

**1. The governing equation cannot balance dimensionally.**
`β_B = A/V = 3/R = κ·T` has m⁻¹ on the left and a dimensionless quantity on the
right. κ therefore tracks the length unit — 164.6 in centimetres, 16,463 in
metres, 16.5 million in kilometres. **No κ value is determinate until this is
resolved.** Everything below is conditional on it.

**2. The GW150914 validation contains no observational content.**
`R_s · T_H` reduces to `ħc/(4πk_B)` — the mass cancels identically. Tested across
six decades of black-hole mass: κ = 16463.3245 every time, to ten significant
figures. Plugging in LIGO's measurement is arithmetically irrelevant. It was
never capable of being an independent check.

**3. κ = 1366 is an artifact of a 12× error.**
Recorded `T_H = 1.2e-8 K`; correct value `9.9517e-10 K`. That error alone
produces 1366. Correcting it gives 16463, which agrees with nothing. The recorded
temperature is the Hawking temperature of a **5.14 M☉** black hole, paired with a
Schwarzschild radius computed for the 62 M☉ remnant.

**4. κ = 1313 is the only reproducible value.**
`3/(l_P·T_P)` = `3k_B/(ħc)` = **1310.11**, within 0.22% of the recorded figure.
The two routes are the same expression differing by exactly 4π.

**5. The production engine never used either value.**
32 files across `E3_CURRENT_PRODUCTION`, `CLEAN_WORKSPACE`, and `E3_Project`
carry `self.bruno_constant = 1.23456789e-23` — a keyboard-walk placeholder, baked
into serialized model JSON. Engine output cannot be evidence for any κ value.

**6. `BRUNO_CONSTANT_FINAL_ANALYSIS.md` is inverted on every point.**
It declares 1366 "DEFINITIVE" and orders 1313 deleted, reasoning the GW route is
more reliable because it uses observational data. The GW route uses none, its
value rests on the 12× error, and the route it dismisses is the one that
reproduces. **Retract it rather than edit it.**

**7. 67% of authored files are byte-identical duplicates**, and one entire tree
(`Entropy-Collapse-Research-main`, 111 `.py` files) is hollow — every file zero
bytes.

---

## Method

The corpus is far too large to read. The approach was to shrink it mechanically
before any file was opened, then recompute rather than trust.

### Phase 1 — Inventory without reading
`find` + `md5sum` only; no file contents examined.

Located the bulk: two vendored virtualenvs (`davp_env`, `bruno_env`) and one
dataset dump account for **96% of all `.py` files**. After excluding noise:
2,408 authored files. After content hashing: **613 unique**.

> `ripgrep` was not installed and was **not needed**. Deduplication collapsed the
> search space from 308,033 files to 613, where plain `grep` returns in under a
> second. Everything ran on stock `find`/`grep`/`md5sum`.

### Phase 2 — Keyword sweeps to disk
Eleven pattern sweeps written straight to `/tmp/audit/`, never into context.
65,178 matching lines. Counts reviewed first, contents only where warranted.

### Phase 3 — Value table
Extracted every numeric assignment, grouped **by value rather than by file**, and
annotated each group with how many *unique contents* it spans — so eight copies
of one file don't read as eight independent decisions.

This is where the branch hypothesis died: 1313 and 1366 have identical branch
lists. They coexist rather than succeed one another. Four notebooks assign
**both**, 1366 always in earlier cells and 1313 later — so no notebook is
internally consistent.

### Phase 4 — Folder-level duplicate detection
Compared filename sets across directories, using hashes only to say whether
same-named files agree. Surfaced the hollow tree, and showed that **59 of 72**
apparently-drifted directory pairs were just empty-vs-populated. Only **13** are
genuine forks.

### Phase 5 — Independent recomputation
Every disputed constant recomputed from an explicitly stated formula. No comment,
docstring, or README claim taken on trust.

One distinction shaped the results: since the 2019 SI redefinition, **c, h and
k_B are exact by definition** — they cannot be recomputed, only checked against
the definition. Only derived quantities are genuinely recomputable.

---

## What survived recomputation

| | Result |
|---|---|
| ✅ Confirmed | `G`, `M☉`, `m_p`, `m_e`, `σ_SB`, `l_P`, `R_s` — all match CODATA/IAU |
| ⚠️ Imprecise | `c = 3.0e8` in **40 files** (+0.069%) — unfit for four-significant-figure claims |
| ❌ Refuted | `T_H` (+1106%), `S_BH` (−99.87%), `κ = 1366` (−91.7%) |
| ⛔ Unverifiable | `κ = 1340e-6`, `f_S = 1.66e-36` — no derivation exists anywhere |

**Four invalid equations** found in the `suspicious_modifications` sweep, each
recomputed:

- Hawking temperature multiplied by dimensionless entropy (~10⁸⁰), commented
  *"Adjusted scaling"* — 7 files
- Bekenstein-Hawking missing the `/4`, commented *"corrected formula"* — exactly
  4× high
- Hawking temperature missing `k_B` entirely — returns joules, not kelvin
- Bekenstein-Hawking with `G` misplaced and `k_B` inverted — seven orders low

The last two sit in the script computing GW150914 entropy — the same event the
κ = 1366 claim rests on.

**Why the 12× error survived for years:** `T_H` is *never* a numeric literal in
code. It is always a computed expression, and the code is correct everywhere it
appears. The bad `1.2e-8` exists only in prose — notes, markdown, LaTeX. No
script ever evaluated it, so no run could contradict it. It propagated by
citation.

---

## Contents

```
E3_audit_2026/
├── README.md                    this file — process report
├── BRUNO_E3_FULL_AUDIT.md       ★ the deliverable: 5-section audit
├── AUDIT.md                     earlier Phase-3-only draft (superseded)
├── data/                        machine-readable
│   ├── findings.json            ★ every finding, structured
│   ├── manifest.json            corpus statistics
│   ├── constants_inventory.json 689 constant assignments
│   ├── equations_inventory.json 121 equation right-hand sides
│   ├── kappa_hits.json          151 κ occurrences with context
│   ├── file_classification.json canonical / superseded / orphan / duplicate
│   └── duplicate_groups.json    md5 → every path with that content
├── reports/
│   ├── VALUE_TABLE.md           values grouped by value, with branch breakdown
│   ├── FOLDER_AUDIT.md          filename recurrence, parallel trees
│   ├── RECOMPUTE.md             full recomputation transcript
│   └── GAP_CHECK.md             value-first sweep for unconventional names
├── scripts/                     9 scripts — fully reproducible
└── raw/                         grep sweeps + file manifests (.gz for large)
```

**Start with `BRUNO_E3_FULL_AUDIT.md`.** `data/findings.json` is the same content
structured for programmatic use.

## Reproducing

```sh
cd scripts
python3 extract.py && python3 verify.py && python3 verify2.py \
  && python3 classify.py && python3 value_table.py \
  && python3 phase4.py && python3 phase5_recompute.py \
  && python3 gap_check.py && python3 make_json.py
```

`verify.py` and `verify2.py` are self-contained — they need only Python and
prove findings 1–4 in about a second. The rest expect the corpus at its original
path and the manifests in `raw/`.

---

## Recommended next steps

**Blocked until the dimensional inconsistency is resolved:** defining κ anywhere.
That is not a cleanup task; it is a physics question the corpus cannot answer.

Independent of it:

1. Delete `Entropy-Collapse-Research-main` — hollow, nothing is lost
2. Delete both virtualenvs (~40 GB), rebuild from `requirements.txt`
3. **Normalize line endings before deduplicating** — 42 files are CRLF/LF twins
   and would otherwise survive as needless copies
4. Remove all 32 placeholder `bruno_constant` sites, including the two
   serialized model JSONs
5. Retract `BRUNO_CONSTANT_FINAL_ANALYSIS.md`
6. Create `e3_core/constants.py` as the single source of truth, **deriving**
   Planck units rather than hardcoding them — that permanently eliminates both
   the three-CODATA-vintage problem and the `t_planck` mislabel

## Known gaps

Listed in full in `BRUNO_E3_FULL_AUDIT.md` §5 and `findings.json`. The two most
worth pursuing:

- **The 94,443 dataset JSONs were excluded as bulk data** — but
  `e3_universal_thermal_model_v2_*.json` proved model parameters *do* get
  serialized to JSON. That exclusion may hide more placeholder values.
- **`git log -S 1366` across the 16 repositories** would date the 1366 → 1313
  transition definitively. No static analysis can.

---

## A note on reading this audit

Directory names in this corpus are not evidence. `CLEAN_`, `Final`,
`CURRENT_PRODUCTION` and `latest` label trees that are in several cases *older*
than what they claim to supersede. Every classification here uses content hashes,
never names.

Where the evidence does not settle a question, the audit says so and states what
would settle it. Choosing 1313 over 1366 is correct within the framework's own
terms and it is the only value reproducible from a stated formula — but that is a
statement about internal consistency, not about physics.
