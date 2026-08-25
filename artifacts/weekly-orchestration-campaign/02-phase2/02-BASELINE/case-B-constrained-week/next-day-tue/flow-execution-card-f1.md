# Flow Execution Card - Lika findings triage (compressed)

> **Readiness:** READY  
> **Outcome target:** Classify Monday's 14 walk findings so Thursday remediation starts without re-analysis.  
> **Next action:** OPEN_PROMPT_FILE   
> **Review needed:** NONE  
> **Warning:** COMPRESSED day - only S3-classification runs; S1/S2 already done Monday

## Start or resume here

**Current sprint:** S3  
**Current status:** NOT_STARTED  
**Exact next operator step:** Open prompt file `../prompts/f1-s3-handoff.md` and dispatch classification on the existing WALK_REPORT.  
**Last confirmed checkpoint:** WALK_REPORT complete with ~14 findings (MON recap reference in day brief)

## Operator controls

- [ ] Execute the named sprint.
- [ ] Open the named prompt file.
- [ ] Defer or skip with a reason.
- [ ] Request review if findings look bulk-classifiable wrong.

**Operator instruction:** PENDING - operator_validation not_requested

## Flow identity and context

**Flow ID:** `F1`  
**Project:** Lika  
**Why today:** keeps THU remediation possible inside a one-block day  
**Weekly priority advanced:** P1-validation-walk  
**Project-state signal:** walk report exists; index untouched since MON  
**Approved route:** not provided  
**Routing reference:** see prompts index

### Goals

- CLASSIFICATION_SUMMARY complete, operator_flags populated

### Expected outputs

- summary appended to `lika-walk-report.md` header block

## Inputs and dependencies

### Available inputs

- Monday's WALK_REPORT content (referenced from day brief delta table)

### Missing inputs (include when material)

(none)

### Flow dependencies

- **Depends on:** completed walk (done)
- **Required before:** THU remediation sprint
- **External gate:** none today

## S1/S2 - not run today

Skipped per compressed-day plan; both sprints completed Monday. Recorded here so the card reflects reality instead of a full arc fiction.

## S3 - Capture, decision, and handoff

**Sprint status:** NOT_STARTED  
**Capture goal:** zero re-analysis needed Thursday

### Evidence tasks

1. Run classification prompt against WALK_REPORT.

### Decisions to record

- archive-related findings -> operator_flags, never decided here.

### Handoff preparation

- append summary to report top.

### Optional prompt access

- [Open S3 prompt file](../prompts/f1-s3-handoff.md) - `next-day-tue/prompts/f1-s3-handoff.md`

### Done when

- every finding classified exactly once; counts stated.

## End-of-flow check

- [ ] Planned outputs checked against actual.
- [ ] Actual completion state: PENDING.
- [ ] Evidence references identifiable.
- [ ] Decisions/blockers/questions separated.
- [ ] Ready for THU intake or missing item named.

**Actual completion state:** PENDING  
**Evidence handoff target:** THU remediation packet - `pending`  
**End-of-flow review:** none

## Material review flags (include when needed)

(none at plan time)

## Provenance and confidence

**Day-plan reference:** [PreCap Next Day Brief TUE](precap-next-day-brief.md) - `precap-next-day-brief.md`  
**Project-state reference:** walk report (MON)  
**Weekly-plan reference:** [Weekly Command Brief W37](../weekly-command-brief.md) - `weekly-command-brief.md`  
**Input freshness:** one day  
**Confidence:** HIGH for this single task  
**Consequential assumptions:** Monday's finding count stable

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-B-constrained-week/next-day-tue/flow-execution-card-f1.md"
  flow_id: "F1"
  project_ref: "lika"
  readiness: "READY"
  current_sprint: "S3"
  prompt_index_ref: "next-day-tue/prompts-index.md"
  approved_route_ref: "none"
  evidence_handoff_ref: "pending"
  review_status: "clean"
  next_consumer: "PROMPT_FILES_AND_INDEX_OR_OPERATOR_EXECUTION"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
```
