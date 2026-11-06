# Weekly Command Brief - {{WEEK_OR_DATE_RANGE}}

> **Weekly state:** {{READY | READY_WITH_REVIEW | PARTIAL | BLOCKED}}  
> **Direction:** {{TWO_TO_FIVE_SENTENCE_PORTFOLIO_DIRECTION}}  
> **Next action:** {{APPROVE_WEEK | EDIT_PRIORITIES | REDUCE_SCOPE | RESOLVE_CONSTRAINT | REJECT_DIRECTION}}  
> **Review needed:** {{HIGHEST_IMPACT_WEEKLY_DECISION_OR_NONE}}  
> **Scope:** {{ACTIVE_PROJECT_COUNT}} projects; {{MAJOR_OUTCOME_COUNT}} major outcomes

## Operator Decisions (Informatics Governed)

- **DEC-01 [P0 | I95/E30/R20] {{DECISION_TITLE}}**
  - • Context: {{DECISION_CONTEXT_OR_CONSTRAINT}}
  - • OpenProject Anchor: `[OP-WP#{{WP_ID}}]`
  - • Action Required: {{OPERATOR_ACTION_OR_CHOICE}}
  - • Status: `{{PROPOSED | APPROVED | REJECTED | DEFERRED}}`

## Weekly Direction

**Portfolio North Star:** {{PORTFOLIO_WEEKLY_INTENT}}

### Highlight Goals by Project Sequence:
- **Seq 1 (Priority Master of Arts Website & Invoices):** {{MA_HIGHLIGHT_GOAL}}
- **Seq 2 (Investment Pipeline & Dashboard):** {{INV_HIGHLIGHT_GOAL}}
- **Seq 3 (Apex OS OpenMouse Integration):** {{APEX_HIGHLIGHT_GOAL}}
- **Seq 4 (Leela Skill Tree Completion):** {{LEELA_HIGHLIGHT_GOAL}}

**Cross-Portfolio Capacity Floor:** {{AVAILABLE_CAPACITY_AND_FIXED_CALENDAR_CONSTRAINTS}}

## Weekly Architecture

### Matrix 1: Project Architecture & Process Flow (Non-Temporal)

*(Repeat for each active project: Priority Master of Arts, Investment, Apex OS, Lila)*

#### Project: {{PROJECT_NAME}} (OP ID: {{PROJECT_SLUG_OR_ID}})
- **Strategic Target:** {{PROJECT_STRATEGIC_TARGET}}
- **Baseline State:** {{WHERE_THE_PROJECT_STANDS_NOW}}

- **Process Flow & Iterations:**
  - `Step 1: [OP-WP#{{ID_1}}] {{STEP_1_NAME}}` ➔ `Step 2: [OP-WP#{{ID_2}}] {{STEP_2_NAME}}` ↻ `Iteration [OP-WP#{{ID_3}}] {{ITERATION_NAME}}` ➔ `Step 3: [OP-WP#{{ID_4}}] {{STEP_3_NAME}}`
  - *Evolution Commentary:*
    - "This is there now": {{CURRENT_STATE_OR_EXISTING_ASSET}}
    - "This goes where": {{DESTINATION_FILE_OR_PIPELINE_HANDOFF}}

- **Shortlist (Weekly Commitments):**
  - [ ] **[OP-WP#{{ID_1}}] {{TASK_NAME}}** (I{{IMP}}/R{{RISK}}/E{{EVID}})
    - • Subtask: {{SUBTASK_NAME}} — Output: `{{OUTPUT_PATH}}`
    - • Subtask: {{SUBTASK_NAME}} — Dependency: `[OP-WP#{{PARENT_ID}}]`
    - • *Handshake*: {{HANDOFF_NOTES}}

- **Longlist (Backlog / Staged / Next in Queue):**
  - [ ] **[OP-WP#{{ID_STAGED}}] {{STAGED_TASK_NAME}}**: {{STAGED_REASON_OR_TRIGGER}}
  - [ ] **[OP-WP#{{ID_DEFERRED}}] {{FUTURE_PHASE_NAME}}**: {{DEPENDENCY_CONDITION}}

### Matrix 2: Timeline & Calendar View (Temporal / Sequences & Sprints)

<div class="weekly-calendar-matrix" style="width: 100%; overflow-x: auto; margin: 16px 0;">
  <table style="width: 100%; min-width: 1050px; border-collapse: collapse; font-family: system-ui, sans-serif; font-size: 0.85em; border: 1px solid rgba(128,128,128,0.3);">
    <thead>
      <tr style="background: rgba(128,128,128,0.15); border-bottom: 2px solid #555;">
        <th style="width: 16%; padding: 8px; text-align: left;">Sequence / Project</th>
        <th style="width: 8%; padding: 8px; text-align: center;">Sprint</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Monday</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Tuesday</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Wednesday</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Thursday</th>
        <th style="width: 13%; padding: 8px; text-align: left;">Friday</th>
        <th style="width: 11%; padding: 8px; text-align: left;">Saturday</th>
      </tr>
    </thead>
    <tbody>
      <!-- Sequence 1: Priority Master of Arts -->
      <tr>
        <td rowspan="3" style="padding: 8px; vertical-align: top; background: rgba(128,128,128,0.05); border-bottom: 2px solid #555;">
          <strong>Seq 1: Master of Arts</strong><br>
          <span style="font-size: 0.85em; color: #888;">Website & Invoices</span>
        </td>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 1</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Buffer</td>
      </tr>
      <tr>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 2</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Review Gate</td>
      </tr>
      <tr style="border-bottom: 2px solid #555;">
        <td style="padding: 6px; text-align: center; font-weight: 600;">Sprint 3</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Archival</td>
      </tr>

      <!-- Sequence 2: Investment -->
      <tr>
        <td rowspan="3" style="padding: 8px; vertical-align: top; background: rgba(128,128,128,0.05); border-bottom: 2px solid #555;">
          <strong>Seq 2: Investment</strong><br>
          <span style="font-size: 0.85em; color: #888;">Pipeline & Dashboard</span>
        </td>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 1</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Buffer</td>
      </tr>
      <tr>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 2</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Signoff Gate</td>
      </tr>
      <tr style="border-bottom: 2px solid #555;">
        <td style="padding: 6px; text-align: center; font-weight: 600;">Sprint 3</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Data Freeze</td>
      </tr>

      <!-- Sequence 3: Apex OS -->
      <tr>
        <td rowspan="3" style="padding: 8px; vertical-align: top; background: rgba(128,128,128,0.05); border-bottom: 2px solid #555;">
          <strong>Seq 3: Apex OS</strong><br>
          <span style="font-size: 0.85em; color: #888;">OpenMouse Integration</span>
        </td>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 1</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Bench Signoff</td>
      </tr>
      <tr>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 2</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Driver Gate</td>
      </tr>
      <tr style="border-bottom: 2px solid #555;">
        <td style="padding: 6px; text-align: center; font-weight: 600;">Sprint 3</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Artifact Build</td>
      </tr>

      <!-- Sequence 4: Leela -->
      <tr>
        <td rowspan="3" style="padding: 8px; vertical-align: top; background: rgba(128,128,128,0.05); border-bottom: 2px solid #555;">
          <strong>Seq 4: Leela</strong><br>
          <span style="font-size: 0.85em; color: #888;">Skill Tree Completion</span>
        </td>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 1</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S1_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Documentation</td>
      </tr>
      <tr>
        <td style="padding: 6px; text-align: center; font-weight: 600; border-bottom: 1px solid rgba(128,128,128,0.2);">Sprint 2</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; border-bottom: 1px solid rgba(128,128,128,0.2);">{{S2_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888; border-bottom: 1px solid rgba(128,128,128,0.2);">Logic Gate</td>
      </tr>
      <tr style="border-bottom: 2px solid #555;">
        <td style="padding: 6px; text-align: center; font-weight: 600;">Sprint 3</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_MON_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_TUE_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_WED_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_THU_TASK}}</td>
        <td style="padding: 6px; vertical-align: top;">{{S3_FRI_TASK}}</td>
        <td style="padding: 6px; vertical-align: top; color: #888;">Package Validate</td>
      </tr>
    </tbody>
  </table>
</div>

## Cross-project sequence

**Must happen first:**

1. {{PRECEDING_WORK_AND_REASON}}

**Can run in parallel:**

- {{PARALLEL_WORK}}

**Should not compete for the same capacity:**

- {{COMPETING_WORK_OR_NONE}}

**Deliberately deferred:**

- {{DEFERRED_ITEM_AND_REASON_OR_NONE}}

## Review flags (include when material)

### {{FLAG_TITLE}}

- **Issue:** {{ISSUE}}
- **Why it matters this week:** {{IMPACT}}
- **Operator action:** {{RESOLUTION}}

## Provenance and confidence

Every consequential claim in this artifact carries an inline source tag `[src: <TAG>]`. Tags resolve here - exactly one hop:

| Tag | Source | Freshness class (CURRENT / AGED / STALE / UNKNOWN) |
| :--- | :--- | :--- |
| {{TAG_1}} | [{{J1_LABEL}}]({{J1_REF}}) - `{{J1_VISIBLE_REF}}` | {{FRESHNESS_CLASS_1}} |

**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Assumptions:** {{ASSUMPTIONS_WITH_TAGS_OR_NONE}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "{{ARTIFACT_REF}}"
  week: "{{WEEK_OR_DATE_RANGE}}"
  result_state: "{{RESULT_STATE}}"
  weekly_intent: "{{WEEKLY_INTENT_SUMMARY}}"
  project_priority_refs:
    - project_ref: "{{PROJECT_REF}}"
      priority_ref: "{{PRIORITY_REF}}"
  fixed_constraints:
    - "{{CONSTRAINT}}"
  review_status: "{{REVIEW_STATUS}}"
  next_consumer: "PreCap_Next_Day_Brief"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/PrecapWeek/SKILL.md"
  source_gap: ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md was referenced by the live skill but not retrievable from main during research."
```

Example: [J02 Weekly Command Brief](../../../apex-meta/operator-output-design/step4-operator-template-system/examples/master-of-arts-example-fragments.md)
