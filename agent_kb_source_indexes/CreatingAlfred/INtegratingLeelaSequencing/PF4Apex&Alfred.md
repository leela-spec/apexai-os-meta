# Prompt flow — Integrate Apex decisions into Apex AI + Alfred KB

Use this in a new chat. It is designed to be stage-gated, repo-grounded, and resistant to over-engineering.

## Critical premise

The other chat must treat these as locked:

- **Alfred is the only current-system personal assistant actor.**

- **Leela is future productization, not current runtime.**

- **Apex orientation uses `value / urgency / leverage / fit`, 0–3, with P0–P3 classification.**

- **Existing first-wave agent handoff contracts use `EVD / IMP / RSK`, 1–100. Do not replace them with V/U/L/F.**

- **Informatics Design owns structure, taxonomy, naming, decomposition, and retrieval-safe packaging, but not truth validation or final promotion.**

- **Agent handoffs must remain bounded, reviewable, state-aware, source-aware, and resistant to drift.**

- **The locked Apex variable/handoff decisions are now captured in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.**


---

# Prompt 0 — Bootstrap and non-drift setup

```text
# Apex + Alfred KB Integration Bootstrap

You are integrating locked workflow decisions into the Apex AI and Alfred KB system.

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
2. Do not introduce another assistant actor.
3. Do not treat Leela app as current runtime.
4. Do not silently mutate SSOT, OpState, calendar, or canonical KB truth.
5. Do not replace first-wave `EVD / IMP / RSK` handoff thresholds with `value / urgency / leverage / fit`.
6. Treat `value / urgency / leverage / fit` as Alfred/Apex planning orientation for project packets, daily boards, craft-flow assignment, and routing—not as a replacement for general agent handoff risk thresholds.
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
3. TWO-TIER_METRIC_MODEL
4. TARGET_FILE_MAP
5. INTEGRATION_RISKS
6. PATCH_ORDER
7. OPEN_QUESTIONS_BLOCKING_WRITES

Stop after this audit.
```

---

# Prompt 1 — Confirm the two-tier metric model

```text
# Control Pass — Two-Tier Metric Model

Mission:
Prevent metric-system collision between:
A. Apex/Alfred planning orientation
B. First-wave agent handoff risk/evidence thresholds

Read:
- managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- managed/processes/AGENT_HANDOFF_CONTRACTS.md

Create a precise decision memo.

Must lock:
1. `value / urgency / leverage / fit` are for Alfred/Apex daily planning, project packets, Daily Command Board, craft-flow allocation, and routing recommendations.
2. `EVD / IMP / RSK` remain the first-wave agent handoff threshold model.
3. Do not merge the systems.
4. Do not convert `EVD / IMP / RSK` to 0–3.
5. Do not convert `value / urgency / leverage / fit` to 1–100.
6. When Alfred sends MetaOps a craft-flow handoff, include Apex orientation only if it helps explain daily priority, but maintain any required handoff contract fields if the handoff crosses first-wave process boundaries.

Output:
1. Final two-tier model.
2. When each metric system applies.
3. Collision examples.
4. Anti-drift rules.
5. Patch targets.
6. Recommended wording for appendices and canonical files.

Do not write files yet.
```

---

# Prompt 2 — Integration architecture map

```text
# Integration Architecture Map — Apex Decisions into Alfred KB

Mission:
Create the file-level integration plan.

Use the locked decisions to determine exactly where each concept belongs.

Candidate new appendices:
- managed/agent_kb/alfred/appendices/APPENDIX_APEX_ORIENTATION_AND_ROUTING.md
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
- Process files should be patched only if the locked decisions expose a real contradiction, gap, or pointer update need.
- Informatics Design should be used as the structure/taxonomy/retrieval-safety lens.
- Knowledge/KB operations should be used as promotion/candidate/canonical lens.
- MetaOps should remain execution workflow owner.
- Alfred should remain operator-facing planner/coordinator.

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

# Prompt 3 — Create appendix: Apex orientation and routing

```text
# Create APPENDIX_APEX_ORIENTATION_AND_ROUTING.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_APEX_ORIENTATION_AND_ROUTING.md

Mission:
Create Alfred’s operational appendix for Apex planning orientation and next-action routing.

Must include:
1. Purpose
2. Authority boundary
3. Relationship to broader first-wave `EVD / IMP / RSK` handoff model
4. Apex Orientation Core v1:
   - value
   - urgency
   - leverage
   - fit
   - 0–3 scale
5. Removed/absorbed variables:
   - time_pressure → urgency
   - risk_if_deferred → urgency
   - effort → fit
   - readiness/calendar/operator constraint → fit
   - default_lane_alignment → policy_lane
6. Controls:
   - confidence as modifier/display field
   - policy_lane as guardrail
7. Hard flags:
   - hard_deadline
   - blocked
   - missing_input
   - operator_decision_needed
   - hygiene_hold
   - calendar_conflict
   - no_actionable_next_step
8. P0–P3 priority classification
9. P1 max-four-craft-flow rule
10. P0 no-auto-assign rule
11. Low-confidence handoff rule
12. Examples:
   - Leela P1
   - Master of Arts P1/P0
   - blocked P3
   - calendar conflict P0/rhythm repair
13. Anti-patterns:
   - weighted total score
   - 0–10 scoring
   - hidden confidence
   - policy lane as score
   - assigning more than four P1s
14. Source basis
15. Open future improvements

Output:
- Full proposed file content.
- Unified diff.
- Simplification check:
  - What could be removed?
  - What is necessary?
  - What is over-engineered?
- Stop before applying unless instructed.
```

---

# Prompt 4 — Create appendix: Daily Command Board and MetaOps handoffs

```text
# Create APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md

Mission:
Define Alfred’s Daily Command Board and Alfred → MetaOps craft-flow handoff.

Must include:
1. Purpose
2. Daily Command Board v1 schema
3. Project Packet v1 schema
4. Four craft-flow working day:
   - CF1 Leela
   - CF2 Leela
   - CF3 Master of Arts
   - CF4 wildcard
5. Daily priority stack
6. Separate `rhythm_profile`
   - physical chunk candidates by flow
   - mental chunk candidates by flow
   - final break/reset
   - afterwork regen plan
7. Board lock rule:
   - before operator lock editable
   - after lock immutable
   - revisions only after lock
8. Deferred/not-today handling
9. P0 risks and repairs section
10. MetaOps Craft Flow Handoff v1:
    - identity
    - intent
    - constraints
    - mandatory outputs
    - optional outputs
    - state_effect defaults
11. Relationship to AGENT_HANDOFF_CONTRACTS:
    - when this is a local Alfred→MetaOps craft-flow brief
    - when formal first-wave handoff packet is required
12. Examples:
    - normal Leela flow
    - urgent Master of Arts override
    - low-confidence discovery handoff
    - overloaded day with deferred P1
13. Operator edit tracking
14. Anti-patterns:
    - board as giant dashboard
    - mixing rhythm profile into every card
    - auto-mutating after lock
    - sending raw project dumps to MetaOps
15. Source basis
16. Open future improvements

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# Prompt 5 — Create appendix: Session Export, OpState, and tracking

```text
# Create APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md

Mission:
Define the trace/state/tracking model for Alfred’s craft-flow loop.

Must include:
1. Purpose
2. Trace vs state distinction
3. Session Export as immutable trace after submission
4. Correction rule:
   - append correction event
   - no silent overwrite
5. Operator-required Session Export fields:
   - objective_met
   - outputs_delivered
   - deviations
   - blockers_found
   - next_highest_impact_tasks max 3
   - process_worked enum
   - chat_flow_efficiency enum
6. What Alfred/Night pre-fills
7. What operator corrects
8. OpState delta candidate v1:
   - delta_id
   - project_id
   - source_session_export_id
   - field_path
   - old_value
   - proposed_value
   - reason
   - evidence
   - operator_approved false
9. OpState approval v1:
   - operator required
   - no auto-apply
   - possible later low-risk auto-apply classes
10. Tracking Record v1 schema
11. Mood/energy/BP-XP excluded in v1
12. Tracking rollups:
   - daily
   - weekly preview
   - pattern candidates
   - future Algorithm evidence
13. Relationship to existing NIGHT_PLANNING_PROTOCOL.md and SESSION_EXPORT_PROTOCOL.md
14. Examples:
   - complete session
   - partial session
   - blocked session
   - correction after submission
15. Anti-patterns:
   - full trace into OpState
   - editable trace without revision
   - making operator write essays
   - mood/energy tracking in v1
16. Source basis
17. Future improvements

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# Prompt 6 — Create appendix: Pattern learning and Rhythm

```text
# Create APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md

Target:
- managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md

Mission:
Define Alfred’s candidate pattern learning and Rhythm planning reference.

Must include:
1. Purpose
2. Pattern learning boundary:
   - candidate is not canonical
   - working pattern library is not accepted truth
3. Pattern candidate creation:
   - repeated success >= 2
   - repeated failure same root cause >= 2
   - repeated operator correction same field >= 2
   - highly efficient workflow seen >= 2
4. Pattern promotion:
   - successful uses >= 3
   - evidence across >= 2 sessions or periods
   - operator approved
   - KB Ops placed
   - emergency manual promotion label
5. Rejected candidate archive
6. Operator override learning:
   - single override = planning correction
   - repeated same override count 2 = candidate
   - canonical change requires validation
7. Rhythm in Daily Command Board:
   - light v1 rhythm_profile
   - separate from execution cards
8. Afterwork regeneration:
   - planned by Alfred
   - does not replace work craft flow
   - optional note only
9. Weekly planning:
   - v1 light preview
   - v1.1 full Weekly Rhythm Plan
10. Monthly planning:
   - later
   - directional only
11. Relationship to skill-tree/chunk system:
   - lightweight candidate capture now
   - no taxonomy over-design
12. Examples:
   - repeated successful MetaOps handoff
   - repeated operator board correction
   - recurring blocker
   - physical/mental chunk rotation
13. Anti-patterns:
   - promoting after one occurrence
   - deleting rejected patterns
   - full weekly automation too early
   - detailed monthly task schedule in v1
14. Source basis
15. Future improvements register

Output:
- Full proposed file content.
- Unified diff.
- Simplification check.
- Stop before applying unless instructed.
```

---

# Prompt 7 — Patch parent working decision lock references

```text
# Patch ALFRED_WORKFLOW_DECISION_LOCK.md references

Target:
- managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md

Mission:
Update the parent Alfred decision lock to point to the new Apex variable/handoff decision lock and mark prior open questions as resolved.

Must update:
1. Add reference to:
   - managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
2. Mark these as resolved:
   - Daily Command Board fields
   - pre-filled Session Export fields
   - first heuristic ranking model
   - how far ahead Alfred plans in v1
   - pattern candidate location/path
   - minimum tracking format
   - MetaOps handoff schema
   - operator board editability
   - Night scaffold low-friction correction
3. Preserve unresolved items that are genuinely still open.
4. Preserve Alfred-only naming lock.
5. Preserve non-canonical working status.

Output:
- Unified diff only.
- Resolution table.
- Remaining open questions.
- Stop before applying unless instructed.
```

---

# Prompt 8 — Canonical patch: ESSENCE.md

```text
# Patch Alfred ESSENCE.md — compact doctrine only

Target:
- managed/agent_kb/alfred/ESSENCE.md

Mission:
Add compact canonical doctrine reflecting the accepted Apex decisions without bloating ESSENCE.md.

Must add:
1. Alfred uses Apex orientation logic for daily/project planning:
   - value
   - urgency
   - leverage
   - fit
2. Alfred uses P0–P3 classes for routing/project packet orientation.
3. Alfred respects the four-craft-flow workday.
4. Alfred creates Daily Command Board recommendations.
5. Alfred sends bounded MetaOps handoffs.
6. Alfred treats Session Exports as trace, OpState as state delta, and patterns as candidates until promoted.
7. Alfred does not silently mutate SSOT, OpState, calendar, or canonical KB.
8. Alfred remains the only current-system personal assistant actor.

Must not include:
- full schemas
- long examples
- detailed tracking fields
- implementation mechanics
- future app assistant naming

Output:
- Unified diff.
- Canonical scope note.
- Over-engineering check.
```

---

# Prompt 9 — Canonical patch: BEST_PRACTICES.md

```text
# Patch Alfred BEST_PRACTICES.md — operational practice

Target:
- managed/agent_kb/alfred/BEST_PRACTICES.md

Mission:
Add accepted practice for using the Apex decisions in real Alfred operation.

Must add practice sections:
1. Project Packet review practice
2. Orientation scoring practice:
   - V/U/L/F
   - confidence
   - policy_lane
   - hard_flags
3. P0–P3 classification practice
4. Daily Command Board practice
5. MetaOps handoff practice
6. Session Export / OpState separation practice
7. Tracking practice
8. Pattern candidate practice
9. Rhythm profile practice
10. Weekly preview / monthly directional practice

Must include:
- Do not use weighted total scoring.
- Do not assign more than four P1 craft-flow items.
- Do not auto-assign P0.
- Do not let Session Export mutate OpState directly.
- Do not promote patterns without threshold.

Output:
- Unified diff.
- Simplification check.
```

---

# Prompt 10 — Canonical patch: MISTAKES.md

```text
# Patch Alfred MISTAKES.md — failure modes

Target:
- managed/agent_kb/alfred/MISTAKES.md

Mission:
Add failure modes created by the new Apex orientation/handoff system.

Add mistakes:
1. Reintroducing a second current-system personal assistant actor.
2. Treating Leela app as runtime.
3. Mixing V/U/L/F with EVD/IMP/RSK.
4. Using weighted score totals as if precise.
5. Treating confidence as priority.
6. Treating policy lane as importance.
7. Ignoring hard flags.
8. Assigning more than four P1 craft-flow items.
9. Auto-assigning P0 without operator confirmation.
10. Mutating board after operator lock.
11. Putting full Session Export trace into OpState.
12. Letting Session Export update OpState directly.
13. Promoting patterns after one occurrence.
14. Tracking mood/energy/BP-XP in v1 despite exclusion.
15. Overbuilding weekly/monthly planning before daily tracking exists.
16. Making the Daily Command Board a giant dashboard.

Output:
- Unified diff.
- Failure-mode rationale.
```

---

# Prompt 11 — Canonical patch: TEMPLATES.md

```text
# Patch Alfred TEMPLATES.md — templates and schemas

Target:
- managed/agent_kb/alfred/TEMPLATES.md

Mission:
Add compact reusable templates. Put full details in appendices; templates should be usable directly.

Add templates:
1. Project Packet v1
2. Daily Command Board v1
3. MetaOps Craft Flow Handoff v1
4. Operator-required Session Export correction
5. OpState Delta Candidate v1
6. Tracking Record v1
7. Pattern Candidate v1
8. Weekly Preview v1
9. Monthly Direction Map placeholder

Rules:
- Keep templates compact.
- Use canonical field names from APEX_VARIABLES_HANDOFF_DECISION_LOCK.md.
- Do not include old variable names except in “removed/absorbed” note if needed.
- Do not include future app assistant naming.
- Do not include weighted score totals.

Output:
- Unified diff.
- Template usability check.
- Over-engineering check.
```

---

# Prompt 12 — Canonical patch: LEARNING_QUEUE.md

```text
# Patch Alfred LEARNING_QUEUE.md — future improvements only

Target:
- managed/agent_kb/alfred/LEARNING_QUEUE.md

Mission:
Capture future improvement candidates without promoting them to doctrine.

Add future candidates:
1. Full Weekly Rhythm Plan v1.1.
2. Monthly Direction Map operationalization.
3. Low-risk OpState auto-apply classes.
4. Future Algorithm from tracking evidence.
5. Future BP/XP relation.
6. Future mood/energy tracking reconsideration.
7. Pattern library storage structure.
8. Automation of candidate detection.
9. Visualization of Daily Command Board.
10. Calibration of V/U/L/F and P-Class rules from real use.

For each:
- source decision
- current status
- blocker
- promotion condition
- target future file

Output:
- Unified diff.
- Candidate register.
```

---

# Prompt 13 — Source/audit patch: SOURCE_MANIFEST.md and COVERAGE_AUDIT.md

```text
# Patch source and coverage controls

Targets:
- managed/agent_kb/alfred/SOURCE_MANIFEST.md
- managed/agent_kb/alfred/COVERAGE_AUDIT.md

Mission:
Update source/audit controls for the new locked Apex decision files and research inputs.

Rules:
- Preserve old history.
- Add new decision-lock and research inputs.
- Mark what is validated by operator.
- Mark what remains candidate/future.
- Do not imply canonical promotion just because working decision lock exists.
- Separate:
  - accepted operator decisions
  - working locked decisions
  - appendix-level doctrine
  - canonical KB doctrine
  - future learning queue candidates

Must include:
- APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- ALFRED_WORKFLOW_DECISION_LOCK.md
- ALFRED_WORKFLOW_PREFILLED_QA.md
- Variables&Metrics research reports if available in repo or upload context
- AGENT_HANDOFF_CONTRACTS.md relationship
- Informatics Design role

Output:
- Unified diffs.
- Coverage delta table.
- Remaining source gaps.
- Stop before applying unless instructed.
```

---

# Prompt 14 — README patch

```text
# Patch Alfred README.md — index and usage map

Target:
- managed/agent_kb/alfred/README.md

Mission:
Update the Alfred KB folder index after appendices and locked decision integration.

Must include:
1. New appendices and what each is for.
2. Working decision locks and their status.
3. Current canonical files remain primary.
4. Appendices are subordinate operational doctrine.
5. Working locks are non-canonical until promoted.
6. Where to look for:
   - orientation variables
   - Daily Command Board
   - MetaOps handoff
   - Session Export / OpState
   - Tracking
   - Pattern learning
   - Rhythm profile
7. Next recommended action.

Output:
- Unified diff.
- Navigation clarity check.
```

---

# Prompt 15 — High-impact control run: completeness audit

```text
# Control Run — Completeness Audit

Mission:
Audit whether all accepted decisions from:
- ALFRED_WORKFLOW_DECISION_LOCK.md
- APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- validated Q&A
- research synthesis

are represented in:
- new appendices
- canonical Alfred KB patches
- source/audit controls
- README

Create a coverage matrix.

Rows:
- Alfred-only naming
- Leela app boundary
- V/U/L/F orientation
- urgency naming
- removed variables
- confidence modifier
- policy_lane guardrail
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
- no V/U/L/F vs EVD/IMP/RSK collision

Columns:
- decision lock
- appendix
- ESSENCE
- BEST_PRACTICES
- MISTAKES
- TEMPLATES
- LEARNING_QUEUE
- SOURCE_MANIFEST
- COVERAGE_AUDIT
- README

Output:
1. Coverage matrix.
2. Missing integrations.
3. Over-integrated areas.
4. Contradictions.
5. Required fixes.
6. No-write verdict.

Do not patch in this run.
```

---

# Prompt 16 — High-impact control run: simplification / over-engineering audit

```text
# Control Run — Simplification and Over-Engineering Audit

Mission:
Challenge the integration for unnecessary complexity.

Use Informatics Design lens:
- structure
- taxonomy
- naming
- decomposition
- retrieval-safe packaging
- bounded context readability

Audit questions:
1. Are there too many appendices?
2. Are any schemas duplicated across files unnecessarily?
3. Are any fields too detailed for v1?
4. Are any fields better marked future/v1.1?
5. Does Daily Command Board risk becoming a giant dashboard?
6. Does MetaOps handoff over-prescribe MetaOps internals?
7. Are V/U/L/F definitions simple enough for real use?
8. Are hard flags clear enough?
9. Are tracking fields minimal?
10. Are pattern thresholds simple and enforceable?
11. Does the system preserve high impact with low operator burden?
12. Does retrieval become easier or harder?

Output:
1. Simplification verdict.
2. Keep/remove/defer table.
3. Minimal viable v1 set.
4. Deferred v1.1 set.
5. Patch recommendations.
6. Risk of over-compression.
7. Final recommended simplification patch list.

Do not patch until the operator approves.
```

---

# Prompt 17 — High-impact control run: process quality and handoff audit

```text
# Control Run — Process Quality and Handoff Audit

Mission:
Validate that the integrated Alfred/Apex process is high-impact, simple, and interoperable with existing Apex handoff contracts.

Read:
- AGENT_HANDOFF_CONTRACTS.md
- APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
- APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md

Check:
1. Are Alfred → MetaOps handoffs bounded?
2. Do handoffs name source, objective, expected output, constraints, stop condition, and return path?
3. Is the difference between local craft-flow handoff and formal first-wave handoff clear?
4. Are EVD/IMP/RSK preserved where existing process requires them?
5. Is V/U/L/F limited to daily/project orientation?
6. Are target states and authority boundaries clear?
7. Are blocked/operator-review-required states respected?
8. Is candidate/canonical separation preserved?
9. Is OpState protected from trace pollution?
10. Are validator paths clear where risk is high?
11. Is there any hidden truth mutation?
12. Is there any role-boundary drift?

Output:
1. Pass/fail by criterion.
2. Required fixes.
3. Recommended improvements.
4. Explicit no-drift verdict.
5. Patch list if needed.

Do not patch in this run.
```

---

# Prompt 18 — High-impact control run: future improvements capture

```text
# Control Run — Future Improvements Capture

Mission:
Save useful insights without bloating v1.

Inputs:
- all appendices
- canonical patch drafts
- simplification audit
- process/handoff audit
- operator corrections

Create a future-improvements register.

Categories:
1. Algorithm evolution
2. Weekly Rhythm Plan v1.1
3. Monthly Direction Map
4. OpState low-risk auto-apply
5. Pattern library storage and retrieval
6. Tracking analytics
7. BP/XP relationship
8. mood/energy reconsideration
9. Daily Command Board visualization
10. MetaOps workflow automation
11. source/audit automation
12. future Leela productization

For each item:
- insight
- current status
- why not v1
- evidence/source
- target future artifact
- promotion condition
- risk if premature
- expected impact

Output:
1. Future improvements table.
2. Items to add to LEARNING_QUEUE.md.
3. Items to leave out.
4. Items requiring operator decision.
5. No-write recommendation.

Do not patch until approved.
```

---

# Prompt 19 — Final consistency gate

```text
# Final Consistency Gate — Before Canonical Patch Merge

Mission:
Run the final gate before accepting the integration.

Must verify:
1. Alfred-only actor rule holds everywhere.
2. Leela app is not treated as runtime.
3. V/U/L/F and EVD/IMP/RSK are not conflated.
4. Appendices contain detail; canonical files stay compact.
5. Daily Command Board is usable, not bloated.
6. MetaOps handoff is bounded and not over-prescriptive.
7. Session Export remains trace.
8. OpState remains state delta only.
9. Pattern learning remains candidate-first.
10. Tracking remains minimal and excludes mood/energy/BP-XP.
11. Rhythm profile is light and separate.
12. Weekly/monthly planning are not prematurely operationalized.
13. Source/audit controls reflect reality.
14. README navigation is clear.
15. All rejected alternatives remain rejected.

Output:
1. Final pass/fail.
2. Remaining blockers.
3. Safe-to-patch list.
4. Unsafe-to-patch list.
5. Exact next implementation sequence.
6. Operator approval request.

Do not merge or patch without explicit operator approval.
```

---

# Recommended execution order

```text
0  Bootstrap
1  Two-tier metric model
2  Integration architecture map
3  APPENDIX_APEX_ORIENTATION_AND_ROUTING
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

## Implementation principle

Use this rule throughout:

```yaml
integration_rule:
  appendices: operational detail
  canonical_files: compact doctrine
  working_locks: decision evidence
  source_audit_files: provenance and coverage
  learning_queue: future improvements only
  process_files: only patch if contradiction_or_pointer_gap_exists
```