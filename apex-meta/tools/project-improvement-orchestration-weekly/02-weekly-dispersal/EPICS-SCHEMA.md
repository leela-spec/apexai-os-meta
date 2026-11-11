---
type: Specification
id: MOA-SEQ-EPICS-SCHEMA
title: Personal Epic Database Entity Schema
description: Six-table entity schema (EPIC, BLOCK, CHUNK, NODE_PLACEMENT, SET_MEMBER, EDGE) governing epics.json across all four branches (M, P, R, C).
status: current
tags: [sequencing, dispersal, epics, schema, entity-model, wd-37, wd-40]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Personal Epic Database Entity Schema

This specification restores and governs the six-table entity model (`10_ENTITY_MODEL.md:13-78`, `WD-37`..`WD-40`) used by [`epics.json`](epics.json) and the `T2` weekly slot allocator ([`allocate_week.py`](allocate_week.py)).

---

## 1. Core Schema Invariants

- **EPS-01 [P0 | I96/E96/R04] Mirror The Six Canonical Tables (`WD-37`)**: Every record in [`epics.json`](epics.json) belongs to one of six tables: `epics` (`EPIC`), `blocks` (`BLOCK`), `chunks` (`CHUNK`), `node_placements` (`NODE_PLACEMENT`), `set_members` (`SET_MEMBER`), or `edges` (`EDGE`). Never invent ad-hoc tables or duplicate intrinsic content inside placements.
- **EPS-02 [P1 | I94/E95/R04] Sub-Blocks Carry `parent_block_id` (`WD-38`)**: Represent sub-blocks as rows in `blocks` with a non-null `parent_block_id` and `level` (`2..4`), never as a separate entity type.
- **EPS-03 [P0 | I95/E96/R04] Canonical Chunk Identity (`WD-39`)**: One `CHUNK` (`CH_*`) owns intrinsic practice or craft metadata (`title`, `duration_min`, `base_xp`, `mode`). Attach a Chunk to an Epic or Block via `NODE_PLACEMENT` (`NP_*`), never by cloning the Chunk.
- **EPS-04 [P0 | I95/E94/R05] Four-Branch Coverage With 6-Portfolio Craft Standard (`WD-40`)**: Populate `epics` across all four branches:
  - **`M` (Mental)**: `Intention`, `ACIM`, `Surrender`, `Breathing`
  - **`P` (Physical)**: `Martial Arts`, `Dance`, `S/BJJ`, `General`, `Knee`
  - **`R` (Regeneration)**: `Regeneration` (with `Yoga Nidra`, `Audiobooks`, and `Socializing` as `BLOCK` rows; `base_xp: 0`)
  - **`C` (Craft / Projects)**: The **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) mapped to OpenProject (`op_project_id: 10, 16, 14, 8, null, null`).

---

## 2. Table Definitions & ID Grammar

| Table Key | Entity | ID Prefix | Required Fields | Notes |
|---|---|---|---|---|
| `epics` | `EPIC` | `EP_<branch>_<slug>` | `epic_id`, `branch` (`M\|P\|R\|C`), `title`, `priority` (`1..10`), `op_project_id` (`int\|null`), `status` | `priority` drives `priority_factor(epic)` in [`ALGORITHM.md`](ALGORITHM.md) (`0.75x..1.50x`). |
| `blocks` | `BLOCK` | `BL_<branch>_<slug>` | `block_id`, `epic_id`, `parent_block_id` (`str\|null`), `level` (`1..4`), `title`, `order_index` | Holds structural groupings such as `Regeneration` Blocks (`Yoga Nidra`, `Audiobooks`, `Socializing`) or physical sub-disciplines (`Strikes`, `Kicks`, `Moves`). |
| `chunks` | `CHUNK` | `CH_<branch>_<slug>` | `chunk_id`, `branch` (`M\|P\|R\|C`), `title`, `duration_min`, `base_xp`, `mode`, `op_ref` (`str\|null`) | For `P/M/C`, `base_xp = 1.0 * duration_min`; for `R`, `base_xp = 0` (`ST-010`, `ALG-01`). |
| `node_placements` | `NODE_PLACEMENT` | `NP_<epic>_<chunk>` | `placement_id`, `epic_id`, `block_id` (`str\|null`), `chunk_id`, `weight`, `rotation_order` | Links canonical `CH_*` records into `EP_*` and `BL_*` hierarchies. |
| `set_members` | `SET_MEMBER` | `SM_<set>_<idx>` | `set_id`, `member_type` (`CHUNK\|BLOCK`), `member_id`, `sequence_index` | Groups ordered drill progressions or micro-sets across iterations `I1..I3`. |
| `edges` | `EDGE` | `ED_<src>_<dst>` | `edge_id`, `from_id`, `to_id`, `relation` (`prerequisite\|synergy\|blocks`), `weight` | Captures cross-Chunk or cross-Project dependencies (`SEQ-Q1`). |

---

## 3. Schema Failure Guards

- **EPS-05 [P0 | I96/E95/R04] Reject Non-Zero `base_xp` on Branch `R`**: Any `CHUNK` with `branch == "R"` and `base_xp > 0` fails schema validation (`ST-010`, `WD-45`).
- **EPS-06 [P1 | I92/E94/R05] Enforce Duration Alignment With Flow Contract**: In-Flow `CHUNK` durations must match branch slot durations (`P = 2`, `M = 3`, `C = 30`, `R = 12`).
- **EPS-07 [P1 | I92/E92/R05] Enforce Priority Range**: Every `EPIC.priority` must be an integer in `1..10`.
