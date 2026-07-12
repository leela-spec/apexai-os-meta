# AI Routing Card - {{TASK_OR_FLOW_LABEL}}

> **Routing state:** {{RECOMMENDATION_READY | READY_WITH_REVIEW | INSUFFICIENT_CONTEXT | OPERATOR_DECIDED | DEFERRED}}  
> **Recommended route:** {{STABLE_SURFACE_OR_TOOL_CLASS}}  
> **Next action:** {{APPROVE_ROUTE | CHOOSE_ALTERNATIVE | OVERRIDE | CLARIFY | DEFER | OPEN_APPROVED_EXECUTION_CONTEXT}}  
> **Review needed:** {{ROUTE_COST_SCARCITY_CAPABILITY_OR_APPROVAL_DECISION_OR_NONE}}  
> **Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}

> **Advisory only:** The recommendation does not authorize execution. J4 or J5 may consume the route only after an operator route decision is recorded.

## Operator route decision

- [ ] Approve the recommended route.
- [ ] Choose a named alternative.
- [ ] Override with a different route and reason.
- [ ] Request clarification or more evidence.
- [ ] Defer or select no route.

**Decision:** {{APPROVE_RECOMMENDATION | APPROVE_ALTERNATIVE | OVERRIDE | CLARIFY | DEFER | NO_ROUTE | PENDING}}  
**Approved route:** {{ROUTE_OR_NONE}}  
**Decision by:** {{OPERATOR}}  
**Decision date:** {{DATE_TIME_OR_PENDING}}  
**Reason or constraint:** {{NOTE_OR_NONE}}

## Task context

**Project:** {{PROJECT_REF}}  
**Flow or task:** {{TASK_DESCRIPTION}}  
**Desired output:** {{OUTPUT_AND_QUALITY_BAR}}  
**Risk or consequence level:** {{LOW | MEDIUM | HIGH_WITH_REASON}}  
**Time sensitivity:** {{DEADLINE_OR_NONE}}  
**Data, privacy, or tool constraints:** {{CONSTRAINTS_OR_NONE}}  
**Confirmed project context:** [{{J11_LABEL}}]({{J11_REF}}) - `{{J11_REF}}`

## Advisory recommendation

**Stable surface or tool class:** {{RECOMMENDED_SURFACE_CLASS}}  
**Execution mode:** {{INTERACTIVE | DEEP_RESEARCH | CODE_OR_TOOL_USE | DOCUMENT_SYNTHESIS | OTHER_STABLE_CLASS}}  
**Why it fits this task:**

- {{TASK_ROUTE_FIT_REASON}}

**Key constraints:**

- {{CAPABILITY_COST_SCARCITY_PRIVACY_OR_TIME_CONSTRAINT}}

**Fallback route:** {{FALLBACK_SURFACE_CLASS}}  
**Do not use when:** {{CONDITION_OR_NONE}}

## Evidence and confidence

**Usage-learning references:**

- [{{J8_LABEL}}]({{J8_REF}}) - `{{J8_REF}}`

**Other route evidence:** {{CURRENT_CAPABILITY_OR_POLICY_REFS}}  
**Evidence status:** {{SUPPORTED | PARTIAL | STALE | INSUFFICIENT}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Material uncertainty:** {{UNCERTAINTY_OR_NONE}}

## Exact model recommendation (include only with current verification)

**Exact model:** {{MODEL_NAME}}  
**Verification source:** [{{SOURCE_LABEL}}]({{SOURCE_REF}}) - `{{SOURCE_REF}}`  
**Verified on:** {{DATE_TIME}}  
**Validity window or recheck trigger:** {{WINDOW_OR_TRIGGER}}  
**Known availability, limit, or pricing caveat:** {{CAVEAT_OR_NONE}}

Remove this section when exact current model truth is not verified. Keep the stable surface recommendation instead.

## Alternatives

### Alternative 1 - {{SURFACE_OR_TOOL_CLASS}}

- **Use when:** {{CONDITION}}
- **Trade-off:** {{QUALITY_SPEED_COST_SCARCITY_OR_CONTROL_TRADEOFF}}
- **Evidence:** `{{REF_OR_NONE}}`

### Alternative 2 - {{SURFACE_OR_TOOL_CLASS}}

- **Use when:** {{CONDITION}}
- **Trade-off:** {{TRADEOFF}}
- **Evidence:** `{{REF_OR_NONE}}`

## Consequence of the operator decision

- **Approved:** the selected route may be passed as execution context to J4 and prompt context to J5.
- **Overridden:** preserve both the recommendation and the operator-selected route; execution uses the operator route.
- **Deferred or no route:** do not treat the recommendation as authorization to execute.
- **Clarify:** request only the missing context that would change the route.

## Approved execution handoff (complete only after an operator decision)

**Approval status:** {{APPROVED | NOT_APPROVED | OVERRIDDEN | DEFERRED}}  
**Route to carry:** {{APPROVED_ROUTE_OR_NONE}}  
**Flow Execution Card reference:** `{{J4_REF_OR_PENDING}}`  
**Prompt Files and Index reference:** `{{J5_REF_OR_PENDING}}`  
**Conditions to preserve:** {{CONDITIONS_OR_NONE}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "AI_Routing_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  task_ref: "{{TASK_OR_FLOW_REF}}"
  selected_surface_class: "{{RECOMMENDED_SURFACE_CLASS}}"
  verified_model_ref: "{{VERIFIED_EXACT_MODEL_REF_OR_NONE}}"
  recommendation_confidence: "{{CONFIDENCE}}"
  operator_route_decision: "{{OPERATOR_DECISION}}"
  operator_approved_route: "{{APPROVED_ROUTE_OR_NONE}}"
  approval_status: "{{APPROVAL_STATUS}}"
  usage_learning_refs:
    - "{{USAGE_LEARNING_REF_OR_NONE}}"
  next_consumers:
    - "{{FLOW_EXECUTION_CARD_OR_NONE}}"
    - "{{PROMPT_FILES_AND_INDEX_OR_NONE}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/17-ai-routing-card-design.okf.yaml"
  round6_overlay_intent_ref: "round6-patches/07-j12-routing-contract-alignment.patch"
  overlay_application_status: "intended_guidance_not_applied_by_this_package"
  domain_contract_refs:
    - ".claude/skills/AIRouting/SKILL.md"
    - ".claude/skills/AIRouting/routing-recommendation-packet-contract.md"
```

Example: [J12 AI Routing Card](../examples/master-of-arts-example-fragments.md#j12-ai-routing-card)
