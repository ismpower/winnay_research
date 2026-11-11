#!/usr/bin/env python3
"""Analyze Phillips (1959) Table II without extrapolation or imputation."""

from __future__ import annotations

import argparse
import bisect
import csv
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from e3_core import bcs  # noqa: E402


TC_K = 1.163
# Phillips (1959): about 2% precision for heat-input/temperature-rise data in the
# adiabatic-demagnetization region (normal state, and superconducting above 0.4 K).
STATED_POINT_PRECISION = 0.02


def interpolate(points: list[tuple[float, float]], temperature: float) -> float:
    xs = [point[0] for point in points]
    if temperature == xs[0]:
        return points[0][1]
    if temperature == xs[-1]:
        return points[-1][1]
    position = bisect.bisect_right(xs, temperature)
    if position == 0 or position == len(points):
        raise ValueError(f"Refusing to extrapolate at {temperature} K")
    x0, y0 = points[position - 1]
    x1, y1 = points[position]
    return y0 + (y1 - y0) * (temperature - x0) / (x1 - x0)


def integrate_segment(a: float, b: float, delta_a: float, delta_b: float) -> float:
    slope = (delta_b - delta_a) / (b - a)
    intercept = delta_a - slope * a
    return slope * (b - a) + intercept * math.log(b / a)


def analyze(input_path: Path, output_dir: Path) -> dict:
    with input_path.open(encoding="utf-8", newline="") as stream:
        source_rows = list(csv.DictReader(stream, delimiter="\t"))
    if len(source_rows) != 149:
        raise ValueError(f"Expected 149 visually checked Table II pairs, found {len(source_rows)}")
    if any(row["verification"] != "visually_checked" for row in source_rows):
        raise ValueError("Table contains a row that has not been visually checked")

    normal = sorted(
        (float(row["temperature_K"]), float(row["heat_capacity_mJ_per_mol_K"]))
        for row in source_rows
        if row["state"] == "normal" and row["region"] == "adiabatic_demagnetization"
    )
    superconducting = sorted(
        (float(row["temperature_K"]), float(row["heat_capacity_mJ_per_mol_K"]))
        for row in source_rows
        if row["state"] == "superconducting"
    )
    if (len(normal), len(superconducting)) != (57, 58):
        raise ValueError("Unexpected Table II analysis selection")

    lower = max(normal[0][0], superconducting[0][0])
    upper = min(normal[-1][0], superconducting[-1][0])
    knots = sorted({
        lower, upper,
        *(temperature for values in (normal, superconducting)
          for temperature, _ in values if lower < temperature < upper),
    })

    curve = []
    roots = []
    root_entropies = []
    cumulative = 0.0
    for index, temperature in enumerate(knots):
        cs = interpolate(superconducting, temperature)
        cn = interpolate(normal, temperature)
        delta = cs - cn
        if index:
            previous = curve[-1]
            cumulative_before = cumulative
            cumulative += integrate_segment(
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
                root_entropies.append(
                    cumulative_before
                    + integrate_segment(previous_temperature, root, previous_delta, 0.0)
                )
        curve.append({
            "temperature_K": temperature,
            "T_over_Tc": temperature / TC_K,
            "C_superconducting_mJ_per_mol_K": cs,
            "C_normal_mJ_per_mol_K": cn,
            "delta_C_mJ_per_mol_K": delta,
            "partial_delta_S_from_lower_bound_mJ_per_mol_K": cumulative,
            "superconducting_value_is_printed_point": any(x == temperature for x, _ in superconducting),
            "normal_value_is_printed_point": any(x == temperature for x, _ in normal),
        })
    if len(roots) != 1:
        raise ValueError(f"Expected one crossover; found {roots}")

    root = roots[0]
    bracket = next(
        [curve[index - 1]["temperature_K"], curve[index]["temperature_K"]]
        for index in range(1, len(curve))
        if curve[index - 1]["delta_C_mJ_per_mol_K"]
        * curve[index]["delta_C_mJ_per_mol_K"] < 0
    )
    bcs_t = bcs.heat_capacity_crossover()
    bcs_temperature = bcs_t * TC_K
    bcs_cs = interpolate(superconducting, bcs_temperature)
    bcs_cn = interpolate(normal, bcs_temperature)
    bcs_relative_delta = (bcs_cs - bcs_cn) / bcs_cn
    bcs_comparison = {
        "model": "weak-coupling BCS, e3_core.bcs.heat_capacity_crossover (see docs/BCS_BASELINE.md)",
        "crossover_T_over_Tc": bcs_t,
        "crossover_temperature_K_at_this_Tc": bcs_temperature,
        "measured_minus_bcs_T_over_Tc": root / TC_K - bcs_t,
        "bcs_temperature_inside_measured_sign_change_bracket": bracket[0] <= bcs_temperature <= bracket[1],
        "measured_relative_delta_C_at_bcs_crossover": bcs_relative_delta,
        "stated_point_precision": STATED_POINT_PRECISION,
        "measured_delta_C_within_stated_precision_at_bcs_crossover": abs(bcs_relative_delta) <= STATED_POINT_PRECISION,
        "interpretation": "At the BCS crossover temperature the interpolated (C_s-C_n)/C_n is compared with the paper's stated point precision. If it lies within that precision, these data do not resolve a departure from weak-coupling BCS. Uncertainty is not formally propagated.",
    }
    summary = {
        "input": str(input_path),
        "paper_doi": "10.1103/PhysRev.114.676",
        "source_table": "Table II, printed page 681",
        "source_pairs_total": 149,
        "analysis_normal_pairs": 57,
        "analysis_superconducting_pairs": 58,
        "Tc_K": TC_K,
        "analysis_range_K": [lower, upper],
        "selection": "Normal and superconducting points with a shared measured temperature range; liquid-helium normal points above the range are excluded.",
        "interpolation": "Piecewise linear through all selected printed points after sorting by temperature; no averaging or extrapolation.",
        "crossover_bracket_K": bracket,
        "crossover_temperature_K": root,
        "crossover_T_over_Tc": root / TC_K,
        "partial_delta_S_at_crossover_mJ_per_mol_K": root_entropies[0],
        "partial_delta_S_at_upper_bound_mJ_per_mol_K": cumulative,
        "entropy_warning": "Both entropy integrals start at 0.1718 K and are offset partial integrals, not absolute S_s-S_n.",
        "precision_warning": "Reported decimals are computational outputs, not experimental significant figures; experimental uncertainty is not propagated here.",
        "bcs_weak_coupling_baseline": bcs_comparison,
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "aluminum_table_ii_curve.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=curve[0].keys(), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(curve)
    (output_dir / "aluminum_table_ii_summary.json").write_text(
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
