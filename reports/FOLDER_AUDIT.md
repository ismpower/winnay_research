# Folder-Level Audit — filename recurrence and parallel trees

Compares folder names and file-name sets, not contents. Content hashes are used only to say whether same-named files actually agree.

## A. Same filename, divergent content (77 filenames)

These are the silent-replacement risks: one name, more than one non-empty implementation. Ordered by number of competing versions.

| Filename | Versions | Copies | Empty | Spread |
|---|---:|---:|---:|---|
| `README.md` | 27 | 65 | 2 | 17 trees |
| `data_pipeline.md` | 4 | 15 | 0 | 4 trees |
| `bruno_threshold.py` | 3 | 23 | 9 | 12 trees |
| `__init__.py` | 3 | 20 | 1 | 9 trees |
| `registry_logger.py` | 3 | 19 | 0 | 8 trees |
| `Entropy Collapse Test 1.5.py` | 3 | 12 | 1 | 6 trees |
| `Entropy Collapse Paper.TeX` | 3 | 10 | 1 | 5 trees |
| `nakazato_flux_integrator.py` | 3 | 7 | 0 | 4 trees |
| `bruno_registry_builder.py` | 3 | 6 | 0 | 3 trees |
| `bruno_sim_1_entropy_vs_radius.py` | 3 | 5 | 0 | 4 trees |
| `fluence_engine.py` | 2 | 23 | 9 | 12 trees |
| `utils.py` | 2 | 21 | 9 | 8 trees |
| `black_hole_entropy.tex` | 2 | 17 | 1 | 6 trees |
| `entropy_gravity_relation.tex` | 2 | 16 | 1 | 6 trees |
| `readData.py` | 2 | 13 | 0 | 6 trees |
| `Bruno_Betelgeuse_Fluence.ipynb` | 2 | 11 | 0 | 5 trees |
| `Bruno_Readme.md` | 2 | 11 | 0 | 4 trees |
| `DATASET_SCHEMA_LOG.md` | 2 | 11 | 0 | 4 trees |
| `Modified Bh Equations.py` | 2 | 10 | 1 | 6 trees |
| `Cosmis Entropy Hubble Test.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 4.0.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 3.1.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 3.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 2.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 1.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 2.3.py` | 2 | 10 | 1 | 6 trees |
| `Entropy Temp Testing Mod 2.1.py` | 2 | 10 | 1 | 6 trees |
| `README_data.md` | 2 | 9 | 0 | 4 trees |
| `ReadFits.ipynb` | 2 | 9 | 0 | 5 trees |
| `EffectiveAreaUses.ipynb` | 2 | 9 | 0 | 5 trees |
| `Entropy Model Comparison.TeX` | 2 | 9 | 1 | 6 trees |
| `plot_bruno_sky_map.py` | 2 | 8 | 0 | 4 trees |
| `test 1.py` | 2 | 8 | 0 | 4 trees |
| `crossmatch_bruno_with_icecube.py` | 2 | 7 | 0 | 4 trees |
| `extract_asassn_to_fluence.py` | 2 | 7 | 0 | 4 trees |
| `parse_supernova_filter.py` | 2 | 7 | 0 | 3 trees |
| `bruno_highlighted_events.md` | 2 | 7 | 0 | 3 trees |
| `Bruno_collapse_tracker.py` | 2 | 7 | 0 | 5 trees |
| `data_structure_audit.py` | 2 | 6 | 0 | 3 trees |

<details><summary>Per-version locations (top 20)</summary>


### `README.md`

- `191c0ef4` — 9 copy(ies)
  - `./Bruno_Entropy_Project/notebooks/snfluxes-public-master/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/data_and_results/experimental_data/raw/snfluxes-public-master/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/data/raw/snfluxes-public-master/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/notebooks/snfluxes-public-master/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/data/raw/snfluxes-public-master/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/snfluxes-public-master/README.md`
  - `./E3_Project_OLD_MESSY/data/raw/snfluxes-public-master/README.md`
  - `./github_repos/bruno-collapse-unified/data_and_results/experimental_data/raw/snfluxes-public-master/README.md`
  - _…1 more_
- `1dd1cfef` — 8 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/legacy/legacy_home/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/legacy/legacy_home/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/documentation/technical_docs/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/legacy_home/README.md`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/legacy/legacy_home/README.md`
  - `./E3_Project_OLD_MESSY/archive/legacy_notebooks/legacy_home/README.md`
  - `./github_repos/bruno-collapse-unified/documentation/technical_docs/README.md`
  - `./notebooks/legacy_home/README.md`
- `b213de3b` — 6 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/data_and_results/experimental_data/exports/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/data/exports/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/data/exports/README.md`
  - `./E3_Project_OLD_MESSY/data/exports/README.md`
  - `./github_repos/bruno-collapse-unified/data_and_results/experimental_data/exports/README.md`
  - `./github_repos/bruno-collapse-unified/evolution_history/phase1_original_hypothesis/data/exports/README.md`
- `d7221887` — 4 copy(ies)
  - `./E3_CURRENT_PRODUCTION/docs/README.md`
  - `./E3_Project/docs/README.md`
  - `./E3_Project_REBUILT/docs/README.md`
  - `./github_repos/E3_Project/docs/README.md`
- `13e3a7eb` — 4 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/LaTex/Entropy Collapse Paper Final/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/report/latex/LaTex/Entropy Collapse Paper Final/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/report/latex/LaTex/Entropy Collapse Paper Final/README.md`
  - `./E3_Project_OLD_MESSY/report/latex/LaTex/Entropy Collapse Paper final/README.md`
- `b4268a07` — 3 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/bruno_core/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/bruno_core/README.md`
  - `./E3_Project_OLD_MESSY/bruno_core/README.md`
- `961a5148` — 2 copy(ies)
  - `./E3_CURRENT_PRODUCTION/README.md`
  - `./E3_Project/README.md`
- **EMPTY** — 2 copy(ies)
  - `./Entropy-Collapse-Research-main/README.md`
  - `./PCB_V/ethic_lab_projects/PCV_Project/README.md`
- `ac895aac` — 2 copy(ies)
  - `./bruno-framework-clean/README.md`
  - `./github_repos/Entropy-Collapse-Research/README.md`
- `95531473` — 2 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/README.md`
  - `./github_repos/bruno-collapse-unified/README.md`
- `6a23621c` — 2 copy(ies)
  - `./E3_Project_REBUILT/E3_Engine/README.md`
  - `./github_repos/E3_Project/E3_Engine/README.md`
- `ac5389d7` — 2 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/README.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/README.md`
- `ca8145a0` — 2 copy(ies)
  - `./E3_CURRENT_PRODUCTION/external/mdqt-sim/README.md`
  - `./E3_Project/external/mdqt-sim/README.md`
- `d428ab4b` — 2 copy(ies)
  - `./E3_CURRENT_PRODUCTION/external/mdqt-sim/laser-cooling-2019/README.md`
  - `./E3_Project/external/mdqt-sim/laser-cooling-2019/README.md`
- `6c3662ba` — 2 copy(ies)
  - `./E3_CURRENT_PRODUCTION/external/mdqt-sim/magnetized-lif-2021/README.md`
  - `./E3_Project/external/mdqt-sim/magnetized-lif-2021/README.md`
- `92195962` — 1 copy(ies)
  - `./bruno-simulator-latest/README.md`
- `2939f61b` — 1 copy(ies)
  - `./CLEAN_WORKSPACE/README.md`
- `854bb225` — 1 copy(ies)
  - `./CLEAN_WORKSPACE/E3_project_rev1/README.md`
- `85558c98` — 1 copy(ies)
  - `./CLEAN_WORKSPACE/bruno-collapse-unified_rev1/README.md`
- `5ba23e11` — 1 copy(ies)
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/README.md`
- `45441ccc` — 1 copy(ies)
  - `./github_repos/bruno-collapse-simulator/README.md`
- `447655b1` — 1 copy(ies)
  - `./Bruno_Entropy_Project/data/exports/README.md`
- `999035f4` — 1 copy(ies)
  - `./E3_Project_OLD_MESSY/README.md`
- `207b2211` — 1 copy(ies)
  - `./sne-1990-1999-master/README.md`
- `4d294a38` — 1 copy(ies)
  - `./bruno-simulator-RESTRUCTURED/README.md`
- `33f6d87c` — 1 copy(ies)
  - `./snewpy-models-presn-master/README.md`
- `360dcb65` — 1 copy(ies)
  - `./sne-2000-2004-master/README.md`
- `addb7478` — 1 copy(ies)
  - `./sne-2005-2009-master/README.md`

### `data_pipeline.md`

- `ea451345` — 8 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/pipeline/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/docs/pipeline/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/documentation/technical_docs/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/docs/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/docs/data_pipeline.md`
  - `./E3_Project_OLD_MESSY/docs/data_pipeline.md`
  - `./E3_Project_OLD_MESSY/docs/pipeline/data_pipeline.md`
  - `./github_repos/bruno-collapse-unified/documentation/technical_docs/data_pipeline.md`
- `6505cfce` — 5 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/utilities/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/utilities/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/scripts/utilities/data_pipeline.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/utilities/data_pipeline.md`
  - `./E3_Project_OLD_MESSY/scripts/utilities/data_pipeline.md`
- `4972f8ed` — 1 copy(ies)
  - `./Bruno_Entropy_Project/docs/data_pipeline.md`
- `5698803e` — 1 copy(ies)
  - `./Bruno_Entropy_Project/scripts/utilities/data_pipeline.md`

### `bruno_threshold.py`

- **EMPTY** — 9 copy(ies)
  - `./Bruno_Entropy_Project/bruno_core/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/E3_project_rev1/bruno_framework/bruno_core/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/bruno_core_unified/theory/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/bruno_core/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/bruno_framework/bruno_core/bruno_threshold.py`
  - `./github_repos/bruno-collapse-unified/computational_development/bruno_framework/bruno_threshold.py`
  - _…1 more_
- `02890648` — 9 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/bruno_core/bruno_threshold.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/bruno_core/bruno_threshold.py`
  - `./E3_CURRENT_PRODUCTION/bruno_framework/theory/bruno_threshold.py`
  - `./E3_Project/bruno_framework/theory/bruno_threshold.py`
  - `./E3_Project_OLD_MESSY/bruno_core/bruno_threshold.py`
  - `./E3_Project_REBUILT/bruno_framework/theory/bruno_threshold.py`
  - `./bruno-simulator-RESTRUCTURED/bruno_framework/theory/bruno_threshold.py`
  - `./github_repos/E3_Project/bruno_framework/theory/bruno_threshold.py`
  - _…1 more_
- `88c535c4` — 4 copy(ies)
  - `./bruno-fluence-app/bruno_threshold.py`
  - `./bruno-framework-clean/organized_research/astronomical_analysis/bruno_threshold.py`
  - `./bruno-new-dataset/scripts/bruno_threshold.py`
  - `./bruno-real-analyzer/bruno_threshold.py`
- `4e0907a7` — 1 copy(ies)
  - `./github_repos/bruno-collapse-unified/bruno_core_unified/theory/bruno_threshold.py`

### `__init__.py`

- `f580f432` — 10 copy(ies)
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/core/__init__.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/bruno_core/__init__.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/bruno_core/__init__.py`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/core/__init__.py`
  - `./E3_CURRENT_PRODUCTION/e3_engine/core/__init__.py`
  - `./E3_Project/e3_engine/core/__init__.py`
  - `./E3_Project_REBUILT/E3_Engine/core/__init__.py`
  - `./bruno-simulator-RESTRUCTURED/e3_engine/core/__init__.py`
  - _…2 more_
- `942ec63d` — 6 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/__init__.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/bruno_core/__init__.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/__init__.py`
  - `./E3_Project_OLD_MESSY/bruno_core/__init__.py`
  - `./github_repos/bruno-collapse-unified/computational_development/bruno_framework/__init__.py`
  - `./github_repos/bruno-collapse-unified/evolution_history/phase1_original_hypothesis/bruno_core/__init__.py`
- `eca8166e` — 3 copy(ies)
  - `./Bruno_Entropy_Project/bruno_core/__init__.py`
  - `./CLEAN_WORKSPACE/E3_project_rev1/bruno_framework/bruno_core/__init__.py`
  - `./CLEAN_WORKSPACE/bruno_framework/bruno_core/__init__.py`
- **EMPTY** — 1 copy(ies)
  - `./PCB_V/ethic_lab_projects/PCV_Project/pcv_tool/__init__.py`

### `registry_logger.py`

- `cd042bae` — 10 copy(ies)
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/core/registry_logger.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/bruno_core/registry_logger.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/bruno_core/registry_logger.py`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/core/registry_logger.py`
  - `./E3_CURRENT_PRODUCTION/e3_engine/core/registry_logger.py`
  - `./E3_Project/e3_engine/core/registry_logger.py`
  - `./E3_Project_REBUILT/E3_Engine/core/registry_logger.py`
  - `./bruno-simulator-RESTRUCTURED/e3_engine/core/registry_logger.py`
  - _…2 more_
- `f753eb67` — 6 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/registry_logger.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/bruno_core/registry_logger.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/registry_logger.py`
  - `./E3_Project_OLD_MESSY/bruno_core/registry_logger.py`
  - `./github_repos/bruno-collapse-unified/computational_development/bruno_framework/registry_logger.py`
  - `./github_repos/bruno-collapse-unified/evolution_history/phase1_original_hypothesis/bruno_core/registry_logger.py`
- `1e9eaa11` — 3 copy(ies)
  - `./Bruno_Entropy_Project/bruno_core/registry_logger.py`
  - `./CLEAN_WORKSPACE/E3_project_rev1/bruno_framework/bruno_core/registry_logger.py`
  - `./CLEAN_WORKSPACE/bruno_framework/bruno_core/registry_logger.py`

### `Entropy Collapse Test 1.5.py`

- `e773411e` — 5 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Entropy Collapse Test 1.5.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Entropy Collapse Test 1.5.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Entropy Collapse Test 1.5.py`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Entropy Collapse Test 1.5.py`
  - `./Entropy-Collapse-Research/Scripts/Archive/Entropy Collapse Test 1.5.py`
- `c45ecc4b` — 4 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Entropy Collapse Test/Entropy Collapse Test 1.5.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Entropy Collapse Test/Entropy Collapse Test 1.5.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Entropy Collapse Test/Entropy Collapse Test 1.5.py`
  - `./Entropy-Collapse-Research/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.5.py`
- `41f64069` — 2 copy(ies)
  - `./bruno-framework-clean/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.5.py`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.5.py`
- **EMPTY** — 1 copy(ies)
  - `./Entropy-Collapse-Research-main/Scripts/Entropy Collapse Test/Entropy Collapse Test 1.5.py`

### `Entropy Collapse Paper.TeX`

- `ea01b606` — 4 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/LaTex/Entropy Collapse Paper Archive/Entropy Collapse Paper.TeX`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/report/latex/LaTex/Entropy Collapse Paper Archive/Entropy Collapse Paper.TeX`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/report/latex/LaTex/Entropy Collapse Paper Archive/Entropy Collapse Paper.TeX`
  - `./E3_Project_OLD_MESSY/report/latex/LaTex/Entropy Collapse Paper archive/Entropy Collapse Paper.TeX`
- `857ad04b` — 3 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/overview/New folder/Entropy Collapse Paper.TeX`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/report/overview/New folder/Entropy Collapse Paper.TeX`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/report/overview/New folder/Entropy Collapse Paper.TeX`
- `a4ec6aa3` — 2 copy(ies)
  - `./bruno-framework-clean/LaTex/Entropy Collapse Paper.TeX`
  - `./github_repos/Entropy-Collapse-Research/LaTex/Entropy Collapse Paper.TeX`
- **EMPTY** — 1 copy(ies)
  - `./Entropy-Collapse-Research-main/LaTex/Entropy Collapse Paper.TeX`

### `nakazato_flux_integrator.py`

- `6ce101a0` — 5 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/nakazato_flux_integrator.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/nakazato_flux_integrator.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/scripts/nakazato_flux_integrator.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/nakazato_flux_integrator.py`
  - `./E3_Project_OLD_MESSY/scripts/nakazato_flux_integrator.py`
- `7365d052` — 1 copy(ies)
  - `./2025.05.10/archive/nakazato_flux_integrator.py`
- `886f4b9f` — 1 copy(ies)
  - `./Bruno_Entropy_Project/scripts/nakazato_flux_integrator.py`

### `bruno_registry_builder.py`

- `8cf4d868` — 4 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/bruno_registry_builder.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/bruno_registry_builder.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/scripts/bruno_registry_builder.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/bruno_registry_builder.py`
- `06c08d82` — 1 copy(ies)
  - `./2025.05.10/archive/bruno_registry_builder.py`
- `fd260616` — 1 copy(ies)
  - `./Bruno_Entropy_Project/scripts/bruno_registry_builder.py`

### `bruno_sim_1_entropy_vs_radius.py`

- `6a253eb5` — 3 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/simulation/bruno_constant/bruno_sim_1_entropy_vs_radius.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/simulation/bruno_constant/bruno_sim_1_entropy_vs_radius.py`
  - `./E3_Project_OLD_MESSY/scripts/simulation/bruno_constant/bruno_sim_1_entropy_vs_radius.py`
- `48012dd1` — 1 copy(ies)
  - `./bruno_sim_1_entropy_vs_radius.py`
- `0711f345` — 1 copy(ies)
  - `./bruno-simulator-latest/bruno_sim_1_entropy_vs_radius.py`

### `fluence_engine.py`

- `e668ed02` — 10 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/bruno_core/fluence_engine.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/bruno_core/fluence_engine.py`
  - `./E3_CURRENT_PRODUCTION/bruno_framework/applications/fluence_engine.py`
  - `./E3_Project/bruno_framework/applications/fluence_engine.py`
  - `./E3_Project_OLD_MESSY/bruno_core/fluence_engine.py`
  - `./E3_Project_REBUILT/bruno_framework/applications/fluence_engine.py`
  - `./bruno-simulator-RESTRUCTURED/bruno_framework/theory/fluence_engine.py`
  - `./github_repos/E3_Project/bruno_framework/applications/fluence_engine.py`
  - _…2 more_
- **EMPTY** — 9 copy(ies)
  - `./Bruno_Entropy_Project/bruno_core/fluence_engine.py`
  - `./CLEAN_WORKSPACE/E3_project_rev1/bruno_framework/bruno_core/fluence_engine.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/bruno_core_unified/computation/fluence_engine.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/fluence_engine.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/bruno_core/fluence_engine.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/fluence_engine.py`
  - `./CLEAN_WORKSPACE/bruno_framework/bruno_core/fluence_engine.py`
  - `./github_repos/bruno-collapse-unified/computational_development/bruno_framework/fluence_engine.py`
  - _…1 more_
- `cf084d7a` — 4 copy(ies)
  - `./bruno-fluence-app/fluence_engine.py`
  - `./bruno-framework-clean/organized_research/astronomical_analysis/fluence_engine.py`
  - `./bruno-new-dataset/scripts/fluence_engine.py`
  - `./bruno-real-analyzer/fluence_engine.py`

### `utils.py`

- `401a9e56` — 11 copy(ies)
  - `./CLEAN_WORKSPACE/E3_project_rev1/e3_engine/e3_engine/core/utils.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/bruno_core/utils.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/bruno_core/utils.py`
  - `./CLEAN_WORKSPACE/e3_engine/e3_engine/core/utils.py`
  - `./E3_CURRENT_PRODUCTION/e3_engine/core/utils.py`
  - `./E3_Project/e3_engine/core/utils.py`
  - `./E3_Project_OLD_MESSY/bruno_core/utils.py`
  - `./E3_Project_REBUILT/E3_Engine/core/utils.py`
  - _…3 more_
- **EMPTY** — 9 copy(ies)
  - `./Bruno_Entropy_Project/bruno_core/utils.py`
  - `./CLEAN_WORKSPACE/E3_project_rev1/bruno_framework/bruno_core/utils.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/bruno_core_unified/computation/utils.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/utils.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/bruno_core/utils.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/utils.py`
  - `./CLEAN_WORKSPACE/bruno_framework/bruno_core/utils.py`
  - `./github_repos/bruno-collapse-unified/computational_development/bruno_framework/utils.py`
  - _…1 more_
- `b5b8950e` — 1 copy(ies)
  - `./github_repos/bruno-collapse-unified/bruno_core_unified/computation/utils.py`

### `black_hole_entropy.tex`

- `2ef4dbc2` — 9 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/formulas/black_hole_entropy.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/documentation/technical_docs/black_hole_entropy.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/formulas/black_hole_entropy.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/legacy_import/repo- 1/z-entropy-hypothesis-history/equations/black_hole_entropy.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/report/overview/New folder/black_hole_entropy.tex`
  - `./E3_Project_OLD_MESSY/bruno_core/formulas/black_hole_entropy.tex`
  - `./E3_Project_OLD_MESSY/legacy_import/repo- 1/z-entropy-hypothesis-history/equations/black_hole_entropy.tex`
  - `./github_repos/bruno-collapse-unified/computational_development/bruno_framework/formulas/black_hole_entropy.tex`
  - _…1 more_
- `c2e5db64` — 7 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/black_hole_entropy.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/report/latex/black_hole_entropy.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/legacy_import/history/Entropy_Hypothesis_History/Equations/black_hole_entropy.tex`
  - `./E3_Project_OLD_MESSY/legacy_import/history/Entropy_Hypothesis_History/Equations/black_hole_entropy.tex`
  - `./Entropy_Hypothesis_History/Equations/black_hole_entropy.tex`
  - `./bruno-framework-clean/Entropy_Hypothesis_History/Equations/black_hole_entropy.tex`
  - `./github_repos/Entropy-Collapse-Research/Entropy_Hypothesis_History/Equations/black_hole_entropy.tex`
- **EMPTY** — 1 copy(ies)
  - `./Entropy-Collapse-Research-main/Entropy_Hypothesis_History/Equations/black_hole_entropy.tex`

### `entropy_gravity_relation.tex`

- `56e0b470` — 10 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/report/latex/entropy_gravity_relation.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/report/latex/entropy_gravity_relation.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/computational_development/bruno_framework/formulas/entropy_gravity_relation.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/documentation/technical_docs/entropy_gravity_relation.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/bruno_core/formulas/entropy_gravity_relation.tex`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/legacy_import/repo- 1/z-entropy-hypothesis-history/equations/entropy_gravity_relation.tex`
  - `./E3_Project_OLD_MESSY/bruno_core/formulas/entropy_gravity_relation.tex`
  - `./E3_Project_OLD_MESSY/legacy_import/repo- 1/z-entropy-hypothesis-history/equations/entropy_gravity_relation.tex`
  - _…2 more_
- `a98624d7` — 5 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/legacy_import/history/Entropy_Hypothesis_History/Equations/entropy_gravity_relation.tex`
  - `./E3_Project_OLD_MESSY/legacy_import/history/Entropy_Hypothesis_History/Equations/entropy_gravity_relation.tex`
  - `./Entropy_Hypothesis_History/Equations/entropy_gravity_relation.tex`
  - `./bruno-framework-clean/Entropy_Hypothesis_History/Equations/entropy_gravity_relation.tex`
  - `./github_repos/Entropy-Collapse-Research/Entropy_Hypothesis_History/Equations/entropy_gravity_relation.tex`
- **EMPTY** — 1 copy(ies)
  - `./Entropy-Collapse-Research-main/Entropy_Hypothesis_History/Equations/entropy_gravity_relation.tex`

### `readData.py`

- `ae164336` — 12 copy(ies)
  - `./Bruno_Entropy_Project/notebooks/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/legacy_import/dupe_archive_final/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/legacy_import/dupe_archive_final/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/data_and_results/experimental_data/raw/Patton_2017/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/data/raw/Patton_2017/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/notebooks/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/data/raw/Patton_2017/readData.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/readData.py`
  - _…4 more_
- `62d11b3d` — 1 copy(ies)
  - `./snewpy-models-presn-master/models/Patton_2017/readData.py`

### `Bruno_Betelgeuse_Fluence.ipynb`

- `f26f9469` — 7 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/notebooks/analysis/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/notebooks/analysis/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
  - `./CLEAN_WORKSPACE/bruno-collapse-simulator_rev1/notebooks/analysis/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
  - `./bruno-simulator-RESTRUCTURED/bruno_framework/legacy_research/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
  - `./github_repos/bruno-collapse-simulator/bruno_framework/legacy_research/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
  - `./notebooks/Betelgeuse_Entropy_audit/Bruno_Betelgeuse_Fluence.ipynb`
- `f16c1f3e` — 4 copy(ies)
  - `./Bruno_Entropy_Project/notebooks/Bruno_Betelgeuse_Fluence.ipynb`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/notebooks/Bruno_Betelgeuse_Fluence.ipynb`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/notebooks/Bruno_Betelgeuse_Fluence.ipynb`
  - `./notebooks/Bruno_Betelgeuse_Fluence.ipynb`

### `Bruno_Readme.md`

- `cd40251a` — 10 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/registry/Bruno_Readme.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/docs/registry/Bruno_Readme.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/data_and_results/experimental_data/registry/Bruno_Readme.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/documentation/technical_docs/Bruno_Readme.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/data/registry/Bruno_Readme.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/data/registry/Bruno_Readme.md`
  - `./E3_Project_OLD_MESSY/data/registry/Bruno_Readme.md`
  - `./E3_Project_OLD_MESSY/docs/registry/Bruno_Readme.md`
  - _…2 more_
- `0c4cb93e` — 1 copy(ies)
  - `./Bruno_Entropy_Project/data/registry/Bruno_Readme.md`

### `DATASET_SCHEMA_LOG.md`

- `45711edb` — 10 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/docs/registry/DATASET_SCHEMA_LOG.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/docs/registry/DATASET_SCHEMA_LOG.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/data_and_results/experimental_data/registry/DATASET_SCHEMA_LOG.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/documentation/technical_docs/DATASET_SCHEMA_LOG.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase1_original_hypothesis/data/registry/DATASET_SCHEMA_LOG.md`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/data/registry/DATASET_SCHEMA_LOG.md`
  - `./E3_Project_OLD_MESSY/data/registry/DATASET_SCHEMA_LOG.md`
  - `./E3_Project_OLD_MESSY/docs/registry/DATASET_SCHEMA_LOG.md`
  - _…2 more_
- `9461aa88` — 1 copy(ies)
  - `./Bruno_Entropy_Project/data/registry/DATASET_SCHEMA_LOG.md`

### `Modified Bh Equations.py`

- `f69f8ad2` — 7 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Modified Bh Equations.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Modified Bh Equations.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase2_research_expansion/scripts/scr/Modified Bh Equations.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Modified Bh Equations.py`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Modified Bh Equations.py`
  - `./Entropy-Collapse-Research/Scripts/Archive/Modified Bh Equations.py`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Modified Bh Equations.py`
- `78f6a25c` — 2 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase2_research_expansion/entropy-hypothesis/scr/Modified Bh Equations.py`
  - `./scr/Modified Bh Equations.py`
- **EMPTY** — 1 copy(ies)
  - `./Entropy-Collapse-Research-main/Scripts/Modified Bh Equations.py`

### `Cosmis Entropy Hubble Test.py`

- `ec786f5b` — 7 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-backup/scripts/legacy_import/Archive/Cosmis Entropy Hubble Test.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-collapse-unified/scripts/legacy_import/Archive/Cosmis Entropy Hubble Test.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase2_research_expansion/scripts/scr/Cosmis Entropy Hubble Test.py`
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase3_unified_framework/scripts/legacy_import/Archive/Cosmis Entropy Hubble Test.py`
  - `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive/Cosmis Entropy Hubble Test.py`
  - `./Entropy-Collapse-Research/Scripts/Archive/Cosmis Entropy Hubble Test.py`
  - `./github_repos/Entropy-Collapse-Research/Scripts/Cosmis Entropy Hubble Test.py`
- `818a0034` — 2 copy(ies)
  - `./CLEAN_WORKSPACE/archived_research/bruno-unified-rev1/evolution_history/phase2_research_expansion/entropy-hypothesis/scr/Cosmis Entropy Hubble Test.py`
  - `./scr/Cosmis Entropy Hubble Test.py`
- **EMPTY** — 1 copy(ies)
  - `./Entropy-Collapse-Research-main/Scripts/Cosmis Entropy Hubble Test.py`

</details>

## B. Near-identical directories (233 pairs, Jaccard >= 0.6)

`Shared` = filenames in both. `Identical` = of those, how many have the same content. A pair with Shared >> Identical is two trees that *look* like copies but have drifted.

| Jaccard | Dir A | Dir B | Shared | Identical |
|---:|---|---|---:|---:|
| 1.00 | `./github_repos/bruno-collapse-unified/computational_development/bruno_framework` | `./github_repos/bruno-collapse-unified/evolution_history/phase1_original_hypothesis/bruno_core` | 5 | 5 |
| 1.00 | `./github_repos/E3_Project/E3_Engine/core` | `./github_repos/bruno-collapse-simulator/e3_engine/core` | 4 | 4 |
| 1.00 | `./bruno-simulator-RESTRUCTURED/notebooks/e3_validation` | `./github_repos/bruno-collapse-simulator/notebooks/e3_validation` | 5 | 5 |
| 1.00 | `./bruno-simulator-RESTRUCTURED/notebooks/e3_core` | `./github_repos/bruno-collapse-simulator/notebooks/e3_core` | 7 | 7 |
| 1.00 | `./bruno-simulator-RESTRUCTURED/e3_engine/core` | `./github_repos/bruno-collapse-simulator/e3_engine/core` | 4 | 4 |
| 1.00 | `./bruno-simulator-RESTRUCTURED/e3_engine/core` | `./github_repos/E3_Project/E3_Engine/core` | 4 | 4 |
| 1.00 | `./bruno-framework-clean/Scripts/Entropy Collapse Test` | `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Collapse Test` | 19 | 19 |
| 1.00 | `./bruno-framework-clean/LaTex/Entropy Collapse Paper 1.0` | `./github_repos/Entropy-Collapse-Research/LaTex/Entropy Collapse Paper 1.0` | 7 | 7 |
| 1.00 | `./bruno-framework-clean/Entropy_Hypothesis_History/Hypothesis` | `./github_repos/Entropy-Collapse-Research/Entropy_Hypothesis_History/Hypothesis` | 11 | 11 |
| 1.00 | `./Entropy_Hypothesis_History/Hypothesis` | `./github_repos/Entropy-Collapse-Research/Entropy_Hypothesis_History/Hypothesis` | 11 | 11 |
| 1.00 | `./Entropy_Hypothesis_History/Hypothesis` | `./bruno-framework-clean/Entropy_Hypothesis_History/Hypothesis` | 11 | 11 |
| 1.00 | `./Entropy-Collapse-Research-main/Scripts/Entropy Collapse Test` | `./github_repos/Entropy-Collapse-Research/Scripts/Entropy Collapse Test` | 19 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/Scripts/Entropy Collapse Test` | `./bruno-framework-clean/Scripts/Entropy Collapse Test` | 19 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/Scripts` | `./github_repos/Entropy-Collapse-Research/Scripts` | 92 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/LaTex/Entropy Collapse Paper 1.0` | `./github_repos/Entropy-Collapse-Research/LaTex/Entropy Collapse Paper 1.0` | 7 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/LaTex/Entropy Collapse Paper 1.0` | `./bruno-framework-clean/LaTex/Entropy Collapse Paper 1.0` | 7 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/Entropy_Hypothesis_History/Hypothesis` | `./github_repos/Entropy-Collapse-Research/Entropy_Hypothesis_History/Hypothesis` | 11 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/Entropy_Hypothesis_History/Hypothesis` | `./bruno-framework-clean/Entropy_Hypothesis_History/Hypothesis` | 11 | 0 ⚠️ |
| 1.00 | `./Entropy-Collapse-Research-main/Entropy_Hypothesis_History/Hypothesis` | `./Entropy_Hypothesis_History/Hypothesis` | 11 | 0 ⚠️ |
| 1.00 | `./E3_Project_Tokamak_Analysis/bruno-analysis` | `./bruno-simulator-latest/bruno-analysis` | 5 | 5 |
| 1.00 | `./E3_Project_REBUILT/docs` | `./github_repos/E3_Project/docs` | 4 | 4 |
| 1.00 | `./E3_Project_REBUILT/E3_Engine/core` | `./github_repos/bruno-collapse-simulator/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_Project_REBUILT/E3_Engine/core` | `./github_repos/E3_Project/E3_Engine/core` | 4 | 4 |
| 1.00 | `./E3_Project_REBUILT/E3_Engine/core` | `./bruno-simulator-RESTRUCTURED/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_Project_REBUILT/E3_Engine` | `./github_repos/E3_Project/E3_Engine` | 13 | 13 |
| 1.00 | `./E3_Project_OLD_MESSY/notebooks/BRUNO_GRCHOMBO_SIMULATION` | `./notebooks/BRUNO_GRCHOMBO_SIMULATION` | 5 | 5 |
| 1.00 | `./E3_Project_OLD_MESSY/legacy_import/history/Entropy_Hypothesis_History/Hypothesis` | `./github_repos/Entropy-Collapse-Research/Entropy_Hypothesis_History/Hypothesis` | 11 | 11 |
| 1.00 | `./E3_Project_OLD_MESSY/legacy_import/history/Entropy_Hypothesis_History/Hypothesis` | `./bruno-framework-clean/Entropy_Hypothesis_History/Hypothesis` | 11 | 11 |
| 1.00 | `./E3_Project_OLD_MESSY/legacy_import/history/Entropy_Hypothesis_History/Hypothesis` | `./Entropy_Hypothesis_History/Hypothesis` | 11 | 11 |
| 1.00 | `./E3_Project_OLD_MESSY/legacy_import/history/Entropy_Hypothesis_History/Hypothesis` | `./Entropy-Collapse-Research-main/Entropy_Hypothesis_History/Hypothesis` | 11 | 0 ⚠️ |
| 1.00 | `./E3_Project_OLD_MESSY/archive/legacy_scripts/archive` | `./Entropy-Collapse-Research/Scripts/Archive` | 111 | 111 |
| 1.00 | `./E3_Project_OLD_MESSY/archive/legacy_notebooks/legacy_home` | `./notebooks/legacy_home` | 7 | 7 |
| 1.00 | `./E3_Project/e3_engine/core` | `./github_repos/bruno-collapse-simulator/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_Project/e3_engine/core` | `./github_repos/E3_Project/E3_Engine/core` | 4 | 4 |
| 1.00 | `./E3_Project/e3_engine/core` | `./bruno-simulator-RESTRUCTURED/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_Project/e3_engine/core` | `./E3_Project_REBUILT/E3_Engine/core` | 4 | 4 |
| 1.00 | `./E3_Project/docs` | `./github_repos/E3_Project/docs` | 4 | 4 |
| 1.00 | `./E3_Project/docs` | `./E3_Project_REBUILT/docs` | 4 | 4 |
| 1.00 | `./E3_CURRENT_PRODUCTION/e3_engine/core` | `./github_repos/bruno-collapse-simulator/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_CURRENT_PRODUCTION/e3_engine/core` | `./github_repos/E3_Project/E3_Engine/core` | 4 | 4 |
| 1.00 | `./E3_CURRENT_PRODUCTION/e3_engine/core` | `./bruno-simulator-RESTRUCTURED/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_CURRENT_PRODUCTION/e3_engine/core` | `./E3_Project_REBUILT/E3_Engine/core` | 4 | 4 |
| 1.00 | `./E3_CURRENT_PRODUCTION/e3_engine/core` | `./E3_Project/e3_engine/core` | 4 | 4 |
| 1.00 | `./E3_CURRENT_PRODUCTION/e3_engine` | `./E3_Project/e3_engine` | 16 | 16 |
| 1.00 | `./E3_CURRENT_PRODUCTION/docs` | `./github_repos/E3_Project/docs` | 4 | 4 |

---

# Analysis

## Finding G — `Entropy-Collapse-Research-main` is a hollow tree

**All 111 `.py` files in it are zero bytes.** Filenames and directory structure
are intact; content is absent.

| Tree | `.py` files | empty |
|---|---:|---:|
| `Entropy-Collapse-Research-main` | 111 | **111** |
| `github_repos/Entropy-Collapse-Research` | 111 | 0 |
| `Entropy-Collapse-Research` | 134 | 0 |
| `bruno-framework-clean` | 114 | 0 |

**441 zero-byte files** corpus-wide (non-noise). This is almost certainly a failed
clone or a `git checkout` that never fetched blobs.

It contaminates any name-based comparison: a directory listing makes
`Entropy-Collapse-Research-main` look like a complete parallel copy. It is not.
**Delete it — nothing is lost.**

## Finding H — most apparent "drift" is the hollow tree, not divergence

Of 233 directory pairs with ≥60% filename overlap, 72 showed content
disagreement. Decomposed:

| Cause | Pairs |
|---|---:|
| One side has empty files | **59** |
| **Genuine content drift** | **13** |

So the corpus is *more* redundant than the raw numbers suggested, not less. The
13 real cases:

- `Bruno_Entropy_Project/scripts/utilities` vs 5 other trees — 8 shared names,
  **0 identical**. A genuinely forked utility set.
- `bruno_core` in `bruno-collapse-backup` / `bruno-collapse-unified` vs
  `E3_Project_OLD_MESSY` — 7 shared, 5 identical, **2 diverged**.
- `phase2_research_expansion/entropy-hypothesis/scr` vs
  `phase2_research_expansion/scripts/scr` vs top-level `./scr` — 10 shared,
  0 identical. Three-way fork of the same directory inside one tree.

## Finding I — `bruno_threshold.py`: 23 copies, 4 contents

| Content | Copies | Where |
|---|---:|---|
| `02890648` (1437 B, CRLF) | 9 | `E3_CURRENT_PRODUCTION`, `E3_Project`, `E3_Project_REBUILT`, `bruno-simulator-RESTRUCTURED`, `CLEAN_WORKSPACE/archived_research` ×2, `E3_Project_OLD_MESSY`, `github_repos` ×2 |
| `88c535c4` (1389 B, LF) | 4 | `bruno-fluence-app`, `bruno-framework-clean`, `bruno-new-dataset`, `bruno-real-analyzer` |
| `4e0907a7` (1639 B) | **1** | `github_repos/bruno-collapse-unified/bruno_core_unified/theory/` |
| empty | 9 | `Bruno_Entropy_Project`, `CLEAN_WORKSPACE/*` ×5, `github_repos/bruno-collapse-unified/*` ×2 |

`02890648` vs `88c535c4` differ **only in line endings** (48 lines, 48 bytes) —
same code. The real outlier is the single copy `4e0907a7`, which adds:

```python
# Bruno Constant - Final experimentally validated value
BRUNO_CONSTANT_KAPPA = 1340e-6  # K⁻¹s⁻¹ (1340 ± 60 × 10⁻⁶)
```

This is the **only** place in the corpus where κ = 1340e-6 is bound to a named
module constant, and it is labelled "Final experimentally validated value" —
directly contradicting `BRUNO_CONSTANT_FINAL_ANALYSIS.md`, which calls the same
value erroneous and orders it removed. Two documents, each calling itself final,
each rejecting the other's value.

## Finding J — two substantive equation errors in `github_repos/Entropy-Collapse-Research/Scripts/`

These are in the *populated* twin of the hollow tree, so they are live code.

**`Hawking Radiation Comparison.py`** — Boltzmann constant omitted:

```python
T_H_standard = [(hbar * c**3) / (8 * pi * G * M) for M in mass_values]   # no k_B
```

Correct: `ħc³/(8πGMk_B)`. As written it returns **joules, not kelvin** — off by
1/k_B = 7.24 × 10²². The file also sets `c = 3.0e8`. It then adds a constant
`f_S = 1.66345592659651e-36` to the result, i.e. adds a number to a quantity
whose units are already wrong.

**`Gw150914 Entropy Test.py`** — Bekenstein-Hawking entropy misassembled:

```python
S = (4 * pi * G * A) / (hbar * c * kB)
```

Correct: `S = k_B c³ A / (4Għ)`. G is in the wrong position and k_B is inverted.
For the 62 M☉ remnant:

| | Value |
|---|---|
| Standard | 5.567 × 10⁵⁷ J/K |
| As coded | 8.096 × 10⁵⁰ |
| Ratio | **1.45 × 10⁻⁷** |

Seven orders of magnitude low. This is the script that computes GW150914 entropy —
the same event underpinning the κ = 1366 claim.

## Correction to Phase 3

I reported that `kappa_named.txt` was empty and inferred κ is "only ever a
lowercase local variable — never a named module constant." **The inference was
wrong.** The `KAPPA_` pattern required a trailing underscore and missed suffix
forms. Case-sensitive re-sweep finds:

| Identifier | Value | Files |
|---|---|---:|
| `KAPPA` | 1366 | 2 |
| `BRUNO_CONSTANT_KAPPA` | 1340e-6 | 1 |

Small in count, but they are the only module-level κ bindings in the corpus, and
one of them is a **fourth** distinct value.

## Refinement — line endings inflate the unique-file count

| Basis | Unique contents |
|---|---:|
| Exact bytes | 614 |
| Ignoring CR/LF | **572** |

42 files are CRLF/LF twins of another file — mechanically distinct, editorially
identical. The true unique-content figure is **572**, not 613. Deduplication
should normalize line endings first or it will preserve 42 needless copies.
