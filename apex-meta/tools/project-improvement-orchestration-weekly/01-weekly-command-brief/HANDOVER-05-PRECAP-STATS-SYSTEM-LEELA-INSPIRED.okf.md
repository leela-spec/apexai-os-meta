---
type: handover
id: HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED-v1.0
title: Handover — Precap Week & Weekly Orchestration Stats System (Leela Feature Stats Grounded)
description: Research findings and architectural handover adapting Leela Cloud's feature-stats telemetry grammar (basis separation, Target/Placed/Realized coverage, XP/TP/BP portfolio balance, and testing-vs-application share) into Precap Week and weekly orchestration.
status: current
date: 2026-11-11
tags: [weekly-orchestration, stats, leela-inspiration, telemetry, precap-week, em-09]
---

# Handover — Precap Week & Weekly Orchestration Stats System (Leela Grounded)

## 1. Mission & Grounded Inspiration

This specification locks the **5 canonical Portfolio Compass header cards** (`Section 00`) grounded in `02-weekly-dispersal/week-blueprint.json` + `slot-inventory.json` (`T1` `Mon–Sun` clock) and the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`), while preserving the verified Leela telemetry grammar (`Leela-Cloud-2026/docs/design/stats/`, `docs/ssot/features/stats/`) as the `T2` (`XP/TP/BP`) upgrade path.

---

## 2. 4-Dimensional Handover Contract (`EM-09`)

### 2.1 Input & Priority Ledger
- **P1 Authoritative Canonical Clock & Portfolio Sources**:
  - [`week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) & `slot-inventory.json`: `24` nominal `120m` Flows (`Mon–Fri` `08:00–24:00` w/ `Day Outro 22:00–22:30` = `20` Flows; `Sat–Sun` `12:00–16:00` = `4` Flows; `48.0h` / `2,880m` gross = `36.0h` / `2,160m` pure Craft `C` across `72 × 30m` sprints + `12.0h` / `720m` `P/M/R/recap` including `72m` trailing `recap_min`).
  - **6 Canonical Portfolio Areas (`06-PORTFOLIO`)**: **`Leela`**, **`IPOS`**, **`Master of Arts`**, **`Apex AI`**, **`Mindful Bar`**, and **`Residual`**.
- **P2 Leela Stats Reference Sources (For `T2` `XP/TP/BP` Projection Only)**:
  - [`00-MACRO.md`](file:///c:/GitDev/Leela-Cloud-2026/docs/design/stats/00-MACRO.md): Basis separation (`● realized · ○ planned · ◇ forecast`).
  - [`spec.md`](file:///c:/GitDev/Leela-Cloud-2026/docs/ssot/features/stats/spec.md): `TP/XP/BP` construct orthogonality (`F5-B01`..`F5-B23`).
- **Deliberately Excluded**: Legacy pre-`T1` `38.5h` (`2,310m`), `21:00` shutdown, and `6d (Mon-Sat)` assumptions; unverified `stats_facts_daily` claims before `FlowRecap`/`StatusMerge` emit JSON logs; duplicate `Weekly Target`, `Operator Agenda`, or `Primary Data Source` panels inside Section `00`.

### 2.2 Locked 5-Card Portfolio Compass Standard (`Option S1` + `6-Portfolio` Roster)
Section `00 · Portfolio Compass` starts open by default and renders **5 visually uniform summary cards**:
1. **`Net Craft Capacity (T1)`**: `36.0h C` (`2,160m` across `72 × 30m` sprints; `48.0h` / `2,880m` gross across `24` Flows with `72m` trailing `recap_min` inside the `12.0h` non-Craft budget) minus verified fixed calendar meeting collisions.
2. **`Total Weekly Flows`**: `24 Flows` (`20` weekday `Mon–Fri` + `4` weekend `Sat–Sun`, `120m` each).
3. **`3×3 Craft Sprints`**: `72 Sprints` (`3 × 30m C` per Flow; `full / compressed / minimal / omitted` deformation tracked explicitly).
4. **`6 Portfolio Areas & Active L1 Scope`**: **`6` Portfolio Areas** (`Leela` · `IPOS` · `Master of Arts` · `Apex AI` · `Mindful Bar` · `Residual`) with active `L1` priority outcome count.
5. **`Gate & Source Readiness`**: `G1` approval status, verified override count, and live OpenProject / Google Calendar provenance state (`ONLINE` vs `[OP-OFFLINE]` / `historical`).

### 2.3 Optional `T2` Leela `XP / TP / BP` Upgrade (`Section 05` / `Option S2`)

When `02-weekly-dispersal/allocate_week.py` (`T2`) runs and produces `week-allocation.json`, projected `TP` (`2,808m` occurrences + `72m` recap = `2,880m`), `XP` (`leverage × TP`, with `R` strictly `XP = 0` per `DD-16`), and structural `BP` (`50/25/25` branch mix, no numeric BP floor) are surfaced in Section `05 · Sequencing` (and may upgrade Compass cards when requested).

#### Downstream Orchestration Integration (`StatusMerge` / `FlowRecap`)
- At `StatusMerge` (`Saturday_or_Sunday` per `week-blueprint.json`), planned capacity (`○ Placed`) compares against realized execution (`● Realized`) once `FlowRecap` logs are present:
  - Exposes **`forecast_gap`** and capped **`execution_rate <= 1.0`** (`overfulfilment_minutes` tracked separately).
  - Surfaces **`zero-denominator`** ("paused / no target") honestly for intentionally paused streams rather than `0%` failure alerts.

### 2.4 Current Cockpit Acceptance (`DoD`)
1. `00 Portfolio Compass` starts open with the 5 locked, source-grounded `T1` + `6-Portfolio` cards (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).
2. Every capacity figure reconciles deterministically with `02-weekly-dispersal/week-blueprint.json` and `slot-inventory.json` (`48.0h` gross / `36.0h` Craft `C` + `12.0h` `P/M/R/recap`).
3. Historical W45 counts are flagged `historical / source-reported`; they are never re-labelled live, independently verified, or current.
4. No `Weekly Target`, `Operator Agenda`, or `Primary Data Source` duplication is added to Section `00`.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: Inspected `week-blueprint.json`, `slot-inventory.json`, and `Leela-Cloud-2026/docs/design/stats/`. Reconciled the pre-`T1` `38.5h` / `5-project` W45 draft against the canonical `T1` `Mon–Sun` (`24` Flows = `48.0h` gross / `36.0h` Craft) clock and the **6-Portfolio standard** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).
2. **Logic Chain**: Grounding the 5 Compass cards directly in `slot-inventory.json`, Calendar collisions, and the 6 Portfolio Areas eliminates unverified prose numbers while keeping `XP/TP/BP` cleanly connected to `T2` (`allocate_week.py`).
3. **Caveats**: Until `StatusMerge` / `FlowRecap` emit machine-verified actual logs for a closing week, Section `00` displays planned (`○`) or historical-snapshot (`historical / source-reported`) basis labels only.
4. **Conclusion**: Locked and aligned to `v05`, `T1`, and `06-PORTFOLIO`.
5. **Verification Method**: Inspect `#s00` in the Cockpit HTML confirming the 5 locked cards, `48.0h` gross / `36.0h` Craft `T1` math, and all 6 Portfolio Areas (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).
