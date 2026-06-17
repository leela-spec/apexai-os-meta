# Source Index for Hermes/OpenCLAW Personal Orchestration System

## 1. Source Inventory

### A. Uploaded Project Resource Files

| Source                                                                | Type                                      | Location                                | What it contains                                                                                                                                                                             | When to consult it                                                                                              | Priority |
| --------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------- |
| `llms.txt`                                                            | Hermes docs index                         | Project resource / `/mnt/data/llms.txt` | Official Hermes documentation map: install, CLI/TUI, config, profiles, tools, skills, curator, memory, context files, plugins, cron, delegation, Kanban, media, messaging, developer guides. | First lookup for canonical Hermes feature docs and doc navigation.                                              | P0       |
| `Hermes Agent - Development Guide.md`                                 | Hermes codebase architecture guide        | Project resource                        | Repo/codebase guide: `run_agent.py`, `model_tools.py`, `toolsets.py`, CLI/TUI/gateway, plugins, tools, cron, tests, profile-aware paths.                                                     | When deciding what is configured vs implemented, or where Hermes functionality lives in code.                   | P0       |
| `HermesAgentMasterClass.md`                                           | Conceptual + practical guide              | Project resource                        | Agent loop, skills, memory, subagents, custom tools, deployment, sandboxing, model routing, production patterns.                                                                             | When explaining Hermes’ operating model or choosing between memory, skills, tools, subagents, deployment modes. | P1       |
| `RedditUserExperienceWithHermes.md`                                   | Community lessons                         | Project resource                        | Practical usage warnings: start small, segment profiles, config hygiene, skill system as core, avoid building everything on day one.                                                         | When defining v1 scope, anti-patterns, and operator adoption path.                                              | P2       |
| `SkillsTraining&Examples_Claude.md`                                   | Skills training / examples                | Project resource                        | Skill format, YAML frontmatter, hierarchy via related skills, progressive disclosure, self-improvement loop, skill taxonomy.                                                                 | When designing reusable Hermes skills and skill relationships.                                                  | P0       |
| `BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md`                     | Prior orchestration research              | Project resource                        | Most directly relevant orchestration report: context files → skills → profiles → delegation/Kanban → curator sequence.                                                                       | Primary design input for later Hermes orchestration architecture.                                               | P0       |
| `WorkflowExamples_Claude.md`                                          | Workflow examples                         | Project resource                        | Concrete skill/workflow examples, code review skill, subagent-driven development, Kanban/swarm examples, skill maps.                                                                         | When converting abstract orchestration into operational loops.                                                  | P1       |
| `FromZeroToUltimateHermes_NateHerk.md`                                | Practical Hermes setup mental model       | Project resource                        | Five pillars: memory, skills, soul, crons, self-improving loop; Telegram/VPS/GitHub backup patterns.                                                                                         | When designing practical operator-facing assistant setup.                                                       | P1       |
| `Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md` | Structured course extraction              | Project resource                        | Personal assistant setup sequence, Telegram/VPS/GitHub, secret handling, cron, backup, multiple-agent decision logic.                                                                        | When designing personal assistant v1 and operational setup.                                                     | P1       |
| `HermesAgentDeepDive.md`                                              | Deep architecture guide                   | Project resource                        | Platform-agnostic core, prompt stability, progressive disclosure, profile isolation, tools, memory, plugin system.                                                                           | When preserving Hermes-native architecture and avoiding brittle prompt/config designs.                          | P0       |
| `TryofTrainersbutFail.md`                                             | Failed attempt / corrective artifact      | Project resource                        | Reframing: tools are not the main vehicle for orchestration logic; skills + delegation + curator + Kanban are.                                                                               | When avoiding wrong abstraction choices and tool/plugin overuse.                                                | P2       |
| `TrainingHermes_claude.md`                                            | Hermes training/source verification notes | Project resource                        | Verified material on `.hermes` structure, memory limits, cron/state surfaces, missing-source notes.                                                                                          | When checking training/setup claims or identifying gaps in verified examples.                                   | P2       |
| `Q&A_ProfileVsAgents.md`                                              | Profile vs agent decision guide           | Project resource                        | Distinction between profile as persistent config/state and agent as running instance; department-head swarm examples.                                                                        | When deciding profile vs skill vs subagent.                                                                     | P0       |
| `Q&A_SwarmOrchestration.md`                                           | Swarm/orchestration guide                 | Project resource                        | Kanban swarm setup, orchestrator profile, dispatcher, subagent delegation alternative, goal mode.                                                                                            | When designing durable multi-agent orchestration.                                                               | P0       |
| `Skill Usage Tracking and Backup.md`                                  | Skill telemetry/lifecycle guide           | Project resource                        | `.usage.json`, view/use/patch counts, lifecycle state, provenance, backup/rollback.                                                                                                          | When designing skill governance, telemetry, curator policy, rollback.                                           | P0       |
| `kanban-orchestrator_skill.md`                                        | Canonical orchestration skill             | Project resource                        | Real `kanban-orchestrator` skill: discover profiles, route not execute, decompose graph, create linked cards, avoid invented assignees.                                                      | Canonical behavior playbook for orchestrator profile.                                                           | P0       |
| `SkillCuratorArchitecture.md`                                         | Curator architecture                      | Project resource                        | Curator lifecycle, idle-triggered review, pin/archive/patch/consolidate, `.curator_state`, invariants.                                                                                       | When defining self-improvement and skill maintenance loop.                                                      | P0       |
| `Skills Management and Security.md`                                   | Skill safety/governance                   | Project resource                        | Programmatic skill creation, validation, security scanning, static guard, synchronization, frontmatter constraints.                                                                          | When creating safe skill promotion/update process.                                                              | P0       |
| `SkillSpecification.md`                                               | Agent Skills spec                         | Project resource                        | Exact skill directory structure, `SKILL.md` frontmatter, optional directories, progressive disclosure, validation.                                                                           | When writing actual skills later.                                                                               | P0       |
| `SkillCreationBestPractice.md`                                        | Skill creation methodology                | Project resource                        | Ground skills in real expertise/artifacts, refine through execution, spend context wisely, structure references.                                                                             | When designing high-quality project-specific skills.                                                            | P0       |
| `OptimizingSkillDescriptions.md`                                      | Skill trigger optimization                | Project resource                        | Description-trigger mechanics, positive/negative trigger evals, trigger-rate testing, overfitting prevention.                                                                                | When making skills activate reliably.                                                                           | P1       |
| `EvaluatingSkills.md`                                                 | Skill eval methodology                    | Project resource                        | Eval cases, baseline comparison, assertions, grading, benchmark output, iteration loop.                                                                                                      | When testing whether a skill improves outputs.                                                                  | P1       |

### B. GitHub / Repo Sources

The connected repo surfaced as `leela-spec/MasterOfArts`, private, indexed, with the description “Best-practice OpenClaw infrastructure on Hetzner: setup, operations, maintenance, and project runbooks.”

|Source|Type|Location|What it contains|When to consult it|Priority|
|---|---|---|---|---|---|
|`OpenClaw/07_finalopenclawsystem`|Repo system root|`leela-spec/MasterOfArts`|Current best-defined OpenCLAW-derived system. Search surfaced managed agents, KB, docs, working reports, source maps, rules, rituals, and processes.|When extracting existing OpenCLAW architecture, logic, prompts, workflows, and system constraints.|P0|
|`OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md`|Agent routing index|Repo|Managed activation and routing entry point for first-wave compact agent seed set. Defines role, seed path, KB root, and validator for agents.|When mapping OpenCLAW agent roles into Hermes profiles, skills, or delegated subagents.|P0|
|`OpenClaw/07_finalopenclawsystem/managed/agents/*.md`|Agent seed files|Repo|Individual seed agents including `alfred`, `meta_strategy`, `special_ops__knowledge_bank`, etc. surfaced in repo search.|When extracting role definitions, identity files, and reusable specialist behavior.|P0|
|`OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md`|Agent KB index|Repo|Index for managed agent KB. Search confirms the path exists.|When locating canonical per-agent knowledge files.|P0|
|`OpenClaw/07_finalopenclawsystem/managed/agent_kb/<agent>/`|Per-agent KB|Repo|Per-role KB folders. Search surfaced `meta_detective` files like `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`, `BEST_PRACTICES.md`.|When translating durable procedural/quality knowledge into Hermes skills or profile context.|P0|
|`OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md`|Knowledge governance map|Repo|Defines starting-source map for seeding, auditing, and routing OpenCLAW managed knowledge; includes authority order, source classes, and governance structures.|When deciding source authority and resolving conflicts across OpenCLAW materials.|P0|
|`OpenClaw/07_finalopenclawsystem/managed/knowledge/*`|Knowledge governance files|Repo|Search surfaced `AGENT_KB_LANES.md`, `CROSS_REFERENCE_MANIFEST.md`, `KB_PROMOTION_LEDGER_TEMPLATE.md`, `OVERLAP_VALIDATION_MATRIX.md`.|When designing memory/KB promotion, conflict detection, source routing, and lifecycle.|P1|
|`OpenClaw/07_finalopenclawsystem/managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`|Workflow/process file|Repo|Search surfaced managed process workflow.|When translating OpenCLAW deep-research or patchspec procedures into Hermes skills.|P1|
|`OpenClaw/07_finalopenclawsystem/managed/rules/AGENTS.base.md`|Base rules/context|Repo|Search surfaced base agent rules file.|When extracting durable global rules that may map to Hermes `AGENTS.md`, `.hermes.md`, or profile `SOUL.md`.|P1|
|`OpenClaw/07_finalopenclawsystem/managed/rituals/BOOTSTRAP.md`|Startup ritual|Repo|Search surfaced bootstrap ritual.|When designing Hermes session-start, intake, and initialization routines.|P1|
|`OpenClaw/07_finalopenclawsystem/docs/hermes-docs/INDEX.txt`|Repo-local Hermes docs index|Repo|Hermes documentation copy/index in repo. Search found `INDEX.txt`, `tools-reference.md`, `toolsets-reference.md`, and `configuration.md`.|When using repo-local Hermes docs instead of internet docs.|P0|
|`OpenClaw/07_finalopenclawsystem/docs/hermes-docs/reference/tools-reference.md`|Hermes tools reference|Repo|Repo-local Hermes tool reference.|When deciding executable capability/tool/plugin surfaces.|P1|
|`OpenClaw/07_finalopenclawsystem/docs/hermes-docs/reference/toolsets-reference.md`|Hermes toolsets reference|Repo|Repo-local toolset reference.|When deciding which toolsets profiles/subagents should receive.|P1|
|`OpenClaw/07_finalopenclawsystem/docs/hermes-docs/user-guide/configuration.md`|Hermes config reference|Repo|Repo-local Hermes configuration guide.|When deciding config vs code vs context files.|P1|
|`OpenClaw/07_finalopenclawsystem/docs/working/*`|Working reports / patches|Repo|Search surfaced validation reports, watchdog QA/hygiene execution plans, patches, handovers.|When extracting negative lessons, QA/hygiene procedures, and verification artifacts.|P2|
|`OpenClaw/04_final-system-setup/NewFinals/NextLevel2/*`|Older system-lock / research artifacts|Repo|Search surfaced locked decision registers, governance specs, validation prompts, deep research prompts, execution plans.|Secondary source only; consult for historical decisions and conflict context.|P2|
|`OpenClaw_Setup/migration_payload/07_finalopenclawsystem/*`|Migration mirror|Repo|Search surfaced duplicated/migration payload versions of agent and KB indexes.|Use only for migration comparison, not primary authority unless current tree is missing data.|P3|
|`docs/HermesResearch`|Expected folder|Repo path requested by user|Exact folder name did **not** surface through repo search. Closest confirmed repo-local Hermes docs folder is `docs/hermes-docs`.|Search again later if a different branch/path exists; otherwise use `docs/hermes-docs`.|Unknown / pending|

---

## 2. Source Lookup Map

```yaml
lookup_map:
  hermes_installation_setup:
    primary_sources:
      - llms.txt
      - Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md
      - FromZeroToUltimateHermes_NateHerk.md
      - OpenClaw/07_finalopenclawsystem/docs/hermes-docs/INDEX.txt
      - OpenClaw/07_finalopenclawsystem/docs/hermes-docs/user-guide/configuration.md
    secondary_sources:
      - HermesAgentMasterClass.md
      - TrainingHermes_claude.md

  hermes_architecture:
    primary_sources:
      - Hermes Agent - Development Guide.md
      - HermesAgentDeepDive.md
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
      - OpenClaw/07_finalopenclawsystem/docs/hermes-docs/INDEX.txt
    secondary_sources:
      - HermesAgentMasterClass.md

  profiles_vs_agents:
    primary_sources:
      - Q&A_ProfileVsAgents.md
      - HermesAgentDeepDive.md
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
    secondary_sources:
      - RedditUserExperienceWithHermes.md
      - FromZeroToUltimateHermes_NateHerk.md

  skills:
    primary_sources:
      - SkillSpecification.md
      - SkillsTraining&Examples_Claude.md
      - Skills Management and Security.md
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
    secondary_sources:
      - WorkflowExamples_Claude.md
      - HermesAgentMasterClass.md

  skill_creation:
    primary_sources:
      - SkillCreationBestPractice.md
      - SkillSpecification.md
      - Skills Management and Security.md
      - SkillsTraining&Examples_Claude.md
    secondary_sources:
      - OptimizingSkillDescriptions.md
      - EvaluatingSkills.md

  skill_evaluation:
    primary_sources:
      - EvaluatingSkills.md
      - OptimizingSkillDescriptions.md
    secondary_sources:
      - SkillCreationBestPractice.md
      - Skill Usage Tracking and Backup.md

  curator_and_skill_lifecycle:
    primary_sources:
      - SkillCuratorArchitecture.md
      - Skill Usage Tracking and Backup.md
      - Skills Management and Security.md
    secondary_sources:
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md

  kanban_orchestration:
    primary_sources:
      - kanban-orchestrator_skill.md
      - Q&A_SwarmOrchestration.md
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
    secondary_sources:
      - WorkflowExamples_Claude.md
      - Q&A_ProfileVsAgents.md

  delegation:
    primary_sources:
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
      - Q&A_SwarmOrchestration.md
      - HermesAgentMasterClass.md
    secondary_sources:
      - Hermes Agent - Development Guide.md
      - WorkflowExamples_Claude.md

  cron_automation:
    primary_sources:
      - llms.txt
      - FromZeroToUltimateHermes_NateHerk.md
      - Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md
      - TrainingHermes_claude.md
    secondary_sources:
      - HermesAgentMasterClass.md

  personal_assistant_setup:
    primary_sources:
      - Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md
      - FromZeroToUltimateHermes_NateHerk.md
      - RedditUserExperienceWithHermes.md
    secondary_sources:
      - HermesAgentMasterClass.md
      - TrainingHermes_claude.md

  openclaw_existing_system:
    primary_sources:
      - OpenClaw/07_finalopenclawsystem
      - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
      - OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md
      - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md
    secondary_sources:
      - OpenClaw/07_finalopenclawsystem/docs/working/*
      - OpenClaw/04_final-system-setup/NewFinals/NextLevel2/*
      - OpenClaw_Setup/migration_payload/07_finalopenclawsystem/*

  openclaw_tool_logic:
    primary_sources:
      - OpenClaw/07_finalopenclawsystem/managed/rules/AGENTS.base.md
      - OpenClaw/07_finalopenclawsystem/managed/processes/*
      - OpenClaw/07_finalopenclawsystem/managed/agent_kb/*
      - OpenClaw/07_finalopenclawsystem/docs/hermes-docs/reference/tools-reference.md
      - OpenClaw/07_finalopenclawsystem/docs/hermes-docs/reference/toolsets-reference.md
    secondary_sources:
      - Hermes Agent - Development Guide.md
      - TryofTrainersbutFail.md

  openclaw_to_hermes_integration:
    primary_sources:
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
      - TryofTrainersbutFail.md
      - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md
      - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
      - OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md
    secondary_sources:
      - Q&A_ProfileVsAgents.md
      - Q&A_SwarmOrchestration.md
      - SkillCreationBestPractice.md

  security_and_secrets:
    primary_sources:
      - Skills Management and Security.md
      - Hermes Agent - Development Guide.md
      - Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md
      - TrainingHermes_claude.md
    secondary_sources:
      - FromZeroToUltimateHermes_NateHerk.md
      - Skill Usage Tracking and Backup.md

  github_backup_sync:
    primary_sources:
      - FromZeroToUltimateHermes_NateHerk.md
      - Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md
      - Skill Usage Tracking and Backup.md
    secondary_sources:
      - TrainingHermes_claude.md
      - Hermes Agent - Development Guide.md

  q_and_a_decision_flow:
    primary_sources:
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
      - Q&A_ProfileVsAgents.md
      - Q&A_SwarmOrchestration.md
      - kanban-orchestrator_skill.md
      - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md
    secondary_sources:
      - RedditUserExperienceWithHermes.md
      - TryofTrainersbutFail.md
```

---

## 3. Q&A Decision Flow

### Phase 1 — System Goal Definition

**Decision target:** define what the system is before designing how it works.

```yaml
phase_1_system_goal_definition:
  core_question: "What should the Hermes personal orchestration system ultimately do?"
  decision_axis:
    - personal_assistant
    - project_manager
    - multi_agent_swarm
    - content_workflow_orchestrator
    - coding_research_assistant
    - life_operating_system
    - all_of_the_above_staged
  questions:
    1: "What is the system's primary v1 job: assist, manage, delegate, automate, verify, or orchestrate?"
    2: "Which domain must become boringly reliable first?"
    3: "Which outcome would prove v1 works within one week?"
    4: "What should v1 explicitly not attempt?"
    5: "What failure would make the system untrustworthy?"
    6: "Is the first milestone a working daily loop, a skill system, a Kanban swarm, or a personal assistant interface?"
  decision_rule:
    - "If the goal is broad, force a staged roadmap."
    - "If no minimal reliable workflow is selected, do not design the full architecture."
    - "If v1 includes autonomous actions, define approval gates before automation."
```

### Phase 2 — Operator Model

```yaml
phase_2_operator_model:
  core_question: "How will the human operator interact with Hermes?"
  interface_options:
    - CLI
    - TUI
    - Telegram
    - desktop
    - GitHub repo
    - daily dashboard
    - voice
  questions:
    7: "Where will the operator actually issue commands most often?"
    8: "Where should outputs be delivered: chat, repo files, dashboard, Kanban board, or all of these?"
    9: "Which decisions must remain manual?"
    10: "Which tasks can Hermes execute without approval?"
    11: "Which tasks may be drafted automatically but require user approval before execution?"
    12: "Should the operator see every intermediate decision, or only summaries/checkpoints?"
  decision_rule:
    - "Use Telegram/voice for lightweight assistant access."
    - "Use CLI/TUI for implementation-heavy sessions."
    - "Use GitHub repo for durable source-of-truth artifacts."
    - "Use Kanban for durable, inspectable multi-step work."
```

### Phase 3 — Day Shift / Night Shift Loop

**Existing concept to preserve:** night shift produces pre-planned sessions; day shift executes selected sessions; day shift recap feeds night shift.

```yaml
phase_3_day_night_loop:
  night_shift_outputs:
    candidate_fields:
      - project
      - goal
      - rationale
      - expected_output
      - macro_meso_micro_plan
      - suggested_prompt_flow
      - model_or_profile_to_use
      - required_skills
      - required_tools
      - context_sources
      - approval_requirements
      - verification_plan
      - stop_conditions
      - recap_template
  day_shift_recap:
    candidate_fields:
      - session_id
      - selected_plan
      - executed_steps
      - outputs_created
      - blocked_steps
      - deviations_from_plan
      - what_worked
      - what_failed
      - operator_feedback
      - next_actions
      - memory_candidates
      - skill_candidates
      - kanban_updates
      - verification_status
  questions:
    13: "What exactly should a night-shift pre-planned session contain?"
    14: "Should night shift create Kanban cards, Markdown plans, prompts, or all three?"
    15: "How many pre-planned sessions should night shift produce per project?"
    16: "Should day shift be free-form, checklist-driven, or Kanban-card-driven?"
    17: "What must the day-shift recap always include?"
    18: "Which recap information becomes durable memory?"
    19: "Which recap information becomes a new or patched skill?"
    20: "Which recap information becomes project state?"
    21: "Which recap information becomes a Kanban card?"
  routing_rule:
    memory: "durable operator preference, stable project fact, long-lived constraint"
    skill: "repeatable procedure, recurring error/fix, reusable workflow"
    project_state: "current status, next action, open decision, artifact location"
    kanban_card: "durable task requiring future work, verification, dependency tracking, or another profile"
```

### Phase 4 — Agent/Profile Architecture

Hermes profile vs agent distinction matters: profile is persistent isolated state/config; agent is the running instance. The repo’s OpenCLAW agent index should be consulted before translating roles, because it defines named seeds and their KB roots. The AGENT_INDEX search result shows role rows such as `meta_strategy`, `meta_detective`, `special_ops__knowledge_bank`, `special_ops__informatics_design`, and `special_ops__prompts_workflows`.

```yaml
phase_4_agent_profile_architecture:
  questions:
    22: "Which roles require full profile isolation?"
    23: "Which roles should be skills inside one profile?"
    24: "Which roles should be temporary delegated subagents?"
    25: "Which roles need persistent Kanban ownership?"
    26: "Which profiles should exist in v1?"
    27: "Which OpenCLAW seed agents map cleanly to Hermes profiles?"
    28: "Which OpenCLAW seed agents are better expressed as skills?"
  candidate_roles_to_evaluate:
    - Orchestrator
    - Strategist
    - Operations
    - Detective / Verifier
    - Researcher
    - Prompt Designer
    - Skill Curator
    - Project Manager
    - Personal Assistant
    - OpenCLAW Tool Specialist
    - Content System Operator
  decision_matrix:
    profile:
      use_when:
        - "Needs persistent isolated memory/config/SOUL/tools."
        - "Represents a stable role with repeated independent work."
        - "Owns Kanban tasks across sessions."
    skill:
      use_when:
        - "Reusable procedure or decision rule."
        - "Does not need isolated memory."
        - "Should be invoked by multiple profiles."
    delegated_subagent:
      use_when:
        - "Temporary specialist work inside one turn."
        - "Parallel research/review/synthesis."
        - "No durable state needed."
    kanban_worker:
      use_when:
        - "Work must survive restarts."
        - "Human may interject."
        - "Audit trail matters."
        - "Multiple dependent workstreams exist."
```

### Phase 5 — Workflow Routing

```yaml
phase_5_workflow_routing:
  questions:
    29: "When should Hermes answer directly?"
    30: "When should Hermes load a skill?"
    31: "When should Hermes delegate to subagents?"
    32: "When should Hermes create Kanban tasks?"
    33: "When should Hermes schedule cron jobs?"
    34: "When should Hermes update memory?"
    35: "When should Hermes create or patch a skill?"
  routing_policy:
    answer_directly:
      when:
        - "Single-turn reasoning."
        - "No durable state."
        - "No specialized reusable procedure."
    use_skill:
      when:
        - "Known reusable procedure exists."
        - "Task matches a domain-specific workflow."
        - "Reliability depends on exact process."
    delegate_task:
      when:
        - "Parallel short-lived specialist analysis is useful."
        - "Independent reviewer/verifier needed."
        - "Result can return in the current session."
    kanban:
      when:
        - "Durable multi-step work."
        - "Cross-session state."
        - "Human-in-the-loop."
        - "Multiple profiles or dependencies."
    cron:
      when:
        - "Recurring schedule."
        - "Nightly/daily/weekly maintenance."
        - "Self-contained prompt can run in isolated session."
    update_memory:
      when:
        - "Stable user preference or durable project fact."
        - "Not a secret."
        - "Not temporary task status."
    create_or_patch_skill:
      when:
        - "Repeated workflow discovered."
        - "A failure mode has a reusable fix."
        - "The same instruction would otherwise be repeated."
```

### Phase 6 — OpenCLAW Integration

**Binding rule:** do not force OpenCLAW logic into Hermes if it breaks Hermes architecture. Translate to the closest Hermes-native primitive.

The repo contains managed OpenCLAW knowledge and authority maps, including `KB_STARTING_SOURCE_MAP.md`, which defines source classes, authority order, final-system surfaces, routing rules, and governance structures.

|OpenCLAW artifact|Hermes equivalent|Q&A test|
|---|---|---|
|Reusable procedure|`SKILL.md`|“Is this a repeatable how-to?”|
|Durable identity/context|`SOUL.md`, `USER.md`, `MEMORY.md`, `.hermes.md`, `AGENTS.md`|“Should this load every session/profile?”|
|Executable capability|Tool/plugin|“Does this need code/API execution?”|
|Long-running project state|Kanban|“Does this need durable status/dependencies?”|
|Recurring automation|Cron|“Should this run on schedule?”|
|Temporary specialist work|`delegate_task`|“Can this complete inside the current session?”|
|Persistent specialist|Profile|“Does this need isolated state and repeated ownership?”|
|Quality gate|Verifier skill/profile/Kanban card|“Does this block acceptance or promotion?”|

```yaml
phase_6_openclaw_integration:
  questions:
    36: "Which parts of 07_finalopenclawsystem are mature enough to preserve?"
    37: "Which parts are tool-use logic?"
    38: "Which parts are orchestration logic?"
    39: "Which parts conflict with Hermes architecture?"
    40: "Which parts should become Hermes skills?"
    41: "Which parts should become profile SOUL/context files?"
    42: "Which parts should become tools/plugins?"
    43: "Which parts should become Kanban state or templates?"
    44: "Which parts should be discarded or rewritten?"
  source_order:
    first:
      - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md
      - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
      - OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md
    second:
      - OpenClaw/07_finalopenclawsystem/managed/agent_kb/*
      - OpenClaw/07_finalopenclawsystem/managed/processes/*
      - OpenClaw/07_finalopenclawsystem/managed/rules/*
    third:
      - OpenClaw/07_finalopenclawsystem/docs/working/*
      - OpenClaw/04_final-system-setup/NewFinals/NextLevel2/*
```

### Phase 7 — Skill System Design

```yaml
phase_7_skill_system_design:
  questions:
    45: "What v1 skills are needed?"
    46: "Which skills are orchestration skills?"
    47: "Which skills are domain/project skills?"
    48: "Which skills are verification skills?"
    49: "Which skills should trigger automatically?"
    50: "Which skills should require manual invocation?"
    51: "How should skills be evaluated?"
    52: "Which skills should be pinned from curator archival?"
    53: "What naming convention should be used?"
  candidate_v1_skills:
    - orchestration-intake
    - day-shift-session-execution
    - night-shift-session-planning
    - session-recap-processing
    - project-routing
    - kanban-task-decomposition
    - openclaw-knowledge-translation
    - skill-promotion-governance
    - verification-and-output-review
    - personal-assistant-briefing
  first_skill_priority:
    1: orchestration-intake
    2: night-shift-session-planning
    3: session-recap-processing
    4: verification-and-output-review
    5: openclaw-knowledge-translation
```

### Phase 8 — Memory and Context Architecture

```yaml
phase_8_memory_context_architecture:
  questions:
    54: "What belongs in USER.md?"
    55: "What belongs in MEMORY.md?"
    56: "What belongs in SOUL.md?"
    57: "What belongs in project-level AGENTS.md or .hermes.md?"
    58: "What should never be remembered?"
    59: "What should be stored in GitHub instead of memory?"
    60: "What should remain session-searchable but not promoted to memory?"
  placement_rules:
    USER_md:
      contains:
        - durable operator preferences
        - interaction style
        - stable personal operating constraints
    MEMORY_md:
      contains:
        - durable project facts
        - recurring system decisions
        - stable workflow constraints
    SOUL_md:
      contains:
        - profile identity
        - behavioral posture
        - role-specific priorities
    AGENTS_or_hermes_md:
      contains:
        - project conventions
        - repo-specific instructions
        - build/test/run commands
        - architecture notes
    GitHub_repo:
      contains:
        - long documents
        - evolving specs
        - workflows
        - source maps
        - decision registers
        - skill backups
    do_not_store_in_memory:
      - secrets
      - temporary task status
      - one-off session debris
      - volatile unverified assumptions
```

### Phase 9 — Automation and Cron

```yaml
phase_9_automation_cron:
  questions:
    61: "Which workflows should be scheduled?"
    62: "What should run daily?"
    63: "What should run nightly?"
    64: "What should run weekly?"
    65: "What should never run automatically?"
    66: "What outputs should be posted to the operator?"
    67: "What outputs should silently update files/state?"
  candidate_crons:
    daily:
      - morning_briefing
      - active_project_snapshot
      - due_kanban_review
    nightly:
      - night_shift_session_planning
      - session_recap_processing
      - skill_candidate_review
      - project_next_step_generation
    weekly:
      - memory_hygiene_review
      - skill_usage_review
      - github_backup_check
      - open_questions_review
  never_automatic_without_approval:
    - destructive file changes
    - secret/API-key changes
    - external posting/sending
    - purchase/payment actions
    - profile deletion
    - skill deletion
    - broad architecture rewrites
```

### Phase 10 — Governance and Safety

```yaml
phase_10_governance_safety:
  questions:
    68: "What operations require explicit user approval?"
    69: "What secrets/API keys are needed?"
    70: "Where should secrets live?"
    71: "What should never be sent to hosted models?"
    72: "How should GitHub backup/sync work?"
    73: "What rollback strategy is needed?"
    74: "How should skill changes be reviewed?"
  approval_required:
    - creating or modifying cron jobs
    - sending external messages
    - committing/pushing to GitHub
    - deleting/archiving skills manually
    - adding plugins/tools
    - changing profile isolation
    - updating secrets
    - running destructive shell commands
  governance_outputs:
    - decision_register
    - source_map
    - skill_promotion_log
    - memory_update_log
    - kanban_audit_trail
    - rollback_snapshot
```

---

## 4. First Questions to Ask the Operator

Start with these. They define scope before architecture.

1. **Primary v1 target:** Is v1 primarily a personal assistant, project manager, multi-agent orchestrator, content/workflow operator, coding/research assistant, or staged life operating system?
    
2. **First reliable loop:** Which workflow should become reliable first: day/night planning, project routing, skill creation, Kanban delegation, personal assistant briefing, or verification?
    
3. **Operator interface:** Where will you actually use it daily: CLI/TUI, Telegram, GitHub repo, dashboard, desktop, or voice?
    
4. **Autonomy boundary:** What can Hermes do without approval, what can it draft only, and what must always require explicit approval?
    
5. **Profile roster:** Which v1 profiles should exist: Orchestrator, Strategist, Operations, Detective, Researcher, Skill Curator, Personal Assistant, OpenCLAW Tool Specialist?
    
6. **OpenCLAW preservation:** Which OpenCLAW areas are considered mature and worth preserving: agent seeds, KB rules, process workflows, verification logic, tool-use procedures, or governance maps?
    
7. **Night shift output:** Should night shift produce Markdown plans, Kanban cards, executable prompts, project recaps, or all of these?
    
8. **Memory boundary:** What should be promoted to memory, what should stay in GitHub, and what should remain only session-searchable?
    
9. **Skill governance:** Should new skills be manually reviewed before use, automatically created but pinned only after validation, or allowed to evolve under curator control?
    
10. **Quality gate:** What does “verified enough” mean for outputs: independent reviewer, checklist, source citation, test run, human approval, or all depending on task type?
    

---

## 5. Proposed Workflow for Designing the Hermes System

```yaml
proposed_next_workflow:
  objective:
    - "Do not design final architecture yet."
    - "Use Q&A to define requirements, constraints, and first workflow."

  session_1_operator_interview:
    inputs:
      - this_source_index
      - lookup_map
      - q_and_a_decision_flow
    outputs:
      - selected_v1_goal
      - selected_first_workflow
      - operator_interface_decision
      - autonomy_approval_policy
      - initial_profile_roster
      - OpenCLAW_preservation_targets

  session_2_source_deep_dive:
    inputs:
      - selected_v1_goal
      - OpenClAW target paths
      - Hermes primitive decisions
    actions:
      - read AGENT_INDEX.md
      - read AGENT_KB_INDEX.md
      - read KB_STARTING_SOURCE_MAP.md
      - inspect relevant per-agent KB folders
      - inspect repo-local hermes-docs for matching Hermes primitives
    outputs:
      - OpenCLAW_to_Hermes_translation_matrix
      - preserve_rewrite_discard_decisions
      - source_conflict_notes

  session_3_minimal_architecture_draft:
    inputs:
      - Q&A answers
      - translation matrix
      - Hermes primitive constraints
    outputs:
      - v1 architecture only
      - profile/skill/Kanban/cron split
      - first three workflows
      - approval gates
      - memory/context placement rules

  session_4_skill_and_workflow_specs:
    inputs:
      - v1 architecture
      - first workflow
    outputs:
      - SKILL.md specs, not necessarily final files
      - trigger descriptions
      - eval cases
      - Kanban card templates
      - recap templates
      - night-shift planning template

  session_5_implementation_plan:
    inputs:
      - approved v1 specs
    outputs:
      - file tree
      - setup order
      - test plan
      - rollback plan
      - GitHub sync plan
```

### Immediate next-session prompt

```markdown
We are designing a Hermes-based personal orchestration system, but we are still in requirements mode.

Use the existing Source Index, Lookup Map, and Q&A Decision Flow.

Task:
1. Ask the operator the First Questions in order.
2. Do not design final architecture yet.
3. After answers, produce:
   - selected_v1_goal
   - first_minimal_reliable_workflow
   - operator_interface_model
   - manual_vs_autonomous_policy
   - initial_profile_vs_skill_vs_delegate decisions
   - OpenCLAW source areas to inspect next
   - unresolved decisions

Important:
- Use Hermes-native primitives first.
- Treat OpenCLAW as supplementary.
- Do not copy OpenCLAW one-to-one.
- Translate OpenCLAW artifacts into skills, profiles, Kanban, cron, tools/plugins, or context files only when the mapping is justified.
```

---

## 6. Assumptions

```yaml
assumptions:
  system_direction:
    primary_runtime: Hermes Agent
    supplementary_source: OpenCLAW / 07_finalopenclawsystem
    goal: personal orchestration system
    method: Q&A-defined requirements before architecture
    architecture_bias: Hermes-native primitives first

  hermes_primitives:
    memory: durable facts and preferences
    skills: reusable procedural knowledge
    profiles: persistent isolated agent roles
    delegation: temporary synchronous subagents
    kanban: durable cross-session orchestration
    cron: scheduled automation
    curator: skill lifecycle maintenance
    plugins_tools: executable capabilities

  openclaw_integration:
    preserve_useful_logic: true
    preserve_everything_as_fixed_constraint: false
    translate_to_hermes_native_forms: true
    conflict_resolution: case_by_case

  repo_findings:
    connected_repo: leela-spec/MasterOfArts
    exact_HermesResearch_folder_found: false
    closest_confirmed_hermes_docs_folder: OpenClaw/07_finalopenclawsystem/docs/hermes-docs
    primary_openclaw_root_confirmed: OpenClaw/07_finalopenclawsystem
    managed_agent_index_confirmed: OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
    managed_kb_index_confirmed: OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md

  first_deliverable:
    not_final_system_architecture: true
    source_index: true
    lookup_map: true
    q_and_a_decision_flow: true
    next_workflow_plan: true
```

---

## 7. Open Questions

### A. Source Authority

1. Is `OpenClaw/07_finalopenclawsystem` always higher authority than `OpenClaw/04_final-system-setup` and `OpenClaw_Setup/migration_payload`?
    
2. Should `managed/knowledge/KB_STARTING_SOURCE_MAP.md` be treated as binding for all OpenCLAW source conflict resolution?
    
3. Does a `docs/HermesResearch` folder exist on another branch or under a different name, or should `docs/hermes-docs` be treated as the correct repo-local Hermes docs folder?
    

### B. System Scope

4. Is v1 a personal assistant, a project orchestration layer, or a night/day planning loop?
    
5. Should v1 include multi-profile Kanban, or begin with a single Orchestrator profile plus skills?
    
6. Should OpenCLAW integration happen in v1, or after the first Hermes-native workflow is stable?
    

### C. Operator Model

7. Is the operator primarily mobile/Telegram-first, terminal-first, or repo/dashboard-first?
    
8. Which actions are allowed without approval?
    
9. Should the system optimize for speed, auditability, or low cognitive load first?
    

### D. Skill Governance

10. Should agent-created skills be active immediately or require review before use?
    
11. Which v1 skills should be pinned from curator archival?
    
12. Should skill evals be required before a skill becomes “canonical”?
    

### E. Memory / Context

13. What exact distinction should the system use between `USER.md`, `MEMORY.md`, `SOUL.md`, `.hermes.md`, and GitHub-backed project files?
    
14. Should session recaps be stored as project files, memory entries, Kanban comments, or all three?
    
15. What information must never be promoted from recap to memory?
    

### F. OpenCLAW Translation

16. Which OpenCLAW agent roles should become Hermes profiles?
    
17. Which OpenCLAW KB files should become Hermes skills?
    
18. Which OpenCLAW workflows are too system-specific and should be rewritten rather than translated?
    
19. Which OpenCLAW verification rules should become quality gates in Hermes?
    
20. What is the minimal OpenCLAW-derived logic needed to improve Hermes orchestration without contaminating Hermes-native architecture?