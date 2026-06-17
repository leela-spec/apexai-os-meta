# Apex Hermes Orchestration Decisions v0.1

```yaml
document:
  id: apex_hermes_orchestration_decisions
  version: 0.1
  status: intermediate_decision_record
  purpose: >
    Capture the current architectural decisions for the Apex/Hermes personal
    orchestration system in a compact, machine-readable form. This file is the
    bridge between conceptual design and the later creation of actual Hermes
    profile files, SOUL.md files, skill folders, workflow skills, Kanban routines,
    cron routines, and context files.
  scope:
    included:
      - profile architecture
      - profile ownership boundaries
      - skill ownership boundaries
      - phase_1_and_phase_2 workflow ownership
      - Kanban/delegation/cron decision rules
      - native Hermes responsibilities
      - files_to_create_next
    excluded:
      - final Hermes implementation
      - full SKILL.md contents
      - final SOUL.md texts
      - concrete Kanban cards
      - runtime config commands
      - exhaustive OpenCLAW role replication

source_basis:
  project_sources:
    - Q&A_ProfileVsAgents.md
    - Q&A_SwarmOrchestration.md
    - kanban-orchestrator_skill.md
    - SkillCuratorArchitecture.md
    - Skill Usage Tracking and Backup.md
    - Skills Management and Security.md
    - SourceIndexAgentInteraction07OC.md
    - SourceIndexAgentInteractionAlfred.md
    - ApexAgent&Workflows.md
  github_repo_surfaces:
    - leela-spec/apexai-os-meta:managed/agents/AGENT_INDEX.md
    - leela-spec/apexai-os-meta:managed/rules/AGENT_SWARM_INTERACTION_CANON.md
    - leela-spec/apexai-os-meta:managed/processes/AGENT_HANDOFF_CONTRACTS.md
    - leela-spec/apexai-os-meta:managed/agent_kb/alfred/ESSENCE.md
    - leela-spec/apexai-os-meta:managed/agent_kb/alfred/BEST_PRACTICES.md
  source_interpretation:
    - OpenCLAW is treated as a source of workflow logic, handoff discipline, validation logic, and historical agent-role vocabulary.
    - Hermes is treated as the implementation substrate.
    - Alfred sources are treated as the operator-facing loop source: intake, daily board, session export, night loop, handoff variables.
    - Hermes profile/skill/Kanban/curator sources override OpenCLAW-style agent proliferation.

core_decision:
  architecture_name: alfred_plus_three_meta_heads
  architecture_summary: >
    The system uses Alfred as the operator-facing interface and three durable
    meta-head profiles for strategy, operations, and control. Most named
    workflows are not agents. They are skills, workflow skills, cron routines,
    Kanban routines, or transient delegated tasks.
  rationale_short:
    - Profiles provide isolated persistent identity, memory, SOUL.md, skills, sessions, and state.
    - Sub-capabilities should remain skills unless they require isolated memory, tools, model, permissions, or durable queue ownership.
    - Kanban is reserved for durable multi-profile work, not for every task.
    - Hermes-native skill management and curator functions replace custom knowledge-promotion agents.

canonical_profiles:
  alfred:
    type: hermes_profile
    layer: operator_interface
    purpose: >
      User-facing assistant for intake, clarification, morning review, session
      continuation, handover interface, and operator decision capture.
    owns:
      - user_intake_surface
      - conversational_continuity
      - morning_review_interface
      - operator_context_capture
      - human_override_capture
      - handover_to_meta_heads
    does_not_own:
      - strategic_decision_logic
      - workflow_system_design
      - quality_control_authority
      - skill_lifecycle_management
      - Kanban_decomposition_for_complex_work
    primary_interacts_with:
      - meta_strategist
      - meta_operations
      - meta_detective_controller
    implementation_files_to_create_later:
      - profiles/alfred/SOUL.md
      - profiles/alfred/config.yaml
      - profiles/alfred/context/operator_context.md
      - profiles/alfred/context/current_projects.md
      - profiles/alfred/skills/operator-interface/SKILL.md
      - profiles/alfred/skills/morning-review/SKILL.md

  meta_strategist:
    type: hermes_profile
    layer: meta_head
    purpose: >
      Strategy head for direction, prioritization, scenario analysis,
      recommendation, leverage evaluation, and high-level synthesis.
    owns:
      - strategic_evaluation
      - prioritization
      - option_generation
      - scenario_planning
      - leverage_analysis
      - strategic_recommendations
      - final_synthesis_when_strategy_is_required
    does_not_own:
      - routine_execution_tracking
      - prompt_workflow_operations
      - quality_control_gatekeeping
      - daily_board_assembly
    primary_interacts_with:
      - alfred
      - meta_operations
      - meta_detective_controller
    implementation_files_to_create_later:
      - profiles/meta_strategist/SOUL.md
      - profiles/meta_strategist/config.yaml
      - profiles/meta_strategist/context/strategy_principles.md
      - profiles/meta_strategist/skills/strategic-evaluation/SKILL.md
      - profiles/meta_strategist/skills/scenario-planning/SKILL.md
      - profiles/meta_strategist/skills/decision-memo/SKILL.md
      - profiles/meta_strategist/skills/leverage-analysis/SKILL.md

  meta_operations:
    type: hermes_profile
    layer: meta_head
    purpose: >
      Operations head for routing, workflow design, prompt design, task
      packaging, handoffs, execution planning, Kanban decomposition, session
      export, night loop, and daily command board generation.
    owns:
      - orchestration_intake
      - project_routing
      - agent_handoff_packets
      - prompt_design
      - workflow_design
      - execution_mode_selection
      - Kanban_decomposition
      - session_export
      - night_loop
      - daily_command_board
      - craft_flow_handoff
      - metrics_and_variables_capture
      - operator_feedback_capture
    does_not_own:
      - final_strategy_authority
      - adversarial_validation_authority
      - native_Hermes_skill_lifecycle_management
      - source_of_truth_promotion_as_custom_architecture
    primary_interacts_with:
      - alfred
      - meta_strategist
      - meta_detective_controller
    implementation_files_to_create_later:
      - profiles/meta_operations/SOUL.md
      - profiles/meta_operations/config.yaml
      - profiles/meta_operations/context/workflow_library_index.md
      - profiles/meta_operations/context/project_routing_rules.md
      - profiles/meta_operations/skills/orchestration-intake/SKILL.md
      - profiles/meta_operations/skills/project-routing/SKILL.md
      - profiles/meta_operations/skills/handoff-packet/SKILL.md
      - profiles/meta_operations/skills/prompt-design/SKILL.md
      - profiles/meta_operations/skills/workflow-design/SKILL.md
      - profiles/meta_operations/skills/kanban-decomposition/SKILL.md
      - profiles/meta_operations/skills/session-export/SKILL.md
      - profiles/meta_operations/skills/night-loop/SKILL.md
      - profiles/meta_operations/skills/daily-command-board/SKILL.md
      - profiles/meta_operations/skills/craft-flow-handoff/SKILL.md
      - profiles/meta_operations/skills/metrics-and-variables/SKILL.md

  meta_detective_controller:
    type: hermes_profile
    layer: meta_head
    purpose: >
      Control head for verification, contradiction detection, quality control,
      no-drift review, mistake memory, escalation, and adversarial pressure.
    owns:
      - output_verification
      - no_drift_validation
      - contradiction_detection
      - handoff_risk_check
      - quality_control
      - escalation_logic
      - mistake_memory
      - failure_pattern_review
      - acceptance_criteria_review
    does_not_own:
      - primary_execution
      - daily_board_generation
      - strategic_option_generation_as_primary_owner
      - skill_lifecycle_management_as_custom_agent
    primary_interacts_with:
      - alfred
      - meta_strategist
      - meta_operations
    implementation_files_to_create_later:
      - profiles/meta_detective_controller/SOUL.md
      - profiles/meta_detective_controller/config.yaml
      - profiles/meta_detective_controller/context/control_principles.md
      - profiles/meta_detective_controller/context/mistake_memory.md
      - profiles/meta_detective_controller/skills/no-drift-validation/SKILL.md
      - profiles/meta_detective_controller/skills/contradiction-detection/SKILL.md
      - profiles/meta_detective_controller/skills/qa-review/SKILL.md
      - profiles/meta_detective_controller/skills/handoff-risk-check/SKILL.md
      - profiles/meta_detective_controller/skills/escalation-check/SKILL.md

optional_profiles:
  orchestrator:
    status: deferred
    create_when:
      - Kanban routing becomes heavy enough to require a dedicated queue coordinator.
      - The operations profile is overloaded by orchestration overhead.
      - Cross-profile graph decomposition becomes a frequent daily task.
    default_now: do_not_create
    default_replacement_now: meta_operations_with_kanban_decomposition_skill

profile_creation_rule:
  create_new_profile_only_if:
    - needs_isolated_memory
    - needs_different_model
    - needs_different_tool_permissions
    - needs_separate_SOUL_identity
    - owns_long_running_Kanban_queue
    - repeatedly_blocks_parent_profile_capacity
  otherwise:
    - implement_as_skill
    - implement_as_workflow_skill
    - implement_as_context_file
    - implement_as_cron_routine
    - implement_as_transient_delegate_task

not_profiles:
  delete_or_do_not_create:
    - deep_researcher
    - patchspec_writer
    - executor_implementer_as_conceptual_profile
    - no_drift_validator_as_separate_profile
    - session_export_agent
    - night_planner
    - daily_command_board_builder
    - morning_review_assistant
    - craft_flow_planner
    - pattern_learning_agent
    - metrics_tracker
    - handoff_packet_builder
    - escalation_gatekeeper
    - knowledge_bank_ops
    - informatics_design
    - promotion_reviewer
    - skill_curator
    - cron_worker_as_conceptual_agent
  replacement_logic:
    deep_researcher: strategist_or_operations_skill
    patchspec_writer: meta_operations_skill
    executor_implementer_as_conceptual_profile: actual_Kanban_assignee_or_delegate_task_when_available
    no_drift_validator_as_separate_profile: meta_detective_controller_skill
    session_export_agent: meta_operations_skill_or_cron
    night_planner: meta_operations_cron_workflow
    daily_command_board_builder: meta_operations_skill_exposed_through_alfred
    morning_review_assistant: alfred_behavior_plus_operations_board_skill
    craft_flow_planner: meta_operations_skill
    pattern_learning_agent: Hermes_curator_plus_detective_mistake_memory_when_needed
    metrics_tracker: meta_operations_skill_or_context_file
    handoff_packet_builder: meta_operations_skill
    escalation_gatekeeper: meta_detective_controller_behavior
    knowledge_bank_ops: Hermes_native_skill_context_management
    informatics_design: simple_markdown_structure_and_skill_design_process
    promotion_reviewer: Hermes_curator_and_manual_review_if_needed
    skill_curator: Hermes_native_curator
    cron_worker_as_conceptual_agent: Hermes_cron_runtime

mechanism_decisions:
  profiles:
    use_for:
      - durable_identity
      - isolated_memory
      - separate_SOUL
      - different_model_or_tools
      - persistent_department_head_behavior
    do_not_use_for:
      - every_workflow
      - every_prompt_pattern
      - every_validation_step
      - every_recurring_routine

  skills:
    use_for:
      - repeatable_procedure
      - profile_local_capability
      - workflow_template
      - prompt_pattern
      - routing_logic
      - validation_logic
      - handoff_schema
      - board_generation_logic
    storage_decision:
      default_shared_skills: false_for_core_department_skills
      preferred_for_core_department_skills: profile_external_skill_dirs
      rationale: keep department-head skills legible and bounded by role

  context_files:
    use_for:
      - stable_role_principles
      - project_index
      - routing_rules
      - mistake_memory
      - operator_context
      - current_project_state
      - workflow_library_index
    do_not_use_for:
      - volatile_session_details
      - unreviewed_candidate_truth
      - large_raw_source_dumps

  delegate_task:
    use_for:
      - transient_one_shot_specialist_work
      - bounded_synchronous_tasks
      - no_persistence_needed
      - no_cross_session_tracking_needed
    do_not_use_for:
      - durable_multi_step_work
      - important_audit_trail_work
      - long_running_work
      - human_in_loop_work

  Kanban:
    use_for:
      - durable_multi_step_work
      - cross_profile_coordination
      - work_that_should_survive_restart
      - human_in_loop_work
      - parallel_lanes
      - review_iteration
      - audit_trail_matters
    routing_owner:
      default_now: meta_operations
      optional_later: orchestrator_profile
    rules:
      - discover_actual_profiles_before_assigning_cards
      - do_not_invent_assignee_names
      - route_do_not_execute_when_acting_as_orchestrator
      - create_parent_links_at_task_creation_time
      - use_goal_mode_only_for_long_multi_turn_cards

  cron:
    use_for:
      - night_loop
      - daily_command_board_generation
      - weekly_review
      - recurring_repo_hygiene
      - recurring_validation_check
    owner:
      default: meta_operations
      validation: meta_detective_controller_when_quality_or_drift_risk_exists
      strategic_input: meta_strategist_when_priorities_or_direction_are_involved

  Hermes_native:
    use_for:
      - skill_lifecycle_management
      - skill_usage_tracking
      - stale_skill_detection
      - archive_and_restore
      - skill_backup
      - agent_created_skill_review
    do_not_rebuild_as_custom_agents:
      - skill_curator
      - promotion_reviewer
      - generic_learning_promotion_pipeline
      - knowledge_bank_ops

phase_decisions:
  phase_0:
    name: architecture_lock
    purpose: lock Alfred plus three meta-head profile structure
    owner: user_with_design_chat
    output:
      - this_decision_record
      - profile_file_creation_plan

  phase_1:
    name: orchestration_kernel
    owner: meta_operations
    interface: alfred
    strategic_review: meta_strategist_when_task_affects_direction_or_priority
    validation: meta_detective_controller_when_task_is_risky_ambiguous_or_high_impact
    workflows:
      orchestration_intake:
        mechanism: skill
        owner: meta_operations
        purpose: normalize raw user/repo/project input into a structured work packet
      project_routing:
        mechanism: skill
        owner: meta_operations
        purpose: choose keep_local vs delegate_task vs Kanban vs cron vs ask_operator
      handoff_packet:
        mechanism: skill
        owner: meta_operations
        purpose: create clean transfer packets for profiles, chats, repos, Kanban cards, or human review
      handoff_risk_check:
        mechanism: skill
        owner: meta_detective_controller
        purpose: validate whether a handoff can safely proceed

  phase_2:
    name: day_night_operating_loop
    owner: meta_operations
    interface: alfred
    strategic_input: meta_strategist_for_priorities_and_direction
    validation: meta_detective_controller_for_drift_quality_and_blockers
    workflows:
      session_export:
        mechanism: skill
        owner: meta_operations
        purpose: capture session outcome, decisions, artifacts, blockers, next actions
      night_loop:
        mechanism: cron_workflow_skill
        owner: meta_operations
        purpose: synthesize session exports into next-day prepared sessions
      daily_command_board:
        mechanism: cron_or_manual_workflow_skill
        owner: meta_operations
        interface: alfred
        purpose: create editable morning execution board
      morning_review:
        mechanism: profile_behavior_plus_skill
        owner: alfred
        purpose: let operator revise priorities, sessions, constraints, and overrides

workflow_routing_decisions:
  route_types:
    keep_local:
      use_when:
        - small_clarification
        - short_structuring_task
        - immediate_answer_possible
      owner: alfred_or_current_profile

    delegate_task:
      use_when:
        - bounded_specialist_work
        - synchronous_one_shot
        - no_durable_tracking_needed
      owner: current_profile_with_delegation

    create_Kanban_card:
      use_when:
        - durable_multi_step_task
        - profile_coordination_required
        - dependencies_exist
        - audit_trail_matters
        - human_may_interject
      owner: meta_operations

    schedule_cron:
      use_when:
        - recurring_routine
        - scheduled_synthesis
        - recurring_review
      owner: meta_operations

    ask_operator:
      use_when:
        - missing_priority
        - unclear_project_owner
        - conflicting_instructions
        - high_impact_acceptance_criteria_missing
        - irreversible_action
        - sensitive_or_private_decision
      owner: alfred

core_interaction_patterns:
  standard_department_flow:
    sequence:
      - step: intake
        actor: alfred
        output: normalized_user_intent
      - step: route
        actor: meta_operations
        output: routing_decision
      - step: strategy_if_needed
        actor: meta_strategist
        condition: strategic_priority_or_direction_question
        output: recommendation_or_option_set
      - step: execute_or_decompose
        actor: meta_operations
        output: direct_workflow_output_or_Kanban_graph
      - step: verify_if_needed
        actor: meta_detective_controller
        condition: quality_risk_drift_or_high_impact
        output: pass_revise_hold_or_escalate
      - step: present
        actor: alfred
        output: operator_facing_summary_or_next_action

  day_night_loop:
    sequence:
      - step: work_session
        actor: operator_or_assigned_profile
        output: work_output
      - step: session_export
        actor: meta_operations
        output: session_export_packet
      - step: night_synthesis
        actor: meta_operations
        input: session_exports
        strategic_input: meta_strategist_when_needed
        validation: meta_detective_controller_when_needed
        output: next_day_prepared_sessions
      - step: daily_board
        actor: meta_operations
        output: daily_command_board
      - step: morning_review
        actor: alfred
        output: operator_confirmed_day_plan

  Kanban_flow:
    sequence:
      - step: profile_discovery
        actor: meta_operations_or_orchestrator_later
        output: actual_profile_roster
      - step: graph_sketch
        actor: meta_operations_or_orchestrator_later
        output: proposed_lanes_and_dependencies
      - step: card_creation
        actor: meta_operations_or_orchestrator_later
        output: cards_with_real_assignees_and_parent_links
      - step: worker_execution
        actor: assigned_profiles
        output: card_outputs
      - step: verification
        actor: meta_detective_controller_or_assigned_reviewer
        output: verification_result
      - step: synthesis
        actor: meta_strategist_or_meta_operations_depending_on_task
        output: final_integrated_result

skill_groups_to_create_next:
  alfred:
    - operator-interface
    - morning-review
    - handover-interface
    - operator-decision-capture

  meta_strategist:
    - strategic-evaluation
    - scenario-planning
    - decision-memo
    - leverage-analysis
    - priority-review

  meta_operations:
    - orchestration-intake
    - project-routing
    - handoff-packet
    - prompt-design
    - workflow-design
    - Kanban-decomposition
    - session-export
    - night-loop
    - daily-command-board
    - craft-flow-handoff
    - metrics-and-variables

  meta_detective_controller:
    - no-drift-validation
    - contradiction-detection
    - qa-review
    - handoff-risk-check
    - escalation-check
    - mistake-memory-review

context_files_to_create_next:
  global:
    - hermes_orchestration_decisions.md
    - project_index.md
    - profile_roster.md
    - workflow_registry.md
    - routing_taxonomy.md

  alfred:
    - operator_context.md
    - current_projects.md
    - morning_review_preferences.md

  meta_strategist:
    - strategy_principles.md
    - prioritization_rules.md
    - decision_frameworks.md

  meta_operations:
    - project_routing_rules.md
    - workflow_library_index.md
    - handoff_packet_schema.md
    - daily_command_board_schema.md
    - session_export_schema.md
    - night_loop_schema.md

  meta_detective_controller:
    - control_principles.md
    - validation_checklist.md
    - mistake_memory.md
    - escalation_rules.md
    - no_drift_rules.md

skill_file_creation_rules:
  SKILL_md_required_sections:
    - frontmatter
    - purpose
    - when_to_use
    - inputs
    - procedure
    - outputs
    - stop_conditions
    - examples
    - related_skills
  frontmatter_minimum:
    name: lowercase-hyphenated-skill-name
    description: concise_trigger_description
    version: 0.1.0
    platforms:
      - linux
      - macos
      - windows
    metadata:
      hermes:
        tags: []
  description_rule: >
    Description must describe when the skill should trigger, not merely what
    the skill is. It must be specific enough to avoid triggering for unrelated
    tasks.
  anti_overengineering_rule: >
    Start each skill with the smallest procedure that works on real examples.
    Expand only after examples expose a missing field or step.

naming_decisions:
  profiles:
    alfred: alfred
    strategist: meta_strategist
    operations: meta_operations
    detective: meta_detective_controller
    optional_orchestrator_later: orchestrator
  skills:
    use_lowercase_hyphenated_names: true
    examples:
      - orchestration-intake
      - project-routing
      - handoff-packet
      - daily-command-board
      - no-drift-validation

open_decisions:
  - id: OD-001
    question: Should a separate orchestrator profile be created later?
    current_default: no
    trigger_to_reopen: Kanban orchestration becomes frequent and heavy.

  - id: OD-002
    question: Should each meta-head use fully isolated external skill directories?
    current_default: yes_for_core_department_skills
    trigger_to_reopen: shared skill access proves simpler without role contamination.

  - id: OD-003
    question: Which actual implementation profiles exist for Kanban worker cards?
    current_default: unknown_until_runtime_profile_discovery
    trigger_to_reopen: before first Kanban graph is created.

  - id: OD-004
    question: How much of OpenCLAW source routing remains useful once Hermes native skill systems are active?
    current_default: preserve_only_as_validation_and_handoff_discipline
    trigger_to_reopen: if source conflict handling becomes a recurring failure point.

next_process:
  name: create_profile_and_skill_file_plan
  purpose: >
    Use this decision record to generate the exact file tree and file-writing
    sequence for the Hermes profile system.
  next_outputs:
    - profile_file_tree.md
    - profile_soul_file_prompts.md
    - skill_creation_sequence.md
    - initial_skill_specs.md
    - context_file_templates.md
    - validation_plan.md
```
