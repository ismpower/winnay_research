==============================================================================
(a) MODIFICATION VERIFICATION
==============================================================================

'Bekenstein-Hawking entropy equation ... (corrected formula)'
  as written : S = k_B*4*pi*r_s^2 / (hbar*G/c^3)
  standard   : S = k_B*c^3*A/(4*G*hbar),  A = 4*pi*r_s^2
  standard   = 5.567029e+57
  as written = 2.226812e+58
  ratio      = 4.0000   <- the /4 of 'A/4' was dropped

'T_H_eq = (hbar*c**3)/(8*pi*G*M) * (S_BH/k_B)   # Adjusted scaling'
  standard T_H = 9.951732e-10 K
  as written   = 5.540158e+48
  ratio        = 5.5670e+57
  The factor S_BH/k_B is the DIMENSIONLESS entropy (~1e80). Multiplying a
  temperature by it is not a scaling correction; it is a unit-less
  quantity of order 10^80 applied to a physical observable.

==============================================================================
(b) VALUE-FIRST SWEEP -- constants under unconventional names
==============================================================================

  M_sun
    `solar_mass_kg`  in 1 file(s)   e.g. ./bruno-framework-clean/organized_research/black_holes/Blackhole_Entropy_Evolution.py

  N_A
    `NA`  in 2 file(s)   e.g. ./notebooks/Fluence_Model_Comparison.ipynb

  a_rad
    `a_rad`  in 5 file(s)   e.g. ./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb
    `a`  in 3 file(s)   e.g. ./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Simulatation_Scripts/bruno_collapse_map.py

  e (charge)
    `e`  in 2 file(s)   e.g. ./E3_DAVP_Pipeline/davp_pipeline.py

  eV
    `e`  in 2 file(s)   e.g. ./E3_DAVP_Pipeline/davp_pipeline.py

  m_Planck
    `planck_mass`  in 3 file(s)   e.g. ./bruno-framework-clean/Scripts/Obervational_Dark_Matter.py

  pc (parsec)
    `pc_to_m`  in 1 file(s)   e.g. ./notebooks/Fluence_Model_Comparison.ipynb

  t_Planck
    `PLANCK_TIME`  in 1 file(s)   e.g. ./sim_results/bruno_universe.py
