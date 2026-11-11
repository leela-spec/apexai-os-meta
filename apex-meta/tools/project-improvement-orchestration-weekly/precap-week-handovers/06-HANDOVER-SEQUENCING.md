---
type: Adapter
id: HO-PW-SEQ-06
title: "Handover 06 — Section 05 Sequencing & Dispersal Engine (epics.json, T2 allocate_week.py, T4, Q13)"
description: "Consolidates MasterOfArts/Sequencing/dispersal/ and 02-weekly-dispersal/ state, verifies operator request #2 feedback preservation, exposes dropped entity schemas and undefined T2 parameters, and defines Section 05 UI closure."
status: current
date: 2026-11-11
tags: [weekly-orchestration, sequencing, dispersal, t2-allocator, epics-json, algorithm]
---

# 06 · Handover: Section `05 · Sequencing` & Dispersal Engine

## 1. Purpose

Bridge the finished `T1` Slot Inventory (`week-blueprint.json` + `build_slot_inventory.py`) to the actual working product: **`epics.json`** across all 4 branches (`M/P/R/C`), **`T2` `allocate_week.py`** (Gaussian + XP/TP/BP solver), **`T4`** Matrix 2 `P/M/R` rendering, register cleanup, and Section `05` UI closure (`Q13` / `SEQ-SKILL-01`).

> **Dual-Repo Authority Rule (`DD-15`):** Edit Sequencing specs/code in **`C:\GitDev\MasterOfArts\Sequencing\dispersal\`** and run `sync_dispersal.py` to mirror into `apexai-os-meta/.../02-weekly-dispersal/`. Edit **`week-blueprint.json`** strictly in `apexai-os-meta` (`sync_dispersal.py` preserves it).

---

## 2. Input & Priority Ledger

| Priority | Source Path | Role & Grounding | Ignore / Exclude |
|---|---|---|---|
| **P1 (Canonical Spec)** | `MasterOfArts/Sequencing/dispersal/SPEC-WEEKLY-DISPERSAL.okf.md` (mirror `02-weekly-dispersal/`) | `WD-01..48`, `3×3` Flow composition (`A-01`), 4-branch Epic scope (`WD-40`: Mental, Physical, Regeneration, Craft/Projects), `WD-36a` Matrix 2 `P/M/R` band (no `C`), guards. | `WD-20` (`SPEC:112`) slightly groups distinct anchors vs `week-blueprint.json:143-183`. |
| **P1 (Algorithm)** | `MasterOfArts/Sequencing/dispersal/ALGORITHM.md` | `projected_xp`, `TP=1m`, `XP=leverage×TP`, `BP=50/25/25`, `DD-16` no BP floor cutoff, `5%` largest-remainder rounding, `DD-39/40` evening physical Gaussian coupling. | Missing `base_xp`, `priority_factor(1..10)`, `quality_multiplier`, `σ`, and `R` tie-break specs (restore below!). |
| **P1 (Dials & Code)** | `week-demand.json`, `build_slot_inventory.py`, `render_blueprint.py`, `week-blueprint.json` | Working `T1` generator producing `240` `slot_occurrences` & `slot-inventory.json`. | Dead `week-demand.json:37-43` (`physical.shares` ignored by Python!), hardcoded `WEEK_TABLE_MAP` & Windows paths in Python. |
| **P1 (Registers)** | `ASSUMPTIONS-AND-DECISIONS-REGISTER.md` & `log.md` | Open cross-module items (`DD-23, DD-24, DD-26, DD-28`, `DD-16` voice check) + closed archive. | Duplicate `Settled Today` table (`:29-41`) repeating `OD-03`, `DD-04`, `DD-05` already in `log.md`. |
| **P2 (Entity Schema Source)** | `MasterOfArts/Sequencing/.../10_ENTITY_MODEL.md:13-78` (referenced before deletion from `57b2b77d` register) | Exact 6-table schema (`EPIC, BLOCK, CHUNK, NODE_PLACEMENT, SET_MEMBER, EDGE`) + ID formats (`EP_hex12`, `BL_hex14`, `CH_hex14`) dropped from dispersal bundle! | Must restore into `02-weekly-dispersal/` before authoring `epics.json`. |
| **P2 (Skill & View Drafts)** | `01-weekly-command-brief/research/Q13-THREE-SEQUENCING-VIEW-VARIANTS-20261106.html` & `SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md` | Layout options (Calendar Grid / Day Cards / Sequence Board) & `SEQ-Q1..Q9` (`D016` stateless Skill). | Stale `Mon–Sat / Sun OFF` and variable `1h/2h` Flows (`WD-41` violation). |
| **Historical Snapshot** | `Otheragent_SequencingPart of PrecapWeek.md`, `PRECAP-INTEGRATION-ANALYSIS.md` | Explains how `DD-39/40` and `week-blueprint.json` split evolved. | Obsolete `18:00–19:30 (90m)` / `15:30–16:00` times. |

---

## 3. Forensic Diff — User Request #2 Feedback Check & Gaps Found

### Operator Feedback Preservation Verified (`ec3e12f3`)
- ✅ `DD-06`, `DD-07`, and `A-01` (Flow definition body) cleanly moved out of `ASSUMPTIONS-AND-DECISIONS-REGISTER.md` into `SPEC §2` & `log.md`.
- ✅ **Epics explicitly cover ALL 4 branches** in `SPEC §8 WD-40` (`:184-188`) and `Register:16`: Mental (`Intention, ACIM, Surrender, Breathing`), Physical (`Martial Arts, Dance, S/BJJ, General, Knee`), Regeneration (`Regeneration` w/ `Yoga Nidra, Audiobooks, Socializing` Blocks), and **Craft/Projects** across the **6 Portfolio Areas** (`Leela, IPOS, Master of Arts, Apex AI, Mindful Bar, Residual`).
- ✅ `ALGORITHM.md` extracted formulas & `week-demand.json` extracted weekly operator dials (`OD-03`, `DD-02`, `DD-03`, `DD-05`).

### Accidental Drops, Regressions & Missing Solver Params Found in `ec3e12f3`
1. **Register Cleanup Left Residue (`ASSUMPTIONS-AND-DECISIONS-REGISTER.md:29-41`):** `OD-03`, `DD-04`, and `DD-05` still sit in a redundant `Settled Today` table inside the "unresolved-only" register; `DD-04` link points to `week-demand.json` in Register (`:38`), `SPEC §5` in `log.md:16`, whereas the governing rule is **`SPEC §8 WD-40`** (`:184-188`).
2. **Dropped Entity Schema (`10_ENTITY_MODEL.md`):** Deleting `§1.2` removed the 6-table JSON schema (`EPIC/BLOCK/CHUNK/NODE_PLACEMENT/SET_MEMBER/EDGE`) needed to build `epics.json`.
3. **Undefined Solver Sub-Formulas (`ALGORITHM.md:21-65`):**
   - Gaussian coupling lacks **`σ` width**, **peak amplitude `w_max`**, **distance center (`19:00` vs edge)**, and **Fri `18:30` -> Sat `12:00` / Sun -> Mon wrap-around** rules!
   - `base_xp(chunk)`, `priority_factor(epic)` (and where each Epic's `1..10` priority lives), `quality_multiplier(...)` curve, `focus_day_alternation(25)` reward/enforcement under `DD-16` ("no numeric BP floor"), **`WD-32a` `5%` tie-break rule**, and **`R` Block selection rule (`XP = 0`)** are all unspecified!
4. **Live Python Bugs (`build_slot_inventory.py` & `render_blueprint.py`):**
   - `build_slot_inventory.py:67-71,111-115` re-derives physical shares from `remaining_proportions` + `knee_share`, **silently ignoring `week-demand.json:37-43` (`physical.shares`)**!
   - Hardcodes `PHYSICAL_EPICS`, `WEEK_TABLE_MAP` (`Strikes/Kicks -> Martial Arts`, `Dance/Moves -> Dance`), and absolute Windows path `C:/GitDev/...` instead of reading `week-demand.json` and relative/CLI `--blueprint`.
   - `week-demand.json:60-64` omits the 5 Craft/Project Epics, `pins` (e.g. `WD-33` `*_*_I3_P -> Knee`), and `priority` (`1..10`) per Epic.
5. **`Q13` & Section `05` Conflict (`SEQ-Q1..Q9`):** `SPEC-PRECAP-WEEK-ITERATIONS.okf.md:249-251` keeps Section `05` as `TODO / OPERATOR_DEFINITION_PENDING`, while `Q13` (`Mon–Sat`, variable `1h/2h` Flows) violates `WD-41` (`strict 120m`), and `SEQ-Q1/Q2` (`Sequence vs Flow` `1:1` vs `N:M`, multi-project `C` sprints) remain unresolved alongside `DD-23, DD-24, DD-26, DD-28, N05`.

---

## 4. Process & Anti-Drift Boundaries

- **Single-Owner Write Discipline:** Author specs & allocator code in `MasterOfArts/Sequencing/dispersal/`; sync mirror with `python sync_dispersal.py`.
- **Namespace & Anti-Duplicate Guards (`WD-42..WD-45`):** Never rename `TP/XP/BP`; never assign synthetic `XP` to `R` (`ALG-01`); never divide `18:30–19:30` physical courses against the `72×2m` `P` slot denominator (`ALG-02`); never let `Matrix 2`'s read-only `P/M/R` strip author `C` work (`WD-44`).
- **Narrow Working Slice First (`<product_first>`):** Seed minimal working `epics.json` (`M/P/R/C`) + build `T2` `allocate_week.py` for one real week (`240` slots) before writing generic UI widgets.

---

## 5. Output & Concrete Examples

### Canonical Deliverables Produced by This Chat
1. **`MasterOfArts/Sequencing/dispersal/EPICS-SCHEMA.md`** (or `SPEC §8` expansion) restoring `EPIC / BLOCK / CHUNK / NODE_PLACEMENT` + `epics.json` populated across `M/P/R/C`.
2. **Repaired `build_slot_inventory.py`** reading `physical.shares` + `WEEK_TABLE_MAP` + `pins` from `week-demand.json` and accepting `--blueprint`.
3. **`ALGORITHM.md` completion + `T2` `allocate_week.py`** emitting `week-allocation.json` (240 bound `slot_id -> chunk_id` + projected `XP/TP/BP`).
4. **`SPEC-WEEKLY-DISPERSAL` + Register hygiene (`CDL-03/05`):** Remove `§2` settled duplicates in `Register`, fix `log.md:16` (`§8`), fix `WD-20` anchor list, close `DD-23/24/28` + `DD-16` voice check.
5. **Section `05` & `PrecapWeek` Integration Spec:** Lock whether Section `05` renders `Q13` Sequence/Craft board, `week-demand.json` dial inspector, or disperser summary alongside Matrix 2 `P/M/R` strip.

### Concrete Example — `epics.json` Chunk + `T2` Allocation Entry
```json
{
  "epics": [
    { "epic_id": "EP_p_knee", "branch": "P", "title": "Knee", "priority": 8, "op_project_id": null },
    { "epic_id": "EP_c_moa", "branch": "C", "title": "MasterOfArts", "priority": 9, "op_project_id": 6 }
  ],
  "chunks": [
    { "chunk_id": "CH_knee_iso_2m", "epic_id": "EP_p_knee", "title": "Isometric Terminal Knee Ext", "duration_min": 2, "base_xp": 10, "mode": "test_and_practice" }
  ],
  "t2_allocation_row": {
    "slot_id": "SO_THU_F2_I3_P", "branch": "P", "epic": "Knee", "chunk_id": "CH_knee_iso_2m",
    "xp": 14.2, "tp": 2, "reason": "quota=11 + gaussian(thu_moves=0.18) + spacing_gap=18h"
  }
}
```

---

## 6. Ratified Operator Decisions `[1–100 (I/E/R)]`

| ID | Topic | Ratified Resolution |
|---|---|---|
| **SEQ-D1 (`Gaussian σ`)** | Gaussian coupling curve around `18:30–19:30` evening physical courses | **LOCKED:** `σ = 6.0 hours` (`360 min`), centered at `19:00` midpoint, `w_max = 1.5x` (`w(Δt) = 1.0 + 0.5 * exp(-(Δt)^2 / (2 * σ^2))`), coupling to same-day (`F1..F4`, peaking `F3/F4`) and next-morning (`F1/F2`) Flows with no Fri→Sat cross-course bleed. |
| **SEQ-D2 (`R` & `DD-16`)** | `DD-16` numeric `BP` floor ruling & `R` Block rotation (`Yoga Nidra`, `Audiobooks`, `Socializing`) | **LOCKED:** Confirmed `DD-16` (*"no numeric BP floor cutoff"*); `24` in-Flow `R` breaks (`12m`, `XP = 0`) rotate via deterministic weighted round-robin (`Audiobooks 45%`, `Yoga Nidra 35%`, `Socializing 20%`) with Flow time-of-day affinity. |
| **SEQ-D3 (`SEQ-Q1/Q2`)** | Sequence vs Flow cardinality (`M04`/`D016`) & mixed `C` sprints | **LOCKED:** A **Sequence** is a multi-Flow learning/execution arc (`N:M` across Flows), and a single `120m` Flow may bind Chunks from different Portfolio Projects across `C1/C2/C3` (`SEQ-Q1/Q2`). |
| **SEQ-D4 (`05 UI / Q13`)** | Role of Section `05 · Sequencing Orientation` inside Precap Week | **LOCKED (Option A `[I90/E40/R15]`):** Section `05` renders the **Dispersal Dial & `Q13` Sequence-Arc View + Projected `XP/TP/BP` Breakdown** read from `week-allocation.json` and `week-demand.json`. |

---

## 7. Definition of Done (DoD)

1. `python build_slot_inventory.py` reads `physical.shares` directly from `week-demand.json` and passes `240`-slot verification (`72 P + 72 M + 72 C + 24 R`).
2. `epics.json` populated across all 4 branches (`M/P/R/C`) with valid OP IDs for `C`; `T2` `allocate_week.py` deterministically fills `168` (`72 P + 72 M + 24 R`) slots matching weekly quotas ±0 within `5%` ladder, respecting evening Gaussian weights & `DD-39/40`.
3. `ASSUMPTIONS-AND-DECISIONS-REGISTER.md` contains ONLY open cross-module decisions + single-owner map (`OD-03/DD-04/DD-05` moved cleanly to `log.md`); `sync_dispersal.py` runs cleanly across repos.
4. `DD-23, DD-24, DD-28, M04, SEQ-Q1..Q9`, and Section `05` cockpit semantics locked in `SPEC-WEEKLY-DISPERSAL.okf.md` & `SPEC-PRECAP-WEEK-ITERATIONS.okf.md`.

## 8. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/06-HANDOVER-SEQUENCING.md and 00-RULE-CANONICAL-DECISION-LOCK.md, working in MasterOfArts/Sequencing/dispersal/ + 02-weekly-dispersal/.
Let us close SEQ-D1..D4 (Gaussian σ, DD-16 voice confirm & R rotation, M04 Sequence vs Flow / SEQ-Q1-Q2, and Section 05 Q13 role), clean the duplicate Settled Today rows in ASSUMPTIONS-AND-DECISIONS-REGISTER.md, fix build_slot_inventory.py ignoring physical.shares, restore the Entity schema to author epics.json across M/P/R/C, build T2 allocate_week.py, and run sync_dispersal.py.
```
