#!/usr/bin/env python3
"""Illustrative P2 prediction table (docs/PREREGISTRATION_P2.md).

Material inputs are APPROXIMATE handbook values recalled from memory, used only
to show the scale of the prediction. A registered test uses each crystal's own
measured Theta_D (from sound velocities, or from the registered fit window) and
its measured dimensions. Writes docs/p2_prediction_table.json.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from e3_core import constants as k  # noqa: E402
from e3_core import prediction_p2 as p2  # noqa: E402
from e3_core import scales  # noqa: E402

# name: (density kg/m^3, molar mass kg/mol per formula unit, atoms per formula unit, Theta_D K) -- approximate
MATERIALS = {
    "Si": (2330.0, 28.086e-3, 1, 645.0),
    "Ge": (5323.0, 72.63e-3, 1, 374.0),
    "diamond": (3515.0, 12.011e-3, 1, 2230.0),
    "TeO2": (6020.0, 159.6e-3, 3, 230.0),
}
CUBE_EDGES_M = (1.0e-3, 1.0e-2, 5.0e-2)


def main() -> None:
    rows = []
    for name, (rho, molar, atoms, theta) in MATERIALS.items():
        spacing = scales.mean_atomic_spacing(rho / molar * k.AVOGADRO_CONSTANT_PER_MOL * atoms)
        for edge in CUBE_EDGES_M:
            threshold = p2.lattice_threshold_per_atom(spacing, 6.0 / edge)
            low, mid, high = p2.predicted_band(threshold, theta)
            fit = p2.registered_fit_window(high, theta)
            rows.append({
                "material": name, "cube_edge_m": edge, "mean_atomic_spacing_m": spacing, "debye_K_approx": theta,
                "T_star_K": {"prefactor_0.25": low, "prefactor_1": mid, "prefactor_4": high},
                "required_window_K": [0.8 * low, 1.1 * high],
                "fallback_fit_window_K": list(fit),
            })
    out = ROOT / "docs" / "p2_prediction_table.json"
    out.write_text(json.dumps({"generated_by": "scripts/p2_prediction_table.py",
                               "inputs": "approximate handbook values, illustration only",
                               "rows": rows}, indent=2) + "\n", encoding="utf-8")
    for r in rows:
        b = r["T_star_K"]
        print(f"{r['material']:8} {r['cube_edge_m']*1e3:5.0f} mm  T*: {b['prefactor_0.25']:.3f} {b['prefactor_1']:.3f} {b['prefactor_4']:.3f} K"
              f"  window {r['required_window_K'][0]:.3f}-{r['required_window_K'][1]:.3f}  fit {r['fallback_fit_window_K'][0]:.2f}-{r['fallback_fit_window_K'][1]:.2f} K")


if __name__ == "__main__":
    main()
