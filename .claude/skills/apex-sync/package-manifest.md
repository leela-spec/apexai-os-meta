# Apex Sync Package Manifest

```yaml
package_manifest:
  package_name: apex-sync
  package_path: ".claude/skills/apex-sync/"
  package_role: deterministic_read_side_synchronization
  generated_files:
    - path: ".claude/skills/apex-sync/SKILL.md"
      purpose: "Skill entrypoint, routing description, compact procedure, failure modes, output requirements, and completion gate."
      canonical_source_for:
        - skill_invocation
        - supporting_file_loading
        - completion_gate

    - path: ".claude/skills/apex-sync/references/sync-cluster-contract.md"
      purpose: "Canonical owner for package_boundary, process_scope, apex_plan_boundary, and apex_session_boundary."
      canonical_source_for:
        - sync_cluster_contract

    - path: ".claude/skills/apex-sync/references/script-command-contract.md"
      purpose: "Canonical owner for command_interface, subcommand_contracts, global_flags, exit_code_policy, and json_output_policy."
      canonical_source_for:
        - script_command_contract

    - path: ".claude/skills/apex-sync/references/registry-and-drift-rules.md"
      purpose: "Canonical owner for registry_schema, registry_rebuild_rules, drift_detection_rules, and malformed_file_policy."
      canonical_source_for:
        - registry_and_drift_rules

    - path: ".claude/skills/apex-sync/references/scoring-and-focus-rules.md"
      purpose: "Canonical owner for priority_score_policy, urgency_score_policy, unlock_depth_policy, and focus_candidate_sort_policy."
      canonical_source_for:
        - scoring_and_focus_rules

    - path: ".claude/skills/apex-sync/package-manifest.md"
      purpose: "Lightweight package inventory and acceptance checklist."
      canonical_source_for:
        - package_inventory

    - path: "apex-meta/scripts/apex_sync.py"
      purpose: "Canonical owner for executable_subcommands, read_only_behavior, registry_write_behavior, and standard_library_implementation."
      canonical_source_for:
        - python_cli_contract

  required_outputs:
    - next_action_report
    - blocker_report
    - registry_report
    - stall_report
    - drift_report
    - score_report
    - focus_candidate_report
    - dependency_validation_report

  acceptance_checks:
    required_files_present: true
    exact_file_count: 7
    standard_library_only_python: true
    no_bash_or_typescript_or_javascript: true
    read_only_by_default: true
    registry_is_only_allowed_write: true
    task_files_are_not_mutated: true
    handoff_files_are_not_mutated: true
    entity_files_are_not_mutated: true
    skill_files_are_not_mutated: true
    schema_owners_are_unique: true
    yaml_blocks_use_2_space_indentation: true
    canonical_key_names_preserved: true

  review_flags:
    - malformed_frontmatter
    - missing_task_id
    - unsupported_status
    - missing_dependency_target
    - circular_dependency_risk
    - blocked_without_reason
    - stale_task_candidate
    - registry_out_of_date
    - drift_detected
    - script_failed

## Manifest Notes

This manifest is an inventory. It does not redefine the command contract, registry schema, scoring rules, or package boundary. Use the listed canonical_source entries to locate the owning contract.
