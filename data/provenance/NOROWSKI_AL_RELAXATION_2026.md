# Norowski aluminum relaxation dataset

- Dataset title: *The experimental data for the paper "Intrinsic quasiparticle lifetime in superconducting aluminum"*
- Authors: Konrad Norowski, Marek Foltyn, Alexander Savin, Maciej Zgirski
- Dataset DOI: `10.5281/zenodo.15236856`
- Article DOI: `10.1103/wsqx-9bgf`
- Dataset license: CC BY 4.0
- Raw location: `data/raw/aluminum_relaxation/norowski_2026/` (gitignored)

## Author files and published MD5 checksums

| File | MD5 |
|---|---|
| `Fig_1.opj` | `c39e6df80bf5672866dc678f7075a021` |
| `Fig_2.opj` | `b33adafa6f964cb17dd148618e6d7094` |
| `Fig_3.opj` | `c6f503c1d3e3a7495c32b31b50e2dad0` |
| `Fig_4.opj` | `984d58ee1dbb9a8845b4e50b6413bd8e` |
| `Fig_5.opj` | `61145094d47b649c430b4f52ee2791c1` |
| `Fig_6.opj` | `6c18ede142cfe368412386863b084bf1` |

All six local files were verified against these hashes on 2026-08-26.

## Supplemental source files

- Main arXiv PDF SHA-256: `763c011d6e6a36c5d2c92f6968cf1f20341829c19193a05903fe10668b49571c`
- Supplemental PDF SHA-256: `7c691ac8811b723b5dcc1ca4d35bf32e0c4746614470cf6e0bfac96d4ffa3c7a`

## Origin extraction

`Fig_2.opj` reports Origin project version `9.900225`. Exact worksheet values were
decoded with `liborigin` 3.0.3 from the archived `Makhber/liborigin` source tree, built
with parser logging enabled. The non-logging build silently returned zero worksheets and
was rejected. The successful parse returned 44 datasets, 6 spreadsheets, 15 workbooks,
and 1 graph. The long-form extraction has SHA-256
`1b68faa28b42420def7a06428c903fd736d1cd52e5cd52306771e28fc41f7e1a`.

No values were inferred from graph pixels. Curated rows retain their source container,
book, columns, and zero-based row index.
