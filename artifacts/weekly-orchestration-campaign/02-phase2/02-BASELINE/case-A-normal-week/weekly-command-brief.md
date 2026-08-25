# Weekly Command Brief - 2026-W36 (Case A: normal week)

> **Weekly state:** READY  
> **Direction:** Consolidate the W1 SSoT lock into stable canonical sets for Lika and ACIM, open the ACIM workshop outline on top of locked content, and give Apex exactly two hygiene blocks while Investment stays deliberately parked.  
> **Next action:** APPROVE_WEEK   
> **Review needed:** Whether ACIM workshop outline may start before the Lika vocabulary glossary task lands (dependency direction is Lika -> ACIM).   
> **Scope:** 3 active projects; 2 major outcomes

## Operator decision

- [ ] Approve the week as the planning basis.
- [ ] Edit project priorities or planned work.
- [ ] Reduce scope or defer a named outcome.
- [ ] Resolve a capacity, dependency, or decision constraint.
- [ ] Reject and reframe the weekly direction.

**Decision or instruction:** PENDING - operator_validation not_requested

## Weekly direction

**Weekly intent:** Turn the W1 SSoT lock from a one-week achievement into a stable operating baseline; begin converting locked ACIM content into the workshop outline.  
**Success at week end:**

- Lika and ACIM SSoT indexes pass a full validation walk with zero unresolved red-status conflicts (carried exit criterion from W1 handoff seed).
- ACIM workshop outline exists as a reviewed draft skeleton built only from canonical source IDs.

**Capacity and constraints:**

- Four project flow blocks per weekday per standard blueprint; fixed personal blocks protected. No external meetings this week.

## Day emphasis (directional only - detail belongs to PrecapNextDay)

| Day | Emphasis | Reason |
| :-- | :-- | :-- |
| MON | Lika index validation prep | Fresh week; validation script needs writing before it can run |
| TUE | Lika + ACIM in parallel | Independent after Monday prep |
| WED | Cross-family overlap spot-check | Highest collision risk midweek |
| THU | ACIM workshop outline sprint | Content is stable by then |
| FRI | Validation walk + handoff seed | Gate-check rhythm |

## Project - Lika

**Weekly target:** SSoT index passes full validation walk (every path exists, every file appears exactly once as canonical/redirect/archive).  
**Why this week:** W1 lock declared canonical files but never ran the exhaustive validation; instability here blocks every downstream consumer.  
**Success evidence:** `Lika/SSoT/index.yaml` walks clean; violation list empty or dispositioned.

### Priorities and desired results

1. **Validation tooling** - a repeatable checklist/script walk exists and has been run once.
2. **Violation remediation** - all findings fixed or explicitly deferred with decision-log entries.

### Planned work

- **Work item:** Write + run index validation walk
  - Expected output: validation report with per-file status
  - Owner or executor: operator + agent worker
  - Dependency: none
  - Candidate day: MON-TUE
- **Work item:** Fix or disposition violations
  - Expected output: updated index.yaml + decision-log entries
  - Owner or executor: operator decisions, agent edits
  - Dependency: validation run
  - Candidate day: TUE-WED

### Blockers, risks, and decisions

- **Blocker or risk:** Archive deletion remains operator-reserved from W1 (deliberately deferred).
- **Decision needed:** none this week beyond archive handling.
- **Response this week:** keep archives in place; record any new deferrals.

### Expected outputs

- [Lika validation report](`artifacts/weekly-plans/W36/lika-validation-report.md`) - `planned path`

## Project - ACIM

**Weekly target:** Workshop outline draft skeleton built exclusively from canonical source IDs.  
**Why this week:** Content lock from W1 makes outline work non-wasteful for the first time.  
**Success evidence:** Outline document references only IDs resolvable in `ACIM/SSoT/index.yaml`.

### Priorities and desired results

1. **Outline skeleton** - section structure with mapped source IDs per section.

### Planned work

- **Work item:** Draft workshop outline
  - Expected output: outline markdown, source-ID annotated
  - Owner or executor: agent worker, operator review
  - Dependency: Lika vocabulary decisions (see review flag)
  - Candidate day: THU (FRI fallback)
- **Work item:** Marketing overclaim re-check on outline claims
  - Expected output: flagged list appended to outline
  - Owner or executor: agent worker
  - Dependency: outline draft
  - Candidate day: FRI

### Blockers, risks, and decisions

- **Blocker or risk:** Vocabulary collisions between Lika ops terms and ACIM therapeutic terms (W1 Integrator warning).
- **Decision needed:** whether outline may proceed on provisional vocabulary (operator).
- **Response this week:** flag carried as weekly review needed item.

### Expected outputs

- [ACIM workshop outline](`artifacts/weekly-plans/W36/acim-workshop-outline.md`) - `planned path`

## Project - Apex (maintenance lane)

**Weekly target:** Exactly two hygiene blocks, nothing more.  
**Why this week:** W1 ADR pointer check found references to verify; scope discipline says two blocks maximum.  
**Success evidence:** Broken-reference note resolved or logged.

### Priorities and desired results

1. **ADR reference hygiene** - all orchestration ADR pointers resolve.

### Planned work

- **Work item:** Fix/log broken ADR pointers
  - Expected output: patch notes or issue list
  - Owner or executor: agent worker
  - Dependency: none
  - Candidate day: WED

### Blockers, risks, and decisions

- **Blocker or risk:** none material.
- **Decision needed:** none.
- **Response this week:** n/a

### Expected outputs

- [ADR pointer audit result](`artifacts/weekly-plans/W36/apex-adr-audit.md`) - `planned path`

## Deliberately parked

- **Investment (IPOS):** no capacity allocated this week; registry expansion resumes after governance weeks stabilize. Source: operator standing intent, IN-1 trajectory.

## Cross-project sequence

**Must happen first:**

1. Lika validation before ACIM outline deep-dive - outline consumes Lika vocabulary; unstable vocabulary poisons sections.

**Can run in parallel:**

- Apex hygiene alongside either lane (independent).

**Should not compete for the same capacity:**

- ACIM marketing re-check vs outline sprint (same project, sequential).

**Deliberately deferred:**

- Investment registry work (parked, above).
- Archive deletions (operator-reserved).

## Review flags (include when material)

### Provisional-vocabulary dependency

- **Issue:** ACIM outline depends on Lika vocabulary that will not be fully glossary-stable until W5 per W1 Integrator finding.
- **Why it matters this week:** starting Thursday may mean rewriting sections later.
- **Operator action:** approve provisional-vocabulary start OR hold outline until glossary task.

## Provenance and confidence

**Project-state input:** [W01 weekly plan trajectory](../../../apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md) - `apex-meta/orchestration/simulations/5-week-progressive-simulation/Week-01/weekly_plan.md` (historical simulation input, not live Session state)  
**Other decisive sources:** [Orchestration Index v3](../../../../apex-meta/kb/Weekly-Orchestration/../Weekly-Orchestrator/indexes/APEX_Weekly_Orchestration_Index_v3.yaml) - `apex-meta/kb/Weekly-Orchestrator/indexes/APEX_Weekly_Orchestration_Index_v3.yaml`; W1 handoff-seed conventions (IN-1)  
**Freshness:** INPUT IS HISTORICAL SIMULATION MATERIAL - no live Session/Sync feed exists in workspace; confidence capped accordingly  
**Confidence:** MEDIUM - portfolio facts consistent across sources but no confirmed live feed  
**Assumptions:** W36 follows W1 trajectory directly; no calendar shocks; archive policy unchanged

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-A-normal-week/weekly-command-brief.md"
  week: "2026-W36"
  result_state: "READY"
  weekly_intent: "Consolidate W1 SSoT lock; start ACIM workshop outline"
  project_priority_refs:
    - project_ref: "lika"
      priority_ref: "P1-validation-walk"
    - project_ref: "acim"
      priority_ref: "P1-outline-skeleton"
    - project_ref: "apex"
      priority_ref: "P1-adr-hygiene"
  fixed_constraints:
    - "4 flow blocks per weekday; personal fixed blocks protected"
    - "Apex capped at 2 blocks"
    - "Investment parked"
  review_status: "provisional-vocabulary dependency awaiting operator decision"
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
