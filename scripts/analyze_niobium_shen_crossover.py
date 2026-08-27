#!/usr/bin/env python3
"""Reproduce the bounded Shen (1965) niobium crossover assessment."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


TC_OVER_T_GRAPHICAL_BRACKET = (1.55, 1.65)
FIT_A = 7.0
FIT_B = 1.46
FIT_TC_OVER_T_VALIDITY = (2.0, 6.0)


def bisection_root() -> float:
    """Solve a*exp(-b/x)=x for x=T/Tc on the physical interval."""
    lower, upper = 0.05, 0.999
    for _ in range(100):
        midpoint = (lower + upper) / 2.0
        residual = FIT_A * math.exp(-FIT_B / midpoint) - midpoint
        if residual > 0:
            upper = midpoint
        else:
            lower = midpoint
    return (lower + upper) / 2.0


def analyze(output_dir: Path) -> dict:
    reciprocal_low, reciprocal_high = TC_OVER_T_GRAPHICAL_BRACKET
    reduced_low = 1.0 / reciprocal_high
    reduced_high = 1.0 / reciprocal_low
    graphical_midpoint = (reduced_low + reduced_high) / 2.0
    graphical_half_width = (reduced_high - reduced_low) / 2.0

    fit_root = bisection_root()
    fit_root_tc_over_t = 1.0 / fit_root
    fit_root_is_valid = (
        FIT_TC_OVER_T_VALIDITY[0]
        < fit_root_tc_over_t
        < FIT_TC_OVER_T_VALIDITY[1]
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    bracket_rows = [
        {
            "Tc_over_T": reciprocal_low,
            "T_over_Tc": 1.0 / reciprocal_low,
            "visual_relation": "Ces/(gamma*Tc) above T/Tc",
            "meaning": "Cs greater than Cn if Cls equals Cln",
        },
        {
            "Tc_over_T": reciprocal_high,
            "T_over_Tc": 1.0 / reciprocal_high,
            "visual_relation": "Ces/(gamma*Tc) below T/Tc",
            "meaning": "Cs less than Cn if Cls equals Cln",
        },
    ]
    with (output_dir / "shen_fig11_graphical_bracket.tsv").open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.DictWriter(
            stream, fieldnames=bracket_rows[0].keys(), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(bracket_rows)

    summary = {
        "source": "Y. L. Shen, UCRL-16117 (1965), Figure 11",
        "source_pdf_page_1_based": 35,
        "observable": "Cs = Cn, reduced to Ces/(gamma*Tc) = T/Tc",
        "required_assumption": "superconducting and normal lattice heat capacities are equal",
        "graphical_assessment": {
            "method": "conservative visual sign-change bracket; no invented point values",
            "Tc_over_T_bracket": [reciprocal_low, reciprocal_high],
            "T_over_Tc_bracket": [reduced_low, reduced_high],
            "bracket_midpoint_T_over_Tc": graphical_midpoint,
            "half_bracket_width_T_over_Tc": graphical_half_width,
            "precision_warning": "Midpoint is a locator, not a measured best-fit estimate.",
        },
        "published_exponential_fit_sensitivity": {
            "equation": "Ces/(gamma*Tc) = 7.0 exp(-1.46 Tc/T)",
            "published_validity_Tc_over_T": list(FIT_TC_OVER_T_VALIDITY),
            "extrapolated_equality_T_over_Tc": fit_root,
            "extrapolated_equality_Tc_over_T": fit_root_tc_over_t,
            "root_inside_published_validity": fit_root_is_valid,
            "acceptance": "Rejected as a measured crossover because the root is outside fit validity.",
        },
        "comparison": {
            "aluminum_table_ii_T_over_Tc": 0.5058064687,
            "niobium_graphical_bracket_contains_aluminum_value": (
                reduced_low <= 0.5058064687 <= reduced_high
            ),
        },
    }
    (output_dir / "shen_crossover_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.output), indent=2))


if __name__ == "__main__":
    main()
