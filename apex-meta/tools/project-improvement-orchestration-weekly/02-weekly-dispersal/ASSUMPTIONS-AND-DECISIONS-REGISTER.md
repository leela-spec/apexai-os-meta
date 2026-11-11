---
type: Reference
id: MOA-SEQ-DISPERSAL-REGISTER
title: Weekly dispersal assumptions and decisions register
description: What the operator confirmed, what is inferred, what conflicts, and what still needs a ruling before the weekly dispersal system is authored.
status: current
as_of: 2026-11-10
tags: [sequencing, dispersal, weekly-orchestration, precap-week, epics, rhythm, path, algorithm]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal — Active Register & Ownership Map

This working register tracks **only unresolved questions and unverified gaps** for the dispersal slice. Closed decisions and moved assumptions live in [log.md](log.md).

Orchestration-wide architectural rulings live in [DECISIONS.md](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md). The Personal Epic database spans **all four branches**: Mental (`Intention`, `ACIM`, `Surrender`, `Breathing`), Physical (`Martial Arts`, `Dance`, `S/BJJ`, `General`, `Knee`), Regeneration (`Regeneration`), and Craft/Projects (`MasterOfArts`, `Leela`, `IPOS`, `Apex OS`, `Residuals`).

## 1. Single-Owner Map

| Concern | Canonical Owner | Role |
|---|---|---|
| Weekly calendar clock (`08:00–24:00` weekday, `12:00–16:00` weekend) | `02-weekly-dispersal/week-blueprint.json` | Sole clock authority |
| Weekly operator dials (shares, focus days, evening table) | [week-demand.json](week-demand.json) | Operator weekly demand (`DD-02`, `DD-03`) |
| Dispersal algorithm, XP/TP/BP, BP authority, Gaussian coupling | [ALGORITHM.md](ALGORITHM.md) | Solver scoring and quotas (`DD-01`, `DD-16`) |
| Flow contract (`3x3`), regimes, `slot_id` rules, Epics & guards | [SPEC-WEEKLY-DISPERSAL.okf.md](SPEC-WEEKLY-DISPERSAL.okf.md) | Governed slice contract (`WD-01`..`WD-48`) |
| Generated capacity & operator blueprint view | [slot-inventory.json](slot-inventory.json) & [week-blueprint.html](week-blueprint.html) | Derived outputs from `build_slot_inventory.py` |
| Closed dispersal decisions (`DD-01`..`DD-40`, `OD-*`, `A-*`, `X-*`) | [log.md](log.md) | Historical archive & changelog |

## 2. Settled Today (`DD-01`..`DD-05`, `DD-16`..`DD-18`)

Closed decisions and moved inputs (`OD-01`..`OD-44`, `A-01`..`A-14`, `X-01`..`X-06`, `DD-01`..`DD-40`) are archived in [log.md](log.md).

| # | Ruling Summary | Single Owner |
|---|---|---|
| **DD-01** | BP authority belongs to the algorithm (`branch_diversity(50) + work_break_alternation(25) + focus_day_alternation(25)`). | [ALGORITHM.md](ALGORITHM.md) |
| **DD-02 / OD-03** | Operator weekly demand draft created (`week-demand.json`) for Mental and Physical slot-occurrence quotas. | [week-demand.json](week-demand.json) |
| **DD-03** | **Solved.** Focus days defined via Mon–Wed Project Night, Mon–Fri evening physical table, and Mental focus days. | [week-demand.json](week-demand.json) |
| **DD-04 / DD-05** | **Solved.** `Knee` belongs to branch `P`; Sunday belongs to `ACIM` (`Sun OFF` retired). | [week-demand.json](week-demand.json) |
| **DD-16** | **Ruled:** No numeric BP floor cutoff (`"there's no flow [floor] for the numeric BP"`). Structural Flow closing enforces balance directly. | [ALGORITHM.md](ALGORITHM.md) |
| **DD-17** | **Solved:** One `Regeneration` Epic holds `Yoga Nidra`, `Audiobooks`, and `Socializing` as Blocks. | [week-demand.json](week-demand.json) |
| **DD-18** | **Solved:** Weekend Sat–Sun runs reduced slot count (`2 × 120m` Flows, `12:00–16:00`) under the same `3x3` algorithm. | `week-blueprint.json` |

> **Transparency Note on `DD-16`:** Operator voice input read *"there's no flow for the numeric BP"*, recorded as **no numeric BP floor cutoff** (`"no floor"`). Flag immediately if a different rule was intended.

## 3. Open Cross-Module Decisions (`Precap Integration`)

| # | Open Question | Recommended Next Step |
|---|---|---|
| **DD-23** | "`Path` and `Sequencing` paused" wording in Precap Week v2.0 | Clarify that Leela's full UI feature is paused while the dispersal slice is active. |
| **DD-24** | Legacy `Sunday OFF` prose inside Handovers `04` and `05` | Align both handovers with `week-blueprint.json` (`Sat/Sun 12:00–16:00`). |
| **DD-26** | Cross-project dependency DAG choice (`HANDOVER-06`) | Deferred until live OpenProject edge count runs. |
| **DD-28** | `HANDOVER-05` XP/BP header chip alignment | Align header KPI calculations with [ALGORITHM.md](ALGORITHM.md). |

## 4. Unverified Runtime Gaps & Guard

- **OpenProject & Epic DB:** Live OpenProject work packages have not been queried yet; Chunk-level JSON entries remain unpopulated.
- **Precap Render Test:** First live Precap Week HTML generation under the Mon–Sun `week-blueprint.json` clock has not yet executed.
- **Register Scope Guard:** Keep formulas in [ALGORITHM.md](ALGORITHM.md), weekly dials in [week-demand.json](week-demand.json), and closed decisions in [log.md](log.md).
