# TEMPLATES

## Purpose

Accepted validated reusable Alfred templates.

## Template schema

```yaml
template_entry:
  id:
  status: accepted | deprecated
  use_when:
  template_body:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: alfred
  validator: meta_ops
  review_due:
```

## Accepted templates

### ALFRED-TPL-001 — First-contact intake

Use when a new operator request arrives and Alfred must convert raw intent into an aligned task frame.

```md
## Alfred Intake

- **Goal:** [what the operator wants changed, decided, created, or understood]
- **Desired output:** [answer / file / patch / route brief / plan / review / recommendation]
- **Context:** [current situation, relevant prior state, live constraint]
- **Timing:** [deadline, day/week pressure, calendar boundary]
- **Capacity:** [energy, available time, cognitive load, emotional sensitivity]
- **Priority:** [why this matters now]
- **Risk:** [what can go wrong if routed or executed incorrectly]
- **Open questions:** [only questions required for safe continuation]
- **Recommended owner:** [Alfred / Meta Ops / Strategy / Detective / KB / Informatics / Prompts / AI Routing / Hygiene]
- **Next action:** [smallest useful step]
```

Evidence: `S1`, `S2`, `S5`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-002 — Weekly alignment

Use when the operator needs to reconcile weekly demand, priorities, capacity, and sequencing.

```md
## Weekly Alignment

- **Path demand:** [targets, priority pressure, carry-over, must-win outcomes]
- **Rhythm supply:** [available windows, boundaries, recovery needs, fixed commitments]
- **Skill Tree / Epic scope:** [which life/work domain or Epic is in focus]
- **Chunk reality:** [what the smallest useful action units are]
- **Sequence mode:** [Spark / Session / Flow / no-run repair]
- **Tradeoff:** [what must be dropped, deferred, shrunk, or protected]
- **Recommendation:** [one clear week-shaping move]
- **Route:** [owner and handoff if Alfred should not execute]
- **Review signal:** [Stats/Sid/feedback signal to inspect later]
```

Evidence: `S3`, `S4`, `S5`, `IDX-N4`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-003 — Day-start sequencing

Use when the operator needs a day-start recommendation that turns priorities and capacity into a next runnable unit.

```md
## Day-Start Sequence Frame

- **Today's anchor:** [main priority or life constraint]
- **Energy/capacity:** [low / medium / high + reason]
- **Time windows:** [available blocks and hard boundaries]
- **Recommended mode:** [Spark / Session / Flow]
- **Why this mode:** [Path demand + Rhythm supply + risk]
- **First Chunk:** [smallest concrete first action]
- **Fallback:** [smaller recovery-safe option]
- **Do not do:** [tempting but wrong action for today]
- **Route if needed:** [Meta Ops / Strategy / Detective / other]
```

Evidence: `S3`, `S4`, `IDX-N4`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-004 — Rhythm repair

Use when the operator's day/week is overloaded, fragmented, blocked, or inconsistent with capacity.

```md
## Rhythm Repair

- **Breakage:** [overload / fragmentation / no recovery / wrong placement / unclear boundary]
- **Demand source:** [Path / Epic / external commitment / emotional pressure]
- **Supply reality:** [available time, energy, calendar, recovery need]
- **Repair move:** [shrink / defer / move / sequence / protect / route / stop]
- **Next runnable unit:** [Spark / Session / Flow / admin repair / rest]
- **Boundary:** [what Alfred must not override]
- **Review cue:** [what to check in Stats or later reflection]
```

Evidence: `S3`, `S4`, `IDX-N4`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-005 — Recommendation handoff

Use when Alfred's recommendation requires another owner to act.

```yaml
alfred_recommendation_handoff:
  from: alfred
  to: [target agent]
  target_surface: [repo path / KB path / project surface / none]
  operator_goal: [goal]
  context: [bounded context]
  constraints:
    time: [timing]
    capacity: [capacity]
    quality: [quality bar]
    boundaries: [do-not-cross]
  recommendation: [what Alfred recommends]
  rationale:
    evidence_band: low | medium | high
    impact_band: low | medium | high
    risk_band: low | medium | high
  expected_output: [what receiver should return]
  validator: [validator]
  open_questions:
    - [question]
  stop_condition: [condition]
```

Evidence: `S1`, `S2`, `S3`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-006 — Escalation to another agent

Use when Alfred detects that normal first-contact coaching is insufficient and the task must route to a governed specialist lane.

```md
## Escalation / Route Decision

- **Reason for escalation:** [execution / strategy / validation / KB / structure / prompt-workflow / AI-routing / hygiene]
- **Why Alfred should not continue alone:** [boundary or risk]
- **Target agent:** [agent id]
- **Expected result:** [specific return artifact]
- **Evidence:** [source, current context, or operator statement]
- **Impact band:** [low / medium / high]
- **Risk band:** [low / medium / high]
- **Validator:** [agent id]
- **Stop condition:** [what blocks safe continuation]
```

Evidence: `S1`, `S2`, `A2`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.
