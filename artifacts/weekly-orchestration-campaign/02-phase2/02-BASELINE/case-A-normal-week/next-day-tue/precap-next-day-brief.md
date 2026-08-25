# PreCap Next Day Brief - 2026-W36 TUE (Case A)

> **Day state:** READY_WITH_REVIEW  
> **Day direction:** Run the Lika validation walk to completion and start ACIM outline prep in the afternoon; Apex stays out of today. Nothing about yesterday's plan changed overnight.  
> **Next action:** OPEN_FIRST_FLOW_CARD   
> **Review needed:** NONE - weekly provisional-vocabulary flag does not bite until Thursday  
> **Plan size:** 3 flows; 6 visible sprints

## Approve or change the day

- [ ] Approve the day outline.
- [ ] Open the first Flow Execution Card.
- [ ] Reorder flows or sprint sequence.
- [ ] Edit, compress, defer, or block a named flow with a reason.

**Decision or instruction:** PENDING - operator_validation not_requested

## Changed since weekly plan / since Monday (delta first)

| What | From | To | Why | Source |
| :-- | :-- | :-- | :-- | :-- |
| F1 scope tightened | validate whole index in one walk | split: Lika main index today, workshops subtree tomorrow | Monday's dry run showed subtree needs its own pass | MON flow recap packet `flow-recap-f1.md` |
| F2 start pulled earlier | planned WED | starts today PM | Monday finished with one spare block | MON flow recap packet |

No other changes vs the weekly plan.

## Day frame

**Primary day outcomes:**

- Lika main-index validation report exists with findings listed
- ACIM outline section mapping table drafted (no prose yet)

**Projects touched and why:**

- **Lika:** validation tooling must run on real index before fixes can be dispositioned
- **ACIM:** source-ID mapping is independent of validation outcome; parallel slot is free

**Continuity from the week:** advances P1-validation-walk (Lika) and prepares P1-outline-skeleton (ACIM) per Weekly Command Brief W36  
**Capacity assumption:** standard weekday, 4 flow blocks, personal fixed blocks protected  
**Fixed constraints:** none beyond blueprint

## Flow 1 - Lika main-index validation walk

**Flow ID:** `F1`  
**Project:** Lika  
**Status:** PLANNED  
**Why today:** weekly sequence puts validation before remediation; Monday wrote the tooling  
**Weekly priority advanced:** P1-validation-walk  
**Expected flow output:** `lika-main-index-validation-report.md` with per-file status  
**Open full workspace:** [Open Flow Execution Card](flow-execution-card-f1.md) - `02-BASELINE/case-A-normal-week/next-day-tue/flow-execution-card-f1.md`

- **S1 - Pre-flight check:** confirm index schema unchanged since Monday -> checklist header filled
- **S2 - Execute walk:** run validation over canonical+redirect entries -> findings list generated
- **S3 - Capture and handoff:** classify findings (fix-now / defer-with-reason) -> handoff note for WED remediation

**Review flag:** none

## Flow 2 - ACIM outline source mapping

**Flow ID:** `F2`  
**Project:** ACIM  
**Status:** COMPRESSED (half block only; expanded if F1 finishes early)  
**Why today:** pulls Wednesday work forward into Monday's leftover capacity  
**Weekly priority advanced:** P1-outline-skeleton (prep only)  
**Expected flow output:** section-to-source-ID mapping table  
**Open full workspace:** [Open Flow Execution Card](flow-execution-card-f2.md) - `02-BASELINE/case-A-normal-week/next-day-tue/flow-execution-card-f2.md`

- **S1 - Section skeleton:** list outline sections from locked content TOC -> section list
- **S2 - Map sources:** attach canonical source IDs per section -> mapping table

**Review flag:** none

## Flow 3 - none scheduled

**Flow ID:** `F3`  
**Project:** -  
**Status:** OMITTED  
**Why today:** Apex hygiene is a WED lane per weekly plan; no third flow needed today  
**Weekly priority advanced:** n/a  
**Expected flow output:** n/a  
**Open full workspace:** n/a

**Review flag:** none

## Cross-flow execution order

1. `F1 / S1-S3` - validation is the day's critical path; ACIM prep fills remaining capacity
2. `F2 / S1-S2` - strictly overflow-priority; compress without ceremony if F1 runs long

## Expected end of day

**Project progress expected:**

- Lika: main index validated, findings classified
- ACIM: outline prep de-risked for Thursday

**Artifacts or decisions expected:**

- validation report file
- mapping table draft
- no operator decisions required today

**Evidence and handoffs to prepare:**

- F1 findings classification feeds Wednesday remediation flow directly

## Review flags (include when material)

(none material today)

## Planning context used

**Project-state source:** [Weekly Command Brief W36](../weekly-command-brief.md) - `02-BASELINE/case-A-normal-week/weekly-command-brief.md`  
**Weekly source:** same brief, priorities P1-validation-walk / P1-outline-skeleton  
**Recent execution signal:** MON flow recap packets (validation tooling written; one spare block)  
**Deferred or ignored signal:** none  
**Confidence:** MEDIUM-HIGH - inputs fresh within one day; underlying portfolio state remains historical-simulation class (see weekly provenance)

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "PreCap_Next_Day_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-A-normal-week/next-day-tue/precap-next-day-brief.md"
  execution_date: "2026-W36-TUE"
  result_state: "READY_WITH_REVIEW"
  ordered_flows:
    - order: "1"
      flow_id: "F1"
      project_ref: "lika"
      flow_status: "PLANNED"
      weekly_priority_ref: "P1-validation-walk"
      flow_execution_card_ref: "flow-execution-card-f1.md"
    - order: "2"
      flow_id: "F2"
      project_ref: "acim"
      flow_status: "COMPRESSED"
      weekly_priority_ref: "P1-outline-skeleton"
      flow_execution_card_ref: "flow-execution-card-f2.md"
    - order: "3"
      flow_id: "F3"
      project_ref: null
      flow_status: "OMITTED"
      weekly_priority_ref: null
      flow_execution_card_ref: null
  review_status: "none material today"
  next_consumer: "Flow_Execution_Card"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml"
  round6_overlay_intent_ref: "round6-patches/02-j3-j4-depth-separation.patch"
  overlay_application_status: "intended_guidance_not_applied_by_this_package"
  domain_contract_refs:
    - ".claude/skills/PrecapNextDay/SKILL.md"
    - ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
    - ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
```
