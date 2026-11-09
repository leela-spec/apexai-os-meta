---
type: handover
id: HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN-v1.0
title: Handover — Operator Decision Brief Redesign (Standard, New, Ongoing Variable Labels & Dropdowns)
description: Research and UX architecture handover replacing complex prose decision cards in Part 01 with scannable Standard, New, and Ongoing variable-dropdown controls, Special Project Days (Mon/Wed evenings), OpenProject override indicators, and (i) info disclosure.
status: ready_for_operator_verification
date: 2026-11-09
tags: [weekly-orchestration, operator-decision-brief, ux-design, special-days, overrides, em-09]
---

# Handover — Operator Decision Brief Redesign (`Standard` / `New` / `Ongoing`)

## 1. Mission & Problem Statement

Part 01 (`Operator Decision Brief`) previously rendered dense 2x2 prose cards that conflated fixed operating rules, weekly topic selections, OpenProject overrides, and background calendar fixtures into cluttered paragraphs. The operator requires a **minimal, control-panel-like Variable Label + Dropdown interface** grouped strictly into **`Standard`**, **`New`**, and **`Ongoing`**, enabling immediate comprehension in under 10 seconds while keeping deep detail behind progressive dropdowns and `(i)` info toggles.

---

## 2. 4-Dimensional Handover Contract (`EM-09`)

### 2.1 Input & Priority Ledger
- **P1 Operator Feedback & Governance Rules**:
  - Three required classification buckets: **`Standard`** | **`New`** | **`Ongoing`**.
  - Interactive row anatomy: `[Category Tag] + [Variable Label] + [Active Value Chip / Dropdown Selector] + [(i) More Info Button]`.
  - Weekly orchestration variables explicitly requested:
    1. **Four Flows Cadence & Sequencing Meta-System** (`Standard` default).
    2. **OpenProject Priority Intake vs Operator Override** (`Standard` default intake + `New` override markers whenever operator reprioritizes).
    3. **Flow Topic Routing** (`New` weekly selection assigning topics/repos to F1–F4).
    4. **Special Project Days (Mon & Wed Evenings)** (`New` weekly signature pattern — e.g., Monday & Wednesday evenings routed to *Sexy Content* and *Dance / Martial Arts*).
    5. **Calendar Fixtures Outside Primary Work** (`Ongoing` items present on calendar without being active workstreams — e.g., *WC Meister*, *Munich Dance*).
- **P2 Existing System Grounding**:
  - [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) (`v2.0`).
  - [`01-operator-output-design-principles.okf.yaml`](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml): Principle D1 (*Decision Before Detail*) and D2 (*First 10 Seconds Contract*).
  - [`DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md): Accepted timing cadence `M06=A` (`Saturday Precap`, Mon–Sat work eligibility, Sunday OFF).
- **Deliberately Excluded**: Low-level task/work-package cards inside Part 01 (tasks belong strictly in Matrix 1); calendar hour-by-hour grid (belongs strictly in Matrix 2).

### 2.2 Process & UX Research Synthesis
- **Pattern Studied**: Configuration Variable Inspector / Progressive Disclosure Accordion vs SaaS Parameter Strips.
- **Comparative Insight**: Prose decision cards force reading `~180 words` before confirming whether any default changed. Switching to **3 compact grouped strips (`Standard`, `New`, `Ongoing`)** with single-line **`Label : Value [▾] [(i)]`** rows eliminates cognitive drag:
  - **`Standard` starts collapsed by summary** (operator trusts defaults unless highlighted as overridden).
  - **`New` draws immediate visual focus** (week's sovereign topic routing, Special Project Evenings, and explicit `OPERATOR OVERRIDE` pills overriding OpenProject default priority order).
  - **`Ongoing` cleanly parks ambient calendar events** (separates calendar coexistence like *Munich Dance* or declined *WC Meister* from active deliverable goals).
- **Anti-Drift Rule**: An **`Operator Override`** badge must always show *what OpenProject proposed by default* inside its dropdown vs *what the operator selected*, preserving provenance without adding surface noise.

### 2.3 Output Specification & Concrete Structural Redraft

#### Target Section Architecture (`Part 01 · Operator Decision Brief`)

```text
01 · OPERATOR DECISION BRIEF
├── [GROUP 1: NEW — Weekly Selections & Overrides]  (Highlighted · Expanded preview)
│   ├── Topic Routing (F1–F4)    : [F1-2 MoA · F3 IPOS · F4 Residuals ▾] [OPERATOR OVERRIDE] [(i)]
│   │   └── Dropdown: Shows OP Default proposal vs Operator choice + per-flow focus intent.
│   ├── Special Days (Mon/Wed)   : [Mon: Sexy Content · Wed: Dance & Martial Arts ▾] [(i)]
│   │   └── Dropdown: Configures Monday & Wednesday evening thematic sprint themes.
│   └── Scope Pauses & Re-routes : [Leela: Skill Tree ONLY · MoA Studio Art -> Residuals ▾] [OPERATOR OVERRIDE] [(i)]
│
├── [GROUP 2: ONGOING — Background Calendar & Carried Fixtures]  (Calm Neutral)
│   ├── Calendar Holds / Ignores : [WC Meister: IGNORED · Munich Dance: Thu 18:45 Protected ▾] [(i)]
│   │   └── Dropdown: External calendar events occupying time/status without driving sprint creation.
│   └── Multi-Week Carryover     : [APEX OpenMouse Hook · IPOS Pipeline Audit ▾] [(i)]
│
└── [GROUP 3: STANDARD — Standing Operating Baselines]  (Folded by default · Click to inspect)
    ├── Intake Priority Engine   : [OpenProject Priority Rank (unless overridden in New) ▾] [(i)]
    ├── Flow & Repetition Rule   : [4 Flows Daily · Sequencing 3x3 (flex 3x2 / 3x1) ▾] [(i)]
    └── Daily Time Geometry      : [08:00–24:00 Window · 21:00 Shutdown · Sun OFF ▾] [(i)]
```

#### Interactive Behavior Spec
1. **Default Summary State**: Each group sits as a clean bordered block or horizontal grid of slim variable bars; all sub-details (`Dropdown` + `(i)` notes) remain hidden until clicked.
2. **Dropdown Drawer**: Clicking the `[Value ▾]` selector reveals exact structured parameters (e.g., which OP work packages would have topped the week without the override, or Mon/Wed evening start/end boundaries).
3. **Info Toggle `(i)`**: Clicking `(i)` toggles a slim contextual footnote citing why this variable exists (`DECISIONS.md` rule ID, calendar conflict policy, or coaching pattern note).

### 2.4 Definition of Done (`DoD`)
1. Part 01 contains zero multi-paragraph `decision-card` blocks; every governance point maps into `Standard`, `New`, or `Ongoing`.
2. Special Project Days (Monday & Wednesday evenings) and OpenProject Default vs `OPERATOR OVERRIDE` indicators are first-class variables in `New`.
3. Passive/background calendar commitments (`WC Meister`, `Munich Dance`) live cleanly in `Ongoing` so they neither clutter active repo deliverables nor disappear from planning context.
4. Full readability test verified: operator identifies active weekly overrides in `< 5 seconds` with zero horizontal overflow.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: Previous Part 01 presented 4 dense boxed essays explaining `D014`, sequencing, and Meister overrides uniformly, hiding what was new vs default cadence.
2. **Logic Chain**: Separating systemic invariants (`Standard`), active weekly choices/special project days (`New`), and ambient calendar holds (`Ongoing`) aligns directly with human executive triage—scan *only what changed (`New`)* while retaining instant dropdown access to baseline (`Standard`) and calendar radar (`Ongoing`).
3. **Caveats**: Exact `(i)` micro-copy content per variable will be finalized alongside live Google Calendar & OpenProject intake values at HTML build time.
4. **Conclusion**: Ready for operator review and sign-off before HTML generation.
5. **Verification Method**: Render test of Part 01 slim strips confirming 3 grouped buckets, clickable `<details>`/JS variable dropdowns, and explicit `OPERATOR OVERRIDE` tags.
