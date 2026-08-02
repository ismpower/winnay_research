# Value Table — grouped by value, not by file

Built from `/tmp/audit/*.txt` (Phase 2 grep output) only. No source file was opened.

**Reading the columns.** *Sites* counts assignment occurrences. *Files* counts distinct paths. *Unique contents* counts distinct md5s among those paths — if Files is 8 but Unique contents is 1, that is one file copied 8 times, not eight independent decisions. *Branches* are top-two path components, the unit at which a rebuild/session diverged.

## `kappa.txt` — kappa

197 assignment sites, 40 distinct files, 6 distinct values.

| Value | Sites | Files | Unique contents | Branches |
|---|---:|---:|---:|---|
| `1366` | 76 | 20 | 5 | `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_Project_OLD_MESSY/archive`, `E3_Project_OLD_MESSY/notebooks` +4 more |
| `1313` | 84 | 20 | 5 | `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_Project_OLD_MESSY/notebooks`, `notebooks/BRUNO_GRCHOMBO_SIMULATION` +1 more |
| `3` | 14 | 14 | 4 | `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_Project_OLD_MESSY/notebooks`, `notebooks/BRUNO_GRCHOMBO_SIMULATION` +1 more |
| `0.001005` | 17 | 8 | 3 | `E3_Project_Tokamak_Analysis/bruno-analysis`, `bruno-simulator-RESTRUCTURED/notebooks`, `bruno-simulator-latest/bruno-analysis`, `bruno-simulator-latest/nb04_gw_corrmap.ipynb` +2 more |
| `1366.0` | 5 | 5 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `bruno-simulator-latest/nb01_toy_core.ipynb`, `entropy-collapse-transient-engine(1).ipynb`, `entropy-collapse-transient-engine.ipynb` +1 more |
| `1340e-6` | 1 | 1 | 1 | `github_repos/bruno-collapse-simulator` |

<details><summary>Branch breakdown</summary>


**`1366`**

- `CLEAN_WORKSPACE/archived_research` — 33 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:139`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:190`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:21`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:358`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:527`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Final/Bruno_collapse_tracker.py:5`
  - _…27 more_
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 5 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:139`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:190`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:21`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:358`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:527`
- `E3_Project_OLD_MESSY/archive` — 1 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/final/Bruno_collapse_tracker.py:5`
- `E3_Project_OLD_MESSY/notebooks` — 15 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:160`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:201`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:35`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:407`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:636`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:121`
  - _…9 more_
- `Entropy-Collapse-Research/Scripts` — 1 site(s)
  - `./Entropy-Collapse-Research/Scripts/Final/Bruno_collapse_tracker.py:5`
- `bruno-simulator-RESTRUCTURED/bruno_framework` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/bruno_framework/historical_scripts/core_development/Bruno_collapse_tracker.py:5`
- `notebooks/BRUNO_GRCHOMBO_SIMULATION` — 15 site(s)
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:160`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:201`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:35`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:407`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:636`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:121`
  - _…9 more_
- `notebooks/archive` — 5 site(s)
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:121`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:211`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:290`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:37`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:95`

**`1313`**

- `CLEAN_WORKSPACE/archived_research` — 39 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:1090`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:193`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:273`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:336`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:396`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:521`
  - _…33 more_
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 10 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:1090`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:193`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:273`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:336`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:396`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:521`
  - _…4 more_
- `E3_Project_OLD_MESSY/notebooks` — 16 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1489`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:672`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:870`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:319`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:414`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:674`
  - _…10 more_
- `notebooks/BRUNO_GRCHOMBO_SIMULATION` — 16 site(s)
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1489`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:672`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:870`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:319`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:414`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:674`
  - _…10 more_
- `notebooks/archive` — 3 site(s)
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:319`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:414`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:674`

**`3`**

- `CLEAN_WORKSPACE/archived_research` — 6 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1154`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1154`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1413`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:637`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1154`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:637`
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 1 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1154`
- `E3_Project_OLD_MESSY/notebooks` — 3 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1413`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:637`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1154`
- `notebooks/BRUNO_GRCHOMBO_SIMULATION` — 3 site(s)
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1413`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:637`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1154`
- `notebooks/archive` — 1 site(s)
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:637`

**`0.001005`**

- `E3_Project_Tokamak_Analysis/bruno-analysis` — 1 site(s)
  - `./E3_Project_Tokamak_Analysis/bruno-analysis/plasma_data_parser.py:6`
- `bruno-simulator-RESTRUCTURED/notebooks` — 5 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb04_gw_corrmap.ipynb:491`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb04_gw_corrmap.ipynb:53`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb04_gw_corrmap.ipynb:65`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb05_GW_Batch_AutoRun.ipynb:753`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb05_GW_Batch_AutoRun.ipynb:888`
- `bruno-simulator-latest/bruno-analysis` — 1 site(s)
  - `./bruno-simulator-latest/bruno-analysis/plasma_data_parser.py:6`
- `bruno-simulator-latest/nb04_gw_corrmap.ipynb` — 3 site(s)
  - `./bruno-simulator-latest/nb04_gw_corrmap.ipynb:491`
  - `./bruno-simulator-latest/nb04_gw_corrmap.ipynb:53`
  - `./bruno-simulator-latest/nb04_gw_corrmap.ipynb:65`
- `bruno-simulator-latest/nb05_GW_Batch_AutoRun.ipynb` — 2 site(s)
  - `./bruno-simulator-latest/nb05_GW_Batch_AutoRun.ipynb:753`
  - `./bruno-simulator-latest/nb05_GW_Batch_AutoRun.ipynb:888`
- `github_repos/bruno-collapse-simulator` — 5 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb04_gw_corrmap.ipynb:491`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb04_gw_corrmap.ipynb:53`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb04_gw_corrmap.ipynb:65`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb05_GW_Batch_AutoRun.ipynb:753`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb05_GW_Batch_AutoRun.ipynb:888`

**`1366.0`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb01_toy_core.ipynb:73`
- `bruno-simulator-latest/nb01_toy_core.ipynb` — 1 site(s)
  - `./bruno-simulator-latest/nb01_toy_core.ipynb:73`
- `entropy-collapse-transient-engine(1).ipynb` — 1 site(s)
  - `./entropy-collapse-transient-engine(1).ipynb:73`
- `entropy-collapse-transient-engine.ipynb` — 1 site(s)
  - `./entropy-collapse-transient-engine.ipynb:73`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb01_toy_core.ipynb:73`

**`1340e-6`**

- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/bruno_framework/historical_scripts/core_development/Bruno_collapse_tracker.py:5`

</details>

## `bruno_constant.txt` — kappa / bruno_constant

255 assignment sites, 94 distinct files, 8 distinct values.

| Value | Sites | Files | Unique contents | Branches |
|---|---:|---:|---:|---|
| `1.23456789e-23` | 42 | 32 | 14 | `CLEAN_WORKSPACE/E3_project_rev1`, `CLEAN_WORKSPACE/e3_engine`, `E3_CURRENT_PRODUCTION/e3_engine`, `E3_Project/e3_engine` +8 more |
| `1313` | 64 | 24 | 5 | `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_Project_OLD_MESSY/archive`, `E3_Project_OLD_MESSY/notebooks` +4 more |
| `1366` | 74 | 23 | 5 | `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_Project_OLD_MESSY/archive`, `E3_Project_OLD_MESSY/notebooks` +4 more |
| `0.001005` | 53 | 20 | 10 | `Bruno_model_sim_final.tex`, `Bruno_model_sim_upd.tex`, `Bruno_model_sim_upd_cleaned.tex`, `CLEAN_WORKSPACE/archived_research` +11 more |
| `1` | 9 | 9 | 5 | `Bruno_model_sim_final.tex`, `Bruno_model_sim_upd.tex`, `Bruno_model_sim_upd_cleaned.tex`, `CLEAN_WORKSPACE/archived_research` +1 more |
| `1366.0` | 8 | 8 | 2 | `bruno-fluence-app/bruno_fluence_analyzer.py`, `bruno-fluence-app/docker-compose.yml`, `bruno-fluence-app/setup_bruno_docker.sh`, `bruno-simulator-RESTRUCTURED/notebooks` +4 more |
| `1.0e-23` | 4 | 4 | 1 | `CLEAN_WORKSPACE/archived_research`, `bruno-framework-clean/Entropy_Notebook`, `github_repos/Entropy-Collapse-Research`, `notebooks/archive` |
| `1340e-6` | 1 | 1 | 1 | `github_repos/bruno-collapse-simulator` |

<details><summary>Branch breakdown</summary>


**`1.23456789e-23`**

- `CLEAN_WORKSPACE/E3_project_rev1` — 8 site(s)
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/comprehensive_e3_parser.py:52`
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/corrected_e3_parser.py:55`
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/debugged_parser.py:43`
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/final_enhanced_parcer.py:47`
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/final_enhanced_parcer.py:493`
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/final_enhanced_parser_2.py:55`
  - _…2 more_
- `CLEAN_WORKSPACE/e3_engine` — 8 site(s)
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/comprehensive_e3_parser.py:52`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/corrected_e3_parser.py:55`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/debugged_parser.py:43`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/final_enhanced_parcer.py:47`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/final_enhanced_parcer.py:493`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/final_enhanced_parser_2.py:55`
  - _…2 more_
- `E3_CURRENT_PRODUCTION/e3_engine` — 8 site(s)
  - `./E3_CURRENT_PRODUCTION/e3_engine/comprehensive_e3_parser.py:52`
  - `./E3_CURRENT_PRODUCTION/e3_engine/corrected_e3_parser.py:55`
  - `./E3_CURRENT_PRODUCTION/e3_engine/debugged_parser.py:43`
  - `./E3_CURRENT_PRODUCTION/e3_engine/final_enhanced_parcer.py:47`
  - `./E3_CURRENT_PRODUCTION/e3_engine/final_enhanced_parcer.py:493`
  - `./E3_CURRENT_PRODUCTION/e3_engine/final_enhanced_parser_2.py:55`
  - _…2 more_
- `E3_Project/e3_engine` — 8 site(s)
  - `./E3_Project/e3_engine/comprehensive_e3_parser.py:52`
  - `./E3_Project/e3_engine/corrected_e3_parser.py:55`
  - `./E3_Project/e3_engine/debugged_parser.py:43`
  - `./E3_Project/e3_engine/final_enhanced_parcer.py:47`
  - `./E3_Project/e3_engine/final_enhanced_parcer.py:493`
  - `./E3_Project/e3_engine/final_enhanced_parser_2.py:55`
  - _…2 more_
- `comprehensive_e3_parser.py` — 1 site(s)
  - `./comprehensive_e3_parser.py:52`
- `corrected_comprehensive_parser.py` — 1 site(s)
  - `./corrected_comprehensive_parser.py:55`
- `debugged_parser.py` — 1 site(s)
  - `./debugged_parser.py:43`
- `e3_validation_test.py` — 1 site(s)
  - `./e3_validation_test.py:31`
- `enhanced_e3_parser.py` — 1 site(s)
  - `./enhanced_e3_parser.py:55`
- `final_enhanced_parser.py` — 2 site(s)
  - `./final_enhanced_parser.py:47`
  - `./final_enhanced_parser.py:493`
- `large_superconductor_generator.py` — 1 site(s)
  - `./large_superconductor_generator.py:35`
- `universal_materials_parser.py` — 2 site(s)
  - `./universal_materials_parser.py:335`
  - `./universal_materials_parser.py:70`

**`1313`**

- `CLEAN_WORKSPACE/archived_research` — 27 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:193`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:396`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1219`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:575`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:744`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:193`
  - _…21 more_
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 5 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:193`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:396`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:1219`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:575`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:744`
- `E3_Project_OLD_MESSY/archive` — 3 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:235`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:312`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:530`
- `E3_Project_OLD_MESSY/notebooks` — 11 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1489`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:672`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:870`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:319`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:414`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:674`
  - _…5 more_
- `Entropy-Collapse-Research/Scripts` — 3 site(s)
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:235`
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:312`
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:530`
- `bugged_snapshots.json` — 1 site(s)
  - `./bugged_snapshots.json:4716`
- `notebooks/BRUNO_GRCHOMBO_SIMULATION` — 11 site(s)
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:1489`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:672`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:870`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:319`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:414`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:674`
  - _…5 more_
- `notebooks/archive` — 3 site(s)
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:319`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:414`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:674`

**`1366`**

- `CLEAN_WORKSPACE/archived_research` — 31 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:190`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:21`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:358`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:527`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Final/Bruno_collapse_tracker.py:5`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:190`
  - _…25 more_
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 4 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:190`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:21`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:358`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/SCHOLARGPT_TEST1.ipynb:527`
- `E3_Project_OLD_MESSY/archive` — 5 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:150`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:215`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:6`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/SCHOLARGPT TEST1.py.txt:74`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/final/Bruno_collapse_tracker.py:5`
- `E3_Project_OLD_MESSY/notebooks` — 12 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:201`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:35`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:407`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:636`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:121`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:211`
  - _…6 more_
- `Entropy-Collapse-Research/Scripts` — 5 site(s)
  - `./Entropy-Collapse-Research/Scripts/Final/Bruno_collapse_tracker.py:5`
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:150`
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:215`
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:6`
  - `./Entropy-Collapse-Research/Scripts/SCHOLARGPT TEST1.py.txt:74`
- `bruno-simulator-RESTRUCTURED/bruno_framework` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/bruno_framework/historical_scripts/core_development/Bruno_collapse_tracker.py:5`
- `notebooks/BRUNO_GRCHOMBO_SIMULATION` — 12 site(s)
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:201`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:35`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:407`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_FROM_SCRIPT_REBUILT.ipynb:636`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:121`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_COLLAPSE_MASTER.ipynb:211`
  - _…6 more_
- `notebooks/archive` — 4 site(s)
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:121`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:211`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:290`
  - `./notebooks/archive/BRUNO_COLLAPSE_MASTER.ipynb:37`

**`0.001005`**

- `Bruno_model_sim_final.tex` — 3 site(s)
  - `./Bruno_model_sim_final.tex:129`
  - `./Bruno_model_sim_final.tex:560`
  - `./Bruno_model_sim_final.tex:789`
- `Bruno_model_sim_upd.tex` — 3 site(s)
  - `./Bruno_model_sim_upd.tex:112`
  - `./Bruno_model_sim_upd.tex:465`
  - `./Bruno_model_sim_upd.tex:660`
- `Bruno_model_sim_upd_cleaned.tex` — 3 site(s)
  - `./Bruno_model_sim_upd_cleaned.tex:127`
  - `./Bruno_model_sim_upd_cleaned.tex:552`
  - `./Bruno_model_sim_upd_cleaned.tex:776`
- `CLEAN_WORKSPACE/archived_research` — 15 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/theory/Bruno_model.tex:110`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/theory/Bruno_model.tex:411`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/theory/Bruno_model.tex:605`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/Entropy_Collapse.tex:129`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/Entropy_Collapse.tex:560`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/Entropy_Collapse.tex:789`
  - _…9 more_
- `E3_Project_OLD_MESSY/report` — 3 site(s)
  - `./E3_Project_OLD_MESSY/report/latex/LaTex/Entropy_Collapse.tex:129`
  - `./E3_Project_OLD_MESSY/report/latex/LaTex/Entropy_Collapse.tex:560`
  - `./E3_Project_OLD_MESSY/report/latex/LaTex/Entropy_Collapse.tex:789`
- `E3_Project_Tokamak_Analysis/bruno-analysis` — 1 site(s)
  - `./E3_Project_Tokamak_Analysis/bruno-analysis/plasma_data_parser.py:6`
- `bruno-new-dataset/docker-compose.yml` — 1 site(s)
  - `./bruno-new-dataset/docker-compose.yml:9`
- `bruno-new-dataset/grb_predictor.py` — 1 site(s)
  - `./bruno-new-dataset/grb_predictor.py:13`
- `bruno-new-dataset/real_data` — 1 site(s)
  - `./bruno-new-dataset/real_data/docker-compose.yml:9`
- `bruno-new-dataset/scripts` — 2 site(s)
  - `./bruno-new-dataset/scripts/bruno_batse_analyzer.py:13`
  - `./bruno-new-dataset/scripts/bruno_dataset_builder.py:13`
- `bruno-simulator-RESTRUCTURED/notebooks` — 2 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb04_gw_corrmap.ipynb:491`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb04_gw_corrmap.ipynb:65`
- `bruno-simulator-latest/bruno-analysis` — 1 site(s)
  - `./bruno-simulator-latest/bruno-analysis/plasma_data_parser.py:6`
- `bruno-simulator-latest/nb04_gw_corrmap.ipynb` — 2 site(s)
  - `./bruno-simulator-latest/nb04_gw_corrmap.ipynb:491`
  - `./bruno-simulator-latest/nb04_gw_corrmap.ipynb:65`
- `bugged_snapshots.json` — 13 site(s)
  - `./bugged_snapshots.json:42446`
  - `./bugged_snapshots.json:42957`
  - `./bugged_snapshots.json:44337`
  - `./bugged_snapshots.json:44773`
  - `./bugged_snapshots.json:45277`
  - `./bugged_snapshots.json:45297`
  - _…7 more_
- `github_repos/bruno-collapse-simulator` — 2 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb04_gw_corrmap.ipynb:491`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb04_gw_corrmap.ipynb:65`

**`1`**

- `Bruno_model_sim_final.tex` — 1 site(s)
  - `./Bruno_model_sim_final.tex:764`
- `Bruno_model_sim_upd.tex` — 1 site(s)
  - `./Bruno_model_sim_upd.tex:638`
- `Bruno_model_sim_upd_cleaned.tex` — 1 site(s)
  - `./Bruno_model_sim_upd_cleaned.tex:753`
- `CLEAN_WORKSPACE/archived_research` — 5 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/theory/Bruno_model.tex:584`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/Entropy_Collapse.tex:764`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/docs/theory/Bruno_model.tex:584`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/report/latex/Entropy_Collapse.tex:764`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/report/latex/LaTex/Entropy_Collapse.tex:764`
- `E3_Project_OLD_MESSY/report` — 1 site(s)
  - `./E3_Project_OLD_MESSY/report/latex/LaTex/Entropy_Collapse.tex:764`

**`1366.0`**

- `bruno-fluence-app/bruno_fluence_analyzer.py` — 1 site(s)
  - `./bruno-fluence-app/bruno_fluence_analyzer.py:97`
- `bruno-fluence-app/docker-compose.yml` — 1 site(s)
  - `./bruno-fluence-app/docker-compose.yml:20`
- `bruno-fluence-app/setup_bruno_docker.sh` — 1 site(s)
  - `./bruno-fluence-app/setup_bruno_docker.sh:25`
- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/nb01_toy_core.ipynb:73`
- `bruno-simulator-latest/nb01_toy_core.ipynb` — 1 site(s)
  - `./bruno-simulator-latest/nb01_toy_core.ipynb:73`
- `entropy-collapse-transient-engine(1).ipynb` — 1 site(s)
  - `./entropy-collapse-transient-engine(1).ipynb:73`
- `entropy-collapse-transient-engine.ipynb` — 1 site(s)
  - `./entropy-collapse-transient-engine.ipynb:73`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/nb01_toy_core.ipynb:73`

**`1.0e-23`**

- `CLEAN_WORKSPACE/archived_research` — 1 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/archive/Emergent_Gravity_Toy_Model.ipynb:116`
- `bruno-framework-clean/Entropy_Notebook` — 1 site(s)
  - `./bruno-framework-clean/Entropy_Notebook/Emergent_Gravity_Toy_Model.ipynb:116`
- `github_repos/Entropy-Collapse-Research` — 1 site(s)
  - `./github_repos/Entropy-Collapse-Research/Entropy Notebook/Emergent_Gravity_Toy_Model.ipynb:116`
- `notebooks/archive` — 1 site(s)
  - `./notebooks/archive/Emergent_Gravity_Toy_Model.ipynb:116`

**`1340e-6`**

- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/bruno_framework/historical_scripts/core_development/Bruno_collapse_tracker.py:5`

</details>

## `t_hawking_values.txt` — T_H

_No numeric assignments matched._

## `r_schwarzschild_values.txt` — R_s

25 assignment sites, 24 distinct files, 1 distinct values.

| Value | Sites | Files | Unique contents | Branches |
|---|---:|---:|---:|---|
| `2` | 25 | 24 | 4 | `CLEAN_WORKSPACE/analysis_tools`, `CLEAN_WORKSPACE/archived_research`, `E3_Project_OLD_MESSY/archive`, `Entropy-Collapse-Research/Scripts` +5 more |

<details><summary>Branch breakdown</summary>


**`2`**

- `CLEAN_WORKSPACE/analysis_tools` — 1 site(s)
  - `./CLEAN_WORKSPACE/analysis_tools/test_bruno_constant.py:40`
- `CLEAN_WORKSPACE/archived_research` — 7 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:21`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:21`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:21`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Entropy Collapse Test 1.9.py:62`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Entropy Collapse Test 2.1.py:58`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Entropy Collapse Test/Entropy Collapse Test 1.9.py:62`
  - _…1 more_
- `E3_Project_OLD_MESSY/archive` — 3 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Blackhole Entropy Fixed.py:21`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Collapse Test 1.9.py:62`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Collapse Test 2.1.py:58`
- `Entropy-Collapse-Research/Scripts` — 5 site(s)
  - `./Entropy-Collapse-Research/Scripts/Archive/Blackhole Entropy Fixed.py:21`
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Collapse Test 1.9.py:62`
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Collapse Test 2.1.py:58`
  - `./Entropy-Collapse-Research/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.9.py:62`
  - `./Entropy-Collapse-Research/Scripts/Entropy Collapse Test/Entropy Collapse Test 2.1.py:58`
- `bruno-framework-clean/Scripts` — 2 site(s)
  - `./bruno-framework-clean/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.9.py:62`
  - `./bruno-framework-clean/Scripts/Entropy Collapse Test/Entropy Collapse Test 2.1.py:58`
- `bruno-framework-clean/organized_research` — 1 site(s)
  - `./bruno-framework-clean/organized_research/black_holes/Blackhole_Entropy_Fixed.py:21`
- `bugged_snapshots.json` — 2 site(s)
  - `./bugged_snapshots.json:39270`
  - `./bugged_snapshots.json:39347`
- `github_repos/Entropy-Collapse-Research` — 3 site(s)
  - `./github_repos/Entropy-Collapse-Research/Scripts/Blackhole Entropy Fixed.py:21`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.9.py:62`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Collapse Test/Entropy Collapse Test 2.1.py:58`
- `test_bruno_constant.py` — 1 site(s)
  - `./test_bruno_constant.py:40`

</details>

## `schwarzschild.txt` — R_s (wide sweep)

23 assignment sites, 17 distinct files, 1 distinct values.

| Value | Sites | Files | Unique contents | Branches |
|---|---:|---:|---:|---|
| `2` | 23 | 17 | 4 | `CLEAN_WORKSPACE/analysis_tools`, `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_Project_OLD_MESSY/archive` +7 more |

<details><summary>Branch breakdown</summary>


**`2`**

- `CLEAN_WORKSPACE/analysis_tools` — 2 site(s)
  - `./CLEAN_WORKSPACE/analysis_tools/simple_bruno_test.py:41`
  - `./CLEAN_WORKSPACE/analysis_tools/test_bruno_constant.py:40`
- `CLEAN_WORKSPACE/archived_research` — 9 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:708`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:758`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:21`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:708`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:758`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:21`
  - _…3 more_
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 2 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:708`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/simulation/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:758`
- `E3_Project_OLD_MESSY/archive` — 1 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Blackhole Entropy Fixed.py:21`
- `E3_Project_OLD_MESSY/notebooks` — 2 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:708`
  - `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:758`
- `Entropy-Collapse-Research/Scripts` — 1 site(s)
  - `./Entropy-Collapse-Research/Scripts/Archive/Blackhole Entropy Fixed.py:21`
- `bruno-framework-clean/organized_research` — 1 site(s)
  - `./bruno-framework-clean/organized_research/black_holes/Blackhole_Entropy_Fixed.py:21`
- `github_repos/Entropy-Collapse-Research` — 1 site(s)
  - `./github_repos/Entropy-Collapse-Research/Scripts/Blackhole Entropy Fixed.py:21`
- `notebooks/BRUNO_GRCHOMBO_SIMULATION` — 2 site(s)
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:708`
  - `./notebooks/BRUNO_GRCHOMBO_SIMULATION/BRUNO_GRCHOMBO_SIMULATION.ipynb:758`
- `simple_bruno_test.py` — 1 site(s)
  - `./simple_bruno_test.py:41`
- `test_bruno_constant.py` — 1 site(s)
  - `./test_bruno_constant.py:40`

</details>

## `planck_units.txt` — Planck units

58 assignment sites, 43 distinct files, 3 distinct values.

| Value | Sites | Files | Unique contents | Branches |
|---|---:|---:|---:|---|
| `1.616255e-35` | 36 | 36 | 6 | `CLEAN_WORKSPACE/archived_research`, `E3_Project_OLD_MESSY/archive`, `Entropy-Collapse-Research/Scripts`, `bruno-framework-clean/Scripts` +2 more |
| `2.17651e-8` | 15 | 15 | 3 | `CLEAN_WORKSPACE/archived_research`, `E3_Project_OLD_MESSY/archive`, `Entropy-Collapse-Research/Scripts`, `bruno-framework-clean/Scripts` +2 more |
| `1.416808e32` | 7 | 7 | 1 | `CLEAN_WORKSPACE/archived_research`, `E3_Project_OLD_MESSY/archive`, `Entropy-Collapse-Research/Scripts`, `bruno-framework-clean/Scripts` +1 more |

<details><summary>Branch breakdown</summary>


**`1.616255e-35`**

- `CLEAN_WORKSPACE/archived_research` — 12 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Blackhole Entropy Evolution.py:8`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:18`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Blackhole Entropy Observation.py:16`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Blackhole Entropy Evolution.py:8`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Blackhole Entropy Fixed.py:18`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Blackhole Entropy Observation.py:16`
  - _…6 more_
- `E3_Project_OLD_MESSY/archive` — 6 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Blackhole Entropy Evolution.py:8`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Blackhole Entropy Fixed.py:18`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Blackhole Entropy Observation.py:16`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Gravity Relation.py:8`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Obervational Dark Matter.py:8`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Quantum Lock Entropy.py:7`
- `Entropy-Collapse-Research/Scripts` — 6 site(s)
  - `./Entropy-Collapse-Research/Scripts/Archive/Blackhole Entropy Evolution.py:8`
  - `./Entropy-Collapse-Research/Scripts/Archive/Blackhole Entropy Fixed.py:18`
  - `./Entropy-Collapse-Research/Scripts/Archive/Blackhole Entropy Observation.py:16`
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Gravity Relation.py:8`
  - `./Entropy-Collapse-Research/Scripts/Archive/Obervational Dark Matter.py:8`
  - `./Entropy-Collapse-Research/Scripts/Archive/Quantum Lock Entropy.py:7`
- `bruno-framework-clean/Scripts` — 1 site(s)
  - `./bruno-framework-clean/Scripts/Obervational_Dark_Matter.py:8`
- `bruno-framework-clean/organized_research` — 5 site(s)
  - `./bruno-framework-clean/organized_research/black_holes/Blackhole_Entropy_Evolution.py:8`
  - `./bruno-framework-clean/organized_research/black_holes/Blackhole_Entropy_Fixed.py:18`
  - `./bruno-framework-clean/organized_research/black_holes/Blackhole_Entropy_Observation.py:16`
  - `./bruno-framework-clean/organized_research/quantum_mechanics/Quantum_Lock_Entropy.py:7`
  - `./bruno-framework-clean/organized_research/thermodynamics/Entropy_Gravity_Relation.py:8`
- `github_repos/Entropy-Collapse-Research` — 6 site(s)
  - `./github_repos/Entropy-Collapse-Research/Scripts/Blackhole Entropy Evolution.py:8`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Blackhole Entropy Fixed.py:18`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Blackhole Entropy Observation.py:16`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Gravity Relation.py:8`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Obervational Dark Matter.py:8`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Quantum Lock Entropy.py:7`

**`2.17651e-8`**

- `CLEAN_WORKSPACE/archived_research` — 3 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Entropy Gravity Relation.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Obervational Dark Matter.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Quantum Lock Entropy.py:9`
- `E3_Project_OLD_MESSY/archive` — 3 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Gravity Relation.py:10`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Obervational Dark Matter.py:10`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Quantum Lock Entropy.py:9`
- `Entropy-Collapse-Research/Scripts` — 3 site(s)
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Gravity Relation.py:10`
  - `./Entropy-Collapse-Research/Scripts/Archive/Obervational Dark Matter.py:10`
  - `./Entropy-Collapse-Research/Scripts/Archive/Quantum Lock Entropy.py:9`
- `bruno-framework-clean/Scripts` — 1 site(s)
  - `./bruno-framework-clean/Scripts/Obervational_Dark_Matter.py:10`
- `bruno-framework-clean/organized_research` — 2 site(s)
  - `./bruno-framework-clean/organized_research/quantum_mechanics/Quantum_Lock_Entropy.py:9`
  - `./bruno-framework-clean/organized_research/thermodynamics/Entropy_Gravity_Relation.py:10`
- `github_repos/Entropy-Collapse-Research` — 3 site(s)
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Gravity Relation.py:10`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Obervational Dark Matter.py:10`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Quantum Lock Entropy.py:9`

**`1.416808e32`**

- `CLEAN_WORKSPACE/archived_research` — 3 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Planck Scale Entropy.py:7`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Planck Scale Entropy.py:7`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Planck Scale Entropy.py:7`
- `E3_Project_OLD_MESSY/archive` — 1 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Planck Scale Entropy.py:7`
- `Entropy-Collapse-Research/Scripts` — 1 site(s)
  - `./Entropy-Collapse-Research/Scripts/Archive/Planck Scale Entropy.py:7`
- `bruno-framework-clean/Scripts` — 1 site(s)
  - `./bruno-framework-clean/Scripts/Planck_Scale_Entropy.py:7`
- `github_repos/Entropy-Collapse-Research` — 1 site(s)
  - `./github_repos/Entropy-Collapse-Research/Scripts/Planck Scale Entropy.py:7`

</details>

## `relaxation.txt` — tau / relaxation_time

227 assignment sites, 72 distinct files, 18 distinct values.

| Value | Sites | Files | Unique contents | Branches |
|---|---:|---:|---:|---|
| `0` | 30 | 30 | 6 | `CLEAN_WORKSPACE/archived_research`, `E3_Project_OLD_MESSY/archive`, `Entropy-Collapse-Research/Scripts`, `bruno-framework-clean/organized_research` +4 more |
| `3.0` | 144 | 29 | 4 | `Bruno_Entropy_Project/notebooks`, `CLEAN_WORKSPACE/archived_research`, `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1`, `E3_CURRENT_PRODUCTION/notebooks` +11 more |
| `57.68` | 6 | 6 | 1 | `E3_CURRENT_PRODUCTION/notebooks`, `E3_Project/notebooks`, `E3_Project_REBUILT/notebooks`, `bruno-simulator-RESTRUCTURED/notebooks` +2 more |
| `25.00` | 6 | 6 | 1 | `E3_CURRENT_PRODUCTION/notebooks`, `E3_Project/notebooks`, `E3_Project_REBUILT/notebooks`, `bruno-simulator-RESTRUCTURED/notebooks` +2 more |
| `2.28` | 12 | 6 | 1 | `E3_CURRENT_PRODUCTION/notebooks`, `E3_Project/notebooks`, `E3_Project_REBUILT/notebooks`, `bruno-simulator-RESTRUCTURED/notebooks` +2 more |
| `25.0` | 2 | 2 | — | `E3_Project_REBUILT/index.html`, `github_repos/E3_Project` |
| `51.99` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `32.66` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `32.10` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `32.49` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `34.10` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `42.86` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `30.71` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `27.62` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `28.09` | 2 | 2 | 1 | `bruno-simulator-RESTRUCTURED/notebooks`, `github_repos/bruno-collapse-simulator` |
| `5.21` | 3 | 1 | — | `bruno-constant-deep-dive.html` |
| `6.05` | 3 | 1 | — | `bruno-constant-deep-dive.html` |
| `7.79` | 3 | 1 | — | `bruno-constant-deep-dive.html` |

<details><summary>Branch breakdown</summary>


**`0`**

- `CLEAN_WORKSPACE/archived_research` — 15 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Entropy Temp Testing Mod 3.1.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Entropy Temp Testing Mod 3.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Entropy Temp Testing Mod 4.0.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Entropy Temp Testing Mod 3.1.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Entropy Temp Testing Mod 3.py:10`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Entropy Temp Testing Mod 4.0.py:10`
  - _…9 more_
- `E3_Project_OLD_MESSY/archive` — 3 site(s)
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Temp Testing Mod 3.1.py:10`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Temp Testing Mod 3.py:10`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Temp Testing Mod 4.0.py:10`
- `Entropy-Collapse-Research/Scripts` — 3 site(s)
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Temp Testing Mod 3.1.py:10`
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Temp Testing Mod 3.py:10`
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Temp Testing Mod 4.0.py:10`
- `bruno-framework-clean/organized_research` — 3 site(s)
  - `./bruno-framework-clean/organized_research/thermodynamics/Entropy_Temp_Testing_Mod_3.1.py:10`
  - `./bruno-framework-clean/organized_research/thermodynamics/Entropy_Temp_Testing_Mod_3.py:10`
  - `./bruno-framework-clean/organized_research/thermodynamics/Entropy_Temp_Testing_Mod_4.0.py:10`
- `github_repos/Entropy-Collapse-Research` — 3 site(s)
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Temp Testing Mod 3.1.py:10`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Temp Testing Mod 3.py:10`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Temp Testing Mod 4.0.py:10`
- `scr/Entropy Temp Testing Mod 3.1.py` — 1 site(s)
  - `./scr/Entropy Temp Testing Mod 3.1.py:10`
- `scr/Entropy Temp Testing Mod 3.py` — 1 site(s)
  - `./scr/Entropy Temp Testing Mod 3.py:10`
- `scr/Entropy Temp Testing Mod 4.0.py` — 1 site(s)
  - `./scr/Entropy Temp Testing Mod 4.0.py:10`

**`3.0`**

- `Bruno_Entropy_Project/notebooks` — 15 site(s)
  - `./Bruno_Entropy_Project/notebooks/Bruno_Visibility_Model.ipynb:1101`
  - `./Bruno_Entropy_Project/notebooks/Bruno_Visibility_Model.ipynb:1214`
  - `./Bruno_Entropy_Project/notebooks/Bruno_Visibility_Model.ipynb:1619`
  - `./Bruno_Entropy_Project/notebooks/Bruno_Visibility_Model.ipynb:1686`
  - `./Bruno_Entropy_Project/notebooks/Bruno_Visibility_Model.ipynb:756`
  - `./Bruno_Entropy_Project/notebooks/Bruno_timeline_analysis.ipynb:1119`
  - _…9 more_
- `CLEAN_WORKSPACE/archived_research` — 55 site(s)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/archive/Historical_Entropy_Audit.ipynb:1104`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/archive/Historical_Entropy_Audit.ipynb:1217`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/archive/Historical_Entropy_Audit.ipynb:1629`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/archive/Historical_Entropy_Audit.ipynb:1696`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/archive/Historical_Entropy_Audit.ipynb:759`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/legacy/Bruno_timeline_analysis.ipynb:1119`
  - _…49 more_
- `CLEAN_WORKSPACE/bruno-collapse-simulator_rev1` — 10 site(s)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/archive/Historical_Entropy_Audit.ipynb:1104`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/archive/Historical_Entropy_Audit.ipynb:1217`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/archive/Historical_Entropy_Audit.ipynb:1629`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/archive/Historical_Entropy_Audit.ipynb:1696`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/archive/Historical_Entropy_Audit.ipynb:759`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/legacy/Bruno_timeline_analysis.ipynb:1119`
  - _…4 more_
- `E3_CURRENT_PRODUCTION/notebooks` — 5 site(s)
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1104`
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1217`
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1629`
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1696`
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:759`
- `E3_Project/notebooks` — 5 site(s)
  - `./E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1104`
  - `./E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1217`
  - `./E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1629`
  - `./E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1696`
  - `./E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:759`
- `E3_Project_OLD_MESSY/notebooks` — 10 site(s)
  - `./E3_Project_OLD_MESSY/notebooks/Bruno_Visibility_Model.ipynb:1101`
  - `./E3_Project_OLD_MESSY/notebooks/Bruno_Visibility_Model.ipynb:1214`
  - `./E3_Project_OLD_MESSY/notebooks/Bruno_Visibility_Model.ipynb:1619`
  - `./E3_Project_OLD_MESSY/notebooks/Bruno_Visibility_Model.ipynb:1686`
  - `./E3_Project_OLD_MESSY/notebooks/Bruno_Visibility_Model.ipynb:756`
  - `./E3_Project_OLD_MESSY/notebooks/Bruno_timeline_analysis.ipynb:1119`
  - _…4 more_
- `E3_Project_REBUILT/notebooks` — 5 site(s)
  - `./E3_Project_REBUILT/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1104`
  - `./E3_Project_REBUILT/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1217`
  - `./E3_Project_REBUILT/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1629`
  - `./E3_Project_REBUILT/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1696`
  - `./E3_Project_REBUILT/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:759`
- `bruno-simulator-RESTRUCTURED/notebooks` — 5 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1104`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1217`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1629`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1696`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:759`
- `bugged_snapshots.json` — 4 site(s)
  - `./bugged_snapshots.json:57188`
  - `./bugged_snapshots.json:57749`
  - `./bugged_snapshots.json:57876`
  - `./bugged_snapshots.json:58977`
- `github_repos/E3_Project` — 5 site(s)
  - `./github_repos/E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1104`
  - `./github_repos/E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1217`
  - `./github_repos/E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1629`
  - `./github_repos/E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:1696`
  - `./github_repos/E3_Project/notebooks/e3_validation/Historical_Entropy_Audit.ipynb:759`
- `github_repos/bruno-collapse-simulator` — 5 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1104`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1217`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1629`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:1696`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_analysis/Historical_Entropy_Audit.ipynb:759`
- `notebooks/Bruno_Visibility_Model.ipynb` — 5 site(s)
  - `./notebooks/Bruno_Visibility_Model.ipynb:1101`
  - `./notebooks/Bruno_Visibility_Model.ipynb:1214`
  - `./notebooks/Bruno_Visibility_Model.ipynb:1619`
  - `./notebooks/Bruno_Visibility_Model.ipynb:1686`
  - `./notebooks/Bruno_Visibility_Model.ipynb:756`
- `notebooks/Bruno_timeline_analysis.ipynb` — 5 site(s)
  - `./notebooks/Bruno_timeline_analysis.ipynb:1119`
  - `./notebooks/Bruno_timeline_analysis.ipynb:1232`
  - `./notebooks/Bruno_timeline_analysis.ipynb:1637`
  - `./notebooks/Bruno_timeline_analysis.ipynb:1704`
  - `./notebooks/Bruno_timeline_analysis.ipynb:774`
- `notebooks/archive` — 5 site(s)
  - `./notebooks/archive/Historical_Entropy_Audit.ipynb:1104`
  - `./notebooks/archive/Historical_Entropy_Audit.ipynb:1217`
  - `./notebooks/archive/Historical_Entropy_Audit.ipynb:1629`
  - `./notebooks/archive/Historical_Entropy_Audit.ipynb:1696`
  - `./notebooks/archive/Historical_Entropy_Audit.ipynb:759`
- `notebooks/snfluxes-public-master` — 5 site(s)
  - `./notebooks/snfluxes-public-master/Untitled.ipynb:1003`
  - `./notebooks/snfluxes-public-master/Untitled.ipynb:1116`
  - `./notebooks/snfluxes-public-master/Untitled.ipynb:1521`
  - `./notebooks/snfluxes-public-master/Untitled.ipynb:1588`
  - `./notebooks/snfluxes-public-master/Untitled.ipynb:658`

**`57.68`**

- `E3_CURRENT_PRODUCTION/notebooks` — 1 site(s)
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_demos/Project_Archipelago.ipynb:188`
- `E3_Project/notebooks` — 1 site(s)
  - `./E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:188`
- `E3_Project_REBUILT/notebooks` — 1 site(s)
  - `./E3_Project_REBUILT/notebooks/e3_demos/Project_Archipelago.ipynb:188`
- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/Project_Archipelago.ipynb:188`
- `github_repos/E3_Project` — 1 site(s)
  - `./github_repos/E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:188`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/Project_Archipelago.ipynb:188`

**`25.00`**

- `E3_CURRENT_PRODUCTION/notebooks` — 1 site(s)
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_demos/Project_Archipelago.ipynb:875`
- `E3_Project/notebooks` — 1 site(s)
  - `./E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:875`
- `E3_Project_REBUILT/notebooks` — 1 site(s)
  - `./E3_Project_REBUILT/notebooks/e3_demos/Project_Archipelago.ipynb:875`
- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/Project_Archipelago.ipynb:875`
- `github_repos/E3_Project` — 1 site(s)
  - `./github_repos/E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:875`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/Project_Archipelago.ipynb:875`

**`2.28`**

- `E3_CURRENT_PRODUCTION/notebooks` — 2 site(s)
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_demos/Project_Archipelago.ipynb:876`
  - `./E3_CURRENT_PRODUCTION/notebooks/e3_demos/Project_Archipelago.ipynb:877`
- `E3_Project/notebooks` — 2 site(s)
  - `./E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:876`
  - `./E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:877`
- `E3_Project_REBUILT/notebooks` — 2 site(s)
  - `./E3_Project_REBUILT/notebooks/e3_demos/Project_Archipelago.ipynb:876`
  - `./E3_Project_REBUILT/notebooks/e3_demos/Project_Archipelago.ipynb:877`
- `bruno-simulator-RESTRUCTURED/notebooks` — 2 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/Project_Archipelago.ipynb:876`
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/Project_Archipelago.ipynb:877`
- `github_repos/E3_Project` — 2 site(s)
  - `./github_repos/E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:876`
  - `./github_repos/E3_Project/notebooks/e3_demos/Project_Archipelago.ipynb:877`
- `github_repos/bruno-collapse-simulator` — 2 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/Project_Archipelago.ipynb:876`
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/Project_Archipelago.ipynb:877`

**`25.0`**

- `E3_Project_REBUILT/index.html` — 1 site(s)
  - `./E3_Project_REBUILT/index.html:695`
- `github_repos/E3_Project` — 1 site(s)
  - `./github_repos/E3_Project/index.html:695`

**`51.99`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_core/E3_data_prep.ipynb:1188`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_core/E3_data_prep.ipynb:1188`

**`32.66`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:224`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:224`

**`32.10`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:225`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:225`

**`32.49`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:226`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:226`

**`34.10`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:227`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:227`

**`42.86`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:228`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:228`

**`30.71`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:229`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:229`

**`27.62`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:230`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:230`

**`28.09`**

- `bruno-simulator-RESTRUCTURED/notebooks` — 1 site(s)
  - `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation/Virtual_kappa_test.ipynb:231`
- `github_repos/bruno-collapse-simulator` — 1 site(s)
  - `./github_repos/bruno-collapse-simulator/notebooks/e3_validation/Virtual_kappa_test.ipynb:231`

**`5.21`**

- `bruno-constant-deep-dive.html` — 3 site(s)
  - `./bruno-constant-deep-dive.html:142`
  - `./bruno-constant-deep-dive.html:178`
  - `./bruno-constant-deep-dive.html:293`

**`6.05`**

- `bruno-constant-deep-dive.html` — 3 site(s)
  - `./bruno-constant-deep-dive.html:142`
  - `./bruno-constant-deep-dive.html:179`
  - `./bruno-constant-deep-dive.html:298`

**`7.79`**

- `bruno-constant-deep-dive.html` — 3 site(s)
  - `./bruno-constant-deep-dive.html:142`
  - `./bruno-constant-deep-dive.html:180`
  - `./bruno-constant-deep-dive.html:303`

</details>

## `hawking.txt` — T_H (wide sweep)

_No numeric assignments matched._

---

# Analysis

## Finding A — the engine runs on a placeholder, not on κ at all

`self.bruno_constant = 1.23456789e-23`

**32 files, 14 independent contents** — the largest single group in the sweep.
The digits are a 1-2-3-4-5-6-7-8-9 keyboard walk: an unmistakable stub value.

It is not confined to scratch code. It appears in:

- `E3_CURRENT_PRODUCTION/e3_engine/` (8 files) — the tree named as production
- `CLEAN_WORKSPACE/e3_engine/` (16 files)
- `E3_Project/e3_engine/` (8 files)
- **Serialized model artifacts**: `e3_universal_thermal_model_v2_1.json:10`,
  `e3_universal_thermal_model_v2_2.json:10`

The last item matters most. The placeholder is baked into saved model JSON, so
any downstream consumer loading those files inherits it silently — no assignment
statement to notice in review.

**Consequence:** the parser/engine pipeline never used 1313 *or* 1366. Whatever
the engine has been computing is unrelated to either derivation. Results produced
by this pipeline cannot be treated as evidence for any κ value.

## Finding B — the divergence is by component, not by phase

The Phase 3 hypothesis was that one rebuild introduced one value and a later
rebuild another. **The data does not support that.** 1313 and 1366 appear in the
*same* branch list, file for file (20 files each, 5 unique contents each) — and
Phase 2 already showed four notebooks assigning both, 1366 always in earlier
cells and 1313 later.

The real split is by **subsystem**, and the three populations are disjoint:

| Lineage | κ value | Units | Where |
|---|---|---|---|
| Research notebooks | 1313 / 1366 | K⁻¹ | `notebooks/`, `CLEAN_WORKSPACE/archived_research`, `E3_Project_OLD_MESSY`, `github_repos/bruno-collapse-*` |
| Engine / parsers | **1.23456789e-23** | — | `*/e3_engine/`, `E3_CURRENT_PRODUCTION`, `E3_Project` |
| Simulator / GW | 0.001005 | strain | `bruno-simulator-*`, `E3_Project_Tokamak_Analysis` |

Three subsystems, three unrelated constants, one name. No subsystem agrees with
any other, and none is a revision of another — they coexist.

## Finding C — T_H is never a literal in code

`t_hawking_values.txt` and the wide `hawking.txt` sweep yield **zero numeric
assignments**. Every occurrence of T_H in code is a *computed expression*.

The erroneous `T = 1.2 × 10⁻⁸ K` therefore lives only in prose — notes, markdown,
LaTeX — never in an executable line. That explains how it survived: no script
ever evaluated it, so no run could contradict it. It propagated by citation.

Corollary: the code implementing `T_H = ħc³/(8πGMk_B)` is correct wherever it
appears. **The defect is documentary, not computational** — which is why the
κ = 1366 in the notebooks was never caught by running them.

## Finding D — the Schwarzschild side is clean

`R_s` has exactly **one** distinct literal across 24 files: the leading `2` in
`R_s = 2*G*M/c**2`. No competing radius formula exists anywhere in the corpus.
The 183,000 m figure is reproducible (computed: 183,107 m). Nothing to fix here.

## Finding E — Planck units are numerically right, semantically mislabelled

| Value | Files | Is | Named |
|---|---:|---|---|
| `1.616255e-35` | 36 | Planck length (m) | correct |
| `2.17651e-8` | 15 | Planck **mass** (kg) | correct |
| `1.416808e32` | 7 | Planck **temperature** (K) | **`t_planck`** in 7 files |

All three literals match CODATA. The defect is naming: `t_planck` reads as Planck
*time* (5.39e-44 s) but holds Planck *temperature* — off by 76 orders of
magnitude if ever consumed as a time. Confirms the Phase 2 single-file finding at
7 files.

## Finding F — tau is a fitted output, not a constant

227 sites / 18 values. `tau = 3.0` (144 sites) is a default; the scatter
(`57.68`, `25.00`, `2.28`, `51.99`, `32.66`, `32.10`, `32.49`, `34.10`, `42.86`,
`30.71`, `27.62`, `28.09`) is per-material fitted relaxation times, each in
exactly 2 files that are copies of each other. **No contradiction here** — these
are results, not asserted constants. Flagged only to close the question.
