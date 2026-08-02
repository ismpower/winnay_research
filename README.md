# winnay_research — Bruno Constant / E3 Engine

Independent audit and, going forward, canonical source of truth for the
Bruno constant (κ) physics framework and E3 engine research.

**Status: pre-restart.** The initial audit (below) found the governing
equation is dimensionally inconsistent — no value of κ is meaningful until
that's resolved. See `bruno_e3_restart_plan.json` for the ordered task list.

---

## Layout

```
winnay_research/
├── README.md                    this file
├── bruno_e3_restart_plan.json   ordered task list, read by personal assistant
│
├── audits/                      IMMUTABLE — historical record, never edited in place
│   └── 2026-08-02_initial/      first full corpus audit (41GB / 308k files)
│       ├── BRUNO_E3_FULL_AUDIT.md   ★ start here for findings
│       ├── AUDIT.md                 earlier Phase-3-only draft, superseded by the above
│       ├── data/                    machine-readable findings (JSON)
│       ├── raw/                     grep sweeps, hash lists, file manifests
│       ├── reports/                 value tables, folder audit, recompute transcript
│       └── scripts/                 9 scripts, fully reproducible
│
├── e3_core/                     MUTABLE — not yet created. Will hold the single
│                                 canonical constants/equations module once the
│                                 dimensional-analysis blocker (task 1) is resolved.
│
└── docs/                        not yet created. Will hold DIMENSIONAL_ANALYSIS.md
                                  and any other living reasoning docs.
```

Future audit passes (e.g. once the two private repos are accessible, or a
re-check after the restart) get their own new dated folder under `audits/` —
never overwrite `2026-08-02_initial/`.

## Start here

1. `bruno_e3_restart_plan.json` — the ordered plan, task 1 is blocking
2. `audits/2026-08-02_initial/BRUNO_E3_FULL_AUDIT.md` — full findings

## Headline findings from the initial audit

1. **The governing equation cannot balance dimensionally.** `β_B = A/V = 3/R = κ·T`
   has m⁻¹ on the left, dimensionless on the right. Blocks everything else.
2. **The GW150914 "independent validation" has no observational content** —
   the black hole mass cancels algebraically in the derivation.
3. **κ = 1366 is an artifact of a 12× error** in Hawking temperature.
   κ = 1313 (1310.11 recomputed) is the only value reproducible from its
   stated formula.
4. **The production engine never used either value** — 32 files carry a
   placeholder constant baked into serialized model JSON.
5. **67% of authored files are byte-identical duplicates**; one entire tree
   is hollow.
6. **The only pipeline run against real observational data** (204 real LIGO
   events) used neither audited κ candidate — it chains an admitted-empirical
   scale factor to a third, unrelated constant with no stated derivation.

Full detail, method, and recomputation transcripts:
`audits/2026-08-02_initial/BRUNO_E3_FULL_AUDIT.md`.
