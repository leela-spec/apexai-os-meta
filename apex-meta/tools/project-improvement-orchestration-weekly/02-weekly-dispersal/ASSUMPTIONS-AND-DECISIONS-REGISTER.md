---
type: Reference
id: MOA-SEQ-DISPERSAL-REGISTER
title: Weekly dispersal assumptions and decisions register
description: Single-owner map and active runtime verification checklist for the weekly dispersal slice after closing DD-01..DD-40 and SEQ-D1..SEQ-D4.
status: current
as_of: 2026-11-11
tags: [sequencing, dispersal, weekly-orchestration, precap-week, epics, rhythm, path, algorithm]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal — Active Register & Ownership Map

This working register tracks **only the single-owner map and active runtime verification items** for the dispersal slice. All closed decisions (`DD-01`..`DD-40`, `SEQ-D1`..`SEQ-D4`, `OD-*`, `A-*`, `X-*`) live in [log.md](log.md).

Orchestration-wide architectural rulings live in [DECISIONS.md](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md). The Personal Epic database ([epics.json](epics.json)) spans **all four branches** (`WD-40`): Mental (`Intention`, `ACIM`, `Surrender`, `Breathing`), Physical (`Martial Arts`, `Dance`, `S/BJJ`, `General`, `Knee`), Regeneration (`Regeneration` with Blocks `Yoga Nidra`, `Audiobooks`, `Socializing`), and Craft/Projects across the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).

## 1. Single-Owner Map

| Concern | Canonical Owner | Role |
|---|---|---|
| Weekly calendar clock (`08:00–24:00` weekday, `12:00–16:00` weekend) | `02-weekly-dispersal/week-blueprint.json` | Sole clock authority |
| Weekly operator dials (shares, priorities, pins, focus days, evening table) | [week-demand.json](week-demand.json) | Operator weekly demand (`DD-02`, `DD-03`) |
| Entity schema & 4-branch Personal Epic database | [EPICS-SCHEMA.md](EPICS-SCHEMA.md) & [epics.json](epics.json) | 6-table schema (`WD-37..WD-40`) across `M/P/R/C` |
| Dispersal algorithm, XP/TP/BP, BP authority, Gaussian coupling | [ALGORITHM.md](ALGORITHM.md) | Solver scoring and quotas (`DD-01`, `DD-16`, `SEQ-D1..D2`) |
| Flow contract (`3x3`), regimes, `slot_id` rules, Epics & guards | [SPEC-WEEKLY-DISPERSAL.okf.md](SPEC-WEEKLY-DISPERSAL.okf.md) | Governed slice contract (`WD-01`..`WD-48`) |
| Generated capacity, `T2` allocation & operator blueprint view | [slot-inventory.json](slot-inventory.json), [week-allocation.json](week-allocation.json), [week-blueprint.html](week-blueprint.html) | Derived outputs from `build_slot_inventory.py`, `allocate_week.py`, and `render_blueprint.py` |
| Closed dispersal decisions (`DD-01`..`DD-40`, `SEQ-D1`..`SEQ-D4`, `OD-*`, `A-*`, `X-*`) | [log.md](log.md) | Historical archive & changelog |

## 2. Active Runtime Verification Guard

- **Live OpenProject Craft Refresh:** When OpenProject (`http://127.0.0.1:8083`) is online during Sunday/Saturday Precap Week execution, `selected_work_reference[]` from Matrix 1 updates the active `op_ref` bindings in `C` slots; when offline, `[OP-OFFLINE]` fallback preserves the 6-Portfolio baseline in [epics.json](epics.json).
- **Register Scope Guard (`CDL-03`):** Keep formulas in [ALGORITHM.md](ALGORITHM.md), weekly dials in [week-demand.json](week-demand.json), entity tables in [EPICS-SCHEMA.md](EPICS-SCHEMA.md), and closed decisions in [log.md](log.md).
