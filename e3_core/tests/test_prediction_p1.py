"""Tests for e3_core.prediction_p1 (docs/PREREGISTRATION_P1.md)."""

import json
import math
import unittest
from pathlib import Path

from e3_core import constants as k
from e3_core import prediction_p1 as p1

ROOT = Path(__file__).resolve().parents[2]
SCALES = json.loads((ROOT / "docs" / "task7_candidate_scales.json").read_text())
REF = {
    entry["id"]: entry
    for category in json.loads((ROOT / "reference" / "known_physics_reference.json").read_text())["categories"]
    for entry in category["entries"]
}

# Phillips (1959) parameters, as used in scripts/task7_candidate_scales.py.
PHILLIPS = {"gamma": 1.350e-3, "tc_k": 1.163, "debye_k": 427.7}
AL_SPACING_M = SCALES["systems"][2]["mean_atomic_spacing_m"]
AL_RADIUS_M = SCALES["systems"][2]["radius_m"]
# Al-27: I = 5/2, mu = +3.6415069 nuclear magnetons (KAERI / LBL nuclear moments table).
AL27_SPIN = 2.5
AL27_MOMENT_NUCLEAR_MAGNETONS = 3.6415069


def nuclear_magneton() -> float:
    return k.ELEMENTARY_CHARGE_C * k.REDUCED_PLANCK_CONSTANT_J_S / (2.0 * REF["m_p"]["value"])


class ThresholdTests(unittest.TestCase):
    def test_sphere_threshold_is_three_spacings_over_radius(self):
        a, r = 2.55e-10, 0.02
        self.assertAlmostEqual(p1.lattice_threshold_per_atom(a, 3.0 / r) / (3.0 * a / r), 1.0, places=15)

    def test_debye_entropy_is_one_third_of_heat_capacity(self):
        self.assertAlmostEqual(
            p1.debye_molar_entropy(0.2, 427.7) * 3.0 / p1.debye_molar_heat_capacity(0.2, 427.7), 1.0, places=15
        )
        with self.assertRaises(ValueError):
            p1.debye_molar_entropy(20.0, 427.7)


class PredictionTests(unittest.TestCase):
    def setUp(self):
        self.threshold = p1.lattice_threshold_per_atom(AL_SPACING_M, 3.0 / AL_RADIUS_M)

    def test_reproduces_task7_script_values(self):
        recorded = SCALES["aluminium_superconducting_lattice_crossing"]["crossing_temperature_K_by_factor"]
        for factor in ("0.25", "1", "4"):
            with self.subTest(factor=factor):
                value = p1.predicted_crossing_temperature(self.threshold, **PHILLIPS, prefactor=float(factor))
                self.assertAlmostEqual(value, recorded[factor], places=9)

    def test_band_is_ordered(self):
        low, mid, high = p1.predicted_band(self.threshold, **PHILLIPS)
        self.assertLess(low, mid)
        self.assertLess(mid, high)

    def test_larger_area_over_volume_gives_higher_crossing(self):
        small = p1.predicted_crossing_temperature(self.threshold, **PHILLIPS)
        big = p1.predicted_crossing_temperature(self.threshold * 10.0, **PHILLIPS)
        self.assertGreater(big, small)

    def test_partner_relation_is_independent_of_prefactor(self):
        s1 = {"spacing_m": AL_SPACING_M, "area_over_volume_per_m": 3.0 / AL_RADIUS_M, **PHILLIPS}
        s2 = {"spacing_m": AL_SPACING_M, "area_over_volume_per_m": 30.0 / AL_RADIUS_M,
              "gamma": 1.36e-3, "tc_k": 1.18, "debye_k": 428.0}
        th1 = p1.lattice_threshold_per_atom(s1["spacing_m"], s1["area_over_volume_per_m"])
        th2 = p1.lattice_threshold_per_atom(s2["spacing_m"], s2["area_over_volume_per_m"])
        for prefactor in (0.3, 1.0, 2.7):
            with self.subTest(prefactor=prefactor):
                t1 = p1.predicted_crossing_temperature(th1, s1["gamma"], s1["tc_k"], s1["debye_k"], prefactor)
                t2 = p1.predicted_crossing_temperature(th2, s2["gamma"], s2["tc_k"], s2["debye_k"], prefactor)
                self.assertAlmostEqual(p1.partner_crossing_temperature(t1, s1, s2), t2, places=9)


class DepartureTests(unittest.TestCase):
    def baseline(self, t):
        return 1.0

    def test_highest_point_of_contiguous_low_temperature_excess(self):
        temps = [0.10, 0.15, 0.20, 0.25, 0.30]
        caps = [3.0, 2.0, 1.5, 1.01, 1.0]
        self.assertEqual(p1.departure_temperature(temps, caps, [0.05] * 5, self.baseline), 0.20)

    def test_run_must_start_at_lowest_point(self):
        temps = [0.10, 0.15, 0.20]
        caps = [1.0, 2.0, 2.0]
        self.assertIsNone(p1.departure_temperature(temps, caps, [0.05] * 3, self.baseline))

    def test_needs_two_points_and_respects_uncertainty(self):
        self.assertIsNone(p1.departure_temperature([0.1, 0.2], [2.0, 1.0], [0.05, 0.05], self.baseline))
        # 50% excess is not significant at 3 sigma when u = 20%.
        self.assertIsNone(p1.departure_temperature([0.1, 0.2], [1.5, 1.5], [0.2, 0.2], self.baseline))

    def test_unsorted_input_is_sorted(self):
        self.assertEqual(
            p1.departure_temperature([0.2, 0.1, 0.3], [1.5, 3.0, 1.0], [0.05] * 3, self.baseline), 0.2
        )

    def test_baseline_reduces_to_bcs_plus_debye(self):
        t = 0.5
        expected = bcs_value = None
        from e3_core import bcs
        bcs_value = bcs.heat_capacity_ratio(t / PHILLIPS["tc_k"]) * PHILLIPS["gamma"] * PHILLIPS["tc_k"]
        expected = bcs_value + p1.debye_molar_heat_capacity(t, PHILLIPS["debye_k"])
        self.assertAlmostEqual(p1.baseline_molar_heat_capacity(t, **PHILLIPS) / expected, 1.0, places=14)


class NuclearBoundTests(unittest.TestCase):
    def test_nuclear_magneton_from_constants(self):
        # CODATA 2018 mu_N = 5.0507837461e-27 J/T; here computed as e hbar/(2 m_p).
        self.assertAlmostEqual(nuclear_magneton() / 5.0507837461e-27, 1.0, places=9)

    def test_high_temperature_limit_matches_exact_sum(self):
        mu = AL27_MOMENT_NUCLEAR_MAGNETONS * nuclear_magneton()
        exact = p1.zeeman_heat_capacity_per_spin(AL27_SPIN, mu, 1.0e-3, 0.1)
        approx = p1.zeeman_heat_capacity_high_t(AL27_SPIN, mu, 1.0e-3, 0.1)
        self.assertLess(abs(exact - approx) / approx, 1.0e-6)
        # Sanity check of the exact sum at large splitting: frozen out, C -> 0.
        self.assertLess(p1.zeeman_heat_capacity_per_spin(AL27_SPIN, mu, 10.0, 1.0e-6), 1.0e-6)

    def test_dipolar_field_estimate_below_one_millitesla(self):
        mu = AL27_MOMENT_NUCLEAR_MAGNETONS * nuclear_magneton()
        mu0_over_4pi = 1.0e-7  # SI value; exact before 2019 and within 1e-9 since
        dipolar = mu0_over_4pi * mu / AL_SPACING_M**3
        self.assertLess(dipolar, 1.0e-3)

    def test_nuclear_active_entropy_small_against_threshold(self):
        # In the high-T regime the entropy below ln(2I+1) is C/2. At 0.1 K, below
        # the whole predicted band:
        #   dipolar field estimate (about 0.11 mT): ratio below 1e-4;
        #   1 mT (registered residual-field limit): ratio below 2e-3;
        #   30 mT (Phillips' normal-state field): ratio of order 1, so normal-state
        #   or field-on data are not usable for P1.
        mu = AL27_MOMENT_NUCLEAR_MAGNETONS * nuclear_magneton()
        threshold = p1.lattice_threshold_per_atom(AL_SPACING_M, 3.0 / AL_RADIUS_M)

        def ratio(field):
            return 0.5 * p1.zeeman_heat_capacity_per_spin(AL27_SPIN, mu, field, 0.1) / threshold

        self.assertLess(ratio(1.1e-4), 1.0e-4)
        self.assertLess(ratio(1.0e-3), 2.0e-3)
        self.assertGreater(ratio(3.0e-2), 0.5)

    def test_nuclear_entropy_shifts_crossing_negligibly_at_one_millitesla(self):
        mu = AL27_MOMENT_NUCLEAR_MAGNETONS * nuclear_magneton()
        threshold = p1.lattice_threshold_per_atom(AL_SPACING_M, 3.0 / AL_RADIUS_M)
        base = p1.predicted_crossing_temperature(threshold, **PHILLIPS)

        def total(t):
            nuclear = 0.5 * p1.zeeman_heat_capacity_per_spin(AL27_SPIN, mu, 1.0e-3, t)
            return p1.active_entropy_per_atom(t, **PHILLIPS) + nuclear

        lo, hi = 0.05, PHILLIPS["tc_k"]
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if total(mid) < threshold else (lo, mid)
        self.assertLess(abs(0.5 * (lo + hi) - base) / base, 1.0e-3)


if __name__ == "__main__":
    unittest.main()
