#!/usr/bin/env python3
"""Compute the P1 prediction table quoted in docs/PREREGISTRATION_P1.md.

Writes docs/p1_prediction_table.json. Illustrative samples use the Phillips (1959)
aluminium parameters; a registered test uses each sample's own parameters.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from e3_core import prediction_p1 as p1  # noqa: E402

SCALES = json.loads((ROOT / "docs" / "task7_candidate_scales.json").read_text())
SPACING_M = SCALES["systems"][2]["mean_atomic_spacing_m"]
PHILLIPS_RADIUS_M = SCALES["systems"][2]["radius_m"]
PHILLIPS = {"gamma": 1.350e-3, "tc_k": 1.163, "debye_k": 427.7}


def main() -> None:
    rows = []
    for multiplier in (0.1, 1.0, 10.0, 100.0, 1000.0):
        area_over_volume = multiplier * 3.0 / PHILLIPS_RADIUS_M
        threshold = p1.lattice_threshold_per_atom(SPACING_M, area_over_volume)
        low, mid, high = p1.predicted_band(threshold, **PHILLIPS)
        rows.append({
            "A_over_V_relative_to_phillips_sphere": multiplier,
            "A_over_V_per_m": area_over_volume,
            "equivalent_sphere_radius_m": 3.0 / area_over_volume,
            "threshold_entropy_per_atom_over_k_B": threshold,
            "T_star_K_prefactor_0.25": low,
            "T_star_K_prefactor_1": mid,
            "T_star_K_prefactor_4": high,
        })
    s1 = {"spacing_m": SPACING_M, "area_over_volume_per_m": 3.0 / PHILLIPS_RADIUS_M, **PHILLIPS}
    s4 = {**s1, "area_over_volume_per_m": 4.0 * 3.0 / PHILLIPS_RADIUS_M}
    t1 = rows[1]["T_star_K_prefactor_1"]
    result = {
        "generated_by": "scripts/p1_prediction_table.py",
        "parameters": {"mean_atomic_spacing_m": SPACING_M, **PHILLIPS},
        "single_sample_bands": rows,
        "two_sample_example": {
            "description": "If sample 1 (Phillips A/V) departs at T1, sample 2 with 4x the A/V is predicted to depart at T2, whatever the prefactor",
            "T1_K": t1,
            "T2_K": p1.partner_crossing_temperature(t1, s1, s4),
        },
    }
    out = ROOT / "docs" / "p1_prediction_table.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
