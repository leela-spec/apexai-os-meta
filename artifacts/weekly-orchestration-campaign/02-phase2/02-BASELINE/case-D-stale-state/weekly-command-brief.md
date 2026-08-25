# Weekly Command Brief - 2026-W36-D (Case D: stale/missing source state)

> **Weekly state:** PARTIAL  
> **Direction:** Planning proceeds on last-known state plus the W1 handoff seed because the Session planning feed is nine days stale and Sync reports are absent for Investment. Every load-bearing assumption is named; confidence is capped accordingly.  
> **Next action:** APPROVE_WEEK | EDIT_PRIORITIES | RESOLVE_CONSTRAINT  
> **Review needed:** Confirm whether to plan Investment at all this week, or extend its park until a fresh Sync report exists  
> **Scope:** 2 confirmed projects + 1 unconfirmed; 1 major outcome

## Operator decision

- [ ] Approve the week as the planning basis.
- [ ] Edit project priorities or planned work.
- [ ] Reduce scope or defer a named outcome.
- [ ] Resolve a capacity, dependency, or decision constraint.
- [ ] Reject and reframe the weekly direction.

**Decision or instruction:** PENDING - operator_validation not_requested

## Weekly direction

**Weekly intent:** Keep consolidation momentum using last-known-good state while making every staleness-driven assumption visible and reversible.  
**Success at week end:**

- Lika/ACIM work advanced one honest step, with no decision that depends on information we do not have.

**Capacity and constraints:**

- Standard four-block weekdays. Source availability, not calendar, is this week's constraint.

## Day emphasis (directional only - detail belongs to PrecapNextDay)

| Day | Emphasis | Reason |
| :-- | :-- | :-- |
| MON | Lika validation prep + refresh attempt | try to re-establish fresh Session/Sync first |
| TUE | Lika walk (state-independent work) | validation reads local files, tolerates staleness |
| WED | ACIM mapping re-check | verify lock assumptions still hold |
| THU | buffer / catch-up | absorbs any staleness surprises |
| FRI | handoff seed + provenance audit | close the week's evidence trail |

## Project - Lika

**Weekly target:** Validation walk complete - chosen partly BECAUSE it does not depend on the missing feeds.  
**Why this week:** highest-leverage work that survives degraded inputs.  
**Success evidence:** classified walk report.

### Priorities and desired results

1. **Walk + classification** - done by TUE EOD.

### Planned work

- **Work item:** State refresh attempt
  - Expected output: fresh Session/Sync pull or documented failure
  - Owner or executor: operator-assisted
  - Dependency: none
  - Candidate day: MON
- **Work item:** Validation walk
  - Expected output: classified report
  - Owner or executor: agent worker
  - Dependency: none beyond Monday tooling
  - Candidate day: TUE

### Blockers, risks, and decisions

- **Blocker or risk:** index.yaml itself may be stale relative to reality - walk findings could reflect drift, not errors.
- **Decision needed:** how to treat drift-class findings (see flags).
- **Response this week:** classify separately as DRIFT_SUSPECTED.

### Expected outputs

- [Classified walk report](`artifacts/weekly-plans/W36D/lika-walk-classified.md`) - `planned path`

## Project - ACIM

**Weekly target:** Mapping table verified against lock state - a staleness check in disguise.  
**Why this week:** if the lock drifted, better to learn it now.  
**Success evidence:** verification note appended to mapping table.

### Priorities and desired results

1. **Mapping verification** - every mapped ID still resolves canonical.

### Planned work

- **Work item:** Mapping verification pass
  - Expected output: verification note
  - Owner or executor: agent worker
  - Dependency: none
  - Candidate day: WED

### Blockers, risks, and decisions

- **Blocker or risk:** content lock assumed stable for 2+ weeks without re-check.
- **Decision needed:** none.
- **Response this week:** verification IS the response.

### Expected outputs

- [Verification note](`artifacts/weekly-plans/W36D/acim-mapping-verification.md`) - `planned path`

## Project - Investment (UNCONFIRMED STATE)

**Weekly target:** none set - cannot be honestly planned from available data.  
**Why this week:** Sync reports absent; registry state unknown.  
**Success evidence:** n/a.

### Priorities and desired results

(none - see review flag)

### Planned work

(none)

### Blockers, risks, and decisions

- **Blocker or risk:** planning blind would violate the no-invention rule.
- **Decision needed:** extend park until fresh Sync exists? (operator)
- **Response this week:** flagged, not decided here.

### Expected outputs

(none)

## Deliberately parked

- **Apex hygiene:** parked pending fresh state (low value under uncertainty).
- **Investment:** park extension requested via flag.

## Cross-project sequence

**Must happen first:**

1. MON state-refresh attempt before anything that would DEPEND on fresh data.

**Can run in parallel:**

- Lika walk and ACIM verification (both read local files).

**Should not compete for the same capacity:**

- n/a.

**Deliberately deferred:**

- anything requiring Investment state; Apex hygiene.

## Review flags (include when material)

### Stale Session feed (9 days)

- **Issue:** no confirmed project-state feed; weekly frame built on last-known state + handoff seed.
- **Why it matters this week:** priorities derived from stale state may misrank.
- **Operator action:** confirm the last-known frame is still valid, or supply corrections.

### Investment park extension

- **Issue:** cannot verify registry state without Sync reports.
- **Operator action:** approve extended park until Sync returns.

## Provenance and confidence

**Project-state input:** NONE CONFIRMED - Session feed stale (last known: 9 days ago); Sync reports absent  
**Substitute sources used:** [W01 trajectory](../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md) (historical input class) + W1 handoff-seed conventions  
**Freshness:** STALE - explicitly capped  
**Confidence:** LOW - every priority carries a staleness caveat; work items were chosen for staleness-tolerance  
**Assumptions:** named inline per section; all revisitable when fresh state arrives

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-D-stale-state/weekly-command-brief.md"
  week: "2026-W36-D"
  result_state: "PARTIAL"
  weekly_intent: "Staleness-tolerant consolidation; refresh attempt first"
  project_priority_refs:
    - project_ref: "lika"
      priority_ref: "P1-walk-staleness-tolerant"
    - project_ref: "acim"
      priority_ref: "P1-mapping-verification"
    - project_ref: "investment"
      priority_ref: "UNPLANNED-awaiting-sync"
  fixed_constraints:
    - "Session feed stale 9 days; Sync absent for Investment"
  review_status: "two flags awaiting operator decisions"
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
