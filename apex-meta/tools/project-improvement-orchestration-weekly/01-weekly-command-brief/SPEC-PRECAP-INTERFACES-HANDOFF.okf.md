---
type: specification
id: SPEC-PRECAP-INTERFACES-HANDOFF-v3.0
title: "Precap Interfaces & Handoff Modular Specification — Machine Schemas, Residuals, Sequencing & PrecapNextDay Handshake"
description: "Canonical modular specification governing machine schemas, Section 04 Residual Information, Section 05 Sequencing Dispersal, and downstream PrecapNextDay handoff."
status: current
date: 2026-11-12
parent_spec: SPEC-PRECAP-WEEK-MASTER.okf.md
scope: [weekly-orchestration, precap-week, interfaces, handoff, schemas, residuals, sequencing]
tags: [weekly-orchestration, precap-week, interfaces, handoff, schemas, specification, okf-v02]
references: [SPEC-PRECAP-WEEK-MASTER.okf.md, SPEC-MATRIX-1-PORTFOLIOS.okf.md, SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md]
---

# Precap Interfaces & Handoff Modular Specification — Machine Schemas, Residuals, Sequencing & PrecapNextDay Handshake

## Section 1 — Machine Schema Architecture & Validation Contracts

All weekly orchestration data structures are strictly governed by JSON Schema Draft 2020-12 definitions under [`schemas/`](schemas/):

1. **Stage 1A Operator Intake Schema**: [`schemas/operator-weekly-command-brief.schema.json`](schemas/operator-weekly-command-brief.schema.json) validates initial weekly inputs, focus overrides, calendar ignores, and personal focus bullets.
2. **Stage 1B PrecapWeek Cockpit Schema**: [`schemas/precap-week-cockpit.schema.json`](schemas/precap-week-cockpit.schema.json) validates the compiled 6-Portfolio state, Matrix 1 goals, Matrix 2 timetable items, Section 04 residuals, and downstream handoff payload.
3. **Downstream Handshake Schema**: [`schemas/presentation-handoff.schema.json`](schemas/presentation-handoff.schema.json) governs the machine envelope passed to `PrecapNextDay` (`PRECAP-WEEK-HANDOFF-v2.1`).

*Validation Contract*: Compiler [`render_precap_cockpit.py`](render_precap_cockpit.py) runs stdlib Python validation across these schemas on every compilation pass. Schema violations abort execution immediately.

---

## Section 2 — Section 04: Residual Information Contract

Section 04 captures operational reality, data quality gaps, longlist deferrals, and provenance ledger tracking across a formal 4-card grid:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ SECTION 04 RESIDUAL INFORMATION (Formal 4-Card Architecture)           │
├───────────────────────────────────┬────────────────────────────────────┤
│ Card 1: Clock & Capacity Recon    │ Card 2: EM-13 & OP Readiness Gaps  │
│ Gross 48h / Net 35h C (Alex -60m) │ OP-OFFLINE fallback, [OP-UNRES]    │
├───────────────────────────────────┼────────────────────────────────────┤
│ Card 3: Longlist Deferrals        │ Card 4: 1-Hop Provenance Ledger    │
│ Reason + Revisit Trigger per item │ [CLK], [DSP], [INT], [GCAL], [OP]  │
└───────────────────────────────────┴────────────────────────────────────┘
```

### Card 1 — Clock & Capacity Reconciliation

Reconciles nominal capacity with external collisions:
- **Canonical Capacity Basis**: Gross duration (`2,880m`), Craft budget (`2,160m` / 72 sprints), non-Craft allowance (`720m` / 144m P, 216m M, 288m R, 72m recap), and 240 slot occurrences are governed canonically by [`SPEC-PRECAP-WEEK-MASTER.okf.md §3.1`](SPEC-PRECAP-WEEK-MASTER.okf.md#section-31--section-00-portfolio-compass--statusmerge-basis).
- **Net Committed Craft Capacity**: Nominal Craft (36.0h) minus verified external meeting overlaps (e.g. -60m Alex & Chris = 35.0h committed Craft).

### Card 2 — EM-13 & OpenProject Readiness Gaps

Monitors alignment and data quality across external systems:
- Audits completeness of the six fields (`G|I|P|S|O|C`) across all active L1 and L2 cards.
- Tracks `[OP-OFFLINE]` fallback states when `http://127.0.0.1:8083` is unreachable (`ECONNREFUSED`).
- Identifies local items awaiting work package mapping (`[OP-UNRESOLVED]`).
- Surfaces relational status-vs-description contradictions (e.g. `WP#220`).

### Card 3 — Longlist Deferrals & Revisit Triggers

Maintains a disciplined register of candidates evaluated but deliberately excluded from active weekly execution:
- Every deferred item must state an explicit, evidence-based **Reason** (e.g. dependency on upstream website information architecture).
- Every deferred item must state an observable, concrete **Revisit Trigger** (e.g. `After OP-WP#163 sign-off` or `After first signed Flow client contract`).
- Prevents cognitive clutter in Matrix 1 while ensuring valuable backlog ideas are not forgotten.

### Card 4 — 1-Hop Provenance Ledger & Downstream Handoff

Provides verifiable source tracking for every figure, policy, and schedule item:
- **Freshness Ledger**: Tracks 1-hop source tags and freshness states:
  - `[CLK]`: `02-weekly-dispersal/week-blueprint.json` (Canonical Clock).
  - `[DSP]`: `02-weekly-dispersal/week-allocation.json` (Dispersal Solver Allocations).
  - `[INT]`: `fixtures/w46-reference-intake.json` (Operator Momentary Intake).
  - `[GCAL]`: Live Google Calendar Query (Nov 9–23).
  - `[GIT]`: Live repository commit SHAs, handovers, and `2Dos.md`.
  - `[OP]`: OpenProject snapshot evidence (`00-openproject-dependency-intake/EVIDENCE-20261106.okf.md`).
  - `[CAR]`: Carrier map definitions (`18-APEX-CARRIER-MAP.md`).
- **Confidence Rating**: Formal statement of analytical certainty (e.g. HIGH on clock math and GCal holds; MEDIUM on offline OpenProject sync).
- **Assumptions**: Transparent enumeration of unverified assumptions (e.g. handling of duplicate calendar entries or unscheduled meetings).
- **Presentation Handoff Pointer**: Direct reference to the machine-validated JSON envelope passed to `PrecapNextDay`.

---

## Section 3 — Section 05: Sequencing Orientation & Dispersal Integration

Section 05 acts as the integration bridge between directional weekly planning and the mathematical dispersal engine under [`02-weekly-dispersal/`](../02-weekly-dispersal/). It dynamically reads [`week-demand.json`](../02-weekly-dispersal/week-demand.json) and [`week-allocation.json`](../02-weekly-dispersal/week-allocation.json) without duplicating solver algorithms.

### Dual-Repository Authority Model (`DD-15`)

- **Solver Canonical Mirror**: Dispersal algorithms and `allocate_week.py` are mirrored between `MasterOfArts/Sequencing/dispersal/` and `02-weekly-dispersal/`.
- **Clock Authority**: The canonical blueprint clock (`week-blueprint.json`) lives authoritative in `apexai-os-meta`.

### Four-Branch Epic Allocations (240 Slot Occurrences)

The dispersal solver allocates all 240 slot occurrences across four foundational branches:

| Epic Branch | Slot Quota | In-Flow Duration | Allocated Focus Modalities / Projects |
|---|:---:|:---:|---|
| **Mental (`M`)** | 72 slots | 216 min | Morning Intention (`focus_days`), ACIM presence, Surrender transitions, Breathing. |
| **Physical (`P`)** | 72 slots | 144 min | Martial Arts, Dance, S/BJJ, General micro-mobility, Knee therapy (pinned `*_*_I3_P`). |
| **Regeneration (`R`)** | 24 breaks | 288 min | Audiobooks, Yoga Nidra, Socializing. Weighted round-robin rotation, `XP = 0`, `DD-16` zero BP floor. |
| **Craft / Projects (`C`)** | 72 sprints | 2,160 min | 6 Canonical Portfolio Epics (Leela, IPOS, Master of Arts, Apex AI, Mindful Bar, Residual). |

*Note*: Evening Physical Courses (e.g. 18:30–19:30 Dance/Kicks/Moves) occur outside the 72 × 2m in-Flow `P` quota.

### Gaussian Focus Coupling & Sequence Arcs (`M04 / Q13`)

- **Temporal Weighting**: Cognitive focus weight follows a Gaussian coupling curve centered around 19:00 with standard deviation $\sigma = 6.0\text{h}$ and maximum weight $w_{\max} = 1.5\times$. Bleed across the Friday-to-Saturday boundary is strictly prohibited.
- **Sequence vs. Flow Cardinality**: Sequences and Flows have an $N:M$ relationship. Mixed-project Craft sprints (`C1–C3`) within a single Flow block are fully authorized when aligned with critical-path sequence arcs.
- **Projected Yields**: Models projected Time Points (`TP`), Experience Points (`XP`), and Balance Points (`BP`) across the standard 50/25/25 ratio. Regeneration breaks mint 0 XP to preserve restorative integrity.

---

## Section 4 — Downstream Handshake Contract (`PrecapWeek -> PrecapNextDay`)

PrecapWeek terminates by emitting exactly one validated `presentation_handoff` envelope conforming to Draft 2020-12 schema [`schemas/presentation-handoff.schema.json`](schemas/presentation-handoff.schema.json) (`PRECAP-WEEK-HANDOFF-v2.1`).

The live reference payload is maintained canonically in [`fixtures/w46-reference-handoff.json`](fixtures/w46-reference-handoff.json).

### Envelope Structure & Core Fields

The handoff object provides `PrecapNextDay` with verified weekly strategy context:
- `schema_version`: Contract version identifier (`PRECAP-WEEK-HANDOFF-v2.1`).
- `artifact_type`: Formal deliverable type (`Weekly_Command_Brief`).
- `packet_id`: Unique deterministic packet identifier.
- `date_range` & `timezone`: ISO week temporal boundaries (`Europe/Berlin`).
- `clock_owner` & `dispersal_owner`: Paths to authoritative clock and allocation artifacts.
- `result_state` & `operator_g1_status`: Pipeline gate status (`READY_WITH_REVIEW`, `PROPOSED_FOR_G1`).
- `source_status`: External system telemetry (`openproject`, `google_calendar`).
- `six_portfolio_areas`: Array of active portfolio goals and cross-repo dependencies.
- `reconciled_calendar_events`: Normalized calendar holds with capacity delta impacts.
- `next_day_seed`: Initial target date and focus emphasis for `PrecapNextDay`.
- `next_consumer`: Downstream consumer identifier (`PrecapNextDay`).

### Orchestration Envelope Wrapping

When executed under `weekly-orchestrator`, the report brief and handoff packet are enclosed in a standardized `handoff_envelope` ([`handoff-schema.md`](../../../../.claude/skills/weekly-orchestrator/references/handoff-schema.md)):
- Preserves `artifact_type: "Weekly_Command_Brief"`.
- Preserves `next_consumer: "PrecapNextDay"`.
- Establishes a verified boundary between weekly strategy and daily tactical execution.

---

## Section 5 — Operative Failure-Mode Guards & Circuit Breakers

In accordance with `WP-25`, this specification closes with operative terminal failure-mode guards:
1. **Schema Validation Guard**: Any presentation handoff packet failing Draft 2020-12 validation against `presentation-handoff.schema.json` causes immediate pipeline halt.
2. **G1 Approval Guard**: Handshake release to `PrecapNextDay` is blocked unless `operator_g1_status` resolves to `APPROVED` or explicit operator override.
3. **Regeneration Purity Guard**: Regeneration slots must mint zero Experience Points (`XP = 0`). Any non-zero XP calculation violates `DD-16` and fails allocation audit.
4. **Boundary Isolation Guard**: Dispersal algorithms remain strictly isolated within `02-weekly-dispersal/` and upstream mirror (`DD-15`); PrecapWeek consumes allocations via JSON interfaces without duplicating solver logic.
