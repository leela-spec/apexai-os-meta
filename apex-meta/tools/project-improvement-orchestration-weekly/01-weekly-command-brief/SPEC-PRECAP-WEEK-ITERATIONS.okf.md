---
type: specification
id: SPEC-PRECAP-WEEK-ITERATIONS-v2.0
title: "Precap Week Iterations — Compact Cockpit, L1/L2 Goal Specification and Hourly Calendar"
description: "Operator-corrected cockpit design: five-card Portfolio Compass; collapsible three-card Operator Decisions; collapsible Matrix 1 with L1/L2 goals and six-field specification; single fit-to-width Mon-Sun hourly calendar sourced from week-blueprint.json; personal Mental/Physical/Regeneration priorities; residual information; Sequencing TODO."
status: current
date: 2026-11-11
scope: [weekly-orchestration, precap-week, matrix-1, matrix-2, task-spec, g-i-p-s-o-c, leela-stats]
tags: [weekly-orchestration, precap-week, specification, matrix-1, matrix-2, g-i-p-s-o-c, leela-stats]
---

# Precap Week Iterations Specification — Operator-Corrected Cockpit and Weekly Planning

## 1. Executive Summary & Core Architectural Invariants

This is the canonical **operator-verified specification** for the Precap Week cockpit (`v05` + `T1` `Mon–Sun` clock + **6-Portfolio Standard**). The `2026-11-09..11` operator locks replace recursive cube trees, `L3`, and supplemental calendar panels with section-level previews, `L1`/`L2` six-field goal detail (`EM-13` unified on `G|I|P|S|O|C`), one fit-to-width hourly timetable driven by [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json), the 5-card Portfolio Compass, and the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`).

### Core Architectural Invariants

- [P0 | I98/E95/R05] **00 · Head / Portfolio Compass**: Title `Precap Week · {{ISO_DATE_SPAN}}` with correctly computed ISO week number and dates, followed by five source-grounded summary cards (`1. Net Craft Capacity 36.0h C / 48.0h gross minus meetings`, `2. 24 Flows`, `3. 72 3×3 Craft Sprints`, `4. Active L1 Outcomes across the 6 Portfolio Areas`, `5. G1 Gate & Source Readiness`, visible by default; collapse optional). Do not inject duplicate `Weekly Target`, `Operator Agenda`, `Primary Data Source`, `Planned vs Realized`, or `Coverage` panels.
- [P0 | I97/E94/R06] **01 · Operator Decision Brief**: The entire section collapses. Its collapsed header keeps three horizontally arranged preview cards (`New`, `Ongoing`, `Standard`) displaying short `setting: current value` summaries. Expanding exposes full setting rows (`<details>` accordion); clicking a setting reveals details, `G1` status (`PROPOSED_FOR_G1 | APPROVED | CONFIRMED_INPUT`), and verified override proof (`{system_default, operator_choice, source_ref}`) without adding a separate redundant controls bar.
- [P0 | I97/E94/R06] **02 · Matrix 1 (Non-Temporal)**: The entire section collapses while keeping up to three highest-priority `L1` weekly goal cards visible in its own header. Expanded content stacks the **6 canonical Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) vertically, each with horizontal `L1 Priority Goals` (with inline `🔗 Cross-Repo:` dependency pills and `⚡` critical-path badges) and folded `L2 Nice-to-Haves` (`no L3`, zero sprints). Selecting any `L1` or `L2` card opens one full-width, single-line six-column `Goal | Input | Process | Skills | Output | Continuation` row directly beneath that goal strip—no recursive child-cube trees and no extra visible `Task Specification` heading; inside expanded `Goal` and `Output` cells, items decompose into `Tasks -> Subtasks` with short drafts/examples.
- [P0 | I96/E94/R08] **03 · Matrix 2 (Temporal)**: Preserve **one** fit-to-width **Monday–Sunday** hourly timetable (`08:00–24:00` weekday regime and `12:00–16:00` Saturday–Sunday weekend regime — same mechanism, reduced slot count) driven dynamically by [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) + `slot-inventory.json`, including `F1–F4` (with read-only `DD-22A` `P/M/R` bands), protected anchors, external commitments, evening `Project Night` (`Mon–Wed`) / `Freizeit` (`Thu–Fri`), `22:00–22:30` `Day Outro`, and `23:30–24:00` `Sleep Routine`. No horizontal scrollbar, duplicate Monday detail panel, extra saved-sprint table, or unsolicited summary-pill bar. Follow the last time row with a dedicated 3-column `Mental | Physical | Regeneration` focus strip (`1–3` operator priorities each or `not yet specified`, no project assignment).
- [P0 | I95/E92/R06] **04 · Residual Information**: Formal 4-card contract covering `(1) Clock & Capacity Reconciliation`, `(2) EM-13 & OpenProject Readiness Gaps`, `(3) Longlist Deferrals & Revisit Triggers` (blocked/future-phase items moved out of Matrix 1 `L2`), and `(4) 1-Hop Provenance & presentation_handoff`. Distinct from the `Residual` portfolio area.
- [P0 | I92/E90/R06] **05 · Sequencing Orientation**: Renders the **Dispersal Dials** (`week-demand.json` shares & `focus_days` across `M`, `P`, `R`, and the **6 Craft/Project Epics**: `Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`), Gaussian placement rules (`σ = 6.0h` around `19:00`, `w_max = 1.5x`), and projected `T2` `TP / XP / BP` breakdown from [`02-weekly-dispersal/`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/index.md).
- [P0 | I96/E95/R05] **Source Discipline**: Keep W45 planning examples historical. Never promote W45 work items, time allocations, scores, OpenProject references, or metric values into universal defaults. Missing fields stay explicitly unresolved rather than invented.
- [P0 | I96/E94/R06] **Canonical 6-Portfolio Standard (`06-PORTFOLIO`)**:
  1. **Leela** (`leela-game-flutter` / `leela-website` / `leela-spec` / OP #10): Skill Tree spatial node contracts, Chunk library, durable placement identity.
  2. **IPOS** (`IPOS` / OP #16): Financial advisory ingestion pipeline, Docling/Trafilatura seam, sovereign time-series visualization.
  3. **Master of Arts** (`MasterOfArts` / OP #14, #6, #7): Website content & responsive layout (`WP #163`), content production (`7` videos), and invoicing / automated PDF billing.
  4. **Apex AI** (`apexai-os-meta` / OP #8): OpenMouse kernel HID bindings (`WP #139`), mindful repository orchestration (`WP #198`), Dark Factory gate (`WP #222`).
  5. **Mindful Bar** (`leela-spec/mindful-bar` / `mindful-bar`): Cacao Bar functional product specification & validation (`v0.2`), ERPNext/Frappe architecture evaluation, and `systems/apex/` integration.
  6. **Residual**: Apartment & studio art, Sexy Content, Community & Travel, personal auxiliary rhythms & overflow recovery.

---

## 2. Linked Canonical Specifications & Authoritative Handovers

### Active v2.0 Extension & Research Handovers
1. **Task Spec Variable System, Symbols & OpenProject Sync (`2do`):**
   [`HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md) (`L1`/`L2` goal selection, six horizontal fields `Goal | Input | Process | Skills | Output | Continuation`, separate Input prerequisites and Continuation successors; OpenProject mapping pending).
2. **Operator Decision Brief UX Redesign:**
   [`HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md) (`New`/`Ongoing`/`Standard` whole-section collapse with visible preview cards, Mon/Wed Special Project Evenings, ambient holds, setting-level details).
3. **Header & Orchestration Stats Research (`2do` Grounded in Leela):**
   [`HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md) (historical Leela-derived metric candidates only; five visible Portfolio Compass metrics remain `OPERATOR_TODO`).
4. **Cross-Project Consolidated Dependency Research:**
   [`HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md) (Comparative bake-off evaluating dropping vs replacing the bottom Consolidated Process Dependency DAG).

### Foundation Specifications & Prior Handovers
5. **P1 OpenProject Dependency Intake Gate:** [`HANDOVER-20261106.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/00-openproject-dependency-intake/HANDOVER-20261106.okf.md) (Read-only OpenProject verification gate preceding live DAGs).
6. **Matrix 1 Foundation Handover (`v1.0`):** [`HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md).
7. **Matrix 2 Calendar Handover (`v1.0` — Validated):** [`HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md).
8. **Master Dual-Matrix Spec:** [`SPEC-DUAL-VIEW-WEEKLY-PRECAP.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md).
9. **Macro Orchestration Spine & Decision Gates:** [`02-MACRO-INTERFACES-AND-DECISION-GATES.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/00-orchestration-spine/02-MACRO-INTERFACES-AND-DECISION-GATES.md).
10. **Master Information Flow Critical Path:** [`MASTER-INFORMATION-FLOW-AND-DESIGN-CRITICAL-PATH-20261106.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/MASTER-INFORMATION-FLOW-AND-DESIGN-CRITICAL-PATH-20261106.okf.md).
11. **Governance Decisions Register:** [`DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md).

---

## 3. Operator Research Synthesis: Pre-Week Comprehension & Motivational Framing

Grounding from [`01_RESEARCH_FINDINGS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step4-operator-template-system/01_RESEARCH_FINDINGS.md), [`01-operator-output-design-principles.okf.yaml`](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml), and [`PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md) establishes what the human operator requires before a week begins:

### 3.1 Primary Operator Mission
The operator needs **calm, grounded clarity** and **tangible momentum**. Rather than wading through database IDs, verbose validation logs, or abstract multi-agent chatter, the operator must see:
* Exactly where each project stands in reality.
* What meaningful progress will be achieved by Sunday close.
* What decisions or approvals require human intervention.
* How the week fits realistically into the physical calendar without burnout.

### 3.2 The First 10 Seconds Motivational Contract (Principle D2)
The head of the brief must immediately communicate:
1. **Strategic Leverage & Excitement:** Clear, inspiring headlines stating what the week will accomplish.
2. **Current Grounded Baseline:** Verified truth from source commits and OpenProject.
3. **Weekly Direction:** The primary milestones to celebrate upon Sunday review.
4. **Immediate Human Action:** The single choice or confirmation required to unlock execution.

### 3.3 Core Presentation Principles
- **Decision Before Detail (D1):** Governance decisions, trade-offs, and critical path gates are presented first. Deeper task decompositions are progressively disclosed.
- **Value Over Machinery (D3):** Focus on human, user-facing, and operational deliverables. Internal test suites and lint runs are background evidence, never primary headlines.
- **Planning Is Directional, Not Executable:** Precap Week establishes directional allocation and capacity balance. Detailed intra-day sprint cards, prompt packets, and executable micro-steps remain strictly with `PrecapNextDay` (`J3`/`J4`).
- **Matrix 1 Contains No Sprints:** Sprints belong strictly in Matrix 2. Matrix 1 visualizes project mechanics, outputs, and dependencies.

---

## 4. Sections 00 & 01 — Portfolio Compass and Operator Decision Brief

The Operator Decision Brief acts as a calm executive control panel rather than a wall of decision essays. Detailed specification lives in [`HANDOVER-04`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md) and candidate stats research lives in [`HANDOVER-05`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md).

### 4.1 Section 00 — Header and Portfolio Compass
* Title: `Precap Week · {{ISO_DATE_SPAN}}` with correctly computed ISO week number; do not use the erroneous W45 label for 09–15 November 2026 (ISO W46).
* Five visually consistent summary cards are immediately visible inside `Portfolio Compass` by default (section-level collapse optional):
  1. **`Net Craft Capacity (T1)`** (`36.0h` pure Craft `C` / `48.0h` gross across `24` Flows, minus verified fixed calendar collisions, with `72m` trailing `recap_min` accounted inside the `12.0h` non-Craft budget).
  2. **`Total Weekly Flows`** (`24` nominal `120m` Flows = `20` weekday `Mon–Fri` + `4` weekend `Sat–Sun`).
  3. **`3×3 Craft Sprints`** (`72` × `30m C` sprints across the week).
  4. **`6 Portfolio Areas & Active L1 Scope`** (`6` Portfolio Areas: **`Leela`**, **`IPOS`**, **`Master of Arts`**, **`Apex AI`**, **`Mindful Bar`**, **`Residual`**, plus active `L1` outcome count).
  5. **`G1 Gate & Source Readiness`** (`G1` approval state, verified overrides, OpenProject / Google Calendar status).
* Historical numbers from W45 may be shown as `historical / source-reported`, never as verified current metrics.
* Do not place a duplicate `Weekly Target`, `Operator Agenda`, or `Primary Data Source` card above or beside the Compass. Strategic goals belong to Matrix 1, evidence metadata to Section `04` or contextual detail.

### 4.2 Section 01 — Collapsible Operator Decision Brief

The section-level summary is always legible and renders three compact side-by-side category **cards** in this exact order:

`[ NEW: setting: current value ]  [ ONGOING: setting: current value ]  [ STANDARD: setting: current value ]`

- With the section collapsed, each category card lists concise factual previews; it is not an empty heading or a tag-only control.
- Expanding `01` exposes the full settings lists for all three categories (`<details>` inline accordion, zero extra toolbar). Each setting is `Variable: Active Value`; selecting it reveals explanation, provenance, `G1` status (`PROPOSED_FOR_G1 | APPROVED | CONFIRMED_INPUT`), and verified `{system_default, operator_choice, source_ref}` proof.
- `New`: weekly changes, topic routing, scope changes, verified operator overrides, and weekly theme overrides on the `Mon–Wed Project Night` baseline.
- `Ongoing`: carried initiatives, verified calendar commitments, and ignored ambient calendar holds (e.g., `WC Meister` ignored hold, `München Tanz` protected external event).
- `Standard`: standing OpenProject intake logic, `3×3` Flow/Sequencing baselines, and daily clock boundaries sourced from [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) (`Mon–Sun`, `08:00–24:00` weekday with `Mon–Wed Project Night 20:30–22:00`, `Thu–Fri Freizeit 20:30–22:00`, and `22:00–22:30` `Day Outro`; `12:00–16:00` weekend regime; Sunday no longer OFF by default).
- An `OPERATOR OVERRIDE` label appears only where source evidence shows an actual default-to-operator difference (`{system_default, operator_choice, source_ref}`). Do not manufacture an override.
- One-click collapse of the **whole** `01` section hides all expanded settings without erasing the three preview cards.

---

## 5. Section 02 — Matrix 1: Collapsible Portfolio Goals (Non-Temporal)

The complete Matrix 1 **body** folds under one section-level control. Even while folded, the `02` header keeps up to three highest-priority weekly **goal cards** visible as previews, chosen from the plan's actual priority order. This is a responsive preview, not three mandatory goals for every project. Cards display human-readable goal titles; technical IDs belong in expanded metadata. Matrix 1 contains **zero calendar times and zero sprints**.

### 5.1 Project and Level Layout
1. On expansion, the **6 canonical Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) stack in a single full-width vertical column.
2. Each portfolio area displays **L1 Priority Goals** side-by-side from left to right in actual weekly execution/priority sequence. The row uses available width, with compact cards allowed; no arbitrary max-one-or-two limit.
3. **L2 Nice-to-Haves** sits immediately below `L1` and starts folded. Opening `L2` reveals its own side-by-side cards (actionable secondary candidates only; blocked/future-phase items move to `Longlist Deferred` in Section `04`), with the identical selection and detail behavior as `L1`.
4. **No L3**. Matrix 1 UI cards stay strictly `L1 / L2` (no `L3` cubes), while inside expanded `Goal` and `Output` cells items decompose into `Tasks -> Subtasks` with short drafts/examples.
5. A project title and status may remain as lightweight metadata; do not render bulky outcome banners, technical ID columns, or redundant priority indicators.

### 5.2 Goal Selection and Expanded Data (Both L1 and L2)
- Selecting a goal card unfolds one specification row **directly beneath that goal-card strip**. No extra visible `Task Specification`, `Test Specification Process`, or other heading bar is placed above it.
- Exactly six fields render **left to right on one screen-width line** (`EM-13` unified on `G | I | P | S | O | C`): `Goal | Input | Process | Skills | Output | Continuation`. Each takes an equal or content-responsive share of the available width; long content wraps within its field. On narrow viewports reflow cleanly without horizontal overflow.
- `Goal`: concrete outcome, observable `acceptance` evidence, and `Tasks -> Subtasks` decomposition with short drafts/examples, not a generic project title.
- `Input`: actual named `sources` in priority order, separately identified `upstream_dependencies`, and explicit `exclusions`. Missing paths/IDs remain unresolved.
- `Process`: source-supported ordered work/method and the verification steps, not an invented generic framework.
- `Skills`: actual registered skill IDs where verified; proposed/unverified capabilities marked explicitly.
- `Output`: concrete `deliverable` artifacts, `redraft` (short drafts/examples), and `Tasks -> Subtasks` output structure; file paths only when grounded.
- `Continuation`: `downstream` consumer, actual successor or unblocked work package, and handoff location where known.
- Preserve the parent project context without duplicating it inside every field. Do not suppress the `Goal` field itself.
- Do **not** add recursive child-cube trees. Arrows and inline `🔗 Cross-Repo:` pills represent only verified material dependency edges; parallel goals have none.
- Goal IDs may be exposed in expanded detail or on request, never as the primary human-facing card text.

### 5.3 Collapsed and Expanded Sketch

```text
02 · MATRIX 1 — PROJECT GOALS  [Goal A] [Goal B] [Goal C]  [Expand/Collapse]
    (collapsed: up to three preview goal cards remain visible; nothing else shows)

    (expanded across 6 Portfolio Areas: Leela, IPOS, Master of Arts, Apex AI, Mindful Bar, Residual)
    PROJECT: Master of Arts
    L1  [7 Produced Videos] [Website Content Draft] [⚡ Automated PDF Billing 🔗->IPOS]
             (click selected goal; order follows verified weekly priority)
        [ Goal (Outcome+Acceptance+Tasks->Subtasks) ] [ Input (Sources+Deps+Exclusions) ] [ Process ] [ Skills ] [ Output (Deliverable+Redraft+Tasks->Subtasks) ] [ Continuation ]
    L2  [Nice-to-Haves: collapsed; expand to same card + six-field interaction]
    PROJECT: Leela / IPOS / Apex AI / Mindful Bar / Residual ...
```

### 5.4 Goal-Card Content
Visible by default: outcome title, optional `⚡` critical-path cue, inline `🔗 Cross-Repo:` dependency pills (`Option B`), and short human-readable state/priority context. Move opaque OpenProject IDs and system provenance to expanded detail. Do not invent a completed state, priority, or critical-path link simply for presentation.

### 5.5 Cross-Project Dependency Pills (`Option B` Ratified)

The bottom standalone Mermaid `Consolidated Cross-Repo Critical Path & Process Dependency DAG` from `v1.2` is **retired** per [`HANDOVER-06`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md). Cross-repo dependencies render directly on `L1` goal cubes via inline clickable **`🔗 Cross-Repo:` pills** (plus `⚡` critical-path badges). Do not render multi-subgraph bottom Mermaid charts.

---

## 6. Section 03 — Matrix 2: Calendar Snapshot & Visualization (Temporal)

Matrix 2 maps the selected work packages from Matrix 1 across the calendar days, respecting verified appointments, routine anchors, and focus capacity.

### 6.1 Daily Time Geometry & Operating Windows

* **Single Canonical Clock Owner:** [`02-weekly-dispersal/week-blueprint.json`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) is the **sole owner** of all weekly start/end clock timestamps. Do not duplicate its full schedule table here; `build_slot_inventory.py`, `render_blueprint.py`, and `PrecapWeek` read `week-blueprint.json` directly.
* **Weekday Regime (`Mon–Fri`, `08:00 – 24:00`, `960 min`):** Four `120m` Flows (`20` weekday Flows total), protected life/meal/admin anchors, `18:30–19:30` Evening Physical Course / VWC (outside the `72×2m` in-Flow `P` quota; `DD-39`/`DD-40` resolved), `20:30–22:00` Project Night (`Mon–Wed`) or `Freizeit` (`Thu–Fri`), and **Day Outro** at `22:00–22:30`.
* **Weekend Regime (`Sat–Sun`, `12:00 – 16:00`, `240 min`):** Two adjacent `120m` Flows (`F1` `12:00–14:00`, `F2` `14:00–16:00`; `4` weekend Flows total). Both Saturday and Sunday run the weekend regime (`24` Flows/week total = `20` weekday + `4` weekend; `240` unique `slot_id`s: `72 P + 72 M + 72 C + 24 R`).

### 6.2 External Calendar Meeting Collision Handling
- Existing external Google Calendar events take absolute non-destructive priority unless explicitly overridden by an operator decision.
- **Operator Decision Override:** The operator may explicitly elect to ignore or decline specific meetings (e.g. Meister meetings ignored for Week 45), freeing up evening focus blocks.
- Schedulable focus flows flex around active verified appointments.

### 6.3 One Full-Width Hourly Week Timetable

Render **one** legible time-of-day timetable across **Monday–Sunday** (`08:00–24:00` weekday regime + `12:00–16:00` Saturday–Sunday weekend regime), driven dynamically from [`02-weekly-dispersal/week-blueprint.json`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json), containing `F1–F4`, routine anchors, breaks, relevant external commitments, evening `Project Night` / `Freizeit`, `22:00–22:30` `Day Outro`, and `23:30–24:00` `Sleep Routine`. It must fit the available viewport width: no `min-width` forcing horizontal scroll, no bottom horizontal scrollbar. Allow text wrapping and compact cell typography; at narrow widths reflow cleanly without horizontal overflow while preserving all weekday/weekend data. Detailed sprint information belongs inline within existing timetable cells on click/inspection rather than creating a second Monday details panel or an additional `full saved sprint-by-day table`.

```html
<!-- Block sequence and exact timestamps are loaded dynamically from 02-weekly-dispersal/week-blueprint.json. -->
<div class="calendar-viewport" style="width:100%; overflow-x:visible; margin:20px 0;">
  <table style="width:100%; table-layout:fixed; overflow-wrap:anywhere; border-collapse:collapse; font-size:12px; border:1px solid #dce4e8; background:#fffdf8;">
    <thead>
      <tr style="background:#162642; color:#fff;">
        <th style="width:12%; padding:10px; border:1px solid #2a3e5c;">Window / Flow</th>
        <th style="width:6%; padding:10px; border:1px solid #2a3e5c;">Sprint</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Monday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Tuesday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Wednesday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Thursday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Friday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Saturday (Weekend Regime)</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Sunday (Weekend Regime)</th>
      </tr>
    </thead>
    <tbody>
      <!-- Weekday (4 Flows + anchors, 08:00-24:00) and Weekend (2 Flows, 12:00-16:00) rows bound from week-blueprint.json -->
      <tr style="border-top:2px solid #507967;">
        <td rowspan="3" style="padding:10px; vertical-align:top; background:#f5f8f5;">
          <b style="color:#2a5035;">Flow {{N}} (2h · 120m)</b><br>
          <span style="font-size:10px; color:#687b8b;">{{FLOW_START}}–{{FLOW_END}}</span><br>
          <span style="font-size:11px; font-weight:700;">{{FLOW_THEME}}</span>
        </td>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 1</td>
        <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <b>{{TASK_A_TITLE}}</b>
          <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
            <li>1. {{ITEM_1}}</li>
            <li>2. {{ITEM_2}}</li>
            <li>3. {{ITEM_3}}</li>
          </ul>
        </td>
        <td colspan="6" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <em>Sprint allocations dynamically populated per day from week-blueprint.json &amp; slot-inventory.json</em>
        </td>
      </tr>
      <tr>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 2</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <em>Sprint 2 items (minimum 3 actionable subtasks)</em>
        </td>
      </tr>
      <tr style="border-bottom:2px solid #507967;">
        <td style="padding:6px; text-align:center; font-weight:700;">Sprint 3</td>
        <td colspan="7" style="padding:6px; vertical-align:top;">
          <em>Sprint 3 items (minimum 3 actionable subtasks)</em>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

### 6.4 Below-the-Timetable Personal Orientation

Immediately **below the final `23:30–24:00` (`Sleep Routine`) time row**, render one full-width horizontal focus strip with three equal areas: `Mental`, `Physical`, and `Regeneration`. Each area holds a **bullet list of 1–3 operator-selected priorities**. These are personal-focus priorities—never projects, work packages, flow assignments, or measurable deliverables. Never fabricate priorities from W45 project content; show `not yet specified` when unsupplied, and preserve all canonical `08:00–24:00` time rows above.

### 6.5 Remove Unrequested Secondary Controls

Forbidden below or around Matrix 2: a secondary expanded Monday details panel (`#flowdetail`), a separate day-role summary card strip (`#daystrip`), a second `Full saved sprint-by-day table`, independent day-summary pill bars (`.displayrow`), redundant legend/meeting buttons, and horizontal scrollbars (`min-width` overflows). The hourly timetable is the single visible calendar surface; removing duplicate UI must not delete underlying canonical data.

---

## 7. Section 04 — Residual Information Contract

Section `04 · Residual Information` renders a structured 4-card grid (`2×2` on desktop, `1`-col on mobile) without duplicating Matrix 1 goal cards, the Matrix 2 calendar, or Section `00`/`01` control surfaces (distinct from the `Residual` portfolio area):
1. **`Clock & Capacity Reconciliation`**: `T1` `week-blueprint.json` gross (`2,880m` / `48.0h`) vs pure Craft (`2,160m` / `36.0h`) vs `P/M/R/recap` (`720m` / `12.0h` including `72m` trailing `recap_min`), plus verified external meeting subtractions and commute buffers (e.g., `Alex & Chris` `10:00–11:00`, `München Tanz` `18:45–21:00` w/ `18:15` transition buffer).
2. **`EM-13 & OpenProject Readiness Gaps`**: Unified `EM-13` (`G|I|P|S|O|C`) field completeness, OpenProject status-vs-description audit findings, and `[OP-OFFLINE]` / `[OP-UNRESOLVED]` provenance markers.
3. **`Longlist Deferrals & Revisit Triggers`**: Blocked or future-phase backlog items moved out of Matrix 1 `L2 Nice-to-Haves` (e.g., `WP #204 ACIM Credits`, `Stripe webhook`, `WP #227 Telegram digest`) with explicit deferral reason and revisit trigger.
4. **`1-Hop Provenance & Downstream Handoff`**: Source freshness ledger and the single embedded `presentation_handoff` pointer to `PrecapNextDay`.

---

## 8. Section 05 — Sequencing Orientation (`02-weekly-dispersal/`)

Section `05 · Sequencing Orientation` displays the weekly Dispersal Engine dials and `T2` allocation summary grounded in [`02-weekly-dispersal/week-demand.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-demand.json), `epics.json`, and `week-allocation.json`:
1. **Branch & Epic Shares (`WD-40` Across 4 Branches)**:
   - **`Mental (24 slots / 120m)`**: `Intention` (`focus_days`), `ACIM`, `Surrender`, `Breathing`.
   - **`Physical (72 slots / 144m)`**: `Martial Arts`, `Dance`, `S/BJJ`, `General`, `Knee` (pinned to `*_*_I3_P`).
   - **`Regeneration (72 in-Flow + 14 routine/break slots / 456m)`**: `Yoga Nidra`, `Audiobooks`, `Socializing` (`XP = 0`, `DD-16` no numeric BP floor).
   - **`Craft / Projects (72 slots / 2,160m across the 6 Portfolio Areas)`**: **`Leela`**, **`IPOS`**, **`Master of Arts`**, **`Apex AI`**, **`Mindful Bar`**, and **`Residual`**.
2. **Gaussian Focus-Day Weighting (`T2`)**: `σ = 6.0h` centered on `19:00` (`1140m`) of each `focus_day` (`w_max = 1.5x`, no Fri→Sat bleed).
3. **Sequence-Arc Summary & Projected `TP / XP / BP`**: Displays the `Q13` Sequence-Arc overview (`Sequence` `M04` broader than a single `Flow`, while mixed-project `C1/C2/C3` sprints are permitted when capacity compression requires) and projected `TP`, `XP`, and structural `BP` (`50/25/25`).

---

## 9. Downstream Consumer Contract: PrecapNextDay Handshake

Precap Week concludes with an embedded YAML `presentation_handoff` block consumed with zero token waste by `PrecapNextDay`:

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  specification_version: "SPEC-PRECAP-WEEK-ITERATIONS-v2.1"
  produced_at: "2026-11-11T00:00:00Z"
  operator_g1_status: "APPROVED"
  week: "{{ACTIVE_ISO_WEEK}}"
  timezone: "Europe/Berlin"
  clock_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
  source_status:
    openproject: "ONLINE | OFFLINE_FALLBACK"
    google_calendar: "ONLINE | OFFLINE_FALLBACK"
  six_portfolio_areas:
    - portfolio_id: "leela"
      label: "Leela"
      priority_goals: ["Skill Tree Spatial Node Contracts & Freeze Gate"]
      selected_work_refs: ["OP-WP#159", "OP-WP#39", "OP-WP#48"]
    - portfolio_id: "ipos"
      label: "IPOS"
      priority_goals: ["Full Pipeline Recheck & Sovereign Data Visualization Over Time"]
      selected_work_refs: ["OP-WP#224", "OP-WP#226", "OP-WP#228"]
    - portfolio_id: "master_of_arts"
      label: "Master of Arts"
      priority_goals: ["Website Content Draft", "7 Produced Videos", "Automated PDF Billing"]
      selected_work_refs: ["OP-WP#163"]
    - portfolio_id: "apex_ai"
      label: "Apex AI"
      priority_goals: ["OpenMouse Kernel HID Binding", "Mindful Repo Orchestration & Dark Factory Gate"]
      selected_work_refs: ["OP-WP#139", "OP-WP#198", "OP-WP#222"]
    - portfolio_id: "mindful_bar"
      label: "Mindful Bar"
      priority_goals: ["Cacao Bar Functional Product Spec v0.2 & Validation", "ERPNext/Frappe Architecture Evaluation"]
      selected_work_refs: ["mindful-bar:spec-v0.2", "mindful-bar:erp-eval"]
    - portfolio_id: "residual"
      label: "Residual"
      priority_goals: ["Mon-Wed Project Night Themes (Sexy Content, Dance/Martial Arts)", "Studio Art & Travel Sync"]
      selected_work_refs: ["residual:studio-art", "residual:sexy-content", "residual:community-travel"]
  operating_geometry:
    week_span: "monday_to_sunday"
    weekday_window: "08:00-24:00"
    project_night_window: "Mon-Wed 20:30-22:00"
    freizeit_evening_window: "Thu-Fri 20:30-22:00"
    day_outro: "22:00-22:30"
    weekend_window: "12:00-16:00"
    reconciled_calendar_events: []
    capacity_deformations_and_omissions: []
  next_consumer: "PrecapNextDay"
```

---

## 10. Failure Guards & Acceptance Tests for Current Operator Design

- [x] **UX-00:** Portfolio Compass starts open with the 5 locked source-grounded metric cards (`Net Craft Capacity`, `24 Flows`, `72 Craft Sprints`, `6 Portfolio Areas & Active L1 Scope`, `G1 Gate & Source Readiness`); no `Weekly Target`, `Operator Agenda`, `Primary Data Source`, `Coverage`, or `Planned vs Realized` duplicate surface is injected.
- [x] **UX-01:** `01` is fully collapsible. With body closed, `New / Ongoing / Standard` remain visible as three compact side-by-side cards displaying `setting: value` previews; with body open, each setting can independently reveal details, `G1` status, and verified override proof.
- [x] **UX-02:** `02` is fully collapsible. With body closed, up to three highest-priority `L1` goal cards remain visible in its own header; all per-project rows across the 6 Portfolio Areas are hidden. No isolated `L1`-only collapse substitutes for section collapse.
- [x] **UX-03:** Expanded Matrix 1 stacks the **6 Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) and has only `L1` and folded `L2`, each using a horizontal goal-card row. Selecting either category's goal reveals one directly-below six-field (`Goal | Input | Process | Skills | Output | Continuation`) horizontal row with `Tasks -> Subtasks` and short drafts/examples inside `Goal` and `Output`, zero extra heading, and zero recursive child tree.
- [x] **UX-04:** Human-readable goal title dominates the card; inline `🔗 Cross-Repo:` pills (`Option B`) and `⚡` critical-path badges appear on `L1` cards; OpenProject IDs remain secondary metadata and are never invented.
- [x] **UX-05:** `03` has exactly one fit-to-width **Monday–Sunday** hourly timetable grounded in [`week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) (`08:00–24:00` weekday + `12:00–16:00` weekend `F1–F4`, read-only `DD-22A` `P/M/R` bands, anchors, `Day Outro 22:00–22:30`), without a second `#daystrip`/`#flowdetail` panel, saved sprint table, extra `.displayrow` pills, or horizontal scrollbar (`scrollWidth <= clientWidth`).
- [x] **UX-06:** Directly under the final `23:30–24:00` timetable row, the `Mental | Physical | Regeneration` strip shows `1–3` operator-specified bullet priorities per category, or explicit `not yet specified` state.
- [x] **UX-07:** `04` renders the 4-card Residual Information contract without duplicated project/calendar panels; `05` renders the Sequencing Orientation panel (`week-demand.json` dials across 4 branches + 6 Craft Epics, Gaussian `σ=6.0h`, and `T2` `TP/XP/BP` summary).
- [x] **CONTRACT-01:** `G/I/P/S/O/Continuation` values are sourced or explicitly unresolved (`EM-13` unified on `G|I|P|S|O|C`, `Goal.acceptance`, `Input.exclusions`, `Output.redraft` included). Upstream dependencies in `Input` remain distinct from downstream successors in `Continuation`.
- [x] **EVAL-01:** Exercise section collapse, preview persistence, `L1`/`L2` selection, 6-field row visibility, timetable fit at desktop and narrow widths, and personal-focus strip using the W45/W46 fixture (`scrollWidth <= clientWidth`).
