"""P2 screening triage: largest sample that a stated lowest temperature can serve.

Criterion 8 of docs/PREREGISTRATION_P2.md needs data down to 0.8 T*(0.25).
T*(0.25) rises with A/V, so a stated lowest temperature T_min serves only
samples small enough. This prints, for each (material, T_min), the largest
equivalent cube edge L_eq = 6/(A/V) for which 0.8 T*(0.25) >= T_min, using the
frozen e3_core.prediction_p2.predicted_band unchanged.

Inputs are approximate handbook values (planning only, like
scripts/p2_prediction_table.py). The triage only rules out candidates whose
floor needs a sample below criterion 4's 0.1 mm minimum dimension; any
candidate that is actually screened is judged on its own measured geometry.

Run: python3 scripts/p2_screening_triage.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from e3_core.prediction_p2 import predicted_band  # noqa: E402

AVOGADRO = 6.02214076e23


def mean_spacing(density_g_cm3: float, molar_mass_g: float, atoms_per_formula: int) -> float:
    """Return a = n^(-1/3), counting all atoms."""
    n = density_g_cm3 * 1e3 / (molar_mass_g * 1e-3) * AVOGADRO * atoms_per_formula
    return n ** (-1.0 / 3.0)


def materials() -> dict:
    table = json.loads((ROOT / "docs" / "p2_prediction_table.json").read_text())
    out = {r["material"]: (r["debye_K_approx"], r["mean_atomic_spacing_m"]) for r in table["rows"]}
    # Approximate handbook values: (Theta_D [K], density [g/cm3], molar mass [g/mol], atoms/formula)
    extra = {
        "KCl": (235.0, 1.98, 74.55, 2),
        "LiF": (730.0, 2.635, 25.94, 2),
        "KI": (132.0, 3.12, 166.0, 2),
        "ZnSe": (300.0, 5.27, 144.3, 2),
        "CaWO4": (250.0, 6.06, 288.0, 6),
    }
    for name, (theta, rho, molar, nat) in extra.items():
        out[name] = (theta, mean_spacing(rho, molar, nat))
    return out


def max_equivalent_cube_edge(theta: float, spacing: float, t_min: float) -> float:
    def serves(edge: float) -> bool:
        try:
            t_low = predicted_band(spacing * 6.0 / edge, theta)[0]
        except ValueError:  # crossing above Theta/50: band is far above t_min
            return True
        return 0.8 * t_low >= t_min

    lo, hi = 1e-9, 10.0
    for _ in range(200):
        mid = (lo * hi) ** 0.5
        if serves(mid):
            lo = mid
        else:
            hi = mid
    return lo


# (candidate label, material, stated lowest temperature in K)
CASES = [
    ("C1 Barucci 2001", "TeO2", 0.06),
    ("C2 White 1990", "TeO2", 0.6),
    ("C3 Keesom-Seidel 1959 (Si)", "Si", 1.2),
    ("C3 Keesom-Seidel 1959 (Ge)", "Ge", 0.5),
    ("C6 Gusev 2015", "Ge", 2.5),
    ("C9 CaWO4 1968", "CaWO4", 5.0),
    ("C10 ZnSe 1975", "ZnSe", 2.0),
    ("C13 Scales 1958 (LiF)", "LiF", 2.0),
    ("C13 Scales 1958 (KI)", "KI", 2.0),
    ("C11 KCl 1953, if floor 1 K", "KCl", 1.0),
]


def main() -> None:
    mats = materials()
    print(f"{'candidate':32s} {'material':8s} {'T_min/K':>8s} {'max L_eq/mm':>12s}")
    for label, mat, t_min in CASES:
        theta, a = mats[mat]
        edge_mm = max_equivalent_cube_edge(theta, a, t_min) * 1e3
        print(f"{label:32s} {mat:8s} {t_min:8.3g} {edge_mm:12.3g}")
    print("\nCriterion 4 allows a thinnest dimension of 0.1 mm, i.e. L_eq >= about 0.3 mm (plate).")


if __name__ == "__main__":
    main()
