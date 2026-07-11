# Usage Learning Card - {{FLOW_OR_TASK_CONTEXT}}

> **Learning result:** {{MEANINGFUL_LEARNING | INSUFFICIENT_DATA | OPERATOR_REVIEW_NEEDED}}  
> **Planned versus actual:** {{COMPARISON_SUMMARY}}  
> **Learning signal:** {{REUSE_ROUTE | AVOID_ROUTE | USE_ONLY_FOR_HIGH_VALUE_TASKS | INSUFFICIENT_DATA | OPERATOR_REVIEW_NEEDED}}  
> **Next action:** {{ACCEPT_LEARNING | CORRECT_USAGE | CHANGE_SIGNAL | IGNORE | REQUEST_EVIDENCE | NO_ACTION}}  
> **Review needed:** {{USAGE_EVIDENCE_OR_SIGNAL_DECISION_OR_NONE}}

## Operator action

- [ ] Accept this contextual usage learning.
- [ ] Correct the actual surface or model recorded.
- [ ] Change the learning signal.
- [ ] Ignore this observation for future routing.
- [ ] Request evidence review.
- [ ] Take no action because data is insufficient.

**Decision or instruction:** {{OPERATOR_DECISION_OR_PENDING}}

## Planned and actual route

**Task context:** {{COMPARABLE_TASK_DESCRIPTION}}  
**Planned surface or model:** {{PLANNED_ROUTE_OR_UNKNOWN}}  
**Planned route reference:** `{{ROUTING_REF_OR_NONE}}`  
**Actual surface or model:** {{ACTUAL_EVIDENCED_ROUTE_OR_UNKNOWN}}  
**Actual usage evidence:** {{SOURCE_REF_OR_NOT_AVAILABLE}}  
**Usage purpose:** {{WHY_THE_ROUTE_WAS_USED}}

## Planned-versus-actual comparison

**Comparison:** {{MATCHED_PLAN | CHEAPER_OR_LIGHTER_THAN_PLANNED | HEAVIER_OR_SCARCER_THAN_PLANNED | DIFFERENT_ROUTE_USED | PLANNED_BUT_NOT_EXECUTED | EXECUTED_WITHOUT_PLAN | INSUFFICIENT_DATA}}  
**Observed difference:** {{CONCISE_DIFFERENCE}}  
**Reason supported by evidence:** {{REASON_OR_UNKNOWN}}

## Outcome quality

**Context-bound quality:** {{USEFUL | MIXED | POOR | UNKNOWN}}  
**Evidence for the rating:** {{OUTPUT_OR_OPERATOR_FEEDBACK_REF}}  
**Important limitation:** {{WHY_THIS_IS_NOT_A_GENERAL_MODEL_BENCHMARK}}

## Reuse or avoidance signal

Select exactly one accepted signal.

- [ ] `reuse_route`
- [ ] `avoid_route`
- [ ] `use_only_for_high_value_tasks`
- [ ] `insufficient_data`
- [ ] `operator_review_needed`

**Selected signal:** `{{SELECTED_SIGNAL}}`  
**Comparable future context:** {{WHEN_THE_SIGNAL_APPLIES}}  
**Do not generalize to:** {{OUT_OF_SCOPE_CONTEXT_OR_NONE}}

## Advisory future-routing hint

{{ONE_TO_THREE_SENTENCE_ADVISORY_HINT_OR_NONE}}

This hint does not change routing automatically and does not override the AI Routing Card.

## Sourced resource note (include only when explicitly sourced)

**Claim:** {{COST_TOKEN_QUOTA_OR_SCARCITY_NOTE}}  
**Source:** [{{SOURCE_LABEL}}]({{SOURCE_REF}}) - `{{SOURCE_REF}}`  
**Observed or verified on:** {{DATE_TIME}}  
**Validity limit:** {{LIMIT_OR_UNKNOWN}}

## Evidence, confidence, and review

**FlowRecap source:** [{{J7_LABEL}}]({{J7_REF}}) - `{{J7_REF}}`  
**Model-usage delta reference:** `{{MODEL_USAGE_DELTA_REF}}`  
**Evidence status:** {{SUPPORTED | PARTIAL | UNKNOWN | CONFLICTING}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Review flag:** {{FLAG_OR_NONE}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Usage_Learning_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  source_flow_recap_ref: "{{FLOW_RECAP_REF}}"
  model_usage_delta_ref: "{{MODEL_USAGE_DELTA_REF}}"
  comparison: "{{PLANNED_VS_ACTUAL_COMPARISON}}"
  route_signal: "{{SELECTED_ROUTE_SIGNAL}}"
  confidence: "{{CONFIDENCE}}"
  future_routing_hint: "{{ADVISORY_HINT_OR_NONE}}"
  operator_review_needed: "{{TRUE_OR_FALSE}}"
  next_consumer: "AI_Routing_Card"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/11-usage-learning-card-design.okf.yaml"
  round6_overlay_intent_ref: "20-round6-cross-cutting-consistency-resolution.okf.yaml"
  overlay_application_status: "intended_advisory_boundary_applied_to_presentation_only"
  domain_contract_refs:
    - ".claude/skills/model-usage-log/SKILL.md"
    - ".claude/skills/model-usage-log/references/model-usage-delta-contract.md"
    - ".claude/skills/model-usage-log/references/usage-summary-contract.md"
```

Example: [J08 Usage Learning Card](../../../../apex-meta/operator-output-design/step4-operator-template-system/examples/master-of-arts-example-fragments.md)
