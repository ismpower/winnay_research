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


# ---------------------------------------------------------------------------
# Combined reference lengths A + D (docs/TASK7_OPTIONS.md, section 6)
# ---------------------------------------------------------------------------

def hawking_scale_ratio(radius_m: float, temperature_k: float) -> float:
    """Return x = lambda_gamma(T)/(4 pi R) = hbar c/(4 pi k_B T R), dimensionless.

    x = 1 is the legacy Hawking-route condition R T = hbar c/(4 pi k_B).
    """
    radius_m = _require_positive(radius_m, "radius_m")
    return thermal_photon_length(temperature_k) / (4.0 * math.pi * radius_m)


def horizon_compactness(mass_kg: float, radius_m: float) -> float:
    """Return y = R_s/R = 2 G M/(R c^2), dimensionless. y = 1 is a horizon."""
    from .constants import schwarzschild_radius

    return schwarzschild_radius(mass_kg) / _require_positive(radius_m, "radius_m")


# ---------------------------------------------------------------------------
# Third length: mean atomic spacing (docs/TASK7_OPTIONS.md, section 6.4)
# ---------------------------------------------------------------------------

def mean_atomic_spacing(number_density_per_m3: float) -> float:
    """Return a = n^(-1/3) in metres, independent of crystal structure."""
    return _require_positive(number_density_per_m3, "number_density_per_m3") ** (-1.0 / 3.0)


def lattice_capacity_ratio(
    active_entropy_per_atom_over_k_b: float, spacing_m: float, radius_m: float
) -> float:
    """Return eta_S for sigma_crit = k_B/a^2 on a sphere of radius R with V = N a^3.

    eta_S = S_act/(sigma_crit A) = (S_act/(N k_B)) / (3 a/R). The active entropy
    and its measurement window must be stated (docs/TASK7_OPTIONS.md, 6.2).
    """
    if not math.isfinite(active_entropy_per_atom_over_k_b) or active_entropy_per_atom_over_k_b < 0.0:
        raise ValueError("active entropy per atom must be finite and nonnegative")
    spacing_m = _require_positive(spacing_m, "spacing_m")
    radius_m = _require_positive(radius_m, "radius_m")
    return active_entropy_per_atom_over_k_b / (3.0 * spacing_m / radius_m)
