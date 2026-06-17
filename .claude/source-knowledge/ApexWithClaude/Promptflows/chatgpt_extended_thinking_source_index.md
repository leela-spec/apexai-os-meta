# Source Index / Source Router — ChatGPT Extended-Thinking Apex Alfred File Flow

```yaml
source_index_metadata:
  id: chatgpt-extended-thinking-source-index-v0-2
  paired_prompt_flow: chatgpt_extended_thinking_file_flow.md
  executor: ChatGPT_extended_thinking_mode
  purpose: >
    Tell ChatGPT which uploaded/project sources to inspect for each generated
    Claude-ready file in the one-file-per-task prompt flow.
```

---

# 0. Use rule

This file is not a generated target file. It is the lookup router for the prompt flow.

For each target file, ChatGPT must:

1. Find the target file in section 4.
2. Inspect required sources first.
3. Inspect recommended sources only if needed.
4. Ignore excluded/legacy sources unless the file-specific entry explicitly allows them.
5. Translate historical source terminology into Claude-ready terminology.

---

# 1. Source priority model

```yaml
priority_model:
  P0_binding:
    meaning: Must obey when relevant; overrides older sources.
  P1_primary_design:
    meaning: Main source for file content and current architecture.
  P2_supporting_logic:
    meaning: Use to enrich procedures, examples, or validation details.
  P3_historical_context:
    meaning: Use only to recover intent; do not copy runtime vocabulary.
  P4_excluded_unless_explicit:
    meaning: Do not use unless a target file explicitly requests it.
```

Conflict resolution:

```yaml
conflict_resolution_order:
  1: Current operator instructions in the active chat
  2: chatgpt_extended_thinking_file_flow.md
  3: chatgpt_extended_thinking_source_index.md
  4: Current accepted design-state files and reviews
  5: Claude setup/build-pack preparation files
  6: Uploaded source index files
  7: Historical Hermes/OpenCLAW/Alfred sources
  8: General skill/spec best practices
```

---

# 2. Global source groups

## G0 — Binding prompt-flow controller

```yaml
G0_binding_prompt_flow:
  priority: P0_binding
  sources:
    - Pasted markdown.md
  use_for:
    - fixed_file_sequence
    - allowed_output_paths
    - global_output_contract
    - role_roster
    - file_by_file_requirements
    - one_file_per_prompt discipline
  caution: >
    Original text may speak as if Claude is the author. In this revised flow,
    ChatGPT is the author and Claude is only the later consumer.
```

## G1 — Claude-ready architecture and build-pack preparation

```yaml
G1_claude_ready_architecture:
  priority: P1_primary_design
  sources:
    - Apex Alfred Orchestration Realization in Claude.md
    - Claude Sonnet Build Pack.txt
    - Apex Hermes Build Pack.txt
    - ClaudePhase1FilePreparation.md
    - ClaudeSetupGeneral.md
  use_for:
    - Claude-ready file architecture
    - Claude Code file conventions
    - translation from previous meta-agent/process material into Claude primitives
    - Stage 0 / build-pack logic
    - source-map and understanding-pack concepts
  caution: >
    Some files discuss Claude Sonnet building later. For this flow, ChatGPT
    creates the files now. Use only the file-architecture logic.
```

## G2 — Current Apex / PreCap / FlowRecap design state

```yaml
G2_current_process_design_state:
  priority: P1_primary_design
  sources:
    - Information Process Architecture.txt
    - Routine Design Spec — PreCapNextDay v0.2_Review.md
    - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
    - Support Design Spec — ModelSubscriptionUsageTracking v0.1_Review.md
    - Routine Design Spec — AllProjectStatusPacketUpdate v0.1_REVIEW.md
    - PreCap Week v0.2.md
    - PreCapNextDay_v1.md
    - PreCapNextDay_Routine_Family_v0_1.md
    - Process Specs Validation.txt
    - Process Handover Validation.txt
  use_for:
    - current core loop
    - accepted removal of DayExecution / FlowExecution as standalone processes
    - FlowRecap as atomic execution-memory layer
    - APSU/status-merge logic
    - prompt routing and model usage requirements
    - artifact/validation lessons
  caution: >
    These are source logic, not the target file set. Do not create these process
    specs as runtime files in this flow.
```

## G3 — Uploaded source indexes

```yaml
G3_source_indexes:
  priority: P1_primary_design
  sources:
    - SourceIndexAgentInteraction07OC.md
    - SourceIndexAgentInteractionAlfred.md
    - SourceIndexProjectGPT.md
    - Source Index for Hermes AI.txt
  use_for:
    - deciding where to search
    - understanding which source family controls which topic
    - identifying OpenCLAW workflow-bearing files
    - identifying Alfred KB / interaction workflow files
    - avoiding unfocused source scans
  caution: >
    Source indexes point to historical/local files. Use them for routing and
    conceptual content, not as final output paths.
```

## G4 — Role/orchestration decision sources

```yaml
G4_role_and_orchestration_decisions:
  priority: P1_primary_design
  sources:
    - apex_hermes_orchestration_decisions_v0_1.md
    - Q&A_ProfileVsAgents.md
    - Q&A_SwarmOrchestration.md
    - Q&AAgent2Workflows.md
    - Q&A_ProcessBlueprintDefinition.md
    - Q&AWorkflowsWithExamples.md
    - Process Definition Workflow.txt
  use_for:
    - Alfred plus three meta-heads architecture
    - role vs skill vs workflow distinction
    - anti-agent-sprawl rules
    - handoff and process vocabulary
    - deciding whether something belongs in agent, skill, or workflow file
  caution: >
    Many sources are Hermes-oriented. Translate into Claude-ready role, skill,
    and workflow language.
```

## G5 — Skill specification and skill-quality sources

```yaml
G5_skill_quality_sources:
  priority: P1_primary_design
  sources:
    - SkillSpecification.md
    - SkillCreationBestPractice.md
    - OptimizingSkillDescriptions.md
    - EvaluatingSkills.md
    - SkillsTraining&Examples_Claude.md
    - WorkflowExamples_Claude.md
  use_for:
    - SKILL.md structure
    - frontmatter fields
    - trigger description quality
    - eval/quality considerations
    - reusable procedure structure
    - skill boundary writing
  caution: >
    Use the open Agent Skills format where useful, but keep target paths under
    `.claude/skills/<name>/SKILL.md`.
```

## G6 — OpenCLAW workflow and handoff logic

```yaml
G6_openclaw_historical_workflow_logic:
  priority: P2_supporting_logic
  sources:
    - SourceIndexAgentInteraction07OC.md
  referenced_workflow_surfaces:
    - PROCESS_BLUEPRINT_SYSTEM.md
    - PROJECT_ROUTING.md
    - HOLDING_ORCHESTRATION_FLOW.md
    - AGENT_HANDOFF_CONTRACTS.md
    - DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md
    - BOOTSTRAP.md
    - CHECKLISTS.md
  use_for:
    - handoff discipline
    - routing logic
    - validation bands
    - source alignment
    - process authority concepts
    - no-drift validation practices
  caution: >
    Do not copy OpenCLAW agent names, runtime assumptions, or file paths into
    generated Claude files unless translated into the four-role Apex Alfred model.
```

## G7 — Alfred KB / operator-facing workflow logic

```yaml
G7_alfred_historical_workflow_logic:
  priority: P2_supporting_logic
  sources:
    - SourceIndexAgentInteractionAlfred.md
  referenced_workflow_surfaces:
    - PromptFlowToCreateKB4Alfred2.md
    - NewPromptPlan.md
    - NewPromptFlow2.md
    - NewIntegration.md
    - PromptFLowValidation.md
    - promptflowChatHistory4Validation.md
    - ChatHistorxSoFar.md
  use_for:
    - Alfred as operator-facing layer
    - intake/routing habits
    - single-file write/verify routines
    - KB consolidation lessons
    - validation prompt-flow lessons
  caution: >
    Use as source logic for Alfred role and intake/handoff workflows, not as
    target KB structure.
```

## G8 — Hermes/runtime background sources

```yaml
G8_hermes_background_only:
  priority: P3_historical_context
  sources:
    - Hermes Agent - Development Guide.md
    - HermesAgentMasterClass.md
    - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
    - HermesAgentDeepDive.md
    - FromZeroToUltimateHermes_NateHerk.md
    - Hermes_Agent_Zero_to_Personal_AI_Assistant_structured_extraction.md
    - TrainingHermes_claude.md
    - TryofTrainersbutFail.md
    - Skill Usage Tracking and Backup.md
    - SkillCuratorArchitecture.md
    - Skills Management and Security.md
    - kanban-orchestrator_skill.md
  use_for:
    - historical reasoning behind skills over agents
    - warnings against runtime overbuild
    - validation and curator concepts as abstract lessons
  do_not_use_for:
    - target runtime claims
    - Hermes profile files
    - Hermes cron files
    - Hermes Kanban task graphs
    - SOUL.md
    - AGENTS.md
```

---

# 3. Global file-family routing

```yaml
file_family_routing:
  CLAUDE_root_file:
    primary_groups: [G0_binding_prompt_flow, G1_claude_ready_architecture, G4_role_and_orchestration_decisions]
    secondary_groups: [G2_current_process_design_state, G3_source_indexes]

  agent_role_files:
    primary_groups: [G0_binding_prompt_flow, G4_role_and_orchestration_decisions, G7_alfred_historical_workflow_logic]
    secondary_groups: [G1_claude_ready_architecture, G6_openclaw_historical_workflow_logic]

  skill_files:
    primary_groups: [G0_binding_prompt_flow, G5_skill_quality_sources, G4_role_and_orchestration_decisions]
    secondary_groups: [G6_openclaw_historical_workflow_logic, G7_alfred_historical_workflow_logic, G2_current_process_design_state]

  workflow_files:
    primary_groups: [G0_binding_prompt_flow, G4_role_and_orchestration_decisions, G6_openclaw_historical_workflow_logic, G7_alfred_historical_workflow_logic]
    secondary_groups: [G2_current_process_design_state, G5_skill_quality_sources]
```

---

# 4. Per-target source routing

## 1. `CLAUDE.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G1_claude_ready_architecture
    - G4_role_and_orchestration_decisions
  recommended_groups:
    - G2_current_process_design_state
    - G3_source_indexes
  extract:
    - mission
    - allowed file families
    - four permanent roles
    - Claude-only translation boundary
    - anti-sprawl rules
    - validation-before-completion principle
    - out-of-scope list
  avoid:
    - Hermes runtime mechanics
    - SOUL.md / AGENTS.md creation
    - implementation commands
```

## 2. `.claude/agents/alfred.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G7_alfred_historical_workflow_logic
    - G4_role_and_orchestration_decisions
  recommended_groups:
    - G1_claude_ready_architecture
    - G6_openclaw_historical_workflow_logic
  extract:
    - operator-facing intake
    - clarification behavior
    - handoff packet creation
    - routing to meta roles
    - non-implementation boundary
    - no-final-validation boundary
```

## 3. `.claude/agents/meta_strategist.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G6_openclaw_historical_workflow_logic
  recommended_groups:
    - G2_current_process_design_state
  extract:
    - goal interpretation
    - priority ranking
    - dependency mapping
    - sequencing
    - risk framing
    - escalation of contradictions
```

## 4. `.claude/agents/meta_operations.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G1_claude_ready_architecture
  recommended_groups:
    - G2_current_process_design_state
    - G7_alfred_historical_workflow_logic
  extract:
    - workflow/spec packaging
    - one-file-per-step discipline
    - skill spec conversion
    - implementation-ready file content production
    - handoff compatibility
    - strategy-respecting boundary
```

## 5. `.claude/agents/meta_detective_controller.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G6_openclaw_historical_workflow_logic
  recommended_groups:
    - G2_current_process_design_state
    - G5_skill_quality_sources
  extract:
    - validation gate behavior
    - contradiction detection
    - source drift detection
    - completion criteria verification
    - veto and correction reports
```

## 6. `.claude/skills/alfred-intake-router/SKILL.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G7_alfred_historical_workflow_logic
    - G5_skill_quality_sources
  recommended_groups:
    - G4_role_and_orchestration_decisions
    - G6_openclaw_historical_workflow_logic
  extract:
    - intake classification
    - ambiguity detection
    - route decision
    - handoff packet production
    - next-action definition
    - SKILL.md trigger description style
```

## 7. `.claude/skills/handoff-packet-writer/SKILL.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G6_openclaw_historical_workflow_logic
    - G5_skill_quality_sources
  recommended_groups:
    - G7_alfred_historical_workflow_logic
    - G4_role_and_orchestration_decisions
  extract:
    - handoff packet fields
    - bounded ownership
    - acceptance criteria rules
    - no hidden assumptions
    - validation_required logic
```

## 8. `.claude/skills/source-constraint-map/SKILL.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G3_source_indexes
    - G5_skill_quality_sources
  recommended_groups:
    - G6_openclaw_historical_workflow_logic
    - G2_current_process_design_state
  extract:
    - source priority mapping
    - fact/assumption/constraint/gap separation
    - conflict controller rules
    - compact source-constraint table
```

## 9. `.claude/skills/goal-skeleton-fill-verify-loop/SKILL.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G5_skill_quality_sources
    - G6_openclaw_historical_workflow_logic
  recommended_groups:
    - G2_current_process_design_state
    - G7_alfred_historical_workflow_logic
  extract:
    - serious-output creation loop
    - skeleton-first discipline
    - verification-before-completion
    - revision loop
    - learning capture as public summary, not chain of thought
```

## 10. `.claude/skills/detective-validation-gate/SKILL.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G6_openclaw_historical_workflow_logic
    - G5_skill_quality_sources
  recommended_groups:
    - G2_current_process_design_state
  extract:
    - PASS/FAIL validation
    - blocking vs non-blocking issues
    - correction report format
    - role boundary checks
    - one-file-only checks
    - Claude-only scope checks
```

## 11. `.claude/skills/workflow-normalizer/SKILL.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G6_openclaw_historical_workflow_logic
    - G7_alfred_historical_workflow_logic
    - G5_skill_quality_sources
  recommended_groups:
    - G2_current_process_design_state
  extract:
    - messy chat/source to workflow spec transformation
    - trigger/role/input/sequence/output/gate/failure handling
    - workflow spec not executable code
```

## 12. `.claude/workflows/intake_to_handoff.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G7_alfred_historical_workflow_logic
    - G4_role_and_orchestration_decisions
  recommended_groups:
    - G6_openclaw_historical_workflow_logic
  extract:
    - operator request intake
    - classification
    - clarification or proceed logic
    - target role selection
    - handoff packet completeness validation
```

## 13. `.claude/workflows/handoff_to_strategy.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G6_openclaw_historical_workflow_logic
  recommended_groups:
    - G2_current_process_design_state
  extract:
    - handoff to goal map
    - constraint map
    - priority rank
    - dependency map
    - strategic consistency validation
```

## 14. `.claude/workflows/strategy_to_operations.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G1_claude_ready_architecture
  recommended_groups:
    - G2_current_process_design_state
    - G7_alfred_historical_workflow_logic
  extract:
    - strategy packet to file/action plan
    - file target identification
    - operational sequence
    - one-file-per-step packaging
    - validation gate definition
```

## 15. `.claude/workflows/operations_to_detective_validation.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G6_openclaw_historical_workflow_logic
  recommended_groups:
    - G5_skill_quality_sources
  extract:
    - output validation workflow
    - packet compliance
    - role boundary checks
    - Claude-only scope check
    - approve/reject report
```

## 16. `.claude/workflows/validated_file_creation_loop.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G1_claude_ready_architecture
    - G7_alfred_historical_workflow_logic
  recommended_groups:
    - G6_openclaw_historical_workflow_logic
    - G5_skill_quality_sources
  extract:
    - fixed sequence rule
    - exactly one file per prompt
    - no side files
    - validation checklist
    - next prompt emission
    - final stop condition
    - failure behavior
```

## 17. `.claude/workflows/workflow_index.md`

```yaml
source_routing:
  required_groups:
    - G0_binding_prompt_flow
    - G4_role_and_orchestration_decisions
    - G1_claude_ready_architecture
  recommended_groups:
    - G3_source_indexes
    - G5_skill_quality_sources
  extract:
    - workflow table
    - trigger per workflow
    - roles used
    - inputs/outputs
    - validation gate
    - relationship to agents and skills
```

---

# 5. Search discipline

```yaml
search_discipline:
  default:
    - Search target-specific required groups only.
    - Prefer source-index summaries before opening large historical files.
    - Use exact target names, role names, and process names as search terms.
    - Stop searching when enough source evidence exists to produce the target file.

  avoid:
    - reading every uploaded file for every target file
    - importing Hermes runtime vocabulary into Claude-ready files
    - expanding the target file beyond its purpose
    - creating future implementation work prematurely
```

---

# 6. Current accepted design facts to preserve

```yaml
accepted_design_facts:
  authoring_agent: ChatGPT_extended_thinking_mode
  later_consumer: Claude_or_Claude_Code
  target_file_set: Claude_ready_predefinition_files
  stable_roles:
    - alfred
    - meta_strategist
    - meta_operations
    - meta_detective_controller
  core_loop_source_logic:
    - PreCapWeek
    - PreCapNextDay
    - OperatorExecutesPlannedFlow
    - FlowRecapSkill_or_flow_recap
    - AllProjectStatusPacketUpdate_or_status_merge
    - next_PreCapNextDay
  removed_from_core_source_logic:
    - DayExecution_as_standalone_process
    - FlowExecution_as_standalone_process
    - required_RecapDay
  daily_flow_source_logic:
    - F1_Leela
    - F2_MasterOfArts
    - F3_Apex_orchestration
    - F4_Residual
  universal_flow_anatomy_source_logic:
    - sprint_1_work_chunk
    - sprint_2_work_chunk_or_iteration
    - sprint_3_recap_planning_digest
```

Use these facts only when relevant. Do not force PreCap-specific content into generic root/agent files unless it clarifies system purpose.
