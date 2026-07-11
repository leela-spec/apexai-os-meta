# Flow Execution Card - {{FLOW_TITLE}}

> **Readiness:** {{READY | READY_WITH_REVIEW | PARTIAL_CONTEXT | BLOCKED}}  
> **Outcome target:** {{FLOW_GOALS_AND_EXPECTED_OUTPUTS_IN_ONE_TO_THREE_SENTENCES}}  
> **Next action:** {{EXECUTE_NEXT_SPRINT | OPEN_PROMPT_FILE | RESOLVE_REVIEW | EDIT_SCOPE | DEFER}}  
> **Review needed:** {{MOST_IMPORTANT_EXECUTION_DECISION_OR_NONE}}  
> **Warning:** {{BLOCKER_DEGRADED_PROMPT_OR_MISSING_INPUT_OR_REMOVE_LINE}}

## Start or resume here

**Current sprint:** {{S1 | S2 | S3 | FLOW_COMPLETE | NOT_STARTED}}  
**Current status:** {{NOT_STARTED | IN_PROGRESS | WAITING | BLOCKED | COMPLETE}}  
**Exact next operator step:** {{ONE_CONCRETE_ACTION}}  
**Last confirmed checkpoint:** {{CHECKPOINT_OR_NONE}}

## Operator controls

- [ ] Execute the next sprint.
- [ ] Open the named prompt file.
- [ ] Edit scope or reorder only where dependencies allow.
- [ ] Request review, defer, mark blocked, or skip with a reason.

**Operator instruction:** {{INSTRUCTION_OR_PENDING}}

## Flow identity and context

**Flow ID:** `{{FLOW_ID}}`  
**Project:** {{PROJECT}}  
**Why today:** {{WHY_THIS_FLOW_IS_SCHEDULED}}  
**Weekly priority advanced:** {{WEEKLY_PRIORITY_SUMMARY}}  
**Project-state signal:** {{FLOW_RELEVANT_CONFIRMED_STATE}}  
**Approved route:** {{OPERATOR_APPROVED_ROUTE_OR_NOT_PROVIDED}}  
**Routing reference:** [{{ROUTING_LABEL}}]({{ROUTING_REF}}) - `{{ROUTING_REF}}`

### Goals

- {{FLOW_GOAL}}

### Expected outputs

- {{EXPECTED_OUTPUT_WITH_DESTINATION_OR_REF}}

## Inputs and dependencies

### Available inputs

- [{{INPUT_LABEL}}]({{INPUT_REF}}) - `{{INPUT_REF}}`

### Missing inputs (include when material)

- {{MISSING_INPUT}} - resolution: {{HOW_TO_RESOLVE}}

### Flow dependencies

- **Depends on:** {{UPSTREAM_DEPENDENCY_OR_NONE}}
- **Required before:** {{DOWNSTREAM_CONSTRAINT_OR_NONE}}
- **External gate:** {{OPERATOR_OR_PROFESSIONAL_GATE_OR_NONE}}

## S1 - {{S1_GOAL}}

**Sprint status:** {{NOT_STARTED | IN_PROGRESS | WAITING | BLOCKED | COMPLETE}}

### Tasks

1. {{S1_TASK}}

### Inputs

- [{{S1_INPUT_LABEL}}]({{S1_INPUT_REF}}) - `{{S1_INPUT_REF}}`

### Prompt access

- [Open S1 prompt file]({{S1_PROMPT_FILE}}) - `{{S1_PROMPT_FILE}}`
- **Recommended surface:** {{S1_TARGET_SURFACE}}
- **Routing reference:** `{{S1_ROUTING_REF}}`
- **Prompt readiness:** {{READY | DEGRADED | MISSING | NOT_REQUIRED}}

### Expected outputs

- {{S1_EXPECTED_OUTPUT}}

### Done when

- {{S1_EVIDENCE_BASED_DONE_CONDITION}}

### Stop or review conditions

- {{S1_STOP_REVIEW_CONDITION_OR_NONE}}

### Evidence to retain

- {{S1_EVIDENCE_ITEM_OR_REF}}

## S2 - {{S2_GOAL}}

**Sprint status:** {{NOT_STARTED | IN_PROGRESS | WAITING | BLOCKED | COMPLETE}}  
**Dependency on S1:** {{S1_OUTPUT_OR_DECISION_REQUIRED}}

### Tasks

1. {{S2_TASK}}

### Inputs

- [{{S2_INPUT_LABEL}}]({{S2_INPUT_REF}}) - `{{S2_INPUT_REF}}`

### Prompt access

- [Open S2 prompt file]({{S2_PROMPT_FILE}}) - `{{S2_PROMPT_FILE}}`
- **Recommended surface:** {{S2_TARGET_SURFACE}}
- **Routing reference:** `{{S2_ROUTING_REF}}`
- **Prompt readiness:** {{READY | DEGRADED | MISSING | NOT_REQUIRED}}

### Expected outputs

- {{S2_EXPECTED_OUTPUT}}

### Done when

- {{S2_EVIDENCE_BASED_DONE_CONDITION}}

### Stop or review conditions

- {{S2_STOP_REVIEW_CONDITION_OR_NONE}}

### Evidence to retain

- {{S2_EVIDENCE_ITEM_OR_REF}}

## S3 - Capture, decision, and handoff

**Sprint status:** {{NOT_STARTED | IN_PROGRESS | WAITING | BLOCKED | COMPLETE}}  
**Capture goal:** {{WHAT_MUST_BE_PRESERVED_FOR_RECAP_AND_HANDOFF}}

### Evidence tasks

1. {{EVIDENCE_CAPTURE_TASK}}

### Decisions to record

- {{DECISION_OR_NONE}}

### Handoff preparation

- {{HANDOFF_TASK_AND_TARGET}}

### Optional prompt access

- [Open S3 prompt file]({{S3_PROMPT_FILE}}) - `{{S3_PROMPT_FILE}}`

### Done when

- {{S3_CAPTURE_AND_HANDOFF_DONE_CONDITION}}

## End-of-flow check

- [ ] Planned outputs are checked against actual outputs.
- [ ] Actual completion state is recorded: {{COMPLETED | PARTIAL | BLOCKED | SKIPPED | UNKNOWN}}.
- [ ] Evidence references are identifiable.
- [ ] Decisions, blockers, and unresolved questions are separated.
- [ ] Evidence is ready for J6 or the exact missing item is named.

**Actual completion state:** {{COMPLETION_STATE_OR_PENDING}}  
**Evidence handoff target:** [{{J6_LABEL}}]({{J6_REF}}) - `{{J6_REF}}`  
**End-of-flow review:** {{REVIEW_OR_NONE}}

## Material review flags (include when needed)

### {{FLAG_TITLE}}

- **Issue:** {{ISSUE}}
- **Why it matters to execution:** {{IMPACT}}
- **Operator action:** {{RESOLUTION}}

## Provenance and confidence

**Day-plan reference:** [{{J3_LABEL}}]({{J3_REF}}) - `{{J3_REF}}`  
**Project-state reference:** `{{PROJECT_STATE_REF}}`  
**Weekly-plan reference:** `{{WEEKLY_PLAN_REF}}`  
**Input freshness:** {{FRESHNESS_STATUS}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Consequential assumptions:** {{ASSUMPTIONS_OR_NONE}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  flow_id: "{{FLOW_ID}}"
  project_ref: "{{PROJECT_REF}}"
  readiness: "{{READINESS}}"
  current_sprint: "{{CURRENT_SPRINT}}"
  prompt_index_ref: "{{PROMPT_INDEX_REF}}"
  approved_route_ref: "{{APPROVED_ROUTE_REF_OR_NONE}}"
  evidence_handoff_ref: "{{EVIDENCE_HANDOFF_REF_OR_PENDING}}"
  review_status: "{{REVIEW_STATUS}}"
  next_consumer: "{{PROMPT_FILES_AND_INDEX_OR_OPERATOR_EXECUTION_OR_EXECUTION_EVIDENCE_HANDOFF}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
    - ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
```

Example: [J04 Flow Execution Card](../../../../apex-meta/operator-output-design/step4-operator-template-system/examples/master-of-arts-example-fragments.md)
