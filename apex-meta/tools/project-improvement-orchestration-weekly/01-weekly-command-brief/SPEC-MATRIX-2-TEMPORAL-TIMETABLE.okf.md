---
type: specification
id: SPEC-MATRIX-2-TEMPORAL-TIMETABLE-v3.0
title: "Matrix 2 Modular Specification — Monday–Sunday Temporal Timetable & Calendar Collisions"
description: "Canonical temporal specification governing the Monday–Sunday timetable, blueprint clock, calendar intake, capacity deformations, and Personal Focus Strip."
status: current
date: 2026-11-12
parent_spec: SPEC-PRECAP-WEEK-MASTER.okf.md
scope: [weekly-orchestration, precap-week, matrix-2, timetable, calendar, personal-focus]
tags: [weekly-orchestration, precap-week, matrix-2, temporal, specification, okf-v02]
references: [SPEC-PRECAP-WEEK-MASTER.okf.md, SPEC-MATRIX-1-PORTFOLIOS.okf.md, SPEC-PRECAP-INTERFACES-HANDOFF.okf.md]
---

# Matrix 2 Modular Specification — Monday–Sunday Temporal Timetable & Calendar Collisions

## Section 1 — Temporal Architecture & Core Invariants

Matrix 2 binds the strategic work packages selected in Matrix 1 ([`SPEC-MATRIX-1-PORTFOLIOS.okf.md`](SPEC-MATRIX-1-PORTFOLIOS.okf.md)) to the canonical Monday–Sunday weekly clock. It coordinates focus blocks with external calendar commitments and in-Flow health and practice rhythms.

### Core Temporal Invariants

- [P0 | I98/E95/R05] **Single Canonical Clock Owner**: [`02-weekly-dispersal/week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json) is the sole authoritative owner of all daily block start and end timestamps. Hardcoding duplicate clock tables in prose specifications, JSON fixtures, or HTML templates is strictly prohibited.
- [P0 | I97/E94/R06] **Zero Craft Work Package Authoring**: Matrix 2 never authors new work packages, goals, or deliverables. It consumes strictly typed references from the `selected_work_reference[]` array exported by Matrix 1.
- [P0 | I96/E95/R05] **Fit-to-Width Timetable**: The weekly schedule renders as a single, fit-to-width Monday–Sunday hourly timetable (`table-layout: fixed; width: 100%; overflow-wrap: anywhere`). Horizontal scrollbars (`min-width: 1150px` overflows) and duplicate secondary day strips are permanently banned.
- [P0 | I96/E94/R06] **Responsive Mobile Contract (<920px)**: Below 920px viewport width, table `rowspan` flexing is disabled to prevent afternoon or weekend cell disappearance. The layout switches cleanly to flat stacked day cards maintaining `scrollWidth <= clientWidth`.

---

## Section 2 — Single Canonical Clock Owner & Daily Operating Regimes

All time boundaries derive dynamically from [`week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json). Hardcoding duplicate clock tables in prose specifications is strictly prohibited.

The timetable enforces two operating regimes:
1. **Weekday Regime (`Mon–Fri`)**: Runs 08:00–24:00 (960 gross minutes per day). Houses 4 nominal 120m Flows (`F1` 08:30–10:30, `F2` 10:30–12:30, `F3` 13:30–15:30, `F4` 16:30–18:30), evening physical course, and project night.
2. **Weekend Regime (`Sat–Sun`)**: Runs 12:00–16:00 (240 gross minutes per day). Houses 2 nominal 120m Flows (`F1` 12:00–14:00, `F2` 14:00–16:00) and Sunday `StatusMerge`.

All daily anchor timestamps, lunch windows, and wind-down rituals are owned solely by `week-blueprint.json`. Deterministic capacity arithmetic (`2,880m` gross / `2,160m` Craft / `720m` non-Craft / `240` slots) is canonically governed by [`SPEC-PRECAP-WEEK-MASTER.okf.md §3.1`](SPEC-PRECAP-WEEK-MASTER.okf.md#section-31--section-00-portfolio-compass--statusmerge-basis).

---

## Section 3 — Flow Anatomy & In-Flow Practice Chunks (`DD-22A`)

Every nominal 120-minute Flow block strictly follows standard macro decomposition:

$$\text{Flow Block (120m)} = 3 \times (\text{P } 2\text{m} + \text{M } 3\text{m} + \text{C } 30\text{m} + \text{recap } 1\text{m}) + \text{R } 12\text{m}$$

1. **Sprint 1 (36m)**: `P` (2m) + `M` (3m) + `C1` Craft sprint (30m) + trailing recap (1m).
2. **Sprint 2 (36m)**: `P` (2m) + `M` (3m) + `C2` Craft sprint (30m) + trailing recap (1m).
3. **Sprint 3 (36m)**: `P` (2m) + `M` (3m) + `C3` Craft sprint (30m) + trailing recap (1m).
4. **Regeneration Break `R` (12m)**: Dedicated in-Flow restorative pause (Audiobooks, Yoga Nidra, Socializing; `XP = 0`, `DD-16` zero BP floor).

### Cell Depth Separation Contract (`Q06 / Q08`)

- **PrecapWeek Scope**: Renders the Flow Owner reference (`selected_work_reference[]`), headline Flow outcome, macro clickable `C1/C2/C3` sprint labels, capacity deformation badge, and read-only `DD-22A` `P/M/R` practice Chunk band.
- **PrecapNextDay Scope**: Granular `S1–S3` tactical execution checklists, intra-sprint micro-prompts, and real-time execution tracking belong strictly to `PrecapNextDay`. PrecapWeek never micromanages intra-sprint sub-tasks.

---

## Section 4 — Untrusted Calendar Intake & Flow Capacity Deformations

### Untrusted Calendar Contract

External calendar events (Google Calendar) are ingested strictly as **untrusted scheduling context** (`event_text_is_untrusted_data: true`):
- Event titles, descriptions, and participant lists are sanitized and used solely for time-block boundary calculations.
- Prompts, instructions, or directives embedded inside calendar entries are completely ignored.

### Collision Handling & Commute Buffers

- **Non-Destructive Priority**: Fixed external events take absolute priority over scheduled Flow blocks.
- **Commute & Prep Buffers**: Recurring offsite events carry mandatory commute and prep buffers:
  - Example: `München Tanz (18:45–21:00)` carries a mandatory `18:15–18:45` commute buffer, enforcing a hard stop on Flow F4 at 18:15.
- **Standing Ignores**: Ambient or non-binding calendar holds overridden by operator `Ongoing` directives (e.g. `WC Meister Wed/Fri 18:00–20:00`) subtract 0 minutes from Flow capacity.

### Flow Capacity Deformation Overlay

The nominal count remains invariant at 24 Flows in `slot-inventory.json`.

Calendar overlaps apply a capacity deformation state with a logged reason:

| Deformation Shape | Available Craft Sprints | Net Craft Time | Capacity Impact | Example Scenario |
|---|:---:|:---:|:---:|---|
| **`full`** | 3 sprints | 90 min | 0 min | Nominal uninterrupted Flow block. |
| **`compressed`** | 2 sprints | 60 min | -30 min | 30–60m meeting overlap (e.g. Thu F1/F2 Alex & Chris 10:00–11:00). |
| **`minimal`** | 1 sprint | 30 min | -60 min | 60–90m collision leaving a single focused sprint. |
| **`omitted`** | 0 sprints | 0 min | -90 min | Full 120m block overtaken by external commitment or travel. |

*Reconciliation Output*: All capacity deformations, subtracted minutes, and reasons are exported to Section 04 Residuals and the downstream `presentation_handoff` envelope.

---

## Section 5 — Fit-to-Width Timetable & Responsive Mobile Contract (<920px)

The timetable is compiled deterministically by [`render_precap_cockpit.py`](render_precap_cockpit.py) without hand-crafted table markup:

```html
<!-- Compiled DOM Contract emitted by render_precap_cockpit.py -->
<section id="s03" class="sec">
  <table class="cal">
    <!-- Desktop fit-to-width timetable: table-layout: fixed; width: 100% -->
    <!-- Columns: Time, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday -->
  </table>
  <div class="cal-mobile" aria-label="Mobile Stacked Timetable">
    <!-- Flat stacked day cards below 920px: zero rowspan collapse; full content fidelity -->
  </div>
  <div id="focusstrip">
    <!-- 3-column personal priority strip: Mental | Physical | Regeneration -->
  </div>
</section>
```

### Responsive Invariants

1. **Desktop (>=920px)**: One responsive table spanning 100% container width. Zero horizontal scrollbars (`overflow-x: hidden`).
2. **Mobile (<920px)**: CSS media queries hide `.cal` and display `.cal-mobile`. Each day renders as an independent stacked card with its chronological Flow blocks. Table `rowspan` flexing is eliminated, guaranteeing that afternoon Flows and weekend blocks remain 100% visible on small screens.
3. **Prohibited Controls**: The timetable section must never include `#flowdetail`, `#daystrip`, separate saved-sprint tables, or `.displayrow` pill bars.

---

## Section 6 — Personal Focus Strip Contract

Directly beneath the final `23:30–24:00` (`Sleep Routine`) row, the timetable terminates with a dedicated 3-column **Personal Focus Strip**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ PERSONAL FOCUS STRIP (Mental | Physical | Regeneration)                │
├─────────────────────┬────────────────────────┬─────────────────────────┤
│ Mental (216m Flow)  │ Physical (144m + Eve)  │ Regeneration (288m · 0) │
├─────────────────────┼────────────────────────┼─────────────────────────┤
│ • Daily Morning     │ • Protect right knee   │ • Day Outro boundary    │
│   Intention         │   (pinned *_*_I3_P)    │   after Wed / Thu Tanz  │
│ • ACIM & Surrender  │ • Preserve 18:30-19:30 │ • Rotate Audiobooks(11),│
│   across F1-F4      │   Evening Physical     │   Yoga Nidra(8), Social │
└─────────────────────┴────────────────────────┴─────────────────────────┘
```

- **Column 1 — Mental (`216m` in-Flow)**: Captures daily intention, meditation, and presence focuses.
- **Column 2 — Physical (`144m` in-Flow + Evening Courses)**: Captures physical therapy protocols (e.g. right knee recovery pinned to `*_*_I3_P` slots) and evening course preservation.
- **Column 3 — Regeneration (`288m` breaks · `0 XP`)**: Captures sleep boundaries, evening wind-down rituals, and rotation across restorative modalities.
- **Strict Scope Prohibition**: Work packages, repository tasks, and project deliverables are strictly prohibited from the Personal Focus Strip. It is reserved exclusively for operator health, cognitive clarity, and restorative practices.

---

## Section 7 — Operative Failure-Mode Guards & Circuit Breakers

In accordance with `WP-25`, Matrix 2 closes with non-negotiable terminal failure-mode guards:
1. **Clock Hardcoding Prohibition**: Any hardcoded anchor start or end timestamp in prose, JSON fixtures, or templates triggers immediate lint failure. All times must read dynamically from `week-blueprint.json`.
2. **Zero Craft Authoring**: Injecting new work packages, goals, or sprint deliverables directly inside Matrix 2 is prohibited. All items must originate from Matrix 1 `selected_work_reference[]`.
3. **Personal Strip Purity**: Introducing project tasks, code references, or work packages into the Personal Focus Strip causes immediate validation failure.
4. **Horizontal Overflow Rejection**: Timetable rendering with horizontal scrollbars (`overflow-x: scroll` or `min-width: 1150px`) is rejected. Desktop must maintain `width: 100%`, and mobile (<920px) must maintain `scrollWidth <= clientWidth`.
