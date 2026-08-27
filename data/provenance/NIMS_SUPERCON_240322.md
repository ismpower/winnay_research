# NIMS MDR SuperCon Datasheet — version 240322

## Identity

- Publisher: National Institute for Materials Science (NIMS), Japan
- Dataset: MDR SuperCon Datasheet Ver.240322
- Dataset record: https://mdr.nims.go.jp/datasets/650c4826-f0ca-42e8-8dd9-94025a5307ce
- Version DOI: https://doi.org/10.48505/nims.4487
- Version readme DOI: https://doi.org/10.48505/nims.4488
- Latest-version collection DOI: https://doi.org/10.48505/nims.3739
- License: Creative Commons Attribution 4.0 International
- Downloaded manually: 2026-08-26

## Preserved download

- Local path: `data/raw/nims_supercon/240322/650c4826-f0ca-42e8-8dd9-94025a5307ce.zip`
- Size reported by `stat`: 58,235,249 bytes
- SHA-256: `764cbf86cc225e857276cba79f9a03514b7002bfa6dea20ccd760b2005cb3a15`

The raw directory is intentionally excluded from Git. The original archive is
preserved unchanged; derived tables must be written outside `data/raw/` and
must cite this record.

## Top-level archive contents

| File | Uncompressed bytes | Role |
|---|---:|---|
| `20240322_MDR_OAndM.txt` | 19,875,381 | Oxide and metallic records |
| `240322_MDR_Organic.txt` | 263,372 | Organic-superconductor records |
| `240322_supercon-mdr-schema.json` | 2,433 | Machine-readable schema |
| `240322_supercon-mdr-schema.yml` | 1,745 | Human-readable schema |
| `data.zip` | 3,015,852 | Associated data files |
| `figure.zip` | 53,751,944 | Associated figures |

## Handling rules

1. Never edit files under `data/raw/nims_supercon/240322/`.
2. Preserve reported composition, sample conditions, measurement method, and
   literature reference before selecting or aggregating critical temperatures.
3. Label measured, recommended, estimated, and derived values separately.
4. Do not use a feature derived from `Tc` to claim an independent prediction of
   `Tc`.
5. Record every filtering and normalization operation in a reproducible script.
