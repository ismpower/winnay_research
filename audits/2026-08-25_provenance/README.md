# Bruno/E3 provenance reconstruction

This audit reconstructs the historical lineage of the Bruno/E3 hypothesis from
the read-only legacy corpus at `/home/winnay/Documents/Codex/E3_Engine`.

It is deliberately separate from `audits/2026-08-02_initial/`. That audit is an
immutable corpus-level validity review; this one asks a different question:
**how did the idea, constants, datasets, notebooks, figures, and engine evolve?**

## Reproduce

```bash
python3 scripts/parse_provenance.py
python3 scripts/extract_key_git_history.py
```

The parser uses only the Python standard library and Git. It writes generated
inventories under `data/` and never modifies the legacy corpus.

## Generated files

- `data/artifacts.csv` — relevant documents, code, notebooks, tables, and media
- `data/content_groups.csv` — exact duplicate groups and candidate ancestors
- `data/notebooks.csv` — cell/output/image counts and extracted notebook dates
- `data/media.csv` — figures/images with hashes, sizes, and nearby source hints
- `data/claims.csv` — equations, constants, thresholds, and suspicious constructs
- `data/git_events.csv` — targeted Git appearances for high-value artifacts
- `data/summary.json` — counts and parser configuration

`PROVENANCE_REPORT.md` is the hand-reviewed interpretation of these inventories.

The main parser skips the corpus-wide Git walk by default because the legacy
tree is a wrapper containing many copied nested repositories. Set
`PROVENANCE_FULL_GIT=1` only when a slow exhaustive history pass is desired;
the targeted extractor is the normal reproducible route.
