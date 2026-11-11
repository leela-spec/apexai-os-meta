# Weekly Command Brief — {{WEEK_ID}} ({{MONDAY_DATE}} – {{SUNDAY_DATE}})

> **Weekly state:** {{READY | READY_WITH_REVIEW | PARTIAL | BLOCKED}}  
> **Direction:** {{TWO_TO_FIVE_SENTENCE_PORTFOLIO_DIRECTION}}  
> **Next action:** {{APPROVE_WEEK | EDIT_PRIORITIES | REDUCE_SCOPE | RESOLVE_CONSTRAINT | REJECT_DIRECTION}}  
> **Review needed:** {{HIGHEST_IMPACT_WEEKLY_DECISION_OR_NONE}}  
> **Scope:** 6 Portfolio Areas (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`); `24` nominal `120m` Flows (`48.0h` gross / `36.0h` Craft `C` + `12.0h` `P/M/R/recap`)  
> **Cockpit view:** `{{HTML_COCKPIT_ARTIFACT_REF}}` (`v05` 6-section interactive view)

## 00 · Portfolio Compass

| Metric | Value | Sub-label / Source Basis |
| :--- | :--- | :--- |
| **Gross / Craft Capacity (`T1`)** | `{{NET_CRAFT_HOURS}}h / 36.0h C` (`48.0h` gross) | `24` nominal `120m` Flows (`72m` trailing `recap_min` inside `12.0h` non-Craft budget) minus `{{MEETING_HOURS}}h` fixed calendar collisions `[src: {{TAG_CLOCK}}]` |
| **Weekly Flows (`Mon–Sun`)** | `{{EFFECTIVE_FLOWS}} / 24 Flows` | `Mon–Fri 4×120m` (`08:00–24:00`) + `Sat–Sun 2×120m` (`12:00–16:00`) `[src: {{TAG_BLUEPRINT}}]` |
| **3×3 Craft Sprints (`C1–C3`)** | `{{EFFECTIVE_SPRINTS}} / 72 Sprints` | `3 × 30m` Craft sprints per Flow (`90m` Craft + `24m` `P/M/R` + `6m` flow recap) |
| **6 Portfolio Areas (`L1` / `L2`)** | `6 Areas · {{L1_COUNT}} L1 · {{L2_COUNT}} L2` | `Leela` · `IPOS` · `Master of Arts` · `Apex AI` · `Mindful Bar` · `Residual` `[src: {{TAG_OP}}]` |
| **G1 Readiness & Provenance** | `{{G1_GATE_STATUS}}` | OP: `{{OP_STATUS}}` · Calendar: `{{CAL_STATUS}}` · Overrides: `{{VERIFIED_OVERRIDE_COUNT}}` |

## 01 · Operator Decisions (Collapsed Default in Cockpit)

### `New` — This Week (`G1` Gate Items)
- **`{{DEC_ID}}` `[{{P_TIER}} | I{{I}}/E{{E}}/R{{R}}]` {{DECISION_LABEL}}** — `{{ACTIVE_VALUE}}` · Gate: `{{PROPOSED_FOR_G1 | APPROVED | CONFIRMED_INPUT}}` `[src: {{TAG_DEC}}]`
  - • *System Default vs Choice:* `{{SYSTEM_DEFAULT_OR_NONE}}` ➔ `{{OPERATOR_CHOICE}}` (`OPERATOR OVERRIDE` badge shown only when verified `{system_default, operator_choice, source_ref}` delta exists)
  - • *Impact & Scope:* {{DECISION_IMPACT_AND_SCOPE}}

### `Standard` — Weekly Blueprint Defaults (`02-weekly-dispersal/week-blueprint.json`)
- **Evening Regime (`Mon–Fri`):** `Mon–Wed Project Night (20:30–22:00)` baseline (weekly theme overrides appear in `New`); `Thu–Fri Freizeit (20:30–22:00)`; `Day Outro (22:00–22:30)`; `18:30–19:30 Evening Physical` outside `72×2m P` quota.
- **Weekend Regime (`Sat–Sun`):** `12:00–16:00` (`2 × 120m` adjacent Flows per day); `StatusMerge` + `PrecapWeek` on `Saturday_or_Sunday` (`D017–D018`).

### `Ongoing` — Standing Multi-Week Rules & Ignored Calendar Holds
- **Ignored Ambient Calendar Holds:** `{{IGNORED_HOLD_SUMMARY}}` (e.g., `WC Meister` ignored per standing operator directive).
- **Standing Portfolio Guards:** `{{STANDING_PORTFOLIO_GUARDS}}`

## 02 · Matrix 1 — Portfolio & Project Architecture (`6 Portfolio Areas`)

*(Render all 6 canonical portfolio areas: `Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`. UI cards remain strictly `L1 / L2` with no `L3` cubes; inside expanded 6-column `G | I | P | S | O | C` drawers, `Goal` and `Output` cells decompose into `Tasks -> Subtasks` with short drafts/examples, `G` includes `acceptance`, `I` includes `sources + upstream_dependencies + exclusions`, and `O` includes `deliverable + redraft`, plus inline `🔗 Cross-Repo:` dependency pills.)*

### 1. `Leela` (`OP: leela-game-flutter / leela-website / leela-spec`)
- **L1 Primary Weekly Outcomes:**
  - [ ] **`[OP-WP#{{ID}}]` {{TITLE}}** (`{{NATIVE_OP_STATUS}}`) · `🔗 Cross-Repo: {{CROSS_REPO_PILL_OR_NONE}}` `[src: {{TAG}}]`
    - `G (Goal + Acceptance + Tasks->Subtasks):` {{GOAL_AND_ACCEPTANCE}}
    - `I (Sources + Deps + Exclusions):` {{INPUTS_DEPS_EXCLUSIONS}}
    - `P (Process):` {{PROCESS}} · `S (Skills):` {{SKILLS}}
    - `O (Deliverable + Redraft + Tasks->Subtasks):` {{DELIVERABLE_AND_REDRAFT}} · `C (Context):` {{CONTEXT}}
- **L2 Nice-to-Haves (Actionable Secondary Candidates Only):**
  - [ ] **`[OP-WP#{{ID}}]` {{L2_TITLE}}** — {{ONE_LINE_OUTCOME}}

### 2. `IPOS` (`OP: ipos`)
- **L1 Primary Weekly Outcomes:** {{IPOS_L1_OUTCOMES}}
- **L2 Nice-to-Haves:** {{IPOS_L2_OUTCOMES}}

### 3. `Master of Arts` (`OP: master-of-arts`)
- **L1 Primary Weekly Outcomes:** {{MOA_L1_OUTCOMES}}
- **L2 Nice-to-Haves:** {{MOA_L2_OUTCOMES}}

### 4. `Apex AI` (`Apex Session / Sync: apexai-os-meta`)
- **L1 Primary Weekly Outcomes:** {{APEX_L1_OUTCOMES}}
- **L2 Nice-to-Haves:** {{APEX_L2_OUTCOMES}}

### 5. `Mindful Bar` (`leela-spec/mindful-bar + mindful-bar`)
- **L1 Primary Weekly Outcomes:** {{MINDFUL_BAR_L1_OUTCOMES}}
- **L2 Nice-to-Haves:** {{MINDFUL_BAR_L2_OUTCOMES}}

### 6. `Residual` (`Overflow / Recovery / Admin / Unassigned`)
- **L1 Primary Weekly Outcomes:** {{RESIDUAL_L1_OUTCOMES}}
- **L2 Nice-to-Haves:** {{RESIDUAL_L2_OUTCOMES}}

## 03 · Matrix 2 — Weekly Blueprint Timetable (`Monday–Sunday` + Personal Focus)

*(Generated dynamically from `02-weekly-dispersal/week-blueprint.json` + `slot-inventory.json`. Weekly cell depth assigns Flow Owner ref from `selected_work_reference[]`, Flow outcome, `C1/C2/C3` macro labels, capacity shape (`full / compressed / minimal / omitted`), and the read-only `DD-22A` `P/M/R` Chunk band; tactical `S1–S3` micro-tasks belong to `PrecapNextDay`.)*

| Day | Regime & Window | Flow 1 (`F1`) | Flow 2 (`F2`) | Flow 3 (`F3`) | Flow 4 (`F4`) | Evening / Calendar / Compression Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Monday** | `08:00–24:00` | {{MON_F1}} | {{MON_F2}} | {{MON_F3}} | {{MON_F4}} | `Project Night 20:30–22:00` · {{MON_NOTES}} |
| **Tuesday** | `08:00–24:00` | {{TUE_F1}} | {{TUE_F2}} | {{TUE_F3}} | {{TUE_F4}} | `Project Night 20:30–22:00` · {{TUE_NOTES}} |
| **Wednesday** | `08:00–24:00` | {{WED_F1}} | {{WED_F2}} | {{WED_F3}} | {{WED_F4}} | `Project Night 20:30–22:00` · {{WED_NOTES}} |
| **Thursday** | `08:00–24:00` | {{THU_F1}} | {{THU_F2}} | {{THU_F3}} | {{THU_F4}} | `Freizeit 20:30–22:00` · {{THU_NOTES}} |
| **Friday** | `08:00–24:00` | {{FRI_F1}} | {{FRI_F2}} | {{FRI_F3}} | {{FRI_F4}} | `Freizeit 20:30–22:00` · {{FRI_NOTES}} |
| **Saturday** | `12:00–16:00` | {{SAT_F1}} | {{SAT_F2}} | — | — | `Weekend Regime (2×120m)` · {{SAT_NOTES}} |
| **Sunday** | `12:00–16:00` | {{SUN_F1}} | {{SUN_F2}} | — | — | `Weekend Regime (2×120m)` + `PrecapWeek / StatusMerge` |

### Personal Focus Strip (`Mental | Physical | Regeneration`)
- **Mental (`M` — `24 × 5m = 120m`):** {{MENTAL_FOCUS_BULLETS}}
- **Physical (`P` — `72 × 2m = 144m` in-Flow + `18:30–19:30` Evening Course):** {{PHYSICAL_FOCUS_BULLETS}}
- **Regeneration (`R` — `72 × 5m = 360m` + `96m` breaks/routines):** {{REGENERATION_FOCUS_BULLETS}}

## 04 · Residual Information, Longlist Deferrals & Provenance

### 4.1 Clock & Capacity Reconciliation
- **Gross vs Net Craft Accounting (`T1`):** `24` Flows × `120m` = `2,880m` (`48.0h`) gross = `2,160m` (`36.0h`) Craft (`72 × 30m`) + `720m` (`12.0h`) non-Craft inside/between Flows (`144m P` + `120m M` + `360m R` + `24m` between-Flow transitions + `72m` trailing `recap_min`).
- **Calendar Subtractions & Buffer Allowances:** {{CALENDAR_SUBTRACTIONS_AND_BUFFERS}}

### 4.2 EM-13 Readiness Gaps & OpenProject Status-vs-Description Audit
- {{EM13_AND_OP_CONTRADICTION_FINDINGS}}

### 4.3 Longlist Deferrals & Revisit Triggers (Moved Out of Matrix 1 `L2`)
- **`[OP-WP#{{DEFERRED_ID}}]` {{DEFERRED_TITLE}}** — Deferred reason: {{REASON}} · Revisit trigger: `{{REVISIT_TRIGGER}}`

### 4.4 1-Hop Provenance Ledger
Every consequential claim in this artifact carries an inline source tag `[src: <TAG>]`. Tags resolve here — exactly one hop:

| Tag | Source | Freshness class (`CURRENT / AGED / STALE / UNKNOWN`) |
| :--- | :--- | :--- |
| {{TAG_1}} | [{{J1_LABEL}}]({{J1_REF}}) - `{{J1_VISIBLE_REF}}` | {{FRESHNESS_CLASS_1}} |

**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Assumptions:** {{ASSUMPTIONS_WITH_TAGS_OR_NONE}}

## 05 · Sequencing & Dispersal Orientation (`02-weekly-dispersal/`)

- **Dispersal Dials (`week-demand.json`):**
  - `Mental (24 slots / 120m):` `Intention` (`focus_days`), `ACIM`, `Surrender`, `Breathing`
  - `Physical (72 slots / 144m):` `Martial Arts`, `Dance`, `S/BJJ`, `General`, `Knee` (pinned to `*_*_I3_P`)
  - `Regeneration (72 in-Flow + 14 routine/break slots / 456m):` `Yoga Nidra`, `Audiobooks`, `Socializing` (`XP = 0`, `DD-16` no numeric BP floor)
  - `Craft / Projects (72 slots / 2,160m across 6 Portfolio Epics):` `Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`
- **Gaussian Placement (`T2`):** `σ = 6.0h` around `19:00` (`1140m`) of each `focus_day` (`w_max = 1.5x`, no Fri→Sat bleed).
- **Projected Weekly Yield (`T2`):** `{{PROJECTED_TP}} TP` · `{{PROJECTED_XP}} XP` · `{{PROJECTED_BP}} BP`

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  specification_version: "PRECAP-WEEK-v2.1"
  artifact_ref: "{{ARTIFACT_REF}}"
  html_cockpit_ref: "{{HTML_COCKPIT_ARTIFACT_REF}}"
  week: "{{WEEK_ID}}"
  date_range: "{{MONDAY_DATE}}_to_{{SUNDAY_DATE}}"
  timezone: "Europe/Berlin"
  clock_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
  result_state: "{{RESULT_STATE}}"
  operator_g1_status: "{{PROPOSED | APPROVED | EDITED}}"
  source_status:
    openproject: "{{ONLINE | OFFLINE_FALLBACK}}"
    google_calendar: "{{ONLINE | OFFLINE_FALLBACK}}"
  weekly_intent: "{{WEEKLY_INTENT_SUMMARY}}"
  six_portfolio_areas:
    - portfolio_id: "leela"
      label: "Leela"
      priority_rank: 1
      selected_work_refs: []
    - portfolio_id: "ipos"
      label: "IPOS"
      priority_rank: 2
      selected_work_refs: []
    - portfolio_id: "master_of_arts"
      label: "Master of Arts"
      priority_rank: 3
      selected_work_refs: []
    - portfolio_id: "apex_ai"
      label: "Apex AI"
      priority_rank: 4
      selected_work_refs: []
    - portfolio_id: "mindful_bar"
      label: "Mindful Bar"
      priority_rank: 5
      selected_work_refs: []
    - portfolio_id: "residual"
      label: "Residual"
      priority_rank: 6
      selected_work_refs: []
  reconciled_calendar_events: []
  capacity_deformations_and_omissions: []
  next_day_seed:
    target_date: "{{NEXT_DAY_DATE}}"
    intended_emphasis: "{{NEXT_DAY_EMPHASIS}}"
  next_consumer: "PrecapNextDay"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md"
  domain_contract_refs:
    - ".claude/skills/PrecapWeek/SKILL.md"
    - ".claude/skills/PrecapWeek/references/operator-weekly-command-brief-intake.md"
    - "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
  legacy_archive_note: "Prior weekly-plan-output-contract.md and v1 Mon-Sat templates are superseded by SPEC-PRECAP-WEEK-ITERATIONS.okf.md (v05) and archived per package-manifest.md."
```

Example: [J02 Weekly Command Brief](../../../apex-meta/operator-output-design/step4-operator-template-system/examples/master-of-arts-example-fragments.md)
