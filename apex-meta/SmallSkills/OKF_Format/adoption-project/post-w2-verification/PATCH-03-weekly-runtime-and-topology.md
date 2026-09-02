---
type: Plan
title: PATCH-03 — Weekly Runtime Isolation and Topology
description: Exact-match patch pack to make Weekly stage isolation executable, align Macro/Meso/entrypoint topology with the live direct-fork Skill design, and remove stale wrapper-agent and Project-KB wiring.
tags: [patch, weekly-orchestrator, claude, skills, agents, topology]
status: proposed_not_applied
---

# Intent

Repair the Weekly Orchestrator without recreating the retired stage-wrapper agents.

Current live design is:

```text
main conversation: weekly-orchestrator control plane
  -> six stage Skills, each forked directly by Skill frontmatter
  -> two reviewer agents, spawned only for consequential review
  -> approved durable mutation through apex-session
```

The current controller already describes this design. The runtime frontmatter and older Weekly Macro/Meso documents do not yet match it.

**Do not apply this file as a whole-file rewrite. Apply each exact-match block independently.**

# A. Make stage isolation executable

Claude Code runtime isolation is controlled by `context: fork` in `SKILL.md` frontmatter. A `skill_contract.execution.context` field inside the Markdown body is descriptive only.

## Block 1 — PrecapWeek

<file>.claude/skills/PrecapWeek/SKILL.md</file>
<old>---
name: PrecapWeek
description: Use this skill when the operator asks to plan the upcoming workweek from weekly intent, detailed project-state inputs, compact project-status overview signals, calendar constraints, and the weekday blueprint. Produces a validated Weekly Command Brief plus a minimal downstream seed for PrecapNextDay. Does not create the detailed next-day plan, prompt packets, project execution, status merge, or calendar events.
---</old>
<new>---
name: PrecapWeek
description: Use this skill when the operator asks to plan the upcoming workweek from weekly intent, detailed project-state inputs, compact project-status overview signals, calendar constraints, and the weekday blueprint. Produces a validated Weekly Command Brief plus a minimal downstream seed for PrecapNextDay. Does not create the detailed next-day plan, prompt packets, project execution, status merge, or calendar events.
context: fork
---</new>

## Block 2 — PrecapNextDay

<file>.claude/skills/PrecapNextDay/SKILL.md</file>
<old>---
name: PrecapNextDay
description: Use this skill when the operator asks to create, compile, or review a resilient next-day orchestration plan from partial planning, project, recap, calendar, prompt, workflow, or usage context. Produces a PreCap Next Day Brief, one Flow Execution Card per full flow, and real prompt files. Does not execute project work, run FlowRecap, merge status, or require complete inputs.
---</old>
<new>---
name: PrecapNextDay
description: Use this skill when the operator asks to create, compile, or review a resilient next-day orchestration plan from partial planning, project, recap, calendar, prompt, workflow, or usage context. Produces a PreCap Next Day Brief, one Flow Execution Card per full flow, and real prompt files. Does not execute project work, run FlowRecap, merge status, or require complete inputs.
context: fork
---</new>

## Block 3 — raw-flow-dump-normalize

<file>.claude/skills/raw-flow-dump-normalize/SKILL.md</file>
<old>---
name: raw-flow-dump-normalize
description: Use this skill when messy operator execution notes, chat fragments, artifact references, or skipped-flow signals need to be normalized into a minimal raw execution handoff for APEX FlowRecap without running FlowRecap or mutating project state.
---</old>
<new>---
name: raw-flow-dump-normalize
description: Use this skill when messy operator execution notes, chat fragments, artifact references, or skipped-flow signals need to be normalized into a minimal raw execution handoff for APEX FlowRecap without running FlowRecap or mutating project state.
context: fork
---</new>

## Block 4 — flow-recap

<file>.claude/skills/flow-recap/SKILL.md</file>
<old>---
name: flow-recap
description: Use this skill when converting one completed, partial, skipped, or blocked flow plus its normalized raw flow dump into a compact operator-reviewable FlowRecap packet with candidate-only project status and model usage deltas.
---</old>
<new>---
name: flow-recap
description: Use this skill when converting one completed, partial, skipped, or blocked flow plus its normalized raw flow dump into a compact operator-reviewable FlowRecap packet with candidate-only project status and model usage deltas.
context: fork
---</new>

## Block 5 — status-merge

<file>.claude/skills/status-merge/SKILL.md</file>
<old>---
name: status-merge
description: Use this skill to review FlowRecap candidate deltas against confirmed Apex Session and Sync references, record the operator merge decision, and prepare a proposal-only Apex Session mutation request.
---</old>
<new>---
name: status-merge
description: Use this skill to review FlowRecap candidate deltas against confirmed Apex Session and Sync references, record the operator merge decision, and prepare a proposal-only Apex Session mutation request.
context: fork
---</new>

## Block 6 — ProjectStatus

<file>.claude/skills/ProjectStatus/SKILL.md</file>
<old>---
name: ProjectStatus
description: >
  Use this skill when the operator asks to create, update, normalize, rank, or
  validate a compact cross-project project status overview. Accepts manual
  notes, project-specific summaries, previous overview text, or unassigned
  incoming items. Produces a project → task → subtask overview with
  [priority/urgency/date] ratings, ranked task view, temporary unassigned
  section, and operator review flags. Does not create weekly plans, next-day
  plans, status merges, project execution, workstreams, or detailed project
  databases.
---</old>
<new>---
name: ProjectStatus
description: >
  Use this skill when the operator asks to create, update, normalize, rank, or
  validate a compact cross-project project status overview. Accepts manual
  notes, project-specific summaries, previous overview text, or unassigned
  incoming items. Produces a project → task → subtask overview with
  [priority/urgency/date] ratings, ranked task view, temporary unassigned
  section, and operator review flags. Does not create weekly plans, next-day
  plans, status merges, project execution, workstreams, or detailed project
  databases.
context: fork
---</new>

# B. Align the locked Weekly Macro decision with the live runtime

## Block 7 — D-M1 topology

<file>apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md</file>
<old>## D-M1. Topology: main-thread meta orchestrator + ephemeral stage subagents

Decision: the meta agent is the **main conversation operating under the `weekly-orchestrator` control skill** (accountability: meta_ops). Every loop stage runs as an **ephemeral, context-isolated subagent invoked from a durable definition** under `.claude/agents/`. No always-on agents; no subagent orchestrates other subagents.</old>
<new>## D-M1. Topology: main-thread controller + forked stage Skills + reviewer agents

Decision: the **main conversation operating under the `weekly-orchestrator` control Skill** holds loop position and gates. Six content stages run directly from their own `.claude/skills/*/SKILL.md` entrypoints with `context: fork`. Only the two independent review lenses use durable definitions under `.claude/agents/`. No stage-wrapper agent sits between the controller and its owning Skill, no always-on agent holds loop state, and no forked worker orchestrates other workers.</new>

## Block 8 — D-M2 mechanism decision

<file>apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md</file>
<old>## D-M2. Skills do NOT become agents; agents own skills by declaration

Decision: the operator hypothesis "skills become agents with their own isolated skill base" is **partially corrected**. Skills stay skills under `.claude/skills/` (the discovery root). Each stage subagent gets its isolated skill base through the `skills:` frontmatter preload field — full skill content injected into the subagent's fresh context at startup. Ownership is declared in the agent definition, not expressed by moving files.

Evidence:
- Explicit KB verdict (`wiki/summaries/max-run-20260709/skill-hook-plugin-mcp-boundaries.md` C001): "Skill, hook, plugin, and MCP surfaces should not collapse into one generic 'agent' mechanism."
- `wiki/summaries/agent-vs-subagent-vs-skill.md` (claim C003): skill = reusability WITHOUT isolation; subagent = isolation + tool restriction + verbose work returning a short summary. The weekly stages need both → subagent + preloaded skill, not a converted skill.
- Sub-agents doc (`raw/.../primary-code-claude-com-docs-en-sub-agents.md.md` line 277): `skills:` field preloads full skill content; unlisted skills remain invocable via the Skill tool.
- Nested "subskills" are non-canonical; flat sibling skill packages win (`ingest-analysis/.../SubskillsVsAgents_CC.md` §5). Therefore: no folder moves of skill packages; the only required file surgery was canonicalizing six entrypoints to `SKILL.md` with valid frontmatter (without which discovery and preload fail).</old>
<new>## D-M2. Stage Skills fork directly; reviewer lenses remain agents

Decision: Skills remain procedure packages under `.claude/skills/`, and agents remain separately defined worker/accountability surfaces under `.claude/agents/`. Claude Code now provides Skill-level isolation through `context: fork`, so a dedicated wrapper agent is not required merely to isolate a Weekly stage. The six Weekly stages therefore fork directly from their owning Skills. The two reviewer lenses remain agents because they require distinct blind-review identities, tools, and dispatch contracts.

Evidence:
- The mechanism-separation finding remains valid: Skill, agent, hook, plugin, and MCP surfaces must not collapse into one generic mechanism.
- Current Claude Code Skill runtime supports `context: fork`; the rendered Skill becomes the isolated worker task and receives invocation arguments without inheriting the parent conversation.
- The live `weekly-orchestrator` contract already dispatches the six stage Skills directly and reserves `.claude/agents/` for the two reviewer lenses.
- Flat sibling Skill packages remain canonical; no stage procedure is moved into an agent directory.</new>

## Block 9 — D-M3 execution matrix

<file>apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md</file>
<old>## D-M3. Agent ↦ skill ownership matrix

| stage agent (`.claude/agents/`) | accountability | preloaded skills (owned base) | via Skill tool on demand | tools | gate |
|---|---|---|---|---|---|
| apex-precap-week | meta_strategy | PrecapWeek | — | Read, Grep, Glob, Write | G1 |
| apex-precap-next-day | meta_ops | PrecapNextDay | PromptEngineer, AIRouting, Workflow&Processes | Read, Grep, Glob, Write, Skill | G2 |
| apex-evidence-normalize | meta_ops | raw-flow-dump-normalize | — | Read, Grep, Glob, Write | G3 capture |
| apex-flow-recap | meta_ops | flow-recap, model-usage-log | — | Read, Grep, Glob, Write | G4 |
| apex-status-merge | meta_ops | status-merge | — | Read, Grep, Glob, Write | G5 |
| apex-project-status | meta_ops | ProjectStatus | — | Read, Grep, Glob, Write | none |
| apex-review-validity | meta_detective | — (self-contained lens instructions) | — | Read, Grep, Glob | review |
| apex-review-alignment | meta_detective | — (self-contained lens instructions) | — | Read, Grep, Glob | review |

Alfred (operator-facing accountability) is carried by the main thread itself: it presents packets, holds gates, and records operator decisions. It is not a spawned agent.</old>
<new>## D-M3. Stage execution matrix

| stage | runtime owner | execution | on-demand dependencies | gate |
|---|---|---|---|---|
| precap_week | `.claude/skills/PrecapWeek/SKILL.md` | direct forked Skill | — | G1 |
| precap_next_day | `.claude/skills/PrecapNextDay/SKILL.md` | direct forked Skill | PromptEngineer, AIRouting, Workflow&Processes when required by the stage contract | G2 |
| evidence_normalize | `.claude/skills/raw-flow-dump-normalize/SKILL.md` | direct forked Skill | — | none |
| flow_recap | `.claude/skills/flow-recap/SKILL.md` | direct forked Skill per flow | model-usage-log is a downstream finalization owner only when actual usage evidence exists; it is not preloaded by default | G4 |
| status_merge | `.claude/skills/status-merge/SKILL.md` | direct forked Skill | — | G5 |
| project_status | `.claude/skills/ProjectStatus/SKILL.md` | optional direct forked Skill | — | none |
| review_validity | `.claude/agents/apex-review-validity.md` | blind reviewer agent | — | review |
| review_alignment | `.claude/agents/apex-review-alignment.md` | blind reviewer agent | — | review |

The main thread carries operator-facing presentation, gate holding, and decision recording. It is not a spawned stage worker.</new>

## Block 10 — D-M4 writer terminology

<file>apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md</file>
<old>Decision: role/tool scoping says who may act; the artifact's `authority.state` (candidate | verified | invalidated) says what may justify action. Weekly stage agents write only their own artifacts. Canon-changing project/task writes happen ONLY in Apex Session after `operator_validation: confirmed` and verified-input closure. No BUILD/VERIFY/LOCK state machine.</old>
<new>Decision: role/tool scoping says who may act; the artifact's `authority.state` (candidate | verified | invalidated) says what may justify action. Forked Weekly stage workers write only their own artifact families. Canon-changing project/task writes happen ONLY in Apex Session after `operator_validation: confirmed` and verified-input closure. No BUILD/VERIFY/LOCK state machine.</new>

## Block 11 — D-M6 return terminology

<file>apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md</file>
<old>Decision: MD-first with one fenced YAML envelope block per packet; snake_case; function-typed labels (Rule/Constraint/Stop/Applies when/Do not); refs-not-copies; compact entrypoints with `read_when`-gated references; stage agents return envelope + ≤12-line summary, never full bodies, so the main thread's context stays flat across the continuous loop.</old>
<new>Decision: MD-first with one fenced YAML envelope block per packet; snake_case; function-typed labels (Rule/Constraint/Stop/Applies when/Do not); refs-not-copies; compact entrypoints with `read_when`-gated references; forked stage workers return envelope + ≤12-line summary, never full bodies, so the main thread's context stays flat across the continuous loop.</new>

## Block 12 — rejected wrapper-agent alternative

<file>apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md</file>
<old>- Moving skill packages into per-agent folders: breaks skill discovery and `skills:` preload; collapses mechanisms the KB says to keep separate (D-M2 evidence).</old>
<new>- Wrapper agent for every stage or moving Skill packages into per-agent folders: adds an unnecessary delegation layer now that stage Skills can fork directly, and risks duplicating the Skill contract in a second runtime surface (D-M2 evidence).</new>

# C. Align the Weekly Meso execution map

## Block 13 — control-plane metadata and glossary owner

<file>apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md</file>
<old>control_plane:
  root_instruction: .claude/CLAUDE.md                                   # identity, core_loop, skills table, agents table, constraints
  orchestrator_skill: .claude/skills/weekly-orchestrator/SKILL.md      # stage routing, gate holding, project-engine handoffs
  handoff_schema: .claude/skills/weekly-orchestrator/references/handoff-schema.md   # one envelope for every packet + gate primitive + authority object
  review_wiring: .claude/skills/weekly-orchestrator/references/review-wiring.md     # dual-blind review procedure + deterministic aggregation
  glossary: apex-meta/GLOSSARY.md                                       # canonical meaning for drifted terms</old>
<new>control_plane:
  root_instruction: .claude/CLAUDE.md                                   # APEX activation router + global boundaries
  orchestrator_skill: .claude/skills/weekly-orchestrator/SKILL.md      # live Weekly stage routing, gates, and Session/Sync handoffs
  handoff_schema: .claude/skills/weekly-orchestrator/references/handoff-schema.md   # one envelope for every packet + gate primitive + authority object
  review_wiring: .claude/skills/weekly-orchestrator/references/review-wiring.md     # dual-blind review procedure + deterministic aggregation
  glossary: apex-meta/orchestration/GLOSSARY.md                         # APEX-wide orchestration terminology authority</new>

## Block 14 — agent layer contains only the actual Weekly agents

<file>apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md</file>
<old>## agent layer (durable definitions, ephemeral invocations)

```yaml
agents:
  - .claude/agents/apex-precap-week.md
  - .claude/agents/apex-precap-next-day.md
  - .claude/agents/apex-evidence-normalize.md
  - .claude/agents/apex-flow-recap.md
  - .claude/agents/apex-status-merge.md
  - .claude/agents/apex-project-status.md
  - .claude/agents/apex-review-validity.md
  - .claude/agents/apex-review-alignment.md
```</old>
<new>## agent layer (review only)

```yaml
review_agents:
  - .claude/agents/apex-review-validity.md
  - .claude/agents/apex-review-alignment.md
```

The six content stages are direct forked Skills. No `.claude/agents/apex-precap-*`, `apex-evidence-normalize`, `apex-flow-recap`, `apex-status-merge`, or `apex-project-status` wrapper definitions are required.</new>

## Block 15 — direct-fork Skill layer and remove implicit Project-KB wiring

<file>apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md</file>
<old>## skill layer (owned bases; canonical SKILL.md entrypoints)

```yaml
weekly_loop_skills:
  - .claude/skills/PrecapWeek/SKILL.md
  - .claude/skills/PrecapNextDay/SKILL.md
  - .claude/skills/raw-flow-dump-normalize/SKILL.md
  - .claude/skills/flow-recap/SKILL.md
  - .claude/skills/model-usage-log/SKILL.md
  - .claude/skills/status-merge/SKILL.md
  - .claude/skills/ProjectStatus/SKILL.md
dependency_skills:                                     # invoked via Skill tool by apex-precap-next-day when needed
  - .claude/skills/PromptEngineer/SKILL.md
  - .claude/skills/AIRouting/SKILL.md
  - .claude/skills/Workflow&Processes/SKILL.md
external_project_engine:
  - .claude/skills/apex-plan/SKILL.md                  # project proposal capability; independently invoked
  - .claude/skills/apex-sync/SKILL.md                  # deterministic project reports; independently invoked
  - .claude/skills/apex-session/SKILL.md               # confirmed project/task mutation and planning-feed owner
optional_knowledge_context: [project-kb-manager]
```

Each skill package keeps its `references/` (read_when-gated), `templates/` (J1–J12 promoted cards), and `examples/` in place — declared ownership by agent preload, no folder moves.</old>
<new>## skill layer (direct-fork stages; canonical SKILL.md entrypoints)

```yaml
weekly_stage_skills:
  - .claude/skills/PrecapWeek/SKILL.md
  - .claude/skills/PrecapNextDay/SKILL.md
  - .claude/skills/raw-flow-dump-normalize/SKILL.md
  - .claude/skills/flow-recap/SKILL.md
  - .claude/skills/status-merge/SKILL.md
  - .claude/skills/ProjectStatus/SKILL.md
dependency_skills:                                     # loaded by the owning stage only when its contract requires them
  - .claude/skills/PromptEngineer/SKILL.md
  - .claude/skills/AIRouting/SKILL.md
  - .claude/skills/Workflow&Processes/SKILL.md
  - .claude/skills/model-usage-log/SKILL.md            # downstream usage finalizer; not a default FlowRecap preload
external_project_engine:
  - .claude/skills/apex-plan/SKILL.md                  # project proposal capability; independently invoked
  - .claude/skills/apex-sync/SKILL.md                  # deterministic project reports; independently invoked
  - .claude/skills/apex-session/SKILL.md               # confirmed project/task mutation and planning-feed owner
```

Each stage package keeps its `references/`, `templates/`, and `examples/` in place. Stage isolation comes from `context: fork` on the owning `SKILL.md`; dependencies load on demand. `project-kb-manager` remains a standalone capability and is not an implicit Weekly stage, state owner, or write path.</new>

## Block 16 — artifact writers are stage workers, not retired stage agents

<file>apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md</file>
<old>artifact_families:                   # proposals/computed packets; stage agents write here only</old>
<new>artifact_families:                   # proposals/computed packets; forked stage workers write only their own family</new>

## Block 17 — write-permission matrix

<file>apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md</file>
<old>| `artifacts/<own family>/` | the producing stage agent | always allowed within its family |
| project/task state | Apex Session | confirmed J9 proposal + operator validation + verified-input closure |
| `.claude/kb/*` | project-kb-manager when invoked | supporting knowledge only; never weekly project-state canon |
| `.claude/skills/`, `.claude/agents/`, control plane | operator-directed sessions only | never during loop runs |
| reviewers | nothing | read-only |</old>
<new>| `artifacts/<own family>/` | the producing forked stage worker | always allowed within its family and selected stage contract |
| project/task state | Apex Session | confirmed mutation proposal + operator validation + verified-input closure |
| `.claude/skills/`, `.claude/agents/`, control plane | operator-directed maintenance sessions only | never during loop runs |
| reviewer agents | nothing | read-only |</new>

# D. Repair the Weekly entrypoint and repo index

## Block 18 — classify Macro/Meso/Micro and runtime locations accurately

<file>apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md</file>
<old>```yaml
architecture_package:
  macro: architecture/01-macro-architecture-decision.md   # locked topology, agent/skill ownership, permission + review model
  meso: architecture/02-meso-file-map.md                  # complete execution-surface file inventory + write matrix
  micro: architecture/03-execution-trace-verification.md  # real dry-run trace + file-level verification record
runtime_entrypoint: ../../../.claude/skills/weekly-orchestrator/SKILL.md
apex_os_router: ../../../.claude/CLAUDE.md
agent_runtime_location: ../../../.claude/agents/
```</old>
<new>```yaml
architecture_package:
  weekly_macro: architecture/01-macro-architecture-decision.md   # current topology, mechanism, permission + review decisions
  weekly_meso: architecture/02-meso-file-map.md                  # current execution-surface inventory + write matrix
  weekly_micro_evidence: architecture/03-execution-trace-verification.md  # historical verification record; not live runtime law
runtime_entrypoint: ../../../.claude/skills/weekly-orchestrator/SKILL.md
apex_os_router: ../../../.claude/CLAUDE.md
stage_skill_runtime_location: ../../../.claude/skills/
reviewer_agent_runtime_location: ../../../.claude/agents/
```</new>

## Block 19 — current weekly loop uses Session, not an implicit Project-KB update

<file>apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md</file>
<old>```text
PrecapWeek
  -> PrecapNextDay
  -> execution and evidence capture
  -> FlowRecap
  -> StatusMerge / Project KB update
  -> ProjectStatus
  -> next planning cycle
```</old>
<new>```text
PrecapWeek
  -> PrecapNextDay
  -> execution and evidence capture
  -> FlowRecap
  -> StatusMerge proposal
  -> apex-session confirmed mutation
  -> ProjectStatus (optional derived overview)
  -> next planning cycle
```</new>

## Block 20 — repository map description of the Weekly loop

<file>apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md</file>
<old>| `Weekly-Orchestrator/` | **live, domain-specific index and research KB** | Defines and indexes the `PrecapWeek -> PrecapNextDay -> execution -> FlowRecap -> status/update` weekly loop. | Start with `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`. Human and machine indexes belong under `indexes/`; load `OperatorResearch/` only when targeted source evidence is needed. |</old>
<new>| `Weekly-Orchestrator/` | **live, domain-specific index and research KB** | Defines and indexes the `PrecapWeek -> PrecapNextDay -> execution/evidence -> FlowRecap -> StatusMerge proposal -> apex-session mutation -> optional ProjectStatus` weekly loop. | Start with `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`. Human and machine indexes belong under `indexes/`; load `OperatorResearch/` only when targeted source evidence is needed. |</new>

# Micro handling

`architecture/03-execution-trace-verification.md` already begins with an explicit historical-record warning and should **not** be rewritten to pretend its 2026-07 wrapper-agent trace is current. The repair is to stop presenting that evidence file as current runtime law from the Weekly entrypoint.

# Runtime verification after application

```text
1. Invoke each six stage Skills in a fresh Claude Code session and confirm a distinct forked worker appears.
2. Confirm the parent conversation does not receive the stage's full working context, only its returned result.
3. Run `Run the Weekly Orchestrator` from a pre-first-cycle state: the controller must route to PrecapWeek without looking for any `.claude/agents/apex-precap-*` file.
4. Trigger a consequential packet: only `apex-review-validity` and `apex-review-alignment` should use `.claude/agents/`.
5. Confirm G5-approved project/task changes route through `apex-session`; `project-kb-manager` must not appear as an implicit Weekly mutation path.
6. Resolve every path in `02-meso-file-map.md`; zero listed live paths may be missing.
```

# Residual not auto-fixed

The retired wrapper agents formerly provided explicit tool lists. `context: fork` restores isolation but does not by itself prove identical host permission behavior. Do not invent a new hard tool-deny profile in this patch. Capture real runtime tool availability during the six-stage verification above; harden only a demonstrated excess capability that conflicts with a stage contract.
