# Execution Evidence Handoff - {{FLOW_TITLE_OR_ID}}

> **Evidence route:** {{DIRECT_TO_FLOWRECAP | NORMALIZE_THEN_SEND | REVIEW_NEEDED | INSUFFICIENT_EVIDENCE}}  
> **Outcome:** {{WHAT_EVIDENCE_IS_ORGANIZED_AND_ITS_READINESS}}  
> **Next action:** {{SEND_TO_FLOWRECAP | COMPLETE_NORMALIZATION | PROVIDE_EXACT_MISSING_EVIDENCE | RESOLVE_CONFLICT}}  
> **Review needed:** {{EVIDENCE_QUALITY_DECISION_OR_NONE}}  
> **Completion state reported:** {{COMPLETED | PARTIAL | BLOCKED | SKIPPED}}

## Handoff decision

**Use the lightest route that preserves evidence quality.**

- [ ] Send directly: evidence is small, structured, clear, sourced, and materially consistent.
- [ ] Normalize first: evidence is fragmented, distributed, long, ambiguous, or conflicting.
- [ ] Request review: a conflict or missing source changes what can be claimed.
- [ ] Mark insufficient: completion or claimed outputs cannot be determined from identifiable evidence.

**Decision reason:** {{ONE_TO_THREE_SENTENCE_EVIDENCE_QUALITY_REASON}}

## Execution identity

**Flow ID:** `{{FLOW_ID}}`  
**Flow Execution Card:** [{{FLOW_CARD_LABEL}}]({{FLOW_CARD_REF}}) - `{{FLOW_CARD_REF}}`  
**Execution window:** {{START_AND_END_OR_DATE}}  
**Operator or executor:** {{EXECUTOR}}

## Planned versus actual evidence

### What was planned

- {{PLANNED_ITEM_OR_REFERENCE}}

### What actually happened

- {{EVIDENCE_SUPPORTED_ACTUAL_ITEM}}

### Changed scope (include when material)

- {{SCOPE_CHANGE_AND_SOURCE_REF}}

## Outputs and artifacts

### Completed or changed outputs

- [{{OUTPUT_LABEL}}]({{OUTPUT_REF}}) - `{{OUTPUT_REF}}`
  - Evidence status: {{IDENTIFIABLE | PARTIAL | UNVERIFIED}}

### Claimed outputs without sufficient evidence (include when present)

- {{CLAIM}} - missing evidence: {{EXACT_EVIDENCE_NEEDED}}

## Decisions recorded during execution

- **Decision:** {{DECISION}}
  - Evidence reference: `{{DECISION_SOURCE_REF}}`

## Blockers and failed attempts

- **Item:** {{BLOCKER_OR_FAILURE_OR_NONE}}
  - Evidence reference: `{{SOURCE_REF_OR_NONE}}`
  - Observable effect: {{EFFECT_ON_EXECUTION}}

## Unresolved questions

- {{QUESTION_OR_NONE}}

## Source evidence (repeat per material source)

### {{SOURCE_LABEL}}

**Reference:** [{{SOURCE_LABEL}}]({{SOURCE_REF}}) - `{{SOURCE_REF}}`  
**What it supports:** {{FACTUAL_CLAIM_SUPPORTED}}  
**Freshness or time:** {{SOURCE_TIME_OR_UNKNOWN}}  
**Limit or conflict:** {{LIMIT_OR_NONE}}

## Evidence gaps and conflicts (include when material)

### {{GAP_OR_CONFLICT_TITLE}}

- **Observed evidence:** {{EVIDENCE_A}}
- **Conflicting or missing evidence:** {{EVIDENCE_B_OR_MISSING_ITEM}}
- **Why it matters for FlowRecap:** {{INTERPRETATION_LIMIT}}
- **Required evidence action:** {{ONE_RESOLVING_ACTION}}

## FlowRecap readiness

**Readiness:** {{READY_FOR_FLOWRECAP | REVIEW_NEEDED | INSUFFICIENT_EVIDENCE}}  
**Evidence reference to send:** `{{HANDOFF_OR_SOURCE_REF}}`  
**Unsupported conclusions that must not be made:** {{LIMITS_OR_NONE}}  
**Usage evidence references:** {{USAGE_EVIDENCE_REFS_OR_NONE}}

This handoff organizes evidence. It does not recommend a project next step, interpret success, or propose a project-state change.

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Execution_Evidence_Handoff"
  artifact_ref: "{{ARTIFACT_REF}}"
  flow_id: "{{FLOW_ID}}"
  completion_state: "{{COMPLETION_STATE}}"
  evidence_route: "{{EVIDENCE_ROUTE}}"
  output_refs:
    - "{{OUTPUT_REF}}"
  source_refs:
    - "{{SOURCE_REF}}"
  material_gaps_or_conflicts:
    - "{{GAP_OR_CONFLICT_OR_NONE}}"
  readiness: "{{FLOWRECAP_READINESS}}"
  next_consumer: "FlowRecap_Result_Card"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/06-execution-evidence-handoff-design.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/raw-flow-dump-normalize/SKILL.md"
    - ".claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md"
    - ".claude/skills/flow-recap/references/flow-recap-packet-contract.md"
```

Example: [J06 Execution Evidence Handoff](../examples/master-of-arts-example-fragments.md#j06-execution-evidence-handoff)
