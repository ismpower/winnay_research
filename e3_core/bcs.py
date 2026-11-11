"""Weak-coupling BCS baseline for superconductivity comparisons.

Every quantity is reduced and dimensionless; the derivation and its hand checks
are in `docs/BCS_BASELINE.md`:

    t     = T/Tc
    delta = Delta(T)/(k_B Tc)
    C/(gamma Tc), S/(gamma Tc)   with gamma the normal-state Sommerfeld coefficient

The model is the cutoff-free weak-coupling limit (hbar omega_D >> k_B Tc).
It is established physics, not an E3 result, and contains no Bruno constant.
Only the Python standard library is used.
"""

from __future__ import annotations

import math
from functools import lru_cache

# Upper limit of numerical x-integration for the gap equation. For t <= 1 and
# x >= 100, tanh(x/2) and tanh(E/(2t)) both equal 1 in double precision, so the
# remaining tail is integrated in closed form (docs/BCS_BASELINE.md, section 2).
_GAP_CUTOFF = 100.0
# Thermal integrands contain f(1-f) or s(z), which are below 1e-24 for z >= 60.
_THERMAL_CUTOFF = 60.0
_REL_TOL = 1.0e-12
_MAX_DEPTH = 60
_GL_ORDER = 10


# ---------------------------------------------------------------------------
# Quadrature
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def gauss_legendre(n: int) -> tuple[tuple[float, ...], tuple[float, ...]]:
    """Return Gauss-Legendre nodes and weights on [-1, 1].

    Nodes are roots of the Legendre polynomial P_n, found by Newton iteration
    from the standard cosine initial guess. The rule integrates polynomials of
    degree <= 2n-1 exactly.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    def legendre_and_derivative(x: float) -> tuple[float, float]:
        # Three-term recurrence k P_k = (2k-1) x P_{k-1} - (k-1) P_{k-2}, and
        # (1 - x^2) P_n'(x) = n (P_{n-1}(x) - x P_n(x)).
        p_prev, p = 1.0, x
        for k in range(2, n + 1):
            p_prev, p = p, ((2 * k - 1) * x * p - (k - 1) * p_prev) / k
        return p, n * (p_prev - x * p) / (1.0 - x * x)

    nodes = []
    weights = []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p, dp = legendre_and_derivative(x)
            step = p / dp
            x -= step
            if abs(step) < 1.0e-16:
                break
        _, dp = legendre_and_derivative(x)
        nodes.append(x)
        weights.append(2.0 / ((1.0 - x * x) * dp * dp))
    return tuple(nodes), tuple(weights)


def _gl_panel(func, a: float, b: float) -> float:
    nodes, weights = gauss_legendre(_GL_ORDER)
    half = 0.5 * (b - a)
    mid = 0.5 * (a + b)
    return half * math.fsum(w * func(mid + half * x) for x, w in zip(nodes, weights))


def integrate(func, a: float, b: float, rel_tol: float = _REL_TOL) -> float:
    """Adaptive Gauss-Legendre integral of a smooth function on [a, b].

    A panel is accepted when the one-panel and two-half-panel estimates agree to
    `rel_tol` relative to the running magnitude of the integral. Raises
    RuntimeError if the subdivision depth limit is reached.
    """
    if b < a:
        raise ValueError("require a <= b")
    if a == b:
        return 0.0
    whole = _gl_panel(func, a, b)
    scale = [abs(whole)]
    pieces: list[float] = []

    def recurse(lo: float, hi: float, estimate: float, depth: int) -> None:
        mid = 0.5 * (lo + hi)
        left = _gl_panel(func, lo, mid)
        right = _gl_panel(func, mid, hi)
        refined = left + right
        scale[0] = max(scale[0], abs(refined))
        if abs(refined - estimate) <= rel_tol * scale[0] or (refined == estimate):
            pieces.append(refined)
            return
        if depth >= _MAX_DEPTH:
            raise RuntimeError("adaptive quadrature did not converge")
        recurse(lo, mid, left, depth + 1)
        recurse(mid, hi, right, depth + 1)

    recurse(a, b, whole, 0)
    return math.fsum(pieces)


# ---------------------------------------------------------------------------
# Numerically stable elementary functions
# ---------------------------------------------------------------------------

def _sech2(u: float) -> float:
    """Return sech(u)^2 = 4 e^{-2|u|} / (1 + e^{-2|u|})^2 without overflow."""
    e = math.exp(-2.0 * abs(u))
    return 4.0 * e / (1.0 + e) ** 2


def _fermi_f_one_minus_f(z: float) -> float:
    """Return f(1-f) for f = 1/(e^z + 1); equals e^{-|z|}/(1 + e^{-|z|})^2."""
    e = math.exp(-abs(z))
    return e / (1.0 + e) ** 2


def _quasiparticle_entropy(z: float) -> float:
    """Return s(z) = -f ln f - (1-f) ln(1-f) = ln(1 + e^{-z}) + z f, z >= 0."""
    e = math.exp(-z)
    return math.log1p(e) + z * e / (1.0 + e)


def _tanh_over(x: float, scale: float) -> float:
    """Return tanh(x/scale)/x, with the x -> 0 limit 1/scale."""
    if x == 0.0:
        return 1.0 / scale
    return math.tanh(x / scale) / x


# ---------------------------------------------------------------------------
# Gap equation F(y, t) = 0 with y = delta^2
# ---------------------------------------------------------------------------

def _require_reduced_temperature(t: float, allow_zero: bool) -> float:
    t = float(t)
    lower_ok = t >= 0.0 if allow_zero else t > 0.0
    if not math.isfinite(t) or not lower_ok or t > 1.0:
        bound = "[0, 1]" if allow_zero else "(0, 1]"
        raise ValueError(f"reduced temperature t must lie in {bound}")
    return t


def gap_function(y: float, t: float) -> float:
    """Return F(y, t); the gap equation is F(delta^2, t) = 0."""
    if y < 0.0:
        raise ValueError("y = delta^2 must be nonnegative")
    if t == 0.0 and y == 0.0:
        return math.inf  # int_0 (1/x - tanh(x/2)/x) dx diverges logarithmically

    def integrand(x: float) -> float:
        energy = math.sqrt(x * x + y)
        first = 1.0 / energy if t == 0.0 else _tanh_over(energy, 2.0 * t)
        return first - _tanh_over(x, 2.0)

    x_max = _GAP_CUTOFF
    energy_max = math.sqrt(x_max * x_max + y)
    # -ln((X + E_X)/(2X)) = -log1p((E_X - X)/(2X)), and E_X - X = y/(E_X + X).
    tail = -math.log1p(y / ((energy_max + x_max) * 2.0 * x_max))
    return integrate(integrand, 0.0, x_max) + tail


_SERIES_SWITCH = 1.0e-2


def _gap_dy_integrand(energy: float, t: float) -> float:
    """Return (u sech^2 u - tanh u)/(16 t^3 u^3) with u = E/(2t), or -1/(2E^3) at t = 0.

    For u < 1e-2 the Taylor series -1/24 + u^2/30 - 17 u^4/840 (times t^-3) is
    used; the omitted term is 31 u^6/2835 < 1.1e-14, while the direct formula
    there loses accuracy to cancellation (its numerator is of order u^3).
    """
    if t == 0.0:
        return -0.5 / energy**3
    u = energy / (2.0 * t)
    if u < _SERIES_SWITCH:
        u2 = u * u
        return (-1.0 / 24.0 + u2 / 30.0 - 17.0 * u2 * u2 / 840.0) / t**3
    return (u * _sech2(u) - math.tanh(u)) / (16.0 * t**3 * u**3)


def gap_function_dy(y: float, t: float) -> float:
    """Return dF/dy at (y, t). Always negative."""
    if y < 0.0:
        raise ValueError("y = delta^2 must be nonnegative")

    def integrand(x: float) -> float:
        return _gap_dy_integrand(math.sqrt(x * x + y), t)

    x_max = _GAP_CUTOFF
    energy_max = math.sqrt(x_max * x_max + y)
    tail = -0.5 / (energy_max * (energy_max + x_max))
    return integrate(integrand, 0.0, x_max) + tail


def gap_function_dt(y: float, t: float) -> float:
    """Return dF/dt at (y, t) for 0 < t <= 1. Always negative."""
    if t <= 0.0:
        raise ValueError("dF/dt is evaluated only for t > 0")

    def integrand(x: float) -> float:
        return _sech2(math.sqrt(x * x + y) / (2.0 * t))

    # sech^2(u) < 2e-30 for u > 35, so x > 70 t contributes negligibly.
    return -integrate(integrand, 0.0, 70.0 * t) / (2.0 * t * t)


@lru_cache(maxsize=4096)
def _gap_squared(t: float) -> float:
    if t == 1.0:
        return 0.0
    # F(0, t) = ln(1/t) > 0 for t < 1 and F decreases in y, so the root lies in
    # (0, y_hi] once F(y_hi, t) < 0. delta <= delta(0) < 2 gives y_hi = 4.
    lo, hi = 0.0, 4.0
    if gap_function(hi, t) >= 0.0:
        raise RuntimeError("gap root not bracketed")
    y = 3.0 if t < 0.5 else 3.0 * (1.0 - t)
    for _ in range(200):
        value = gap_function(y, t)
        if value > 0.0:
            lo = y
        else:
            hi = y
        step = value / gap_function_dy(y, t)
        candidate = y - step
        if not (lo < candidate < hi):
            candidate = 0.5 * (lo + hi)
        if abs(candidate - y) <= 1.0e-14 * max(candidate, 1.0e-300):
            return candidate
        y = candidate
        if hi - lo <= 1.0e-15 * hi:
            return 0.5 * (lo + hi)
    raise RuntimeError("gap equation did not converge")


def gap_ratio(t: float) -> float:
    """Return Delta(T)/(k_B Tc) for reduced temperature 0 <= t <= 1."""
    t = _require_reduced_temperature(t, allow_zero=True)
    return math.sqrt(_gap_squared(t))


def gap_squared_slope(t: float) -> float:
    """Return d(delta^2)/dt on the superconducting branch, 0 < t <= 1.

    At t = 1 this is the left limit t -> 1^-.
    """
    t = _require_reduced_temperature(t, allow_zero=False)
    y = _gap_squared(t)
    return -gap_function_dt(y, t) / gap_function_dy(y, t)


# ---------------------------------------------------------------------------
# Thermodynamics in units of gamma Tc
# ---------------------------------------------------------------------------

_SIX_OVER_PI2 = 6.0 / math.pi**2


def entropy_ratio(t: float) -> float:
    """Return superconducting electronic entropy S_s/(gamma Tc), 0 <= t <= 1."""
    t = _require_reduced_temperature(t, allow_zero=True)
    if t == 0.0:
        return 0.0
    y = _gap_squared(t)

    def integrand(x: float) -> float:
        return _quasiparticle_entropy(math.sqrt(x * x + y) / t)

    return _SIX_OVER_PI2 * integrate(integrand, 0.0, _THERMAL_CUTOFF * t)


def heat_capacity_ratio(t: float) -> float:
    """Return superconducting electronic heat capacity C_s/(gamma Tc), 0 < t <= 1.

    At t = 1 this is the superconducting-side value just below Tc.
    """
    t = _require_reduced_temperature(t, allow_zero=False)
    y = _gap_squared(t)
    half_slope = 0.5 * gap_squared_slope(t)

    def integrand(x: float) -> float:
        energy_sq = x * x + y
        return _fermi_f_one_minus_f(math.sqrt(energy_sq) / t) * (energy_sq / t - half_slope)

    return _SIX_OVER_PI2 * integrate(integrand, 0.0, _THERMAL_CUTOFF * t) / t


def normal_heat_capacity_ratio(t: float) -> float:
    """Return normal-state electronic heat capacity C_n/(gamma Tc) = t."""
    return _require_reduced_temperature(t, allow_zero=True)


def heat_capacity_crossover(tol: float = 1.0e-12) -> float:
    """Return t* in (0, 1) where C_s = C_n, found by bisection.

    g(t) = C_s/(gamma Tc) - t is negative at t = 0.2 and positive at t = 1.
    The tests check that g has a single sign change on (0, 1).
    """
    lo, hi = 0.2, 1.0
    if not (heat_capacity_ratio(lo) - lo < 0.0 < heat_capacity_ratio(hi) - hi):
        raise RuntimeError("crossover not bracketed")
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if heat_capacity_ratio(mid) - mid < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
