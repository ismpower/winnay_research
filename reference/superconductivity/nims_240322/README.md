# NIMS SuperCon elemental reference — version 240322

This is the first curated superconductivity reference set for the E3 restart.
It contains only observations copied from the NIMS MDR SuperCon Datasheet
Ver.240322. No missing value was filled and no measurement was averaged,
converted, corrected, or selected as a universal value.

## Evidence boundary

`reported_in_nims_supercon_240322` means that NIMS associates the observation
with the cited source. It does **not** mean that this project has independently
verified the original paper. Independent verification must be recorded as a
separate future audit; it must never overwrite the source observation.

The first selection contains records whose NIMS `element` field exactly equals
`Al1`, `Sn1`, `Pb1`, `Nb1`, or `Hg1`. This extraction rule is project metadata,
not an experimental claim or a NIMS-supplied material classification.

## Files

- `elemental_observations.tsv`: selected sample-level observations with source
  line, transition definitions, units, thermodynamic and transport properties,
  preparation information, and citations.
- `literature_references.tsv`: distinct citation strings present in the selected
  NIMS rows.
- `data_dictionary.tsv`: original NIMS labels for every retained field.
- `selection_manifest.json`: source identity, checksum, selection rule, counts,
  and explicit list of transformations not performed.

Blank cells are meaningful: they state only that the corresponding NIMS field
is blank for that observation. They are not zero.

## Reproduce

From the repository root:

```bash
python3 scripts/extract_nims_elemental_reference.py \
  --zip data/raw/nims_supercon/240322/650c4826-f0ca-42e8-8dd9-94025a5307ce.zip \
  --source data/raw/nims_supercon/240322/extracted/20240322_MDR_OAndM.txt \
  --output reference/superconductivity/nims_240322
```

The script refuses to run if the raw archive does not match the recorded
SHA-256 checksum.
