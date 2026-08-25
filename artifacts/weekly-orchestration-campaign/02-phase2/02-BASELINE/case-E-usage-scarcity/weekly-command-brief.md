# Weekly Command Brief - 2026-W36-E (Case E: usage scarcity / routing degradation)

> **Weekly state:** READY_WITH_REVIEW  
> **Direction:** Case-A consolidation goals under quota constraint: the primary recommended AI surface is exhausted for the week, so sprint routing falls back to a slower local model. Work selection shifts toward tasks that tolerate degraded throughput; two sprints cannot run as recommended and say so explicitly.  
> **Next action:** APPROVE_WEEK | EDIT_PRIORITIES  
> **Review needed:** Accept slower local-model execution for the large-context walk (F1-S2), or defer the walk until quota resets  
> **Scope:** 3 active projects; 2 major outcomes

## Operator decision

- [ ] Approve the week as the planning basis.
- [ ] Edit project priorities or planned work.
- [ ] Reduce scope or defer a named outcome.
- [ ] Resolve a capacity, dependency, or decision constraint.
- [ ] Reject and reframe the weekly direction.

**Decision or instruction:** PENDING - operator_validation not_requested

## Weekly direction

**Weekly intent:** Keep consolidation moving under quota scarcity by matching task difficulty to available surfaces - and making every routing compromise visible instead of silent.  
**Success at week end:**

- Validation walk completed on whatever surface honestly supports it, with readiness flags intact.

**Capacity and constraints:**

- Standard weekday blocks. CONSTRAINT: primary recommended surface quota exhausted; fallback = local model (slower on large contexts).

## Day emphasis (directional only - detail belongs to PrecapNextDay)

| Day | Emphasis | Reason |
| :-- | :-- | :-- |
| MON | small-context tasks only | local model handles these well |
| TUE | walk attempt on fallback OR defer decision | depends on review flag |
| WED | ACIM mapping (small context) | quota-free work |
| THU | catch-up / quota re-check | midweek reset possible |
| FRI | handoff seed + usage summary | close the loop |

## Project - Lika

**Weekly target:** Walk completed via fallback surface IF quality holds, else explicitly deferred to post-reset.  
**Why this week:** still the gating item.  
**Success evidence:** either classified report or a documented deferral decision.

### Priorities and desired results

1. **Walk resolution** - done or consciously deferred.

### Planned work

- **Work item:** Small-sprint prep (S1/S3 class tasks)
  - Expected output: pre-flight and classification ready for instant use
  - Owner or executor: agent worker (local)
  - Dependency: none
  - Candidate day: MON
- **Work item:** Walk execution attempt
  - Expected output: full report
  - Owner or executor: local model fallback
  - Dependency: review flag decision
  - Candidate day: TUE

### Blockers, risks, and decisions

- **Blocker or risk:** local model may degrade walk quality on full-index context.
- **Decision needed:** accept degraded-surface risk or defer (flag below).
- **Response this week:** chunked-walk variant prepared as mitigation.

### Expected outputs

- [Walk report or deferral note](`artifacts/weekly-plans/W36E/lika-walk-or-deferral.md`) - `planned path`

## Project - ACIM

**Weekly target:** Mapping table extended (small context - unaffected by quota).  
**Why this week:** quota-immune progress lane.  
**Success evidence:** mapping coverage increased.

### Priorities and desired results

1. **Mapping extension** - remaining sections mapped.

### Planned work

- **Work item:** Extend mapping
  - Expected output: updated table
  - Owner or executor: agent worker (local)
  - Dependency: none
  - Candidate day: WED

### Blockers, risks, and decisions

- **Blocker or risk:** none material.
- **Decision needed:** none.
- **Response this week:** n/a

### Expected outputs

- [Extended map](`artifacts/weekly-plans/W36E/acim-map-ext.md`) - `planned path`

## Project - Apex

**Weekly target:** one hygiene block (small task, fits degraded week).  
**Why this week:** kept minimal rather than zeroed to preserve momentum.  
**Success evidence:** audit note updated.

### Priorities and desired results

1. **ADR pointer spot-check** - quick pass.

### Planned work

- **Work item:** Pointer spot-check
  - Expected output: updated audit note
  - Candidate day: MON overflow

### Blockers, risks, and decisions

- **Blocker or risk:** none.
- **Decision needed:** none.

### Expected outputs

- [Audit update](`artifacts/weekly-plans/W36E/apex-audit-update.md`) - `planned path`

## Deliberately parked

- **Investment:** standing park.

## Cross-project sequence

**Must happen first:**

1. Review-flag decision before Tuesday's walk attempt.

**Can run in parallel:**

- ACIM mapping alongside any wait state.

**Should not compete for the same capacity:**

- n/a.

**Deliberately deferred:**

- anything requiring the exhausted surface at full fidelity (named per flow in daily plans).

## Review flags (include when material)

### Degraded-surface walk risk

- **Issue:** F1-S2 full-context walk on local fallback may produce lower-quality findings.
- **Why it matters this week:** bad classifications poison Thursday remediation.
- **Operator action:** approve chunked-fallback attempt OR defer until quota reset.

## Provenance and confidence

**Project-state input:** [W01 trajectory](../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md) - historical input class  
**Other decisive sources:** quota status supplied as scenario fact (receipt); routing semantics per PrecapNextDay usage-tracking contract references  
**Freshness:** same class as Case A  
**Confidence:** MEDIUM  
**Assumptions:** quota stays exhausted all week unless THU reset occurs

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-E-usage-scarcity/weekly-command-brief.md"
  week: "2026-W36-E"
  result_state: "READY_WITH_REVIEW"
  weekly_intent: "Quota-aware consolidation; explicit routing compromises"
  project_priority_refs:
    - project_ref: "lika"
      priority_ref: "P1-walk-resolution"
    - project_ref: "acim"
      priority_ref: "P1-mapping-extension"
    - project_ref: "apex"
      priority_ref: "P2-spot-check"
  fixed_constraints:
    - "primary surface quota exhausted; local fallback slower on large contexts"
  review_status: "degraded-surface walk risk awaiting decision"
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
