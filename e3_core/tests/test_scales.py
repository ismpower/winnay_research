"""Tests for e3_core.scales: the algebra behind docs/TASK7_OPTIONS.md."""

import json
import math
import unittest
from pathlib import Path

from e3_core import constants as k
from e3_core import scales
from e3_core.geometry import sphere_area, sphere_volume

REF = {
    entry["id"]: entry
    for category in json.loads(
        (Path(__file__).resolve().parents[2] / "reference" / "known_physics_reference.json").read_text()
    )["categories"]
    for entry in category["entries"]
}


def rel_diff(a: float, b: float) -> float:
    return abs(a - b) / abs(b)


class ThermalPhotonLengthTests(unittest.TestCase):
    def test_length_times_temperature_is_hbar_c_over_k_b(self):
        expected = k.REDUCED_PLANCK_CONSTANT_J_S * k.SPEED_OF_LIGHT_M_PER_S / k.BOLTZMANN_CONSTANT_J_PER_K
        for t in (1.0e-6, 1.0, 300.0, 1.0e9):
            self.assertLess(rel_diff(scales.thermal_photon_length(t) * t, expected), 1.0e-15)

    def test_legacy_planck_route_is_radius_equals_photon_length(self):
        # beta_geom = kappa_T^Pl T  <=>  3/R = kappa_T^Pl T  <=>  R = hbar c/(k_B T).
        for t in (0.1, 1.0, 300.0):
            radius = 3.0 / (k.kappa_t_planck_route_per_m_k() * t)
            self.assertLess(rel_diff(radius, scales.thermal_photon_length(t)), 1.0e-15)

    def test_hawking_route_is_radius_equals_photon_length_over_four_pi(self):
        for t in (0.1, 1.0, 300.0):
            radius = 3.0 / (k.kappa_t_hawking_route_per_m_k(REF["M_sun"]["value"]) * t)
            self.assertLess(rel_diff(radius, scales.thermal_photon_length(t) / (4.0 * math.pi)), 1.0e-14)

    def test_any_rt_condition_calibrated_at_planck_point_is_g_free(self):
        # A condition R T = const that holds at (l_P, T_P) has const = l_P T_P,
        # which equals hbar c/k_B for every value of G.
        for scale in (0.5, 1.0, 10.0):
            g = k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2 * scale
            const = k.planck_length(g) * k.planck_temperature(g)
            self.assertLess(rel_diff(const, scales.thermal_photon_length(1.0)), 1.0e-15)

    def test_not_the_wien_peak_wavelength(self):
        # Wien b = h c/(x k_B), x = 4.965114231744276 (root of x = 5(1 - e^-x)).
        x = 4.965114231744276
        self.assertLess(abs(x - 5.0 * (1.0 - math.exp(-x))), 1.0e-14)
        wien_b = k.PLANCK_CONSTANT_J_S * k.SPEED_OF_LIGHT_M_PER_S / (x * k.BOLTZMANN_CONSTANT_J_PER_K)
        ratio = wien_b / scales.thermal_photon_length(1.0)
        self.assertAlmostEqual(ratio, 2.0 * math.pi / x, places=14)  # about 1.2655, not 1


class DeBroglieTests(unittest.TestCase):
    def test_ratio_to_photon_length(self):
        # lambda_dB/lambda_gamma = sqrt(2 pi k_B T/(m c^2)), so it is much less
        # than 1 for any non-relativistic particle.
        m, t = REF["m_e"]["value"], 1.0
        ratio = scales.thermal_de_broglie_wavelength(m, t) / scales.thermal_photon_length(t)
        expected = math.sqrt(2.0 * math.pi * k.BOLTZMANN_CONSTANT_J_PER_K * t / (m * k.SPEED_OF_LIGHT_M_PER_S**2))
        self.assertLess(rel_diff(ratio, expected), 1.0e-14)
        self.assertLess(ratio, 1.0e-3)

    def test_scaling(self):
        m = REF["m_p"]["value"]
        base = scales.thermal_de_broglie_wavelength(m, 1.0)
        self.assertAlmostEqual(scales.thermal_de_broglie_wavelength(m, 4.0) / base, 0.5, places=14)
        self.assertAlmostEqual(scales.thermal_de_broglie_wavelength(4.0 * m, 1.0) / base, 0.5, places=14)


class PhotonGasTests(unittest.TestCase):
    def test_radiation_constant_matches_reference(self):
        # Reference prints a_rad to 5 significant figures and sigma_SB to 10.
        self.assertLess(rel_diff(scales.radiation_constant(), REF["radiation_constant"]["value"]), 5.0e-5)
        from_sigma = 4.0 * REF["sigma_SB"]["value"] / k.SPEED_OF_LIGHT_M_PER_S
        self.assertLess(rel_diff(scales.radiation_constant(), from_sigma), 1.0e-9)

    def test_capacity_ratio_closed_form(self):
        for radius, t in ((0.01, 1.0), (1.0e-5, 300.0), (2.0, 2.7255)):
            closed = 4.0 * math.pi**2 / 135.0 * radius / scales.thermal_photon_length(t)
            self.assertLess(rel_diff(scales.sphere_photon_gas_capacity_ratio(radius, t), closed), 1.0e-14)

    def test_photon_gas_reaches_unit_ratio_at_about_3_42_photon_lengths(self):
        t = 1.0
        radius = 135.0 / (4.0 * math.pi**2) * scales.thermal_photon_length(t)
        self.assertAlmostEqual(scales.sphere_photon_gas_capacity_ratio(radius, t), 1.0, places=13)
        self.assertAlmostEqual(radius / scales.thermal_photon_length(t), 3.4195899479, places=9)


class BoundaryCapacityTests(unittest.TestCase):
    def test_bekenstein_hawking_is_one_kb_per_four_planck_areas(self):
        self.assertLess(
            rel_diff(scales.one_kb_per_area(2.0 * k.PLANCK_LENGTH_M), k.bekenstein_hawking_surface_entropy_density()),
            1.0e-15,
        )

    def test_black_hole_saturates_bekenstein_hawking_capacity(self):
        # S_BH = k_B c^3 A/(4 G hbar) by definition, so eta_S = 1 for every mass.
        c, hbar, g = k.SPEED_OF_LIGHT_M_PER_S, k.REDUCED_PLANCK_CONSTANT_J_S, k.GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        for mass in (1.0e30, 1.0e36):
            area = sphere_area(k.schwarzschild_radius(mass))
            entropy = k.BOLTZMANN_CONSTANT_J_PER_K * c**3 * area / (4.0 * g * hbar)
            eta = entropy / (k.bekenstein_hawking_surface_entropy_density() * area)
            self.assertAlmostEqual(eta, 1.0, places=14)

    def test_lattice_capacity_threshold_is_three_spacings_over_radius(self):
        # sigma = k_B/a^2 and V = N a^3: eta_S = 1  <=>  S/(N k_B) = 3a/R.
        a, radius = 2.5e-10, 0.02
        n_atoms = sphere_volume(radius) / a**3
        required = scales.one_kb_per_area(a) * sphere_area(radius) / (n_atoms * k.BOLTZMANN_CONSTANT_J_PER_K)
        self.assertLess(rel_diff(required, 3.0 * a / radius), 1.0e-14)


class InputValidationTests(unittest.TestCase):
    def test_nonphysical_inputs_fail_loudly(self):
        for bad in (0.0, -1.0, math.nan, math.inf):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    scales.thermal_photon_length(bad)
                with self.assertRaises(ValueError):
                    scales.one_kb_per_area(bad)


if __name__ == "__main__":
    unittest.main()
