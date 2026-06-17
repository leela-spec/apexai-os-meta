# 1. Source Scan Summary

**Inspected source indexes**

- `SourceIndexAgentInteraction07OC.md` — OpenCLAW / OpenClaw `07_finalopenclawsystem` workflow index. It points primarily to `managed/processes`, `managed/rules`, `managed/rituals`, `managed/knowledge`, and selected promptflow / working artifacts.
- `SourceIndexAgentInteractionAlfred.md` — APEX AI / Alfred workflow index. It points to Alfred KB-build flows, validation flows, Daily Command Board, handoffs, variables, metrics, night loop, session export, and pattern-learning materials.

**Primary source areas treated as authoritative**

- **OpenCLAW:** `managed/processes`, `managed/rules`, `managed/rituals`, `managed/knowledge`, `managed/agents`, and `managed/agent_kb`.
- **Alfred:** `CreatingAlfred/*` and especially `INtegratingLeelaSequencing/*`.

**Excluded / deprioritized**

- OpenCLAW `special_ops` as final implementation architecture where superseded by Hermes, but **kept as source for workflow logic**.
- Knowledge-base architecture as final architecture, but **kept as promotion / learning / governance source**.
- Empty or purely historical Alfred files unless they contained reusable workflow logic.

**Uncertainty**

- I could access index files and repo-search snippets. Some repo file bodies were only partially exposed by search, so the catalogue below is an extraction-oriented first pass, not a canonical final implementation.

---

# 2. Extracted Agent / Role Catalogue

The OpenCLAW `AGENT_INDEX` is explicitly the activation and routing entry point for the first-wave compact agent seed set, and its read order points to base rules, operating spine, swarm interaction canon, promotion protocol, KB index, holding flow, handoff contracts, overlap validation, and cross-reference manifest. The same index keeps seed files compact while putting rich doctrine into `managed/agent_kb`, with `LEARNING_QUEUE.md` explicitly candidate-only rather than runtime truth.

|Agent / Role|Source System|Core Function|Inputs|Outputs|Tools / Capabilities|Interacts With|Hermes Translation Candidate|
|---|---|---|---|---|---|---|---|
|**Alfred / Operator Assistant**|Alfred + OpenCLAW|Front-door personal assistant; intake, alignment, routing, operator support|User request, project state, constraints, daily context|Clarified request, route decision, board/session packet|Conversation, project context, routing matrix|Operator, Meta Ops, Meta Strategy, Meta Detective|`Hermes Profile`, `Kanban Assignee`, `Memory/Context File`|
|**Holding Orchestrator**|OpenCLAW|Bounded activation; decides smallest agent set needed|Intake packet, task class, risk/impact/evidence|Activation plan, agent set, validation band|Routing, thresholds, validation logic|Alfred, Meta Ops, validators|`Hermes Profile`, `Hermes Skill`, `Kanban Assignee`|
|**Workflow Router**|OpenCLAW + Alfred|Chooses keep-local vs delegate vs board vs cron|Task type, urgency, dependencies, risk|Route recommendation|Routing matrix, role boundaries|Alfred, Orchestrator, Meta Ops|`Hermes Skill`, `Delegated Subagent`|
|**Project Router**|OpenCLAW|Routes work to correct project/interface|Project packet, current state, next action|Project-specific work packet|Project interface contract, OpState|Alfred, Operator, Night Planner|`Hermes Skill`, `Memory/Context File`|
|**Meta Ops**|OpenCLAW|Execution coordination, task sequencing, bounded delivery|Routed task, acceptance criteria, constraints|Execution plan, task breakdown, handoff|Planning, task management, executor coordination|Alfred, Prompt/Workflow Ops, Detective|`Hermes Profile`, `Kanban Assignee`|
|**Meta Strategy**|OpenCLAW|Options, timing, leverage, recommendation|Strategic question, decision context, options requested|Scenarios, recommendation, tradeoffs|Strategic analysis, prioritization|Alfred, Meta Detective|`Hermes Profile`, `Delegated Subagent`|
|**Meta Detective**|OpenCLAW|Adversarial validation, drift detection, plausibility pressure, escalation pressure|Output, assumptions, source claims, handoff packet|Pass/fail/revise/hold/escalate verdict|QA, contradiction search, risk review|Meta Strategy, Meta Ops, Hygiene Clean|`Hermes Profile`, `Delegated Subagent`, `Kanban Assignee`|
|**QA / Hygiene Clean**|OpenCLAW|QA findings, structural correctness, pointer integrity, cleanup safety|Candidate files, diffs, KB pointers, workflow outputs|Hygiene report, cleanup patchspec, fail/hold signal|Structural QA, pointer checks, cleanup safety|Meta Detective, KB Ops, Informatics|`Hermes Skill`, `Delegated Subagent`, `Kanban Assignee`|
|**Knowledge Bank Ops**|OpenCLAW|KB placement, lifecycle, manifest, source routing|Candidate learning, source material, promotion request|KB placement decision, promotion packet|Source routing, manifest logic, canon/candidate split|Informatics Design, Meta Detective|`Hermes Skill`, `Memory/Context File`, `Cron Worker`|
|**Informatics Design**|OpenCLAW|Structure, terminology, readability, taxonomy|KB structure, naming, folder surfaces|Taxonomy / structure recommendation|Information architecture|KB Ops, Hygiene Clean|`Hermes Skill`, `Delegated Subagent`|
|**Prompt / Workflow Ops**|OpenCLAW|Reusable prompt, workflow, and patchspec patterns|Task flow, repeated prompt pattern, execution failure|Promptflow, patchspec, workflow template|Prompt design, workflow abstraction|Meta Ops|`Hermes Skill`, `Delegated Subagent`|
|**AI Handling / Routing Advisor**|OpenCLAW|Model/tool/capability fit and fallback posture|Task, available tools/models, risk profile|Advisory routing recommendation|Model/tool routing|Meta Ops, Operator|`Hermes Skill`|
|**Deep Researcher**|OpenCLAW implied|Source-aligned deep research before patchspec|Research question, source map, scope lock|Findings, evidence map, patch implications|Web/repo research, source comparison|Patchspec Writer, Detective|`Delegated Subagent`, `Hermes Skill`|
|**Patchspec Writer**|OpenCLAW|Turns research into safe implementation spec|Research packet, target files, constraints|Patchspec, diff safety notes, executor instructions|Diff planning, acceptance criteria|Executor, QA, Detective|`Hermes Skill`, `Delegated Subagent`|
|**Executor / Implementer**|OpenCLAW + Alfred|Applies bounded task or patch|Patchspec, exact target files, acceptance criteria|Changed files, execution report|Terminal/file/code tools|Meta Ops, QA, Codex executor|`Kanban Assignee`, `Delegated Subagent`|
|**No-Drift Validator**|Alfred|Read-only validation of patched branch correctness|Diff, target spec, source basis|Validation report, drift findings|Diff audit, no-write mode|Executor, Meta Detective|`Hermes Skill`, `Delegated Subagent`|
|**Session Export Agent**|OpenCLAW + Alfred|End-of-session trace capture|Session actions, findings, decisions, next steps|Session export / OpState delta|Summarization, state extraction|Night Planner, Knowledge Ops|`Hermes Skill`, `Cron Worker`|
|**Night Planner**|OpenCLAW + Alfred|Cross-session synthesis and next-day packet creation|Session exports, project state, hygiene findings, promotion queue|Next-day plan, pre-planned sessions, blockers|Planning, synthesis, prioritization|Alfred, Operator, Daily Board|`Cron Worker`, `Hermes Profile`|
|**Daily Command Board Builder**|Alfred|Creates daily actionable project board|Night plan, active projects, priority variables|Daily board, project packets, flow assignments|Scheduling, priority scoring|Operator, Alfred, Night Planner|`Cron Worker`, `Hermes Skill`, `Kanban Routine`|
|**Morning Review Assistant**|Alfred|Lets operator adjust the board|Daily board, constraints, human edits|Confirmed execution plan|Interactive review|Operator, Alfred|`Hermes Profile`, `Hermes Skill`|
|**Craft Flow Planner**|Alfred|Maps work into craft/session flows|Daily board, flow IDs, time windows, target outputs|Flow handoff packet|Sequencing, task shaping|Operator, Session Agent|`Hermes Skill`, `Kanban Routine`|
|**Pattern Learning Agent**|Alfred|Detects repeated workflows, behavior patterns, routing patterns|Session exports, metrics, repeated events|Candidate patterns, skill candidates|Pattern mining, candidate queue|Knowledge Ops, Curator|`Cron Worker`, `Memory/Context File`|
|**Metrics / Variables Tracker**|Alfred|Tracks deadline pressure, strategic value, dependency unlock, energy/friction, etc.|Session/project data|Visible metrics, routing variables|Scoring, trend capture|Daily Board, Night Planner|`Memory/Context File`, `Hermes Skill`|
|**Handoff Packet Builder**|OpenCLAW + Alfred|Creates structured handoff packets|Objective, current state, inputs, risk, expected outputs|Handoff packet|Schema enforcement|All role pairs|`Hermes Skill`|
|**Escalation Gatekeeper**|OpenCLAW|Holds/rejects/escalates unsafe or ambiguous tasks|Handoff packet, authority ambiguity, source gap|Hold/reject/escalate decision|Stop-condition logic|Meta Detective, Operator|`Hermes Skill`, `Hermes Profile`|
|**Promotion Reviewer**|OpenCLAW|Promotes candidate learning into accepted truth/process|Candidate, evidence, validator verdict|Promotion / rejection / archive record|Promotion protocol, ledger|KB Ops, Meta Detective, Operator|`Hermes Skill`, `Kanban Assignee`|
|**Skill Curator**|Hermes target|Reviews, patches, consolidates, archives reusable skills|Skill usage, task outcomes, stale skills|Active/stale/archived/pinned decisions|Skill lifecycle management|Pattern Learning, KB Ops|`Cron Worker`, `Hermes Skill`|
|**Kanban Orchestrator**|Hermes target|Decomposes requests into cards and routes to profiles|Goal, available profiles, dependency graph|Kanban task graph|Board creation, dependency linking|Profiles, Dispatcher, Operator|`Hermes Profile`, `Kanban Routine`|
|**Kanban Worker**|Hermes target|Executes assigned board card|Kanban card, attached skill/context|Card result, heartbeat, block/done status|Profile-specific tools|Kanban Orchestrator|`Kanban Assignee`|
|**Cron Worker**|Hermes target|Runs recurring isolated workflows|Schedule, self-contained prompt, workdir/context|Scheduled outputs, reports, updates|Cron execution|Alfred, Night Planner, Curator|`Cron Worker`|

Additional role grounding: the agent index explicitly lists `meta_strategy`, `meta_detective`, `special_ops__knowledge_bank`, `special_ops__informatics_design`, and `special_ops__prompts_workflows` with their core roles and validators. It also lists `special_ops__hygiene_clean` as responsible for QA findings, structural correctness, pointer integrity, and cleanup safety. Alfred’s validated routing practice says to route execution coordination to `meta_ops`, options/scenarios to `meta_strategy`, adversarial review to `meta_detective`, reusable workflow shape to `special_ops__prompts_workflows`, and KB/source-canon separation to `special_ops__knowledge_bank`.

---

# 3. Agent Interaction Map

```
bounded_intake_and_activation:  purpose: >    Convert a broad user request into the smallest bounded agent/profile set    that can do the job legibly.  participating_agents:    - Alfred / Operator Assistant    - Holding Orchestrator    - Workflow Router    - Meta Ops    - Meta Strategy    - Meta Detective  trigger: new user request; broad, multi-owner, high-stakes, or ambiguous task  input_packet:    objective:    project_context:    current_state:    constraints:    evidence_level:    impact_level:    risk_level:  sequence:    - step: 1      acting_agent: Alfred      action: clarify task enough to determine whether it is local, delegated, board-based, or cron-worthy      output: normalized intake packet    - step: 2      acting_agent: Workflow Router      action: classify task by execution, strategy, validation, workflow design, or KB placement      output: route recommendation    - step: 3      acting_agent: Holding Orchestrator      action: choose smallest bounded activation set      output: activation set    - step: 4      acting_agent: Target specialist      action: accept, reject, request revision, hold, or escalate      output: receiver disposition  validation_gate: Meta Detective or role-specific validator checks evidence/risk/authority  final_output: bounded task graph or direct local answer  likely_hermes_mechanism:    - Hermes Skill    - Hermes Profile    - Delegated Subagent    - Kanban Routine
```

```
structured_agent_handoff:  purpose: >    Transfer bounded work between agents without role drift, authority ambiguity,    or context loss.  participating_agents:    - Sender Agent    - Receiver Agent    - Validator Agent    - Escalation Gatekeeper  trigger: task exceeds current agent lane or requires another specialist  input_packet:    objective:    current_state:    inputs:    evidence_refs:    expected_outputs:    acceptance_criteria:    evd_imp_rsk:    stop_conditions:  sequence:    - step: 1      acting_agent: Sender Agent      action: build handoff packet      output: structured transfer request    - step: 2      acting_agent: Receiver Agent      action: decide accept/reject/revise/hold/escalate      output: receiver disposition    - step: 3      acting_agent: Validator Agent      action: check risk, evidence, authority, and role fit      output: validation note    - step: 4      acting_agent: Receiver Agent      action: execute only within accepted scope      output: bounded output  validation_gate: valid receiver disposition plus evidence/risk review  final_output: accepted output, rejection, hold, or escalation  likely_hermes_mechanism:    - Hermes Skill    - Delegated Subagent    - Kanban dependency
```

The handoff-contract source describes a structured protocol for bounded task transfer, authority transparency, validation, and risk management, with fields such as `objective`, `current_state`, `inputs`, `expected_outputs`, and `EVD`/`IMP`/`RSK`. It also says receivers should reject handoffs outside their lane, lacking context, conflicting with role boundaries, requiring forbidden authority, or forcing unsafe implementation; stop conditions outrank momentum.

```
deep_research_to_patchspec:  purpose: turn source-grounded research into executable implementation instructions  participating_agents:    - Deep Researcher    - Patchspec Writer    - Meta Detective    - Executor    - No-Drift Validator  trigger: code/system change requires source alignment or high precision  input_packet:    research_question:    target_files:    source_authority_order:    scope_lock:    constraints:  sequence:    - step: 1      acting_agent: Deep Researcher      action: lock scope and inspect authoritative sources      output: source-aligned findings    - step: 2      acting_agent: Patchspec Writer      action: translate findings into target-locked patchspec      output: patch plan, diff safety notes, acceptance tests    - step: 3      acting_agent: Meta Detective      action: adversarially review assumptions and drift risk      output: validation verdict    - step: 4      acting_agent: Executor      action: apply bounded patch      output: changed files and execution report    - step: 5      acting_agent: No-Drift Validator      action: verify patch against source and acceptance criteria      output: pass/fail/revise verdict  validation_gate: no-drift validation before acceptance  final_output: validated patch or revise packet  likely_hermes_mechanism:    - Hermes Skill    - Kanban task chain    - Delegated Subagents
```

```
session_export_to_night_plan:  purpose: convert day execution into next-day prepared work packets  participating_agents:    - Operator    - Session Export Agent    - Night Planner    - Daily Command Board Builder    - Pattern Learning Agent  trigger: end of working session or scheduled night loop  input_packet:    session_summary:    decisions:    artifacts_changed:    blockers:    next_actions:    workflow_feedback:  sequence:    - step: 1      acting_agent: Session Export Agent      action: extract operative delta, findings, next actions, promotion candidates      output: session export    - step: 2      acting_agent: Night Planner      action: synthesize exports, project state, hygiene findings, and promotion queue      output: next-day session packets    - step: 3      acting_agent: Pattern Learning Agent      action: detect repeated patterns and candidate skills      output: learning candidates    - step: 4      acting_agent: Daily Command Board Builder      action: create editable morning board      output: daily command board  validation_gate: board must expose assumptions, blockers, and editable operator fields  final_output: daily board + prepared project packets  likely_hermes_mechanism:    - Cron Worker    - Hermes Skill    - Memory/Context File    - Kanban Routine
```

Alfred’s source index identifies `ChatsoFar.md` as covering Alfred/Sid correction, craft flows, night loop, rhythm logic, pattern tracking, and next prompt sequence; it classifies this as Alfred operating loop, craft-flow routine, night planning/session export loop, and pattern-learning workflow. The Alfred variables/metrics material defines system roles including **Night** as a cross-session synthesis process that reads Session Exports, produces next-day packets, detects blockers, and proposes improved plans.

```
daily_command_board_morning_review:  purpose: produce and human-adjust the day execution plan  participating_agents:    - Night Planner    - Daily Command Board Builder    - Alfred    - Operator    - Craft Flow Planner  trigger: morning review or daily cron output  input_packet:    previous_night_plan:    active_projects:    available_time:    operator_energy:    constraints:  sequence:    - step: 1      acting_agent: Daily Command Board Builder      action: assemble project packets, priorities, flows, constraints      output: draft board    - step: 2      acting_agent: Operator      action: edit priority order, flow assignment, time windows, target outputs, chunk choices, constraints, deferred items, override notes      output: confirmed board    - step: 3      acting_agent: Alfred      action: convert selected board item into craft/session flow      output: session-start packet  validation_gate: operator editability and explicit override notes  final_output: confirmed daily board and first execution packet  likely_hermes_mechanism:    - Cron Worker    - Hermes Profile    - Hermes Skill
```

Alfred handoff/variables material explicitly says the operator can edit priority order, flow assignment, time windows, target outputs, chunk choices, constraints, deferred items, and override notes during morning review.

```
candidate_learning_to_promotion:  purpose: prevent raw learning from becoming doctrine without review  participating_agents:    - Pattern Learning Agent    - Knowledge Bank Ops    - Promotion Reviewer    - Meta Detective    - Skill Curator  trigger: repeated pattern, workflow improvement, new source-backed rule, discovered mistake  input_packet:    candidate_learning:    evidence_refs:    source_class:    affected_skill_or_kb:    risk_level:  sequence:    - step: 1      acting_agent: Pattern Learning Agent      action: stage learning as candidate-only      output: learning queue entry    - step: 2      acting_agent: Knowledge Bank Ops      action: decide placement and source/canon separation      output: placement recommendation    - step: 3      acting_agent: Meta Detective      action: validate evidence, conflict, and self-promotion risk      output: promotion verdict    - step: 4      acting_agent: Skill Curator      action: patch, pin, archive, or keep related skills      output: updated skill/KB state  validation_gate: no self-promotion; source material remains evidence until promoted  final_output: promoted rule/skill, rejected candidate, or archived learning  likely_hermes_mechanism:    - Hermes Skill    - Cron Worker    - Memory/Context File    - Kanban Review Card
```

The indexed governance rules emphasize that every KB root uses the five-file scaffold, `LEARNING_QUEUE.md` is candidate-only, source material is evidence rather than canon, and self-promotion is forbidden. The KB lanes source distinguishes per-agent KB roots from shared governance and process contract surfaces, and states that accepted files are usable on demand while queues are not truth.

```
kanban_swarm_decomposition:  purpose: durable decomposition of multi-agent work across profiles  participating_agents:    - Kanban Orchestrator    - Specialist Profiles    - Verifier    - Synthesizer    - Operator  trigger: multi-specialist task, restart-safe task, human-in-loop task, audit-trail task  input_packet:    goal:    available_profiles:    lanes:    dependencies:    acceptance_criteria:  sequence:    - step: 1      acting_agent: Kanban Orchestrator      action: discover actual profiles and avoid invented assignees      output: profile roster    - step: 2      acting_agent: Kanban Orchestrator      action: split lanes, map each lane to a real assignee, define dependencies      output: task graph    - step: 3      acting_agent: Kanban Orchestrator      action: create parallel and dependent cards      output: board cards    - step: 4      acting_agent: Worker Profiles      action: execute assigned cards and report done/blocked      output: worker outputs    - step: 5      acting_agent: Verifier / Synthesizer      action: validate and synthesize final result      output: final report  validation_gate: explicit dependencies and verifier card  final_output: durable multi-agent board outcome  likely_hermes_mechanism:    - Kanban Routine    - Hermes Profile    - Kanban Assignee
```

---

# 4. Concrete Workflow Catalogue

## A. OpenCLAW-derived workflows

|#|Workflow|Task Trigger|Agent Chain|Core Output|Later Hermes Form|
|---|---|---|---|---|---|
|1|**Bounded Intake**|New broad task|Alfred → Router → Orchestrator|Normalized intake packet|Skill + Profile|
|2|**Keep-Local vs Delegate Routing**|Task might be simple or multi-agent|Alfred → Router|Local/delegate/board decision|Routing Skill|
|3|**Holding Activation Flow**|Multi-agent task|Orchestrator → specialists|Smallest activation set|Orchestrator Profile|
|4|**Structured Handoff**|Agent lane boundary reached|Sender → Receiver → Validator|Handoff packet|Handoff Skill|
|5|**Receiver Disposition**|Handoff arrives|Receiver → Validator|Accept/reject/revise/hold/escalate|Skill + Kanban status|
|6|**Validation Banding**|Risk/impact/evidence scoring needed|Router → Detective|Low/material/high-control posture|QA Skill|
|7|**Deep Research to Patchspec**|Source-grounded implementation needed|Researcher → Patchspec Writer → Executor|Patchspec|Skill + Kanban chain|
|8|**Executor Handoff**|Patchspec ready|Patchspec Writer → Executor|Target-locked execution task|Kanban card|
|9|**No-Drift Diff Validation**|Patch applied|Executor → Validator|Pass/fail report|Validation Skill|
|10|**Bootstrap Ritual**|New session/system start|Bootstrap Agent|Environment and governing-file check|Startup Skill|
|11|**Recurring Checklist**|Periodic maintenance|Checklist Agent → QA|Foundation/safety/interface checks|Cron Worker|
|12|**Heartbeat Maintenance**|Ongoing continuity check|Heartbeat → Memory/KBOps|Continuity and maintenance signals|Cron Worker|
|13|**Session Export**|End of session|Session Export Agent|Operative delta, findings, next actions|Skill + Cron|
|14|**Night Planning**|End of day|Night Planner|Next-day packets and plans|Cron Worker|
|15|**Promotion Protocol**|Candidate truth/process change|KBOps → Detective → Reviewer|Promotion/rejection record|Skill + Review Card|
|16|**QA Hygiene Protocol**|Structural or content risk|Hygiene Clean → Detective|QA findings, closure rules|QA Skill|
|17|**Project Interface Entry**|Project-specific work starts|Project Router → Project Interface|State/interface/truth separation|Context File + Skill|
|18|**KB Placement Workflow**|New reusable knowledge|KBOps → Informatics → Detective|Correct KB lane/placement|Skill|
|19|**Source Routing Workflow**|Multiple sources conflict|KBOps → Detective|Authority-order decision|Skill|
|20|**KB Promotion Ledger**|Candidate accepted/rejected|Promotion Reviewer|Ledger entry|Memory/Context File|
|21|**Promptflow Base Build**|Need new prompt/workflow KB|Prompt/Workflow Ops|Scaffold + appendices + quality gates|Skill|
|22|**Constant-Frame Integration**|High precision KB integration|Prompt/Workflow Ops → Validator|Atomic frame, gate check, HALT/CLARIFY|Skill|
|23|**Clean Handoff Template**|Any cross-agent task|Sender|Handoff in accepted shape|Skill|
|24|**Watchdog QA/Hygiene**|Drift or stale state suspected|Detective → Hygiene|Watchdog report|Cron + QA Skill|
|25|**Overlap Validation**|Role boundaries blur|Detective → Governance|Required cross-check / stop condition|Skill|

## B. Alfred-derived workflows

| #   | Workflow                                     | Task Trigger                                | Agent Chain                   | Core Output                             | Later Hermes Form   |
| --- | -------------------------------------------- | ------------------------------------------- | ----------------------------- | --------------------------------------- | ------------------- |
| 26  | **Alfred KB Build**                          | Build/rebuild Alfred KB from sources        | KB Builder → Validator        | One agent KB scaffold                   | Skill               |
| 27  | **KB Consolidation**                         | Recovery files need merging                 | KB Builder → KBOps            | Canonical five-file scaffold            | Skill               |
| 28  | **Extended KB Audit**                        | Duplicate/appendix/redirect decision needed | Auditor → KBOps               | Keep/redirect/delete/appendix decisions | Skill               |
| 29  | **Scaffold Integration**                     | Templates/routing/metrics cleanup           | KBOps → Informatics           | Integrated scaffold without duplicates  | Skill               |
| 30  | **Read-Only Validation Prompt**              | Patched branch must be checked              | Validator                     | No-drift validation report              | Delegated Subagent  |
| 31  | **Daily Command Board Generation**           | Start of day                                | Night Planner → Board Builder | Daily board                             | Cron + Skill        |
| 32  | **Morning Board Review**                     | Operator begins day                         | Alfred ↔ Operator             | Edited daily board                      | Profile + Skill     |
| 33  | **Craft Flow Handoff**                       | Operator selects session                    | Alfred → Craft Flow Planner   | Session-start handoff                   | Skill               |
| 34  | **Four-Flow Day Assignment**                 | Day planning                                | Board Builder → Operator      | Flow ID / lane allocation               | Skill               |
| 35  | **Priority Metrics Capture**                 | Board/session planning                      | Metrics Tracker               | Visible priority metrics                | Memory File + Skill |
| 36  | **Session Export / OpState Tracking**        | End of focused work                         | Session Export Agent          | State delta + next actions              | Skill               |
| 37  | **Night Loop Synthesis**                     | Night cron                                  | Night Planner                 | Next-day session packets                | Cron                |
| 38  | **Pattern Learning**                         | Repeated behavior detected                  | Pattern Agent → KBOps         | Candidate patterns                      | Cron + Curator      |
| 39  | **Handoff Variable Capture**                 | Any inter-agent transfer                    | Handoff Builder               | Handoff variables record                | Skill               |
| 40  | **Chat Continuation / Handover**             | New chat after prior work                   | Alfred                        | Continuation packet                     | Context File        |
| 41  | **Codex Diff Application**                   | Target-locked unified diff needed           | Codex Executor → Validator    | Applied diff + validation               | Kanban Worker       |
| 42  | **Source-Authority Validation**              | Patch/source mismatch suspected             | Validator → Detective         | Source authority verdict                | Skill               |
| 43  | **Routing Architecture / State-Delta-Trace** | Workflow design task                        | Router → Metrics Tracker      | Routing + state delta model             | Skill               |
| 44  | **Leela Sequencing Support**                 | Leela project day/workflow planning         | Alfred → Board Builder        | Sequenced project packets               | Skill               |
| 45  | **Operator Feedback Capture**                | Session recap includes what worked/failed   | Alfred → Pattern Agent        | Workflow improvement candidates         | Memory + Curator    |

Alfred’s `HandoffsFormats&Variables.md` is summarized as defining operational templates and tracking schemas for the Alfred assistant, including project packet inclusion criteria, session export scaffolds, priority metrics, craft-flow display formats, and operator interaction protocols. It also defines visible priority metrics including `deadline_pressure`, `strategic_value`, and `dependency_unlock`.

---

# 5. Hermes Translation Map

|Source Pattern|Translate as Hermes Profile|Translate as Hermes Skill|Translate as Delegated Subagent|Translate as Kanban Routine|Translate as Cron Routine|Translate as Memory/Context|
|---|---|---|---|---|---|---|
|Alfred personal assistant|yes|supporting skills|sometimes|yes|no|yes|
|Holding Orchestrator|yes|yes|sometimes|yes|no|yes|
|Meta Ops|yes|yes|yes|yes|no|no|
|Meta Strategy|yes|yes|yes|yes|no|no|
|Meta Detective|yes|yes|yes|yes|yes for scheduled QA|no|
|Knowledge Bank Ops|maybe|yes|yes|yes|yes|yes|
|Prompt/Workflow Ops|maybe|yes|yes|yes|no|yes|
|Hygiene Clean|maybe|yes|yes|yes|yes|no|
|Daily Command Board|no|yes|no|maybe|yes|yes|
|Night Planning|maybe|yes|no|maybe|yes|yes|
|Session Export|no|yes|no|no|yes|yes|
|Promotion Protocol|no|yes|yes|yes|maybe|yes|
|Deep Research to Patchspec|no|yes|yes|yes|no|no|
|No-Drift Validation|no|yes|yes|yes|no|no|
|Pattern Learning|maybe|yes|yes|maybe|yes|yes|
|Skill Curator|no|yes|no|maybe|yes|yes|

**Implementation bias for later:** use **profiles** for persistent role identity and tool separation; use **skills** for reusable procedures; use **delegation** for synchronous one-off specialist work; use **Kanban** for durable multi-step / multi-agent workflows; use **cron** for daily/nightly maintenance, board generation, skill review, and pattern-learning loops.

---

# 6. Candidate Hermes Skill Backlog

|Skill Name Candidate|Purpose|Main Source Pattern|Trigger Description|
|---|---|---|---|
|`orchestration-intake`|Normalize broad requests into bounded packets|Holding flow + Alfred intake|Use when a user request spans projects, agents, or unclear execution modes|
|`project-routing`|Choose project/interface/lane|Project routing + Alfred routing matrix|Use when work must be assigned to a project or owner|
|`agent-handoff-packet`|Generate handoff packet schema|AGENT_HANDOFF_CONTRACTS|Use before delegating or creating a Kanban card|
|`receiver-disposition`|Accept/reject/revise/hold/escalate|Handoff contracts|Use when evaluating incoming work|
|`evd-imp-rsk-validation`|Apply evidence/impact/risk banding|Handoff contracts|Use when risk, impact, or evidence level changes routing|
|`deep-research-to-patchspec`|Convert research to implementation spec|OpenCLAW process|Use for source-grounded implementation|
|`no-drift-diff-validation`|Validate patch vs spec/source|Alfred validation flows|Use after patch or file edits|
|`session-export`|Capture session state and next actions|Session export protocol|Use at end of every session|
|`night-planning-loop`|Synthesize exports into next-day work|Night planning protocol + Alfred night loop|Use nightly or after large day recap|
|`daily-command-board`|Generate editable daily board|Alfred board templates|Use every morning|
|`craft-flow-handoff`|Prepare a focused work session|Alfred craft-flow routine|Use when operator selects a board task|
|`pattern-learning-capture`|Stage repeated patterns as candidates|Alfred pattern learning|Use after repeated workflows or session recaps|
|`knowledge-promotion-review`|Promote/reject candidate doctrine|Promotion protocol|Use when a learning item might become canonical|
|`kb-placement-and-source-routing`|Place knowledge in correct lane|KB lanes/source map|Use when storing durable knowledge|
|`qa-hygiene-watchdog`|Detect structural drift and stale pointers|QA hygiene / watchdog|Use periodically or after large edits|
|`promptflow-template-builder`|Create reusable prompt/workflow patterns|Prompt/Workflow Ops|Use when a process becomes repeatable|
|`kanban-decomposition`|Create durable multi-agent task graph|Kanban orchestrator concept|Use when work needs specialists, dependencies, or audit trail|
|`operator-morning-review`|Guide human edits to the day board|Alfred templates|Use when confirming daily plan|
|`metrics-and-variables-capture`|Capture routing variables and session metrics|Alfred Variables & Metrics|Use during board creation/session export|
|`source-gap-protection`|Mark provisional/inferred claims|Alfred best practices|Use when source access is incomplete or inferred|

---

# 7. Priority Build Order for Later Translation

|Phase|Build First|Why|
|---|---|---|
|1|`orchestration-intake`, `project-routing`, `agent-handoff-packet`|These define the routing grammar. Without them, all later delegation becomes vague.|
|2|`session-export`, `night-planning-loop`, `daily-command-board`|These create the day/night operating loop and persistent project continuity.|
|3|`no-drift-diff-validation`, `qa-hygiene-watchdog`, `evd-imp-rsk-validation`|These prevent silent drift and unsafe promotion.|
|4|`knowledge-promotion-review`, `kb-placement-and-source-routing`, `pattern-learning-capture`|These create the learning/promotion pipeline.|
|5|`kanban-decomposition`, profile-specific SOUL/context files|These turn the system into durable multi-agent orchestration.|
|6|Deep specialist skills: research-to-patchspec, craft-flow, metrics, promptflow builder|These make the system productive rather than merely well-governed.|

---

# 8. Key Extraction Conclusions

**Core architectural finding:** OpenCLAW contributes strong **role boundaries, handoff contracts, validation bands, promotion discipline, and QA loops**. Alfred contributes the **operator-facing daily/nightly assistant loop**, including Daily Command Board, session export, variables/metrics, craft-flow handoffs, and pattern learning.

**Hermes mapping principle:** do not port OpenCLAW as a final architecture. Extract its process logic into Hermes-native primitives: profiles for persistent roles, skills for procedures, Kanban for durable multi-agent work, delegation for bounded synchronous specialist calls, cron for daily/nightly loops, and memory/context files for stable state.

**Most important preserved invariant:** candidate learning must not become runtime truth automatically. The source material repeatedly separates accepted doctrine from `LEARNING_QUEUE.md`, source evidence, and provisional claims. This should become a first-class Hermes skill-curation and promotion rule.