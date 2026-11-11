---
type: handover
id: HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN-v1.0
title: Handover — Collapsible Operator Decision Brief (New, Ongoing, Standard Preview Cards & Setting Detail)
description: UX architecture handover defining one collapsible Section 01 whose folded header retains New, Ongoing, and Standard preview cards with factual setting summaries, plus per-setting expansion when opened.
status: ready_for_operator_verification
date: 2026-11-10
tags: [weekly-orchestration, operator-decision-brief, ux-design, special-days, overrides, em-09]
---

# Handover — Collapsible Operator Decision Brief (`New` / `Ongoing` / `Standard`)

## 1. Mission & Problem Statement

Section 01 has an **overall expand/collapse control**. Its collapsed state shows three side-by-side cards—`New`, `Ongoing`, `Standard`—each already containing short factual `setting: value` previews. Opening Section 01 expands those cards into setting lists; clicking a setting reveals its detail. A collapsed header with empty category names is not acceptable.

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
  - [`DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md): Accepted Monday–Sunday cadence (`D017` superseding `M06=A`; Saturday or Sunday Precap; Sunday weekend regime via [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json)).
- **Deliberately Excluded**: Low-level task/work-package cards inside Part 01 (tasks belong strictly in Matrix 1); calendar hour-by-hour grid (belongs strictly in Matrix 2).

### 2.2 Process & UX Research Synthesis
- **Pattern Studied**: Configuration Variable Inspector / Progressive Disclosure Accordion vs SaaS Parameter Strips.
- **Control Structure**: One collapsible Section `01` with three responsive preview cards in the order **New | Ongoing | Standard**. Cards display concise `setting: current value` summaries even while Section `01` is closed.
- **Expanded Interaction**: Open Section `01` -> each card shows complete setting rows -> click an individual setting for its detailed parameters, reasons, and provenance. Closing Section `01` hides these details while preserving its three preview cards.
- **`New`** emphasizes genuinely changed weekly routing, overrides, topic selections, and special project evenings.
- **`Ongoing`** shows carried work and background calendar state without turning external calendar events into project tasks.
- **`Standard`** shows standing OpenProject intake priority, `3×3` Flow cadence, and daily clock boundaries sourced from [`02-weekly-dispersal/week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) (`Mon–Fri` `08:00–24:00` with `22:00–22:30` `Day Outro`; `Sat–Sun` `12:00–16:00` weekend regime; Sunday no longer OFF).
- **Anti-Drift Rule**: Display an `Operator Override` label only with evidence of both the default and the operator choice. When either is unknown, mark `unverified` rather than fabricating comparison values.

### 2.3 Output Specification & Concrete Structural Redraft

#### Target Section Architecture (`Section 01 · Operator Decision Brief`)

```text
01 · OPERATOR DECISION BRIEF              [Collapse/Expand whole section]
    [ NEW                     ] [ ONGOING                  ] [ STANDARD                         ]
    [ Flow routing: F1-F4     ] [ Calendar holds: ...      ] [ Intake priority: OP              ]
    [ Scope pause: Leela      ] [ Carryover: ...           ] [ Flows: 4 Mon-Fri / 2 Sat-Sun     ]
    [ Evening themes: ...     ] [ ...                      ] [ Clock: 08:00-24:00 / Day Outro   ]
    (Above three preview cards remain visible when Section 01 is collapsed.)

    On Section 01 expansion: the SAME three cards reveal the full list of
    `Variable: Current value` rows. Selecting one row opens its parameters,
    grounded override state, and provenance. No unrelated summary toolbar.
```

#### Interactive Behavior Spec
1. **Whole-section collapse**: Hide expanded setting rows/drawers while retaining all three `New | Ongoing | Standard` preview cards and their `setting: value` summaries.
2. **Whole-section expansion**: Reveal full setting lists across the three cards without creating a duplicate control strip.
3. **Setting click**: Expose exact structured values and provenance inline inside that setting item; any `(i)` rationale lives inside the expanded setting detail, never as an extra global toolbar button.

### 2.4 Definition of Done (`DoD`)
1. Section `01` has a functional whole-section fold; **`New`, `Ongoing`, `Standard`** preview cards remain visible when collapsed.
2. Each preview contains actual `setting: value` rows, not empty category-only headers. Expanded cards let individual settings open concrete details.
3. Calendar holds and carried states stay under `Ongoing`; verified operator overrides under `New`; baseline defaults (`week-blueprint.json` `Mon–Sun`) under `Standard`.
4. Responsive layout has zero horizontal overflow; no redundant decision panel is added. Empirical readability timing is measured, never claimed from mock data.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: Previous Part 01 variants either buried defaults in prose essays or folded settings into uncollapsible `<details>` buckets lacking section-level collapse with persistent `setting: value` cards.
2. **Logic Chain**: Separating active weekly changes (`New`), carried calendar state (`Ongoing`), and standing clock/intake baselines (`Standard`) into one collapsible panel whose collapsed state preserves three scannable `setting: value` preview cards delivers instant `< 10s` triage without losing depth.
3. **Caveats**: Exact `(i)` micro-copy content per variable binds dynamically to live Google Calendar, OpenProject intake, and [`week-blueprint.json`](file:///C:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json) at HTML build time.
4. **Conclusion**: Aligned to `v05` operator corrections and `Mon–Sun` blueprint clock (`DD-24` resolved).
5. **Verification Method**: Render and exercise whole-section collapse/expand (`#s01`) confirming three visible `New | Ongoing | Standard` `setting: value` preview cards when folded and independent setting-level detail expansion when opened.
