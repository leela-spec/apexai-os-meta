# PreCap Next Day Brief - 2026-W36-E TUE (Case E)

> **Day state:** READY_WITH_REVIEW  
> **Day direction:** Quota-constrained triage day: run what the local fallback handles well, keep the big walk pending the operator's degraded-risk decision, and mark the affected prompts DEGRADED rather than pretending they are ready.  
> **Next action:** RESOLVE_REVIEW   
> **Review needed:** F1-S2 walk prompt is DEGRADED on fallback - approve chunked attempt or defer  
> **Plan size:** 3 flows; 4 visible sprints (2 flagged)

## Approve or change the day

- [ ] Approve the day outline.
- [ ] Open the first Flow Execution Card.
- [ ] Reorder flows or sprint sequence.
- [ ] Edit, compress, defer, or block a named flow with a reason.

**Decision or instruction:** PENDING - operator_validation not_requested

## Changed since weekly plan / since Monday (delta first)

| What | From | To | Why | Source |
| :-- | :-- | :-- | :-- | :-- |
| F1-S2 readiness | assumed READY at week level | DEGRADED | quota exhaustion confirmed for full week; fallback quality on large context unproven | MON usage check |
| F3 spot-check | WED lane | pulled to today | small context; fills the walk's wait slot | capacity math |

## Day frame

**Primary day outcomes:**

- Decision-ready packet for the walk question; small-context flows advanced.

**Projects touched and why:**

- **Lika:** walk blocked on decision, prep continues
- **ACIM:** quota-free progress
- **Apex:** slot-fill hygiene

**Continuity from the week:** P1-walk-resolution critical path  
**Capacity assumption:** standard blocks; surface speed reduced  
**Fixed constraints:** primary surface unavailable all week

## Flow 1 - Lika prep + walk decision packet

**Flow ID:** `F1`  
**Project:** Lika  
**Status:** PARTIAL (S1 runs; S2 DEGRADED-pending decision; S3 waits on S2)  
**Why today:** keeps walk resumable instantly once decided  
**Weekly priority advanced:** P1-walk-resolution  
**Expected flow output:** freshness-stamped pre-flight done + decision packet staged  
**Open full workspace:** [Open Flow Execution Card](flow-execution-card-f1.md) - `next-day-tue/flow-execution-card-f1.md`

- **S1 - Pre-flight (local OK):** schema + freshness stamp -> READY
- **S2 - Full walk:** DEGRADED on fallback - needs operator choice (chunked attempt vs defer)
- **S3 - Classify:** waits for S2 outcome

**Review flag:** S2 readiness DEGRADED - see card warning block

## Flow 2 - ACIM mapping extension

**Flow ID:** `F2`  
**Project:** ACIM  
**Status:** PLANNED  
**Why today:** quota-immune  
**Weekly priority advanced:** P1-mapping-extension  
**Expected flow output:** additional sections mapped  
**Open full workspace:** [Open Flow Execution Card](flow-execution-card-f2.md) - `next-day-tue/flow-execution-card-f2.md`

- **S1 - Map next section batch:** extend table -> coverage update

**Review flag:** none

## Flow 3 - Apex pointer spot-check

**Flow ID:** `F3`  
**Project:** Apex  
**Status:** COMPRESSED (single pass)  
**Why today:** fills walk-wait slot with useful small work  
**Weekly priority advanced:** P2-spot-check  
**Expected flow output:** updated audit note  
**Open full workspace:** see prompts index entry

- **S1 - Spot-check pass:** verify ADR links sample -> note appended

**Review flag:** none

## Cross-flow execution order

1. `F1 / S1` - unblocks everything downstream regardless of decision
2. `F2 / S1` - parallel-safe
3. `F3 / S1` - overflow fill
4. `F1 / S2-S3` - GATED on operator decision

## Expected end of day

**Project progress expected:** mapping extended; audit touched; walk decision staged.

**Artifacts or decisions expected:** decision packet (chunk vs defer) ready for operator.

**Evidence and handoffs to prepare:** pre-flight stamp feeds whichever path is chosen.

## Review flags (include when material)

### DEGRADED: F1-S2 on fallback surface

- **Issue:** full-context validation exceeds proven local-model envelope.
- **Why it matters before execution:** wrong classifications would contaminate later remediation.
- **Operator action:** choose chunked-fallback attempt or defer to post-reset.

## Planning context used

**Project-state source:** [Weekly Brief W36-E](../weekly-command-brief.md)  
**Weekly source:** same brief  
**Recent execution signal:** MON usage check confirming quota exhaustion  
**Deferred or ignored signal:** nothing ignored - the walk is gated, not skipped  
**Confidence:** MEDIUM - plan quality good, execution surface uncertain

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "PreCap_Next_Day_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-E-usage-scarcity/next-day-tue/precap-next-day-brief.md"
  execution_date: "2026-W36-E-TUE"
  result_state: "READY_WITH_REVIEW"
  ordered_flows:
    - {order: "1", flow_id: "F1", project_ref: "lika", flow_status: "PARTIAL", weekly_priority_ref: "P1-walk-resolution", flow_execution_card_ref: "flow-execution-card-f1.md"}
    - {order: "2", flow_id: "F2", project_ref: "acim", flow_status: "PLANNED", weekly_priority_ref: "P1-mapping-extension", flow_execution_card_ref: "flow-execution-card-f2.md"}
    - {order: "3", flow_id: "F3", project_ref: "apex", flow_status: "COMPRESSED", weekly_priority_ref: "P2-spot-check", flow_execution_card_ref: null}
  review_status: "F1-S2 DEGRADED decision open"
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
