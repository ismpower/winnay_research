#!/usr/bin/env python3
"""Curate Norowski et al. Fig. 2 data and compare reduced temperatures."""

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/aluminum_relaxation/norowski_2026/Fig_2_extracted_long.tsv"
OUT = ROOT / "reference/superconductivity/relaxation/norowski_2026"

PHILLIPS_TC_K = 1.163
PHILLIPS_CROSSOVER_K = 0.5882529230512992
NOROWSKI_TC_K = 1.3
AUTHOR_BOUNDARY_K = 0.7  # approximate prose boundary, not a fitted breakpoint

SERIES = (
    ("spreadsheet", "wire37um", "A", "B", 37),
    ("spreadsheet", "A40umwire", "A", "B", 40),
    ("workbook", "A90umwire", "A", "B", 90),
    ("spreadsheet", "A180umwire", "A", "B", 180),
    ("spreadsheet", "A200umwire", "A", "H", 200),
    ("spreadsheet", "Joonas800umwi", "A", "B", 800),
)
THEORY = ("spreadsheet", "electronphono", "A", "B")


def load_columns():
    columns = defaultdict(dict)
    with RAW.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["value_type"] != "number":
                continue
            key = (row["container_type"], row["book"], row["column"])
            columns[key][int(row["row_zero_based"])] = float(row["value"])
    return columns


def paired(columns, kind, book, x_column, y_column):
    x = columns[(kind, book, x_column)]
    y = columns[(kind, book, y_column)]
    return [(row, x[row], y[row]) for row in sorted(x.keys() & y.keys())]


def interpolate(points, target):
    lower = max((point for point in points if point[1] <= target), key=lambda point: point[1])
    upper = min((point for point in points if point[1] >= target), key=lambda point: point[1])
    if lower[1] == upper[1]:
        return lower[2], lower, upper
    fraction = (target - lower[1]) / (upper[1] - lower[1])
    value = lower[2] + fraction * (upper[2] - lower[2])
    return value, lower, upper


def main():
    columns = load_columns()
    OUT.mkdir(parents=True, exist_ok=True)

    curated = []
    measured = {}
    for kind, book, xcol, ycol, length_um in SERIES:
        points = paired(columns, kind, book, xcol, ycol)
        measured[length_um] = points
        curated.extend(
            {
                "series_kind": "measured",
                "length_um": length_um,
                "temperature_K": temperature,
                "tau_us": tau,
                "source_container": kind,
                "source_book": book,
                "source_x_column": xcol,
                "source_y_column": ycol,
                "source_row_zero_based": row,
            }
            for row, temperature, tau in points
        )

    theory_points = paired(columns, *THEORY)
    curated.extend(
        {
            "series_kind": "electron_phonon_reference",
            "length_um": "",
            "temperature_K": temperature,
            "tau_us": tau,
            "source_container": THEORY[0],
            "source_book": THEORY[1],
            "source_x_column": THEORY[2],
            "source_y_column": THEORY[3],
            "source_row_zero_based": row,
        }
        for row, temperature, tau in theory_points
    )

    fieldnames = list(curated[0])
    with (OUT / "fig2_relaxation_curves.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(curated)

    reduced_target = PHILLIPS_CROSSOVER_K / PHILLIPS_TC_K
    target_K = reduced_target * NOROWSKI_TC_K
    theory_value, theory_lower, theory_upper = interpolate(theory_points, target_K)
    samples = []
    for length_um, points in measured.items():
        value, lower, upper = interpolate(points, target_K)
        samples.append(
            {
                "length_um": length_um,
                "tau_us_at_target": value,
                "electron_phonon_reference_us": theory_value,
                "tau_ratio_measured_to_reference": value / theory_value,
                "interpolation_bracket_K": [lower[1], upper[1]],
            }
        )

    result = {
        "classification": "exploratory_alignment_not_confirmation",
        "normalization": {
            "phillips_Tc_K": PHILLIPS_TC_K,
            "phillips_crossover_K": PHILLIPS_CROSSOVER_K,
            "target_reduced_temperature_T_over_Tc": reduced_target,
            "norowski_Tc_K": NOROWSKI_TC_K,
            "mapped_target_temperature_K": target_K,
        },
        "author_reported_boundary": {
            "temperature_K": AUTHOR_BOUNDARY_K,
            "reduced_temperature_T_over_Tc": AUTHOR_BOUNDARY_K / NOROWSKI_TC_K,
            "absolute_difference_from_mapped_target_K": abs(AUTHOR_BOUNDARY_K - target_K),
            "note": "The paper states an approximate regime boundary; it does not report a fitted breakpoint uncertainty.",
        },
        "interpolation": {
            "method": "linear between adjacent published worksheet values",
            "electron_phonon_bracket_K": [theory_lower[1], theory_upper[1]],
            "samples": samples,
        },
    }
    (OUT / "alignment_result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
