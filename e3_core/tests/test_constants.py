"""Tests for e3_core.constants.

Three kinds of check:
1. agreement with the independently sourced reference/known_physics_reference.json,
   to the precision its values are printed;
2. algebraic identities, evaluated by a route different from the code's;
3. cancellation: quantities whose formula contains no G must not change when G does.
"""

import json
import math
import unittest
from pathlib import Path

from e3_core import constants as k

REFERENCE_PATH = Path(__file__).resolve().parents[2] / "reference" / "known_physics_reference.json"


def load_reference() -> dict[str, dict]:
    data = json.loads(REFERENCE_PATH.read_text(encoding="utf-8"))
    return {
        entry["id"]: entry
        for category in data["categories"]
        for entry in category["entries"]
    }


REF = load_reference()
# Masses spanning the stellar to supermassive range, in solar masses.
SOLAR_MASS_KG = REF["M_sun"]["value"]
TEST_MASSES_KG = [m * SOLAR_MASS_KG for m in (1.0, 5.0, 62.0, 1.0e6, 1.0e9)]


def rel_diff(a: float, b: float) -> float:
    return abs(a - b) / abs(b)


class ExactConstantTests(unittest.TestCase):
    def test_exact_si_constants_equal_reference(self):
        for ref_id, value in (
            ("c", k.SPEED_OF_LIGHT_M_PER_S),
            ("h", k.PLANCK_CONSTANT_J_S),
            ("k_B", k.BOLTZMANN_CONSTANT_J_PER_K),
            ("e", k.ELEMENTARY_CHARGE_C),
            ("N_A", k.AVOGADRO_CONSTANT_PER_MOL),
        ):
            with self.subTest(ref_id=ref_id):
                self.assertEqual(REF[ref_id]["status"], "exact")
                self.assertEqual(value, REF[ref_id]["value"])

    def test_hbar_matches_reference_to_printed_precision(self):
        # CODATA prints hbar = 1.054 571 817... e-34, truncated rather than rounded
        # (h/(2 pi) = 1.0545718176...e-34). So the computed value must lie within
        # one unit of the last printed digit above the reference value.
        printed = REF["hbar"]["value"]
        self.assertGreater(k.REDUCED_PLANCK_CONSTANT_J_S, printed)
        self.assertLess(k.REDUCED_PLANCK_CONSTANT_J_S, printed + 1.0e-43)

    def test_hbar_is_computed_from_exact_h(self):
        expected = REF["h"]["value"] / (2.0 * math.pi)
        self.assertLess(rel_diff(k.REDUCED_PLANCK_CONSTANT_J_S, expected), 1.0e-16)

    def test_gravitational_constant_matches_reference(self):
        self.assertEqual(k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2, REF["G"]["value"])
        self.assertEqual(
            k.GRAVITATIONAL_CONSTANT_RELATIVE_UNCERTAINTY, REF["G"]["relative_uncertainty"]
        )


class PlanckUnitTests(unittest.TestCase):
    def test_planck_units_match_published_values(self):
        # CODATA prints l_P, t_P, m_P and T_P to 7 significant figures and the
        # reference prints E_P to 5; tolerance is half a unit in the last place.
        cases = (
            ("l_planck", k.PLANCK_LENGTH_M, 5.0e-7),
            ("t_planck", k.PLANCK_TIME_S, 5.0e-7),
            ("m_planck", k.PLANCK_MASS_KG, 5.0e-7),
            ("T_planck", k.PLANCK_TEMPERATURE_K, 5.0e-7),
            ("E_planck", k.PLANCK_ENERGY_J, 5.0e-5),
        )
        for ref_id, value, tolerance in cases:
            with self.subTest(ref_id=ref_id):
                self.assertLess(rel_diff(value, REF[ref_id]["value"]), tolerance)

    def test_planck_unit_identities(self):
        hbar, c, k_b = k.REDUCED_PLANCK_CONSTANT_J_S, k.SPEED_OF_LIGHT_M_PER_S, k.BOLTZMANN_CONSTANT_J_PER_K
        identities = (
            ("t_P = l_P/c", k.PLANCK_TIME_S, k.PLANCK_LENGTH_M / c),
            ("m_P = hbar/(l_P c)", k.PLANCK_MASS_KG, hbar / (k.PLANCK_LENGTH_M * c)),
            ("E_P = m_P c^2", k.PLANCK_ENERGY_J, k.PLANCK_MASS_KG * c**2),
            ("E_P = k_B T_P", k.PLANCK_ENERGY_J, k_b * k.PLANCK_TEMPERATURE_K),
            ("l_P T_P = hbar c/k_B", k.PLANCK_LENGTH_M * k.PLANCK_TEMPERATURE_K, hbar * c / k_b),
        )
        for name, left, right in identities:
            with self.subTest(identity=name):
                self.assertLess(rel_diff(left, right), 1.0e-15)

    def test_planck_units_scale_as_half_power_of_g(self):
        # Each Planck unit scales as G^(+1/2) or G^(-1/2), so it carries half of
        # G's relative uncertainty.
        factor = 1.0 + 1.0e-3
        g = k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        expected = math.sqrt(factor)
        self.assertAlmostEqual(k.planck_length(g * factor) / k.PLANCK_LENGTH_M, expected, places=14)
        self.assertAlmostEqual(k.planck_temperature(g) / k.planck_temperature(g * factor), expected, places=14)


class BlackHoleTests(unittest.TestCase):
    def test_schwarzschild_radius_of_the_sun(self):
        # IAU 2015 Resolution B3 fixes the nominal solar mass parameter
        # (GM)_sun^N = 1.3271244e20 m^3 s^-2 and derives the reference M_sun with
        # the CODATA 2014 G = 6.67408e-11. Multiplying that M_sun by the CODATA 2018
        # G used here shifts R_s by a known factor, which this test checks exactly.
        gm_nominal = 1.3271244e20
        g_2014 = 6.67408e-11
        nominal_radius = 2.0 * gm_nominal / k.SPEED_OF_LIGHT_M_PER_S**2
        expected_ratio = (k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2 / g_2014) * (
            SOLAR_MASS_KG / (gm_nominal / g_2014)
        )
        ratio = k.schwarzschild_radius(SOLAR_MASS_KG) / nominal_radius
        self.assertLess(rel_diff(ratio, expected_ratio), 1.0e-14)
        self.assertAlmostEqual(nominal_radius, 2953.25, places=2)
        # The mismatch is about 3e-5, which exceeds G's own uncertainty (2.2e-5).
        self.assertGreater(ratio - 1.0, k.GRAVITATIONAL_CONSTANT_RELATIVE_UNCERTAINTY)

    def test_hawking_product_is_mass_independent(self):
        expected = k.REDUCED_PLANCK_CONSTANT_J_S * k.SPEED_OF_LIGHT_M_PER_S / (
            4.0 * math.pi * k.BOLTZMANN_CONSTANT_J_PER_K
        )
        for mass in TEST_MASSES_KG:
            with self.subTest(mass_kg=mass):
                product = k.schwarzschild_radius(mass) * k.hawking_temperature(mass)
                self.assertLess(rel_diff(product, expected), 1.0e-15)

    def test_surface_entropy_density_matches_reference_formula(self):
        # Reference: S_BH = k_B c^3 A/(4 G hbar), so S_BH/A = k_B c^3/(4 G hbar).
        c, hbar, g = k.SPEED_OF_LIGHT_M_PER_S, k.REDUCED_PLANCK_CONSTANT_J_S, k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        expected = k.BOLTZMANN_CONSTANT_J_PER_K * c**3 / (4.0 * g * hbar)
        self.assertLess(rel_diff(k.bekenstein_hawking_surface_entropy_density(), expected), 1.0e-15)
        self.assertAlmostEqual(k.bekenstein_hawking_surface_entropy_density() / 1.3213063e46, 1.0, places=7)

    def test_surface_entropy_density_scales_as_inverse_g(self):
        base = k.bekenstein_hawking_surface_entropy_density()
        doubled = k.bekenstein_hawking_surface_entropy_density(2.0 * k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2)
        self.assertLess(rel_diff(doubled, 0.5 * base), 1.0e-15)


class LegacyCoefficientRouteTests(unittest.TestCase):
    """docs/NOTATION.md, 'Legacy kappa values'."""

    def setUp(self):
        self.k_over_hbar_c = k.BOLTZMANN_CONSTANT_J_PER_K / (
            k.REDUCED_PLANCK_CONSTANT_J_S * k.SPEED_OF_LIGHT_M_PER_S
        )

    def test_planck_route_equals_three_k_b_over_hbar_c(self):
        self.assertLess(rel_diff(k.kappa_t_planck_route_per_m_k(), 3.0 * self.k_over_hbar_c), 1.0e-15)
        self.assertAlmostEqual(k.kappa_t_planck_route_per_m_k(), 1310.11, places=2)

    def test_hawking_route_equals_twelve_pi_k_b_over_hbar_c_for_every_mass(self):
        expected = 12.0 * math.pi * self.k_over_hbar_c
        for mass in TEST_MASSES_KG:
            with self.subTest(mass_kg=mass):
                self.assertLess(rel_diff(k.kappa_t_hawking_route_per_m_k(mass), expected), 1.0e-15)
        self.assertAlmostEqual(k.kappa_t_hawking_route_per_m_k(SOLAR_MASS_KG), 16463.32, places=2)

    def test_routes_differ_by_exactly_four_pi(self):
        ratio = k.kappa_t_hawking_route_per_m_k(SOLAR_MASS_KG) / k.kappa_t_planck_route_per_m_k()
        self.assertLess(rel_diff(ratio, 4.0 * math.pi), 1.0e-15)

    def test_gravitational_constant_cancels_in_both_routes(self):
        g = k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        for scale in (0.5, 1.1, 10.0):
            with self.subTest(scale=scale):
                self.assertLess(
                    rel_diff(k.kappa_t_planck_route_per_m_k(g * scale), k.kappa_t_planck_route_per_m_k()),
                    1.0e-15,
                )
                self.assertLess(
                    rel_diff(
                        k.kappa_t_hawking_route_per_m_k(SOLAR_MASS_KG, g * scale),
                        k.kappa_t_hawking_route_per_m_k(SOLAR_MASS_KG),
                    ),
                    1.0e-15,
                )

    def test_retired_literals_are_not_reproduced(self):
        # 1313 is 0.22% above the Planck-route expression; 1366 is 91.7% below
        # the Hawking-route expression. Neither is a correct evaluation.
        self.assertGreater(rel_diff(1313.0, k.kappa_t_planck_route_per_m_k()), 2.0e-3)
        self.assertGreater(rel_diff(1366.0, k.kappa_t_hawking_route_per_m_k(SOLAR_MASS_KG)), 0.9)


class InputValidationTests(unittest.TestCase):
    def test_nonphysical_inputs_fail_loudly(self):
        for bad in (0.0, -1.0, math.nan, math.inf):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    k.schwarzschild_radius(bad)
                with self.assertRaises(ValueError):
                    k.planck_length(bad)


if __name__ == "__main__":
    unittest.main()
