---
type: specification
id: SPEC-PRECAP-WEEK-ITERATIONS-v2.0
title: "Precap Week Iterations Specification — Cube-Tree Matrix 1, G-I-P-S-O Task Specs, Variable Brief & Leela Stats"
description: "Canonical specification for Precap Week v2.0: Leela-grounded Header Metrics, Variable-Dropdown Operator Decision Brief (Standard/New/Ongoing), Matrix 1 (Always-On L1 Goal Cubes, Left-Rail Levels, Foldable L2 Nice-to-Have Cubes, L3 Work Packages, G-I-P-S-O Drill-Down), and Matrix 2 (Calendar Flows 08:00–24:00, Shutdown 21:00)."
status: operator_review_pending
date: 2026-11-09
scope: [weekly-orchestration, precap-week, matrix-1, matrix-2, task-spec, g-i-p-s-o, leela-stats, process-trees]
tags: [weekly-orchestration, precap-week, specification, matrix-1, matrix-2, g-i-p-s-o, leela-stats]
---

# Precap Week Iterations Specification — Cube-Tree Matrix 1, G-I-P-S-O Task Specs & Variable Brief

## 1. Executive Summary & Core Architectural Invariants

This specification is the **canonical source of truth** for authoring, evaluating, and running the **Precap Week** iteration artifact (the *Weekly Command Brief*). Version `v2.0` supersedes `v1.2`'s bulky Level-1 prose banner, card-prose decision grid, and mandatory bottom Mermaid deck, establishing the Goal-Cube Tree, standardized `G-I-P-S-O` Task Specification, and `Standard`/`New`/`Ongoing` Variable Decision Brief.

### Core Architectural Invariants

- [P0 | I98/E95/R05] **Header Framing & Leela-Grounded Stats**: Title is strictly `Precap Week` followed by the ISO date span (e.g. `Precap Week · 09 – 15 November 2026`). Abstract taglines remain prohibited. Header telemetry follows Leela's Stat-Chip Laws (`HANDOVER-05`): separating basis (`○ Planned` vs `● Realized` vs `◇ Forecast`), enforcing Coverage accounting (`Target / Placed / Realized`), `XP/TP/BP` balance, and `Testing vs Application` ratio.
- [P0 | I97/E94/R06] **Three-Part Sequential Building**:
  1. **Part 1: Operator Decision Brief (`Standard` / `New` / `Ongoing`)**: Compact variable labels with expandable dropdowns and `(i)` info toggles replacing verbose prose blocks (`HANDOVER-04`). Highlights weekly flow routing, Special Project Days (Mon/Wed evenings), OpenProject overrides, and ongoing calendar holds.
  2. **Part 2: Matrix 1 — Goal-Cube Tree & Project Overview (Non-Temporal)**: Single stacked column of repository rows. **Top `L1: Priority Goals` strip is always visible** under each repo header as side-by-side clickable Goal Cubes (1–2 operator goals/project; arrows drawn *only* if major goals strictly depend on each other). Levels use **compact left-rail vertical labels (`L1` / `L2` / `L3`)**; **`L2: Nice-to-Haves`** (cube-cards side-by-side) and **`L3: Other Work Packages`** start **folded**. Clicking any cube fans out child sub-cubes and/or reveals its inline **`G-I-P-S-O`** Task Specification (`HANDOVER-03`). **Zero sprints in Matrix 1.**
  3. **Part 3: Matrix 2 — Calendar Snapshot & Visualization (Temporal)**: Full-width **Monday–Sunday** hourly table mapping F1–F4 and 30m sprints across `08:00–24:00` with `21:00` Daily Shutdown. **Monday–Friday run the weekday regime; Saturday and Sunday run the weekend regime** — the same mechanism under a reduced slot count and distinct standing content, never a second mechanism.
- [P0 | I96/E94/R08] **Five Repository Boundaries**:
  1. **Master of Arts** (`MasterOfArts` / OP #14, #6, #7): Website content draft, content production week (7 videos), and business operations (invoicing engine & automated PDF billing).
  2. **Leela** (`Leela-Cloud-2026` / OP #10): Focused **strictly on the Skill Tree** (spatial node contracts, Chunk library, durable placement identity). Path & Sequencing paused this week.
  3. **Investment / IPOS** (`investment-ipos` / OP #16): Complete pipeline recheck, external ingestion possibilities, and sovereign data visualization over time.
  4. **Apex OS** (`apexai-os-meta` / OP #8): Standalone systems repo covering OpenMouse kernel bindings, mindful repo orchestration, and dark factory integration.
  5. **Residuals** (Personal creative sprints & auxiliary infrastructure): Studio art & apartment setup (Sprint 1), Sexy Content (Sprint 2), Community & Travel (Sprint 3), PM Infrastructure.
- [P0 | I95/E95/R05] **OpenProject Default vs Operator Decision State**: OpenProject supplies the default priority baseline (`Standard`). When the operator assigns weekly topic themes or Special Project Days, Part 1 flags them under **`New`** with explicit **`OPERATOR OVERRIDE`** markers.
- [P0 | I94/E92/R10] **Matrix 2 Operating Window & Shutdown**: `08:00 – 24:00` daily span; `21:00` sharp Daily Shutdown.
- [P0 | I93/E90/R08] **Universal Specification Invariant**: This specification governs schemas, structural slots, variable syntax, and interaction contracts (`{{Goal}}`, `[OP-WP#<id>]`). Week 45 items illustrate structure only.

---

## 2. Linked Canonical Specifications & Authoritative Handovers

### Active v2.0 Extension & Research Handovers
1. **Task Spec Variable System, Symbols & OpenProject Sync (`2do`):**
   [`HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md) (`G-I-P-S-O` variable system, conditional omission in parent Goal cubes, Leela cube grammar, fractal tree click expansion, OpenProject task-creation alignment).
2. **Operator Decision Brief UX Redesign:**
   [`HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md) (`Standard`/`New`/`Ongoing` variable-dropdown strips, Mon/Wed Special Project Evenings, `WC Meister`/`Munich Dance` ambient holds, `(i)` info toggles).
3. **Header & Orchestration Stats Research (`2do` Grounded in Leela):**
   [`HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md) (Adapts Leela `00-MACRO.md` & `10-STATS-FEATURE.md` stat-chip laws, Coverage Triple, `XP/TP/BP`, Testing-vs-Application).
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

## 4. Part 1 Specification: Operator Decision Brief (`Standard` / `New` / `Ongoing`)

The Operator Decision Brief acts as a calm executive control panel rather than a wall of decision essays. Detailed specification lives in [`HANDOVER-04`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md) and stats rules live in [`HANDOVER-05`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-05-PRECAP-STATS-SYSTEM-LEELA-INSPIRED.okf.md).

### 4.1 Header & Leela-Grounded Metric Strap
* **Visual Anchor:** Clean title `"Precap Week"` followed by the exact date span (e.g. `09 – 15 November 2026 · ISO Week 45`).
* **Portfolio Metrics Strap (Leela Stat-Chip Grammar):** Five non-blending KPI cards separating basis marks (`○` planned · `●` trailing realized · `◇` forecast):
  1. **`○ TP · Capacity Placed`** — Planned focus hours & minutes across F1–F4 (e.g. `○ 38.5h · 2,310 min`).
  2. **`🎯 Coverage Triple`** — `Target / Placed / Lag` check proving every `L1 Priority Goal` fits in Matrix 2 (`Target 9 · Placed 9`).
  3. **`⚡ XP · Priority Focus Ratio`** — Percentage of weekly capacity allocated directly to `L1 Priority Goals` vs nice-to-haves/maintenance.
  4. **`⚖ BP · Week Balance Index`** — Adapted 0–100 health score blending branch diversity (50%), `21:00` shutdown preservation (25%), and Mon/Wed Special-Day alternation (25%).
  5. **`⚗ Testing vs Application`** — Split between exploratory R&D (`Testing`: IPOS recheck, Apex OpenMouse) and deterministic production (`Application`: 7 Videos, PDF billing).

### 4.2 Decision Classification & Variable-Dropdown Model (`Standard` / `New` / `Ongoing`)

Every governance parameter is rendered as a slim single-line control:
`[Category Tag] Variable Label : Active Summary Chip [▾ Dropdown] [(i) Info]`

1. **`New` — Weekly Topic Selections & Operator Overrides** *(Visibly badged `OPERATOR OVERRIDE` where diverging from OP default)*:
   - **Flow Topic Routing (`F1–F4`):** Maps weekly focus streams (e.g. `F1–F2 MoA · F3 IPOS · F4 Residuals`).
   - **Special Project Days (Mon & Wed Evenings):** Assigns the operator's Monday & Wednesday special-project themes (e.g. Mon: *Sexy Content*, Wed: *Dance & Martial Arts*).
   - **Weekly Scope Locks / Pauses:** e.g., `Leela = Skill Tree ONLY` (Path & Sequencing paused).
2. **`Ongoing` — Background Calendar Fixtures & Carried States**:
   - External calendar bookings present on the calendar grid without actively driving focus sprints (e.g. `WC Meister`: Declined/Ignored; `Munich Dance`: Thu 18:45 fixed social anchor), plus multi-week carried engineering threads.
3. **`Standard` — Standing Operating Baselines** *(Folded/compact by default)*:
   - **Priority Intake Engine:** OpenProject Priority List decides default ordering unless overridden in `New`.
   - **Flow & Sequencing System:** 4 Flows/day; Sequencing 3×3 standard cadence (flex 3×2 or 3×1).
   - **Time Window Anchor:** `08:00–24:00` span, `21:00` Daily Shutdown on every day. **Sunday is planned**, under the weekend regime rather than the weekday regime; it is no longer OFF by default.

---

## 5. Part 2 Specification: Matrix 1 (Goal-Cube Tree & Project Overview — Non-Temporal)

Matrix 1 gives the operator fast **goal-to-goal comprehension across projects**, backed by recursive click-to-drill-down Task Specifications (`G-I-P-S-O`, [`HANDOVER-03`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md)). Matrix 1 contains **zero calendar times and zero sprints**.

### 5.1 Structural Layout & Core Rules
1. **Single Stacked Column:** Repositories stack vertically full-width (`1. MoA`, `2. Leela`, `3. IPOS`, `4. Apex OS`, `5. Residuals`). Multi-column project grids remain prohibited.
2. **1–2 Operator Goals Rule:** At week start, the operator identifies **1 (at most 2) concrete Weekly Goals** per active repository.
3. **Remove Bulky Outcome Banner:** Fat top-of-card prose paragraphs (`Level 1 High Level Strategic Outcome`) are **explicitly removed**.
4. **Always-On `L1: Priority Goals` + Folded `L2`/`L3`:** Directly underneath each project header, **`Level 1: Priority Goals`** is **always open and visible**. **`Level 2: Nice-to-Haves`** and **`Level 3: Other Work Packages`** start **folded**.
5. **Left-Bar Vertical Level Rail:** Each layer is labeled cleanly on a narrow left-side vertical rail (`L1`, `L2`, `L3`) rather than burning vertical height with top strip headers.

### 5.2 Three-Layer Cube & Tree-Click Specification

1. **Left Rail `L1 · Priority Goals` *(Always Visible)***
   - Renders compact side-by-side **square/cube buttons** showing *what will be reached* for the week's priority goals.
   - **Conditional Critical Path:** Dependency arrows (`➔`) appear **only** if major goals strictly block/depend on each other. Independent parallel goals render side-by-side without forced arrows.
   - **Click Behavior (Tree Fan-Out + `I-P-S-O`):** Clicking any `L1` Goal cube drops down:
     - *(a)* A **branching tree bus** (`|` ➔ horizontal bar ➔ downward ticks) fanning out side-by-side **child sub-output / sub-process cubes** (click again recursively for deeper granularity), AND/OR
     - *(b)* An inline **`Task Specification`** drawer showing **`Input (Sources by Priority)` | `Process (Framework/Logical Path)` | `Skills (Priority)` | `Output (Files / Header Skeleton Draft)`** — omitting redundant parent `Goal` wording since the clicked Goal cube already names it.
2. **Left Rail `L2 · Nice-to-Haves` *(Foldable, Cube-Card Grid)***
   - Folded immediately beneath `L1`. Uses the **exact same horizontal side-by-side clickable cube-card style** (never fat full-width bars stacked vertically). Clicking any cube opens its tree breakdown / `I-P-S-O` specification.
3. **Left Rail `L3 · Other Work Packages` *(Foldable, Dense Task List)***
   - Folded at the bottom of the project card. Holds the remaining OpenProject backlog/secondary tasks as a compact list; clicking any row expands its full **`G-I-P-S-O`** Task Specification (`Goal > Task > Subtask` + `I` + `P` + `S` + `O`).

### 5.3 Visual Architecture Sketch (Per Project Card)

```text
+---------------------------------------------------------------------------------------------------+
| [Repo Header]  1. Master of Arts (Website, Content Week & Invoicing)     [OP #14, #6, #7]        |
+-------+-------------------------------------------------------------------------------------------+
| L1    | [ ▣ Website Content Draft ]   ➔   [ ▣ 7 Produced Videos ]     [ ⚡ Automated PDF Billing ] |
| Goal  |         │                                    (Arrows drawn ONLY when major goals depend)  |
| Cubes |         ├──┬────────────┬────────────┐                                                    |
| Always|         ▼  ▼            ▼            ▼                                                    |
| On    |       [Nav Grid]   [Essay Copy]  [Reading Drawer]                                         |
|       |       └─ Drawer on click: [Input: P1/P2] | [Process: Framework] | [Skills] | [Output]     |
+-------+-------------------------------------------------------------------------------------------+
| ▸ L2  | [Folded Bar] Level 2: Nice-to-Haves (expands to side-by-side clickable cube cards)        |
+-------+-------------------------------------------------------------------------------------------+
| ▸ L3  | [Folded Bar] Level 3: Other Work Packages (expands to clickable OP task list + G-I-P-S-O) |
+-------+-------------------------------------------------------------------------------------------+
```

### 5.4 Repository Scope Mapping (Five Frontiers)

- **1. Master of Arts (`MasterOfArts`):** Website content draft, Content Week (7 videos), Business Invoicing & automated PDF billing. *(Studio fine art assigned to Residuals).*
- **2. Leela (`Leela-Cloud-2026`):** **Skill Tree ONLY** (node contracts, durable placement IDs, Chunk schema). Path & Sequencing explicitly paused this week.
- **3. Investment / IPOS (`investment-ipos`):** Full pipeline recheck, external ingestion evaluation, and modularizing sovereign data visualization over time.
- **4. Apex OS (`apexai-os-meta`):** Dedicated standalone systems project: OpenMouse kernel HID hooks, mindful repo orchestration, dark factory pipeline.
- **5. Residuals:** Mon/Wed Special Project Evenings & personal sprints — Studio Art & Apartment, Sexy Content, Community & Travel, PM Infrastructure.

### 5.5 Cross-Project Consolidated Dependency Deck — `DEPRECATED_UNDER_RESEARCH`

The bottom standalone Mermaid `Consolidated Cross-Repo Critical Path & Process Dependency DAG` from `v1.2` is **deprecated pending research** per [`HANDOVER-06`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md). Do not auto-render multi-subgraph bottom Mermaid charts unless [`HANDOVER-06`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md) ratifies an inline or milestone-only replacement.

---

## 6. Part 3 Specification: Matrix 2 (Calendar Snapshot & Visualization — Temporal)

Matrix 2 maps the selected work packages from Matrix 1 across the calendar days, respecting verified appointments, routine anchors, and focus capacity.

### 6.1 Daily Time Geometry & Operating Windows

* **Standard Operating Window:** `08:00 – 24:00` (16 hours total daily span).
* **Daily Shutdown:** `21:00` sharp.
* **Routine Anchors & Time Architecture:**
  - `08:00 – 09:00`: Morning Routine, Meditation, Daily Setup (60m).
  - `09:00 – 11:00`: **Flow 1** — Master of Arts: Creative Content Production (7 videos production pass).
  - `11:15 – 12:30`: **Flow 2** — Master of Arts: Website Content Draft & Invoicing Engine.
  - `12:30 – 13:30`: Protected Anchor: Midday Reset, Healthy Lunch & Outdoor Walk (60m).
  - `13:30 – 15:30`: **Flow 3** — Investment / IPOS: Pipeline Recheck & Data Visualization Over Time.
  - `16:00 – 17:45`: **Flow 4** — Residual Flow: Personal Sprints (Apartment & Art, Sexy Content, Community & Travel).
  - `17:45 – 21:00`: Evening Work Window / Dinner / External Personal Commitments.
  - `21:00 – 21:30`: **Daily Shutdown (21:00)**: Outro, Day Evidence Commit & Workspace Reset.
  - `21:30 – 24:00`: Evening Regeneration, Rest, Reading & Night Recovery.

### 6.2 External Calendar Meeting Collision Handling
- Existing external Google Calendar events take absolute non-destructive priority unless explicitly overridden by an operator decision.
- **Operator Decision Override:** The operator may explicitly elect to ignore or decline specific meetings (e.g. Meister meetings ignored for Week 45), freeing up evening focus blocks.
- Schedulable focus flows flex around active verified appointments (e.g. `Alex & Chris` Thursday 10:00–11:00 compresses Flow 1 to `09:00–10:00`; `München Tanz` Thursday 18:45–21:00 wraps evening flow before `18:15`).

### 6.3 Full-Width Responsive HTML Calendar Specification

Matrix 2 is rendered using a full-width, horizontally scrollable HTML table spanning **Monday through Sunday**. All four flows are explicitly displayed, with sprint slots containing **at least three distinct actionable items**. Saturday and Sunday columns render under the weekend regime: the same flow and sprint structure at a reduced slot count.

```html
<div class="calendar-viewport" style="width:100%; overflow-x:auto; margin:20px 0;">
  <table style="width:100%; min-width:1300px; border-collapse:collapse; font-size:12px; border:1px solid #dce4e8; background:#fffdf8;">
    <thead>
      <tr style="background:#162642; color:#fff;">
        <th style="width:12%; padding:10px; border:1px solid #2a3e5c;">Window / Flow</th>
        <th style="width:6%; padding:10px; border:1px solid #2a3e5c;">Sprint</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Monday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Tuesday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Wednesday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Thursday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Friday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Saturday</th>
        <th style="width:11.7%; padding:10px; border:1px solid #2a3e5c;">Sunday</th>
      </tr>
    </thead>
    <tbody>
      
      <!-- Protected Routine Anchor: Morning -->
      <tr style="background:#f4f1ea; color:#687b8b;">
        <td style="padding:6px; text-align:center; font-family:monospace;">08:00–09:00</td>
        <td colspan="8" style="padding:6px; text-align:center;">🔒 Protected Anchor: Morning Routine, Meditation & Setup</td>
      </tr>

      <!-- Focus Flow Block 1 -->
      <tr style="border-top:2px solid #507967;">
        <td rowspan="3" style="padding:10px; vertical-align:top; background:#f5f8f5;">
          <b style="color:#2a5035;">Flow 1 (2h)</b><br>
          <span style="font-size:10px; color:#687b8b;">09:00–11:00</span><br>
          <span style="font-size:11px; font-weight:700;">MoA: Content (Videos)</span>
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
          <em>Sprint allocations dynamically populated per day</em>
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

      <!-- Flow 2: MoA Website & Invoicing -->
      <tr style="border-top:2px solid #355570;">
        <td rowspan="3" style="padding:10px; vertical-align:top; background:#f0f5fa;">
          <b style="color:#1d3859;">Flow 2 (1.25h)</b><br>
          <span style="font-size:10px; color:#687b8b;">11:15–12:30</span><br>
          <span style="font-size:11px; font-weight:700;">MoA: Website/Invoicing</span>
        </td>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 1</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <em>Website content draft & invoicing schema sprints</em>
        </td>
      </tr>
      <tr>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 2</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <em>PDF template & tax calculation unit tests</em>
        </td>
      </tr>
      <tr style="border-bottom:2px solid #355570;">
        <td style="padding:6px; text-align:center; font-weight:700;">Sprint 3</td>
        <td colspan="7" style="padding:6px; vertical-align:top;">
          <em>Staging validation & client billing test run</em>
        </td>
      </tr>

      <!-- Protected Routine Anchor: Lunch -->
      <tr style="background:#f4f1ea; color:#687b8b;">
        <td style="padding:6px; text-align:center; font-family:monospace;">12:30–13:30</td>
        <td colspan="8" style="padding:6px; text-align:center;">🔒 Protected Anchor: Midday Reset, Healthy Lunch & Fresh Air Walk</td>
      </tr>

      <!-- Flow 3: IPOS Pipeline Recheck -->
      <tr style="border-top:2px solid #b08445;">
        <td rowspan="3" style="padding:10px; vertical-align:top; background:#fdf9f2;">
          <b style="color:#784f1e;">Flow 3 (2h)</b><br>
          <span style="font-size:10px; color:#687b8b;">13:30–15:30</span><br>
          <span style="font-size:11px; font-weight:700;">IPOS: Pipeline Recheck</span>
        </td>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 1</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <em>Pipeline architecture audit & external ingestion possibilities</em>
        </td>
      </tr>
      <tr>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 2</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <em>Data visualization over time modularization</em>
        </td>
      </tr>
      <tr style="border-bottom:2px solid #b08445;">
        <td style="padding:6px; text-align:center; font-weight:700;">Sprint 3</td>
        <td colspan="7" style="padding:6px; vertical-align:top;">
          <em>Test harness & sovereign JSON schema benchmarks</em>
        </td>
      </tr>

      <!-- Flow 4: Residual Life & Creative Sprints -->
      <tr style="border-top:2px solid #806655;">
        <td rowspan="3" style="padding:10px; vertical-align:top; background:#f9f5f0;">
          <b style="color:#684f3e;">Flow 4 (1.75h)</b><br>
          <span style="font-size:10px; color:#687b8b;">16:00–17:45</span><br>
          <span style="font-size:11px; font-weight:700;">Residual Life Flows</span>
        </td>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 1</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <b>Apartment & Studio Art:</b> Workspace acoustic tuning, studio clean room, canvas stretching, painting.
        </td>
      </tr>
      <tr>
        <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 2</td>
        <td colspan="7" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
          <b>Sexy Content:</b> Aesthetic moodboards, photoshoot lighting, high-resolution portrait capture, color grading.
        </td>
      </tr>
      <tr style="border-bottom:2px solid #806655;">
        <td style="padding:6px; text-align:center; font-weight:700;">Sprint 3</td>
        <td colspan="7" style="padding:6px; vertical-align:top;">
          <b>Community & Traveling:</b> Peer network outreach, community dinner sync, travel route planning, logistics.
        </td>
      </tr>

      <!-- Protected Routine Anchor: Daily Shutdown at 21:00 -->
      <tr style="background:#eef2f7; color:#355570; font-weight:700; border-top:2px solid #304e86;">
        <td style="padding:8px; text-align:center; font-family:monospace;">21:00–21:30</td>
        <td colspan="8" style="padding:8px; text-align:center;">🔒 Daily Shutdown (21:00): Outro, Day Evidence Commit & Workspace Reset</td>
      </tr>

      <!-- Evening Regeneration Window: 21:30 to 24:00 -->
      <tr style="background:#f9f8f5; color:#788b99;">
        <td style="padding:8px; text-align:center; font-family:monospace;">21:30–24:00</td>
        <td colspan="8" style="padding:8px; text-align:center;">Evening Regeneration, Rest, Reading & Night Recovery</td>
      </tr>

    </tbody>
  </table>
</div>
```

---

## 7. Downstream Consumer Contract: PrecapNextDay Handshake

Precap Week concludes with an embedded YAML `presentation_handoff` block consumed with zero token waste by `PrecapNextDay`:

```yaml
presentation_handoff:
  specification: "SPEC-PRECAP-WEEK-ITERATIONS-v2.0"
  produced_at: "2026-11-09T10:45:00Z"
  operator_governance_status: "OPERATOR_SPEC_VERIFICATION_PENDING"
  active_week: "{{ACTIVE_ISO_WEEK}}"
  timezone: "Europe/Berlin"
  
  repository_priorities:
    master_of_arts:
      priority_goals: ["Website Content Draft", "7 Produced Videos", "Automated PDF Billing"]
      active_workstreams: ["website_content", "content_week_7_videos", "business_invoicing"]
    leela:
      priority_goals: ["Skill Tree Spatial Node Contracts & Freeze Gate"]
      active_workstreams: ["skill_tree_contracts"]
    investment_ipos:
      priority_goals: ["Full Pipeline Recheck & Sovereign Data Visualization Over Time"]
      active_workstreams: ["pipeline_recheck", "data_viz_over_time"]
    apex_os:
      priority_goals: ["OpenMouse Kernel HID Binding", "Mindful Repo Orchestration & Dark Factory Gate"]
      active_workstreams: ["openmouse_integration", "mindful_repo_orchestration", "dark_factory"]
    residuals:
      priority_goals: ["Mon/Wed Special Project Evenings (Sexy Content, Dance/Martial Arts)", "Studio Art & Travel Sync"]
      active_workstreams: ["apartment_studio_art", "sexy_content", "community_travel"]

  operating_geometry:
    daily_window: "08:00-24:00"
    daily_shutdown: "21:00"
    special_project_evenings: ["Monday", "Wednesday"]
    reconciled_calendar_events: []

  next_consumer: "PrecapNextDay"
  next_action: "Verify v2.0 spec & Handovers 03–06 before regenerating Precap HTML"
```

---

## 8. Failure Guards & Anti-Drift Gates

- [ ] **FG-01 (No Sprints in Matrix 1):** Matrix 1 must **never** contain sprint allocations or 30-minute breakdown units. Sprints belong strictly in Matrix 2.
- [ ] **FG-02 (Stacked Layout & Cube Grid):** Matrix 1 repositories stack in a single full-width column; `L1 Priority Goals` and `L2 Nice-to-Haves` render items as side-by-side clickable cubes, never full-width fat stacked task rows.
- [ ] **FG-03 (Always-On L1 & Left-Rail Folding):** Under each repo header, `L1: Priority Goals` is always visible (bulky prose green banner prohibited; arrows only on dependent major goals). `L2: Nice-to-Haves` and `L3: Other Work Packages` start folded with vertical left-rail labels.
- [ ] **FG-04 (Universal `G-I-P-S-O` & Conditional Omission):** Every task defines `Goal > Task > Subtask`, `Input` (Sources by Priority), `Process` (Framework), `Skills` (Prioritized), and `Output` (Files/Headers). Child cubes omit redundant parent Goal headers inline.
- [ ] **FG-05 (Calendar Operating Window):** Matrix 2 timeline spans `08:00–24:00` with daily shutdown at `21:00`. All four daily flows remain explicitly visible.
- [ ] **FG-06 (No Synthetic IDs & Deferred Dag Research):** Cited work packages carry verified OpenProject IDs (`[OP-WP#<id>]`) or `[OP-UNRESOLVED]`. Bottom Consolidated DAG remains suppressed under `HANDOVER-06` research.
