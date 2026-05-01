# APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW

## 0. File role

```yaml
file_id: APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW
repo: leela-spec/apexai-os-meta
path: managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md
status: working_handover_prompt_flow
canonical_status: non_canonical
purpose: corrected prompt flow for integrating locked Alfred/Apex process-handover priority decisions into Apex AI and Alfred KB
created_for: operator_handoff_to_new_chat
source_decision_locks:
  - managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
  - managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
  - managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md
integration_style: staged_audit_appendices_then_compact_canonical_patches
supersedes: prior V/U/L/F-oriented handover prompt flow
```

This file is a handover prompt flow. It is not canonical doctrine. It gives another chat a controlled sequence for integrating the corrected accepted Alfred/Apex decisions into the repo without reintroducing drift, over-engineering, or hidden truth mutation.

---

# 1. Critical corrected premise

The integration chat must treat these as locked:

- **Alfred is the only current-system personal assistant actor.**
- **Leela is future productization, not current runtime.**
- **Existing first-wave agent handoff contracts use `EVD / IMP / RSK`, 1-100. Preserve them.**
- **Alfred/Apex process handovers use `EVD / IMP / RSK + URG`, 1-100, only where time pressure changes prioritization.**
- **The prior `value / urgency / leverage / fit` model is rejected as a parallel canonical metric system.**
- **`value` is absorbed into `IMP`.**
- **`urgency` becomes `URG`.**
- **`leverage` becomes rationale / unlock effect, not a score.**
- **`fit` becomes readiness, constraints, and hard flags, not a score.**
- **Informatics Design owns structure, taxonomy, naming, decomposition, and retrieval-safe packaging, but not truth validation or final promotion.**
- **Agent handoffs and process handovers must remain bounded, reviewable, state-aware, source-aware, and resistant to drift.**
- **The corrected locked decisions are captured in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.**

---

# 2. Non-negotiable constraints

1. Do not introduce another current-system personal assistant actor.
2. Do not treat Leela app as current runtime.
3. Do not silently mutate SSOT, OpState, calendar, or canonical KB truth.
4. Do not reintroduce `value / urgency / leverage / fit` as canonical fields.
5. Do not create `APPENDIX_APEX_ORIENTATION_AND_ROUTING.md` under the old V/U/L/F model.
6. Do not replace first-wave `EVD / IMP / RSK` handoff thresholds.
7. Add `URG` only for process handovers where time pressure matters.
8. Preserve candidate/canonical separation.
9. Use appendices for operational detail, then compact canonical patches.
10. Process files should be patched only if there is a real contradiction, gap, or pointer update need.
11. Every patch must include a simplification check.
12. Prefer one file per patch pass unless the operator explicitly authorizes a paired source/audit update.

---

# 3. Correct metric model

```yaml
agent_handoff_metrics_v1:
  EVD: 1-100
  IMP: 1-100
  RSK: 1-100

process_handover_priority_v1:
  metrics:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
    URG: 1-100
  controls:
    readiness: ready|partial|missing_input|blocked|operator_decision_needed
    lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3
  rationale:
    impact_reason:
    urgency_reason:
    unlocks: []
    risk_note:
    next_action:
```

## 3.1 Applies to

| Surface | Model |
|---|---|
| Formal first-wave agent handoff | `EVD / IMP / RSK`; add `URG` only if time pressure materially affects priority |
| Night -> Alfred morning handover | `EVD / IMP / RSK + URG` |
| Session Export -> Night synthesis | trace first; Night may derive `EVD / IMP / RSK + URG` planning packets |
| Daily Command Board priority stack | `EVD / IMP / RSK + URG` plus readiness/lane/hard flags |
| Craft-flow allocation CF1-CF4 | P-class derived from process-handover metrics and readiness |
| Raw Session Export trace | no priority metrics required in raw trace |
| OpState delta candidate | evidence and operator approval fields; no P-class unless routed for planning |
| Pattern candidate | evidence count and source refs; no P-class unless routed for planning |

---

# 4. Prompt 0 — Bootstrap and non-drift setup

```text
# Apex + Alfred KB Integration Bootstrap — Corrected Metric Model

You are integrating locked Alfred/Apex process-handover decisions into the Apex AI and Alfred KB system.

Repo:
- leela-spec/apexai-os-meta

Primary locked decision files:
- managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
- managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md

Process / informatics / handoff sources:
- managed/agents/special_ops__informatics_design.md
- managed/processes/AGENT_HANDOFF_CONTRACTS.md
- managed/rules/OPERATING_SPINE_CANON.md
- managed/rituals/NIGHT_PLANNING_PROTOCOL.md
- managed/rituals/SESSION_EXPORT_PROTOCOL.md
- managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
- managed/knowledge/AGENT_KB_LANES.md
- managed/agent_kb/alfred/README.md
- managed/agent_kb/alfred/ESSENCE.md
- managed/agent_kb/alfred/BEST_PRACTICES.md
- managed/agent_kb/alfred/MISTAKES.md
- managed/agent_kb/alfred/TEMPLATES.md
- managed/agent_kb/alfred/LEARNING_QUEUE.md
- managed/agent_kb/alfred/SOURCE_MANIFEST.md
- managed/agent_kb/alfred/COVERAGE_AUDIT.md

Non-negotiable constraints:
1. Alfred is the only current-system personal assistant actor.
2. Leela is future productization, not current runtime.
3. Existing first-wave `EVD / IMP / RSK` handoff thresholds remain intact.
4. Process handovers use `EVD / IMP / RSK + URG`, 1-100.
5. `value / urgency / leverage / fit` must not be reintroduced as canonical fields.
6. `value` is absorbed into `IMP`; `urgency` becomes `URG`; `leverage` becomes rationale/unlock effect; `fit` becomes readiness/constraints/hard flags.
7. Preserve candidate/canonical separation.
8. Use appendices first, then compact canonical patches.
9. One file per patch pass unless explicitly instructed otherwise.
10. Every proposed patch must include a simplification check.

First task:
- Read all listed files.
- Produce a source map and integration risk map.
- Do not write files yet.

Output:
1. SOURCE_MAP
2. DECISION_SUMMARY
3. CORRECTED_METRIC_MODEL
4. TARGET_FILE_MAP
5. INTEGRATION_RISKS
6. PATCH_ORDER
7. OPEN_QUESTIONS_BLOCKING_WRITES

Stop after this audit.
```

---

# 5. Prompt 1 — Confirm corrected metric model

```text
# Control Pass — Corrected Metric Model

Mission:
Prevent metric-system collision and lock the corrected model.

Read:
- managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- managed/processes/AGENT_HANDOFF_CONTRACTS.md

Must lock:
1. `EVD / IMP / RSK` remain the existing first-wave handoff control model.
2. Alfred/Apex process handovers add `URG` when time pressure matters.
3. Do not merge in `value / leverage / fit` as score variables.
4. `value` is absorbed into `IMP`.
5. `urgency` becomes `URG` and uses 1-100.
6. `leverage` is rationale/unlock effect, not score.
7. `fit` is readiness/constraints/hard flags, not score.
8. Do not convert `EVD / IMP / RSK` to 0-3.
9. Do not create a second 0-3 orientation system.

Output:
1. Final corrected model.
2. When `URG` applies.
3. Collision examples.
4. Anti-drift rules.
5. Patch targets.
6. Recommended wording for appendices and canonical files.

Do not write files yet.
```

---

# 6. Prompt 2 — Integration architecture map

```text
# Integration Architecture Map — Corrected Alfred/Apex Process Handover Model

Mission:
Create the file-level integration plan for the corrected `EVD / IMP / RSK + URG` model.

Candidate new appendices:
- managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md
- managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
- managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
- managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md

Canonical files to patch later:
- ESSENCE.md
- BEST_PRACTICES.md
- MISTAKES.md
- TEMPLATES.md
- LEARNING_QUEUE.md
- SOURCE_MANIFEST.md
- COVERAGE_AUDIT.md
- README.md

Process files to inspect but not overwrite unless necessary:
- AGENT_HANDOFF_CONTRACTS.md
- OPERATING_SPINE_CANON.md
- NIGHT_PLANNING_PROTOCOL.md
- SESSION_EXPORT_PROTOCOL.md

Rules:
- Appendices carry operational detail.
- Canonical files carry compact doctrine only.
- Process files should be patched only if the corrected decisions expose a real contradiction, gap, or pointer update need.
- Informatics Design should be used as the structure/taxonomy/retrieval-safety lens.
- Knowledge/KB operations should be used as promotion/candidate/canonical lens.
- MetaOps remains execution workflow owner.
- Alfred remains operator-facing planner/coordinator.

Output:
1. Concept-to-file matrix.
2. Proposed appendix set.
3. Canonical patch matrix.
4. Process-file patch/no-patch verdict.
5. Naming/taxonomy recommendations.
6. Retrieval-safety recommendations.
7. Simplification opportunities.
8. Open issues.

Do not write files yet.
```

---

# 7. Prompt 3 — Create appendix: Process handover priority

```text
# Create APPENDIX_PROCESS_HANDOVER_PRIORITY.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md

Mission:
Create Alfred's operational appendix for process-handover priority using `EVD / IMP / RSK + URG`.

Must include:
1. Purpose
2. Authority boundary
3. Relationship to `AGENT_HANDOFF_CONTRACTS.md`
4. Difference between agent handoff and process handover
5. Core metrics:
   - EVD
   - IMP
   - RSK
   - URG
   - 1-100 scale
6. Replaced variable mapping:
   - value -> IMP
   - urgency -> URG
   - leverage -> rationale.unlocks
   - fit -> readiness/constraints/hard_flags
7. Controls:
   - readiness
   - lane
   - hard_flags
8. Hard flags:
   - hard_deadline
   - blocked
   - missing_input
   - operator_decision_needed
   - hygiene_hold
   - calendar_conflict
   - no_actionable_next_step
9. P0-P3 priority classification
10. P1 max-four-craft-flow rule
11. P0 no-auto-assign rule
12. Low-evidence / low-readiness handoff rule
13. Examples:
   - Night -> Day Leela P1
   - urgent Master of Arts P0 candidate
   - blocked P3
   - calendar conflict P0/rhythm repair
14. Anti-patterns:
   - reintroducing V/U/L/F
   - weighted total score
   - hidden evidence weakness
   - lane as score
   - assigning more than four P1s
15. Source basis
16. Open future improvements

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# 8. Prompt 4 — Create appendix: Daily Command Board and MetaOps handoffs

```text
# Create APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md

Mission:
Define Alfred's Daily Command Board and Alfred -> MetaOps craft-flow handoff using corrected `EVD / IMP / RSK + URG` priority control.

Must include:
1. Purpose
2. Daily Command Board v1 schema
3. Project Packet v1 schema
4. Priority control fields:
   - EVD
   - IMP
   - RSK
   - URG
   - readiness
   - lane
   - hard_flags
   - priority_class
5. Four craft-flow working day:
   - CF1 Leela
   - CF2 Leela
   - CF3 Master of Arts
   - CF4 wildcard
6. Daily priority stack
7. Separate `rhythm_profile`
8. Board lock rule
9. Deferred/not-today handling
10. P0 risks and repairs section
11. MetaOps Craft Flow Handoff v1
12. Relationship to AGENT_HANDOFF_CONTRACTS:
    - local craft-flow brief
    - formal first-wave handoff packet
13. Examples
14. Operator edit tracking
15. Anti-patterns
16. Source basis
17. Open future improvements

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# 9. Prompt 5 — Create appendix: Session Export, OpState, and tracking

```text
# Create APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md

Mission:
Define the trace/state/tracking model for Alfred's craft-flow loop.

Must preserve:
- Session Export is trace.
- OpState is state delta candidate only.
- Raw Session Export does not need priority metrics.
- Night may derive process-handover priority packets from Session Exports.

Must include:
1. Purpose
2. Trace vs state distinction
3. Session Export as immutable trace after submission
4. Correction rule
5. Operator-required Session Export fields
6. What Alfred/Night pre-fills
7. What operator corrects
8. OpState delta candidate v1
9. OpState approval v1
10. Tracking Record v1 schema
11. Mood/energy/BP-XP excluded in Alfred tracking v1
12. Tracking rollups
13. Relationship to NIGHT_PLANNING_PROTOCOL.md and SESSION_EXPORT_PROTOCOL.md
14. Examples
15. Anti-patterns
16. Source basis
17. Future improvements

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# 10. Prompt 6 — Create appendix: Pattern learning and Rhythm

```text
# Create APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md

Mission:
Define Alfred's candidate pattern learning and Rhythm planning reference.

Must include:
1. Purpose
2. Pattern learning boundary
3. Pattern candidate creation thresholds
4. Pattern promotion thresholds
5. Rejected candidate archive
6. Operator override learning
7. Rhythm in Daily Command Board
8. Afterwork regeneration
9. Weekly planning v1 / v1.1 split
10. Monthly planning later/directional
11. Relationship to skill-tree/chunk system
12. Examples
13. Anti-patterns
14. Source basis
15. Future improvements register

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# 11. Prompt 7 — Patch parent working decision lock references

```text
# Patch ALFRED_WORKFLOW_DECISION_LOCK.md references

Target:
- managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md

Mission:
Update the parent Alfred decision lock to point to the corrected Apex variable/handoff decision lock and mark prior open questions as resolved.

Must update:
1. Add reference to:
   - managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
2. Mark first heuristic ranking model as resolved by:
   - `EVD / IMP / RSK + URG` process-handover priority model
3. Mark these as resolved:
   - Daily Command Board fields
   - pre-filled Session Export fields
   - how far ahead Alfred plans in v1
   - pattern candidate location/path
   - minimum tracking format
   - MetaOps handoff schema
   - operator board editability
   - Night scaffold low-friction correction
4. Preserve unresolved items that are genuinely still open.
5. Preserve Alfred-only naming lock.
6. Preserve non-canonical working status.

Output:
- Unified diff only.
- Resolution table.
- Remaining open questions.
- Stop before applying unless instructed.
```

---

# 12. Canonical patch prompts

Canonical patches must be compact. They must not repeat full appendix schemas.

## ESSENCE.md

Add only compact doctrine:

- Alfred may use corrected process-handover priority control: `EVD / IMP / RSK + URG`.
- Alfred uses P0-P3 classes for Daily Command Board and process-handover routing.
- Alfred respects the four-craft-flow workday.
- Alfred creates Daily Command Board recommendations.
- Alfred sends bounded MetaOps handoffs.
- Alfred treats Session Exports as trace, OpState as state delta, and patterns as candidates until promoted.
- Alfred does not silently mutate SSOT, OpState, calendar, or canonical KB.
- Alfred remains the only current-system personal assistant actor.

Must not include V/U/L/F.

## BEST_PRACTICES.md

Add accepted practice for:

- Project Packet review
- `EVD / IMP / RSK + URG` process-handover priority
- readiness/lane/hard flag practice
- P0-P3 classification
- Daily Command Board
- MetaOps handoff
- Session Export / OpState separation
- tracking
- pattern candidates
- rhythm profile
- weekly preview/monthly directional planning

Must include:

- Do not use weighted total scoring.
- Do not reintroduce V/U/L/F.
- Do not assign more than four P1 craft-flow items.
- Do not auto-assign P0.
- Do not let Session Export mutate OpState directly.
- Do not promote patterns without threshold.

## MISTAKES.md

Add failure modes:

- Reintroducing V/U/L/F as a second metric system.
- Treating Leela app as runtime.
- Reintroducing a second current-system personal assistant actor.
- Using weighted score totals as if precise.
- Treating lane as importance.
- Ignoring hard flags.
- Assigning more than four P1 craft-flow items.
- Auto-assigning P0 without operator confirmation.
- Mutating board after operator lock.
- Putting full Session Export trace into OpState.
- Letting Session Export update OpState directly.
- Promoting patterns after one occurrence.
- Tracking mood/energy/BP-XP in Alfred v1 despite exclusion.
- Overbuilding weekly/monthly planning before daily tracking exists.
- Making the Daily Command Board a giant dashboard.

## TEMPLATES.md

Add compact reusable templates:

1. Project Packet v1
2. Daily Command Board v1
3. MetaOps Craft Flow Handoff v1
4. Operator-required Session Export correction
5. OpState Delta Candidate v1
6. Tracking Record v1
7. Pattern Candidate v1
8. Weekly Preview v1
9. Monthly Direction Map placeholder

Templates must use `EVD / IMP / RSK + URG`, readiness, lane, hard flags, and P-class where priority control is needed.

## LEARNING_QUEUE.md

Capture future candidates only:

- Full Weekly Rhythm Plan v1.1
- Monthly Direction Map operationalization
- Low-risk OpState auto-apply classes
- Future Algorithm from tracking evidence
- Future BP/XP relation
- Future mood/energy tracking reconsideration
- Pattern library storage structure
- Automation of candidate detection
- Visualization of Daily Command Board
- Calibration of `EVD / IMP / RSK + URG` and P-class rules from real use

## SOURCE_MANIFEST.md and COVERAGE_AUDIT.md

Add corrected source/audit controls for:

- corrected `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- `ALFRED_WORKFLOW_DECISION_LOCK.md`
- `ALFRED_WORKFLOW_PREFILLED_QA.md`
- `AGENT_HANDOFF_CONTRACTS.md` relationship
- uploaded/manual Rhythm, Sequencing, Craft Flow, and Daily Flow sources when directly available
- Informatics Design role

Do not imply canonical promotion just because a working lock exists.

## README.md

Update index after appendices and corrected lock integration. It must show where to find:

- process-handover priority variables
- Daily Command Board
- MetaOps handoff
- Session Export / OpState
- Tracking
- Pattern learning
- Rhythm profile

---

# 13. Control runs

## Completeness audit rows

- Alfred-only naming
- Leela app boundary
- EVD/IMP/RSK preservation
- URG process-handover extension
- V/U/L/F rejected
- value -> IMP
- urgency -> URG
- leverage -> rationale.unlocks
- fit -> readiness/constraints/hard_flags
- readiness control
- lane guardrail
- hard flags
- P0-P3 classes
- P1 max 4
- P0 no auto-assign
- artifact contract
- Project Packet
- Daily Command Board
- separate rhythm_profile
- board lock/revision
- MetaOps handoff
- Session Export immutability
- operator-required Session Export fields
- OpState delta candidate
- OpState operator approval
- pattern candidate threshold
- pattern promotion threshold
- rejected pattern archive
- tracking v1
- mood/energy/BP-XP excluded
- afterwork regen
- weekly preview v1 / full v1.1
- monthly later/directional

## Simplification audit questions

1. Are there too many appendices?
2. Are schemas duplicated unnecessarily?
3. Are any fields too detailed for v1?
4. Does the Daily Command Board risk becoming a giant dashboard?
5. Does MetaOps handoff over-prescribe MetaOps internals?
6. Is `URG` necessary and bounded?
7. Are readiness and hard flags simple enough?
8. Are tracking fields minimal?
9. Are pattern thresholds enforceable?
10. Does the system preserve high impact with low operator burden?
11. Does retrieval become easier or harder?

## Process/handoff audit questions

1. Are Alfred -> MetaOps handoffs bounded?
2. Do handoffs name source, objective, expected output, constraints, stop condition, and return path?
3. Is the difference between local craft-flow brief and formal first-wave handoff clear?
4. Are EVD/IMP/RSK preserved where existing process requires them?
5. Is URG limited to time-sensitive process handovers?
6. Are V/U/L/F absent as canonical fields?
7. Are target states and authority boundaries clear?
8. Are blocked/operator-review-required states respected?
9. Is candidate/canonical separation preserved?
10. Is OpState protected from trace pollution?
11. Is there any hidden truth mutation?
12. Is there any role-boundary drift?

---

# 14. Recommended execution order

```text
0  Bootstrap
1  Corrected metric model control pass
2  Integration architecture map
3  APPENDIX_PROCESS_HANDOVER_PRIORITY
4  APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS
5  APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING
6  APPENDIX_PATTERN_LEARNING_AND_RHYTHM
7  Patch parent working decision lock references
15 Completeness audit
16 Simplification audit
17 Process/handoff audit
18 Future improvements capture
19 Final consistency gate
8  ESSENCE
9  BEST_PRACTICES
10 MISTAKES
11 TEMPLATES
12 LEARNING_QUEUE
13 SOURCE_MANIFEST + COVERAGE_AUDIT
14 README
19 Final consistency gate again
```

---

# 15. Implementation principle

```yaml
integration_rule:
  appendices: operational_detail
  canonical_files: compact_doctrine
  working_locks: decision_evidence
  source_audit_files: provenance_and_coverage
  learning_queue: future_improvements_only
  process_files: only_patch_if_contradiction_or_pointer_gap_exists
  metric_model: preserve_EVD_IMP_RSK_add_URG_only_for_process_handovers
```

---

# 16. Handover note for next chat

Before doing repo writes, the next chat should read this file and the corrected `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.

The main failure modes to avoid are:

1. Reintroducing V/U/L/F as a canonical metric system.
2. Reintroducing a second current-system personal assistant actor.
3. Treating the future Leela app as runtime.
4. Replacing `EVD / IMP / RSK` in first-wave handoff contracts.
5. Using `URG` outside time-sensitive process handovers.
6. Duplicating long schemas across too many files.
7. Turning the Daily Command Board into a bloated dashboard.
8. Making Session Export mutate OpState directly.
9. Promoting pattern candidates too early.
10. Moving v1.1/monthly future improvements into v1.
11. Patching canonical files before appendices stabilize.
12. Writing process-file changes without a demonstrated contradiction or pointer gap.
