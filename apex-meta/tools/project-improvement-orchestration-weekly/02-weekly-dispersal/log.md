<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal — Closed Decisions & Change Log

Historical record of closed decisions, settled assumptions, resolved conflicts, and past migrations moved out of [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md) (`FA-01`, `FA-11`).

---

## 1. Closed & Reassigned Decisions (`DD-*` / `OD-*`)

| ID | Topic | Final Resolution & Current Single Owner |
|---|---|---|
| **DD-01** | BP authority | Algorithm-owned `50 / 25 / 25` model (`branch_diversity`, `work_break_alternation`, `focus_day_alternation`). Owned by [ALGORITHM.md](ALGORITHM.md). |
| **DD-02** | `WeekDemand` share format | Slot-occurrence quotas per week. Draft created in [week-demand.json](week-demand.json) (absorbs `OD-03`). |
| **DD-03** | Focus-day specifications | **Solved.** Defined via Mon–Wed Project Night (`20:30–22:00`), Mon–Fri evening physical courses (`18:30–19:30`), and Mental focus days in [week-demand.json](week-demand.json). |
| **DD-04** | `Knee` Epic branch | **Solved.** Branch `P` Physical (training, not recovery). Owned by the Epic database ([SPEC-WEEKLY-DISPERSAL.okf.md](SPEC-WEEKLY-DISPERSAL.okf.md) §8 `WD-40`). |
| **DD-05** | Sunday focus & scope | **Solved.** ACIM on Sunday (`week-demand.json`); `Sun OFF` retired everywhere (`week-blueprint.json`). |
| **DD-06..DD-15** | Architecture & sync baseline | Mon–Sun span applied; stateless within-week solver; OpenProject owns `C` work packages; `week-blueprint.json` in `apexai-os-meta` owns calendar clock; `MasterOfArts` owns Sequencing & generated `slot-inventory.json`. |
| **DD-16** | Numeric BP floor | **Ruled:** No numeric BP floor cutoff (`ALGORITHM.md`). |
| **DD-17** | `R` Epic ownership | **Solved:** One `Regeneration` Epic with Blocks (`Yoga Nidra`, `Audiobooks`, `Socializing`) in [week-demand.json](week-demand.json). |
| **DD-18** | Weekend regime | **Solved:** `2 × 120m` Flows Sat–Sun (`12:00–16:00`), same `3x3` algorithm (`week-blueprint.json`). |
| **DD-19..DD-31** | XP/TP/BP & Flow reconciliation | `XP = leverage × TP`; `36m` sprint (`30m` Craft + `1m` recap owned by Craft); practice binds inside Flows; `35/25/10/15/15` Physical & `40/20/20/20` Mental on `5%` ladder; `EFX` dropped; `DD-23/24/26/28` closed across `SPEC-PRECAP-WEEK-ITERATIONS.okf.md` and `HANDOVER-03..06`. |
| **DD-32..DD-40** | Clock geometry & evening `P` decoupling | Screenshot Col-1 clock locked in `week-blueprint.json` (`08:00–24:00`, `960m`, Thu/Fri `Freizeit 20:30–22:00`, `Day Outro 22:00–22:30`); `18:30–19:30` evening physical courses excluded from `72 × 2m` `P` quota and coupled via Gaussian weighting (`ALGORITHM.md`). |
| **SEQ-D1..SEQ-D4** | `T2` Solver & Section `05` closure | `σ = 6.0h` (`360m`), `19:00` midpoint, `w_max = 1.5x`, no Fri→Sat bleed (`SEQ-D1`); `DD-16` confirmed with weighted round-robin `R` Block rotation (`XP = 0`, `SEQ-D2`); multi-Flow Sequences & multi-project `C` sprints ratified (`SEQ-D3`); Section `05` Option A (`Q13` Sequence-Arc View + Dispersal Dial & `XP/TP/BP` Breakdown) locked (`SEQ-D4`). |
| **OD-01..OD-44** | Legacy raw chat utterances | Superseded as raw list: `OD-02` rewritten in [SPEC-WEEKLY-DISPERSAL.okf.md](SPEC-WEEKLY-DISPERSAL.okf.md); `OD-03` moved to [week-demand.json](week-demand.json); `OD-04` cleared in Precap/blueprint; `OD-05..06` owned by Epic model; `OD-07` moved to [week-demand.json](week-demand.json). |

---

## 2. Settled Assumptions & Resolved Conflicts (`A-*`, `X-*`)

- **A-01 (Flow composition):** Moved into [SPEC-WEEKLY-DISPERSAL.okf.md](SPEC-WEEKLY-DISPERSAL.okf.md) §2 (`3 × (P 2m + M 3m + C 30m + recap 1m) + R 12m = 120m`).
- **A-02..A-14:** Branches confirmed across all four branches (`P`, `M`, `C`, `R`); anchors outside quota; week starts Monday; physical uses share quotas + Gaussian evening coupling; `Sun OFF` retired.
- **X-01..X-06:** Glossary `50/25/25` BP wins over duplicate Algorithm draft; Sunday ACIM active; Monday–Sunday applied across PrecapWeek; `R` reachable via BP rather than minting XP.

---

## 3. Change History

- **2026-11-11 (`T2` Allocator, `epics.json`, 6-Portfolio Standard & `SEQ-D1..D4` Closure):**
  - Created [EPICS-SCHEMA.md](EPICS-SCHEMA.md) and populated [epics.json](epics.json) across `M`, `P`, `R`, and the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).
  - Fixed [build_slot_inventory.py](build_slot_inventory.py) to read `physical.shares` directly from [week-demand.json](week-demand.json) and accept `--blueprint`.
  - Specified `base_xp`, `priority_factor`, `quality_multiplier`, `R` weighted round-robin rotation (`XP = 0`), and Gaussian parameters (`σ = 6.0h`, `19:00` midpoint, `w_max = 1.5x`) in [ALGORITHM.md](ALGORITHM.md).
  - Built [allocate_week.py](allocate_week.py) generating [week-allocation.json](week-allocation.json) across all `240` slot occurrences (`72 P + 72 M + 72 C + 24 R`).
  - Removed duplicate `§2 Settled Today` table from [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md) and closed `DD-23`, `DD-24`, `DD-26`, `DD-28`.
- **2026-11-10 (T1 + Informatics Cleanup):**
  - Created single canonical clock owner `apex-meta/.../02-weekly-dispersal/week-blueprint.json` (`08:00–24:00` weekday, `12:00–16:00` weekend).
  - Extracted algorithm rules into [ALGORITHM.md](ALGORITHM.md) and operator weekly dials into [week-demand.json](week-demand.json).
  - Wired [build_slot_inventory.py](build_slot_inventory.py) and [render_blueprint.py](render_blueprint.py) to read `week-blueprint.json` and `week-demand.json`.
  - Moved closed `DD-*`/`OD-*`/`A-*`/`X-*` records here from [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md).
- **2026-11-09:**
  - Applied Monday–Sunday amendment (22 edits across 5 files: `SPEC-PRECAP-WEEK-ITERATIONS.okf.md`, `SKILL.md`, `validation-checklist.md`, `weekly-blueprint-standard.md`, `weekly-blueprint-meeting-example.md`).
  - Built initial `SPEC-WEEKLY-DISPERSAL.okf.md`, `build_slot_inventory.py`, and `render_blueprint.py`.
