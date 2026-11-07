"""Candidate length scales and boundary capacities for plan task 7.

These are standard physics definitions, implemented so that the options in
`docs/TASK7_OPTIONS.md` are computed rather than asserted. Nothing here chooses
L_0 or sigma_crit; that decision belongs to the researcher.
"""

from __future__ import annotations

import math

from .constants import (
    BOLTZMANN_CONSTANT_J_PER_K as _K_B,
    PLANCK_CONSTANT_J_S as _H,
    REDUCED_PLANCK_CONSTANT_J_S as _HBAR,
    SPEED_OF_LIGHT_M_PER_S as _C,
)
from .geometry import sphere_volume


def _require_positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


def thermal_photon_length(temperature_k: float) -> float:
    """Return the reduced thermal photon length hbar c/(k_B T) in metres.

    This is the inverse of the thermal photon wavenumber k_B T/(hbar c). It is
    not the Wien peak wavelength.
    """
    return _HBAR * _C / (_K_B * _require_positive(temperature_k, "temperature_k"))


def thermal_de_broglie_wavelength(mass_kg: float, temperature_k: float) -> float:
    """Return h/sqrt(2 pi m k_B T) in metres for a non-relativistic particle."""
    mass_kg = _require_positive(mass_kg, "mass_kg")
    temperature_k = _require_positive(temperature_k, "temperature_k")
    return _H / math.sqrt(2.0 * math.pi * mass_kg * _K_B * temperature_k)


def radiation_constant() -> float:
    """Return a = pi^2 k_B^4/(15 hbar^3 c^3) in J m^-3 K^-4."""
    return math.pi**2 * _K_B**4 / (15.0 * _HBAR**3 * _C**3)


def photon_gas_entropy(temperature_k: float, volume_m3: float) -> float:
    """Return blackbody photon-gas entropy (4/3) a T^3 V in J/K."""
    temperature_k = _require_positive(temperature_k, "temperature_k")
    volume_m3 = _require_positive(volume_m3, "volume_m3")
    return (4.0 / 3.0) * radiation_constant() * temperature_k**3 * volume_m3


def one_kb_per_area(length_m: float) -> float:
    """Return the boundary capacity k_B/l^2 in J K^-1 m^-2 for a length l.

    `k_B/(4 l_P^2)` (Bekenstein-Hawking) is this with l = 2 l_P. The numerical
    prefactor is a modelling choice and must be justified, not fitted.
    """
    return _K_B / _require_positive(length_m, "length_m") ** 2


def sphere_photon_gas_capacity_ratio(radius_m: float, temperature_k: float) -> float:
    """Return eta_S for a blackbody sphere with sigma_crit = k_B/lambda_gamma(T)^2.

    Closed form: (4 pi^2/135) R/lambda_gamma(T). The tests check the closed form
    against a direct entropy/area calculation.
    """
    radius_m = _require_positive(radius_m, "radius_m")
    entropy = photon_gas_entropy(temperature_k, sphere_volume(radius_m))
    area = 4.0 * math.pi * radius_m**2
    return entropy / (one_kb_per_area(thermal_photon_length(temperature_k)) * area)
