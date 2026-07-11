# FlowRecap Result Card - {{FLOW_TITLE_OR_ID}}

> **Flow result:** {{COMPLETED | PARTIALLY_COMPLETED | BLOCKED | SKIPPED | ABANDONED | UNKNOWN}}  
> **What changed:** {{EVIDENCE_SUPPORTED_RESULT_SUMMARY}}  
> **Next action:** {{APPROVE_CANDIDATE_FOR_REVIEW | EDIT_CANDIDATE | REQUEST_EVIDENCE | DEFER | NO_ACTION}}  
> **Review needed:** {{CANDIDATE_OR_EVIDENCE_DECISION_OR_NONE}}  
> **Confidence:** {{SHOW_WHEN_BELOW_HIGH_OR_MATERIAL}}

> **Candidate only:** Any project-state change below is proposed for downstream review. It is not approved, written, merged, or confirmed project truth.

## Operator actions

- [ ] Approve the candidate for downstream merge review.
- [ ] Edit or reject the candidate.
- [ ] Defer pending named evidence.
- [ ] Request the exact missing evidence item.
- [ ] Send the usage candidate to usage learning.
- [ ] Take no action when no supported change exists.

**Operator instruction:** {{INSTRUCTION_OR_PENDING}}

## Planned versus actual

**Planned intent:** {{COMPACT_PLAN_SUMMARY_WITH_FLOW_CARD_REF}}  
**Actual work:** {{EVIDENCE_SUPPORTED_ACTUAL_SUMMARY}}  
**Material variance:** {{VARIANCE_AND_REASON_OR_NONE}}

Do not repeat the full Flow Execution Card here.

## Outcomes and artifacts

### Completed outcomes

- {{COMPLETED_OUTCOME_WITH_EVIDENCE_REF}}

### Incomplete or out-of-scope items

- {{INCOMPLETE_ITEM_AND_REASON_OR_NONE}}

### Created or changed artifacts

- [{{ARTIFACT_LABEL}}]({{ARTIFACT_REF}}) - `{{ARTIFACT_REF}}`
  - Evidence status: {{CONFIRMED | INFERRED | UNCERTAIN | CONFLICTING}}

## Decisions

- **Made:** {{DECISION_OR_NONE}}
- **Proposed:** {{PROPOSAL_OR_NONE}}
- **Deferred:** {{DEFERRED_DECISION_OR_NONE}}
- **Needs operator validation:** {{DECISION_OR_NONE}}

## Blockers or failures

- **Item:** {{BLOCKER_FAILURE_OR_NONE}}
- **Effect:** {{EFFECT_ON_RESULT}}
- **Evidence reference:** `{{SOURCE_REF_OR_NONE}}`

## Unresolved questions

- {{QUESTION_OR_NONE}}

## Candidate project-state change

**Candidate status:** {{CANDIDATE | PROPOSED | NO_STATE_CHANGE_PROPOSED | NOT_ENOUGH_EVIDENCE}}  
**Project:** {{PROJECT_REF}}  
**Current accepted value:** {{CURRENT_VALUE_OR_UNKNOWN}}  
**Proposed value:** {{PROPOSED_VALUE_OR_NONE}}  
**Why the evidence supports this candidate:** {{CONCISE_RATIONALE}}  
**Supporting evidence:**

- `{{EVIDENCE_REF}}`

**Conflicts or limits:** {{CONFLICTS_GAPS_OR_NONE}}  
**Ready for downstream review:** {{YES | NO}}  
**Required reviewer decision:** {{APPROVE | EDIT | REJECT | DEFER | REQUEST_EVIDENCE | NONE}}

## Advisory usage evidence reference

**Usage evidence found:** {{YES | NO | UNKNOWN}}  
**Observed surface or model:** {{EVIDENCED_VALUE_OR_UNKNOWN}}  
**Usage purpose:** {{TASK_CONTEXT}}  
**Usage candidate reference:** `{{MODEL_USAGE_DELTA_CANDIDATE_REF_OR_NONE}}`  
**Handoff status:** {{READY_FOR_USAGE_LEARNING | REVIEW_NEEDED | ABSENT}}

## Evidence and confidence

**Evidence handoff:** [{{J6_LABEL}}]({{J6_REF}}) - `{{J6_REF}}`  
**Evidence status:** {{COMPLETE | PARTIAL | CONFLICTING | INSUFFICIENT}}  
**Main supporting references:** {{SOURCE_REFS}}  
**Unsupported conclusions excluded:** {{LIMITS_OR_NONE}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}

## Downstream handoffs

**Candidate destination:** {{STATUS_MERGE | NONE}}  
**Usage destination:** {{USAGE_LEARNING | NONE}}  
**Proposed operational next step:** {{PROPOSAL_OR_NONE}}

A proposed next step is not a next-day plan and does not authorize execution.

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "FlowRecap_Result_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  flow_recap_packet_ref: "{{FLOW_RECAP_PACKET_REF}}"
  flow_result: "{{FLOW_RESULT}}"
  evidence_status: "{{EVIDENCE_STATUS}}"
  candidate_project_status_delta_ref: "{{CANDIDATE_DELTA_REF_OR_NO_STATE_CHANGE}}"
  model_usage_delta_candidate_ref: "{{USAGE_CANDIDATE_REF_OR_NONE}}"
  next_step_proposal_ref: "{{NEXT_STEP_PROPOSAL_REF_OR_NONE}}"
  operator_review_flags:
    - "{{REVIEW_FLAG_OR_NONE}}"
  confidence: "{{CONFIDENCE}}"
  next_consumers:
    - "{{USAGE_LEARNING_CARD_OR_NONE}}"
    - "{{STATUS_MERGE_DECISION_CARD_OR_NONE}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/10-flow-recap-result-card-design.okf.yaml"
  round6_overlay_intent_ref: "20-round6-cross-cutting-consistency-resolution.okf.yaml"
  overlay_application_status: "intended_state_boundary_applied_to_presentation_only"
  domain_contract_refs:
    - ".claude/skills/flow-recap/SKILL.md"
    - ".claude/skills/flow-recap/references/flow-recap-packet-contract.md"
    - ".claude/skills/flow-recap/references/project-status-delta-contract.md"
```

Example: [J07 FlowRecap Result Card](../examples/master-of-arts-example-fragments.md#j07-flowrecap-result-card)
