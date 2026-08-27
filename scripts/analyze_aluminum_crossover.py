#!/usr/bin/env python3
"""Find heat-capacity crossover cues in NIMS MSP151067 without extrapolation."""

from __future__ import annotations

import argparse
import bisect
import csv
import json
import math
from pathlib import Path


TC_K = 1.163  # NIMS record 151067 and Phillips (1959)
UPPER_MEASURED_SUPERCONDUCTING_K = 1.160


def parse_nims_dat(path: Path) -> dict[str, list[tuple[float, float]]]:
    # The legacy file uses CR-only line endings.
    text = path.read_bytes().decode("utf-8").replace("\r", "\n")
    metadata: dict[str, str] = {}
    series: dict[str, list[tuple[float, float]]] = {}
    in_data = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line == "XDATA\tYDATA\tPDATA\tNUMBER":
            in_data = True
            continue
        if not in_data and ":" in line:
            key, value = line.split(":", 1)
            metadata[key] = value.strip()
            continue
        if in_data and line[0].isdigit():
            columns = line.split()
            temperature, capacity, field = float(columns[0]), float(columns[1]), columns[2]
            series.setdefault(field, []).append((temperature, capacity))
    for values in series.values():
        values.sort()
    required_metadata = {
        "FIGNO": "MSP151067", "XPROP": "T", "XUNIT": "K",
        "YPROP": "C", "YUNIT": "mJ/mol.K", "PPROP": "H", "PUNIT": "gauss",
    }
    for key, expected in required_metadata.items():
        if metadata.get(key) != expected:
            raise ValueError(f"Unexpected {key}: {metadata.get(key)!r}")
    if {key: len(value) for key, value in series.items()} != {"0": 48, "300": 37}:
        raise ValueError("Unexpected MSP151067 series or point counts")
    return series


def interpolate(points: list[tuple[float, float]], x: float) -> float:
    xs = [point[0] for point in points]
    position = bisect.bisect_right(xs, x)
    if position == 0 or position == len(points):
        if x == xs[0]:
            return points[0][1]
        if x == xs[-1]:
            return points[-1][1]
        raise ValueError(f"Refusing to extrapolate at T={x}")
    x0, y0 = points[position - 1]
    x1, y1 = points[position]
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def integral_linear_delta_over_t(a: float, b: float, da: float, db: float) -> float:
    """Exact integral of a linearly interpolated delta-C divided by T."""
    slope = (db - da) / (b - a)
    intercept = da - slope * a
    return slope * (b - a) + intercept * math.log(b / a)


def analyze(input_path: Path, output_dir: Path) -> dict:
    series = parse_nims_dat(input_path)
    superconducting = series["0"]
    normal = series["300"]
    lower = max(superconducting[0][0], normal[0][0])
    upper = min(UPPER_MEASURED_SUPERCONDUCTING_K, superconducting[-1][0], normal[-1][0])
    knots = sorted({
        lower, upper,
        *(x for values in series.values() for x, _ in values if lower < x < upper),
    })

    rows = []
    cumulative = 0.0
    roots = []
    entropy_at_roots = []
    for position, temperature in enumerate(knots):
        cs = interpolate(superconducting, temperature)
        cn = interpolate(normal, temperature)
        delta = cs - cn
        if position:
            previous = rows[-1]
            cumulative_before_interval = cumulative
            cumulative += integral_linear_delta_over_t(
                previous["temperature_K"], temperature,
                previous["delta_C_mJ_per_mol_K"], delta,
            )
            previous_delta = previous["delta_C_mJ_per_mol_K"]
            if previous_delta * delta < 0:
                previous_temperature = previous["temperature_K"]
                root = previous_temperature + (
                    (temperature - previous_temperature)
                    * (-previous_delta) / (delta - previous_delta)
                )
                roots.append(root)
                entropy_at_roots.append(
                    cumulative_before_interval
                    + integral_linear_delta_over_t(
                        previous_temperature, root, previous_delta, 0.0
                    )
                )
        rows.append({
            "temperature_K": temperature,
            "reduced_temperature_T_over_Tc": temperature / TC_K,
            "C_zero_gauss_mJ_per_mol_K": cs,
            "C_300_gauss_mJ_per_mol_K": cn,
            "delta_C_mJ_per_mol_K": delta,
            "partial_delta_S_from_lower_bound_mJ_per_mol_K": cumulative,
            "zero_gauss_value_is_measured_point": any(x == temperature for x, _ in superconducting),
            "field_300_gauss_value_is_measured_point": any(x == temperature for x, _ in normal),
        })

    if len(roots) != 1:
        raise ValueError(f"Expected one crossover in measured analysis range, found {roots}")
    crossover = roots[0]
    summary = {
        "input": str(input_path),
        "source_figure_id": "MSP151067",
        "paper_doi": "10.1103/PhysRev.114.676",
        "states_confirmed_from_paper_figure_4": {
            "0_gauss_below_Tc": "superconducting",
            "300_gauss": "normal",
        },
        "Tc_K": TC_K,
        "analysis_range_K": [lower, upper],
        "range_rule": "Shared measured range, ending at the last zero-gauss point below Tc; no extrapolation.",
        "interpolation": "Piecewise linear between adjacent measured points.",
        "crossover_temperature_K": crossover,
        "crossover_reduced_temperature_T_over_Tc": crossover / TC_K,
        "crossover_definition": "Piecewise-linear root of C_zero_gauss - C_300_gauss.",
        "physical_interpretation_boundary": "Heat-capacity equality, not the superconducting phase-transition temperature.",
        "partial_entropy_difference_at_crossover_mJ_per_mol_K": entropy_at_roots[0],
        "partial_entropy_difference_at_upper_bound_mJ_per_mol_K": cumulative,
        "entropy_warning": "Partial integral starts at 0.236 K, so it is not absolute S_s-S_n and must not be expected to vanish at Tc.",
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "aluminum_crossover_curve.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys(), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    (output_dir / "aluminum_crossover_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.input, args.output), indent=2))


if __name__ == "__main__":
    main()
