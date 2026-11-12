---
type: specification
id: SPEC-SEQUENCING-v3.0
title: "Precap Sequencing Modular Specification — Section 05 & Dispersal Sub-Specification Root"
description: "Canonical PrecapWeek specification governing Section 05 Sequencing Orientation, Gaussian coupling rules, compiler JSON bindings, and delegation to 02-weekly-dispersal subspecs under DD-15."
status: current
date: 2026-11-12
parent_spec: SPEC-PRECAP-WEEK-MASTER.okf.md
scope: [weekly-orchestration, precap-week, sequencing, dispersal, gaussian, section-05]
tags: [weekly-orchestration, precap-week, sequencing, dispersal, specification, okf-v02]
references: [SPEC-PRECAP-WEEK-MASTER.okf.md, SPEC-MATRIX-1-PORTFOLIOS.okf.md, SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md, SPEC-PRECAP-INTERFACES-HANDOFF.okf.md]
---

# Precap Sequencing Modular Specification — Section 05 & Dispersal Sub-Specification Root

## Section 1 — Sequencing Architecture & `DD-15` Authority Boundary

Sequencing is a distribution system powered by interleaving, spaced repetition, chunking, and testing across personal and portfolio priorities. Under [`SPEC-PRECAP-WEEK-MASTER.okf.md`](SPEC-PRECAP-WEEK-MASTER.okf.md), this specification serves as the **canonical PrecapWeek root for Sequencing (`Section 05`)**, bridging weekly portfolio planning to the mathematical dispersal suite under [`02-weekly-dispersal/`](../02-weekly-dispersal/index.md).

### Dual-Repository Authority Model (`DD-15`)

- **Engine Canonical Source (`MasterOfArts`)**: Dispersal contracts, entity schemas, solver algorithms, and [`allocate_week.py`](../02-weekly-dispersal/allocate_week.py) originate in `MasterOfArts/Sequencing/dispersal/` and mirror one-way into [`02-weekly-dispersal/`](../02-weekly-dispersal/index.md) via `sync_dispersal.py`.
- **Clock & Precap Presentation (`apexai-os-meta`)**: [`week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json) owns daily time windows (`08:00–24:00` weekday, `12:00–16:00` weekend), while this specification owns Section `05` PrecapWeek rendering and cross-module integration without duplicating solver formulas.

---

## Section 2 — Delegated Sequencing Sub-Specifications (`02-weekly-dispersal/`)

| Sub-Specification / Artifact | Concern Owned | Upstream Research Origin |
|---|---|---|
| [`SPEC-WEEKLY-DISPERSAL.okf.md`](../02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md) | `3x3` Flow contract (`120m`), regimes, `slot_id` taxonomy, guards (`WD-01`..`WD-48`) | `MasterOfArts/Sequencing/dispersal/` |
| [`ALGORITHM.md`](../02-weekly-dispersal/ALGORITHM.md) | Objective function, `XP/TP/BP` scoring (`DD-01`, `DD-16`), rounding, Gaussian weighting | `MasterOfArts/Sequencing/dispersal/` |
| [`EPICS-SCHEMA.md`](../02-weekly-dispersal/EPICS-SCHEMA.md) | Six-table entity schema (`EPIC`, `BLOCK`, `CHUNK`, `NODE_PLACEMENT`, `SET_MEMBER`, `EDGE`) | `MasterOfArts/Sequencing/dispersal/` (`epics.json`) |
| [`02-weekly-dispersal/index.md`](../02-weekly-dispersal/index.md) | Bundle map linking [`week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json), [`week-demand.json`](../02-weekly-dispersal/week-demand.json), [`slot-inventory.json`](../02-weekly-dispersal/slot-inventory.json), [`week-allocation.json`](../02-weekly-dispersal/week-allocation.json) | `MasterOfArts/Sequencing/` corpus (`sources/`, `research/`) |

---

## Section 3 — Section 05 Presentation & Orientation Rules (`M04 / Q13 / SEQ-D1..D4`)

### Four-Branch Epic Allocation Summary (`240` Slot Occurrences)

All temporal slot counts reconcile to [`SPEC-PRECAP-WEEK-MASTER.okf.md §3.1`](SPEC-PRECAP-WEEK-MASTER.okf.md#section-31--section-00-portfolio-compass--canonical-capacity-arithmetic-t1). For weekly Section `05` display, `allocate_week.py` binds all 240 slot occurrences across four branches:

| Epic Branch | Slot Quota | In-Flow Duration | Allocated Focus Modalities / Portfolio Epics |
|---|:---:|:---:|---|
| **Mental (`M`)** | 72 slots | 216 min | Morning Intention (`focus_days`), ACIM presence, Surrender transitions, Breathing. |
| **Physical (`P`)** | 72 slots | 144 min | Martial Arts, Dance, S/BJJ, General micro-mobility, Knee therapy (pinned `*_*_I3_P`). |
| **Regeneration (`R`)** | 24 breaks | 288 min | Audiobooks, Yoga Nidra, Socializing. Weighted round-robin rotation, `XP = 0`, `DD-16` zero BP floor. |
| **Craft / Projects (`C`)** | 72 sprints | 2,160 min | 6 Canonical Portfolio Epics (Leela, IPOS, Master of Arts, Apex AI, Mindful Bar, Residual). |

*Note*: Evening Physical Courses (e.g. `18:30–19:30` Dance/Kicks/Moves) occur outside the `72 × 2m` in-Flow `P` quota.

### Gaussian Focus Coupling & Sequence Arcs

- **Temporal Weighting (`SEQ-D1`)**: Cognitive focus weight follows a Gaussian coupling curve centered on `19:00` with standard deviation $\sigma = 6.0\text{h}$ and maximum weight $w_{\max} = 1.5\times$. Bleed across the Friday-to-Saturday boundary is strictly prohibited.
- **Sequence vs. Flow Cardinality (`SEQ-D3`)**: Sequences and Flows have an $N:M$ relationship. Mixed-project Craft sprints (`C1–C3`) within a single Flow block are authorized when aligned with critical-path sequence arcs.
- **Projected Yields (`Q13 / Option A`)**: Section `05` surfaces projected `TP`, `XP`, and `BP` (`50/25/25` balance components) without minting `XP` on `R` breaks (`WD-03`) or displaying realized ledger scores (`WD-07`).

---

## Section 4 — Compiler & Runtime Bindings

1. **HTML Cockpit (`#s05`) & OKF Brief (`§05`)**: [`render_precap_cockpit.py`](render_precap_cockpit.py) hydrates Section `05` dynamically from [`week-demand.json`](../02-weekly-dispersal/week-demand.json), [`slot-inventory.json`](../02-weekly-dispersal/slot-inventory.json), and [`week-allocation.json`](../02-weekly-dispersal/week-allocation.json) without hardcoding solver weights.
2. **Blueprint Independence (`render_blueprint.py`)**: Standalone clock grids live in [`02-weekly-dispersal/week-blueprint.html`](../02-weekly-dispersal/week-blueprint.html) for dispersal audits while PrecapWeek renders end-to-end portfolio orientation in `#s05`.

---

## Section 5 — Operative Failure-Mode Guards & Circuit Breakers

In accordance with `WP-25`, this specification closes with operative terminal failure-mode guards:
1. **Regeneration Purity Guard (`WD-03 / DD-16`)**: Regeneration slots must mint zero Experience Points (`XP = 0`). Any non-zero `XP` calculation fails allocation validation.
2. **Boundary Isolation Guard (`DD-15`)**: Dispersal solver logic, entity tables, and formulas stay isolated inside `02-weekly-dispersal/` (mirrored from `MasterOfArts/Sequencing/dispersal/`); PrecapWeek consumes JSON interfaces without duplicating solver formulas.
3. **Gaussian Bleed Guard (`SEQ-D1`)**: Evening focus coupling must respect the Friday-to-Saturday wall; cross-weekend spillover invalidates allocation alignment.
4. **Projected-Only Display Guard (`WD-07`)**: PrecapWeek Section `05` renders strictly projected `TP/XP/BP`; realized `FlowRecap` reconciliation remains isolated to opening Stage `00` StatusMerge and Stage `4/5`.
