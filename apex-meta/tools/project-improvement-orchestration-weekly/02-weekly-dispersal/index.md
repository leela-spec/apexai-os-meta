---
okf_version: "0.2"
title: Weekly Dispersal Bundle
description: The weekly dispersal slice — governed specification, algorithm rules, weekly demand dials, slot inventory, active register, and changelog.
status: current
date: 2026-11-10
tags: [sequencing, dispersal, weekly-orchestration, precap-week, slot-inventory, quota]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal Bundle

> **Zone:** `MasterOfArts/Sequencing/dispersal/`, mirrored one-way into
> `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/`.
> **Single Blueprint Clock Owner:** `apexai-os-meta/.../02-weekly-dispersal/week-blueprint.json` owns the calendar clock (`08:00–24:00` weekday, `12:00–16:00` weekend); `MasterOfArts` owns Sequencing (`Epics`, shares, allocator) and derived slot inventory outputs (`DD-15`).

Sequencing is a distribution system powered by interleaving, spaced repetition, chunking, and testing to achieve a valuable dispersion of practicing and pursuing goals, skills, and trainings.

## Files

| File | Type | Description |
|---|---|---|
| `week-blueprint.json` *(in `apexai-os-meta/.../02-weekly-dispersal/`)* | **Canonical Clock Owner** | Sole canonical owner of the weekly calendar clock (`08:00–24:00` Mon–Fri, `960 min`; `12:00–16:00` Sat–Sun, `240 min`). |
| [`week-demand.json`](week-demand.json) | Operator Demand (`DD-02`) | Weekly priority shares, priorities, pins, focus days, and evening physical course table (`OD-03`, `DD-03`). |
| [`EPICS-SCHEMA.md`](EPICS-SCHEMA.md) | **Specification** | Six-table entity schema (`EPIC`, `BLOCK`, `CHUNK`, `NODE_PLACEMENT`, `SET_MEMBER`, `EDGE`) governing `epics.json` (`WD-37`..`WD-40`). |
| [`epics.json`](epics.json) | Canonical Data | Personal Epic database across `M`, `P`, `R`, and the 6 Portfolio Areas (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`). |
| [`SPEC-WEEKLY-DISPERSAL.okf.md`](SPEC-WEEKLY-DISPERSAL.okf.md) | **Specification** | Canonical contract: `3x3` Flow composition, regimes, slot inventory rules, Epics across all 4 branches, and guards (`WD-01`..`WD-48`). |
| [`ALGORITHM.md`](ALGORITHM.md) | **Specification** | Single owner of projected XP/TP/BP scoring, BP authority (`DD-01`, `DD-16`), quota rounding, and evening-to-flow Gaussian coupling. |
| [`build_slot_inventory.py`](build_slot_inventory.py) | Generator (`T1`) | Reads `week-blueprint.json` and `week-demand.json`, validates zero overlaps, and generates `slot-inventory.json`. |
| [`slot-inventory.json`](slot-inventory.json) | Generated Data (`T1`) | 24 Flows, 240 slot occurrences with stable addresses, regime timelines, and resolved Mental/Physical quotas. |
| [`allocate_week.py`](allocate_week.py) | Allocator (`T2`) | Reads `slot-inventory.json`, `week-demand.json`, and `epics.json`; binds all 240 slots and computes projected `TP`, `XP`, and `BP`. |
| [`week-allocation.json`](week-allocation.json) | Generated Data (`T2`) | 240 bound slot allocations, Matrix 2 `P/M/R` bands, and projected `TP / XP / BP` summary. |
| [`render_blueprint.py`](render_blueprint.py) | Renderer | Reads `slot-inventory.json` and `week-blueprint.json` to generate `week-blueprint.html` (`WD-36b`). |
| [`week-blueprint.html`](week-blueprint.html) | Generated View | Human-readable week timeline, Flow grid, and quota tables. Regenerate; never edit. |
| [`sync_dispersal.py`](sync_dispersal.py) | Tool | One-way mirror of this bundle into `apexai-os-meta`, preserving canonical `week-blueprint.json` there. |
| [`ASSUMPTIONS-AND-DECISIONS-REGISTER.md`](ASSUMPTIONS-AND-DECISIONS-REGISTER.md) | Reference | Active open cross-module questions, unverified runtime gaps, and single-owner map. |
| [`PRECAP-INTEGRATION-ANALYSIS.md`](PRECAP-INTEGRATION-ANALYSIS.md) | Reference (Snapshot) | Historical 2026-11-09 integration analysis against Precap Week v2.0 and Handovers 03–06. |
| [`log.md`](log.md) | Changelog | Archive of closed `DD-*` / `OD-*` / `A-*` / `X-*` rulings and modification history. |

## Status

Calendar clock (`week-blueprint.json`), `week-demand.json` draft (`DD-02`), focus days (`DD-03`), `Knee` in branch `P` (`DD-04`), Sunday ACIM (`DD-05`), no numeric BP cutoff (`DD-16`), one `Regeneration` Epic with Blocks (`DD-17`), and weekend 2-Flow regime (`DD-18`) are settled. Four cross-module Precap questions (`DD-23`, `DD-24`, `DD-26`, `DD-28`) remain open in [`ASSUMPTIONS-AND-DECISIONS-REGISTER.md`](ASSUMPTIONS-AND-DECISIONS-REGISTER.md).

Next in product build: the slot-filling allocator (`T2`), Personal Epic JSON data across `M/P/R/C`, and live Matrix 2 HTML rendering (`T4`).

## Related

- Weekly Orchestration Ledger: `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md`
- Precap Week specification: `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`
- Sequencing decisions: [`../decisions.md`](../decisions.md) — open choice `N05`
