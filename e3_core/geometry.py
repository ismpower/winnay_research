"""Geometry and entropy-capacity identities for the E3 restart.

All inputs and outputs are SI-valued floats. Function names carry the intended
dimensions; no function in this module supplies or assumes a Bruno constant.
"""

from __future__ import annotations

import math


def _require_positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


def _require_nonnegative(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def sphere_area(radius_m: float) -> float:
    """Return `4*pi*R^2` in square metres for radius in metres."""
    radius_m = _require_positive(radius_m, "radius_m")
    return 4.0 * math.pi * radius_m**2


def sphere_volume(radius_m: float) -> float:
    """Return `(4/3)*pi*R^3` in cubic metres for radius in metres."""
    radius_m = _require_positive(radius_m, "radius_m")
    return (4.0 / 3.0) * math.pi * radius_m**3


def surface_to_volume(radius_m: float) -> float:
    """Return spherical `A/V = 3/R` in inverse metres."""
    radius_m = _require_positive(radius_m, "radius_m")
    return 3.0 / radius_m


def normalized_surface_to_volume(radius_m: float, reference_length_m: float) -> float:
    """Return dimensionless `L_0*A/V = 3*L_0/R`."""
    radius_m = _require_positive(radius_m, "radius_m")
    reference_length_m = _require_positive(reference_length_m, "reference_length_m")
    return reference_length_m * surface_to_volume(radius_m)


def volume_entropy_density(entropy_j_per_k: float, volume_m3: float) -> float:
    """Return `S/V` in joules per kelvin per cubic metre."""
    entropy_j_per_k = _require_nonnegative(entropy_j_per_k, "entropy_j_per_k")
    volume_m3 = _require_positive(volume_m3, "volume_m3")
    return entropy_j_per_k / volume_m3


def surface_entropy_density(entropy_j_per_k: float, area_m2: float) -> float:
    """Return `S/A` in joules per kelvin per square metre."""
    entropy_j_per_k = _require_nonnegative(entropy_j_per_k, "entropy_j_per_k")
    area_m2 = _require_positive(area_m2, "area_m2")
    return entropy_j_per_k / area_m2


def critical_volume_entropy_density(
    critical_surface_entropy_density_j_per_k_m2: float,
    radius_m: float,
) -> float:
    """Convert a surface entropy capacity to its spherical volume equivalent."""
    sigma_crit = _require_nonnegative(
        critical_surface_entropy_density_j_per_k_m2,
        "critical_surface_entropy_density_j_per_k_m2",
    )
    return sigma_crit * surface_to_volume(radius_m)


def entropy_capacity_ratio(
    system_volume_entropy_density_j_per_k_m3: float,
    critical_volume_entropy_density_j_per_k_m3: float,
) -> float:
    """Return dimensionless `eta_S = s_system/s_crit`."""
    system_density = _require_nonnegative(
        system_volume_entropy_density_j_per_k_m3,
        "system_volume_entropy_density_j_per_k_m3",
    )
    critical_density = _require_positive(
        critical_volume_entropy_density_j_per_k_m3,
        "critical_volume_entropy_density_j_per_k_m3",
    )
    return system_density / critical_density


def temperature_coefficient(radius_m: float, temperature_k: float) -> float:
    """Return `kappa_T = (A/V)/T = 3/(R*T)` in `m^-1 K^-1`.

    This exposes the dimensions of the legacy relationship. It does not assert
    that the returned coefficient is universal.
    """
    temperature_k = _require_positive(temperature_k, "temperature_k")
    return surface_to_volume(radius_m) / temperature_k

