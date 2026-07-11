# Apex/Hermes Claude  Build Pack — Macro Document v0.1

Source grounding: user task requirements and required structure are taken from the pasted macro-build instruction. Current Stage 0 build-pack logic, accepted architecture, and artifact-contract emphasis are grounded in the prior Claude  Build Pack handover. Current information-process architecture, core loop, removed models, FlowRecap/APSU contracts, and runtime-blocking variables are grounded in the latest information-process architecture document.

## 0. Document Control

```yaml
document:
  id: apex-hermes-claude--build-pack-macro-v0-1
  status: macro_build_pack_for_claude_
  implementation_status: not_runtime_implementation
  output_type: single_markdown_document
  audience: Claude  via Claude Code
  purpose: >
    Prepare Claude  to understand the Apex/Hermes orchestration system
    and later create the actual file pack safely.

scope:
  included:
    - macro system intent
    - source map
    - compact decision register
    - macro artifact contract registry
    - proposed target file tree
    - blocking build questions
    - draft Claude  build prompt
    - acceptance checks
    - forbidden actions
  excluded:
    - actual Hermes runtime implementation
    - actual SOUL.md files
    - actual SKILL.md files
    - actual cron jobs
    - actual Kanban task graphs
    - profile installation
    - secret handling
    - install commands

source_citations:
  pasted_task_prompt: "turn2file0"
  stage_0_build_pack_handover: "turn2file1"
  information_process_architecture: "turn2file2"

status_flags:
  design_first: true
  runtime_translation_ready: false
  file_tree_verified_against_local_repo: false
  absolute_paths_resolved: false
  profiles_installed: false
  skills_installed: false
  cron_enabled: false
  kanban_graphs_created: false
```

---

## 1. 00_SYSTEM_INTENT.md

```yaml
file_chapter:
  intended_future_file: 00_SYSTEM_INTENT.md
  chapter_role: compact_system_understanding
  implementation_status: macro_only_not_final_file

system_intent:
  project_name: Apex/Hermes personal AI orchestration system

  what_is_being_built: >
    A personal orchestration layer that helps the operator plan projects,
    prepare daily and weekly execution flows, route work across AI surfaces,
    recap completed flows, update project status packets, and eventually
    translate stable procedures into Hermes-compatible skills, profiles,
    Kanban routines, and cron-triggered processes.

  target_runtime: Hermes Agent

  why_Hermes:
    - supports persistent profiles, memory, skills, cron, delegation, Kanban, gateway usage, and local/runtime automation surfaces
    - fits the desired orchestration/runtime layer better than a pure chat interface
    - can preserve repeatable procedures as skill-like files rather than relying only on conversation memory
    - can later run scheduled triggers and durable multi-profile task graphs

  build_executor: Claude  via Claude Code

  why_Claude__Claude_Code:
    - can inspect local filesystem and repository state
    - can create draft Markdown files and structured folders
    - can compare design specs against actual repo contents
    - can generate and patch build-pack files before anything is installed into Hermes runtime

  operator_role:
    name: human_CEO_operator
    responsibilities:
      - decide priorities
      - approve or correct plans
      - execute planned flows manually when needed
      - provide raw flow dumps
      - validate FlowRecap next-step proposals
      - approve runtime activation

canonical_architecture:
  alfred:
    type: Hermes_profile_candidate
    role: operator-facing interface
    responsibilities:
      - intake
      - operator clarification
      - daily/weekly review surface
      - human gate management
      - presentation of plans and recaps

  meta_strategist:
    type: Hermes_profile_candidate
    role: strategy, prioritization, leverage, direction
    responsibilities:
      - strategic validation
      - priority tradeoff review
      - leverage assessment
      - long-horizon direction checks

  meta_operations:
    type: Hermes_profile_candidate
    role: process orchestration, routing, artifact creation, build coordination
    responsibilities:
      - build-pack coordination
      - artifact creation
      - process routing
      - prompt and AI routing
      - later Kanban graph ownership where appropriate

  meta_detective_controller:
    type: Hermes_profile_candidate
    role: verification, drift detection, quality control, safety gates
    responsibilities:
      - detect mismatches
      - validate artifact contracts
      - catch deprecated model revival
      - verify runtime-readiness before activation

profile_policy:
  rule: >
    Profiles are durable identity/runtime boundaries, not names for every
    function or workflow.
  create_profile_only_when:
    - isolated identity is needed
    - separate memory is needed
    - separate permissions/toolsets are needed
    - separate model/provider selection is needed
    - durable queue ownership is needed
    - long-running department-head behavior is needed

skill_policy:
  rule: >
    Most repeatable procedures should become skills or skill candidates before
    becoming profiles or plugins.
  examples:
    - flow-recap
    - precap-next-day
    - status-merge
    - prompt-and-ai-routing-planning
    - model-usage-log
    - precap-week

accepted_core_loop:
  - PreCapWeek
  - PreCapNextDay
  - OperatorExecutesPlannedFlow
  - FlowRecapSkill_or_flow-recap
  - AllProjectStatusPacketUpdate_or_status-merge_APSU
  - next_PreCapNextDay

deprecated_from_core:
  - DayExecution_as_standalone_process
  - FlowExecution_as_standalone_process
  - DayExecutionController_as_standalone_process
  - RecapDay_as_required_project_state_layer

optional_later:
  RecapDay:
    role: Alfred_or_personal_evening_reflection_layer
    status: deferred_not_core_project_state_loop

design_first_status:
  current_phase: macro_build_pack_before_runtime_translation
  runtime_translation_blocked_until:
    - actual repo root is inspected
    - artifact paths are resolved
    - profile draft scope is approved
    - skill draft scope is approved
    - Kanban/cron automation timing is approved
    - AI_surface_inventory storage is chosen

light_processual_reasoning_default:
  use_as: compact_file_creation_check_not_standalone_theory
  before_each_future_file:
    goal: What is this file/artifact supposed to enable?
    sources: Which project resources and accepted decisions constrain it?
    skeleton: What sections are needed before filling content?
    fill: What concrete content belongs in each section?
    verify: Does it preserve accepted decisions and avoid deprecated models?
    next_step: What should Claude  do after this exists?
```

---

## 2. 01_SOURCE_MAP.md

```yaml
file_chapter:
  intended_future_file: 01_SOURCE_MAP.md
  chapter_role: source_navigation_and_authority_map
  implementation_status: macro_only_not_final_file

source_map:
  - source_name_or_category: Hermes runtime / official docs
    source_type: official_or_primary_Hermes_reference
    examples:
      - llms.txt
      - Hermes Agent - Development Guide.md
      - Hermes official docs if locally mirrored or accessible
    what_it_contains:
      - installation surfaces
      - CLI/TUI/gateway concepts
      - profile-aware paths
      - config and environment behavior
      - runtime constraints
      - toolsets
      - cron
      - Kanban
      - skills
      - memory
      - sessions
    when_to_use:
      - deciding actual Hermes runtime behavior
      - checking whether a planned artifact maps to a real Hermes primitive
      - verifying profile, skill, Kanban, cron, and toolset claims
    authority_level: P0_for_Hermes_runtime_claims
    caution: >
      Do not infer runtime behavior from Apex design specs when official Hermes
      sources contradict or constrain them.

  - source_name_or_category: Hermes skill/profile/Kanban docs
    source_type: Hermes_native_mechanism_reference
    examples:
      - Q&A_ProfileVsAgents.md
      - Q&A_SwarmOrchestration.md
      - kanban-orchestrator_skill.md
      - SkillSpecification.md
      - SkillCreationBestPractice.md
      - SkillsTraining&Examples_Claude.md
      - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
      - HermesAgentDeepDive.md
      - TrainingHermes_claude.md
    what_it_contains:
      - profile vs agent distinction
      - skill format and triggering logic
      - Kanban/delegation decision rules
      - curator and skill lifecycle concepts
      - skill creation best practices
      - warnings against plugin/tool overuse
    when_to_use:
      - mapping a repeatable process to skill/profile/delegate_task/Kanban/cron
      - drafting future SKILL.md candidates
      - deciding when a process needs durable multi-profile orchestration
    authority_level: P0_to_P1
    caution: >
      Some files are prior analyses or community-derived summaries. Verify
      final runtime claims against official Hermes docs or local repo code.

  - source_name_or_category: Apex/Hermes decision records
    source_type: project_decision_state
    examples:
      - apex_hermes_orchestration_decisions_v0_1.md
      - Process Handover Validation outputs
      - Process Specs Validation outputs
      - Claude  Build Pack.txt
    what_it_contains:
      - accepted architecture
      - locked and deprecated process models
      - profile boundaries
      - workflow-to-Hermes primitive decisions
      - build sequencing
    when_to_use:
      - preventing reopened decisions
      - checking whether a model has already been deprecated
      - generating decision register
    authority_level: P0_for_project_decisions
    caution: >
      Use newest accepted decisions over older specs. Older files may still
      contain deprecated DayExecution/FlowExecution/RecapDay core assumptions.

  - source_name_or_category: PreCap / FlowRecap / APSU process specs
    source_type: design_layer_process_specs
    examples:
      - Process Spec — PreCap / FlowRecap / Status-Merge Information Loop
      - Information Process Architecture.txt
      - Macro info file flow
      - PreCap Week v0.2.md
      - PreCapNextDay_v1.md
      - Routine Design Spec — PreCapNextDay v0.2_Review.md
      - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
      - Routine Design Spec — AllProjectStatusPacketUpdate v0.1_REVIEW.md
      - Support Design Spec — ModelSubscriptionUsageTracking v0.1_Review.md
    what_it_contains:
      - current operating loop
      - artifact handoffs
      - FlowRecapSkill purpose
      - APSU/status-merge purpose
      - prompt routing support logic
      - model usage tracking assumptions
      - unresolved schema and path issues
    when_to_use:
      - defining artifact contracts
      - drafting future skill candidates
      - testing flow examples
      - deriving build questions
    authority_level: P0_for_current_design_logic
    caution: >
      These are not runtime files. They do not prove that SKILL.md files,
      profiles, cron jobs, or Kanban graphs already exist.

  - source_name_or_category: validation/review notes
    source_type: external_or_internal_quality_review
    examples:
      - Routine Design Spec — PreCapNextDay v0.2_Review.md
      - Routine Design Spec — AllProjectStatusPacketUpdate v0.1_REVIEW.md
      - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
      - Support Design Spec — ModelSubscriptionUsageTracking v0.1_Review.md
      - Process Specs Validation.txt
    what_it_contains:
      - runtime ambiguity flags
      - schema contradiction flags
      - missing storage questions
      - cron/Kanban warnings
      - profile/toolset ownership concerns
    when_to_use:
      - before converting design specs into runtime drafts
      - when generating blocking questions
      - when building acceptance checks
    authority_level: P0_for_known_gaps
    caution: >
      Treat review notes as constraints and questions, not as final runtime
      architecture.

  - source_name_or_category: Master of Arts workflow examples
    source_type: project_specific_example_domain
    examples:
      - Master of Arts workflow/example database if present
      - ProcessRanking_GPT&MasterOA.md if present
      - Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1.md if present
    what_it_contains:
      - concrete project examples
      - workflow candidates
      - process portfolio examples
      - website/content/design handoff patterns
    when_to_use:
      - testing whether generic artifact contracts work for real project flows
      - validating F2_MasterOfArts flow examples
    authority_level: P1_for_examples
    caution: >
      Do not generalize Master of Arts-specific process logic into global
      Hermes runtime rules without explicit decision.

  - source_name_or_category: process ranking / process portfolio
    source_type: process_prioritization_reference
    examples:
      - ProcessRanking_GPT&MasterOA.md
      - workflow/process catalogue materials
    what_it_contains:
      - candidate process importance
      - which routines should be built first
      - example prioritization logic
    when_to_use:
      - ordering future skill drafts
      - deciding which process gets implementation attention first
    authority_level: P1
    caution: >
      Ranking files guide priority, not runtime mechanism.

  - source_name_or_category: Claude Code / adapter layer notes
    source_type: cross_runtime_adapter_reference
    examples:
      - Hermes Installer Issue.txt
      - Q&AAgent2Workflows.md
      - Claude  Build Pack.txt
      - Claude/Hermes adapter discussions
    what_it_contains:
      - one-repo/shared-source concept
      - Claude Code as build executor
      - Hermes as orchestration runtime
      - adapter layer cautions
      - SKILL.md portability boundary
    when_to_use:
      - deciding what Claude Code should build first
      - separating portable Markdown/skill layer from non-portable runtime layer
      - designing repo-based build pack
    authority_level: P1_for_build_strategy
    caution: >
      Do not assume Claude Code and Hermes share runtime semantics. The shared
      layer is specs/Markdown/SKILL.md drafts, not profiles, hooks, cron,
      Kanban, permissions, or memory.

source_authority_order:
  1: explicit_latest_user_decisions
  2: latest_Apex_Hermes_decision_records
  3: official_Hermes_docs_or_local_Hermes_repo_code
  4: latest_design_specs_and_reviews
  5: examples_and_prior_artifacts
  6: older_or_deprecated_process_specs

source_handling_rules:
  - distinguish_design_layer_from_runtime_layer
  - mark unverified files as design_only
  - never treat a proposed file tree as an existing repo tree
  - never treat a future SKILL.md candidate as installed Hermes skill
  - prefer latest corrected loop over older PreCapNextDay family assumptions
```

---

## 3. 02_DECISION_REGISTER.md

```yaml
file_chapter:
  intended_future_file: 02_DECISION_REGISTER.md
  chapter_role: locked_decisions_and_deprecation_barrier
  implementation_status: macro_only_not_final_file

locked_decisions:
  architecture:
    - decision: architecture_uses_Alfred_plus_three_meta_heads
      meaning: >
        The system has Alfred as operator-facing interface and three durable
        meta-head candidates: meta_strategist, meta_operations,
        meta_detective_controller.
      status: locked_for_current_build_pack

    - decision: do_not_create_large_agent_swarm_first
      meaning: >
        Most named workflows are not agents. They become skills, routines,
        support processes, prompt packets, Kanban graphs, or cron triggers.
      status: locked_for_current_build_pack

  Hermes_mechanism_mapping:
    - decision: repeatable_procedures_should_usually_become_skills
      status: locked
      examples:
        - flow-recap
        - prompt-and-ai-routing-planning
        - status-merge
        - model-usage-log

    - decision: profiles_are_durable_identity_runtime_boundaries
      status: locked
      implication: >
        Do not create a profile for every task, function, workflow, or process
        name.

    - decision: Kanban_reserved_for_durable_multi_profile_audit_or_human_gate_work
      status: locked
      implication: >
        Use Kanban when work needs durability, multiple profiles, audit trail,
        human interjection, parallel fan-out, or review loops.

    - decision: delegate_task_for_short_lived_synchronous_subwork
      status: locked
      implication: >
        Use delegation for bounded reasoning-heavy or specialist subwork where
        the caller needs the result inside the current session.

    - decision: cron_for_scheduled_triggers_not_direct_heavy_synthesis_v0_1
      status: locked
      implication: >
        In v0.1, cron may later trigger lightweight checks or create Kanban
        work, but should not directly perform heavy planning synthesis.

  artifact_policy:
    - decision: artifacts_are_real_markdown_or_file_like_artifacts
      status: locked
      implication: >
        Planning packets, recaps, registries, and status packets should be
        durable files or structured Markdown/YAML blocks.

    - decision: do_not_store_large_structured_artifacts_in_MEMORY_md
      status: locked
      implication: >
        MEMORY.md is not the storage layer for flow recaps, plans, status
        packets, or large registries.

    - decision: runtime_phase_must_resolve_absolute_paths
      status: locked
      implication: >
        This macro document uses logical slots and proposed paths only.

  process_loop:
    - decision: current_core_loop
      status: locked
      value:
        - PreCapWeek
        - PreCapNextDay
        - OperatorExecutesPlannedFlow
        - FlowRecapSkill_or_flow-recap
        - AllProjectStatusPacketUpdate_or_status-merge_APSU
        - next_PreCapNextDay

    - decision: FlowRecapSkill_should_become_Hermes_skill_candidate
      likely_runtime_name: flow-recap
      status: locked
      implication: >
        Treat FlowRecapSkill as a future SKILL.md procedure, not as a callable
        function.

    - decision: FlowRecapSkill_is_atomic_execution_memory_unit
      status: locked
      outputs:
        - structured_flow_recap
        - project_status_delta
        - artifact_index
        - model_usage_delta
        - operator_validated_next_step
        - context_for_future_PreCapNextDay

    - decision: APSU_status_merge_runs_once_daily_or_manually
      status: locked
      implication: >
        APSU/status-merge does not run automatically after every FlowRecap.

    - decision: APSU_writes_next_PreCapNextDay_context_first
      status: locked_for_v0_1
      implication: >
        APSU should publish next_PreCapNextDay_input_context before any later
        auto-triggering mechanism is implemented.

    - decision: APSU_auto_trigger_PreCapNextDay_deferred
      status: locked_for_v0_1
      implication: >
        In first implementation pass, prefer manual/operator-triggered
        PreCapNextDay from updated context. Later automation may create a
        Kanban task, not recursive cron.

  processual_thinking:
    - decision: processual_thinking_is_support_layer_not_build_phase
      status: locked
      implication: >
        Use goal/sources/skeleton/fill/verify/next_step as a compact reasoning
        default inside file drafting. Do not create a process-kernel library.

deprecated:
  - item: DayExecution_standalone_process
    replacement: OperatorExecutesPlannedFlow_as_human_SOP_boundary_plus_FlowRecapSkill
    status: deprecated_from_core

  - item: FlowExecution_standalone_process
    replacement: operator_executes_flow_from_PreCapNextDay_flow_packet
    status: deprecated_from_core

  - item: DayExecutionController_as_standalone_process
    replacement: PreCapNextDay_outputs_executable_flow_packets
    status: deprecated_from_core

  - item: required_RecapDay_core_loop
    replacement: optional_later_Alfred_personal_reflection_layer
    status: deprecated_from_current_project_state_loop

  - item: creating_many_agents_or_profiles_for_every_workflow
    replacement: skills_routines_Kanban_or_delegation_based_on_mechanism_decision
    status: deprecated

  - item: treating_workflow_as_Hermes_runtime_primitive
    replacement: skill_or_Kanban_task_graph_or_cron_or_delegate_task
    status: deprecated

  - item: treating_FlowRecapSkill_as_callable_function
    replacement: future_SKILL_md_procedure_named_flow_recap
    status: deprecated

  - item: using_MEMORY_md_for_large_structured_artifacts
    replacement: markdown_or_yaml_file_like_artifacts
    status: deprecated

  - item: direct_heavy_cron_synthesis_in_v0_1
    replacement: manual_first_or_cron_creates_Kanban_task_later
    status: deprecated

decision_review_rule:
  Claude__must:
    - preserve locked decisions unless operator explicitly changes them
    - flag conflicts with older files
    - cite or report source conflict before changing architecture
    - never silently revive deprecated models
```

---

## 4. 03_ARTIFACT_CONTRACT_REGISTRY.md

```yaml
file_chapter:
  intended_future_file: 03_ARTIFACT_CONTRACT_REGISTRY.md
  chapter_role: macro_artifact_registry
  implementation_status: macro_contracts_only_not_full_schemas

artifact_rule:
  - artifacts are real files or file-like Markdown/YAML blocks
  - do not store large structured artifacts in MEMORY.md
  - runtime phase must later resolve absolute paths
  - every artifact should have a primary producer
  - every artifact should have at least one consumer
  - every artifact needs missing-input behavior before runtime translation
  - logical paths are allowed now; absolute paths are CHECK_LATER

registry_field_template:
  artifact_id: string
  artifact_name: string
  producer: process_or_operator
  consumer:
    - process_or_operator
  purpose: string
  format: markdown_with_yaml_blocks_or_yaml_block_or_freeform_then_normalized
  lifecycle_position: string
  required_later_detail:
    - storage_path
    - minimal_schema
    - validation_rule
    - missing_input_behavior
    - example

artifacts:
  - artifact_id: A01
    artifact_name: weekly_plan_packet
    producer: PreCapWeek
    consumer:
      - PreCapNextDay
      - PreCapWeek_archive_or_review
    purpose: >
      Carries weekly priorities, project allocations, calendar constraints,
      and first execution-day planning context into daily planning.
    format: markdown_with_yaml_blocks
    lifecycle_position: weekly_planning_to_daily_planning
    required_later_detail:
      - week_id_schema
      - day_by_day_direction_schema
      - project_allocation_schema
      - first_PreCapNextDay_context_schema
      - logical_storage_slot

  - artifact_id: A02
    artifact_name: next_day_plan
    producer: PreCapNextDay
    consumer:
      - Operator
      - FlowRecapSkill_indirectly
      - APSU_indirectly
      - future_calendar_block_creation
    purpose: >
      Provides the full executable plan for one intended execution day,
      including four flow packets, routing instructions, context instructions,
      and recap requirements.
    format: markdown_with_yaml_blocks
    lifecycle_position: daily_planning_to_operator_execution
    required_later_detail:
      - execution_day_id_schema
      - review_status_schema
      - four_flow_sequence_schema
      - calendar_feasibility_schema
      - storage_path

  - artifact_id: A03
    artifact_name: flow_packet
    producer: PreCapNextDay
    consumer:
      - Operator
      - FlowRecapSkill
      - APSU_indirectly
    purpose: >
      Defines one executable flow with project, goal, three sprints, prompt
      packets, context instructions, expected outputs, and recap capture rules.
    format: markdown_section_or_extractable_markdown_file_with_yaml_blocks
    lifecycle_position: daily_plan_to_flow_execution_to_flow_recap
    required_later_detail:
      - flow_id_schema
      - fixed_position_schema
      - sprint_schema
      - extractable_storage_rule
      - residual_flow_split_rule

  - artifact_id: A04
    artifact_name: prompt_packet
    producer:
      - PreCapNextDay
      - PromptAndAIRoutingPlanning
    consumer:
      - Operator
      - FlowRecapSkill
      - ModelSubscriptionUsageTracking
    purpose: >
      Defines one promptable task with AI surface/model/mode recommendation,
      context to include, expected output, fallback route, and usage tracking
      requirement.
    format: embedded_yaml_block_inside_flow_packet_or_extractable_section
    lifecycle_position: flow_planning_to_prompt_execution_to_recap
    required_later_detail:
      - prompt_packet_id_schema
      - AI_surface_fields
      - expected_output_contract
      - output_capture_instruction
      - actual_usage_delta_link

  - artifact_id: A05
    artifact_name: context_instructions
    producer:
      - PreCapNextDay
      - PromptAndAIRoutingPlanning
    consumer:
      - Operator
      - Claude_or_other_AI_surface_used_by_operator
      - FlowRecapSkill_indirectly
    purpose: >
      Tells the operator which source material, files, prior outputs, or
      context packets should be included when executing a prompt packet.
    format: embedded_markdown_or_yaml_block_inside_flow_packet
    lifecycle_position: prompt_preparation
    required_later_detail:
      - context_source_types
      - file_upload_manifest_schema
      - paste_context_schema
      - missing_context_behavior

  - artifact_id: A06
    artifact_name: raw_flow_dump
    producer: Operator
    consumer:
      - FlowRecapSkill
    purpose: >
      Captures messy or semi-structured evidence from an executed flow:
      chat logs, outputs, artifacts, notes, decisions, blockers, usage notes,
      and suspected next steps.
    format: freeform_markdown_normalized_to_one_file_per_flow
    lifecycle_position: after_operator_executes_flow_before_FlowRecap
    required_later_detail:
      - raw_dump_minimum_fields
      - normalization_rule
      - accepted_input_forms
      - storage_path
      - validation_before_FlowRecap

  - artifact_id: A07
    artifact_name: skipped_flow_marker
    producer:
      - Operator
      - FlowRecapSkill
      - APSU
    consumer:
      - APSU
      - PreCapNextDay
    purpose: >
      Marks a planned flow or sprint as skipped, partial, blocked, or deferred
      so APSU and the next PreCapNextDay can account for it without guessing.
    format: yaml_block_or_markdown_file
    lifecycle_position: execution_exception_to_status_merge_to_next_planning
    required_later_detail:
      - skip_reason_enum
      - affected_flow_or_sprint_id
      - reschedule_or_drop_rule
      - registry_storage

  - artifact_id: A08
    artifact_name: flow_recap_packet
    producer: FlowRecapSkill_or_flow-recap
    consumer:
      - APSU_or_status-merge
      - PreCapNextDay
      - ModelSubscriptionUsageTracking
      - Operator
    purpose: >
      Converts one flow plan and raw dump into structured execution memory,
      project status delta, artifact index, model usage delta, blockers,
      learning, and operator-validated next step.
    format: markdown_with_structured_yaml_blocks
    lifecycle_position: flow_recap_to_status_merge_and_next_planning
    required_later_detail:
      - flow_recap_id_schema
      - project_status_delta_schema
      - model_usage_delta_schema
      - operator_validation_schema
      - residual_flow_split_schema

  - artifact_id: A09
    artifact_name: model_usage_delta
    producer:
      - FlowRecapSkill
      - Operator_optional
    consumer:
      - ModelSubscriptionUsageTracking
      - APSU
      - PreCapNextDay
    purpose: >
      Records planned vs actual AI surface/model/mode usage, quality, route
      performance, cost/scarcity class, and reuse/avoid signals.
    format: yaml_block_inside_flow_recap_packet_or_usage_file_entry
    lifecycle_position: prompt_execution_to_usage_tracking_to_future_routing
    required_later_detail:
      - planned_route_fields
      - actual_route_fields
      - confidence_enum
      - quality_enum
      - scarce_mode_fields
      - usage_summary_owner

  - artifact_id: A10
    artifact_name: updated_all_project_status_packet
    producer: AllProjectStatusPacketUpdate_or_status-merge_APSU
    consumer:
      - PreCapNextDay
      - PreCapWeek
      - Operator
      - meta_strategist_optional_review
    purpose: >
      Publishes the canonical cross-project planning state after merging
      FlowRecaps, skipped markers, blockers, next chunks, priority changes,
      and unresolved conflicts.
    format: markdown_with_yaml_blocks
    lifecycle_position: daily_or_manual_status_merge_to_next_planning
    required_later_detail:
      - project_status_entry_schema
      - next_executable_chunks_schema
      - conflict_schema
      - consumed_registry_embedding_rule
      - storage_path

  - artifact_id: A11
    artifact_name: consumed_flow_recap_registry
    producer: APSU_or_status-merge
    consumer:
      - APSU_next_run
      - PreCapNextDay_optional
      - meta_detective_controller_optional
    purpose: >
      Prevents duplicate merging by tracking which FlowRecap packets were
      already consumed in status updates.
    format: yaml_block_embedded_or_separate_registry_file_CHECK_LATER
    lifecycle_position: status_merge_idempotency
    required_later_detail:
      - embedded_vs_separate_storage_decision
      - flow_recap_id_reference_schema
      - consumed_timestamp_or_update_id
      - duplicate_merge_behavior

  - artifact_id: A12
    artifact_name: skipped_flow_marker_registry
    producer: APSU_or_status-merge
    consumer:
      - APSU_next_run
      - PreCapNextDay
      - Operator
    purpose: >
      Tracks skipped/partial/deferred flow markers across daily planning cycles.
    format: yaml_block_embedded_or_separate_registry_file_CHECK_LATER
    lifecycle_position: exception_tracking_across_cycles
    required_later_detail:
      - embedded_vs_separate_storage_decision
      - marker_id_schema
      - resolved_unresolved_state
      - next_planning_behavior

  - artifact_id: A13
    artifact_name: next_PreCapNextDay_input_context
    producer: APSU_or_status-merge
    consumer:
      - PreCapNextDay
      - Operator
      - meta_operations
    purpose: >
      Provides the immediate next planning context from the status merge:
      next executable chunks, blockers, skipped markers, prompt routes to reuse
      or avoid, and high-impact changes requiring review.
    format: yaml_block_or_markdown_section
    lifecycle_position: status_merge_to_next_daily_planning
    required_later_detail:
      - execution_day_target_schema
      - project_next_chunks_schema
      - prompt_route_signal_schema
      - high_impact_review_threshold

  - artifact_id: A14
    artifact_name: AI_surface_inventory
    producer: Operator_or_config_file_CHECK_LATER
    consumer:
      - PreCapNextDay
      - PromptAndAIRoutingPlanning
      - ModelSubscriptionUsageTracking
    purpose: >
      Defines available AI surfaces, models, modes, subscriptions, scarcity
      limits, capabilities, and preferred use cases.
    format: markdown_or_yaml_config_CHECK_LATER
    lifecycle_position: routing_configuration
    required_later_detail:
      - canonical_storage_location
      - owner
      - update_cadence
      - surface_capability_schema
      - subscription_limit_schema

  - artifact_id: A15
    artifact_name: Claude__build_output_manifest
    producer: Claude__via_Claude_Code
    consumer:
      - Operator
      - meta_detective_controller
      - future_runtime_translation_step
    purpose: >
      Records what Claude  inspected, created, modified, deferred, and
      refused to create during the first build-pack execution.
    format: markdown_with_yaml_blocks
    lifecycle_position: build_execution_audit
    required_later_detail:
      - created_files_list_schema
      - skipped_files_list_schema
      - unresolved_conflicts_schema
      - operator_approval_needed_schema
      - next_prompt_schema

macro_validation_rules:
  - every_artifact_has_producer: true
  - every_artifact_has_consumer: true
  - every_artifact_has_lifecycle_position: true
  - full_schema_required_now: false
  - full_schema_required_before_runtime_translation: true
```

---

## 5. 04_TARGET_FILE_TREE_PROPOSAL.md

```yaml
file_chapter:
  intended_future_file: 04_TARGET_FILE_TREE_PROPOSAL.md
  chapter_role: proposed_build_pack_tree
  implementation_status: proposal_only_not_verified_against_local_repo

tree_status: proposed_not_verified

rule: >
  Claude  must inspect the local repository/filesystem before creating
  paths. This tree is a build-pack proposal, not final Hermes-compatible pathing.

path_policy:
  logical_paths_allowed_now: true
  absolute_paths_allowed_now: false
  runtime_Hermes_paths_finalized_now: false
  Claude__first_action: inspect_local_repo_before_writing

proposed_tree: |
  apex-hermes/
    docs/
      00_SYSTEM_INTENT.md
      01_SOURCE_MAP.md
      02_DECISION_REGISTER.md
      03_ARTIFACT_CONTRACT_REGISTRY.md
      04_TARGET_FILE_TREE_PROPOSAL.md
      05_BUILD_QUESTIONS.md
      06_CLAUDE__BUILD_PROMPT.md

    profiles/
      alfred/
        README.md
        SOUL.draft.md
        config.draft.yaml
        context/
          operator_context.draft.md
          current_projects.draft.md

      meta_strategist/
        README.md
        SOUL.draft.md
        config.draft.yaml
        context/
          strategy_principles.draft.md
          prioritization_rules.draft.md

      meta_operations/
        README.md
        SOUL.draft.md
        config.draft.yaml
        context/
          process_routing_rules.draft.md
          artifact_management_rules.draft.md
          workflow_library_index.draft.md

      meta_detective_controller/
        README.md
        SOUL.draft.md
        config.draft.yaml
        context/
          verification_rules.draft.md
          deprecated_model_blocklist.draft.md
          mistake_memory.draft.md

    skills/
      precap-week/
        SKILL.draft.md
        references/
        evals/

      precap-next-day/
        SKILL.draft.md
        references/
        templates/
        evals/

      flow-recap/
        SKILL.draft.md
        references/
        templates/
        evals/

      status-merge/
        SKILL.draft.md
        references/
        templates/
        evals/

      prompt-and-ai-routing-planning/
        SKILL.draft.md
        references/
        templates/
        evals/

      model-usage-log/
        SKILL.draft.md
        references/
        templates/
        evals/

    artifacts/
      plans/
        weekly/
        daily/

      flows/
        packets/
        raw/

      recaps/
        flows/

      status/
        current/
        archive/

      registry/
        consumed-flow-recaps/
        skipped-flow-markers/

      usage/
        model-usage/
        routing-signals/

      context/
        next-precapnextday/
        calendar/
        source-packets/

      config/
        AI_surface_inventory.draft.yaml
        artifact_location_slots.draft.yaml
        id_schema.draft.yaml

    runtime-later/
      cron/
        README.not-active.md
      kanban/
        README.not-active.md
      hermes-install/
        README.not-active.md

tree_annotations:
  docs:
    role: macro build-pack understanding layer
    current_action: create_or_generate_after_operator_approval
  profiles:
    role: draft profile content only
    current_action: do_not_install
  skills:
    role: draft skill candidates only
    current_action: do_not_install_final_SKILL_md_unless_approved
  artifacts:
    role: proposed durable artifact storage
    current_action: logical_storage_until_paths_verified
  runtime_later:
    role: placeholders for later translation notes
    current_action: no_cron_no_kanban_no_install

do_not_claim:
  - this_is_final_Hermes_HOME_structure
  - profiles_are_already_created
  - skills_are_already_installed
  - cron_jobs_exist
  - Kanban_graphs_exist
```

---

## 6. 05_BUILD_QUESTIONS.md

```yaml
file_chapter:
  intended_future_file: 05_BUILD_QUESTIONS.md
  chapter_role: blocking_questions_only
  implementation_status: macro_questions_only

question_policy:
  ask_only_blocking_questions: true
  recommendations_favor_safe_staging: true
  default_posture:
    - create drafts first
    - do not install runtime files yet
    - do not create cron jobs yet
    - inspect local repo before writing
    - preserve deprecated model blocklist

blocking_questions:
  - question_id: BQ01_project_root
    question: Where should Claude Code create the Apex/Hermes build pack?
    why_it_matters: >
      The root determines whether files are isolated design drafts, part of an
      existing repo, or placed dangerously close to active Hermes runtime paths.
    options:
      A: Inside the existing project/repo.
      B: In a new dedicated repo/folder.
      C: As a docs-only folder first, then later copied or translated into Hermes home.
    recommendation: C_then_B_if_clean_repo_is_preferred
    default_if_unanswered: C
    affected_future_files:
      - 04_TARGET_FILE_TREE_PROPOSAL.md
      - 06_CLAUDE__BUILD_PROMPT.md
      - all_generated_files

  - question_id: BQ02_design_only_vs_draft_runtime_files
    question: Should Claude  create only macro/design files first, or also draft runtime-style files without installing them?
    why_it_matters: >
      Draft runtime files are useful but can be mistaken for active Hermes
      files. Pure design files are safer but less testable.
    options:
      A: Macro/design files only.
      B: Draft runtime-style SOUL.draft.md and SKILL.draft.md files, not installed.
      C: Create final runtime files immediately.
    recommendation: B_after_docs_are_created
    default_if_unanswered: A_for_first_pass_then_B_after_review
    affected_future_files:
      - profiles/*/SOUL.draft.md
      - skills/*/SKILL.draft.md
      - runtime-later/

  - question_id: BQ03_profile_creation_timing
    question: When should Alfred and the three meta-head profiles be created as actual Hermes profiles?
    why_it_matters: >
      Profile creation changes runtime state and may create isolated memories,
      skills, configs, sessions, or tool boundaries before content is validated.
    options:
      A: Draft profile files now, install later.
      B: Install all four profiles immediately.
      C: Draft only meta_operations first.
    recommendation: A
    default_if_unanswered: A
    affected_future_files:
      - profiles/alfred/
      - profiles/meta_strategist/
      - profiles/meta_operations/
      - profiles/meta_detective_controller/

  - question_id: BQ04_skill_draft_scope
    question: Which skill candidates should Claude  draft first?
    why_it_matters: >
      Drafting too many skill files risks shallow generic procedures. Drafting
      too few may leave the core loop untestable.
    options:
      A: flow-recap only.
      B: flow-recap, precap-next-day, status-merge.
      C: full skill candidate set.
    recommendation: B
    default_if_unanswered: B
    affected_future_files:
      - skills/flow-recap/SKILL.draft.md
      - skills/precap-next-day/SKILL.draft.md
      - skills/status-merge/SKILL.draft.md
      - skills/prompt-and-ai-routing-planning/SKILL.draft.md
      - skills/model-usage-log/SKILL.draft.md
      - skills/precap-week/SKILL.draft.md

  - question_id: BQ05_absolute_artifact_paths
    question: Should absolute artifact paths be chosen now?
    why_it_matters: >
      Runtime files need real paths. Choosing paths before inspecting the local
      repo can create broken references or pollute active runtime directories.
    options:
      A: Choose absolute paths now.
      B: Use logical slots only.
      C: Claude  inspects repo and proposes absolute paths.
    recommendation: C
    default_if_unanswered: B_until_repo_inspection
    affected_future_files:
      - 03_ARTIFACT_CONTRACT_REGISTRY.md
      - artifacts/config/artifact_location_slots.draft.yaml
      - all artifact-producing skills

  - question_id: BQ06_AI_surface_inventory_storage
    question: Where should AI_surface_inventory live?
    why_it_matters: >
      Prompt routing and model usage tracking need a durable source for
      available AI surfaces, models, modes, scarcity limits, and preferences.
    options:
      A: Dedicated config file under artifacts/config/AI_surface_inventory.draft.yaml.
      B: Profile memory/context file.
      C: Operator paste at each PreCapNextDay run.
      D: Later runtime config integration.
    recommendation: A_with_D_later
    default_if_unanswered: A_as_draft_config
    affected_future_files:
      - artifacts/config/AI_surface_inventory.draft.yaml
      - skills/precap-next-day/SKILL.draft.md
      - skills/prompt-and-ai-routing-planning/SKILL.draft.md
      - skills/model-usage-log/SKILL.draft.md

  - question_id: BQ07_Kanban_cron_automation_timing
    question: Should Kanban or cron automation be implemented in the first Claude  pass?
    why_it_matters: >
      Cron and Kanban create runtime behavior. The current design is not yet
      path/toolset/profile verified.
    options:
      A: No automation; manual invocation and draft specs only.
      B: Draft Kanban/cron design notes but do not activate.
      C: Implement active Kanban and cron immediately.
    recommendation: B
    default_if_unanswered: B
    affected_future_files:
      - runtime-later/cron/README.not-active.md
      - runtime-later/kanban/README.not-active.md
      - 06_CLAUDE__BUILD_PROMPT.md

  - question_id: BQ08_APSU_to_PreCapNextDay_trigger
    question: How should APSU/status-merge trigger or prepare the next PreCapNextDay?
    why_it_matters: >
      This controls loop continuation and duplicate-planning risk. In v0.1,
      auto-triggering is intentionally deferred.
    options:
      A: APSU only writes next_PreCapNextDay_input_context; operator manually starts PreCapNextDay.
      B: APSU creates a Kanban task for PreCapNextDay after status merge.
      C: APSU creates or modifies cron jobs.
      D: Separate LoopContinuationCheck handles this later.
    recommendation: A_for_v0_1_then_B_later_if_runtime_verified
    default_if_unanswered: A
    affected_future_files:
      - skills/status-merge/SKILL.draft.md
      - skills/precap-next-day/SKILL.draft.md
      - runtime-later/kanban/
      - runtime-later/cron/

  - question_id: BQ09_Claude__first_action
    question: Should Claude  inspect the repository first or write files immediately?
    why_it_matters: >
      Claude Code has filesystem access. Inspection prevents wrong paths,
      duplicate files, and accidental runtime activation.
    options:
      A: Write files immediately from this macro document.
      B: Inspect repo/filesystem, summarize findings, then propose exact file creation plan.
      C: Ask questions before inspecting.
    recommendation: B
    default_if_unanswered: B
    affected_future_files:
      - 06_CLAUDE__BUILD_PROMPT.md
      - Claude__build_output_manifest
      - all generated files

  - question_id: BQ10_runtime_activation_gate
    question: What approval phrase should permit Claude  to create active Hermes runtime files later?
    why_it_matters: >
      Prevents accidental installation of profiles, skills, cron jobs, or
      Kanban graphs during design/build-pack stages.
    options:
      A: "Draft only" remains default until explicit phrase "activate Hermes runtime".
      B: Any instruction to create files may include runtime files.
      C: Runtime activation is permanently out of scope for Claude .
    recommendation: A
    default_if_unanswered: A
    affected_future_files:
      - 06_CLAUDE__BUILD_PROMPT.md
      - runtime-later/
      - profiles/
      - skills/
```

---

## 7. 06_CLAUDE__BUILD_PROMPT.md

````markdown
# Claude  / Claude Code Build Prompt — Apex/Hermes Macro Build Pack v0.1

You are Claude  running through Claude Code with local filesystem access.

You are helping build the **Apex/Hermes personal AI orchestration system**.

Your first job is **not** to install Hermes runtime files. Your first job is to inspect the local repository/filesystem, understand the existing project state, and create or propose a safe draft build-pack file sequence.

## Role

```yaml
role:
  - expert_Hermes_Agent_implementer
  - Claude_Code_filesystem_operator
  - cautious_runtime_translator
  - no_drift_reviewer
  - artifact_contract_designer
````

## Core system to preserve

```yaml
canonical_architecture:
  alfred: operator-facing interface
  meta_strategist: strategy_prioritization_leverage_direction
  meta_operations: process_orchestration_routing_artifact_creation_build_coordination
  meta_detective_controller: verification_drift_detection_quality_control_safety_gates

accepted_core_loop:
  - PreCapWeek
  - PreCapNextDay
  - OperatorExecutesPlannedFlow
  - FlowRecapSkill_or_flow-recap
  - AllProjectStatusPacketUpdate_or_status-merge_APSU
  - next_PreCapNextDay

deprecated_from_core:
  - DayExecution_as_standalone_process
  - FlowExecution_as_standalone_process
  - DayExecutionController_as_standalone_process
  - RecapDay_as_required_project_state_layer
```

## First actions

```yaml
first_actions:
  - inspect_local_repository_or_filesystem
  - identify_current_project_root
  - locate_existing_Hermes_related_files
  - locate_existing_Apex_Hermes_design_docs
  - read_this_macro_build_pack_document
  - summarize_findings
  - identify_path_conflicts_or_missing_paths
  - identify_existing_profiles_or_skill_files_if_any
  - propose_exact_file_creation_plan
  - wait_or_proceed_based_on_operator_instruction
```

## Do not write immediately unless instructed

```yaml
default_behavior:
  first_pass:
    - inspect
    - summarize
    - propose
    - ask only blocking questions
  write_files_only_if:
    - operator explicitly asks to create draft files
    - paths have been inspected or a safe draft folder is selected
```

## Hard constraints

```yaml
hard_constraints:
  - do_not_install_Hermes_profiles_unless_explicitly_approved
  - do_not_create_cron_jobs_in_first_pass
  - do_not_create_active_Kanban_graphs_in_first_pass
  - do_not_write_secrets
  - do_not_invent_unavailable_Hermes_profiles
  - do_not_place_large_artifacts_in_MEMORY_md
  - do_not_revive_DayExecution_or_FlowExecution
  - do_not_treat_workflow_as_Hermes_runtime_primitive
  - do_not_create_final_SKILL_md_files_unless_explicitly_asked
  - do_not_treat_FlowRecapSkill_as_callable_function
  - do_not_use_install_commands
  - do_not_assume_proposed_tree_is_final
```

## Mechanism rules

```yaml
mechanism_rules:
  skill:
    use_when:
      - repeatable procedure
      - one profile can execute
      - user-triggered or reusable
      - output is a structured artifact
    examples:
      - flow-recap
      - prompt-and-ai-routing-planning
      - status-merge
      - model-usage-log

  profile:
    use_when:
      - durable identity needed
      - isolated memory needed
      - separate toolsets or permissions needed
      - separate model/provider needed
      - queue ownership needed

  Kanban:
    use_when:
      - durable multi-profile work
      - audit trail needed
      - human gate needed
      - parallel fan-out needed
      - restart/crash survival needed

  delegate_task:
    use_when:
      - short-lived synchronous subwork
      - caller needs result in same session
      - no durable audit graph needed

  cron:
    use_when:
      - scheduled trigger needed
    avoid_in_v0_1:
      - heavy direct synthesis
      - recursive cron creation
```

## Before each file

For every future file you propose or create, include this compact reasoning block:

```yaml
before_each_file:
  goal: What this file enables.
  source_basis: Which project resources or accepted decisions constrain it.
  skeleton: Required sections.
  fill: Concrete content to include.
  verification_rule: How to check it preserves decisions and avoids deprecated models.
  next_step: What happens after the file exists.
```

## Expected first output

```yaml
expected_first_output:
  - repository_inspection_summary
  - detected_project_root
  - detected_existing_Hermes_files
  - detected_existing_Apex_Hermes_build_files
  - conflict_or_gap_report
  - proposed_safe_target_folder
  - proposed_file_creation_plan
  - files_to_create_first
  - files_not_to_create_yet
  - blocking_questions_if_any
```

## Preferred first file sequence after inspection

```yaml
preferred_first_file_sequence:
  phase_1_understanding_pack:
    - docs/00_SYSTEM_INTENT.md
    - docs/01_SOURCE_MAP.md
    - docs/02_DECISION_REGISTER.md

  phase_2_contract_pack:
    - docs/03_ARTIFACT_CONTRACT_REGISTRY.md
    - docs/04_TARGET_FILE_TREE_PROPOSAL.md
    - docs/05_BUILD_QUESTIONS.md
    - docs/06_CLAUDE__BUILD_PROMPT.md

  phase_3_draft_runtime_candidates_only_after_approval:
    - profiles/*/SOUL.draft.md
    - skills/*/SKILL.draft.md
    - artifacts/config/*.draft.yaml

  phase_4_runtime_translation_later:
    - actual_Hermes_profiles
    - actual_SKILL_md_files
    - cron_jobs
    - Kanban_graph_specs
```

## Acceptance criteria for your work

```yaml
acceptance_criteria:
  - preserves_Alfred_plus_three_meta_heads
  - preserves_core_loop
  - blocks_deprecated_models
  - separates_design_files_from_runtime_files
  - uses_artifacts_as_files_not_MEMORY_md
  - inspects_repo_before_path_creation
  - marks unresolved runtime decisions explicitly
  - produces machine-readable Markdown with YAML blocks
  - does not over-engineer process theory
```

````

---

## 8. Acceptance Checks

```yaml
acceptance_checks:
  document_level:
    - check: one_document_only
      status: pass_if_no_separate_files_created

    - check: machine_readable
      status: pass_if_dense_markdown_and_yaml_blocks_used

    - check: macro_level
      status: pass_if_no_final_runtime_files_or_install_commands_are_created

    - check: no_runtime_implementation
      status: pass_if_no_actual_SOUL_SKILL_cron_Kanban_profile_installation_is_done

    - check: source_aware
      status: pass_if_sources_are_categorized_and_design_vs_runtime_distinction_is_explicit

    - check: accepted_decisions_preserved
      status: pass_if_Alfred_plus_three_meta_heads_and_core_loop_are_present

    - check: deprecated_models_blocked
      status: pass_if_DayExecution_FlowExecution_required_RecapDay_and_workflow_runtime_primitive_are_marked_deprecated

    - check: processual_thinking_included_lightly
      status: pass_if_goal_sources_skeleton_fill_verify_next_step_exists_only_as_compact_default

    - check: Claude__can_understand_next_build_step
      status: pass_if_prompt_instructs_repo_inspection_before_file_creation

    - check: artifact_contracts_started
      status: pass_if_required_artifacts_have_producer_consumer_purpose_format_lifecycle_required_later_detail

    - check: target_tree_not_overclaimed
      status: pass_if_tree_is_marked_proposed_not_verified

    - check: blocking_questions_only
      status: pass_if_questions_are implementation_blockers_not_general_theory_questions

runtime_readiness_checks:
  current_status:
    ready_for_Claude_Code_repo_inspection: true
    ready_for_docs_draft_creation_after_operator_approval: true
    ready_for_final_Hermes_SKILL_md_installation: false
    ready_for_profile_installation: false
    ready_for_cron_creation: false
    ready_for_Kanban_graph_creation: false
    ready_for_secret_handling: false

Claude__success_conditions:
  - can_explain_system_in_under_10_bullets
  - can_identify_source_authority_order
  - can_distinguish_design_specs_from_runtime_files
  - can_propose_safe_file_creation_plan
  - can_refuse_or_defer_runtime_activation_without_approval
````

---

## 9. Non-Goals / Forbidden Actions

```yaml
non_goals:
  - no_final_runtime_implementation
  - no_actual_Hermes_install_commands
  - no_actual_profile_creation
  - no_actual_cron_jobs
  - no_final_Kanban_graph_creation
  - no_active_SKILL_md_installation
  - no_secrets
  - no_large_abstract_process_library
  - no_excessive_prose
  - no_human_facing_essay
  - no_runtime_path_claims_before_repo_inspection
  - no_reviving_deprecated_process_models

forbidden_actions:
  - action: create_actual_SOUL_md_files_in_HermES_HOME
    reason: runtime profile activation not approved

  - action: create_actual_SKILL_md_files_as_installed_Hermes_skills
    reason: skill drafts must be reviewed first

  - action: create_or_modify_Hermes_cron_jobs
    reason: automation deferred and heavy cron synthesis deprecated in v0_1

  - action: create_active_Kanban_task_graphs
    reason: profile/toolset/path readiness unresolved

  - action: place_plans_recaps_or_status_packets_in_MEMORY_md
    reason: large structured artifacts must be files or file-like artifacts

  - action: invent_available_profiles
    reason: Hermes profiles must be discovered or explicitly created later

  - action: treat_workflow_as_runtime_primitive
    reason: Hermes mapping must use skill, Kanban task graph, delegate_task, cron, profile, or artifact

  - action: treat_Claude_Code_and_Hermes_as_same_runtime
    reason: shared layer is repo/spec/SKILL_md draft layer, not full runtime semantics

  - action: create_install_or_activation_commands
    reason: current stage is macro build pack only

  - action: ask_user_questions_before_producing_macro_document
    reason: missing information belongs in 05_BUILD_QUESTIONS.md

final_state:
  produced: one_macro_markdown_document
  next_recommended_action: >
    Give this document to Claude  via Claude Code and instruct it to
    inspect the local repository first, then propose a safe file creation plan
    before writing any draft files.
```