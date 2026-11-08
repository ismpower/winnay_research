"""Tests for e3_core.prediction_p2 (docs/PREREGISTRATION_P2.md)."""

import math
import unittest

from e3_core import constants as k
from e3_core import prediction_p1 as p1
from e3_core import prediction_p2 as p2

HBAR = k.REDUCED_PLANCK_CONSTANT_J_S
KB = k.BOLTZMANN_CONSTANT_J_PER_K


class DebyeTests(unittest.TestCase):
    def test_heat_capacity_is_t_ds_dt(self):
        theta, t, h = 640.0, 1.0, 1.0e-4
        numeric = t * (p2.phonon_entropy_per_atom(t + h, theta) - p2.phonon_entropy_per_atom(t - h, theta)) / (2 * h)
        self.assertAlmostEqual(numeric / p2.phonon_heat_capacity_per_atom(t, theta), 1.0, places=7)

    def test_validity_limit_enforced(self):
        with self.assertRaises(ValueError):
            p2.phonon_entropy_per_atom(20.0, 640.0)

    def test_sound_velocity_theta_matches_phonon_gas(self):
        # Independent route: three acoustic branches as a phonon gas,
        # C/V = (2 pi^2/15) k_B^4 T^3/hbar^3 * sum_i 1/v_i^3.
        n, vl, vt, t = 5.0e28, 8.4e3, 5.8e3, 0.5
        theta = p2.debye_temperature_from_sound_velocities(n, vl, vt)
        debye_per_volume = n * KB * p2.phonon_heat_capacity_per_atom(t, theta)
        gas_per_volume = (2 * math.pi**2 / 15) * KB**4 * t**3 / HBAR**3 * (1 / vl**3 + 2 / vt**3)
        self.assertAlmostEqual(debye_per_volume / gas_per_volume, 1.0, places=12)

    def test_coefficient_inversion(self):
        theta = 374.0
        a = p2.phonon_heat_capacity_per_atom(1.0, theta)  # = A at T = 1 K
        self.assertAlmostEqual(p2.debye_temperature_from_coefficient(a) / theta, 1.0, places=13)


class CrossingTests(unittest.TestCase):
    def test_closed_form_solves_entropy_equation(self):
        theta, s_th = 645.0, 1.6e-7
        for f in (0.25, 1.0, 4.0):
            t = p2.predicted_crossing_temperature(s_th, theta, f)
            self.assertAlmostEqual(p2.phonon_entropy_per_atom(t, theta) / (f * s_th), 1.0, places=13)

    def test_band_ratios_are_cube_roots(self):
        low, mid, high = p2.predicted_band(1.6e-7, 645.0)
        self.assertAlmostEqual(mid / low, 4.0 ** (1 / 3), places=13)
        self.assertAlmostEqual(high / mid, 4.0 ** (1 / 3), places=13)

    def test_partner_relation_is_independent_of_prefactor(self):
        s1 = {"spacing_m": 2.72e-10, "area_over_volume_per_m": 600.0, "debye_k": 645.0}
        s2 = {"spacing_m": 2.72e-10, "area_over_volume_per_m": 6000.0, "debye_k": 640.0}
        th1 = p1.lattice_threshold_per_atom(s1["spacing_m"], s1["area_over_volume_per_m"])
        th2 = p1.lattice_threshold_per_atom(s2["spacing_m"], s2["area_over_volume_per_m"])
        for f in (0.3, 1.0, 2.7):
            t1 = p2.predicted_crossing_temperature(th1, s1["debye_k"], f)
            t2 = p2.predicted_crossing_temperature(th2, s2["debye_k"], f)
            self.assertAlmostEqual(p2.partner_crossing_temperature(t1, s1, s2) / t2, 1.0, places=13)

    def test_outside_debye_range_refused(self):
        with self.assertRaises(ValueError):
            p2.predicted_crossing_temperature(1.0e-2, 100.0)


class FitTests(unittest.TestCase):
    def test_fit_recovers_known_coefficients(self):
        a_true, b_true = 3.0e-7, 2.0e-9
        temps = [2.0, 3.0, 4.0, 6.0, 8.0, 10.0]
        caps = [(a_true + b_true * t * t) * t**3 for t in temps]
        a, b = p2.fit_low_temperature_coefficients(temps, caps, [0.01] * len(temps))
        self.assertAlmostEqual(a / a_true, 1.0, places=10)
        self.assertAlmostEqual(b / b_true, 1.0, places=8)

    def test_fit_uses_uncertainty_weights(self):
        # A corrupted point with a 1000x larger stated uncertainty must barely move A.
        a_true, b_true = 3.0e-7, 2.0e-9
        temps = [2.0, 3.0, 4.0, 6.0, 8.0, 10.0]
        caps = [(a_true + b_true * t * t) * t**3 for t in temps]
        caps[0] *= 2.0
        u = [0.01] * len(temps)
        u[0] = 10.0
        a, _ = p2.fit_low_temperature_coefficients(temps, caps, u)
        self.assertAlmostEqual(a / a_true, 1.0, places=5)

    def test_fit_window_and_degenerate_cases(self):
        self.assertEqual(p2.registered_fit_window(1.0, 645.0), (1.5, 12.9))
        with self.assertRaises(ValueError):
            p2.registered_fit_window(10.0, 645.0)
        with self.assertRaises(ValueError):
            p2.fit_low_temperature_coefficients([1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [0.1] * 3)

    def test_departure_rule_is_p1s(self):
        self.assertIs(p2.departure_temperature, p1.departure_temperature)


if __name__ == "__main__":
    unittest.main()
