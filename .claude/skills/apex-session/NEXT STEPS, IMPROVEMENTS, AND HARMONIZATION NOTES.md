# NEXT STEPS, IMPROVEMENTS, AND HARMONIZATION NOTES

Review the package in four passes. First, verify the mutation gate wording: every mutation must remain a proposal until `confirmation_token` is exactly `CONFIRM`, `CONFIRM WRITE`, or `CONFIRM MUTATION`. Second, verify that every mutation path has a `before_after_mutation_preview`. Third, verify that raw source policy is intact: `apex-meta/raw/` is preserved and entity files under `apex-meta/entities/` update only after confirmation. Fourth, verify that `next-session.md` contains Current Step, Open Items, Risks, Decisions Made, and Next Actions.

Suggested manual tests: missing confirmation, ambiguous status delta, uncertain entity update, duplicate entity risk, next-session context generation, and planning_layer_feed generation.

Harmonize against `apex-plan` by checking that apex-plan creates proposed task records, owns decomposition and rationale, and leaves confirmed state-delta capture to apex-session. Harmonize against `apex-sync` by checking that apex-sync computes stall, drift, registry, scores, blocker scans, and focus ordering, while apex-session only requests sync when needed.

Future improvements: add fixture-based manual tests later, add a mutation audit template after real task files exist, and add an `entity_type` taxonomy after the first real entity updates.

# VALIDATION REPORT

```
validation:  required_mapping_source_used: true  decisions_md_used_if_available: true  no_web_search: true  no_repo_write: true  output_is_chat_file_blocks_only: true  no_scripts_generated: true  no_bash_or_python_or_typescript_or_javascript_generated: true  status_enum_preserved: true  depends_on_preserved: true  handoff_format_preserved: true  mutation_gate_required: true  accepted_confirm_tokens_preserved: true  raw_source_preservation_policy_present: true  canonical_key_names_preserved: true  file_schema_ownership_preserved: true  all_yaml_blocks_use_2_space_indentation: true  no_collapsed_yaml_blocks: true  no_duplicate_schema_definitions: true  non_goals_are_imperative: true  apex_plan_boundary_preserved: true  apex_sync_boundary_preserved: true  skill_best_practice_structure_followed: true
```