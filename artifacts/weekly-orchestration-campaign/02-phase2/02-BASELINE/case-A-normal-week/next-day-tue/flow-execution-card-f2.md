# Flow Execution Card - ACIM outline source mapping

> **Readiness:** READY  
> **Outcome target:** Produce the section-to-source-ID mapping table that Thursday's outline sprint consumes.  
> **Next action:** OPEN_PROMPT_FILE   
> **Review needed:** NONE  
> **Warning:** COMPRESSED flow - half block; drop without ceremony if F1 needs capacity

## Start or resume here

**Current sprint:** NOT_STARTED  
**Current status:** NOT_STARTED  
**Exact next operator step:** Open prompt file `../prompts/f2-s1-sections.md` and dispatch the section skeleton task.  
**Last confirmed checkpoint:** none - flow not started

## Operator controls

- [ ] Execute the next sprint.
- [ ] Open the named prompt file.
- [ ] Edit scope or reorder only where dependencies allow.
- [ ] Request review, defer, mark blocked, or skip with a reason.

**Operator instruction:** PENDING - operator_validation not_requested

## Flow identity and context

**Flow ID:** `F2`  
**Project:** ACIM  
**Why today:** overflow slot from Monday's spare block; prep de-risks Thursday  
**Weekly priority advanced:** P1-outline-skeleton (prep only - prose writing stays Thursday)  
**Project-state signal:** ACIM content locked W1; canonical IDs stable per handoff seed  
**Approved route:** not provided  
**Routing reference:** see Prompt Files and Index - `prompts-index.md`

### Goals

- Mapping table complete for all planned sections

### Expected outputs

- mapping table: section -> one or more canonical source IDs

## Inputs and dependencies

### Available inputs

- ACIM content TOC from locked sources (scenario input, IN-1 trajectory)
- `ACIM/SSoT/index.yaml` ID space

### Missing inputs (include when material)

(none)

### Flow dependencies

- **Depends on:** W1 content lock (complete)
- **Required before:** THU outline sprint
- **External gate:** provisional-vocabulary decision affects THU, not today's mapping

## S1 - Section skeleton

**Sprint status:** NOT_STARTED

### Tasks

1. List the workshop outline sections derived from the locked-content TOC.

### Inputs

- locked content TOC

### Prompt access

- [Open S1 prompt file](../prompts/f2-s1-sections.md) - `next-day-tue/prompts/f2-s1-sections.md`
- **Recommended surface:** session-local agent worker
- **Routing reference:** see prompts index
- **Prompt readiness:** READY

### Expected outputs

- ordered section list with one-line purpose each

### Done when

- section list covers full workshop arc with no placeholder entries

### Stop or review conditions

- TOC gaps discovered -> stop and flag rather than inventing sections

### Evidence to retain

- section list in working notes referenced by table

## S2 - Map sources

**Sprint status:** NOT_STARTED  
**Dependency on S1:** section list required

### Tasks

1. For each section, attach the canonical source IDs that feed it.

### Inputs

- section list from S1
- `ACIM/SSoT/index.yaml`

### Prompt access

- [Open S2 prompt file](../prompts/f2-s2-map.md) - `next-day-tue/prompts/f2-s2-map.md`
- **Recommended surface:** session-local agent worker
- **Routing reference:** see prompts index
- **Prompt readiness:** READY

### Expected outputs

- completed mapping table

### Done when

- every section has >=1 resolvable source ID; zero unresolved references

### Stop or review conditions

- any section with no canonical source -> flag for operator (content gap)

### Evidence to retain

- mapping table draft saved to day artifacts

## End-of-flow check

- [ ] Planned outputs are checked against actual outputs.
- [ ] Actual completion state is recorded: PENDING.
- [ ] Evidence references are identifiable.
- [ ] Decisions, blockers, and unresolved questions are separated.
- [ ] Evidence is ready for recap or the exact missing item is named.

**Actual completion state:** PENDING  
**Evidence handoff target:** THU outline flow packet - `pending`  
**End-of-flow review:** none

## Material review flags (include when needed)

(none at plan time)

## Provenance and confidence

**Day-plan reference:** [PreCap Next Day Brief TUE](precap-next-day-brief.md) - `next-day-tue/precap-next-day-brief.md`  
**Project-state reference:** ACIM lock state per W1 handoff seed (IN-1)  
**Weekly-plan reference:** [Weekly Command Brief W36](../weekly-command-brief.md) - `weekly-command-brief.md`  
**Input freshness:** same-week  
**Confidence:** MEDIUM - locked-content assumption inherited from weekly provenance  
**Consequential assumptions:** TOC is complete for workshop purposes

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Flow_Execution_Card"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-A-normal-week/next-day-tue/flow-execution-card-f2.md"
  flow_id: "F2"
  project_ref: "acim"
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
