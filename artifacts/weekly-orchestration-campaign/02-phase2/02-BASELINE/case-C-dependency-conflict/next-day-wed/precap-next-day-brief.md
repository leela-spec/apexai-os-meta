# PreCap Next Day Brief - 2026-W36-C WED (Case C: deadline crunch day)

> **Day state:** READY_WITH_REVIEW  
> **Day direction:** Full-day ACIM outline writing sprint; Lika vocabulary decisions landed TUE so the dependency is clear. Slip rule from the weekly brief is armed: if this day loses blocks, the walk slides to FRI - not the deadline.  
> **Next action:** OPEN_FIRST_FLOW_CARD   
> **Review needed:** NONE today unless TUE slip occurred  
> **Plan size:** 2 flows; 4 visible sprints

## Approve or change the day

- [ ] Approve the day outline.
- [ ] Open the first Flow Execution Card.
- [ ] Reorder flows or sprint sequence.
- [ ] Edit, compress, defer, or block a named flow with a reason.

**Decision or instruction:** PENDING - operator_validation not_requested

## Changed since weekly plan / since Tuesday (delta first)

| What | From | To | Why | Source |
| :-- | :-- | :-- | :-- | :-- |
| F2 (Lika) | PLANNED per weekly grid | DROPPED from today | vocabulary decisions completed TUE evening; nothing left to parallelize | TUE flow recap packet |
| Slip rule | armed | still armed | no trigger yet | weekly review flag |

## Day frame

**Primary day outcomes:**

- Complete outline draft (all sections with prose).

**Projects touched and why:**

- **ACIM:** deadline lane owns the whole day.

**Continuity from the week:** P1-deadline-delivery critical path  
**Capacity assumption:** standard four-block day, all assigned to ACIM  
**Fixed constraints:** THU 17:00 print cutoff

## Flow 1 - ACIM outline prose sprint

**Flow ID:** `F1`  
**Project:** ACIM  
**Status:** PLANNED  
**Why today:** last full day before deadline buffer  
**Weekly priority advanced:** P1-deadline-delivery  
**Expected flow output:** complete draft covering every section in the source map  
**Open full workspace:** [Open Flow Execution Card](flow-execution-card-f1.md) - `next-day-wed/flow-execution-card-f1.md`

- **S1 - Draft core sections** -> prose for sections 1-3
- **S2 - Draft remaining sections** -> prose complete
- **S3 - Self-check against source map + handoff prep** -> gap list + print-prep note

**Review flag:** none

## Flow 2 - Lika

**Status:** OMITTED today - deliberately. Vocabulary dependency is satisfied; walk resumes FRI or earlier if F1 finishes with a block to spare.

## Cross-flow execution order

1. `F1 / S1-S3` - single critical path.

## Expected end of day

**Project progress expected:**

- Outline draft complete; only final pass + operator approval remain for THU.

**Artifacts or decisions expected:**

- full draft file
- gap list if any section lacked source coverage

**Evidence and handoffs to prepare:**

- draft staged for THU morning final pass and operator approval gate before printing.

## Review flags (include when material)

### Trigger check: TUE slip

- **Issue:** if TUE vocabulary work had slipped, today would carry a dual load and the slip rule would need invoking.
- **Why it matters before execution:** changes what "done" means tonight.
- **Operator action:** none required - TUE held; flag auto-clears.

## Planning context used

**Project-state source:** [Weekly Command Brief W36-C](../weekly-command-brief.md) - `weekly-command-brief.md`  
**Weekly source:** same brief, slip-priority rule  
**Recent execution signal:** TUE recap: vocabulary decisions recorded, source map stable  
**Deferred or ignored signal:** Lika omitted today with reason above  
**Confidence:** HIGH for the day plan; deadline pressure noted as environment fact

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "PreCap_Next_Day_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-C-dependency-conflict/next-day-wed/precap-next-day-brief.md"
  execution_date: "2026-W36-C-WED"
  result_state: "READY_WITH_REVIEW"
  ordered_flows:
    - order: "1"
      flow_id: "F1"
      project_ref: "acim"
      flow_status: "PLANNED"
      weekly_priority_ref: "P1-deadline-delivery"
      flow_execution_card_ref: "flow-execution-card-f1.md"
  review_status: "slip-rule armed, untriggered"
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
```
