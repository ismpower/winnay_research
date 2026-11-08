#!/usr/bin/env python3
"""Numbers for the P1 measurement design (docs/P1_MEASUREMENT_DESIGN.md).

Uses the frozen P1 code (e3_core.prediction_p1, bcs, constants) unchanged.
Planning values for gamma, Tc and Debye are Phillips (1959); the registered
analysis must use the values measured on these samples. Writes
docs/p1_measurement_design.json.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from e3_core import constants as k  # noqa: E402
from e3_core import prediction_p1 as p1  # noqa: E402
from e3_core import scales  # noqa: E402

PLANNING = {"gamma": 1.350e-3, "tc_k": 1.163, "debye_k": 427.7}   # Phillips (1959)
# Assumptions (handbook values): density and molar mass of aluminium.
DENSITY_KG_PER_M3 = 2700.0
MOLAR_MASS_KG_PER_MOL = 26.9815e-3
# Al-27 nuclear constants (KAERI / LBL nuclear moments table); mu_N = e hbar/(2 m_p).
AL27_SPIN = 2.5
AL27_MOMENT_NUCLEAR_MAGNETONS = 3.6415069
PROTON_MASS_KG = 1.67262192369e-27  # CODATA 2018, as in reference/known_physics_reference.json
NORMAL_STATE_FIELD_T = 0.02          # design choice: about 2x the critical field of Al at T = 0
ZERO_FIELD_LIMIT_T = 1.0e-3          # registered inclusion criterion 3

SAMPLES = {
    # name: (length_m, width_m, thickness_m, description)
    "S1_block": (4.0e-3, 4.0e-3, 4.0e-3, "cube 4 x 4 x 4 mm"),
    "S2_plate": (10.0e-3, 10.0e-3, 0.25e-3, "plate 10 x 10 x 0.25 mm"),
    "S3_foil": (10.0e-3, 10.0e-3, 0.025e-3, "foil 10 x 10 x 0.025 mm (every dimension >= 10 um)"),
}


def nuclear_magneton() -> float:
    return k.ELEMENTARY_CHARGE_C * k.REDUCED_PLANCK_CONSTANT_J_S / (2.0 * PROTON_MASS_KG)


def sample_row(name: str, dims: tuple) -> dict:
    length, width, thickness, description = dims
    volume = length * width * thickness
    area = 2.0 * (length * width + length * thickness + width * thickness)
    mass = DENSITY_KG_PER_M3 * volume
    moles = mass / MOLAR_MASS_KG_PER_MOL
    spacing = scales.mean_atomic_spacing(moles * k.AVOGADRO_CONSTANT_PER_MOL / volume)
    threshold = p1.lattice_threshold_per_atom(spacing, area / volume)
    low, mid, high = p1.predicted_band(threshold, **PLANNING)
    window = (0.8 * low, 1.1 * high)

    def heat_capacity_j_per_k(t: float) -> float:
        return moles * p1.baseline_molar_heat_capacity(t, **PLANNING)

    mu = AL27_MOMENT_NUCLEAR_MAGNETONS * nuclear_magneton()
    t_low = window[0]
    electrons_phonons_per_atom = p1.baseline_molar_heat_capacity(t_low, **PLANNING) / p1.GAS_CONSTANT_J_PER_MOL_K
    return {
        "description": description,
        "mass_mg": mass * 1.0e6,
        "moles": moles,
        "area_over_volume_per_m": area / volume,
        "threshold_entropy_per_atom_over_k_B": threshold,
        "predicted_T_star_K": {"prefactor_0.25": low, "prefactor_1": mid, "prefactor_4": high},
        "required_window_K": list(window),
        "baseline_heat_capacity_J_per_K": {
            "at_window_bottom": heat_capacity_j_per_k(window[0]),
            "at_T_star_prefactor_1": heat_capacity_j_per_k(mid),
            "at_window_top": heat_capacity_j_per_k(window[1]),
        },
        "nuclear_zeeman_heat_capacity_over_baseline_at_window_bottom": {
            "zero_field_limit_1_mT": p1.zeeman_heat_capacity_per_spin(AL27_SPIN, mu, ZERO_FIELD_LIMIT_T, t_low)
            / electrons_phonons_per_atom,
        },
    }


def normal_state_nuclear_check() -> dict:
    """Nuclear Zeeman heat capacity vs gamma*T in the normal-state field."""
    mu = AL27_MOMENT_NUCLEAR_MAGNETONS * nuclear_magneton()
    out = {}
    for t in (0.1, 0.2, 0.4):
        nuclear = p1.zeeman_heat_capacity_per_spin(AL27_SPIN, mu, NORMAL_STATE_FIELD_T, t)
        electronic = PLANNING["gamma"] * t / p1.GAS_CONSTANT_J_PER_MOL_K
        out[f"{t:g} K"] = nuclear / electronic
    return out


def pair_predictions(rows: dict) -> dict:
    """Prefactor-free partner temperatures: if S1 departs at T1(f), where must S2 and S3 depart."""
    s1 = {"spacing_m": None}
    out = {}
    for f in (0.25, 1.0, 4.0):
        t1 = rows["S1_block"]["predicted_T_star_K"][f"prefactor_{f:g}"]
        entry = {"T1_K": t1}
        for other in ("S2_plate", "S3_foil"):
            entry[f"T_{other}_K"] = rows[other]["predicted_T_star_K"][f"prefactor_{f:g}"]
            entry[f"shift_{other}_K"] = entry[f"T_{other}_K"] - t1
        out[f"prefactor_{f:g}"] = entry
    smallest = min(abs(e["shift_S2_plate_K"]) for e in out.values())
    out["smallest_S1_S2_shift_K"] = smallest
    out["required_point_spacing_K"] = smallest / 4.0
    return out


def check_partner_function(rows: dict) -> float:
    """Confirm with partner_crossing_temperature that the band values are mutually consistent."""
    def sample(name):
        r = rows[name]
        spacing = r["threshold_entropy_per_atom_over_k_B"] / r["area_over_volume_per_m"]
        return {"spacing_m": spacing, "area_over_volume_per_m": r["area_over_volume_per_m"], **PLANNING}

    t1 = rows["S1_block"]["predicted_T_star_K"]["prefactor_1"]
    t2 = p1.partner_crossing_temperature(t1, sample("S1_block"), sample("S2_plate"))
    return abs(t2 - rows["S2_plate"]["predicted_T_star_K"]["prefactor_1"])


def main() -> None:
    rows = {name: sample_row(name, dims) for name, dims in SAMPLES.items()}
    result = {
        "generated_by": "scripts/p1_measurement_design.py",
        "planning_values": {**PLANNING, "source": "Phillips (1959); replace with values measured on the samples"},
        "samples": rows,
        "area_over_volume_ratios_to_S1": {
            name: rows[name]["area_over_volume_per_m"] / rows["S1_block"]["area_over_volume_per_m"] for name in rows
        },
        "pair_predictions": pair_predictions(rows),
        "partner_function_consistency_K": check_partner_function(rows),
        "normal_state_field_T": NORMAL_STATE_FIELD_T,
        "normal_state_nuclear_over_electronic_heat_capacity": normal_state_nuclear_check(),
    }
    out = ROOT / "docs" / "p1_measurement_design.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
