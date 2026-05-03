# Apex AI system description + research prompt

## 1. Immediate simplification recommendation

Your concern is correct: the orientation metrics are useful, but the current metric set can be reduced.

The current draft uses several overlapping dimensions: deadline pressure, strategic value, dependency unlock, readiness, calendar fit, default-lane alignment, risk if deferred, confidence, blockers, and operator decisions. The attached Q&A draft already defines these as part of project packets, visible ranking, MetaOps handoffs, Session Export scaffolds, tracking, and Rhythm logic.

For Apex AI, I recommend reducing this to:

```yaml
apex_orientation_core_v0:
  value: 0-3
  time_pressure: 0-3
  leverage: 0-3
  fit: 0-3
  confidence: low|medium|high
  policy_lane: leela|master_of_arts|wildcard|none
  hard_flags:
    - hard_deadline
    - blocked
    - missing_input
    - operator_decision_needed
    - hygiene_hold
    - calendar_conflict
```

## 2. Reduced variable model

### 2.1 Four core variables

|Variable|Meaning|Absorbs older variables|Practical question|
|---|---|---|---|
|**Value**|How much this matters if completed.|strategic value, project importance, long-term relevance|“Why should this matter?”|
|**Time pressure**|How soon this matters.|deadline pressure, risk if deferred|“Why now?”|
|**Leverage**|What this unlocks or blocks.|dependency unlock, blocker removal, compounding effect|“What does this enable?”|
|**Fit**|Whether it can realistically be done now.|readiness, calendar fit, operator constraint fit, input availability|“Can this actually be acted on today?”|

### 2.2 Control fields

|Field|Role|Why it should not be part of the main score|
|---|---|---|
|**Confidence**|Evidence quality marker.|A high-value task with weak evidence should not look equally trustworthy.|
|**Policy lane**|Standing allocation rule.|Leela/Master/Wildcard lanes are planning policy, not inherent task value.|
|**Hard flags**|Overrides or blockers.|Some conditions should route or block a task before scoring matters.|

### 2.3 Mapping from old variables to reduced model

|Older variable|New placement|
|---|---|
|`strategic_value`|`value`|
|`deadline_pressure`|`time_pressure`|
|`risk_if_deferred`|`time_pressure`|
|`dependency_unlock`|`leverage`|
|`readiness_of_inputs`|`fit`|
|`calendar_fit`|`fit`|
|`operator_constraint_fit`|`fit`|
|`default_lane_alignment`|`policy_lane`|
|`confidence`|`confidence`|
|`blocker`|`hard_flags.blocked`|
|`missing_inputs`|`hard_flags.missing_input`|
|`operator_decision_needed`|`hard_flags.operator_decision_needed`|

### 2.4 Recommended scoring posture

Avoid a fragile formula too early. Use a **classification-first** model:

```yaml
apex_priority_class_v0:
  P0:
    meaning: must_handle_now
    conditions:
      - hard_deadline
      - hygiene_hold
      - blocking_operator_decision
      - severe_calendar_conflict
  P1:
    meaning: should_receive_craft_flow_today
    conditions:
      - high_value_and_high_fit
      - high_time_pressure_and_medium_fit
      - high_leverage_and_ready
  P2:
    meaning: valid_default_lane_work
    conditions:
      - supports_default_lane
      - ready
      - no urgent conflict
  P3:
    meaning: defer_or_backlog
    conditions:
      - low_fit
      - missing_inputs
      - stale_without_delta
      - no_actionable_next_step
```

Then use the four variables only to explain the recommendation:

```yaml
example_orientation:
  project: Leela
  task: "Finalize Daily Command Board schema"
  value: 3
  time_pressure: 2
  leverage: 3
  fit: 3
  confidence: high
  policy_lane: leela
  hard_flags: []
  priority_class: P1
  recommendation: "Assign to Leela craft flow 1"
  reason: "High leverage, ready inputs, default lane alignment, needed before KB hardening."
```

This gives Apex AI a reusable decision logic without turning every workflow into over-engineered scoring.

---

# 3. Apex AI system description

## 3.1 System identity

**Apex AI** is an operator-centered AI operating system for converting bounded work traces, project states, priorities, and planning constraints into coordinated daily execution.

Its purpose is not to “chat about work.” Its purpose is to maintain a controlled operating spine:

```text
Session work
→ Session Export
→ Night synthesis
→ Project packet
→ Alfred Daily Command Board
→ MetaOps execution handoff
→ Craft-flow execution
→ Session Export again
```

The current personal assistant actor in this system is **Alfred only**. The decision-lock explicitly prevents introducing a second current-system personal assistant or treating the future Leela app as the runtime environment.

## 3.2 Core actors

|Actor / system part|Role|Owns|Does not own|
|---|---|---|---|
|**Operator**|Final authority|validation, correction, final priorities, explicit overrides|passive execution of AI plans|
|**Alfred**|Personal executive assistant|Daily Command Board, priority synthesis, craft-flow allocation, personal-context-aware planning, Rhythm-style recommendations|detailed project execution workflows, silent truth mutation|
|**MetaOps**|Project execution architect|sprint workflow, task decomposition, prompt chains, AI routing, execution packages|personal daily priority authority|
|**Night**|Cross-session synthesis process|reads Session Exports, produces next-day packets, detects blockers, proposes improved plans|silent SSOT mutation|
|**Project interface / OpState**|Live project state layer|current project status, next actions, blockers, holds|full session history|
|**Knowledge / KB Ops**|Durable knowledge hardening|pattern promotion, KB placement, doctrine update, audit|unreviewed candidate dumping|
|**Rhythm logic**|Planning reference model|day/week/month placement logic, branch balance, regeneration planning|separate agent in v1|
|**Pattern library**|Candidate learning layer|repeated behavior/workflow/flow/chunk patterns|canonical truth before validation|

## 3.3 Core artifacts

|Artifact|Created by|Consumed by|Purpose|
|---|---|---|---|
|**Session Export**|Operator + Alfred scaffold|Night, OpState, MetaOps, KB Ops|Durable trace of what happened in a session.|
|**Night Plan**|Night process|Alfred, MetaOps|Synthesis of actuals, blockers, next tasks, project packets.|
|**Project Packet**|Night / MetaOps / OpState|Alfred|Compact project input for daily planning.|
|**Daily Command Board**|Alfred|Operator, MetaOps|Morning plan: ranked packets + four craft-flow sessions.|
|**Craft Flow Handoff**|Alfred|MetaOps|Request for executable workflow package.|
|**MetaOps Workflow Package**|MetaOps|Operator, Alfred|Task/sprint/prompt/AI-routing plan for execution.|
|**Tracking Record**|Alfred from board + Session Export|Pattern Library, Rhythm, future Algorithm|Planned vs actual learning signal.|
|**Pattern Candidate**|Alfred / Night|KB Ops|Candidate reusable pattern, not truth.|
|**OpState Delta Candidate**|Alfred / Session Export|Project interface|Live project state update candidate.|

## 3.4 Apex interchange principle

Every interchange between system parts should answer:

```yaml
apex_interchange_minimum:
  identity:
    artifact_id:
    artifact_type:
    project_id:
    created_by:
    target_consumer:
  source_basis:
    source_artifacts: []
    evidence_quality: low|medium|high
  intent:
    objective:
    expected_outputs: []
    decision_needed:
  orientation:
    value: 0-3
    time_pressure: 0-3
    leverage: 0-3
    fit: 0-3
    confidence: low|medium|high
    policy_lane:
    hard_flags: []
  routing:
    requested_action:
    owner_or_next_surface:
    stop_condition:
  state_effect:
    opstate_delta_candidate: true|false
    pattern_candidate: true|false
    kb_candidate: true|false
```

This is the central anti-drift mechanism: each artifact has identity, evidence, intent, orientation, routing, and state effect.

---

# 4. Example: reduced Project Packet

```yaml
project_packet_v1_simplified:
  identity:
    packet_id: PP-2026-05-01-LEELA-01
    project_id: leela
    source_artifacts:
      - night_plan: NP-2026-05-01
      - session_export: SE-LEELA-CF2-2026-04-30
      - opstate: projects/leela/OpState.md
  proposed_work:
    task: "Finalize Alfred Daily Command Board schema"
    expected_outputs:
      - "validated board fields"
      - "MetaOps handoff schema"
      - "tracking hooks"
    next_action: "Run schema validation pass and prepare appendix patch"
  orientation:
    value: 3
    time_pressure: 2
    leverage: 3
    fit: 3
    confidence: high
    policy_lane: leela
    hard_flags: []
    priority_class: P1
  routing:
    recommended_flow: CF1
    requested_metaops_action: "Create sprint workflow and acceptance checklist"
    operator_decision_needed: false
  state_effect:
    opstate_delta_candidate: true
    pattern_candidate: true
    kb_candidate: true
```

---

# 5. Example: reduced visible ranking

Instead of showing seven metrics, Alfred should show:

|Rank|Packet|V|T|L|F|Class|Reason|
|--:|---|--:|--:|--:|--:|---|---|
|1|Leela board schema|3|2|3|3|P1|Unlocks KB hardening; ready now.|
|2|Master of Arts offer work|3|3|2|2|P1|Deadline pressure; needs focused output.|
|3|Wildcard admin cleanup|1|2|1|3|P2|Easy fit but low leverage.|
|4|Deep research task|3|1|3|1|P3|Valuable but not ready; needs inputs.|

Human-readable:

```text
Recommended flow allocation:
CF1: Leela board schema — high leverage, ready, default lane.
CF2: Leela appendix preparation — high value, supports same dependency chain.
CF3: Master of Arts offer work — time pressure.
CF4: Wildcard admin cleanup — good fit, low cognitive load.
```

---

# 6. Research prompt for another AI

Copy/paste the following prompt into a deep research AI.

```text
# Deep Research Prompt — Apex AI Interchange, Handoff, Workflow, and Variable Simplification

## 1. Role

You are a senior AI systems researcher, workflow architect, and organizational design analyst. Your task is to research established practices that can inform the design of Apex AI: an operator-centered AI operating system that coordinates personal planning, project execution, Night synthesis, handoffs, workflow packages, session exports, project state, and pattern learning.

You must research rigorously, cite sources, compare frameworks, and produce a practical architecture recommendation. Do not produce generic productivity advice. Focus on established practices for human-AI workflow orchestration, multi-agent coordination, trace artifacts, project state management, decision handoffs, work planning, and process learning.

## 2. Core context

Apex AI is a system for turning bounded work traces into daily action.

The current loop is:

Session work
→ Session Export
→ Night synthesis
→ Project Packet
→ Alfred Daily Command Board
→ MetaOps Craft Flow Handoff
→ MetaOps Workflow Package
→ Operator executes a Craft Flow
→ Session Export again

Current-system personal assistant actor:
- Alfred

Important naming rule:
- Do not introduce another current-system personal-assistant actor.
- Alfred is the operator-facing assistant in this system.
- Leela is a future app/product and is not the current runtime environment.
- The future Leela app may later productize patterns learned from Alfred, but it must not be treated as active in the Apex AI workflow.

## 3. Main research objective

Research established practices for designing the interchange, handoff, workflow, and decision-variable system for Apex AI.

The goal is to answer:

1. What is the simplest robust variable model for orienting project packets, daily priorities, and workflow handoffs?
2. What handoff artifacts are needed between Alfred, MetaOps, Night, OpState, Knowledge/KB Ops, and the operator?
3. What should each artifact contain to avoid ambiguity, drift, duplicated work, hidden truth mutation, and over-engineering?
4. Which established practices should Apex AI borrow from, adapt, or avoid?
5. How should Apex AI structure traceability, state updates, pattern learning, and human validation?

## 4. Existing Apex concepts

### 4.1 Actors and roles

Operator:
- Final authority.
- Validates, corrects, approves, overrides.
- Supplies reality updates.

Alfred:
- Personal executive assistant.
- Builds Daily Command Board.
- Ranks project packets.
- Allocates four craft-flow sessions.
- Sends handoffs to MetaOps.
- Checks session-outro completeness.
- Maintains pattern candidates.
- Uses Rhythm-style planning logic.

MetaOps:
- Project execution architect.
- Creates sprint workflows, task decomposition, prompt chains, AI routing, execution packages.
- Processes session outputs into next-day project plans.

Night:
- Cross-session synthesis process.
- Reads Session Exports and project state.
- Produces next-day project packets, predicted session scaffolds, blockers, next tasks, and learning candidates.
- Must not silently mutate canonical truth.

Project interface / OpState:
- Live project state surface.
- Contains current state, active work, next actions, blockers, holds.
- Should receive state deltas only, not entire session traces.

Knowledge / KB Ops:
- Hardens pattern candidates into durable knowledge.
- Reviews, promotes, rejects, or archives candidate learning.
- Prevents candidate material from becoming accidental doctrine.

Rhythm logic:
- Planning reference logic for days, weeks, months.
- Helps Alfred place work in time, protect four craft flows, handle calendar conflicts, plan afterwork regeneration, and balance physical/mental/regen branches.
- Not a separate agent in v1.

Pattern Library:
- Candidate layer for repeated useful workflows, planning corrections, chunk combinations, handoff patterns, failure/repair patterns.
- Not canonical truth until validated.

### 4.2 Current unresolved design problem

The current variable model is useful but possibly too detailed.

Old variables include:
- deadline_pressure
- strategic_value
- dependency_unlock
- readiness_of_inputs
- calendar_fit
- default_lane_alignment
- operator_constraint_fit
- risk_if_deferred
- confidence
- blockers
- operator_decision_needed

We want to research whether these can be reduced into a simpler universal model.

Proposed reduced model:

Apex Orientation Core v0:
- value: 0-3
- time_pressure: 0-3
- leverage: 0-3
- fit: 0-3
- confidence: low|medium|high
- policy_lane: leela|master_of_arts|wildcard|none
- hard_flags:
  - hard_deadline
  - blocked
  - missing_input
  - operator_decision_needed
  - hygiene_hold
  - calendar_conflict

Priority classes:
- P0 = must handle now / override / hard blocker
- P1 = should receive craft flow today
- P2 = valid default-lane work
- P3 = defer or backlog

Research whether this model is sound, too simple, too complex, or missing a critical variable.

## 5. Established practice areas to research

Research at least the following domains:

1. Human-in-the-loop AI workflow design
2. Multi-agent orchestration patterns
3. Workflow management and business process modeling
4. Handoff protocols in operations, medicine, aviation, incident response, software teams, and command systems
5. Agile, Scrum, Kanban, and work-in-progress management
6. GTD, PARA, OKR, RICE, ICE, WSJF, Eisenhower Matrix, MoSCoW, and other prioritization frameworks
7. Decision logs, ADRs, postmortems, incident reports, session logs, and audit trails
8. Event sourcing and state transition logs
9. Observability and traceability for AI/tool workflows
10. Knowledge management, promotion workflows, and candidate-to-canonical pipelines
11. Cognitive load and human factors in dashboards, checklists, and handoffs
12. Planning systems for daily/weekly/monthly execution
13. Personal productivity systems that integrate body/mental/work rhythms
14. AI agent memory, reflection, and pattern-learning architectures
15. Data contracts and schema design for inter-agent communication

## 6. Specific research questions

### A. Variable simplification

1. Is the proposed Value / Time Pressure / Leverage / Fit model sufficient?
2. Is there a better established 3-5 variable model?
3. Should confidence be a variable, a modifier, or a display-only field?
4. Should policy lane be part of scoring or a guardrail?
5. Should hard flags short-circuit scoring?
6. Should risk if deferred remain independent or fold into time pressure?
7. Should readiness and calendar fit merge into fit?
8. Should effort be explicit or included in fit?
9. Should priority use numeric scoring, classes, or rules?
10. What is the most robust simple model for AI-human planning?

### B. Artifact design

Evaluate required Apex artifacts:
- Project Packet
- Daily Command Board
- Craft Flow Handoff
- MetaOps Workflow Package
- Expected Session Export Scaffold
- Session Export
- OpState Delta Candidate
- Pattern Candidate
- Night Plan
- Tracking Record
- Weekly Rhythm Plan
- Monthly Direction Map

For each artifact, research:
1. What is the minimum viable field set?
2. What fields cause unnecessary friction?
3. What fields prevent drift?
4. Which fields should be mandatory, optional, or derived?
5. What should never appear in this artifact?
6. What is the best lifecycle?
7. What is the best owner/consumer model?

### C. Handoff quality

Research established best practices for handoffs:
1. What does a good handoff include?
2. What causes handoff failure?
3. How should handoffs represent intent, constraints, state, evidence, and stop condition?
4. How should handoffs separate action from truth mutation?
5. How much source context should be included?
6. When should a handoff ask for a decision rather than assign work?
7. How should handoffs handle blockers and unknowns?
8. What validation checklist should Apex use for every handoff?

### D. Session trace and state

Research:
1. Difference between trace artifact and truth/state artifact.
2. How to prevent session logs from becoming accidental source of truth.
3. How to update live project state from session exports.
4. How to design OpState delta candidates.
5. How much detail belongs in Session Export versus OpState.
6. How to avoid forcing humans to write too much after a session.
7. How to design prefilled session-export scaffolds.

### E. Pattern learning

Research:
1. How AI systems should learn from repeated workflows without silently mutating doctrine.
2. How candidate patterns should be detected.
3. What evidence threshold should promote a pattern.
4. How rejected patterns should be archived.
5. How pattern libraries should support future productization.
6. How to avoid overfitting to early behavior.

### F. Daily/weekly/monthly planning

Research:
1. How to structure a daily command board.
2. How many visible metrics are optimal for a human operator.
3. How to represent four planned work sessions.
4. How to plan around hard calendar locks.
5. How to handle afterwork regeneration without confusing it with work sessions.
6. How to roll daily tracking into weekly planning.
7. How to make monthly planning directional rather than over-scheduled.

## 7. Apex artifact examples to evaluate

### 7.1 Project Packet v1 simplified

project_packet_v1:
  identity:
    packet_id:
    project_id:
    source_artifacts: []
  proposed_work:
    task:
    expected_outputs: []
    next_action:
  orientation:
    value: 0-3
    time_pressure: 0-3
    leverage: 0-3
    fit: 0-3
    confidence: low|medium|high
    policy_lane:
    hard_flags: []
    priority_class: P0|P1|P2|P3
  routing:
    recommended_flow:
    requested_metaops_action:
    operator_decision_needed:
  state_effect:
    opstate_delta_candidate: true|false
    pattern_candidate: true|false
    kb_candidate: true|false

Evaluate:
- Is this sufficient?
- What should be mandatory?
- What should be optional?
- What should be renamed?
- What established practice supports or contradicts it?

### 7.2 Daily Command Board v0

daily_command_board_v0:
  date:
  generated_at:
  source_window:
  calendar_reality:
    hard_locks: []
    available_work_windows: []
  incoming_project_packets: []
  daily_priority_stack: []
  craft_flows:
    - flow_id: CF1|CF2|CF3|CF4
      lane: leela_1|leela_2|master_of_arts|wildcard
      time_window:
      project:
      objective:
      expected_outputs: []
      craft_template: Sprint Alex
      physical_chunk:
      mental_chunk:
      break_or_regen_chunk:
      metaops_handoff_needed:
      operator_decision_needed:
  deferred_or_not_today: []
  risks_and_repairs: []

Evaluate this board for:
- cognitive load
- decision clarity
- traceability
- editing ease
- handoff quality
- daily usability

### 7.3 MetaOps Craft Flow Handoff v0

metaops_craft_flow_handoff_v0:
  handoff_id:
  flow_id:
  project_id:
  target_output:
  expected_outputs: []
  priority_reason:
  source_artifacts: []
  constraints:
    time_container_min: 120
    sprint_template: Sprint Alex
    must_use: []
    must_avoid: []
  requested_metaops_outputs:
    - sprint_workflow
    - prompt_chain
    - task_sequence
    - AI_routing_plan
    - acceptance_criteria
    - final_session_export_expectation
  stop_condition:
  return_to: Alfred

Evaluate:
- Is this too much?
- What should MetaOps absolutely need?
- What should be moved to context?
- What should be a checklist?
- What should be machine-readable?

### 7.4 Session Export Scaffold v0

expected_session_export_scaffold_v0:
  metadata:
    project_id:
    flow_id:
    session_id:
    generated_by: Night
    reviewed_by: Alfred
    source_night_plan:
  expected:
    objective:
    planned_outputs: []
    planned_sprints: []
    anticipated_next_tasks: []
    anticipated_blockers: []
  operator_corrections:
    actual_outputs: []
    sprints_completed:
    deviations:
    blockers_found: []
    next_highest_impact_tasks: []
    priority_changes: []
    artifacts_created: []
  learning:
    process_worked:
    chat_or_prompt_flow_efficiency:
    pattern_candidates: []
    chunk_candidates: []
    kb_candidates: []
  downstream:
    metaops_processing_needed:
    opstate_update_candidate:
    night_plan_input:
    promotion_candidate:

Evaluate:
- How to minimize operator burden?
- What is best as checkbox versus free text?
- What should be inferred by Alfred?
- What should be mandatory for audit?
- What should not enter OpState?

### 7.5 Tracking Record v1

tracking_record_v1:
  identity:
    date:
    flow_id:
    lane:
    project_id:
    session_export_id:
  planned:
    objective:
    outputs: []
    time_window:
    craft_template:
    physical_chunk:
    mental_chunk:
    metaops_workflow_id:
  actual:
    flow_completion:
    sprints_completed:
    outputs: []
    next_highest_impact_tasks: []
    blockers: []
    deviation_reason:
  process_learning:
    process_worked:
    chat_flow_efficiency:
    useful_prompt_or_workflow:
    failed_prompt_or_workflow:
  candidates:
    pattern_candidates: []
    chunk_candidates: []
    kb_candidates:
  excluded_v1:
    mood: not_tracked
    energy: not_tracked
    bp_xp: not_authoritative

Evaluate:
- Is this minimum viable tracking?
- What can be automated?
- What should be operator-entered?
- What should become weekly rollup?
- What fields should be removed?

## 8. Expected final deliverables

Produce a structured research report with these sections:

1. Executive summary
2. Recommended Apex variable model
3. Comparison of prioritization frameworks
4. Recommended artifact taxonomy
5. Handoff best practices and Apex-specific checklist
6. Session trace vs live state recommendations
7. Pattern learning and candidate promotion model
8. Daily/weekly/monthly planning recommendations
9. Recommended schemas for each Apex artifact
10. What to remove or simplify from the current design
11. Risks and anti-patterns
12. Implementation roadmap:
    - v0
    - v1
    - v1.1
    - later
13. Open questions requiring operator decision
14. Source bibliography with links and citations

## 9. Research quality requirements

- Use citations for all external frameworks and best-practice claims.
- Separate established practice from your own synthesis.
- Do not overfit one framework.
- Compare at least five prioritization approaches.
- Compare at least five handoff/trace/state practices.
- Explicitly state what not to use.
- Prefer simple robust systems over complex scoring.
- Include concrete schemas.
- Include example artifacts.
- Include failure modes.
- Include decision rules.
- Identify which parts should be machine-readable and which should be human-readable.
- Use must/should/may language.
- Avoid ambiguous terms like “important,” “soon,” or “ready” without definitions.

## 10. Anti-drift constraints

Do not:
- Introduce a second current-system assistant besides Alfred.
- Treat Leela app as current runtime.
- Make Night a silent truth mutator.
- Put full session trace into OpState.
- Turn every artifact into a prose essay.
- Create scoring complexity that the operator will ignore.
- Treat candidate pattern learning as canonical truth.
- Optimize for automation before operator correction is reliable.
```

---

# 7. Recommended answer to your metric concern

Use this as the next Apex standard unless research disproves it:

```yaml
apex_orientation_core_v1_candidate:
  core_scores:
    value: 0-3
    time_pressure: 0-3
    leverage: 0-3
    fit: 0-3
  controls:
    confidence: low|medium|high
    policy_lane: leela|master_of_arts|wildcard|none
  hard_flags:
    - hard_deadline
    - blocked
    - missing_input
    - operator_decision_needed
    - hygiene_hold
    - calendar_conflict
  output:
    priority_class: P0|P1|P2|P3
    recommended_route:
    visible_reason:
    operator_decision_needed:
```

This is simpler, more reusable, and less brittle than keeping every original metric as a top-level score.