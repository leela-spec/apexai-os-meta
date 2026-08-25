# Flow Execution Card - ACIM outline prose sprint

> **Readiness:** READY  
> **Outcome target:** Complete draft of all outline sections, checked against the TUE source map, staged for THU final pass.  
> **Next action:** EXECUTE_NEXT_SPRINT   
> **Review needed:** NONE  
> **Warning:** deadline lane - if any block is lost today, invoke the weekly slip rule (Lika slides to FRI)

## Start or resume here

**Current sprint:** NOT_STARTED  
**Current status:** NOT_STARTED  
**Exact next operator step:** Open prompt file `../prompts/f1-s1-core-sections.md` and dispatch core-section drafting.  
**Last confirmed checkpoint:** none - flow not started

## Operator controls

- [ ] Execute the next sprint.
- [ ] Open the named prompt file.
- [ ] Edit scope or reorder only where dependencies allow.
- [ ] Request review, defer, mark blocked, or skip with a reason.

**Operator instruction:** PENDING - operator_validation not_requested

## Flow identity and context

**Flow ID:** `F1`  
**Project:** ACIM  
**Why today:** last full day before THU 17:00 print cutoff  
**Weekly priority advanced:** P1-deadline-delivery  
**Project-state signal:** source map complete and stable since TUE  
**Approved route:** not provided  
**Routing reference:** see prompts index

### Goals

- Every section drafted; zero silent gaps

### Expected outputs

- complete draft markdown + gap list

## Inputs and dependencies

### Available inputs

- SOURCE_MAP from TUE (section -> canonical IDs)

### Missing inputs (include when material)

(none - vocabulary dependency satisfied TUE)

### Flow dependencies

- **Depends on:** TUE source map + vocabulary decisions
- **Required before:** THU final pass and operator approval gate
- **External gate:** operator approval required before print handoff THU

## S1 - Draft core sections

**Sprint status:** NOT_STARTED

### Tasks

1. Write prose for sections 1-3 per SOURCE_MAP, using only canonical sources.

### Prompt access

- [Open S1 prompt](../prompts/f1-s1-core-sections.md) - `next-day-wed/prompts/f1-s1-core-sections.md`
- **Prompt readiness:** READY

### Done when
- sections 1-3 prose complete with source IDs cited inline

### Stop or review conditions
- a section lacks resolvable source coverage -> STOP, log in gap list, continue to next section only if independent

## S2 - Draft remaining sections

**Sprint status:** NOT_STARTED  
**Dependency on S1:** style consistency with S1 output

### Tasks

1. Write prose for remaining sections per SOURCE_MAP.

### Prompt access
- [Open S2 prompt](../prompts/f1-s2-rest-sections.md) - `next-day-wed/prompts/f1-s2-rest-sections.md`
- **Prompt readiness:** READY

### Done when
- draft covers every mapped section

### Stop or review conditions
- same as S1 for uncovered sections

## S3 - Capture, decision, handoff

**Sprint status:** NOT_STARTED  
**Capture goal:** clean THU start

### Evidence tasks
1. Cross-check draft against SOURCE_MAP; produce gap list.

### Decisions to record
- any unresolved content gaps -> operator decision list for THU morning.

### Handoff preparation
- stage draft + gap list as THU intake packet.

### Done when
- gap list written; draft file path recorded for THU brief.

## End-of-flow check

- [ ] Outputs vs plan checked.
- [ ] Completion state: PENDING.
- [ ] Evidence references identifiable.
- [ ] Decisions/blockers separated.
- [ ] THU packet ready or missing item named.

**Actual completion state:** PENDING  
**Evidence handoff target:** THU final-pass flow - `pending`  
**End-of-flow review:** none

## Material review flags

### Slip-rule trigger watch

- **Issue:** any lost block today arms the weekly slip rule.
- **Operator action:** automatic per rule; no input unless override desired.

## Provenance and confidence

**Day-plan reference:** [WED brief](precap-next-day-brief.md)  
**Project-state reference:** SOURCE_MAP (TUE artifact)  
**Weekly-plan reference:** [Weekly Brief W36-C](../weekly-command-brief.md)  
**Input freshness:** one day  
**Confidence:** HIGH on inputs; deadline pressure environmental  
**Consequential assumptions:** source map stability

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-C-dependency-conflict/next-day-wed/flow-execution-card-f1.md"
  flow_id: "F1"
  project_ref: "acim"
  readiness: "READY"
  current_sprint: "NOT_STARTED"
  prompt_index_ref: "next-day-wed/prompts-index.md"
  approved_route_ref: "none"
  evidence_handoff_ref: "pending"
  review_status: "slip-rule armed"
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
