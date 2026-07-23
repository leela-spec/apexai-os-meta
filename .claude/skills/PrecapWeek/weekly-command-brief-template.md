# Weekly Command Brief - {{WEEK_OR_DATE_RANGE}}

> **Weekly state:** {{READY | READY_WITH_REVIEW | PARTIAL | BLOCKED}}  
> **Direction:** {{TWO_TO_FIVE_SENTENCE_PORTFOLIO_DIRECTION}}  
> **Next action:** {{APPROVE_WEEK | EDIT_PRIORITIES | REDUCE_SCOPE | RESOLVE_CONSTRAINT | REJECT_DIRECTION}}  
> **Review needed:** {{HIGHEST_IMPACT_WEEKLY_DECISION_OR_NONE}}  
> **Scope:** {{ACTIVE_PROJECT_COUNT}} projects; {{MAJOR_OUTCOME_COUNT}} major outcomes

## Operator decision

- [ ] Approve the week as the planning basis.
- [ ] Edit project priorities or planned work.
- [ ] Reduce scope or defer a named outcome.
- [ ] Resolve a capacity, dependency, or decision constraint.
- [ ] Reject and reframe the weekly direction.

**Decision or instruction:** {{OPERATOR_DECISION_OR_PENDING}}

## Weekly direction

**Weekly intent:** {{WHAT_THE_PORTFOLIO_SHOULD_ACCOMPLISH}}  
**Success at week end:**

- {{MAJOR_CROSS_PROJECT_OUTCOME}}

**Capacity and constraints:**

- {{AVAILABLE_CAPACITY_OR_FIXED_CONSTRAINT}}

**Major operator decisions:**

- {{DECISION_NEEDED_OR_NONE}}

## Project - {{PROJECT_NAME}} (repeat per active project)

**Weekly target:** {{PROJECT_LEVEL_TARGET}}  
**Why this week:** {{TIMING_OR_LEVERAGE_REASON}}  
**Success evidence:** {{WHAT_WILL_DEMONSTRATE_PROGRESS}}

### Priorities and desired results

1. **{{PRIORITY}}** - {{DESIRED_RESULT}}

### Planned work

- **Work item:** {{ACTIONABLE_WORK_ITEM}}
  - Expected output: {{OUTPUT_OR_ARTIFACT}}
  - Owner or executor: {{OWNER_OR_OPERATOR}}
  - Dependency: {{DEPENDENCY_OR_NONE}}
  - Candidate day: {{DAY_OR_UNASSIGNED}}

### Blockers, risks, and decisions

- **Blocker or risk:** {{ITEM_OR_NONE}}
- **Decision needed:** {{DECISION_OR_NONE}}
- **Response this week:** {{MITIGATION_OR_OPERATOR_ACTION}}

### Expected outputs

- [{{OUTPUT_LABEL}}]({{OUTPUT_REF_OR_PLANNED_PATH}}) - `{{VISIBLE_REF_OR_PATH}}`

## Cross-project sequence

**Must happen first:**

1. {{PRECEDING_WORK_AND_REASON}}

**Can run in parallel:**

- {{PARALLEL_WORK}}

**Should not compete for the same capacity:**

- {{COMPETING_WORK_OR_NONE}}

**Deliberately deferred:**

- {{DEFERRED_ITEM_AND_REASON_OR_NONE}}

## Daily seed map (include when useful; not a frozen day plan)

- **{{WEEKDAY}}:** {{CANDIDATE_PROJECTS_AND_LIKELY_OUTCOME}}
  - Dependency or constraint: {{SUMMARY_OR_NONE}}

Final day-level planning remains owned by the PreCap Next Day Brief.

## Review flags (include when material)

### {{FLAG_TITLE}}

- **Issue:** {{ISSUE}}
- **Why it matters this week:** {{IMPACT}}
- **Operator action:** {{RESOLUTION}}

## Provenance and confidence

**Project-state input:** [{{J1_LABEL}}]({{J1_REF}}) - `{{J1_VISIBLE_REF}}`  
**Other decisive sources:** {{SOURCE_REFS_OR_NONE}}  
**Freshness:** {{FRESHNESS_STATUS}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Assumptions:** {{ASSUMPTIONS_OR_NONE}}

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
