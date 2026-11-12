---
okf_version: "0.2"
type: index
id: INDEX-SEQUENCING-ONLINE-AI-v1.0
title: "Online AI Sequencing & Precap Index — Relative-Path Map & Settled Decisions"
description: "QMD-curated relative-path index for online AIs without local QMD access, mapping PrecapWeek, Sequencing, Dispersal solver, HTML Cockpit, PrecapNextDay, and MasterOfArts origin boundaries."
status: current
date: 2026-11-12
scope: [weekly-orchestration, sequencing, dispersal, precap-week, precap-next-day, online-ai-index]
tags: [weekly-orchestration, sequencing, online-context, index, okf-v02]
references: [HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md, DECISIONS.md, 01-weekly-command-brief/SPEC-SEQUENCING.okf.md, 01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md, 02-weekly-dispersal/index.md]
---

# Online AI Sequencing & Precap Index (`apexai-os-meta` + `MasterOfArts`)

This index guides an online AI across both connected repositories (`leela-spec/apexai-os-meta` and `leela-spec/MasterOfArts`). Every in-repo link resolves relative to `apex-meta/tools/project-improvement-orchestration-weekly/`. Section 7 maps companion files inside `MasterOfArts/Sequencing/`.

## Section 1 — Locked Architecture & Operator Model Summary

Start with these settled facts before reading individual specs:

- **Foreground HTML Scope:** `PrecapWeek` HTML shows only the operator-decided **Epics/Chunks standard** and **very short Project-Day alignments**.
- **Background Engine Scope:** The **Gaussian focus window** and **Epic band slot targets** run in the background, feeding both `PrecapWeek` and `PrecapNextDay`.
- **Craft (`C`) Belongs to Flows & Matrix 1:** Actual project tasks (`C`) are authored in **Matrix 1** (`selected_work_reference[]`) and executed inside Flows, not `epics.json` micro-chunks.
- **Sequencing Branch Scope (`P`, `M`, `R`):** `epics.json` stores `Epics -> Blocks -> Chunks` for non-Craft mastery (`P` `72`, `M` `72`, `R` `24`). `PrecapNextDay` hydrates daily Flows with concrete Chunks.
- **Locked Weekly Math (`D018 / D020`):** Every week runs `24` Flows (`4/day` Mon–Fri, `2/day` Sat–Sun). Each Flow equals `120m` across `3 × (2m P + 3m M + 30m C + 1m recap) + 12m R` (`240` slots, `2,880m`).
- **Gaussian Coupling for `P` and `M` (`SEQ-D1`):** Evening physical courses (`18:30–19:30`, outside `P` quota `DD-39`) radiate `w(Δt) = 1.0 + 0.5 × exp(-(Δt)² / (2σ²))` around `19:00` (`σ = 6.0h`, `w_max = 1.5x`, no Fri→Sat bleed) for **both `P` and `M`** in the background.
- **Verified Live Solver Gaps:** Today `allocate_week.py` runs Gaussian coupling only on `P` (not `M`), carries static `C` placeholder chunks (`c_portfolio_cycle`), and pre-binds `chunk_id` at weekly time instead of delegating `CH_*` selection to `PrecapNextDay`.

---

## Section 2 — P0: Entry Handover & Locked Decision Registers

Read these files first to understand the active design task and settled rulings:

| Priority | Relative Path (`apexai-os-meta`) | Owner / Role | Key Content to Extract |
|:---:|---|---|---|
| **P0** | [`HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md`](HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md) | Active Task Contract | Gaps, `D-SEQ-01..06` questions, HTML/PrecapWeek/PrecapNextDay tracks, verification gates |
| **P0** | [`DECISIONS.md`](DECISIONS.md) | Master Decision Ledger | Locked `D001–D021` orchestration, `3x3`, `06-PORTFOLIO`, `OP`, and `DD-15` rules |
| **P0** | [`CURRENT-STATE.md`](CURRENT-STATE.md) | Active System Snapshot | Live module state, unpushed local baseline, active workstreams |
| **P0** | [`00-openproject-dependency-intake/HANDOVER-20261106.okf.md`](00-openproject-dependency-intake/HANDOVER-20261106.okf.md) | OP Intake Contract (`D014`) | Read-only `:8083` WP frontier rules and offline fallback protocol |
| **P0** | [`00-openproject-dependency-intake/EVIDENCE-20261106.okf.md`](00-openproject-dependency-intake/EVIDENCE-20261106.okf.md) | OP Snapshot Fixture | Verified Nov 6 OpenProject portfolio/WP snapshot used offline |

---

## Section 3 — P1: PrecapWeek Master, Sequencing & Dispersal Specs

Read these single-owner specifications next without merging or duplicating their bodies:

| Priority | Relative Path (`apexai-os-meta`) | Owner / Role | Key Content to Extract |
|:---:|---|---|---|
| **P1** | [`01-weekly-command-brief/SPEC-SEQUENCING.okf.md`](01-weekly-command-brief/SPEC-SEQUENCING.okf.md) | Section `05` Root Spec | `PrecapWeek` Sequencing scope, `DD-15` dual-repo boundary, Gaussian/BP guards |
| **P1** | [`01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md`](01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md) | Master Week Spec | Sections `00–05` hierarchy, `2,880m / 240` slot accounting, G1 gate |
| **P1** | [`01-weekly-command-brief/SPEC-MATRIX-1-PORTFOLIOS.okf.md`](01-weekly-command-brief/SPEC-MATRIX-1-PORTFOLIOS.okf.md) | Matrix 1 Spec | 6 Portfolios, `L1/L2` depth, `EM-13` `G\|I\|P\|S\|O\|C`, `selected_work_reference[]` |
| **P1** | [`01-weekly-command-brief/SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`](01-weekly-command-brief/SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md) | Matrix 2 Spec | `Mon–Sun` timetable, `DD-22A` anatomy, `Q06/Q08` depth wall vs `PrecapNextDay` |
| **P1** | [`01-weekly-command-brief/SPEC-PRECAP-INTERFACES-HANDOFF.okf.md`](01-weekly-command-brief/SPEC-PRECAP-INTERFACES-HANDOFF.okf.md) | Interfaces & Handoff Spec | Schema ownership, Section `04` Residuals, `PrecapNextDay` handshake |
| **P1** | [`02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md`](02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md) | Dispersal Contract (Mirror) | `WD-01..48`, `SO_<DAY>_<FLOW>_I<n>_<BRANCH>`, day regimes, guards |
| **P1** | [`02-weekly-dispersal/ALGORITHM.md`](02-weekly-dispersal/ALGORITHM.md) | Solver Math Spec (Mirror) | `XP/TP/BP` scoring (`50/25/25`), rounding, Gaussian `w(Δt)`, `ALG-01..03` |
| **P1** | [`02-weekly-dispersal/EPICS-SCHEMA.md`](02-weekly-dispersal/EPICS-SCHEMA.md) | Entity Schema (Mirror) | 6-table `epics.json` model (`EPIC`, `BLOCK`, `CHUNK`, `NODE_PLACEMENT`, `SET_MEMBER`, `EDGE`) |
| **P1** | [`02-weekly-dispersal/ASSUMPTIONS-AND-DECISIONS-REGISTER.md`](02-weekly-dispersal/ASSUMPTIONS-AND-DECISIONS-REGISTER.md) | Active Register (Mirror) | Open cross-module questions (`AD-register`) and runtime verification status |
| **P1** | [`02-weekly-dispersal/log.md`](02-weekly-dispersal/log.md) | Closed Dispersal Log | Settled `DD-01..40` and `SEQ-D1..D4` engineering rulings |

---

## Section 4 — P2: Dispersal Data, Cockpit Compiler, Schemas & Fixtures

Inspect these scripts and JSON artifacts to verify live behavior before designing changes:

| Priority | Relative Path (`apexai-os-meta`) | Owner / Role | Key Content to Extract |
|:---:|---|---|---|
| **P2** | [`02-weekly-dispersal/week-blueprint.json`](02-weekly-dispersal/week-blueprint.json) | Canonical Clock (`T1`) | Sole timestamp owner (`Mon–Fri 08:00–24:00`, `Sat–Sun 12:00–16:00`, anchors) |
| **P2** | [`02-weekly-dispersal/week-demand.json`](02-weekly-dispersal/week-demand.json) | Operator Demand Dials | `M` shares/`focus_days`, `P` shares/`Knee` pin/evening courses, `C` priorities, `R` weights |
| **P2** | [`02-weekly-dispersal/epics.json`](02-weekly-dispersal/epics.json) | Epic/Block/Chunk DB | Live `P/M/R` drills and current single-chunk-per-Portfolio `C` placeholders |
| **P2** | [`02-weekly-dispersal/allocate_week.py`](02-weekly-dispersal/allocate_week.py) | `T2` Dispersal Solver | Shows current `P` Gaussian logic, `M` focus days, `R` rotation, hardcoded `c_portfolio_cycle` |
| **P2** | [`02-weekly-dispersal/week-allocation.json`](02-weekly-dispersal/week-allocation.json) | Compiled Solver Output | `240` slot allocations, `matrix2_pmr_bands`, projected `TP/XP/BP` summary |
| **P2** | [`02-weekly-dispersal/build_slot_inventory.py`](02-weekly-dispersal/build_slot_inventory.py) | `T1` Slot Generator | Builds `slot-inventory.json` from `week-blueprint.json` and `week-demand.json` |
| **P2** | [`02-weekly-dispersal/slot-inventory.json`](02-weekly-dispersal/slot-inventory.json) | Slot Geometry Output | `24` Flows, `240` canonical `slot_ids`, resolved `M/P` slot quotas |
| **P2** | [`01-weekly-command-brief/render_precap_cockpit.py`](01-weekly-command-brief/render_precap_cockpit.py) | Multi-Surface Compiler | `compute_dispersal_stats()`, `#s03` Matrix 2 cells, `#s05` Sequencing HTML, OKF brief loop |
| **P2** | [`01-weekly-command-brief/schemas/precap-week-cockpit.schema.json`](01-weekly-command-brief/schemas/precap-week-cockpit.schema.json) | Stage 1B Schema | Draft 2020-12 contract for Matrix 1 & Matrix 2 JSON cockpit inputs |
| **P2** | [`01-weekly-command-brief/schemas/presentation-handoff.schema.json`](01-weekly-command-brief/schemas/presentation-handoff.schema.json) | Handoff Schema | Contract linking `PrecapWeek` (`dispersal_owner`) to `PrecapNextDay` |
| **P2** | [`01-weekly-command-brief/fixtures/w46-reference-cockpit.json`](01-weekly-command-brief/fixtures/w46-reference-cockpit.json) | W46 Cockpit Fixture | Live ISO `2026-W46` cockpit dataset powering the current HTML |
| **P2** | [`01-weekly-command-brief/fixtures/w46-reference-handoff.json`](01-weekly-command-brief/fixtures/w46-reference-handoff.json) | W46 Handoff Fixture | Example `PRECAP-WEEK-HANDOFF-v2.1` envelope passed to `PrecapNextDay` |
| **P2** | [`01-weekly-command-brief/fixtures/w46-reference-weekly-command-brief.okf.md`](01-weekly-command-brief/fixtures/w46-reference-weekly-command-brief.okf.md) | W46 OKF Brief | Compiled `<100L` executive brief (`Sections 00–05` + handoff) |
| **P2** | [`01-weekly-command-brief/precap-week-cockpit-2026-W46.html`](01-weekly-command-brief/precap-week-cockpit-2026-W46.html) | Current HTML Cockpit | Baseline `v0.5` interactive cockpit rendered for operator visual review |

---

## Section 5 — P3: Runtime Skills, `PrecapNextDay` & Downstream `FlowRecap`

Consult these files when shaping weekly intake Q&A (`PrecapWeek`) and daily chunk hydration (`PrecapNextDay`):

| Priority | Relative Path (`apexai-os-meta`) | Owner / Role | Key Content to Extract |
|:---:|---|---|---|
| **P3** | [`../../../.claude/skills/PrecapWeek/SKILL.md`](../../../.claude/skills/PrecapWeek/SKILL.md) | `PrecapWeek` Skill Root | Weekly skill boundaries, modular spec routing, read-only calendar guard |
| **P3** | [`../../../.claude/skills/PrecapWeek/references/operator-weekly-command-brief-intake.md`](../../../.claude/skills/PrecapWeek/references/operator-weekly-command-brief-intake.md) | Stage 1A Q&A Guide | Adaptive intake flow where operator sets weekly sequencing dials |
| **P3** | [`../../../.claude/skills/PrecapWeek/calendar-planning-guidance.md`](../../../.claude/skills/PrecapWeek/calendar-planning-guidance.md) | Calendar Deformation | Meeting density tiers (`full/compressed/minimal/omitted`) and `Residual` deferral |
| **P3** | [`../../../.claude/skills/PrecapWeek/references/validation-checklist.md`](../../../.claude/skills/PrecapWeek/references/validation-checklist.md) | Weekly Quality Gates | Pre-output checks before presenting the HTML Cockpit and OKF Brief |
| **P3** | [`02-next-day-brief/README.md`](02-next-day-brief/README.md) | Module 02 Overview | Role of daily brief vs Flow Execution Cards and duplication avoidance |
| **P3** | [`02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`](02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md) | Daily Calendar Writer | `[APEX F#]` GCal write payload (`3x3` sprints + `DD-22A` bands) |
| **P3** | [`../../../.claude/skills/PrecapNextDay/SKILL.md`](../../../.claude/skills/PrecapNextDay/SKILL.md) | `PrecapNextDay` Skill Root | Daily execution modes, Flow card boundaries, anti-duplication contract |
| **P3** | [`../../../.claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md`](../../../.claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md) | Daily Intake Contract | Authority order, partial-input fallback, and conflict surfacing |
| **P3** | [`../../../.claude/skills/PrecapNextDay/references/daily-plan-output-contract.md`](../../../.claude/skills/PrecapNextDay/references/daily-plan-output-contract.md) | Daily Brief Contract | Required fields for tomorrow's overview and Flow routing |
| **P3** | [`../../../.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md`](../../../.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md) | Flow Card Template | Target `S1..S3` structure that will receive `epics.json` Chunks |
| **P3** | [`06-flow-recap/README.md`](06-flow-recap/README.md) | FlowRecap Interface | Post-Flow evidence format feeding next day's `PrecapNextDay` chunk state |
| **P3** | [`07-status-merge/README.md`](07-status-merge/README.md) | StatusMerge Interface | Weekly reconciliation closing the loop back to `PrecapWeek` |

---

## Section 6 — P4: Archived Sequencing Research (`apexai-os-meta`)

Reference only for historical UI variants and design principles; never promote unratified draft rules over Section 3–4 specs:

| Priority | Relative Path (`apexai-os-meta`) | Owner / Role | Key Content to Extract |
|:---:|---|---|---|
| **P4** | [`../../archive/weekly-orchestration/precap-week-research-2026-11/research/SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md`](../../archive/weekly-orchestration/precap-week-research-2026-11/research/SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md) | Capability Backlog | `Sequence` vs `Flow` definitions, multi-project sprint mixing ideas (`TODO`) |
| **P4** | [`../../archive/weekly-orchestration/precap-week-research-2026-11/research/Q13-THREE-SEQUENCING-VIEW-VARIANTS-20261106.html`](../../archive/weekly-orchestration/precap-week-research-2026-11/research/Q13-THREE-SEQUENCING-VIEW-VARIANTS-20261106.html) | Visual Prototype | Visual Option A/B/C exploration behind Section `05` calm orientation |
| **P4** | [`../../archive/weekly-orchestration/precap-week-research-2026-11/research/OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md`](../../archive/weekly-orchestration/precap-week-research-2026-11/research/OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md) | Decision Delta | Operator Q13 answers locking `PrecapWeek` vs `PrecapNextDay` depth split |
| **P4** | [`../../archive/weekly-orchestration/precap-week-research-2026-11/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](../../archive/weekly-orchestration/precap-week-research-2026-11/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) | Retired Monolith | Historical v2.0 spec superseded by modular Section 3 files (`D021`) |

---

## Section 7 — Cross-Repository Map (`leela-spec/MasterOfArts`)

`02-weekly-dispersal/` is a one-way mirror (`DD-15`) of upstream solver files in `leela-spec/MasterOfArts`. When both repositories are attached to the online chat, read these `MasterOfArts` paths directly:

- **`Sequencing/dispersal/`**: Upstream canonical home for `SPEC-WEEKLY-DISPERSAL.okf.md`, `ALGORITHM.md`, `EPICS-SCHEMA.md`, `epics.json`, `week-demand.json`, `allocate_week.py`, and `sync_dispersal.py`.
- **`Sequencing/decisions.md` & `Sequencing/index.md`**: Confirmed Sequencing project decisions (`N05`) and project router inside `MasterOfArts`.
- **`Sequencing/online-context/index.md` & `Sequencing/sources/definition-source-index.md`**: Core interleaving, spaced-repetition, chunking, and `Learn2Learn` source extracts (`D01–D08`).
- **Dispersal Reconciliation History (`PRECAP-INTEGRATION-ANALYSIS.md`)**: Read [`02-weekly-dispersal/PRECAP-INTEGRATION-ANALYSIS.md`](02-weekly-dispersal/PRECAP-INTEGRATION-ANALYSIS.md) inside `apexai-os-meta` for the `DD-19..DD-40` reconciliation.
