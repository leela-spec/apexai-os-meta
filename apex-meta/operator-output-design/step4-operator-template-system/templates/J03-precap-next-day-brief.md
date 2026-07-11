# PreCap Next Day Brief - {{EXECUTION_DATE}}

> **Day state:** {{READY | READY_WITH_REVIEW | PARTIAL | BLOCKED}}  
> **Day direction:** {{TWO_TO_FIVE_SENTENCE_DAY_SUMMARY}}  
> **Next action:** {{APPROVE_DAY | OPEN_FIRST_FLOW_CARD | REORDER | EDIT_SCOPE | DEFER_FLOW}}  
> **Review needed:** {{MOST_IMPORTANT_PRE_EXECUTION_DECISION_OR_NONE}}  
> **Plan size:** {{FLOW_COUNT}} flows; {{TOTAL_SPRINT_COUNT}} visible sprints

## Approve or change the day

- [ ] Approve the day outline.
- [ ] Open the first Flow Execution Card.
- [ ] Reorder flows or sprint sequence.
- [ ] Edit, compress, defer, or block a named flow with a reason.

**Decision or instruction:** {{OPERATOR_DECISION_OR_PENDING}}

## Day frame

**Primary day outcomes:**

- {{DAY_OUTCOME}}

**Projects touched and why:**

- **{{PROJECT}}:** {{WHY_THIS_PROJECT_TODAY}}

**Continuity from the week:** {{WEEKLY_PRIORITY_TRACE_SUMMARY}}  
**Capacity assumption:** {{CAPACITY_ASSUMPTION}}  
**Fixed constraints:** {{CONSTRAINTS_OR_NONE}}

## Flow {{ORDER}} - {{FLOW_TITLE}} (repeat per represented flow)

**Flow ID:** `{{FLOW_ID}}`  
**Project:** {{PROJECT}}  
**Status:** {{PLANNED | COMPRESSED | SKIPPED | BLOCKED | OMITTED}}  
**Why today:** {{SHORT_REASON}}  
**Weekly priority advanced:** {{PRIORITY_TRACE}}  
**Expected flow output:** {{OUTPUT_SUMMARY}}  
**Open full workspace:** [Open Flow Execution Card]({{FLOW_EXECUTION_CARD_REF}}) - `{{FLOW_EXECUTION_CARD_REF}}`

- **S1 - {{S1_GOAL}}:** {{S1_SHORT_INTENT}} -> {{S1_EXPECTED_OUTPUT_SUMMARY}}
- **S2 - {{S2_GOAL}}:** {{S2_SHORT_INTENT}}; dependency cue: {{S2_DEPENDENCY_SUMMARY}} -> {{S2_EXPECTED_OUTPUT_SUMMARY}}
- **S3 - {{S3_GOAL}}:** {{S3_CAPTURE_OR_HANDOFF_INTENT}} -> {{S3_EXPECTED_HANDOFF_SUMMARY}}

**Review flag:** {{FLOW_LEVEL_REVIEW_FLAG_OR_NONE}}

## Cross-flow execution order

1. `{{FLOW_ID}} / {{SPRINT}}` - {{WHY_THIS_POSITION}}

## Expected end of day

**Project progress expected:**

- {{EXPECTED_PROJECT_PROGRESS}}

**Artifacts or decisions expected:**

- {{EXPECTED_ARTIFACT_OR_DECISION}}

**Evidence and handoffs to prepare:**

- {{EVIDENCE_OR_HANDOFF_SUMMARY}}

## Review flags (include when material)

### {{FLAG_TITLE}}

- **Issue:** {{MISSING_CONTEXT_BLOCKER_OR_CONFLICT}}
- **Why it matters before execution:** {{IMPACT}}
- **Operator action:** {{RESOLUTION}}

## Planning context used

**Project-state source:** [{{J1_LABEL}}]({{J1_REF}}) - `{{J1_VISIBLE_REF}}`  
**Weekly source:** [{{J2_LABEL}}]({{J2_REF}}) - `{{J2_VISIBLE_REF}}`  
**Recent execution signal:** {{RECENT_EXECUTION_REF_OR_NONE}}  
**Deferred or ignored signal:** {{SIGNAL_AND_REASON_OR_NONE}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "PreCap_Next_Day_Brief"
  artifact_ref: "{{ARTIFACT_REF}}"
  execution_date: "{{EXECUTION_DATE}}"
  result_state: "{{DAY_STATE}}"
  ordered_flows:
    - order: "{{ORDER}}"
      flow_id: "{{FLOW_ID}}"
      project_ref: "{{PROJECT_REF}}"
      flow_status: "{{FLOW_STATUS}}"
      weekly_priority_ref: "{{WEEKLY_PRIORITY_REF}}"
      flow_execution_card_ref: "{{FLOW_EXECUTION_CARD_REF}}"
  review_status: "{{REVIEW_STATUS}}"
  next_consumer: "Flow_Execution_Card"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml"
  round6_overlay_intent_ref: "round6-patches/02-j3-j4-depth-separation.patch"
  overlay_application_status: "intended_guidance_not_applied_by_this_package"
  domain_contract_refs:
    - ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    - ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
    - ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
```

Example: [J03 PreCap Next Day Brief](../examples/master-of-arts-example-fragments.md#j03-precap-next-day-brief)
