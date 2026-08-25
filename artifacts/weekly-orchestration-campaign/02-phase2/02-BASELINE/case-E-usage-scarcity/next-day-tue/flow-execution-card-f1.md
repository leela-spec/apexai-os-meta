# Flow Execution Card - Lika prep + walk decision packet

> **Readiness:** PARTIAL_CONTEXT  
> **Outcome target:** Pre-flight done, walk decision staged; walk itself gated on operator's degraded-surface choice.  
> **Next action:** RESOLVE_REVIEW   
> **Review needed:** S2 DEGRADED - chunked fallback vs defer  
> **Warning:** S2 prompt is NOT execution-ready on the fallback surface until decided

## Start or resume here

**Current sprint:** S1 (S2 gated)  
**Current status:** WAITING on review for S2  
**Exact next operator step:** Run S1 pre-flight (local-safe), then answer the S2 readiness question.  
**Last confirmed checkpoint:** quota exhaustion confirmed MON

## Operator controls

- [ ] Execute S1.
- [ ] Resolve the S2 DEGRADED flag: CHUNKED_FALLBACK | DEFER_TO_RESET.
- [ ] Defer or skip with a reason.

**Operator instruction:** PENDING - operator_validation not_requested

## Flow identity and context

**Flow ID:** `F1`  
**Project:** Lika  
**Why today:** instant resumability after the routing decision  
**Weekly priority advanced:** P1-walk-resolution  
**Project-state signal:** index unchanged; freshness to be stamped by S1  
**Approved route:** primary surface UNAVAILABLE (quota); fallback pending approval for S2 only  
**Routing reference:** see prompts index - degraded entry flagged there

### Goals

- Decision-ready state for the week's critical path

### Expected outputs

- S1 stamp + staged decision packet

## Inputs and dependencies

### Available inputs

- index.yaml; chunked-walk variant prompt (prepared as mitigation)

### Missing inputs (include when material)

- operator decision on S2 route - resolution: flagged in day brief and here

### Flow dependencies

- **Depends on:** none for S1
- **Required before:** THU remediation planning
- **External gate:** operator routing decision

## S1 - Pre-flight (local-safe)

**Sprint status:** NOT_STARTED

### Tasks
1. Schema check + freshness stamp per Case-D pattern.

### Prompt access
- [Open S1 prompt](../prompts/f1-s1-preflight-freshness.md) - `next-day-tue/prompts/f1-s1-preflight-freshness.md`
- **Recommended surface:** local model (small context - proven adequate)
- **Prompt readiness:** READY

### Done when
- stamp block returned

### Stop/review conditions
- unreadable index -> stop

## S2 - Full walk (DEGRADED)

**Sprint status:** BLOCKED (pending routing decision)  
**Dependency on S1:** clean pre-flight

### Tasks
1. Full-index validation OR chunked variant per operator choice.

### Prompt access
- [Open S2 prompt - full](../prompts/f1-s2-walk-full.md) - `next-day-tue/prompts/f1-s2-walk-full.md`
- [Open S2 prompt - chunked fallback](../prompts/f1-s2-walk-chunked.md) - `next-day-tue/prompts/f1-s2-walk-chunked.md`
- **Recommended surface:** local model ONLY IF chunked variant approved
- **Routing reference:** default-session-local - DEGRADED for full-context on this surface
- **Prompt readiness:** DEGRADED

### Done when
- report complete via chosen path, readiness caveat recorded in output header

### Stop/review conditions
- chunked path shows cross-chunk inconsistency > threshold -> stop and escalate

## S3 - Classify and stage

**Sprint status:** GATED on S2  
**Capture goal:** clean intake for THU

### Evidence tasks
1. Classification per chosen-path output.

### Handoff preparation
- summary appended to report.

### Done when
- all findings classified with path-quality note.

## End-of-flow check

- [ ] Outputs vs plan checked.
- [ ] Completion state: PENDING.
- [ ] Evidence identifiable.
- [ ] Decisions/blockers separated.
- [ ] Handoff ready or missing item named (routing decision currently missing).

**Actual completion state:** PENDING  
**Evidence handoff target:** THU remediation - `pending`  
**End-of-flow review:** routing decision outcome should be reviewed for future quota weeks

## Material review flags

### S2 routing degradation

- **Issue:** full-context walk exceeds local fallback envelope.
- **Why it matters to execution:** quality risk vs schedule risk tradeoff.
- **Operator action:** CHUNKED_FALLBACK or DEFER_TO_RESET.

## Provenance and confidence

**Day-plan reference:** [TUE brief](precap-next-day-brief.md)  
**Project-state reference:** index.yaml  
**Weekly-plan reference:** [Weekly Brief W36-E](../weekly-command-brief.md)  
**Input freshness:** stamped by S1 at run time  
**Confidence:** HIGH on plan; MEDIUM on degraded-surface execution  
**Consequential assumptions:** chunked variant preserves finding quality

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-E-usage-scarcity/next-day-tue/flow-execution-card-f1.md"
  flow_id: "F1"
  project_ref: "lika"
  readiness: "PARTIAL_CONTEXT"
  current_sprint: "S1"
  prompt_index_ref: "next-day-tue/prompts-index.md"
  approved_route_ref: "primary-unavailable-quota"
  evidence_handoff_ref: "pending"
  review_status: "S2 DEGRADED open"
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
    - ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
```
