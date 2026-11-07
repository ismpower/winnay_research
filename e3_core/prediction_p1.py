"""Prediction P1: lattice-capacity crossing in superconducting aluminium.

Implements every quantity used by docs/PREREGISTRATION_P1.md:

- the threshold entropy per atom, a * (A/V), for any sample geometry;
- the active entropy per atom (weak-coupling BCS electrons + Debye phonons);
- the predicted crossing temperature and its prefactor band;
- the prefactor-free two-sample relation;
- the operational departure temperature in measured data;
- a first-principles bound on nuclear-spin (Zeeman) heat capacity.

Molar quantities are SI (J mol^-1 K^-n). Entropies "per atom" are in units of k_B.
"""

from __future__ import annotations

import math
from typing import Callable, Sequence

from . import bcs
from .constants import AVOGADRO_CONSTANT_PER_MOL, BOLTZMANN_CONSTANT_J_PER_K

GAS_CONSTANT_J_PER_MOL_K = AVOGADRO_CONSTANT_PER_MOL * BOLTZMANN_CONSTANT_J_PER_K
PREFACTOR_BAND = (0.25, 4.0)


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


# ---------------------------------------------------------------------------
# Threshold and active entropy
# ---------------------------------------------------------------------------

def lattice_threshold_per_atom(spacing_m: float, area_over_volume_per_m: float) -> float:
    """Return a * (A/V): the active entropy per atom (in k_B) at which eta_S = 1.

    From eta_S = S_act/((k_B/a^2) A) with V = N a^3. For a sphere A/V = 3/R.
    """
    return _positive(spacing_m, "spacing_m") * _positive(area_over_volume_per_m, "area_over_volume_per_m")


def debye_molar_entropy(temperature_k: float, debye_k: float) -> float:
    """Return low-temperature Debye entropy (4 pi^4/5) R (T/Theta)^3, valid for T << Theta."""
    ratio = _positive(temperature_k, "temperature_k") / _positive(debye_k, "debye_k")
    if ratio > 0.02:
        raise ValueError("T^3 Debye law used outside T < Theta/50")
    return 0.8 * math.pi**4 * GAS_CONSTANT_J_PER_MOL_K * ratio**3


def debye_molar_heat_capacity(temperature_k: float, debye_k: float) -> float:
    """Return low-temperature Debye heat capacity (12 pi^4/5) R (T/Theta)^3."""
    return 3.0 * debye_molar_entropy(temperature_k, debye_k)


def active_entropy_per_atom(temperature_k: float, gamma: float, tc_k: float, debye_k: float) -> float:
    """Return S_act/(N k_B): zero-field BCS electronic + Debye phonon entropy, T <= Tc."""
    temperature_k = _positive(temperature_k, "temperature_k")
    tc_k = _positive(tc_k, "tc_k")
    if temperature_k > tc_k:
        raise ValueError("superconducting-state entropy requires T <= Tc")
    electrons = bcs.entropy_ratio(temperature_k / tc_k) * _positive(gamma, "gamma") * tc_k
    return (electrons + debye_molar_entropy(temperature_k, debye_k)) / GAS_CONSTANT_J_PER_MOL_K


def baseline_molar_heat_capacity(temperature_k: float, gamma: float, tc_k: float, debye_k: float) -> float:
    """Return the no-E3 baseline C_s: BCS electronic + Debye phonon, J mol^-1 K^-1."""
    t = _positive(temperature_k, "temperature_k") / _positive(tc_k, "tc_k")
    electrons = bcs.heat_capacity_ratio(t) * _positive(gamma, "gamma") * tc_k
    return electrons + debye_molar_heat_capacity(temperature_k, debye_k)


# ---------------------------------------------------------------------------
# Predictions
# ---------------------------------------------------------------------------

def predicted_crossing_temperature(
    threshold_per_atom: float,
    gamma: float,
    tc_k: float,
    debye_k: float,
    prefactor: float = 1.0,
    lower_k: float | None = None,
) -> float:
    """Return T* where active entropy per atom = prefactor * threshold (bisection).

    `prefactor` is the unknown O(1) factor in sigma_crit = prefactor * k_B/a^2.
    Active entropy increases strictly with T, so the root is unique.
    """
    target = _positive(prefactor, "prefactor") * _positive(threshold_per_atom, "threshold_per_atom")
    lo = lower_k if lower_k is not None else 0.02 * tc_k
    hi = tc_k

    def s(t: float) -> float:
        return active_entropy_per_atom(t, gamma, tc_k, debye_k)

    if not s(lo) < target < s(hi):
        raise ValueError("crossing not inside (lower bound, Tc)")
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if s(mid) < target else (lo, mid)
    return 0.5 * (lo + hi)


def predicted_band(threshold_per_atom: float, gamma: float, tc_k: float, debye_k: float) -> tuple[float, float, float]:
    """Return (T*(0.25), T*(1), T*(4)) for the registered prefactor band."""
    low, high = PREFACTOR_BAND
    return tuple(
        predicted_crossing_temperature(threshold_per_atom, gamma, tc_k, debye_k, f)
        for f in (low, 1.0, high)
    )


def partner_crossing_temperature(
    measured_t1_k: float,
    sample1: dict,
    sample2: dict,
) -> float:
    """Prefactor-free two-sample prediction.

    For samples of one material, eta_S = 1 at both crossings means
    S_act,1(T1)/threshold_1 = S_act,2(T2)/threshold_2, with the same unknown
    prefactor on both sides. Given the measured T1, return the predicted T2.
    Each sample dict needs: spacing_m, area_over_volume_per_m, gamma, tc_k, debye_k.
    """
    th1 = lattice_threshold_per_atom(sample1["spacing_m"], sample1["area_over_volume_per_m"])
    th2 = lattice_threshold_per_atom(sample2["spacing_m"], sample2["area_over_volume_per_m"])
    s1 = active_entropy_per_atom(measured_t1_k, sample1["gamma"], sample1["tc_k"], sample1["debye_k"])
    implied_prefactor = s1 / th1
    return predicted_crossing_temperature(
        th2, sample2["gamma"], sample2["tc_k"], sample2["debye_k"], implied_prefactor
    )


# ---------------------------------------------------------------------------
# Operational observable
# ---------------------------------------------------------------------------

def departure_temperature(
    temperatures_k: Sequence[float],
    heat_capacities: Sequence[float],
    relative_uncertainties: Sequence[float],
    baseline: Callable[[float], float],
    n_sigma: float = 3.0,
) -> float | None:
    """Return the registered departure temperature, or None.

    Sort the points by temperature. A point is "in excess" if
    (C - C_base)/C_base > n_sigma * u. The departure temperature is the highest
    measured T_k such that T_k and every measured point below it are in excess,
    with at least two such points. Returns None if there is no such run.
    """
    rows = sorted(zip(temperatures_k, heat_capacities, relative_uncertainties))
    if len(rows) < 2:
        return None
    in_excess = []
    for t, c, u in rows:
        base = baseline(t)
        in_excess.append((c - base) / base > n_sigma * _positive(u, "relative uncertainty"))
    run = 0
    while run < len(rows) and in_excess[run]:
        run += 1
    return rows[run - 1][0] if run >= 2 else None


# ---------------------------------------------------------------------------
# Nuclear-spin bound
# ---------------------------------------------------------------------------

def zeeman_heat_capacity_per_spin(spin: float, moment_j_per_t: float, field_t: float, temperature_k: float) -> float:
    """Exact Schottky heat capacity C/(N k_B) for levels E_m = -(mu/I) m B, m = -I..I."""
    beta = 1.0 / (BOLTZMANN_CONSTANT_J_PER_K * _positive(temperature_k, "temperature_k"))
    levels = [-(moment_j_per_t / spin) * (spin - j) * field_t for j in range(int(round(2 * spin)) + 1)]
    weights = [math.exp(-beta * (e - min(levels))) for e in levels]
    z = math.fsum(weights)
    mean = math.fsum(w * e for w, e in zip(weights, levels)) / z
    mean_sq = math.fsum(w * e * e for w, e in zip(weights, levels)) / z
    return beta**2 * (mean_sq - mean**2)


def zeeman_heat_capacity_high_t(spin: float, moment_j_per_t: float, field_t: float, temperature_k: float) -> float:
    """High-temperature limit (I+1)/(3I) (mu B/(k_B T))^2 of the Zeeman heat capacity."""
    x = moment_j_per_t * field_t / (BOLTZMANN_CONSTANT_J_PER_K * _positive(temperature_k, "temperature_k"))
    return (spin + 1.0) / (3.0 * spin) * x * x
