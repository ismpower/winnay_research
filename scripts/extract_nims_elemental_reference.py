#!/usr/bin/env python3
"""Extract an auditable elemental-superconductor reference from NIMS SuperCon.

The extractor copies source strings verbatim. It does not impute missing data,
convert units, average observations, or promote any observation to a consensus
value. Added fields are explicitly named ``extraction_*`` or ``source_*``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


EXPECTED_SHA256 = "764cbf86cc225e857276cba79f9a03514b7002bfa6dea20ccd760b2005cb3a15"
DATASET_DOI = "https://doi.org/10.48505/nims.4487"
DATASET_RECORD = "https://mdr.nims.go.jp/datasets/650c4826-f0ca-42e8-8dd9-94025a5307ce"
ELEMENT_FORMULAS = ("Al1", "Sn1", "Pb1", "Nb1", "Hg1")

# NIMS field codes, in output order. Values are copied exactly as supplied.
SELECTED_CODES = (
    "num", "refno", "commt", "name", "element", "shape", "year",
    "str1", "str3", "spaceg", "tblno", "ulat", "lata", "latb", "latc",
    "utc", "t1", "t2", "t3", "tcsus", "tcn", "tcwidth", "tc", "tcfig",
    "tcmeth", "udtcdp", "dtcdp", "pmax", "isotope", "isoel", "isorat",
    "dtc", "vols", "uhc1", "mhc1", "hc1zero", "uhc2", "mhc2", "hc2zero",
    "udhc2dt", "mdhc2dt", "dhc2dt", "ucohere", "mcohere", "cohere",
    "upenet", "mpenet", "penet", "ugap", "gap", "gapene", "gapmeth",
    "jche", "jc77", "spheat", "ujump", "spjump", "ugamma", "gamma",
    "gamcom", "debyet", "mdebye", "ures", "reshe", "res77", "resn",
    "nort", "resrt", "ucarr", "carrier", "rawmat", "method", "prepcmt",
    "title", "month", "keyword", "institute", "journal", "author", "sample",
    "comments",
)

REFERENCE_CODES = (
    "refno", "year", "title", "month", "keyword", "institute", "journal", "author",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_source(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream, delimiter="\t")
        labels = next(reader)
        codes = next(reader)
        if len(labels) != len(codes):
            raise ValueError("NIMS label and code header lengths differ")
        missing = [code for code in SELECTED_CODES if code not in codes]
        if missing:
            raise ValueError(f"Required NIMS fields absent: {missing}")
        rows = list(reader)
    return labels, codes, rows


def write_tsv(path: Path, header, rows) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def extract(zip_path: Path, source_path: Path, output_dir: Path) -> dict:
    archive_hash = sha256(zip_path)
    if archive_hash != EXPECTED_SHA256:
        raise ValueError(
            f"Archive SHA-256 mismatch: expected {EXPECTED_SHA256}, got {archive_hash}"
        )

    labels, codes, rows = read_source(source_path)
    index = {code: position for position, code in enumerate(codes)}
    label_for = dict(zip(codes, labels))
    chosen = [
        (source_line, row)
        for source_line, row in enumerate(rows, start=3)
        if row[index["element"]].strip() in ELEMENT_FORMULAS
    ]

    # Validate the extraction boundary without altering any source value.
    observed_formulas = {row[index["element"]].strip() for _, row in chosen}
    if observed_formulas != set(ELEMENT_FORMULAS):
        raise ValueError(f"Elemental selection incomplete: {sorted(observed_formulas)}")
    if any(len(row) != len(codes) for _, row in chosen):
        raise ValueError("Selected NIMS row has a different field count from the header")

    output_dir.mkdir(parents=True, exist_ok=True)
    observation_header = (
        "source_line_number",
        "extraction_evidence_status",
        *SELECTED_CODES,
    )
    observation_rows = [
        (
            str(source_line),
            "reported_in_nims_supercon_240322",
            *(row[index[code]] for code in SELECTED_CODES),
        )
        for source_line, row in chosen
    ]
    write_tsv(output_dir / "elemental_observations.tsv", observation_header, observation_rows)

    # A reference can have multiple sample rows. Preserve every distinct set of
    # source citation strings; do not guess missing bibliographic information.
    reference_rows = sorted(
        {
            tuple(row[index[code]] for code in REFERENCE_CODES)
            for _, row in chosen
        }
    )
    write_tsv(output_dir / "literature_references.tsv", REFERENCE_CODES, reference_rows)

    dictionary_rows = [
        (code, label_for[code], "verbatim NIMS source field")
        for code in SELECTED_CODES
    ]
    dictionary_rows[:0] = [
        ("source_line_number", "One-based line in 20240322_MDR_OAndM.txt", "extraction metadata"),
        ("extraction_evidence_status", "Dataset membership; not independent paper verification", "extraction metadata"),
    ]
    write_tsv(
        output_dir / "data_dictionary.tsv",
        ("field", "meaning", "origin"),
        dictionary_rows,
    )

    formula_counts = {
        formula: sum(row[index["element"]].strip() == formula for _, row in chosen)
        for formula in ELEMENT_FORMULAS
    }
    manifest = {
        "dataset": "NIMS MDR SuperCon Datasheet Ver.240322",
        "dataset_doi": DATASET_DOI,
        "dataset_record": DATASET_RECORD,
        "source_archive_sha256": archive_hash,
        "source_table": source_path.name,
        "source_total_observations": len(rows),
        "source_total_fields": len(codes),
        "selection_rule": {
            "source_field": "element",
            "exact_values": list(ELEMENT_FORMULAS),
            "note": "Selection metadata chosen for the first E3 reference audit; not a NIMS classification field.",
        },
        "selected_observations": len(chosen),
        "selected_counts_by_formula": formula_counts,
        "distinct_reference_rows": len(reference_rows),
        "transformations": [
            "Selected rows by exact element-field match.",
            "Copied selected source strings verbatim.",
            "Added source_line_number and extraction_evidence_status metadata.",
            "Did not impute blanks, parse numbers, convert units, average values, or select consensus values.",
        ],
    }
    (output_dir / "selection_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    manifest = extract(args.zip, args.source, args.output)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
