# ChatGPT Workspace Patch-Only Mutation Policy — Enterprise / Business Handover

```okf
handover:
  id: chatgpt-workspace-patch-only-mutation-policy
  status: operator_mandated
  criticality: highest
  scope:
    organizational: entire_ChatGPT_Business_or_Enterprise_workspace
    surfaces:
      - normal_ChatGPT_chats
      - ChatGPT_projects
      - shared_projects
      - custom_GPTs
      - Workspace_Agents
      - ChatGPT_Work
      - Codex
      - repository_coding_agents
      - CLI_agents_when_given_this_policy
  purpose: >
    Prevent AI agents from damaging unrelated content when modifying existing
    files by prohibiting conversational whole-file reconstruction and requiring
    surgical patch-based mutation with explicit diff verification.

  core_rule: >
    EXISTING FILES MUST BE MODIFIED ONLY THROUGH SURGICAL PATCHES.
    An agent must never rewrite or replace an existing file merely to change a
    subset of its content. Generate and apply an exact patch against the current
    file/base revision, then inspect the resulting diff before commit or push.

  precedence:
    operator_rule: mandatory
    override_allowed_only_when:
      - operator_explicitly_authorizes_full_file_replacement_for_that_specific_change
      - file_is_generated_deterministically_from_an_authoritative_source
      - entire_existing_file_is_intentionally_being_replaced_as_the_task_itself
```

## 1. Canonical mutation policy

```okf
mutation_policy:
  default_for_existing_files: patch_only

  patch_definition:
    accepted_forms:
      - unified_diff
      - git_apply_compatible_patch
      - deterministic_edit_operation_that_changes_only_explicitly_targeted_ranges
    preferred_form: unified_diff

  required_before_patch:
    - read_current_target_file_or_exact_relevant_context
    - identify_current_base_commit_or_blob_revision_when_available
    - identify_exact_target_region_and_anchors
    - preserve_all_unrelated_content

  required_after_patch:
    - verify_patch_applied_without_fuzzy_reconstruction
    - inspect_git_diff_or_equivalent_exact_diff
    - verify_only_intended_files_changed
    - verify_only_intended_hunks_changed
    - run_diff_syntax_check_when_git_is_available
    - run_targeted_validation_or_tests_when_applicable

  prohibited:
    - whole_file_rewrite_for_partial_change
    - reconstructing_unrelated_sections_from_model_context
    - silently_reformatting_untouched_content
    - opportunistic_cleanup_outside_the_requested_hunk
    - renaming_reordering_or_compressing_unrelated_content
    - deleting_adjacent_material_because_it_looks_stale
    - using_complete_file_replacement_APIs_as_if_they_were_patch_APIs
    - assuming_a_file_blob_SHA_protects_against_semantic_rewrite_damage

  fail_closed_when:
    - target_context_does_not_match_expected_base
    - patch_hunk_does_not_apply_cleanly
    - current_file_differs_materially_from_the_version_used_to_create_patch
    - agent_cannot_verify_the_resulting_diff

  fail_closed_action: >
    Do not improvise a replacement file. Stop the mutation, report the mismatch,
    reread the current file, and regenerate a new surgical patch from current
    evidence.
```

## 2. Allowed direct-write exceptions

```okf
direct_write_policy:
  new_file:
    allowed: true
    reason: no_existing_content_can_be_destroyed

  existing_small_file:
    default: patch_only
    full_replace_allowed: false

  deterministic_generated_file:
    full_replace_allowed: conditional
    conditions:
      - authoritative_generator_or_source_exists
      - regeneration_is_the_defined_workflow
      - output_can_be_deterministically_verified

  intentional_total_replacement:
    full_replace_allowed: conditional
    conditions:
      - total_replacement_is_the_explicit_task
      - operator_or_authoritative_spec_supports_the_replacement
      - old_file_is_preserved_in_git_history_or_other_required_audit_surface

  explicit_operator_exception:
    full_replace_allowed: true
    requirement: exception_must_be_specific_to_the_target_change
```

## 3. Required patch workflow

```okf
patch_workflow:
  S1_read:
    actions:
      - resolve_repository_and_branch
      - read_current_target_file
      - resolve_current_base_commit_when_available
      - locate_smallest_valid_change_region

  S2_construct:
    artifact: exact_patch
    requirements:
      - minimal_hunks
      - sufficient_context_lines_for_safe_application
      - no_unrelated_normalization
      - no_hidden_semantic_changes

  S3_preflight:
    preferred_command: git_apply_check
    examples:
      powershell:
        - "git apply --check <patch-file>"
    on_failure: regenerate_from_current_file

  S4_apply:
    preferred_command: git_apply
    examples:
      powershell:
        - "git apply <patch-file>"

  S5_verify:
    examples:
      powershell:
        - "git diff --check"
        - "git diff -- <target-files>"
        - "git status --short"
    required_assertions:
      - intended_files_only
      - intended_hunks_only
      - unrelated_content_byte_or_semantically_unchanged

  S6_validate:
    actions:
      - run_targeted_tests_if_applicable
      - run_lint_or_schema_validation_if_applicable
      - inspect_semantic_result

  S7_publish:
    prerequisites:
      - diff_verified
      - tests_or_validation_satisfactory
    actions:
      - commit
      - push
```

## 4. Patch artifact contract

```okf
patch_artifact:
  required_metadata:
    - repository
    - target_branch
    - base_commit_or_revision
    - target_files
    - purpose
    - expected_semantic_delta

  required_body:
    format: unified_diff_preferred

  required_invariants:
    - apply_only_against_matching_context
    - no_fuzzy_manual_reconstruction
    - no_unrelated_file_edits
    - no_unrelated_hunk_edits
    - preserve_existing_structure_outside_patch

  recommended_companion_checks:
    - git_apply_check
    - git_diff_check
    - targeted_git_diff
    - targeted_tests
```

## 5. Why this must be propagated at multiple ChatGPT layers

```okf
propagation_model:
  principle: >
    Do not assume one ChatGPT instruction surface automatically reaches all
    projects, GPTs, agents, or Codex environments. Reinforce the same compact
    canonical rule at every instruction boundary that can independently govern
    an agent.

  enterprise:
    workspace_instructions:
      priority: highest_chat_surface
      action: install_compact_core_rule
    workspace_policy:
      role: human_facing_governance_reminder
      action: mention_patch_only_file_mutation_policy
    project_instructions:
      action: include_compact_core_rule_in_every_code_or_repository_project
      reason: project_instructions_govern_project_chats
    custom_GPTs:
      action: include_rule_in_each_GPT_instruction_set
      reason: custom_GPTs_do_not_inherit_global_custom_instructions
    workspace_agents:
      action:
        - include_rule_in_agent_instructions
        - preferably_attach_shared_patch_only_skill_where_available
      reason: Workspace_Agents_have_their_own_reusable_instructions_and_skills
    codex:
      action:
        - place_short_rule_in_root_AGENTS.md_or_AGENTS.override.md
        - point_to_this_canonical_policy_or_repo_specific_policy
      reason: Codex_reads_AGENTS_instruction_files_by_directory_scope

  business:
    user_custom_instructions:
      action: install_compact_core_rule_for_normal_chats
      limitation: not_sufficient_for_GPTs_or_project_override_cases
    project_instructions:
      action: include_compact_core_rule_in_every_code_or_repository_project
      reason: project_instructions_override_global_custom_instructions_inside_project
    custom_GPTs:
      action: include_rule_in_each_GPT_instruction_set
      reason: custom_GPTs_do_not_use_custom_instructions
    workspace_agents:
      action:
        - include_rule_in_agent_instructions
        - preferably_attach_shared_patch_only_skill_where_available
    codex:
      action:
        - place_short_rule_in_root_AGENTS.md_or_AGENTS.override.md

  warning: >
    Human-facing workspace policy notices alone are not sufficient technical
    enforcement. The rule must exist in the actual instruction context used by
    each autonomous or coding surface.
```

## 6. Compact instruction payload to install everywhere

```okf
compact_instruction:
  id: PATCH_ONLY_EXISTING_FILES
  text: >
    PATCH-ONLY FILE MUTATION: For every existing file, make changes only through
    a surgical patch/diff against the current file. Never rewrite, regenerate,
    or replace the whole file to implement a partial change. Preserve all
    unrelated content exactly. Preflight the patch against current context,
    apply it, then inspect the exact resulting diff before commit/push. If a
    patch does not apply cleanly or current context differs, stop and regenerate
    the patch from the current file; never improvise a whole-file replacement.
    Direct full writes are allowed only for genuinely new files, deterministic
    generated files, explicit total-file replacement tasks, or a specific
    operator-authorized exception.
```

## 7. Enterprise deployment handover

```okf
enterprise_deployment:
  admin_surface:
    - Workspace_settings
    - General
    - Workspace_Instructions
  install:
    - compact_instruction.text

  human_policy_surface:
    - Workspace_Policy
  human_policy_message: >
    Existing repository and document files must be edited through reviewable
    patches/diffs. Whole-file replacement for partial edits is prohibited.

  projects:
    action: >
      Add compact_instruction.text to Project Instructions for every shared or
      private project that can mutate files. Do not assume Workspace Instructions
      eliminate the need for project-level reinforcement where project-specific
      instructions govern context.

  GPTs:
    action: >
      Add compact_instruction.text to the Instructions of every GPT capable of
      editing repository/document files.

  Workspace_Agents:
    action: >
      Add compact_instruction.text to agent Instructions. Prefer one shared
      reusable patch-only skill containing the full policy, then attach that skill
      to every file-mutating agent; keep the compact rule directly in agent
      instructions as the non-negotiable trigger.

  Codex_and_repo_agents:
    action: >
      Put the compact rule in repository-root AGENTS.md (or applicable
      AGENTS.override.md). Keep AGENTS.md short and link to a canonical detailed
      policy rather than duplicating a large manual.
```

## 8. Business deployment handover

```okf
business_deployment:
  normal_chat:
    surface:
      - Settings
      - Personalization
      - Custom_Instructions
    install:
      - compact_instruction.text

  limitation: >
    Treat Custom Instructions as one layer only. Project Instructions override
    global custom instructions inside projects, and custom GPTs do not use saved
    custom instructions. Therefore the patch-only rule must also be installed at
    those independent instruction boundaries.

  projects:
    action: add_compact_rule_to_each_file_mutating_project_instruction_set

  GPTs:
    action: add_compact_rule_to_each_file_mutating_GPT_instruction_set

  Workspace_Agents:
    action:
      - add_compact_rule_to_agent_instructions
      - attach_shared_patch_only_skill_when_supported_and_managed

  Codex_and_repo_agents:
    action: add_compact_rule_to_root_AGENTS_md_or_AGENTS_override_md
```

## 9. Repository enforcement pattern

```okf
repository_enforcement:
  root_instruction_file:
    preferred: AGENTS.md
    purpose: short_high_priority_agent_map_and_patch_only_trigger

  canonical_policy_file:
    purpose: detailed_policy_system_of_record
    recommendation: >
      Keep the root AGENTS.md short. Point to one canonical policy file containing
      the detailed patch workflow, exceptions, and validation rules.

  local_overrides:
    allowed: true
    constraint: may_strengthen_but_must_not_weaken_patch_only_rule_without_explicit_operator_authority

  mechanical_enforcement_recommended:
    - git_diff_check_before_commit
    - patch_preflight
    - changed_file_allowlist_when_task_is_bounded
    - review_exact_diff_before_push
```

## 10. Agent self-check

```okf
agent_pre_mutation_check:
  questions:
    - is_target_a_preexisting_file
    - is_change_partial
    - do_i_have_current_file_context
    - do_i_have_a_surgical_patch
    - does_patch_apply_cleanly
    - will_i_inspect_exact_resulting_diff

  decision:
    existing_file_and_partial_change:
      required_method: patch
    new_file:
      direct_create_allowed: true
    uncertain:
      action: do_not_mutate_until_current_context_and_patch_are_available
```

## 11. Compliance examples

```okf
examples:
  compliant_existing_file:
    task: change_one_section_in_SKILL_md
    method:
      - read_current_section_and_anchors
      - create_unified_diff
      - git_apply_check
      - git_apply
      - git_diff_check
      - inspect_targeted_diff

  noncompliant_existing_file:
    task: change_one_section_in_SKILL_md
    forbidden_method: >
      Generate a complete replacement SKILL.md from model context and submit it
      through a whole-file update API.

  compliant_new_file:
    task: create_new_handover
    method: direct_create_file

  exception:
    task: regenerate_lockfile_from_package_manager
    method: deterministic_full_regeneration
    condition: authoritative_tool_output_and_diff_review
```

## 12. Implementation priority

```okf
rollout_order:
  1: install_compact_rule_at_highest_available_workspace_or_user_instruction_layer
  2: install_rule_in_all_active_file_mutating_projects
  3: install_rule_in_all_custom_GPTs_that_can_modify_files
  4: install_rule_in_all_Workspace_Agents_that_can_modify_files
  5: add_or_patch_root_AGENTS_md_in_each_active_repository
  6: add_shared_patch_only_skill_for_Workspace_Agents_if_operationally_useful
  7: audit_agent_and_project_inventory_for_missing_instruction_coverage

  success_condition: >
    Every independent AI surface capable of modifying files receives the
    PATCH_ONLY_EXISTING_FILES instruction directly or through an instruction
    mechanism proven to be in its runtime context.
```

## 13. Evidence basis

```okf
evidence_basis:
  researched_date: 2026-08-18
  official_OpenAI_findings:
    - Enterprise_admin_guidance_identifies_Workspace_Instructions_and_Workspace_Policy_as_workspace_level_user_guidance_surfaces
    - Custom_Instructions_apply_to_normal_chats_but_are_user_level
    - Project_Instructions_apply_inside_the_project_and_override_global_Custom_Instructions
    - Shared_project_chats_use_project_context_and_instructions
    - Custom_GPTs_have_their_own_instructions_and_do_not_use_saved_memory_or_Custom_Instructions
    - Workspace_Agents_have_reusable_agent_instructions_and_can_attach_skills
    - Codex_is_guided_by_AGENTS_md_files_with_directory_scoping
    - OpenAI_recommends_short_AGENTS_md_maps_instead_of_monolithic_instruction_manuals_for_large_agentic_repositories

  design_inference: >
    Because instruction inheritance differs across ChatGPT surfaces, no single
    current mechanism should be assumed to govern every chat, project, GPT,
    Workspace Agent, and Codex run. A layered propagation strategy with one
    canonical compact rule and repo-local enforcement is the resilient design.
```

## 14. Operator handoff

```okf
next_operator_or_admin_action:
  objective: deploy_patch_only_rule_across_workspace
  use_this_file_as: canonical_handover_and_policy_source
  do_not:
    - manually_rephrase_rule_differently_for_each_agent
    - weaken_rule_for_convenience
    - assume_custom_instructions_reach_GPTs
    - assume_project_instructions_inherit_global_custom_instructions
    - rely_only_on_human_policy_modal

  preferred_execution: >
    Copy the compact instruction verbatim into each applicable ChatGPT
    instruction surface, then add repository AGENTS.md enforcement through
    surgical patches. Maintain this file as the canonical detailed policy.
```
