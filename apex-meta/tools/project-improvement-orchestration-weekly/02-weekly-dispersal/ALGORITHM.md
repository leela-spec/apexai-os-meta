---
type: Specification
id: MOA-SEQ-ALGORITHM
title: Weekly Dispersal Algorithm & Point Model
description: Single-owner specification for projected XP/TP/BP scoring, BP authority, weekly quota rounding, and evening-to-flow Gaussian coupling.
status: current
tags: [sequencing, dispersal, algorithm, xp, bp, tp, gaussian, quota]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal Algorithm & Point Model

**Sequencing** is a distribution system powered by interleaving, spaced repetition, chunking, and testing. Its goal is valuable dispersion across practicing and pursuing goals, skills, and trainings.

This document owns the solver scoring, point rules, quota math, and Gaussian coupling. Calendar clock ownership lives in `week-blueprint.json`, and weekly operator dials live in [week-demand.json](week-demand.json).

---

## 1. Objective Function & Point Model

The solver assigns personal practice Chunks to `M`, `P`, and `R` slots to maximise weekly **projected XP**.

```text
projected_xp = base_xp(chunk) × priority_factor(epic) × quality_multiplier(spacing, interleaving, chunking, testing)
```

| Quantity | Rule | Source |
|---|---|---|
| **TP (Time Points)** | `1 TP = 1 minute`, read directly from the Flow contract (`P 2m`, `M 3m`, `C 30m`, `R 12m`). | Determinate per slot |
| **XP (Experience Points)** | Goal-progress leverage over TP (`XP = leverage × TP`), using `0.75x–1.50x` priority curve. | Computed per slot |
| **BP (Balance Points)** | `branch_diversity(50) + work_break_alternation(25) + focus_day_alternation(25)`. | Week-level property |

### Branch Sourcing Rules

| Branch | Sources XP | Sources BP | Solver Consequence |
|---|---|---|---|
| `P` Physical | Yes | Yes | Ranked by XP; feeds branch diversity |
| `M` Mental | Yes | Yes | Ranked by XP; feeds branch diversity |
| `C` Craft | Yes | Never (`ST-010`) | Ranked by XP; bound to OpenProject work packages |
| `R` Regeneration | Never (`ST-010`) | Yes | Reached structurally via BP & Flow closing break |

---

## 2. Balance Point (BP) Authority (`DD-01`, `DD-16`)

1. **BP belongs to the Algorithm** using the three `50 / 25 / 25` components above. Never use repository diversity as BP.
2. **Focus-day alternation reads active emphasis days** from [week-demand.json](week-demand.json) (Mon–Wed Project Night, Mon–Fri physical course table, and Mental focus days).
3. **No numeric BP floor (`DD-16`):** The solver enforces structural Flow closing (`C -> recap -> R`) and branch balance directly. It does not apply an arbitrary numeric BP cutoff floor.

---

## 3. Quota Allocation & Rounding

1. Mental (`72` slots) and Physical (`72` in-Flow slots) use identical quota allocation logic.
2. Weekly shares in [week-demand.json](week-demand.json) snap to the `5%` ladder via largest remainder.
3. Whole-week slot quotas divide by largest remainder once per week so per-day counts float cleanly.
4. Rounding ties go to the Epic with the lowest focus-day capacity to compensate Epics penalized by weekend reduction.

---

## 4. Evening-to-Flow Gaussian Coupling

1. Weekday evening physical courses (`18:30–19:30`, `60m`) do **not** share the `72 × 2m` in-Flow `P` slot denominator.
2. Each evening physical session places a smooth normal (Gaussian) weight curve centered on that evening block.
3. Matching physical practice receives peak weight right before (`F3`, `F4`) and after (`F1`, `F2` next day). Weight fades smoothly with temporal distance while preserving weekly percentage quotas and `[I1, I2, I3]` interleaving.

---

## 5. Algorithm Failure Guards

- **ALG-01 [P0 | I95/E95/R05] Enforce `R` Never Mints XP:** Reject any solver variant that assigns synthetic XP to Regeneration (`ST-010`).
- **ALG-02 [P0 | I94/E92/R06] Keep Evening Courses Outside `P` Quota:** Reject any budget model that divides `18:30–19:30` minutes against the `72 × 2m` in-Flow denominator.
- **ALG-03 [P1 | I92/E90/R06] Self-Penalising Clustering:** Never hard-code manual per-slot spreading when `quality_multiplier` already penalises adjacent same-Epic placement.
