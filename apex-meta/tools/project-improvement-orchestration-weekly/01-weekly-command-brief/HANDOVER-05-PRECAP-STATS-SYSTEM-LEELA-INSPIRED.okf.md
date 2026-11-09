---
type: handover
id: HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED-v1.0
title: Handover — Precap Week & Weekly Orchestration Stats System (Leela Feature Stats Grounded)
description: Research findings and architectural handover adapting Leela Cloud's feature-stats telemetry grammar (basis separation, Target/Placed/Realized coverage, XP/TP/BP portfolio balance, and testing-vs-application share) into Precap Week and weekly orchestration.
status: ready_for_operator_verification
date: 2026-11-09
tags: [weekly-orchestration, stats, leela-inspiration, telemetry, precap-week, em-09]
---

# Handover — Precap Week & Weekly Orchestration Stats System (Leela Grounded)

## 1. Mission & Grounded Inspiration

Per the operator's `2do` directive to research high-signal statistics for **Precap Week** and **weekly orchestration** inspired by Leela's feature stats, this handover distills the verified metric architecture inside `Leela-Cloud-2026` (`docs/design/stats/`, `docs/ssot/features/stats/`, `lib/features/stats/`) into a rigorous, non-gamified portfolio KPI system for Precap Week.

---

## 2. 4-Dimensional Handover Contract (`EM-09`)

### 2.1 Input & Priority Ledger
- **P1 Authoritative Leela Stats Sources (Inspected Live)**:
  - [`00-MACRO.md`](file:///c:/GitDev/Leela-Cloud-2026/docs/design/stats/00-MACRO.md): The eleven stat-chip laws (`L1–L11`), non-color basis marks (`● realized · ○ planned · ◇ forecast`), and cross-feature consumer routing.
  - [`10-STATS-FEATURE.md`](file:///c:/GitDev/Leela-Cloud-2026/docs/design/stats/10-STATS-FEATURE.md): Six canonical UX surfaces (`S1 Today`, `S2 Week dashboard`, `S3 Drill-down cascade`, `S4 Flow & Session efficacy`, `S5 Evidence & data quality`).
  - [`spec.md`](file:///c:/GitDev/Leela-Cloud-2026/docs/ssot/features/stats/spec.md): Rules `F5-B01` through `F5-B23` (TP/XP/BP construct separation, `F5-B13` Target/Placed/Realized coverage, `F5-B17` capped adherence vs over-delivery, `F5-B20` testing vs application split).
  - [`stats-system.md`](file:///c:/GitDev/Leela-Cloud-2026/docs/design/stats-system.md): Embedded evidence vs destination analysis thesis.
  - [`stats_cube_symbol.dart`](file:///c:/GitDev/Leela-Cloud-2026/lib/features/stats/stats_cube_symbol.dart): Visual cube/envelope symbol taxonomy (`Chunk`, `Sequence`, `Epic`, `Branch`).
- **Deliberately Excluded**: Legacy streak badges and completion-driven level-up (`SD-004` drift refused per `00-MACRO.md` §8 and baseline `ST-033`); arbitrary invented vanity metrics lacking verifiable denominators.

### 2.2 Process & Comparative Stat Selection
- **Framework Used**: Construct Separation + Coverage Accounting (`Target` vs `Placed` vs `Realized`).
- **Four Leela Laws Enforced in Precap Week**:
  1. **Non-Blending Basis Marks (`L2`, `F5-B16`)**: Header chips never conflate what is planned (`○`) with last week's actuals (`●`) or probability forecast (`◇`). Every metric wears its explicit symbol and basis marker.
  2. **Coverage Triple (`F5-B13`)**: Replaces naive "72 sprints" with an honest capacity check:
     - **Target**: Goals/Tasks declared in Matrix 1 `L1 Priority Goals`.
     - **Placed**: Hours/Flows physically protected inside Matrix 2 around Google Calendar anchors.
     - **Realized (Trailing Benchmark)**: Previous week's execution rate (`min(1.0, realized/planned)` per `F5-B17`) to reality-check ambitious capacity assumptions!
  3. **XP · TP · BP Portfolio Health (`F5-B01`, `00-MACRO.md` §4)**:
     - **TP (Time Capacity)**: Exact planned focus minutes/hours across F1–F4 (`○ 38.5h / 2310 TP`).
     - **XP (Leverage / Priority Concentration)**: Count/share of placed minutes advancing Matrix 1 `L1 Priority Goals` vs nice-to-haves/maintenance.
     - **BP (Weekly Balance Index, 0–100)**: Adapted 3-part balance across `(a) Build/Create/System/Life-Regen repo diversity (50%)`, `(b) Shutdown 21:00 & Lunch Anchor preservation (25%)`, and `(c) Special-Day Mon/Wed alternation (25%)`.
  4. **Testing vs Application Split (`F5-B20`)**: Exposes cognitive load balance between greenfield R&D/recheck (`Testing`: e.g. IPOS Pipeline Recheck, Apex OpenMouse HID) and reliable production throughput (`Application`: e.g. MoA 7 Videos, PDF Invoicing).

### 2.3 Output Specification & Precap Header KPI Redraft

#### Recommended Precap Week Header Telemetry Strap (5 Leela-Aligned Stat Chips)
Instead of ungrounded counts (`24 Flows`, `72 Sprints`), render five `LeelaStatChip`-style cards with hover breakdown drawers:

```text
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| ○ TP · CAPACITY PLACED        | 🎯 COVERAGE TRIPLE             | ⚡ XP · PRIORITY FOCUS RATIO   | ⚖ BP · WEEK BALANCE INDEX      | ⚗ TESTING VS APPLICATION       |
| ○ 38.5h (2,310 min)           | 9 / 9 Goals Placed            | 74% on L1 Goals               | 84 / 100                      | 28% Test · 72% Apply          |
| Across 24 Flows · 6d (Mon-Sat)| Target 9 · Placed 9 · Lag 0%  | Mon-Sat Focus Allocation      | Diversity+Rest+Mon/Wed Themes | IPOS/Apex vs MoA Execution    |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
```

*Optional Trailing Baseline Pill (on `●` button/tooltip)*: `● W44 Realized Rate: 0.78 (on track) · 5/6 shutdowns @ 21:00`.

#### Downstream Orchestration Integration (`StatusMerge` / `FlowRecap`)
- At Saturday `StatusMerge`, each metric flips cleanly from **`○ Placed`** to **`● Realized`** without changing chip position:
  - Exposes **`forecast_gap`** and capped **`execution_rate <= 1.0`** (`overfulfilment_minutes` tracked separately so heroic Monday surges never disguise skipped Fridays).
  - Surfaces **`zero-denominator`** ("paused / no target") honestly for intentionally paused streams like *Leela Path/Sequencing*, rather than showing `0%` red failure alerts!

### 2.4 Definition of Done (`DoD`)
1. Precap Week header stat cards enforce basis marks (`○` planned, `●` trailing realized, `◇` forecast), never blending them.
2. Intentionally paused workstreams (e.g. `Leela Path/Sequencing`) display `Paused (no denominator)` rather than `0%`.
3. `Target vs Placed` exposes any unplaced L1 Priority Goal immediately before execution begins Monday morning.
4. Balance Index (`BP`) visibly validates evening rest (`21:00` shutdown integrity) and Mon/Wed Special Project alternation alongside code/creative work.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: Inspected `Leela-Cloud-2026/docs/design/stats/{00-MACRO.md,10-STATS-FEATURE.md}`, `docs/ssot/features/stats/spec.md`, and `lib/features/stats/stats_cube_symbol.dart`. Leela solved exact anti-vanity stat challenges via `L1–L11`, `XP/TP/BP` construct orthogonality, and `Target/Placed/Realized` accounting.
2. **Logic Chain**: Precap Week asks *"Is my planned week realistic, focused on top goals, and sustainable across creative + technical + rest domains?"* Leela's metrics directly answer capacity (`○ TP`), priority concentration (`XP`), completeness (`Target vs Placed`), burnout guard (`BP`), and cognitive risk (`Testing vs Application`).
3. **Caveats**: Until `StatusMerge` / `FlowRecap` emit machine-verified trailing `stats_facts_daily` JSON logs for prior weeks, the `●` trailing actual badge displays provisional manual/OP estimates flagged as `provisional` per `L9`.
4. **Conclusion**: Ready for operator selection of which 4–5 header chips become the frozen Precap standard.
5. **Verification Method**: Inspect generated HTML stat strip against `L1–L4` rules (explicit basis glyphs, no `0%` on paused modules, capped adherence formulas in spec).
