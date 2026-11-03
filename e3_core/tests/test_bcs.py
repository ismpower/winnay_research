"""Tests for the weak-coupling BCS baseline.

Reference values are closed forms derived in docs/BCS_BASELINE.md, section 5.
They are mathematical constants, so they are independent of the numerical
method under test.
"""

import math
import unittest

from e3_core import bcs

EULER_GAMMA = 0.57721566490153286061  # Euler-Mascheroni constant
ZETA_3 = 1.20205690315959428540  # Apery's constant zeta(3)


def zeta3_by_series() -> float:
    """Independent check of ZETA_3 with an Euler-Maclaurin tail correction."""
    n = 2000
    head = math.fsum(1.0 / k**3 for k in range(1, n))
    # sum_{k>=n} k^-3 = 1/(2 n^2) + 1/(2 n^3) + 1/(4 n^4) + O(n^-6)
    return head + 1.0 / (2 * n**2) + 1.0 / (2 * n**3) + 1.0 / (4 * n**4)


class QuadratureTests(unittest.TestCase):
    def test_gauss_legendre_is_exact_to_degree_2n_minus_1(self):
        for n in (1, 2, 5, 10):
            nodes, weights = bcs.gauss_legendre(n)
            for degree in range(2 * n):
                exact = 0.0 if degree % 2 else 2.0 / (degree + 1)
                approx = math.fsum(w * x**degree for x, w in zip(nodes, weights))
                self.assertAlmostEqual(approx, exact, places=13, msg=(n, degree))

    def test_adaptive_integral_of_known_functions(self):
        self.assertAlmostEqual(bcs.integrate(math.exp, 0.0, 1.0), math.e - 1.0, places=14)
        # int_0^inf s(z) dz = pi^2/6 (normal-state entropy normalization)
        value = bcs.integrate(bcs._quasiparticle_entropy, 0.0, 60.0)
        self.assertAlmostEqual(value, math.pi**2 / 6.0, places=12)

    def test_reference_zeta3(self):
        self.assertAlmostEqual(zeta3_by_series(), ZETA_3, places=14)


class GapTests(unittest.TestCase):
    def test_zero_temperature_gap_is_pi_exp_minus_gamma(self):
        expected = math.pi * math.exp(-EULER_GAMMA)
        self.assertAlmostEqual(bcs.gap_ratio(0.0), expected, places=11)

    def test_gap_vanishes_at_tc_and_decreases_with_temperature(self):
        self.assertEqual(bcs.gap_ratio(1.0), 0.0)
        temperatures = [0.0, 0.2, 0.4, 0.6, 0.8, 0.95, 0.999]
        gaps = [bcs.gap_ratio(t) for t in temperatures]
        for colder, warmer in zip(gaps, gaps[1:]):
            self.assertGreater(colder, warmer)

    def test_gap_satisfies_its_equation(self):
        for t in (0.05, 0.3, 0.7, 0.99):
            y = bcs.gap_ratio(t) ** 2
            self.assertLess(abs(bcs.gap_function(y, t)), 1.0e-12)

    def test_small_u_series_matches_direct_formula(self):
        # Where the direct formula is accurate (u = 0.02 to 0.1), it must equal
        # the series used below u = 1e-2 plus the next two terms of the same
        # Taylor expansion, 31 u^6/2835 - 691 u^8/124740. The remaining
        # O(u^10) term is below 1e-11 relative at u = 0.1.
        t = 0.7
        for u in (0.02, 0.05, 0.1):
            energy = 2.0 * t * u
            direct = bcs._gap_dy_integrand(energy, t)
            u2 = u * u
            series = (-1.0 / 24.0 + u2 / 30.0 - 17.0 * u2 * u2 / 840.0) / t**3
            omitted = (31.0 * u2**3 / 2835.0 - 691.0 * u2**4 / 124740.0) / t**3
            self.assertLess(abs(direct - series - omitted), 1.0e-11 * abs(direct))
        # The switch at u = 1e-2 is continuous to near machine precision.
        below = bcs._gap_dy_integrand(2.0 * t * 0.01 * (1 - 1e-12), t)
        above = bcs._gap_dy_integrand(2.0 * t * 0.01 * (1 + 1e-12), t)
        self.assertLess(abs(below - above), 1.0e-11 * abs(above))

    def test_gap_equation_derivative_at_tc(self):
        expected = -7.0 * ZETA_3 / (8.0 * math.pi**2)
        self.assertAlmostEqual(bcs.gap_function_dy(0.0, 1.0), expected, places=12)

    def test_gap_squared_slope_at_tc(self):
        expected = -8.0 * math.pi**2 / (7.0 * ZETA_3)
        self.assertAlmostEqual(bcs.gap_squared_slope(1.0), expected, places=10)

    def test_slope_matches_finite_difference_of_gap(self):
        t, h = 0.6, 1.0e-4
        numeric = (bcs.gap_ratio(t + h) ** 2 - bcs.gap_ratio(t - h) ** 2) / (2 * h)
        self.assertAlmostEqual(bcs.gap_squared_slope(t), numeric, places=7)


class ThermodynamicTests(unittest.TestCase):
    def test_entropy_is_normal_at_tc(self):
        self.assertAlmostEqual(bcs.entropy_ratio(1.0), 1.0, places=12)
        self.assertEqual(bcs.entropy_ratio(0.0), 0.0)

    def test_heat_capacity_jump_at_tc(self):
        jump = bcs.heat_capacity_ratio(1.0) - bcs.normal_heat_capacity_ratio(1.0)
        self.assertAlmostEqual(jump, 12.0 / (7.0 * ZETA_3), places=10)

    def test_heat_capacity_equals_t_dS_dt(self):
        h = 1.0e-4
        for t in (0.3, 0.5, 0.8):
            numeric = t * (bcs.entropy_ratio(t + h) - bcs.entropy_ratio(t - h)) / (2 * h)
            self.assertAlmostEqual(bcs.heat_capacity_ratio(t), numeric, places=7)

    def _integrate_over_t(self, func):
        # c_s is smooth on [0, 1): all derivatives vanish as t -> 0 and the
        # function is analytic up to t = 1^-. Composite Gauss-Legendre suffices.
        nodes, weights = bcs.gauss_legendre(10)
        edges = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        total = []
        for a, b in zip(edges, edges[1:]):
            half, mid = 0.5 * (b - a), 0.5 * (a + b)
            total.extend(half * w * func(mid + half * x) for x, w in zip(nodes, weights))
        return math.fsum(total)

    def test_entropy_balance_between_zero_and_tc(self):
        balance = self._integrate_over_t(lambda t: bcs.heat_capacity_ratio(t) / t - 1.0)
        self.assertAlmostEqual(balance, 0.0, places=10)

    def test_condensation_energy(self):
        energy = self._integrate_over_t(lambda t: bcs.heat_capacity_ratio(t) - t)
        self.assertAlmostEqual(energy, 0.75 * math.exp(-2.0 * EULER_GAMMA), places=10)


class CrossoverTests(unittest.TestCase):
    def test_crossover_is_a_root_and_unique(self):
        t_star = bcs.heat_capacity_crossover()
        self.assertLess(abs(bcs.heat_capacity_ratio(t_star) - t_star), 1.0e-10)
        grid = [0.02 * k for k in range(1, 51)]
        signs = [bcs.heat_capacity_ratio(t) - t > 0.0 for t in grid]
        changes = [i for i in range(1, len(signs)) if signs[i] != signs[i - 1]]
        self.assertEqual(len(changes), 1)
        self.assertTrue(grid[changes[0] - 1] < t_star < grid[changes[0]])

    def test_crossover_value(self):
        # Regression value. Cross-checked to 1e-13 against an independent
        # Matsubara-sum implementation (scipy) on 2026-11-03.
        self.assertAlmostEqual(bcs.heat_capacity_crossover(), 0.5147917502752, places=11)


class InputValidationTests(unittest.TestCase):
    def test_out_of_range_temperatures_fail_loudly(self):
        for bad in (-0.1, 1.1, math.nan, math.inf):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    bcs.gap_ratio(bad)
        with self.assertRaises(ValueError):
            bcs.heat_capacity_ratio(0.0)


if __name__ == "__main__":
    unittest.main()
