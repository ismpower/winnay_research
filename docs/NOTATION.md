# E3 restart notation

The restart does not reuse bare `k` or `kappa`. Each symbol names one physical
role and carries explicit units.

| Symbol | Code name | Meaning | SI units | Status |
|---|---|---|---|---|
| `R` | `radius_m` | Spherical-region radius | `m` | geometric input |
| `A` | `sphere_area_m2` | Boundary area | `m^2` | derived |
| `V` | `sphere_volume_m3` | Enclosed volume | `m^3` | derived |
| `beta_geom` | `surface_to_volume_per_m` | `A/V = 3/R` | `m^-1` | exact geometry |
| `L_0` | `reference_length_m` | Declared normalization length | `m` | model input |
| `beta_tilde` | `normalized_surface_to_volume` | `L_0 A/V` | dimensionless | derived |
| `S` | `entropy_j_per_k` | Entropy | `J K^-1` | measured/inferred input |
| `s_V` | `volume_entropy_density` | `S/V` | `J K^-1 m^-3` | derived |
| `sigma_A` | `surface_entropy_density` | `S/A` | `J K^-1 m^-2` | derived |
| `sigma_crit` | `critical_surface_entropy_density` | Proposed boundary capacity | `J K^-1 m^-2` | hypothesis/input |
| `s_crit` | `critical_volume_entropy_density` | `sigma_crit A/V` | `J K^-1 m^-3` | derived |
| `eta_S` | `entropy_capacity_ratio` | `s_system/s_crit` | dimensionless | candidate observable |
| `k_decay` | — | Exponential saturation/decay rate | inverse units of its independent variable | legacy quantity, unresolved |
| `kappa_T` | — | Coefficient in `beta_geom = kappa_T T` | `m^-1 K^-1` | derived role, no accepted value |
| `F_cut` | — | Event fluence classification cut | `J m^-2` | analysis choice, not a constant |

Reserved names:

- `k_B` always means the Boltzmann constant.
- `kappa_sg` means black-hole surface gravity when needed.
- `BRUNO_CONSTANT` is prohibited until one quantity has an independently
  justified universal value.

## Legacy kappa values: naming decision (plan task 2)

**Decided:** 2026-11-03. Six different numbers shared the name `kappa` in the legacy
corpus. Each is assigned its own symbol below, or retired. The physical role and units
come from `audits/2026-08-02_initial/BRUNO_E3_FULL_AUDIT.md` (sections 1.4, 1.5, 3 and 6).
The audit also records where each value occurs. The name `kappa` alone
is never used for any of them.

| Legacy literal | Restart symbol | Code name | What it is | Units | Status |
|---|---|---|---|---|---|
| `1313` | `kappa_T^Pl` | `kappa_t_planck_route_per_m_k` | `kappa_T` evaluated at `R = l_P`, `T = T_P`: `3/(l_P T_P) = 3 k_B/(hbar c)` | `m^-1 K^-1` | Expression reproduces as `1310.11`; the literal `1313` is a +0.22% misreport labelled with the wrong units (`K^-1`). Use the expression, never the literal. Tested in `e3_core/tests/test_constants.py`. |
| `1366` | `kappa_T^GW` | `kappa_t_hawking_route_per_m_k` | `kappa_T` evaluated at `R = R_s`, `T = T_H`: `3/(R_s T_H) = 12 pi k_B/(hbar c)`, independent of mass | `m^-1 K^-1` | Correct expression evaluates to `16463.32`. The literal `1366` is an artifact of a wrong `T_H` and is **retired**. Tested in `e3_core/tests/test_constants.py`. |
| `0.001005` | `chi_tan` | `planck_tangency_fraction` | Pure-number multiplier, `T_tangent = chi_tan T_P` ("Chajar constant") | dimensionless | Chosen, never derived. The GW pipeline also used it as a coefficient on `abs(strain) * 1e23` treated as a temperature. That second use is a different role and is not covered by this symbol (task 4). |
| `1340e-6` (`+/- 60e-6`) | `kappa_lab` | `lab_rate_coefficient_per_k_s` | Claimed laboratory measurement, no method or source recorded | `K^-1 s^-1` as stated | Unsourced (task 5). Its stated units differ from `kappa_T`, so even if a source is found it is not the same quantity as `kappa_T^Pl` or `kappa_T^GW`. |
| `1.23456789e-23` | none | none | Keyboard-sequence placeholder baked into engine files | none | **Retired**; all sites are deleted in task 6. |
| `1.0e-23` | none | none | Parameter in `Emergent_Gravity_Toy_Model.ipynb`; the audit records it as unrelated and does not establish its role | unknown | **Not carried into the restart.** |

### Consequences

1. `kappa_T^Pl` and `kappa_T^GW` are not rival measurements of one constant. They are
   the same coefficient role evaluated on two pairs `(R, T)`. Their ratio is exactly
   `4 pi` because `l_P T_P = hbar c/k_B` and `R_s T_H = hbar c/(4 pi k_B)`.
   Neither contains `G` or a mass, and neither carries observational information.
2. `chi_tan`, `kappa_lab` and `kappa_T` have three different dimensions
   (dimensionless, `K^-1 s^-1`, `m^-1 K^-1`). No numerical comparison among them is
   meaningful without a stated conversion.
3. `BRUNO_CONSTANT` stays prohibited (see "Reserved names" above). None of the
   symbols here is a universal constant with an independent justification.

