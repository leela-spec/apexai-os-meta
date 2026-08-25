# Weekly Command Brief - 2026-W36-C (Case C: deadline vs high-impact conflict)

> **Weekly state:** READY_WITH_REVIEW  
> **Direction:** ACIM workshop outline carries a hard external Thursday-17:00 printing deadline; Lika validation is the higher-leverage item with no external clock and feeds the outline's vocabulary. The week sequences both honestly instead of pretending they fit side by side.  
> **Next action:** RESOLVE_CONSTRAINT | APPROVE_WEEK   
> **Review needed:** Which item absorbs a Wednesday slip: the deadline (ACIM) or the leverage (Lika)? Default per sequence below: Lika yields first, deadline protected.  
> **Scope:** 2 active projects (Apex parked this variant); 2 major outcomes

## Operator decision

- [ ] Approve the week as the planning basis.
- [ ] Edit project priorities or planned work.
- [ ] Reduce scope or defer a named outcome.
- [ ] Resolve a capacity, dependency, or decision constraint.
- [ ] Reject and reframe the weekly direction.

**Decision or instruction:** PENDING - operator_validation not_requested

## Weekly direction

**Weekly intent:** Deliver the ACIM outline to the printer on time WITHOUT silently cannibalizing the Lika validation walk that later weeks depend on.  
**Success at week end:**

- Outline delivered for printing by THU 17:00.
- Lika walk either complete OR explicitly rescheduled with a named new date - never vague.

**Capacity and constraints:**

- Standard four-block weekdays; no calendar anomalies in this variant.

## Day emphasis (directional only - detail belongs to PrecapNextDay)

| Day | Emphasis | Reason |
| :-- | :-- | :-- |
| MON | Lika walk run | dependency source goes first |
| TUE | Lika classification + vocabulary decisions | unblocks outline prose |
| WED | ACIM outline writing sprint | full day available before deadline crunch |
| THU | AM: outline final pass / PM: print handoff | hard deadline 17:00 |
| FRI | Lika catch-up if WED slipped | recovery slot |

## Project - ACIM

**Weekly target:** Workshop outline delivered for printing THU 17:00.  
**Why this week:** external venue deadline - immovable.  
**Success evidence:** print-ready file handed off before cutoff.

### Priorities and desired results

1. **Deadline delivery** - print-ready outline.

### Planned work

- **Work item:** Outline prose sprint
  - Expected output: full draft
  - Owner or executor: agent worker + operator review pass
  - Dependency: Lika vocabulary decisions (TUE)
  - Candidate day: WED (THU AM buffer)
- **Work item:** Print handoff
  - Expected output: file delivered, confirmation received
  - Owner or executor: operator
  - Dependency: draft approved by operator (THU midday)
  - Candidate day: THU PM - HARD GATE

### Blockers, risks, and decisions

- **Blocker or risk:** vocabulary dependency from Lika could slip and compress WED.
- **Decision needed:** see review flag - slip priority.
- **Response this week:** WED morning checkpoint decides which lane absorbs any slip.

### Expected outputs

- [Print-ready outline](`artifacts/weekly-plans/W36C/acim-outline-print.md`) - `planned path`

## Project - Lika

**Weekly target:** Validation walk complete by TUE EOD; slips to FRI only via explicit review-flag decision.  
**Why this week:** highest long-term leverage; also feeds outline vocabulary.  
**Success evidence:** completed classified walk report.

### Priorities and desired results

1. **Walk + classification** - done by TUE EOD.

### Planned work

- **Work item:** Validation walk + triage
  - Expected output: classified report
  - Owner or executor: agent worker
  - Dependency: Monday tooling (done)
  - Candidate day: MON-TUE

### Blockers, risks, and decisions

- **Blocker or risk:** being crowded out by deadline pressure despite being the dependency source.
- **Decision needed:** none if TUE target holds.
- **Response this week:** FRI is its explicit recovery slot.

### Expected outputs

- [Classified walk report](`artifacts/weekly-plans/W36C/lika-walk-classified.md`) - `planned path`

## Deliberately parked

- **Apex hygiene:** parked this variant - two competing priorities already stress the week.
- **Investment:** standing park.

## Cross-project sequence

**Must happen first:**

1. Lika vocabulary decisions (TUE) before outline prose (WED) - dependency direction is real even though the deadline belongs to ACIM.

**Can run in parallel:**

- nothing material; sequencing is the point of this case.

**Should not compete for the same capacity:**

- THU buffer belongs to ACIM until 17:00 passes; Lika does not sneak in.

**Deliberately deferred:**

- Apex hygiene, Investment (above).

## Review flags (include when material)

### Slip-priority rule

- **Issue:** if TUE vocabulary work slips into WED, either the deadline or the walk loses ground.
- **Why it matters this week:** default rule protects the immovable deadline; Lika slides to FRI. Operator may prefer the opposite.
- **Operator action:** confirm default rule or override.

## Provenance and confidence

**Project-state input:** [W01 trajectory](../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md) - historical simulation input class  
**Other decisive sources:** deadline fact supplied as scenario input (see receipt); dependency direction from W1 cross-family findings  
**Freshness:** same class as Case A  
**Confidence:** MEDIUM  
**Assumptions:** venue deadline immovable; print handoff is operator-executed

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-C-dependency-conflict/weekly-command-brief.md"
  week: "2026-W36-C"
  result_state: "READY_WITH_REVIEW"
  weekly_intent: "Deliver ACIM outline by THU 17:00 without silently dropping Lika validation"
  project_priority_refs:
    - project_ref: "acim"
      priority_ref: "P1-deadline-delivery"
    - project_ref: "lika"
      priority_ref: "P1-walk-by-TUE"
  fixed_constraints:
    - "THU 17:00 print cutoff"
    - "Lika -> ACIM dependency direction"
  review_status: "slip-priority rule awaiting confirmation"
  next_consumer: "PreCap_Next_Day_Brief"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/PrecapWeek/SKILL.md"
```
