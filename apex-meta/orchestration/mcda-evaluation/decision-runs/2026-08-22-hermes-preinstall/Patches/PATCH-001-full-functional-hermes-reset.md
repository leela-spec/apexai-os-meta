# PATCH-001 — Full-functional Hermes realization reset

Status: **PATCH SPECIFICATION / APPLIED IN SAME CHANGESET AND VERIFIED AFTER COMMIT**

This file records the exact-match mutable-state patches required by the 2026-08-22 operator correction. Historical ADR/runbook files are not rewritten; ADR-002 and runbook v2 supersede them as active guidance.

## PATCH INSTRUCTION FORMAT — EXACT-MATCH BLOCK REPLACEMENT

Each block below is one literal replacement. `OLD` must match exactly once before application. The executor must reject the block if it does not match character-for-character.

```text
/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
schema_version: 1
project: master-of-arts-hermes-preinstall-validation
repository: leela-spec/MasterOfArts
branch: main
created: 2026-08-22
status: preinstall_validation_ready
implementation_authorized: false
human_decision_required: true

entrypoint: Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK.md
decision_record: Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-001-provisional-hermes-stack.md
parent_selection_handover: Orchestration/09-PRIMARY-ORCHESTRATION-SELECTION-HANDOVER.md
parent_mcda_state: Orchestration/mcda-state.yaml

selection:
  primary_candidate: hermes_agent
  direct_challenger: openclaw
  production_winner: null
  confidence_primary_candidate: B+
  confidence_production_fit: C

non_negotiables:
  upstream_existing_target_percent: 90-95
  max_project_specific_connection_percent: 5-10
  custom_orchestration_runtime: forbidden
  custom_memory_sync: forbidden
  custom_kb_engine: forbidden
  duplicate_canonical_task_systems: forbidden_by_default
  install_before_human_approval: forbidden
  mass_repo_reorganization_before_validation: forbidden
</OLD>
<NEW>
schema_version: 2
project: master-of-arts-hermes-preinstall-validation
repository: leela-spec/MasterOfArts
branch: main
created: 2026-08-22
last_updated: 2026-08-22
status: full_functional_hermes_target_validation_ready
implementation_authorized: false
human_decision_required: true

entrypoint: Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK-v2.md
decision_record: Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md
folder_index: Orchestration/decision-runs/2026-08-22-hermes-preinstall/README.md
historical_decision_record: Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-001-provisional-hermes-stack.md
historical_runbook: Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK.md
parent_selection_handover: Orchestration/09-PRIMARY-ORCHESTRATION-SELECTION-HANDOVER.md
parent_selection_handover_status: historical_background_only
parent_mcda_state: Orchestration/mcda-state.yaml
future_alternative_backlog: Orchestration/future-development/OPENCLAW-ALTERNATIVE-EVALUATION.md

selection:
  active_target: hermes_agent_full_stack
  production_winner: null
  confidence_active_target: B+
  confidence_production_fit: C
  openclaw_active_comparison: false
  openclaw_status: deferred_future_operator_decision

non_negotiables:
  full_end_to_end_functionality_required: true
  reduced_scope_mvp_substitute_for_required_capability: forbidden
  custom_orchestration_runtime: forbidden
  custom_memory_sync: forbidden
  custom_kb_engine: forbidden
  custom_rag_server: forbidden
  custom_mcp_server_for_qmd: forbidden
  duplicate_canonical_task_systems: forbidden_by_default
  install_before_human_approval: forbidden
  mass_repo_reorganization_before_validation: forbidden
  custom_code_before_explicit_blocker_decision: forbidden
  implementation_size_is_not_success_metric: true
  upstream_existing_complete_functionality_is_success_metric: true

locked_target_components:
  - hermes_agent
  - hermes_kanban
  - existing_masterofarts_project_folders
  - hermes_hierarchical_project_context
  - bmad
  - marketingskills
  - qmd_official_hermes_integration
  - hermes_memory
  - hermes_curator
  - verified_model_provider_path
  - verified_local_safety_configuration
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
  specialist_skills:
    component: Agent Skills
    status: verified_upstream_hermes_support
    project_location_candidate: .agents/skills
  bmad:
    component: BMAD Method
    status: verified_upstream_install_target_for_hermes
    target_dir: .agents/skills
    global_target_dir: ~/.hermes/skills
    custom_middleware_required: false
  memory:
    component: Hermes MEMORY.md and USER.md
    status: verified_upstream
    role: profile_runtime_memory_not_canonical_project_truth
  curator:
    component: Hermes Curator
    status: verified_upstream
    role: agent_created_skill_lifecycle_audit_backup_rollback
  retrieval:
    baseline: native_file_and_search_tools
    optional_component: QMD
    qmd_status: official_hermes_integration_verified_need_unproven
    qmd_connection: Hermes native MCP client -> local QMD MCP server
    qmd_cloud_required: false
    qmd_platform_gate: official_skill_lists_macos_linux_target_windows_path_must_be_verified
</OLD>
<NEW>
  specialist_skills:
    component: Agent Skills
    status: verified_upstream_hermes_support
    project_location_candidate: .agents/skills
  bmad:
    component: BMAD Method
    status: verified_upstream_install_target_for_hermes
    target_dir: .agents/skills
    global_target_dir: ~/.hermes/skills
    custom_middleware_required: false
    installation_locked_after_validation: true
  marketingskills:
    component: coreyhaines31/marketingskills
    status: verified_upstream_agent_skills_package
    documented_universal_target_dir: .agents/skills
    foundational_context_file: .agents/product-marketing.md
    multi_project_context_fit: research_required
    installation_locked_after_validation: true
  memory:
    component: Hermes MEMORY.md and USER.md
    status: verified_upstream
    role: profile_runtime_memory_not_canonical_project_truth
  curator:
    component: Hermes Curator
    status: verified_upstream
    role: agent_created_skill_lifecycle_audit_backup_rollback
    configuration_fit: research_required
  retrieval:
    component: QMD
    target_status: locked_required_component_pending_preinstall_validation
    qmd_status: official_hermes_integration_verified
    qmd_connection: Hermes native MCP client -> local QMD MCP server/process
    qmd_cloud_required: false
    qmd_canonical_truth: false
    qmd_role: derived_local_retrieval_index_over_project_files
    qmd_platform_gate: official_hermes_skill_lists_macos_linux_target_windows_or_wsl_path_must_be_verified
  safety:
    component: Hermes official security controls
    status: research_required
    target: protect_local_host_and_credentials_without_blocking_normal_moa_work
    custom_guardrail_system: forbidden
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
source_of_truth_policy:
  project_files: existing_repo
  kanban_task_state: hermes_if_candidate_selected
  runtime_memory: noncanonical
  qmd_index: derived_noncanonical
  skills:
    approved_shared: repo_or_pinned_upstream_skill_files
    hermes_learned: hermes_local_until_reviewed
</OLD>
<NEW>
source_of_truth_policy:
  project_files: existing_repo_and_validated_project_local_artifacts
  kanban_task_state: hermes_if_target_selected
  runtime_memory: noncanonical
  qmd_index: derived_noncanonical
  skills:
    approved_shared: repo_or_pinned_upstream_skill_files
    hermes_learned: hermes_local_until_reviewed
  openclaw_state: not_active

research_tracks:
  R01_safety:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md
    status: pending
    blocks_installation: true
  R02_project_knowledge_pm:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md
    status: pending
    blocks_installation: true
  R03_qmd_repo:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R03-HERMES-QMD-REPO-INTEGRATION.md
    status: pending
    blocks_installation: true
    depends_on: R02_project_knowledge_pm
  R04_knowledge_lifecycle:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md
    status: pending
    blocks_installation: true
    depends_on:
      - R02_project_knowledge_pm
      - R03_qmd_repo
  R05_specialist_priming:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md
    status: pending
    blocks_installation: true
    depends_on: R02_project_knowledge_pm
  R06_continuous_learning:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R06-HERMES-CONTINUOUS-LEARNING.md
    status: pending
    blocks_installation: true
    depends_on:
      - R04_knowledge_lifecycle
      - R05_specialist_priming
  R07_marketingskills:
    spec: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md
    status: pending
    blocks_installation: true
    depends_on:
      - R02_project_knowledge_pm
      - R05_specialist_priming
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
hypotheses:
  H1_shared_specialist_across_projects:
    status: open
    pass_condition: one_specialist_definition_same_skills_correct_project_context_no_contamination_no_manual_context_paste
  H2_macro_meso_micro:
    status: open
    pass_condition: hermes_native_boards_tasks_dependencies_workdirs_context_cover_required_levels_without_second_pm_system
  H3_project_knowledge_native:
    status: open
    pass_condition: existing_projects_become_operable_with_minimal_native_context_and_file_organization_no_custom_kb
  H4_qmd_value:
    status: open_optional
    pass_condition: measurable_retrieval_or_token_advantage_and_supported_target_environment
  H5_learning_boundary:
    status: open
    pass_condition: runtime_learning_reusable_without_becoming_competing_project_truth_and_without_cross_runtime_sync
  H6_web_ai_portability:
    status: open
    pass_condition: useful_bounded_repo_tasks_possible_with_clear_distinction_between_file_access_and_native_skill_execution
  H7_openclaw_switch:
    status: open
    pass_condition: openclaw_materially_solves_failed_hermes_requirement_with_less_or_equal_custom_glue
</OLD>
<NEW>
hypotheses:
  H1_shared_specialist_across_projects:
    status: open
    pass_condition: one_specialist_definition_same_skills_correct_project_context_no_contamination_no_manual_context_paste
  H2_macro_meso_micro:
    status: open
    pass_condition: hermes_native_boards_tasks_dependencies_workdirs_context_cover_required_levels_without_second_pm_system
  H3_project_knowledge_native:
    status: open
    pass_condition: existing_projects_become_reliably_operable_with_complete_upstream_consumed_context_and_file_organization_no_custom_kb
  H4_qmd_integration:
    status: open_required
    pass_condition: official_hermes_qmd_path_supported_on_target_environment_scoped_to_real_repo_and_measurably_reduces_retrieval_context_waste_without_custom_connection
  H5_learning_boundary:
    status: open
    pass_condition: runtime_learning_reusable_without_becoming_competing_project_truth_and_without_cross_runtime_sync
  H6_web_ai_portability:
    status: open
    pass_condition: useful_repo_backed_tasks_possible_with_clear_distinction_between_file_access_and_native_skill_execution
  H7_full_stack_completeness:
    status: open
    pass_condition: all_required_user_stories_execute_end_to_end_through_upstream_native_official_or_established_skill_mechanisms_without_reduced_substitutes
  H8_safety_usability:
    status: open
    pass_condition: official_safety_controls_protect_host_credentials_and_high_risk_operations_while_normal_moa_work_remains_practical
  H9_marketingskills_multi_project:
    status: open
    pass_condition: one_upstream_marketingskills_installation_and_shared_marketing_specialist_can_serve_multiple_projects_with_correct_scoped_product_marketing_context
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
user_stories:
  US1_research_to_knowledge_to_workshop:
    status: not_simulated
    required: true
  US2_workshop_to_marketing_launch:
    status: not_simulated
    required: true
  US3_weekly_ceo_cycle:
    status: not_simulated
    required: true
  US4_failure_recovery:
    status: not_simulated
    required: true
  US5_learning_after_success:
    status: not_simulated
    required: true
  US6_shared_marketing_specialist_two_projects:
    status: not_simulated
    required: true
  US7_web_subscription_ai_repo_work:
    status: not_simulated
    required: true
</OLD>
<NEW>
user_stories:
  US1_research_to_knowledge_to_workshop:
    status: not_simulated
    required: true
  US2_workshop_to_marketing_launch:
    status: not_simulated
    required: true
  US3_same_marketing_specialist_second_project:
    status: not_simulated
    required: true
  US4_weekly_ceo_cycle:
    status: not_simulated
    required: true
  US5_failure_recovery:
    status: not_simulated
    required: true
  US6_learning_after_success:
    status: not_simulated
    required: true
  US7_qmd_scoped_retrieval_and_refresh:
    status: not_simulated
    required: true
  US8_safety_allowed_and_blocked_operations:
    status: not_simulated
    required: true
  US9_web_subscription_ai_repo_work:
    status: not_simulated
    required: true
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
phase_gates:
  A_component_map:
    status: pending
    operator_confirmation_required: true
  B_project_knowledge_pm:
    status: pending
    allowed_outcomes:
      - HERMES_NATIVE_SUFFICIENT
      - HERMES_NATIVE_PLUS_OFFICIAL_QMD_SUFFICIENT
      - HERMES_REQUIRES_CUSTOM_KB_OR_SECOND_PM_SYSTEM
  C_shared_specialists_bmad:
    status: pending
  D_user_story_simulations:
    status: pending
  E_qmd_decision:
    status: pending
    allowed_outcomes:
      - QMD_NOT_NEEDED
      - QMD_OFFICIAL_PATH_SUPPORTED
      - QMD_VALUE_HIGH_BUT_PLATFORM_BLOCKED
      - QMD_REQUIRES_CUSTOM_WORK
  F_web_ai_interop:
    status: pending
  G_token_cost_privacy:
    status: pending
  H_openclaw_gap_comparison:
    status: pending
  I_final_decision:
    status: pending
    allowed_decisions:
      - APPROVE_INSTALL_HERMES
      - APPROVE_INSTALL_OPENCLAW
      - RESEARCH_ONE_BLOCKER
      - REJECT_CURRENT_FINALISTS
</OLD>
<NEW>
phase_gates:
  A_component_map:
    status: pending
    operator_confirmation_required: true
  B_safety:
    status: pending
  C_project_knowledge_pm:
    status: pending
  D_qmd_integration:
    status: pending
  E_project_knowledge_lifecycle:
    status: pending
  F_shared_specialists_priming:
    status: pending
  G_continuous_learning:
    status: pending
  H_marketingskills:
    status: pending
  I_integrated_user_story_simulations:
    status: pending
  J_token_cost_privacy:
    status: pending
  K_installation_blueprint:
    status: pending
  L_final_decision:
    status: pending
    allowed_decisions:
      - APPROVE_INSTALL_HERMES_TARGET_STACK
      - RESEARCH_BLOCKER
      - REJECT_HERMES_TARGET_STACK
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
hard_fail_conditions:
  - custom_core_orchestration_required
  - custom_memory_synchronization_required
  - custom_kb_or_rag_required_for_basic_operation
  - more_than_one_canonical_task_state_required
  - specialist_definitions_must_be_duplicated_per_project
  - manual_context_copy_paste_required_for_normal_handoffs
  - no_durable_failure_recovery
  - unacceptable_private_data_egress_without_operator_approval
  - more_than_10_percent_project_specific_infrastructure_needed
</OLD>
<NEW>
hard_fail_conditions:
  - custom_core_orchestration_required
  - custom_memory_synchronization_required
  - custom_kb_or_rag_required_for_basic_operation
  - custom_qmd_or_mcp_wrapper_required
  - more_than_one_canonical_task_state_required
  - specialist_definitions_must_be_duplicated_per_project
  - manual_context_copy_paste_required_for_normal_handoffs
  - no_durable_failure_recovery
  - unacceptable_private_data_egress_without_operator_approval
  - required_capability_replaced_with_reduced_or_mvp_substitute
  - safety_configuration_blocks_normal_required_work
  - qmd_target_environment_requires_unsupported_hack
  - marketingskills_requires_custom_fork_for_basic_multi_project_use
</NEW>

/Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
<OLD>
verified_sources:
  hermes_context: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
  hermes_kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
  hermes_skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
  hermes_memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
  hermes_curator: https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
  hermes_providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
  hermes_qmd: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
  hermes_platform_support: https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
  bmad_platform_targets: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml
  project_scope: Orchestration/03-SCOPE-LOCK.md
  operating_model: Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md
  existing_pilot_protocol: Orchestration/02-PILOT-PROTOCOL.md

next_action:
  owner: separate_validation_chat
  instruction: execute_QA_VALIDATION_RUNBOOK_interactively_without_installing_anything
  completion_condition: explicit_human_decision_from_phase_I
</OLD>
<NEW>
verified_sources:
  hermes_context: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
  hermes_kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
  hermes_skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
  hermes_memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
  hermes_curator: https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
  hermes_security: https://hermes-agent.nousresearch.com/docs/user-guide/security/
  hermes_secure_work_machine: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
  hermes_providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
  hermes_qmd: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
  hermes_platform_support: https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
  qmd_repo: https://github.com/tobi/qmd
  bmad_platform_targets: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml
  marketingskills_repo: https://github.com/coreyhaines31/marketingskills
  marketingskills_product_marketing: https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md
  project_scope: Orchestration/03-SCOPE-LOCK.md
  operating_model: Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md
  existing_pilot_protocol: Orchestration/02-PILOT-PROTOCOL.md

next_action:
  owner: separate_validation_chat
  instruction: execute_QA_VALIDATION_RUNBOOK_v2_interactively_starting_with_phase_A_then_research_tracks
  installation_before_completion: forbidden
  completion_condition: explicit_human_decision_from_phase_L
</NEW>

/Orchestration/mcda-state.yaml
<OLD>
schema_version: 2
project: master-of-arts-integrated-agent-operating-system-selection
initialized: 2026-08-21
repository: leela-spec/MasterOfArts
branch: main
phase: integrated_full_stack_agent_ecosystem_research_required
selection_status: none
implementation_authorized: false

operator_decisions:
  weight_profile: balanced
  scope_status: corrected_and_locked
  scope_authority: operator_supplied_master_of_arts_project_description_plus_2026_08_21_agent_integration_feedback

objective: >-
  Select an existing battle-proven integrated operating stack for Master of Arts in
  which shared knowledge and portfolio state drive reusable workflows that activate
  specialist agents, tools and reviewers; available subscription/local AI clients
  execute those roles; consequential choices stop at CEO gates; finished outputs,
  provenance and validated learning persist for reuse.

hard_rule: >-
  Reuse before invention. Prefer established integrated ecosystems, official packs,
  marketplaces, plugins and portable skill standards before creating MoA-specific
  orchestration, agents, workflows, memory, knowledge infrastructure or project state.
</OLD>
<NEW>
schema_version: 3
project: master-of-arts-integrated-agent-operating-system-selection
initialized: 2026-08-21
last_updated: 2026-08-22
repository: leela-spec/MasterOfArts
branch: main
phase: hermes_full_functional_preinstall_validation
selection_status: provisional_hermes_target_selected_for_realization
implementation_authorized: false

operator_decisions:
  weight_profile: balanced
  scope_status: corrected_and_locked
  scope_authority: operator_supplied_master_of_arts_project_description_plus_2026_08_22_realization_feedback
  active_target: hermes_agent_full_stack
  qmd_target: required_pending_validation
  marketingskills_target: required_pending_validation
  openclaw_status: deferred_future_operator_decision
  reduced_scope_or_mvp_substitute: prohibited

objective: >-
  Validate whether the complete Hermes-centered Master of Arts operating stack works
  end to end using existing upstream mechanisms: Hermes Agent, Hermes Kanban, existing
  project folders, hierarchical project context, BMAD, MarketingSkills, official QMD
  integration, provider execution, memory/Curator learning and low-friction official
  safety controls. Do not install until the complete stack and real user stories are
  verified and the human CEO explicitly approves installation.

hard_rule: >-
  Reuse before invention. A required capability must work completely through an
  upstream-native capability, official integration/plugin/skill, established portable
  Agent Skills package, or documented configuration. Do not replace a required capability
  with a smaller, minimal, MVP, toy or reduced substitute simply because that substitute
  is easy to implement. Custom orchestration, KB, memory synchronization, retrieval/MCP
  wrappers and other replacement subsystems are not authorized in this validation phase.
</NEW>

/Orchestration/mcda-state.yaml
<OLD>
reuse_order_per_capability:
  - existing_integrated_ecosystem_with_relevant_agent_workflow_skill
  - official_upstream_marketplace_pack_plugin_or_skill
  - portable_established_agent_or_skill_package
  - project_specific_configuration_of_established_component
  - custom_moa_role_only_if_no_proven_option_exists

candidate_reclassification:
  github_issues_projects:
    role: foundational_portfolio_state_component
    not_full_system: true
  github_spec_kit:
    role: foundational_workflow_control_component
    not_full_system: true
  beads:
    role: agent_task_graph_component
    not_full_system: true
  openspec:
    role: change_control_component_or_method_donor
    not_full_system: true
  task_master:
    role: task_decomposition_component
    not_full_system: true
  bmad_method:
    role: integrated_agent_and_workflow_ecosystem_candidate
    reconsider: true
  superpowers:
    role: specialist_skill_and_review_workflow_ecosystem_candidate
    reconsider: true
  ruflo:
    role: integrated_orchestration_agent_workflow_memory_ecosystem_candidate
    reconsider: true
  gas_city:
    role: packaged_multi_agent_workflow_runtime_candidate
    reconsider_subject_to_nonsoftware_fit: true
  hermes:
    role: executor_plus_skills_delegation_memory_runtime_candidate
    reconsider: true
  openclaw:
    role: executor_plus_subagents_skills_automation_runtime_candidate
    reconsider: true
</OLD>
<NEW>
reuse_order_per_capability:
  - existing_integrated_ecosystem_with_relevant_agent_workflow_skill
  - official_upstream_marketplace_pack_plugin_or_skill
  - portable_established_agent_or_skill_package
  - documented_project_specific_configuration_of_established_component
  - stop_and_record_blocker_if_complete_required_function_would_need_custom_subsystem

candidate_reclassification:
  github_issues_projects:
    role: foundational_portfolio_state_component
    not_full_system: true
    active_target: false
  github_spec_kit:
    role: foundational_workflow_control_component
    not_full_system: true
    active_target: false
  beads:
    role: agent_task_graph_component
    not_full_system: true
    active_target: false
  openspec:
    role: change_control_component_or_method_donor
    not_full_system: true
    active_target: false
  task_master:
    role: task_decomposition_component
    not_full_system: true
    active_target: false
  bmad_method:
    role: required_upstream_agent_and_workflow_package_in_hermes_target
    active_target: true
  marketingskills:
    role: required_upstream_marketing_agent_skills_package_in_hermes_target
    active_target: true
  qmd:
    role: required_official_hermes_retrieval_integration_pending_validation
    active_target: true
  hermes:
    role: active_primary_orchestration_runtime_target
    active_target: true
  openclaw:
    role: deferred_alternative_orchestration_system
    active_target: false
    deferred_to: Orchestration/future-development/OPENCLAW-ALTERNATIVE-EVALUATION.md
</NEW>

/Orchestration/mcda-state.yaml
<OLD>
previous_mcda_status:
  spec_kit_github_score_91_2:
    valid_for: project_and_workflow_control_layer_only
    invalid_for: complete_integrated_master_of_arts_agent_operating_system
  previous_finalists:
    status: demoted_to_layer_candidates
    reason: operator_requires_integrated_specialist_agents_workflows_knowledge_and_executors
</OLD>
<NEW>
previous_mcda_status:
  complete_system_research:
    status: closed_for_current_phase
    result: hermes_selected_as_first_full_stack_realization_target
    note: selection_is_not_production_install_approval
  spec_kit_github_score_91_2:
    valid_for: project_and_workflow_control_layer_only
    invalid_for: complete_integrated_master_of_arts_agent_operating_system
  prior_alternatives:
    status: historical_evidence_only_until_explicitly_reopened
</NEW>

/Orchestration/mcda-state.yaml
<OLD>
complete_system_proof_questions:
  - which_specialist_agents_and_workflows_already_exist
  - are_they_battle_tested_and_maintained
  - can_they_be_installed_or_reused_instead_of_rewritten
  - can_subscription_and_local_ai_clients_execute_or_participate
  - how_does_the_orchestrator_choose_and_activate_agents
  - how_is_relevant_knowledge_retrieved_for_each_agent
  - how_do_agents_share_and_handoff_durable_state
  - how_are_reviewers_separated_from_makers
  - which_steps_are_deterministic
  - where_do_outputs_and_provenance_live
  - how_does_validated_learning_return_to_the_kb
  - can_ceo_view_priorities_exceptions_and_decisions_without_agent_chatter
  - can_same_system_produce_research_workshops_content_operations_and_leela_outputs
  - what_custom_work_remains_and_can_another_existing_ecosystem_reduce_it
</OLD>
<NEW>
complete_system_proof_questions:
  - do_all_required_components_have_current_upstream_install_and_integration_paths
  - can_hermes_operate_macro_meso_micro_projects_without_custom_project_framework
  - can_existing_project_files_become_current_retrievable_context_without_custom_kb
  - can_qmd_index_and_retrieve_real_repo_content_through_official_hermes_integration
  - can_bmad_and_marketingskills_be_installed_and_used_without_custom_middleware_or_fork
  - can_one_shared_specialist_work_across_multiple_projects_without_context_contamination
  - can_hermes_continuous_learning_reuse_procedures_without_competing_project_truth
  - can_official_safety_controls_protect_the_local_machine_without_blocking_normal_work
  - which_steps_are_deterministic_and_which_require_semantic_model_calls
  - what_context_tokens_and_external_data_egress_each_step_causes
  - can_web_subscription_ai_clients_use_the_same_repo_artifacts_truthfully_with_their_actual_capabilities
  - can_interrupted_work_resume_from_durable_state_without_chat_archaeology
  - do_research_workshop_content_operations_and_portfolio_user_stories_work_end_to_end
</NEW>

/Orchestration/mcda-state.yaml
<OLD>
next_decision:
  owner: research_process
  action: research_and_rank_complete_integrated_agent_ecosystems_or_minimal_proven_compositions
  sequence:
    - search_existing_integrated_agent_ecosystems_and_official_agent_skill_workflow_libraries
    - map_verified_specialist_agents_workflows_tools_memory_and_executor_support
    - construct_complete_candidate_architectures_using_only_documented_integrations
    - score_complete_architectures_not_isolated_tools
    - retain_simple_control_architecture
    - select_two_or_three_complete_pilot_stacks
    - run_same_end_to_end_moa_output_workflows
    - present_operator_decision_with_concrete_user_stories_and_failure_modes
</OLD>
<NEW>
active_decision_run:
  root: Orchestration/decision-runs/2026-08-22-hermes-preinstall
  decision_record: Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md
  runbook: Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK-v2.md
  machine_state: Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml
  research_specs:
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R03-HERMES-QMD-REPO-INTEGRATION.md
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R06-HERMES-CONTINUOUS-LEARNING.md
    - Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md

next_decision:
  owner: separate_validation_chat_plus_human_ceo
  action: execute_full_functional_hermes_preinstall_validation
  sequence:
    - verify_target_component_edges
    - research_and_select_low_friction_official_hermes_safety_profile
    - validate_macro_meso_micro_project_and_knowledge_model
    - validate_qmd_integration_against_real_repo
    - validate_project_knowledge_freshness_and_lifecycle
    - validate_shared_specialist_and_skill_priming
    - validate_hermes_continuous_learning_and_curator_boundaries
    - validate_marketingskills_multi_project_context
    - run_integrated_user_story_simulations
    - audit_tokens_determinism_cost_privacy_and_web_ai_access
    - produce_official_installation_blueprint_without_executing_it
    - obtain_explicit_ceo_install_or_reject_decision
  allowed_outcomes:
    - APPROVE_INSTALL_HERMES_TARGET_STACK
    - RESEARCH_BLOCKER
    - REJECT_HERMES_TARGET_STACK
</NEW>
```

## Verification requirement

After application, verify:

1. active `state.yaml` points to ADR-002 and runbook v2;
2. no active state field treats OpenClaw as a current challenger;
3. no active state field uses the former 5–10% custom-infrastructure target;
4. QMD and MarketingSkills are locked target components pending validation;
5. all seven research specs exist;
6. `mcda-state.yaml` phase is `hermes_full_functional_preinstall_validation`;
7. final installation remains unauthorized.
