# Apex AIOS Meta — Orchestration Control Plane

This directory houses the primary orchestration control plane, workflow blueprints, evaluation matrices, and multi-domain simulations.

## Contents
- `simulations/` — Multi-domain simulations:
  - `5-week-progressive-simulation/` — The 5-week progressive orchestration stress-test (`00_SIMULATION_OVERVIEW.md`, `Week-01`–`Week-05` daily runs).
  - `US-IDEA-01-20260711/`, `US-SEQ-01-20260712/` — Prior scenario simulations.
- `mcda-evaluation/` — Multi-Criteria Decision Analysis (MCDA) framework, candidate screening, pilot protocols, and selection handover (`00-MCDA-CHARTER.md` through `09-PRIMARY-ORCHESTRATION-SELECTION-HANDOVER.md`).
- `workflows/` — Standardized execution blueprints:
  - `WEEKLY_ORCHESTRATION_BLUEPRINT.md` — The Monday–Friday operating cadence and milestone gates (`G1`–`G5`).
- `rollups/` — Zero-token automated portfolio snapshots (`portfolio-snapshot.json`, `portfolio-snapshot.md`, `health-receipt.yaml`).
- `registry/` — Live capability registry (`capability-registry.yaml`).
- `docs/` — Architecture showcases and interaction guides (`HERMES_MULTI_REPO_CURRENT_STATE_SHOWCASE.md`).
