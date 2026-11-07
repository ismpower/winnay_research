#!/usr/bin/env python3
"""Compute the reference-system numbers quoted in docs/TASK7_OPTIONS.md.

Every number in that document's tables comes from this script's output,
docs/task7_candidate_scales.json. Inputs that are not in
reference/known_physics_reference.json are labelled as assumptions.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from e3_core import bcs  # noqa: E402
from e3_core import constants as k  # noqa: E402
from e3_core import scales  # noqa: E402
from e3_core.geometry import sphere_area, sphere_volume  # noqa: E402

OUTPUT = ROOT / "docs" / "task7_candidate_scales.json"

REFERENCE = {
    entry["id"]: entry
    for category in json.loads((ROOT / "reference" / "known_physics_reference.json").read_text())["categories"]
    for entry in category["entries"]
}

# Phillips (1959) aluminium sample, see
# reference/superconductivity/comparison_material/analysis/ALUMINUM_CROSSOVER.md.
AL_SAMPLE_MASS_G = 212.64          # paper
AL_GAMMA_J_PER_MOL_K2 = 1.350e-3   # paper
AL_TC_K = 1.163                    # paper
AL_DEBYE_K = 427.7                 # paper
AL_NUCLEAR_SPIN = 2.5              # Al-27, the only stable isotope
# Assumptions (standard handbook values, not from this repository's sources):
AL_MOLAR_MASS_G_PER_MOL = 26.9815
AL_DENSITY_KG_PER_M3 = 2700.0


def capacities(entropy: float, area: float, temperature: float, spacing: float | None) -> dict:
    out = {
        "eta_bekenstein_hawking": entropy / (k.bekenstein_hawking_surface_entropy_density() * area),
        "eta_thermal_photon": entropy / (scales.one_kb_per_area(scales.thermal_photon_length(temperature)) * area),
    }
    if spacing is not None:
        out["eta_lattice"] = entropy / (scales.one_kb_per_area(spacing) * area)
    return out


def black_hole(solar_masses: float) -> dict:
    mass = solar_masses * REFERENCE["M_sun"]["value"]
    radius = k.schwarzschild_radius(mass)
    temperature = k.hawking_temperature(mass)
    area = sphere_area(radius)
    entropy = k.bekenstein_hawking_surface_entropy_density() * area
    return {
        "system": f"Schwarzschild black hole, {solar_masses:g} solar masses",
        "radius_m": radius,
        "temperature_K": temperature,
        "radius_over_thermal_photon_length": radius / scales.thermal_photon_length(temperature),
        **capacities(entropy, area, temperature, None),
    }


def photon_cavity(radius: float, temperature: float, label: str) -> dict:
    area = sphere_area(radius)
    entropy = scales.photon_gas_entropy(temperature, sphere_volume(radius))
    return {
        "system": label,
        "radius_m": radius,
        "temperature_K": temperature,
        "radius_over_thermal_photon_length": radius / scales.thermal_photon_length(temperature),
        **capacities(entropy, area, temperature, None),
    }


def aluminium_sample(temperature: float) -> dict:
    moles = AL_SAMPLE_MASS_G / AL_MOLAR_MASS_G_PER_MOL
    volume = AL_SAMPLE_MASS_G * 1.0e-3 / AL_DENSITY_KG_PER_M3
    radius = (3.0 * volume / (4.0 * math.pi)) ** (1.0 / 3.0)
    atoms = moles * k.AVOGADRO_CONSTANT_PER_MOL
    spacing = (volume / atoms) ** (1.0 / 3.0)
    area = sphere_area(radius)
    entropy = AL_GAMMA_J_PER_MOL_K2 * moles * temperature  # normal-state electronic, S = gamma T
    gas_constant = k.AVOGADRO_CONSTANT_PER_MOL * k.BOLTZMANN_CONSTANT_J_PER_K
    lattice_threshold_per_atom = 3.0 * spacing / radius
    return {
        "system": f"Phillips aluminium sample as an equal-volume sphere, normal-state electrons, {temperature:g} K",
        "radius_m": radius,
        "temperature_K": temperature,
        "mean_atomic_spacing_m": spacing,
        "radius_over_thermal_photon_length": radius / scales.thermal_photon_length(temperature),
        **capacities(entropy, area, temperature, spacing),
        "lattice_threshold_entropy_per_atom_over_k_B": lattice_threshold_per_atom,
        "normal_state_temperature_where_eta_lattice_is_1_K": lattice_threshold_per_atom * gas_constant / AL_GAMMA_J_PER_MOL_K2,
        "assumptions": {
            "molar_mass_g_per_mol": AL_MOLAR_MASS_G_PER_MOL,
            "density_kg_per_m3": AL_DENSITY_KG_PER_M3,
            "geometry": "sample treated as a sphere of equal volume",
            "entropy": "normal-state electronic entropy gamma*T only; lattice entropy neglected (Debye 427.7 K)",
        },
    }


def aluminium_superconducting_lattice_crossing(threshold_per_atom: float) -> dict:
    """Temperature where zero-field electronic (BCS) + phonon (Debye) entropy reaches
    the lattice capacity, for capacity x (A/V) factors f. Nuclear-spin entropy is
    excluded; that exclusion is a modelling choice and is reported alongside."""
    gas_constant = k.AVOGADRO_CONSTANT_PER_MOL * k.BOLTZMANN_CONSTANT_J_PER_K

    def molar_entropy(temperature: float) -> float:
        electrons = bcs.entropy_ratio(temperature / AL_TC_K) * AL_GAMMA_J_PER_MOL_K2 * AL_TC_K
        phonons = (4.0 * math.pi**4 / 5.0) * gas_constant * (temperature / AL_DEBYE_K) ** 3
        return electrons + phonons

    def crossing(factor: float) -> float:
        target = factor * threshold_per_atom * gas_constant
        lo, hi = 0.02, AL_TC_K
        if not molar_entropy(lo) < target < molar_entropy(hi):
            raise RuntimeError("crossing not bracketed")
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if molar_entropy(mid) < target else (lo, mid)
        return 0.5 * (lo + hi)

    t_ref = crossing(1.0)
    electrons = bcs.entropy_ratio(t_ref / AL_TC_K) * AL_GAMMA_J_PER_MOL_K2 * AL_TC_K
    return {
        "model": "zero-field weak-coupling BCS electronic entropy + Debye phonon entropy; nuclear spins excluded",
        "crossing_temperature_K_by_factor": {f"{f:g}": crossing(f) for f in (0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 10.0)},
        "factor_meaning": "f multiplies the threshold: sigma prefactor (k_B/a^2 -> f k_B/a^2) times the sample's A/V relative to a sphere; for a geometrically similar sample, f = R_sphere/R_sample (size dependence)",
        "phonon_to_electron_entropy_at_f1": (molar_entropy(t_ref) - electrons) / electrons,
        "nuclear_spin_entropy_over_threshold": math.log(2.0 * AL_NUCLEAR_SPIN + 1.0) / threshold_per_atom,
        "phillips_reported_anomaly": "measured C_s near 0.17 K about 4x the exponential extrapolation (ALUMINUM_CROSSOVER.md)",
        "status": "post hoc: found after the anomaly was known; not evidence",
    }


# Assumptions for the Sun (IAU 2015 nominal radius, nominal effective temperature):
SUN_RADIUS_M = 6.957e8
SUN_EFFECTIVE_TEMPERATURE_K = 5772.0


def combined_a_d_ratios(systems: list[dict]) -> list[dict]:
    """x = hbar c/(4 pi k_B T R) (option A), y = R_s/R (option D); (1, 1) is a horizon."""
    al_mass = AL_SAMPLE_MASS_G * 1.0e-3
    bh_mass = 10.0 * REFERENCE["M_sun"]["value"]
    sun_mass = REFERENCE["M_sun"]["value"]
    rows = [
        ("Schwarzschild black hole, 10 solar masses", bh_mass, systems[0]["radius_m"], systems[0]["temperature_K"]),
        ("Phillips aluminium sample, 1 K", al_mass, systems[2]["radius_m"], 1.0),
        ("Sun (assumed nominal radius and effective temperature)", sun_mass, SUN_RADIUS_M, SUN_EFFECTIVE_TEMPERATURE_K),
    ]
    return [
        {
            "system": name,
            "x_hawking_scale_ratio": scales.hawking_scale_ratio(radius, temperature),
            "y_horizon_compactness": scales.horizon_compactness(mass, radius),
        }
        for name, mass, radius, temperature in rows
    ]


def main() -> None:
    result = {
        "generated_by": "scripts/task7_candidate_scales.py",
        "thermal_photon_length_m": {
            "1 K": scales.thermal_photon_length(1.0),
            "2.7255 K (CMB)": scales.thermal_photon_length(REFERENCE["cmb_temperature_today"]["value"]),
            "300 K": scales.thermal_photon_length(300.0),
        },
        "hbar_c_over_k_B_m_K": scales.thermal_photon_length(1.0),
        "hawking_product_hbar_c_over_4pi_k_B_m_K": scales.thermal_photon_length(1.0) / (4.0 * math.pi),
        "photon_gas_unit_ratio_radius_over_photon_length": 135.0 / (4.0 * math.pi**2),
        "systems": [
            black_hole(10.0),
            photon_cavity(0.01, 1.0, "Blackbody cavity, R = 1 cm, 1 K"),
            aluminium_sample(1.0),
        ],
        "aluminium_superconducting_lattice_crossing": None,
        "combined_a_d_ratios": None,
    }
    al = result["systems"][2]
    result["aluminium_superconducting_lattice_crossing"] = aluminium_superconducting_lattice_crossing(
        al["lattice_threshold_entropy_per_atom_over_k_B"]
    )
    result["combined_a_d_ratios"] = combined_a_d_ratios(result["systems"])
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
