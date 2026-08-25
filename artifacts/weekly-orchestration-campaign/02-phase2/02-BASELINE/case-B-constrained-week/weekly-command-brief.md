# Weekly Command Brief - 2026-W37 (Case B: meeting-heavy/constrained week)

> **Weekly state:** READY_WITH_REVIEW  
> **Direction:** Same consolidation goals as W36 under a heavily reduced calendar: protect the Lika validation walk, compress ACIM outline work to its minimum viable slice, and explicitly omit everything that cannot honestly fit.  
> **Next action:** APPROVE_WEEK | REDUCE_SCOPE   
> **Review needed:** ACIM outline target must drop from reviewed-draft to mapping-table-only this week - confirm acceptance  
> **Scope:** 3 active projects; 1 major outcome (reduced)

## Operator decision

- [ ] Approve the week as the planning basis.
- [ ] Edit project priorities or planned work.
- [ ] Reduce scope or defer a named outcome.
- [ ] Resolve a capacity, dependency, or decision constraint.
- [ ] Reject and reframe the weekly direction.

**Decision or instruction:** PENDING - operator_validation not_requested

## Weekly direction

**Weekly intent:** Keep the SSoT consolidation moving under a ~55%-capacity week; accept explicit, reasoned omissions instead of silent slippage.  
**Success at week end:**

- Lika main-index validation walk completed (the one non-negotiable).

**Capacity and constraints:**

- TUE 09:00-12:00 external meetings; WED workshop-prep day plus 2h review call; FRI half-day. Effective project-flow capacity reduced to roughly 45% of a standard week.

## Day emphasis (directional only - detail belongs to PrecapNextDay)

| Day | Free flows | Emphasis | Deformation |
| :-- | :-- | :-- | :-- |
| MON | 4 | Lika validation run #1 | full |
| TUE | 1-2 | Lika findings triage only | COMPRESSED |
| WED | 1 | none guaranteed - workshop prep dominates | MINIMAL / likely OMITTED |
| THU | 4 | recovery day: remediation + ACIM mapping catch-up | full |
| FRI | 1-2 | validation re-run + handoff seed | COMPRESSED |

## Project - Lika

**Weekly target:** Validation walk completed despite constraint; violations listed even if remediation slips.  
**Why this week:** validation is the gating item for every later consumer; it must not silently slide.  
**Success evidence:** completed walk report exists by FRI noon.

### Priorities and desired results

1. **Validation walk** - executed once fully, findings classified.

### Planned work

- **Work item:** Run + classify validation
  - Expected output: walk report with classification summary
  - Owner or executor: agent worker
  - Dependency: Monday tooling (done in W36)
  - Candidate day: MON (THU fallback)
- **Work item:** Remediation sprint
  - Expected output: fixes for FIX_NOW class only
  - Owner or executor: agent worker
  - Dependency: classification done
  - Candidate day: THU - FIRST TO BE CUT if week degrades further

### Blockers, risks, and decisions

- **Blocker or risk:** WED effectively lost to workshop prep; any MON/TUE slip pushes validation into THU and evicts remediation.
- **Decision needed:** none yet.
- **Response this week:** validation has absolute priority over remediation.

### Expected outputs

- [Walk report](`artifacts/weekly-plans/W37/lika-walk-report.md`) - `planned path`

## Project - ACIM

**Weekly target:** REDUCED - source-ID mapping table maintained; prose outline NOT attempted.  
**Why this week:** capacity honesty: outline writing needs protected blocks that do not exist this week.  
**Success evidence:** mapping table survives the week without regression.

### Priorities and desired results

1. **Mapping maintenance** - keep Thursday's catch-up slot if it materializes.

### Planned work

- **Work item:** Mapping table catch-up
  - Expected output: updated table if THU slot holds
  - Owner or executor: agent worker
  - Dependency: THU capacity actually free
  - Candidate day: THU - cut first inside ACIM lane

### Blockers, risks, and decisions

- **Blocker or risk:** expectation mismatch - operator may still expect outline progress.
- **Decision needed:** confirm reduced ACIM target (review needed item).
- **Response this week:** reduction surfaced in top block, not buried.

### Expected outputs

(none committed this week beyond optional mapping update)

## Project - Apex (maintenance lane)

**Weekly target:** Zero blocks this week - hygiene capped out by constraint.  
**Why this week:** two-block W36 discipline continues as zero under compression.  
**Success evidence:** nothing breaks from being left alone.

### Priorities and desired results

(none - omitted lane)

### Planned work

(none)

### Blockers, risks, and decisions

- **Blocker or risk:** none.
- **Decision needed:** none.
- **Response this week:** n/a

### Expected outputs

(none)

## Deliberately parked

- **Investment (IPOS):** unchanged park.
- **Apex hygiene:** newly parked THIS WEEK by capacity decision (was active W36) - visible omission, not drift.

## Cross-project sequence

**Must happen first:**

1. Lika validation before anything else claims MON capacity.

**Can run in parallel:**

- nothing reliably - parallel slots are what the calendar removed.

**Should not compete for the same capacity:**

- ACIM catch-up vs Lika remediation on THU: Lika wins.

**Deliberately deferred:**

- ACIM prose outline (to W38, pending operator confirmation of reduction)
- Apex hygiene (to W38)
- Investment (standing park)

## Review flags (include when material)

### Reduced ACIM commitment

- **Issue:** outline draft is impossible in ~55% week without evicting the validation walk.
- **Why it matters this week:** sets stakeholder expectations for venue-printing timeline downstream.
- **Operator action:** approve reduction OR name what to evict instead.

## Provenance and confidence

**Project-state input:** [W01 trajectory](../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md) - `apex-meta/.../Week-01/weekly_plan.md` (historical simulation input class)  
**Other decisive sources:** calendar constraints supplied as scenario facts (see receipt inputs); deformation semantics from `calendar-planning-guidance.md` + `weekly-blueprint-meeting-example.md`  
**Freshness:** same class as Case A - no live feed  
**Confidence:** MEDIUM - capacity math derived from stated meeting blocks, not a live calendar read  
**Assumptions:** meeting blocks are immovable; no additional shocks

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-B-constrained-week/weekly-command-brief.md"
  week: "2026-W37"
  result_state: "READY_WITH_REVIEW"
  weekly_intent: "Validation walk under 55% capacity; explicit omissions"
  project_priority_refs:
    - project_ref: "lika"
      priority_ref: "P1-validation-walk"
    - project_ref: "acim"
      priority_ref: "REDUCED-mapping-only"
    - project_ref: "apex"
      priority_ref: "OMITTED-this-week"
  fixed_constraints:
    - "TUE AM meetings; WED lost; FRI half-day"
    - "~55% capacity vs standard blueprint"
  review_status: "ACIM reduction awaiting operator decision"
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
