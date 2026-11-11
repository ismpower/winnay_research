"""Physical constants for the E3 restart: single source of truth.

Exact constants are the 2019 SI defining values. G is the only measured input.
Every other value is computed here from those inputs, never hardcoded.
Tests in `e3_core/tests/test_constants.py` compare the results with the
independently sourced `reference/known_physics_reference.json` and with
algebraic identities.

Symbols follow `docs/NOTATION.md`. Nothing in this module is a Bruno constant.
The legacy coefficient routes at the bottom are evaluations of the coefficient
role `kappa_T = (A/V)/T`, kept so their algebra stays under test; they are not
accepted universal constants.
"""

from __future__ import annotations

import math

from .geometry import temperature_coefficient

# ---------------------------------------------------------------------------
# Exact 2019 SI defining constants
# ---------------------------------------------------------------------------

SPEED_OF_LIGHT_M_PER_S = 299_792_458.0
PLANCK_CONSTANT_J_S = 6.626_070_15e-34
BOLTZMANN_CONSTANT_J_PER_K = 1.380_649e-23
ELEMENTARY_CHARGE_C = 1.602_176_634e-19
AVOGADRO_CONSTANT_PER_MOL = 6.022_140_76e23

# Derived from an exact constant, so also exact in principle (rounded in floating point).
REDUCED_PLANCK_CONSTANT_J_S = PLANCK_CONSTANT_J_S / (2.0 * math.pi)

# ---------------------------------------------------------------------------
# Measured input
# ---------------------------------------------------------------------------

# CODATA 2018 recommended value and standard relative uncertainty.
GRAVITATIONAL_CONSTANT_M3_PER_KG_S2 = 6.674_30e-11
GRAVITATIONAL_CONSTANT_RELATIVE_UNCERTAINTY = 2.2e-5

# Short aliases used in formulas below.
_C = SPEED_OF_LIGHT_M_PER_S
_HBAR = REDUCED_PLANCK_CONSTANT_J_S
_K_B = BOLTZMANN_CONSTANT_J_PER_K
_G = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2


def _require_positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


# ---------------------------------------------------------------------------
# Planck units. G is a parameter so that tests can show where it cancels.
# Each Planck unit scales as G^(+-1/2), so it carries half of G's relative
# uncertainty: about 1.1e-5.
# ---------------------------------------------------------------------------

def planck_length(G: float = _G) -> float:
    """Return l_P = sqrt(hbar G / c^3) in metres."""
    return math.sqrt(_HBAR * _require_positive(G, "G") / _C**3)


def planck_time(G: float = _G) -> float:
    """Return t_P = sqrt(hbar G / c^5) in seconds."""
    return math.sqrt(_HBAR * _require_positive(G, "G") / _C**5)


def planck_mass(G: float = _G) -> float:
    """Return m_P = sqrt(hbar c / G) in kilograms."""
    return math.sqrt(_HBAR * _C / _require_positive(G, "G"))


def planck_energy(G: float = _G) -> float:
    """Return E_P = sqrt(hbar c^5 / G) in joules."""
    return math.sqrt(_HBAR * _C**5 / _require_positive(G, "G"))


def planck_temperature(G: float = _G) -> float:
    """Return T_P = sqrt(hbar c^5 / G) / k_B in kelvin."""
    return planck_energy(G) / _K_B


PLANCK_LENGTH_M = planck_length()
PLANCK_TIME_S = planck_time()
PLANCK_MASS_KG = planck_mass()
PLANCK_ENERGY_J = planck_energy()
PLANCK_TEMPERATURE_K = planck_temperature()


# ---------------------------------------------------------------------------
# Black-hole relations (Schwarzschild, non-rotating)
# ---------------------------------------------------------------------------

def schwarzschild_radius(mass_kg: float, G: float = _G) -> float:
    """Return R_s = 2 G M / c^2 in metres."""
    return 2.0 * _require_positive(G, "G") * _require_positive(mass_kg, "mass_kg") / _C**2


def hawking_temperature(mass_kg: float, G: float = _G) -> float:
    """Return T_H = hbar c^3 / (8 pi G M k_B) in kelvin."""
    mass_kg = _require_positive(mass_kg, "mass_kg")
    return _HBAR * _C**3 / (8.0 * math.pi * _require_positive(G, "G") * mass_kg * _K_B)


def bekenstein_hawking_surface_entropy_density(G: float = _G) -> float:
    """Return k_B / (4 l_P^2) = k_B c^3 / (4 G hbar) in J K^-1 m^-2.

    This is S_BH / A for a horizon. It is one candidate for sigma_crit
    (plan task 7), not an accepted choice.
    """
    return _K_B / (4.0 * planck_length(G) ** 2)


# ---------------------------------------------------------------------------
# Legacy coefficient routes (docs/NOTATION.md, "Legacy kappa values")
# ---------------------------------------------------------------------------

def kappa_t_planck_route_per_m_k(G: float = _G) -> float:
    """Return kappa_T^Pl = 3/(l_P T_P) in m^-1 K^-1.

    Algebraically equal to 3 k_B/(hbar c): G cancels. The legacy literal 1313
    is a misreport of this expression and is retired.
    """
    return temperature_coefficient(planck_length(G), planck_temperature(G))


def kappa_t_hawking_route_per_m_k(mass_kg: float, G: float = _G) -> float:
    """Return kappa_T^GW = 3/(R_s T_H) in m^-1 K^-1.

    Algebraically equal to 12 pi k_B/(hbar c): the mass and G cancel. The
    legacy literal 1366 came from a wrong T_H and is retired.
    """
    return temperature_coefficient(
        schwarzschild_radius(mass_kg, G), hawking_temperature(mass_kg, G)
    )
