import math
import unittest

from e3_core.geometry import (
    critical_volume_entropy_density,
    entropy_capacity_ratio,
    normalized_surface_to_volume,
    sphere_area,
    sphere_volume,
    surface_entropy_density,
    surface_to_volume,
    temperature_coefficient,
    volume_entropy_density,
)


class SphereGeometryTests(unittest.TestCase):
    def test_area_over_volume_equals_three_over_radius(self):
        for radius_m in (1.0e-9, 0.25, 2.0, 1.0e6):
            direct_ratio = sphere_area(radius_m) / sphere_volume(radius_m)
            self.assertTrue(
                math.isclose(
                    direct_ratio,
                    surface_to_volume(radius_m),
                    rel_tol=2.0e-16,
                    abs_tol=0.0,
                )
            )

    def test_inverse_length_numeric_value_changes_with_unit_representation(self):
        radius_m = 2.0
        ratio_per_m = surface_to_volume(radius_m)

        radius_cm = radius_m * 100.0
        ratio_per_cm = 3.0 / radius_cm

        self.assertAlmostEqual(ratio_per_m, 1.5)
        self.assertAlmostEqual(ratio_per_cm, 0.015)
        self.assertAlmostEqual(ratio_per_cm * 100.0, ratio_per_m)

    def test_normalized_ratio_is_scale_invariant(self):
        beta_m = normalized_surface_to_volume(2.0, 0.5)
        beta_cm = normalized_surface_to_volume(200.0, 50.0)
        self.assertAlmostEqual(beta_m, beta_cm)


class EntropyDensityTests(unittest.TestCase):
    def test_entropy_density_ratio_reduces_to_geometry(self):
        radius_m = 4.0
        entropy_j_per_k = 17.0
        volume_density = volume_entropy_density(entropy_j_per_k, sphere_volume(radius_m))
        surface_density = surface_entropy_density(entropy_j_per_k, sphere_area(radius_m))
        self.assertAlmostEqual(volume_density / surface_density, surface_to_volume(radius_m))

    def test_surface_capacity_maps_to_radius_dependent_volume_capacity(self):
        sigma_crit = 12.0
        small = critical_volume_entropy_density(sigma_crit, radius_m=1.0)
        large = critical_volume_entropy_density(sigma_crit, radius_m=10.0)
        self.assertAlmostEqual(small / large, 10.0)

    def test_capacity_ratio_is_dimensionless(self):
        self.assertAlmostEqual(entropy_capacity_ratio(7.5, 3.0), 2.5)


class TemperatureCoefficientTests(unittest.TestCase):
    def test_coefficient_retains_inverse_length(self):
        kappa_per_m_k = temperature_coefficient(radius_m=2.0, temperature_k=10.0)
        kappa_per_cm_k = 3.0 / (200.0 * 10.0)
        self.assertAlmostEqual(kappa_per_m_k, 0.15)
        self.assertAlmostEqual(kappa_per_cm_k * 100.0, kappa_per_m_k)

    def test_invalid_physical_inputs_fail_loudly(self):
        for invalid in (0.0, -1.0, math.inf, math.nan):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    sphere_area(invalid)
        with self.assertRaises(ValueError):
            temperature_coefficient(1.0, 0.0)
        with self.assertRaises(ValueError):
            entropy_capacity_ratio(1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
