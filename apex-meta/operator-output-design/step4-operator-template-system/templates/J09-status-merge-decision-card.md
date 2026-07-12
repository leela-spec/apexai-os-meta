# Status Merge Decision Card - {{PROJECT_OR_CANDIDATE_LABEL}}

> **Merge decision state:** {{PENDING_REVIEW | APPROVED_FOR_SESSION_MUTATION | REJECTED | DEFERRED | UNRESOLVED}}
> **Decision summary:** {{WHAT_THE_CANDIDATE_WOULD_CHANGE}}  
> **Next action:** {{APPROVE_FOR_MERGE | EDIT | REJECT | DEFER | REQUEST_EVIDENCE | SEND_TO_SESSION_MUTATION}}
> **Review needed:** {{CONFLICT_OR_OPERATOR_DECISION_OR_NONE}}  
> **Durable write:** {{NOT_PERFORMED_HERE | J10_REFERENCE_AVAILABLE}}

> **Boundary:** This card records the operator merge decision only. Approval permits Apex Session to perform the owning project-state mutation; J10 alone reports the write result, and J11 alone projects confirmed accepted truth.

## Operator merge decision

- [ ] Approve the candidate for merge and send it to J10.
- [ ] Edit the candidate before approval.
- [ ] Reject the candidate.
- [ ] Defer pending named evidence or timing.
- [ ] Mark unresolved because evidence or current state conflicts.

**Decision:** {{APPROVE_FOR_MERGE | EDIT | REJECT | DEFER | UNRESOLVED | PENDING}}  
**Decision by:** {{OPERATOR_OR_REVIEWER}}  
**Decision date:** {{DATE_TIME_OR_PENDING}}  
**Decision note:** {{CONCISE_RATIONALE}}

## Candidate review

**Candidate reference:** [{{J7_CANDIDATE_LABEL}}]({{J7_CANDIDATE_REF}}) - `{{J7_CANDIDATE_REF}}`  
**Project:** {{PROJECT_REF}}  
**Target field or accepted-state area:** {{TARGET}}  
**Current accepted value:** {{CURRENT_VALUE}}  
**Candidate value:** {{CANDIDATE_VALUE}}  
**Proposed effect:** {{WHAT_CHANGES_IF_APPROVED}}  
**No-change alternative:** {{ALTERNATIVE_OR_NONE}}

## Evidence and provenance

**Supporting evidence:**

- [{{EVIDENCE_LABEL}}]({{EVIDENCE_REF}}) - `{{EVIDENCE_REF}}`

**Evidence status:** {{SUFFICIENT | PARTIAL | CONFLICTING | INSUFFICIENT}}  
**Freshness:** {{CURRENT | STALE | MIXED | UNKNOWN}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Source gap:** {{GAP_OR_NONE}}

## Conflicts and consequences (include when material)

### {{CONFLICT_TITLE}}

- **Conflict:** {{CURRENT_AND_CANDIDATE_CONFLICT}}
- **Why it matters:** {{IMPACT_ON_ACCEPTED_STATE_OR_DOWNSTREAM_WORK}}
- **Required resolution:** {{OPERATOR_ACTION}}

**Consequence of approval:** {{WHAT_J10_WILL_BE_AUTHORIZED_TO_PREPARE_OR_WRITE}}  
**Consequence of rejection or deferral:** {{WHAT_REMAINS_UNCHANGED}}

## Approved change for J10 (complete only after approval)

**Approval state:** {{APPROVED_FOR_MERGE | NOT_APPROVED}}  
**Approved value:** {{APPROVED_VALUE_OR_NONE}}  
**Target destination:** {{SESSION_MUTATION_TARGET_OR_UNRESOLVED}}
**Required provenance to retain:** {{SOURCE_REFS}}  
**Operator conditions:** {{CONDITIONS_OR_NONE}}

## Downstream J10 reference (optional; navigation only)

**J10 card or result reference:** [{{J10_LABEL}}]({{J10_RESULT_REF}}) - `{{J10_RESULT_REF_OR_NONE}}`  
**Status as reported by J10:** {{NOT_STARTED | PREPARED | EXECUTED | PARTIAL | SKIPPED | BLOCKED | UNKNOWN}}

This reference does not make J9 the write authority. Read J10 for the durable result and J11 for confirmed accepted project truth.

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Status_Merge_Decision_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  candidate_status_delta_ref: "{{CANDIDATE_STATUS_DELTA_REF}}"
  project_ref: "{{PROJECT_REF}}"
  approval_state: "{{APPROVAL_STATE}}"
  approved_change_ref: "{{APPROVED_CHANGE_REF_OR_NONE}}"
  operator_decision_ref: "{{OPERATOR_DECISION_REF}}"
  review_status: "{{REVIEW_STATUS}}"
  next_consumer: "{{PROJECT_STATE_UPDATE_RECEIPT_OR_OPERATOR_REVIEW_OR_NONE}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/14-status-merge-decision-card-design.okf.yaml"
  round6_overlay_intent_ref: "round6-patches/03-j9-durable-merge-confirmation.patch"
  overlay_application_status: "intended_guidance_not_applied_by_this_package"
  domain_contract_refs:
    - ".claude/skills/status-merge/SKILL.md"
    - ".claude/skills/status-merge/references/status-merge-packet-contract.md"
```

Example: [J09 Status Merge Decision Card](../examples/master-of-arts-example-fragments.md#j09-status-merge-decision-card)
