---
type: Adapter
id: HO-PW-STATS-02
title: "Handover 02 — Section 00 Portfolio Compass (Stats & Leela Basis Discipline)"
description: "Audits Portfolio Compass v05 rules, exposes the W45 38.5h vs T1 48.0h arithmetic contradiction and HANDOVER-05 self-contradictions, and prepares operator selection of the 5 canonical header cards."
status: current
date: 2026-11-11
tags: [weekly-orchestration, portfolio-compass, stats, handover-05, leela, t1-clock]
---

# 02 · Handover: Section `00 · Portfolio Compass` (Stats & Head KPIs)

## 1. Purpose

Lock the exact **5 top summary cards** of Section `00 · Portfolio Compass` (`precap-week-cockpit` header) so they show truthful, non-duplicated portfolio capacity and state grounded strictly in `week-blueprint.json`, `opCall.js`, Google Calendar, and (when approved) `02-weekly-dispersal/ALGORITHM.md`.

---

## 2. Input & Priority Ledger

| Priority | Source Path | Role & Grounding | Ignore / Exclude |
|---|---|---|---|
| **P1 (Spec)** | `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md:20,89-95,301` | Controls `00` placement, `OPERATOR_TODO` freeze, non-duplication rules (`UX-00`), ISO week title rule (`W46`, not W45). | W45 numeric values (`38.5h`, `7 videos`) as defaults. |
| **P1 (Module Spec)** | `01-weekly-command-brief/HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md:30-67` (`§2.2–§2.4`) | Canonical `v05` demotion of unapproved Leela chips and strict 5-card Compass acceptance gates. | Stale `§1`, `§2.1`, `§3` (`:15,22-28,73-77`) still instructing `L1–L4` & `21:00` verification! |
| **P1 (Live Math)** | `02-weekly-dispersal/week-blueprint.json:30,75-120` & `build_slot_inventory.py:235-248,305-340` | Deterministic `T1` Flow totals (`24` Flows × `120m` = `48.0h` gross; `72 C = 2160m`, `72 P = 144m`, `72 M = 216m`, `24 R = 288m`, plus `72m` trailing `recap_min`). | Legacy `38.5h` / `38h vs 35h` pre-`T1` estimates. |
| **P2 (Dispersal Bridge)** | `02-weekly-dispersal/ALGORITHM.md:19-48` & `ASSUMPTIONS-AND-DECISIONS-REGISTER.md:52` (`DD-28`) | Exact `TP/XP/BP` formulas if operator unlocks Leela-basis KPIs (`XP = leverage × TP`; `BP = 50/25/25` on branches, NEVER mint `XP` for `R`). | Synthetic `composite scores` on Matrix 1 items (`HANDOVER-MATRIX-1:64`). |

---

## 3. Forensic Diff — Latest vs Added (`Nov 9–11`) vs Lost / Contradicted

### Locked State (`v05` in `SPEC:20,89-95` & `HANDOVER-05:30-67` — Operator Verified `2026-11-11`)
- Section `00` starts **open by default** with title `Precap Week · {{ISO_DATE_SPAN}}` (correctly computed ISO week).
- Contains **5 visually uniform summary cards** grounded in `slot-inventory.json`, Calendar intersections, and the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`):
  1. **`Net Craft Capacity`** (`36.0h` pure Craft `C` / `48.0h` gross across `24` Flows, minus verified fixed calendar collisions, with explicit `72m` trailing `recap_min` inside the `12.0h` non-Craft budget)
  2. **`Total Flows`** (`24` nominal `120m` Flows = `20` weekday `Mon–Fri` + `4` weekend `Sat–Sun`)
  3. **`Craft Sprints`** (`72` × `30m C` sprints across the week)
  4. **`Active L1 Outcomes (6 Portfolio Areas)`** (`N` active `L1` outcomes across the **6 Portfolio Areas**: **`Leela`**, **`IPOS`**, **`Master of Arts`**, **`Apex AI`**, **`Mindful Bar`**, and **`Residual`**)
  5. **`Gate / Readiness`** (`G1` status, unblocked vs conflict count, OP/Calendar source status)
- Upgradeable to Leela `XP / TP / BP` (`Option S2`) once `T2` (`allocate_week.py`) emits `week-allocation.json`.
- **Forbidden duplicate panels in `00`:** `Weekly Target`, `Operator Agenda`, and `Primary Data Source`.
- Historical W45 counts MUST be labeled `historical / source-reported` (`HANDOVER-05:66`, `v03.html:19,32`), never disguised as live recomputed truth.

### Demoted vs Broken in `v03.html` & `HANDOVER-05`
1. **Demoted Nov 9 (`8ff2eb89`) -> Nov 10 (`ec3e12f3`):** The 5-chip Leela strap (`TP CAPACITY PLACED`, `COVERAGE TRIPLE`, `XP`, `BP`, `TESTING VS APPLICATION` + `W44` dot) was moved to `Historical Candidate KPI Redraft` (`HANDOVER-05:30-46`).
2. **Severe Arithmetic Contradiction (`v03.html:27` vs `T1` `week-blueprint.json`):**
   - `v03.html` `DATA.metrics` displays **`38.5 h` (*Planned focus*)** right above a Matrix 2 rendering **`24` `T1` Flows**!
   - Under `T1`, `24` Flows × `120m` = **`48.0 h` gross** (`36.0 h` pure Craft `C` + `12.0 h` structured `P/M/R/recap`). Even subtracting Thu `10:00–11:00` Alex & Chris (`1h`), net does not equal `38.5h` (which came from pre-`T1` `Mon–Fri + Sat AM + Sun OFF`).
   - Card #4 in `v03.html:27` (`7 Videos due`) is a single-project MoA deliverable disguised as a portfolio-wide metric.
3. **Internal Contradictions Inside `HANDOVER-05`:**
   - `:15`, `:22-28`, and `:77` still require testing `L1–L4` Leela chips, directly contradicting `:31, 46, 65`.
   - `:39, 41, 51, 52, 56` still reference `21:00 Shutdown`, `6d (Mon-Sat)`, and `2,310 TP`!
   - `:59` fixed `Saturday_or_Sunday` (`A-12`), yet `:75` assumes a non-existent `stats_facts_daily` JSON producer from `StatusMerge`/`FlowRecap`.

---

## 4. Process & Anti-Drift Boundaries

- **Single Computation Path:** Any time/capacity card MUST be deterministically derived from `02-weekly-dispersal/slot-inventory.json` minus verified external calendar blocks (`week-blueprint.json` intersections). Never hardcode `38.5 h`.
- **Recap-Minute Accounting Rule (`build_slot_inventory.py:235-237,308-310`):** Account transparently for the `72 min` (`24 × 3 × 1m` post-Craft recap) difference between summed `slot_occurrences` (`2808 min`) and gross Flow time (`2880 min` = `48.0 h`).
- **Epistemic Separation:** Clearly separate `Planned Capacity` (from `week-blueprint.json` + Calendar), `Active Portfolio Scope` (from OP + Session), and `Realized` (only after `FlowRecap`/`StatusMerge` emits actual logs).

---

## 5. Output & Concrete Examples

### Canonical Targets to Update Upon Decision
1. `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md` (`§4.1`, replacing `OPERATOR_TODO` with the locked 5-card schema).
2. `01-weekly-command-brief/HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md` (purge `L1-L4` contradiction at `:15,22-28,73-77`, purge `21:00`/`6d`/`38.5h`, archive superseded research draft or lock as canonical Stats reference per `CDL-05`).
3. `01-weekly-command-brief/precap-week-cockpit-W45-actual-data-v03.html` `#s00` (`#stats` bound to real `T1` + Calendar numbers).

### Concrete Candidate 5-Card Sets for Operator Selection `[1–100 (I/E/R)]`

| Option | The 5 Compass Cards | `(I/E/R)` | Pros / Cons |
|---|---|---|---|
| **Option S1 (Pure Grounded Capacity & Scope — Recommended V1)** | `1. Net Craft Capacity` (`36.0h` − meetings) · `2. Total Flows` (`24` / `20 wkday + 4 wkend`) · `3. Craft Sprints` (`72` × `30m C`) · `4. Active L1 Outcomes` (`N` across `K` projects) · `5. Gate / Readiness` (`# unblocked / # conflicts`) | **I92 / E95 / R08** | **Zero invented formulas.** Every number comes straight from `slot-inventory.json`, Calendar, and OP today. |
| **Option S2 (Leela `XP/TP/BP` Hybrid — Needs `T2`)** | `1. Craft + Flow TP` (`36.0h C` / `2880m`) · `2. Projected XP` (from `T2` + Matrix 1) · `3. Structural BP` (`50/25/25` branch mix) · `4. L1 Coverage` (`Placed / Selected L1`) · `5. Conflicts / Deferrals` | **I96 / E55 / R28** | Aligns with `ALGORITHM.md` (`DD-28`), **blocked** until `T2` allocator & `Priority_Factor` exist; cannot claim "Realized" until `FlowRecap` JSON logs exist. |
| **Option S3 (Execution Tracking — Needs Daily Bridge)** | Option S1 cards + live `Realized vs Planned` progress bar driven by `StatusMerge` | **I94 / E30 / R40** | Deferred until `stats_facts_daily` exists in Modules `06–07` (`FlowRecap -> StatusMerge`). |

---

## 6. Definition of Done (DoD)

1. Operator confirms Option `S1`, `S2`, or custom 5-card definition (`OPERATOR_TODO` closed in `SPEC-PRECAP-WEEK-ITERATIONS.okf.md`).
2. `HANDOVER-05` internal self-contradictions (`§1, §2.1, §3` vs `§2.2–2.4`) and stale `21:00`/`6d`/`38.5h` strings eliminated via `rg`.
3. Arithmetic reconciles deterministically: `slot-inventory.json` (`24 Flows`, `240 slots`, `2880m` gross / `2808m` occurrences + `72m` recap) minus verified calendar overlaps.
4. Cockpit Section `00` shows zero prohibited panels (`Weekly Target`, `Agenda`, `Primary Data Source`) and clearly marks source state (`ONLINE` / `OFFLINE` / `historical`).

## 7. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/02-HANDOVER-STATS-COMPASS.md and 00-RULE-CANONICAL-DECISION-LOCK.md.
Present Options S1 vs S2 concisely so I can lock the exact 5 Portfolio Compass cards (closing OPERATOR_TODO in SPEC §4.1 and DD-28), fix the W45 38.5h vs T1 48h/36h math mismatch, clean the internal L1-L4 / 21:00 contradictions inside HANDOVER-05, and update the Cockpit Section 00 generator.
```
