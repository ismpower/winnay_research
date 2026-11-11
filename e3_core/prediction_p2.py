"""Prediction P2: lattice-capacity crossing in insulating single crystals.

Implements every quantity used by docs/PREREGISTRATION_P2.md. In an insulating
crystal at T << Theta_D the active entropy is the phonon entropy, so the
crossing has a closed form with no BCS model:

    S_act/(N k_B) = (4 pi^4/5) (T/Theta_D)^3 = f * a * (A/V)
    T* = Theta_D * (5 f a (A/V) / (4 pi^4))^(1/3)

Entropies "per atom" are in units of k_B; heat capacities "per atom" likewise.
The departure-temperature rule is reused unchanged from e3_core.prediction_p1.
"""

from __future__ import annotations

import math
from typing import Sequence

from .constants import BOLTZMANN_CONSTANT_J_PER_K, REDUCED_PLANCK_CONSTANT_J_S
from .prediction_p1 import PREFACTOR_BAND, departure_temperature, lattice_threshold_per_atom  # noqa: F401

DEBYE_ENTROPY_COEFFICIENT = 4.0 * math.pi**4 / 5.0       # S/(N k_B) = c (T/Theta)^3
DEBYE_HEAT_CAPACITY_COEFFICIENT = 12.0 * math.pi**4 / 5.0  # C/(N k_B) = 3c (T/Theta)^3
DEBYE_VALIDITY = 1.0 / 50.0                               # T^3 law used only for T < Theta/50


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


def phonon_entropy_per_atom(temperature_k: float, debye_k: float) -> float:
    """Return (4 pi^4/5)(T/Theta)^3, the low-temperature Debye entropy per atom (k_B)."""
    ratio = _positive(temperature_k, "temperature_k") / _positive(debye_k, "debye_k")
    if ratio > DEBYE_VALIDITY:
        raise ValueError("T^3 Debye law used outside T < Theta/50")
    return DEBYE_ENTROPY_COEFFICIENT * ratio**3


def phonon_heat_capacity_per_atom(temperature_k: float, debye_k: float) -> float:
    """Return (12 pi^4/5)(T/Theta)^3, the low-temperature Debye heat capacity per atom (k_B)."""
    return 3.0 * phonon_entropy_per_atom(temperature_k, debye_k)


def predicted_crossing_temperature(threshold_per_atom: float, debye_k: float, prefactor: float = 1.0) -> float:
    """Return T* = Theta (5 f s_th/(4 pi^4))^(1/3), where phonon entropy = f * threshold."""
    target = _positive(prefactor, "prefactor") * _positive(threshold_per_atom, "threshold_per_atom")
    t_star = _positive(debye_k, "debye_k") * (target / DEBYE_ENTROPY_COEFFICIENT) ** (1.0 / 3.0)
    if t_star / debye_k > DEBYE_VALIDITY:
        raise ValueError("crossing lies outside the T < Theta/50 range of the Debye law")
    return t_star


def predicted_band(threshold_per_atom: float, debye_k: float) -> tuple[float, float, float]:
    """Return (T*(0.25), T*(1), T*(4)) for the registered prefactor band."""
    low, high = PREFACTOR_BAND
    return tuple(predicted_crossing_temperature(threshold_per_atom, debye_k, f) for f in (low, 1.0, high))


def partner_crossing_temperature(measured_t1_k: float, sample1: dict, sample2: dict) -> float:
    """Prefactor-free two-sample relation.

    eta_S = 1 at both crossings with one unknown prefactor gives
    (T1/Theta1)^3/s_th1 = (T2/Theta2)^3/s_th2, so
    T2 = Theta2 * (T1/Theta1) * (s_th2/s_th1)^(1/3).
    Each sample dict needs: spacing_m, area_over_volume_per_m, debye_k.
    """
    th1 = lattice_threshold_per_atom(sample1["spacing_m"], sample1["area_over_volume_per_m"])
    th2 = lattice_threshold_per_atom(sample2["spacing_m"], sample2["area_over_volume_per_m"])
    t1 = _positive(measured_t1_k, "measured_t1_k")
    return sample2["debye_k"] * (t1 / sample1["debye_k"]) * (th2 / th1) ** (1.0 / 3.0)


# ---------------------------------------------------------------------------
# Baseline: Debye coefficient from an independent source
# ---------------------------------------------------------------------------

def debye_temperature_from_sound_velocities(atom_density_per_m3: float, v_longitudinal: float, v_transverse: float) -> float:
    """Return Theta = (hbar/k_B) (6 pi^2 n)^(1/3) v_m, with 3/v_m^3 = 1/v_l^3 + 2/v_t^3.

    Isotropic average; for an anisotropic crystal, v_l and v_t must be the
    stated directional averages.
    """
    n = _positive(atom_density_per_m3, "atom_density_per_m3")
    vl = _positive(v_longitudinal, "v_longitudinal")
    vt = _positive(v_transverse, "v_transverse")
    v_mean = (3.0 / (1.0 / vl**3 + 2.0 / vt**3)) ** (1.0 / 3.0)
    return REDUCED_PLANCK_CONSTANT_J_S / BOLTZMANN_CONSTANT_J_PER_K * (6.0 * math.pi**2 * n) ** (1.0 / 3.0) * v_mean


def fit_low_temperature_coefficients(
    temperatures_k: Sequence[float], heat_capacities: Sequence[float], relative_uncertainties: Sequence[float]
) -> tuple[float, float]:
    """Weighted least squares of C/T^3 = A + B T^2. Returns (A, B).

    Used only on points inside the registered fit window, above the predicted
    band; A is the T -> 0 Debye coefficient used for the baseline C = A T^3.
    """
    rows = list(zip(temperatures_k, heat_capacities, relative_uncertainties))
    if len(rows) < 3:
        raise ValueError("need at least three points to fit A and B")
    s = sx = sy = sxx = sxy = 0.0
    for t, c, u in rows:
        t = _positive(t, "temperature")
        y = c / t**3
        x = t * t
        w = 1.0 / (_positive(u, "relative uncertainty") * y) ** 2
        s += w; sx += w * x; sy += w * y; sxx += w * x * x; sxy += w * x * y
    det = s * sxx - sx * sx
    if det <= 0.0:
        raise ValueError("fit is degenerate: temperatures must differ")
    a = (sxx * sy - sx * sxy) / det
    b = (s * sxy - sx * sy) / det
    return a, b


def debye_temperature_from_coefficient(coefficient_per_atom_kb: float) -> float:
    """Invert C/(N k_B) = (12 pi^4/5)(T/Theta)^3 = A T^3: Theta = (12 pi^4/(5 A))^(1/3)."""
    return (DEBYE_HEAT_CAPACITY_COEFFICIENT / _positive(coefficient_per_atom_kb, "coefficient")) ** (1.0 / 3.0)


def registered_fit_window(band_high_k: float, debye_k: float) -> tuple[float, float]:
    """Return the registered fallback fit window [1.5 T*(4), Theta/50] for A and B."""
    low = 1.5 * _positive(band_high_k, "band_high_k")
    high = DEBYE_VALIDITY * _positive(debye_k, "debye_k")
    if low >= high:
        raise ValueError("no room for a fit window above the band; use sound velocities")
    return low, high
