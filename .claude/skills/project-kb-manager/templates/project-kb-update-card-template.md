# Project KB Update Card - {{PROJECT_AND_UPDATE_LABEL}}

> **Write state:** {{PREPARED | AWAITING_CONFIRMATION | EXECUTED | PARTIALLY_EXECUTED | SKIPPED | BLOCKED}}  
> **Durable effect:** {{EFFECTIVE_CHANGE_OR_NOT_YET_WRITTEN}}  
> **Next action:** {{CONFIRM_WRITE | EXECUTE_APPROVED_WRITE | VERIFY_RESULT | RESOLVE_FAILURE | SEND_CONFIRMED_RESULT_TO_OVERVIEW | NO_ACTION}}  
> **Review needed:** {{WRITE_TARGET_CONTENT_OR_FAILURE_DECISION_OR_NONE}}  
> **Result reference:** {{DURABLE_RESULT_REF_OR_NOT_AVAILABLE}}

> **Boundary:** A prepared update is not a durable result. J11 may use new truth only after an executed write has an identifiable result reference and effective value.

## Operator write control

- [ ] Confirm the prepared write.
- [ ] Execute the already approved write through the owning KB process.
- [ ] Verify the durable result and effective value.
- [ ] Resolve a partial, skipped, or blocked write.
- [ ] Send only the confirmed result to J11.

**Write instruction or confirmation:** {{OPERATOR_INSTRUCTION_OR_PENDING}}

## Approved input

**J9 decision reference:** [{{J9_LABEL}}]({{J9_REF}}) - `{{J9_REF}}`  
**Approval state received:** {{APPROVED_FOR_MERGE}}  
**Approved by:** {{OPERATOR_OR_REVIEWER}}  
**Approved value:** {{APPROVED_VALUE}}  
**Approval conditions:** {{CONDITIONS_OR_NONE}}

If the J9 input is not approved for merge, stop and return it for review.

## Update target and intent

**Project:** {{PROJECT_REF}}  
**Destination:** {{EXPLICIT_KB_FILE_OR_RECORD_REF}}  
**Target section or field:** {{TARGET_LOCATION}}  
**Change type:** {{ADD | CORRECT | SUPERSEDE | CONSOLIDATE | NO_UPDATE | OPERATOR_REVIEW_NEEDED}}  
**Write intent:** {{APPEND | REPLACE_EXPLICIT_TARGET | OTHER_CONTRACT_ALLOWED_OPERATION}}  
**Expected effect:** {{WHAT_SHOULD_BE_TRUE_AFTER_A_SUCCESSFUL_WRITE}}

## Prepared update

### Current durable content

{{CURRENT_CONTENT_OR_REFERENCE}}

### Proposed durable content

{{PROPOSED_CONTENT}}

### Provenance to retain

- [{{SOURCE_LABEL}}]({{SOURCE_REF}}) - `{{SOURCE_REF}}`

### Pre-write checks

- [ ] Destination and target are explicit.
- [ ] The proposed content matches the approved J9 value.
- [ ] Conflicts, stale content, and replacement scope are visible.
- [ ] The operation follows the owning write rules.
- [ ] No unrelated durable state will be changed.

## Write execution

**Confirmation received:** {{YES | NO | NOT_REQUIRED_BY_OWNER_CONTRACT}}  
**Execution attempted:** {{YES | NO}}  
**Execution date:** {{DATE_TIME_OR_NOT_EXECUTED}}  
**Executor or owning process:** {{EXECUTOR_OR_SKILL}}  
**Operation performed:** {{ACTUAL_APPEND_REPLACE_OR_NONE}}

## Actual durable result

**Write status:** {{EXECUTED | PARTIALLY_EXECUTED | SKIPPED | BLOCKED | NOT_EXECUTED}}  
**Result or receipt reference:** [{{RESULT_LABEL}}]({{RESULT_REF}}) - `{{RESULT_REF_OR_NONE}}`  
**Effective durable value:** {{EFFECTIVE_VALUE_OR_NOT_CONFIRMED}}  
**Target after write:** {{POST_WRITE_TARGET_REF_OR_NOT_CONFIRMED}}  
**Freshness date:** {{DATE_TIME_OR_NOT_CONFIRMED}}  
**Verification method:** {{READ_BACK_RECEIPT_DIFF_OR_OTHER_EVIDENCE}}  
**Difference from approved intent:** {{DIFFERENCE_OR_NONE}}

## Failure or partial-write handling (include when material)

### {{FAILURE_TITLE}}

- **Observed result:** {{WHAT_HAPPENED}}
- **Durable effect known:** {{YES_NO_OR_PARTIAL_WITH_DETAIL}}
- **Risk:** {{WHY_RETRY_OR_OVERVIEW_USE_COULD_BE_UNSAFE}}
- **Required action:** {{RESOLVE_VERIFY_RETRY_OR_ROLL_BACK_PER_OWNER_RULES}}

A skipped, blocked, unknown, or unverified write must not be presented to J11 as effective project truth.

## J11 readiness

**Ready for Project Status Overview:** {{YES_ONLY_IF_CONFIRMED | NO}}  
**Confirmed result reference:** `{{RESULT_REF_OR_NONE}}`  
**Accepted value to project:** {{EFFECTIVE_VALUE_OR_NONE}}  
**Freshness to carry:** {{FRESHNESS_OR_NONE}}  
**Residual review flag:** {{FLAG_OR_NONE}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Project_KB_Update_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  approved_change_ref: "{{J9_APPROVED_CHANGE_REF}}"
  project_ref: "{{PROJECT_REF}}"
  target_ref: "{{KB_TARGET_REF}}"
  change_type: "{{CHANGE_TYPE}}"
  durable_write_state: "{{WRITE_STATE}}"
  durable_update_result_ref: "{{RESULT_REF_OR_NONE}}"
  effective_value_ref: "{{EFFECTIVE_VALUE_REF_OR_NONE}}"
  freshness: "{{FRESHNESS_OR_NONE}}"
  confirmed_for_overview: "{{TRUE_OR_FALSE}}"
  next_consumer: "{{PROJECT_STATUS_OVERVIEW_OR_OPERATOR_REVIEW_OR_NONE}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/15-project-kb-update-card-design.okf.yaml"
  round6_overlay_intent_ref: "round6-patches/04-j10-durable-update-result.patch"
  overlay_application_status: "intended_guidance_not_applied_by_this_package"
  domain_contract_refs:
    - ".claude/skills/project-kb-manager/SKILL.md"
    - ".claude/skills/project-kb-manager/references/write-rules.md"
```

Example: [J10 Project KB Update Card](../examples/master-of-arts-example-fragments.md#j10-project-kb-update-card)
