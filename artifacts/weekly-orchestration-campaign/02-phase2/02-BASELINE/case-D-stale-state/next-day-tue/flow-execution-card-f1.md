# Flow Execution Card - Lika validation walk (drift-aware)

> **Readiness:** PARTIAL_CONTEXT  
> **Outcome target:** Walk the Lika main index and classify findings as true errors vs DRIFT_SUSPECTED, given that input freshness cannot be established.  
> **Next action:** EXECUTE_NEXT_SPRINT   
> **Review needed:** NONE  
> **Warning:** refresh attempt failed MON - all findings carry an age caveat

## Start or resume here

**Current sprint:** NOT_STARTED  
**Current status:** NOT_STARTED  
**Exact next operator step:** Open prompt file `../prompts/f1-s1-preflight-freshness.md` and dispatch the freshness-stamped pre-flight.  
**Last confirmed checkpoint:** none

## Operator controls

- [ ] Execute the next sprint.
- [ ] Open the named prompt file.
- [ ] Edit scope or reorder only where dependencies allow.
- [ ] Request review, defer, mark blocked, or skip with a reason.

**Operator instruction:** PENDING - operator_validation not_requested

## Flow identity and context

**Flow ID:** `F1`  
**Project:** Lika  
**Why today:** staleness-tolerant work item per weekly brief  
**Weekly priority advanced:** P1-walk-staleness-tolerant  
**Project-state signal:** UNVERIFIED - no fresh feed since 9+ days ago  
**Approved route:** not provided  
**Routing reference:** see prompts index

### Goals

- Full walk with honest freshness labeling

### Expected outputs

- classified report: ERROR classes + DRIFT_SUSPECTED class separated

## Inputs and dependencies

### Available inputs

- `Lika/SSoT/index.yaml` (age unknown)
- filesystem subtree listing

### Missing inputs (include when material)

- fresh Session/Sync feed - resolution: none available; proceed with drift-awareness per weekly flag

### Flow dependencies

- **Depends on:** Monday tooling (done)
- **Required before:** WED ACIM verification approach
- **External gate:** none

## S1 - Pre-flight with freshness stamp

**Sprint status:** NOT_STARTED

### Tasks
1. Schema check PLUS record last-modified times of index and sampled entries.

### Prompt access
- [Open S1 prompt](../prompts/f1-s1-preflight-freshness.md) - `next-day-tue/prompts/f1-s1-preflight-freshness.md`
- **Prompt readiness:** READY

### Done when
- schema verdict + freshness stamp block returned

### Stop or review conditions
- unreadable index -> stop immediately

## S2 - Execute walk

**Sprint status:** NOT_STARTED  
**Dependency on S1:** pre-flight clean

### Tasks
1. Standard validation rules; findings that could stem from outdated index data get tagged DRIFT_SUSPECTED.

### Prompt access
- [Open S2 prompt](../prompts/f1-s2-walk-drift.md) - `next-day-tue/prompts/f1-s2-walk-drift.md`
- **Prompt readiness:** READY

### Done when
- coverage complete; every finding carries class ERROR or DRIFT_SUSPECTED

### Stop or review conditions
- bulk drift suspicion (>30% findings) -> pause, surface to operator

## S3 - Classify and flag

**Sprint status:** NOT_STARTED  
**Capture goal:** separation of real defects from staleness artifacts

### Evidence tasks
1. Two-list summary: FIX_NOW/DEFER for errors; VERIFY_WITH_FRESH_STATE for drift suspects.

### Decisions to record
- archive items -> operator flags as always.

### Handoff preparation
- report header updated for WED intake.

### Done when
- both lists complete; no unclassified findings.

## End-of-flow check

- [ ] Outputs vs plan checked.
- [ ] Completion state: PENDING.
- [ ] Evidence identifiable.
- [ ] Decisions/blockers separated.
- [ ] Handoff ready or missing item named.

**Actual completion state:** PENDING  
**Evidence handoff target:** WED ACIM verification - `pending`  
**End-of-flow review:** none

## Material review flags

(none at plan time)

## Provenance and confidence

**Day-plan reference:** [TUE brief](precap-next-day-brief.md)  
**Project-state reference:** index.yaml - AGE UNKNOWN  
**Weekly-plan reference:** [Weekly Brief W36-D](../weekly-command-brief.md)  
**Input freshness:** STALE/UNKNOWN - explicitly stamped in outputs  
**Confidence:** LOW-MEDIUM  
**Consequential assumptions:** local files are internally consistent even if externally stale

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-D-stale-state/next-day-tue/flow-execution-card-f1.md"
  flow_id: "F1"
  project_ref: "lika"
  readiness: "PARTIAL_CONTEXT"
  current_sprint: "NOT_STARTED"
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
