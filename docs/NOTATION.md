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

