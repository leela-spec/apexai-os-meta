# Flow Execution Card - Lika main-index validation walk

> **Readiness:** READY  
> **Outcome target:** Run the validation walk across the full Lika main SSoT index and produce a findings report with every violation classified fix-now or defer-with-reason.  
> **Next action:** EXECUTE_NEXT_SPRINT   
> **Review needed:** NONE  
> **Warning:** none

## Start or resume here

**Current sprint:** NOT_STARTED  
**Current status:** NOT_STARTED  
**Exact next operator step:** Open prompt file `../prompts/f1-s1-preflight.md` and dispatch the pre-flight check.  
**Last confirmed checkpoint:** none - flow not started

## Operator controls

- [ ] Execute the next sprint.
- [ ] Open the named prompt file.
- [ ] Edit scope or reorder only where dependencies allow.
- [ ] Request review, defer, mark blocked, or skip with a reason.

**Operator instruction:** PENDING - operator_validation not_requested

## Flow identity and context

**Flow ID:** `F1`  
**Project:** Lika  
**Why today:** weekly sequence: validation before remediation; Monday produced the tooling, today consumes it  
**Weekly priority advanced:** P1-validation-walk (Lika, W36 brief)  
**Project-state signal:** index.yaml stable since Monday; schema unchanged per MON recap  
**Approved route:** not provided - routing reference pending operator confirmation  
**Routing reference:** see Prompt Files and Index - `prompts-index.md`

### Goals

- Full main-index walk executed with zero silent skips

### Expected outputs

- `lika-main-index-validation-report.md`: one line per entry (canonical/redirect/archive), status OK or finding

## Inputs and dependencies

### Available inputs

- [Lika SSoT index](../../../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md) - `Lika/SSoT/index.yaml` (in-world path; scenario input per 02-INPUT-CORPUS.md IN-1)
- [Validation checklist conventions]('../../../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md') - Thursday validation-pass pattern, IN-1

### Missing inputs (include when material)

(none)

### Flow dependencies

- **Depends on:** Monday tooling write (complete per MON recap)
- **Required before:** WED remediation flow consumes findings
- **External gate:** archive deletion stays operator-reserved; findings may propose but not execute it

## S1 - Pre-flight check

**Sprint status:** NOT_STARTED

### Tasks

1. Confirm index schema fields unchanged since Monday (canonical_id, path, owner, status, redirect_target).

### Inputs

- `Lika/SSoT/index.yaml`

### Prompt access

- [Open S1 prompt file](../prompts/f1-s1-preflight.md) - `next-day-tue/prompts/f1-s1-preflight.md`
- **Recommended surface:** session-local agent worker
- **Routing reference:** see prompts index
- **Prompt readiness:** READY

### Expected outputs

- checklist header filled: schema hash + field list confirmed

### Done when

- schema field set matches Monday's recorded field set exactly

### Stop or review conditions

- any missing/renamed field -> stop, flag to operator before walking

### Evidence to retain

- schema diff output (or no-diff note) in report header

## S2 - Execute walk

**Sprint status:** NOT_STARTED  
**Dependency on S1:** clean pre-flight required

### Tasks

1. Walk every index entry: verify path exists; verify each file under scope appears exactly once as canonical/redirect/archive.

### Inputs

- `Lika/SSoT/index.yaml`
- filesystem listing of `Lika/` subtree

### Prompt access

- [Open S2 prompt file](../prompts/f1-s2-walk.md) - `next-day-tue/prompts/f1-s2-walk.md`
- **Recommended surface:** session-local agent worker
- **Routing reference:** see prompts index
- **Prompt readiness:** READY

### Expected outputs

- findings list in report body: entry id, problem class (missing-path / duplicate-listing / bad-status / orphan-file), suggested disposition

### Done when

- walk covered 100% of entries AND produced zero unclassified findings

### Stop or review conditions

- more than ~20 findings -> pause and surface to operator rather than auto-classifying bulk

### Evidence to retain

- raw walk log referenced from report footer

## S3 - Capture, decision, and handoff

**Sprint status:** NOT_STARTED  
**Capture goal:** findings classified so Wednesday remediation starts with zero re-analysis

### Evidence tasks

1. Split findings into fix-now vs defer-with-reason.

### Decisions to record

- any finding that looks like an operator-reserved decision (archives) gets flagged, not decided

### Handoff preparation

- classification summary appended to report top for WED flow intake

### Optional prompt access

- [Open S3 prompt file](../prompts/f1-s3-handoff.md) - `next-day-tue/prompts/f1-s3-handoff.md`

### Done when

- every finding carries exactly one classification and a one-line reason

## End-of-flow check

- [ ] Planned outputs are checked against actual outputs.
- [ ] Actual completion state is recorded: PENDING.
- [ ] Evidence references are identifiable.
- [ ] Decisions, blockers, and unresolved questions are separated.
- [ ] Evidence is ready for recap or the exact missing item is named.

**Actual completion state:** PENDING  
**Evidence handoff target:** WED remediation flow packet - `pending`  
**End-of-flow review:** none

## Material review flags (include when needed)

(none at plan time)

## Provenance and confidence

**Day-plan reference:** [PreCap Next Day Brief TUE](precap-next-day-brief.md) - `next-day-tue/precap-next-day-brief.md`  
**Project-state reference:** `Lika/SSoT/index.yaml` (scenario input, IN-1)  
**Weekly-plan reference:** [Weekly Command Brief W36](../weekly-command-brief.md) - `weekly-command-brief.md`  
**Input freshness:** same-week; index untouched since MON  
**Confidence:** MEDIUM-HIGH - historical-simulation input class, internally consistent  
**Consequential assumptions:** schema stability since Monday

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-A-normal-week/next-day-tue/flow-execution-card-f1.md"
  flow_id: "F1"
  project_ref: "lika"
  readiness: "READY"
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
    - ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
```
