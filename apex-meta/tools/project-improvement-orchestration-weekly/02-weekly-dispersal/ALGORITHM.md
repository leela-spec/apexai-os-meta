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

### Sub-Formula Specifications (`T2` Solver Parameters)

1. **`base_xp(chunk)`:**
   - For `P`, `M`, and `C` slots: `base_xp(chunk) = 1.0 × duration_min` (`P = 2.0`, `M = 3.0`, `C = 30.0`).
   - For `R` slots: `base_xp(chunk) = 0.0` (`ST-010`, `ALG-01`).
2. **`priority_factor(epic)`:**
   - Reads integer `priority` (`1..10`) from [`epics.json`](epics.json) / [`week-demand.json`](week-demand.json):
     ```text
     priority_factor(epic) = 0.75 + (priority - 1) × (0.75 / 9)
     ```
     mapping `priority = 1 -> 0.75x` through `priority = 10 -> 1.50x`.
3. **`quality_multiplier(spacing, interleaving, chunking, testing)`:**
   - Combines temporal spacing gap, within-Flow iteration interleaving (`I1..I3`), Mental focus-day bonus (`+0.15`), and Physical evening Gaussian coupling (`w(Δt)`):
     ```text
     quality_multiplier = spacing_factor × interleaving_factor × focus_or_gaussian_factor
     ```
   - `spacing_factor = 1.0 + 0.20 × min(1.0, hours_since_last_same_epic / 12.0)` (rewards spacing across Flows; penalises back-to-back placement).
   - `interleaving_factor = 1.05` when adjacent iterations (`I1 -> I2 -> I3`) inside the same Flow switch sub-blocks/drills (`SET_MEMBER` rotation), `0.85` on consecutive same-Epic repetition inside one Flow.
4. **Regeneration (`R`) Block Selection (`SEQ-D2`, `DD-16`, `DD-17`):**
   - Because `R` never mints `XP` (`base_xp = 0`) and `DD-16` forbids a numeric BP cutoff floor, the `24` in-Flow `R` breaks (`12m`) rotate across the three `Regeneration` Blocks (`Yoga Nidra`, `Audiobooks`, `Socializing`) via deterministic **weighted round-robin** (`block_weights` in [`week-demand.json`](week-demand.json): `Audiobooks 45%`, `Yoga Nidra 35%`, `Socializing 20%`) with time-of-day affinity (`F2/F4 -> Yoga Nidra / Socializing`, `F1/F3 -> Audiobooks`).

---

## 2. Balance Point (BP) Authority (`DD-01`, `DD-16`)

1. **BP belongs to the Algorithm** using the three `50 / 25 / 25` components above. Never use repository diversity as BP.
2. **Focus-day alternation reads active emphasis days** from [week-demand.json](week-demand.json) (Mon–Wed Project Night, Mon–Fri physical course table, and Mental focus days).
3. **No numeric BP floor (`DD-16`):** The solver enforces structural Flow closing (`C -> recap -> R`) and branch balance directly. It does not apply an arbitrary numeric BP cutoff floor.

---

## 3. Quota Allocation & Rounding

1. Mental (`72` slots) and Physical (`72` in-Flow slots) use identical quota allocation logic.
2. Weekly shares in [week-demand.json](week-demand.json) snap to the `5%` ladder via largest remainder (`WD-32a`: ties on the `5%` ladder go to the Epic covering more week-table activities, then alphabetical).
3. Whole-week slot quotas divide by largest remainder once per week so per-day counts float cleanly.
4. Rounding ties go to the Epic with the lowest focus-day capacity to compensate Epics penalized by weekend reduction (`WD-30`).

---

## 4. Evening-to-Flow Gaussian Coupling (`SEQ-D1`)

1. Weekday evening physical courses (`18:30–19:30`, `60m`) do **not** share the `72 × 2m` in-Flow `P` slot denominator (`DD-39`, `DD-40`).
2. Each weekday evening physical course (`d ∈ Mon..Fri`) places a smooth Gaussian weight curve centered at the **midpoint `t_center = 19:00` (`1140 min`)** with standard deviation **`σ = 6.0 hours` (`360 min`)** and peak multiplier **`w_max = 1.5x`**:
   ```text
   w(Δt) = 1.0 + 0.5 × exp(-(Δt)² / (2 × σ²))
   ```
3. **Active Coupling Window (No Fri→Sat Cross-Course Bleed):** A course on weekday `d` couples to same-day Flows (`F1..F4` on day `d`, peaking at `F3/F4`) and next-morning Flows (`F1/F2` on day `d+1` for `Mon..Thu -> Tue..Fri`), without bleeding across the Friday evening boundary into Saturday's `12:00` weekend regime.

---

## 5. Algorithm Failure Guards

- **ALG-01 [P0 | I95/E95/R05] Enforce `R` Never Mints XP:** Reject any solver variant that assigns synthetic XP to Regeneration (`ST-010`).
- **ALG-02 [P0 | I94/E92/R06] Keep Evening Courses Outside `P` Quota:** Reject any budget model that divides `18:30–19:30` minutes against the `72 × 2m` in-Flow denominator.
- **ALG-03 [P1 | I92/E90/R06] Self-Penalising Clustering:** Never hard-code manual per-slot spreading when `quality_multiplier` already penalises adjacent same-Epic placement.
