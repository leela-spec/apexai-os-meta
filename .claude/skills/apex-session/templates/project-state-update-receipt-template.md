# Project State Update Receipt - {{PROJECT_AND_UPDATE_LABEL}}

> **Mutation state:** {{PREPARED | AWAITING_CONFIRMATION | EXECUTED | PARTIALLY_EXECUTED | SKIPPED | BLOCKED}}
> **Durable effect:** {{EFFECTIVE_CHANGE_OR_NOT_YET_APPLIED}}
> **Next action:** {{CONFIRM_SESSION_MUTATION | VERIFY_RESULT | RESOLVE_FAILURE | SEND_CONFIRMED_RESULT_TO_OVERVIEW | NO_ACTION}}

> **Boundary:** J10 is the confirmed Apex Session mutation receipt. A prepared request is not accepted truth; J11 may use new truth only after an executed Session result identifies the effective value.

## Approved input

**J9 decision reference:** {{J9_REF}}
**Approved candidate and evidence refs:** {{APPROVED_REFS}}
**Operator confirmation:** {{CONFIRMED | NOT_CONFIRMED}}

## Apex Session mutation

**Session mutation request:** {{STATUS_OR_ENTITY_CHANGE}}
**Current confirmed value:** {{CURRENT_VALUE}}
**Expected value:** {{EXPECTED_VALUE}}
**Session result reference:** {{SESSION_RESULT_REF_OR_NONE}}

## Confirmed result

**Write status:** {{EXECUTED | PARTIALLY_EXECUTED | SKIPPED | BLOCKED | NOT_EXECUTED}}  
**Effective durable value:** {{EFFECTIVE_VALUE_OR_NOT_CONFIRMED}}  
**Refreshed planning feed:** {{PLANNING_FEED_REF_OR_NONE}}
**Verification method:** {{SESSION_READ_BACK_OR_OTHER_EVIDENCE}}
**Ready for J11:** {{YES_ONLY_IF_CONFIRMED | NO}}

```yaml
presentation_handoff:
  artifact_type: Project_State_Update_Receipt
  approved_change_ref: "{{J9_APPROVED_CHANGE_REF}}"
  session_result_ref: "{{SESSION_RESULT_REF_OR_NONE}}"
  planning_feed_ref: "{{PLANNING_FEED_REF_OR_NONE}}"
  confirmed_for_overview: "{{TRUE_OR_FALSE}}"
```
