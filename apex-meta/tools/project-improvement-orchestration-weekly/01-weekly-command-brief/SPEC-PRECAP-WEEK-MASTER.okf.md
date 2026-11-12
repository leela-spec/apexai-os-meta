---
type: specification
id: SPEC-PRECAP-WEEK-MASTER-v3.0
title: "Precap Week Master Specification — Operator Cockpit & Weekly Orchestration"
description: "Canonical master specification governing the weekly planning process, 6-Portfolio Standard, Portfolio Compass (00), Operator Decisions (01), lifecycle, and acceptance gates."
status: current
date: 2026-11-12
scope: [weekly-orchestration, precap-week, master-spec, six-portfolios, g1-gate]
tags: [weekly-orchestration, precap-week, specification, okf-v02]
references: [SPEC-MATRIX-1-PORTFOLIOS.okf.md, SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md, SPEC-SEQUENCING.okf.md, SPEC-PRECAP-INTERFACES-HANDOFF.okf.md]
---

# Precap Week Master Specification — Operator Cockpit & Weekly Orchestration

## Section 1 — Executive Summary & Core Architectural Invariants

This master specification governs the **Precap Week Planning Process (`PrecapWeek`)**, its deterministic multi-surface presentation compiler ([`render_precap_cockpit.py`](render_precap_cockpit.py)), Draft 2020-12 machine schemas ([`schemas/`](schemas/)), and the three synchronized output surfaces: the interactive HTML Cockpit (`v0.5`), the OKF v0.2 Weekly Command Brief, and the downstream handoff JSON.

### Process vs. Artifact Boundary (Architectural Decision D1 / Option 1B)

- **`PrecapWeek`**: Designates the weekly planning skill and orchestration process (owned by `.claude/skills/PrecapWeek/`).
- **`Weekly Command Brief`**: Designates the executive report deliverable emitted for human review and downstream agents.
- The directory `01-weekly-command-brief/` is retained for filesystem stability while this master specification establishes single-source truth.

### Modular Specification Suite Governance

Modular specifications govern dedicated concerns without duplicate bodies:
- **Matrix 1 (Non-Temporal Goals)**: Governed by [`SPEC-MATRIX-1-PORTFOLIOS.okf.md`](SPEC-MATRIX-1-PORTFOLIOS.okf.md). Stacks the 6 portfolios, `L1/L2` hierarchy, `EM-13` `G|I|P|S|O|C` drawers, and inline cross-repo pills. Contains zero sprints.
- **Matrix 2 (Temporal Timetable)**: Governed by [`SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`](SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md). Governs the Monday–Sunday timetable, blueprint clock, calendar intake, and Personal Focus Strip.
- **Sequencing (Section 05 & Dispersal Root)**: Governed by [`SPEC-SEQUENCING.okf.md`](SPEC-SEQUENCING.okf.md). Owns Section `05` orientation, Gaussian coupling, and delegates solver subspecs to [`02-weekly-dispersal/`](../02-weekly-dispersal/index.md) (`DD-15`).
- **Interfaces & Handoff**: Governed by [`SPEC-PRECAP-INTERFACES-HANDOFF.okf.md`](SPEC-PRECAP-INTERFACES-HANDOFF.okf.md). Governs machine schemas, Section 04 Residuals, and `PrecapNextDay` handshake.

---

## Section 2 — Canonical 6-Portfolio Architecture Standard (`06-PORTFOLIO`)

Every weekly orchestration surface and JSON schema strictly enforces the canonical 6-Portfolio standard:

| # | Portfolio Area | Canonical Repositories | Work Packages | Core Architectural Scope |
|---|---|---|---|---|
| 1 | **Leela** | `leela-game-flutter`, `leela-website`, `leela-spec` | OpenProject #10 | Skill Tree spatial node contracts, Chunk library, Crown engine §F.1–§F.5. |
| 2 | **IPOS** | `IPOS` | OpenProject #16 | Financial advisory ingestion pipeline, Docling/Trafilatura seam, YouTube/RSS breadth. |
| 3 | **Master of Arts** | `MasterOfArts` | OpenProject #14, #6, #7 | Flow video series (01..06) to filming, Website Stage 3 IA, automated PDF billing. |
| 4 | **Apex AI** | `apexai-os-meta` | OpenProject #8 | OpenMouse kernel HID bindings, mindful repository orchestration, Layer-1 Benchmark. |
| 5 | **Mindful Bar** | `leela-spec/mindful-bar`, `mindful-bar` | Carrier Map / OP Sync | Cacao Bar product specification, ERPNext evaluation, 20–60 friend tasting Micro pass. |
| 6 | **Residual** | Root environment, Personal rhythms | Auxiliary / Unmapped | Apartment & studio art, Sexy Content, Community & Travel, auxiliary rhythms. |

---

## Section 3 — Executive Overviews: Section 00 & Section 01

### Section 3.1 — Section 00: Portfolio Compass & Canonical Capacity Arithmetic (`T1`)

The Portfolio Compass delivers an instant, source-grounded executive summary via 5 visible cards (`Net Craft Capacity`, `Total Weekly Flows`, `3x3 Craft Sprints`, `6 Portfolio Areas`, `Gate & Source Readiness`).

This master specification is the single authoritative owner of weekly capacity arithmetic:
- **Gross Duration**: Exactly **2,880 minutes** (`48.0h` across 24 Flows).
- **Nominal Craft Budget**: Exactly **2,160 minutes** (`36.0h` across 72 sprints of 30m).
- **Nominal Non-Craft Allowance**: Exactly **720 minutes** (`12.0h`), partitioned into `P` (144m, 72 × 2m), `M` (216m, 72 × 3m), `R` (288m, 24 × 12m), and trailing recap (72m, 24 Flows × 3 sprints × 1m).
- **Slot Invariant**: Instantiates exactly **240 unique slot occurrences** (`72 P + 72 M + 72 C + 24 R`).
- **StatusMerge Reconciliation**: Closing-week `FlowRecap` logs reconcile `○ Placed` vs `● Realized` with capped `execution_rate <= 1.0` and zero-denominator handling.

### Section 3.2 — Section 01: Operator Decision Brief & G1 Governance

The Operator Decision Brief triages executive dials, week-specific pivots, and external calendar holds:
- **Three-Card Preview**: `NEW` (scope changes, overrides, G1 gates), `ONGOING` (standing guards, ignored ambient holds, protected events), `STANDARD` (hydrated dynamically from [`week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json)).
- **Override Evidence Triad**: `OPERATOR OVERRIDE` renders if and only if `{system_default, operator_choice, source_ref}` are all verified and `system_default != operator_choice`.
- **Gate G1 Governance**: Formally tracks approval states (`PROPOSED_FOR_G1`, `APPROVED`, `EDITED`, `REJECTED`). Unapproved plans block downstream execution.

---

## Section 4 — Macro 4-Stage Weekly Planning Lifecycle

| Stage | Name | Schema / Tool | Primary Operations |
|---|---|---|---|
| **1A** | Operator Intake | `operator-weekly-command-brief.schema.json` | Focus overrides, calendar ignores, personal focus bullets. |
| **1B** | PrecapWeek Compilation | `render_precap_cockpit.py` | Validates schemas; compiles HTML Cockpit, OKF Brief, and handoff JSON. |
| **2/3** | Downstream Handshake | `presentation-handoff.schema.json` | `PrecapNextDay` decomposes weekly targets into daily S1-S3 sprints. |
| **4/5** | Flow Recap & StatusMerge | `FlowRecap` cadence | Saturday/Sunday closing window; reconciles yields and seeds W(n+1) intake. |

---

## Section 5 — Operator Research Synthesis & Comprehension Framing (`D1–D12`)

- **Calm Clarity over Data Dumps**: Make project reality and capacity legible within seconds (`D2` 10-second contract).
- **Decision Before Detail (`D1`)**: Governance choices and gates appear first; tactical breakdowns disclose progressively.
- **Value Over Machinery (`D3`)**: Lead with user-facing deliverables; keep validation mechanics in Section 04 Residuals.
- **Directional vs Executable Separation**: `PrecapWeek` establishes macro direction; tactical intra-sprint checklists belong to `PrecapNextDay`.

---

## Section 6 — Canonical Companion Owners & Machine Contracts

| Operational Domain | Authoritative Canonical Owner | Secondary / Downstream Consumer | Governance Standard |
|---|---|---|---|
| **Multi-Surface Compiler** | [`render_precap_cockpit.py`](render_precap_cockpit.py) | CI, pre-commit, agent invocations | Stdlib-only Python, Draft 2020-12 |
| **Machine Schemas** | [`schemas/`](schemas/) | Compiler, test runners | Draft 2020-12 strict JSON schemas |
| **Canonical Blueprint Clock** | [`02-weekly-dispersal/week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json) | Matrix 2, StatusMerge, HTML Cockpit | Single clock source for all daily times |
| **Weekly Allocation & Dials** | [`02-weekly-dispersal/week-allocation.json`](../02-weekly-dispersal/week-allocation.json) | Section 05, HTML Cockpit | `allocate_week.py`, Gaussian coupling |
| **OpenProject Intake Seam** | [`00-openproject-dependency-intake/HANDOVER-20261106.okf.md`](../00-openproject-dependency-intake/HANDOVER-20261106.okf.md) | Matrix 1 intake, Section 04 gaps | `opCall.js` read-only, `[OP-OFFLINE]` fallback |
| **Downstream Handoff Envelope** | [`schemas/presentation-handoff.schema.json`](schemas/presentation-handoff.schema.json) | `PrecapNextDay` daily execution | `PRECAP-WEEK-HANDOFF-v2.1` contract |

---

## Section 7 — Acceptance Gates & Operative Failure-Mode Guards

The weekly planning suite enforces six acceptance gates (`UX-00` through `UX-07`, `CONTRACT-01`). In accordance with `WP-25`, this master specification closes with non-negotiable operative failure-mode guards:
1. **Unverified Override Rejection**: Overrides lacking the verified evidence triad `{system_default, operator_choice, source_ref}` trigger validation errors.
2. **Offline Fallback Guard**: Unreachable services fail closed with explicit tokens (`[OP-OFFLINE]`, `[OP-UNRESOLVED]`). Synthetic numeric IDs are prohibited.
3. **Gate G1 Execution Blocker**: Unapproved weekly plans (`PROPOSED_FOR_G1`) cannot be executed by `PrecapNextDay` without explicit operator sign-off.
4. **Capacity Conservation Invariant**: Total gross time must equal exactly 2,880 minutes. The 240 slot occurrences are immutable across all planning surfaces.
