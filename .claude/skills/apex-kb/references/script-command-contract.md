# Apex KB Script Command Contract
```yaml
script_command_contract:
  artifact_name: apex_kb_script_command_contract
  file_role: deterministic_python_command_interface_contract
  package_path: ".claude/skills/apex-kb/"
  script_path: "apex-meta/scripts/apex_kb.py"
  canonical_rules:
    kb_contract: ".claude/skills/apex-kb/references/kb-contract.md"
    operation_rules: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
  purpose: >
    Define the deterministic Python interface used by apex-kb for scaffold,
    source hashing, preflight validation, manifest checks, index structure
    generation, link validation, orphan detection, stale-index detection, and
    audit listing. This contract does not define semantic extraction, page
    drafting, contradiction interpretation, or query synthesis.
  runtime_policy:
    language: python
    python_version_floor: "3.10"
    standard_library_only: true
    external_dependencies_allowed: false
    shell_out_allowed: false
    bash_allowed: false
    javascript_allowed: false
    typescript_allowed: false
    package_manager_allowed: false
    network_access_allowed: false
  write_policy:
    default_mode: dry_run
    destructive_writes_allowed: false
    write_outside_kb_root_allowed: false
    writes_require_explicit_flag: true
    semantic_writes_allowed: false
    script_may_create_or_update:
      - "apex-meta/kb/<kb-slug>/README.md"
      - "apex-meta/kb/<kb-slug>/kb-schema.md"
      - "apex-meta/kb/<kb-slug>/raw/"
      - "apex-meta/kb/<kb-slug>/ingest-analysis/"
      - "apex-meta/kb/<kb-slug>/wiki/index.md"
      - "apex-meta/kb/<kb-slug>/wiki/concepts/"
      - "apex-meta/kb/<kb-slug>/wiki/entities/"
      - "apex-meta/kb/<kb-slug>/wiki/summaries/"
      - "apex-meta/kb/<kb-slug>/manifests/source-manifest.json"
      - "apex-meta/kb/<kb-slug>/audit/"
      - "apex-meta/kb/<kb-slug>/audit/resolved/"
      - "apex-meta/kb/<kb-slug>/outputs/queries/"
      - "apex-meta/kb/<kb-slug>/log/"
```


#

# Command Surface
```yaml
command_surface:
  invocation_pattern: >
    python apex-meta/scripts/apex_kb.py [global-options] <subcommand> [subcommand-options]
  global_arguments:
    kb_root:
      flag: "--kb-root"
      required: true
      value_type: path
      description: "Path to one Apex KB root, usually apex-meta/kb/<kb-slug>/."
    json:
      flag: "--json"
      required: false
      value_type: boolean
      default: false
      description: "Emit machine-readable JSON instead of human-readable text."
    dry_run:
      flag: "--dry-run"
      required: false
      value_type: boolean
      default: true
      description: "Preview planned deterministic changes without writing."
    allow_write:
      flag: "--allow-write"
      required: false
      value_type: boolean
      default: false
      description: "Permit non-semantic deterministic writes inside kb_root."
    strict:
      flag: "--strict"
      required: false
      value_type: boolean
      default: false
      description: "Treat warnings as failure where validation supports it."
  subcommands:
    scaffold:
      role: "Create or preview the required KB folder skeleton and starter deterministic files."
      writes_possible: true
      semantic_behavior: false
    hash:
      role: "Calculate source file or directory hash for manifest identity and duplicate detection."
      writes_possible: false
      semantic_behavior: false
    preflight:
      role: "Validate KB root, schema, source path, manifest state, duplicate hash, and index freshness before ingest."
      writes_possible: false
      semantic_behavior: false
    manifest:
      role: "Validate or update deterministic source-manifest fields."
      writes_possible: true
      semantic_behavior: false
    index:
      role: "Generate or validate the machine-generated section of wiki/index.md."
      writes_possible: true
      semantic_behavior: false
    lint:
      role: "Run deterministic KB health checks."
      writes_possible: false
      semantic_behavior: false
    audit:
      role: "List, group, and validate audit files."
      writes_possible: false
      semantic_behavior: false
```


#

# Subcommand Contracts
```yaml
subcommand_contracts:
  scaffold:
    required_arguments:
      - "--kb-root"
    optional_arguments:
      - "--json"
      - "--dry-run"
      - "--allow-write"
      - "--title"
      - "--topic-title"
      - "--force"
    required_checks:
      - parent_directory_exists_or_can_be_created
      - target_kb_root_does_not_conflict_with_file
      - no_forbidden_root_files_required
    creates_when_allow_write_true:
      - "README.md"
      - "kb-schema.md"
      - "raw/articles/"
      - "raw/papers/"
      - "raw/notes/"
      - "raw/refs/"
      - "ingest-analysis/"
      - "wiki/index.md"
      - "wiki/concepts/"
      - "wiki/entities/"
      - "wiki/summaries/"
      - "manifests/source-manifest.json"
      - "audit/resolved/"
      - "outputs/queries/"
      - "log/"
    must_not_create:
      - "CLAUDE.md"
      - "SKILL.md"
      - ".llm-wiki/"
      - "graph.html"
      - "graph.json"
      - "Obsidian plugin files"
    output_artifact: scaffold_report
  hash:
    required_arguments:
      - "--path"
    optional_arguments:
      - "--json"
    default_algorithm: "sha256"
    directory_hash_rule: >
      For a directory, hash each contained file deterministically, sort by
      relative path, then hash the ordered path/hash manifest.
    output_artifact: hash_report
    writes_possible: false
  preflight:
    required_arguments:
      - "--kb-root"
      - "--source"
      - "--source-slug"
    optional_arguments:
      - "--json"
      - "--strict"
    required_checks:
      - kb_root_exists
      - kb_schema_exists
      - source_exists_or_pointer_mode_declared
      - source_hash_calculated_or_no_hash_reason_recorded
      - source_manifest_exists_or_can_be_initialized
      - source_hash_duplicate_checked
      - ingest_analysis_existing_checked
      - wiki_index_exists
      - index_freshness_checked
    output_artifact: ingest_preflight_report
    writes_possible: false
  manifest:
    required_arguments:
      - "--kb-root"
    optional_arguments:
      - "--source"
      - "--source-slug"
      - "--source-hash"
      - "--analysis-path"
      - "--generated-page"
      - "--json"
      - "--dry-run"
      - "--allow-write"
      - "--validate-only"
    deterministic_fields:
      - source_id
      - source_path
      - source_hash
      - hash_algorithm
      - first_seen_at
      - last_seen_at
      - ingest_analysis_path
      - generated_pages
      - review_flags
      - no_hash_reason
    llm_owned_fields:
      - source_summary
      - source_authority_note
      - semantic_tags
      - concept_candidates
      - entity_candidates
      - contradiction_summary
    rule: "The script may validate llm_owned_fields shape but must not synthesize their values."
    output_artifact: manifest_report
  index:
    required_arguments:
      - "--kb-root"
    optional_arguments:
      - "--json"
      - "--dry-run"
      - "--allow-write"
      - "--validate-only"
    machine_section_marker: "<!-- BEGIN AUTO-GENERATED INDEX -->"
    llm_section_marker: "<!-- BEGIN LLM SUMMARY -->"
    owns:
      - page_file_list
      - page_type_grouping
      - frontmatter_extraction
      - wikilink_target_inventory
      - source_pointer_inventory
      - stale_index_hash
      - machine_generated_index_section
    must_not_generate:
      - category_summaries
      - concept_descriptions
      - knowledge_gap_callouts
      - contradiction_summary
      - LLM_written_index_summary_section
    output_artifact: index_report
  lint:
    required_arguments:
      - "--kb-root"
    optional_arguments:
      - "--json"
      - "--strict"
      - "--check"
    allowed_check_values:
      - all
      - structure
      - frontmatter
      - links
      - orphans
      - source-pointers
      - manifest
      - index
      - audit
    deterministic_checks:
      - required_paths_exist
      - kb_schema_shape_valid
      - wiki_index_exists
      - wiki_page_frontmatter_valid
      - dead_wikilinks_detected
      - orphan_pages_detected
      - source_pointer_presence_checked
      - manifest_shape_valid
      - manifest_page_consistency_checked
      - stale_index_detected
      - audit_shape_valid
    output_artifact: lint_report
    writes_possible: false
  audit:
    required_arguments:
      - "--kb-root"
    optional_arguments:
      - "--json"
      - "--status"
      - "--severity"
      - "--target-path"
      - "--group-by"
    allowed_status_values:
      - open
      - resolved
      - deferred
      - rejected
      - all
    allowed_group_by_values:
      - target_path
      - type
      - severity
      - status
    deterministic_checks:
      - audit_directory_exists
      - audit_item_shape_valid
      - audit_target_path_exists_or_reported_missing
      - resolved_items_listed
      - open_items_grouped
    output_artifact: audit_report
    writes_possible: false
```


#

# Output Contracts
```yaml
output_contracts:
  common_report_fields:
    artifact_name: string
    kb_root: string
    command: string
    status: "passed | passed_with_flags | failed"
    dry_run: boolean
    writes_performed: boolean
    review_flags: list
    errors: list
    warnings: list
  scaffold_report:
    required_fields:
      - artifact_name
      - kb_root
      - status
      - dry_run
      - writes_performed
      - created_paths
      - existing_paths
      - skipped_paths
      - review_flags
      - errors
  hash_report:
    required_fields:
      - artifact_name
      - path
      - path_type
      - hash_algorithm
      - hash_value
      - file_count
      - bytes_total
      - errors
  ingest_preflight_report:
    required_fields:
      - artifact_name
      - kb_root
      - source_path
      - source_exists
      - source_hash
      - no_hash_reason
      - source_status
      - duplicate_source_candidates
      - existing_manifest_entry
      - existing_phase_1_analysis
      - index_status
      - required_paths_status
      - review_flags
      - errors
  manifest_report:
    required_fields:
      - artifact_name
      - kb_root
      - manifest_path
      - status
      - source_entries_count
      - changed_entries
      - missing_required_fields
      - invalid_entries
      - writes_performed
      - review_flags
      - errors
  index_report:
    required_fields:
      - artifact_name
      - kb_root
      - index_path
      - status
      - page_count
      - page_types
      - machine_section_status
      - llm_section_status
      - stale_index
      - broken_links_count
      - orphan_pages_count
      - writes_performed
      - review_flags
      - errors
  lint_report:
    required_fields:
      - artifact_name
      - kb_root
      - status
      - checks_run
      - missing_required_paths
      - malformed_frontmatter
      - broken_links
      - orphan_pages
      - missing_source_pointers
      - stale_index
      - manifest_issues
      - audit_shape_issues
      - review_flags
      - errors
  audit_report:
    required_fields:
      - artifact_name
      - kb_root
      - status
      - open_count
      - resolved_count
      - deferred_count
      - rejected_count
      - grouped_items
      - malformed_items
      - missing_targets
      - review_flags
      - errors
```


#

# Exit Code Policy
```yaml
exit_code_policy:  0:
    meaning: "Command completed with status passed."  1:
    meaning: "Command completed with status passed_with_flags."  2:
    meaning: "Command failed due to validation errors, missing inputs, or malformed KB files."  3:
    meaning: "Command refused because requested write is unsafe or outside policy."  4:
    meaning: "Command invocation error, such as unknown subcommand or invalid argument."
  rule: >
    When --json is supplied, the script must still emit a valid JSON object for
    exit codes 0, 1, 2, and 3 whenever possible.
```


#

# Safety and Boundary Rules
```yaml
safety_and_boundary_rules:
  no_semantic_generation:
    rule: "The script must never generate concept summaries, entity descriptions, contradiction interpretations, or query answers."
    reason: "Semantic synthesis is owned by the LLM and must remain source-visible."
  no_hidden_state:
    rule: "The script must store deterministic state only in visible files under the KB root."
    forbidden:
      - hidden_metadata_directories
      - local_database_files
      - cache_files_outside_kb_root
      - opaque_binary_state
  no_external_access:
    rule: "The script must not access the network, external services, package registries, or public URLs."
    allowed:
      - local_filesystem_reads
      - local_filesystem_writes_inside_kb_root_when_allowed
  no_destructive_actions:
    forbidden:
      - delete_raw_sources
      - overwrite_wiki_pages_without_allow_write
      - remove_source_pointers
      - delete_audit_history
      - delete_manifest_entries_without_explicit_future_contract
      - rewrite_llm_summary_section
  path_containment:
    rule: "All write targets must resolve inside the supplied kb_root."
    failure_exit_code: 3
  dry_run_default:
    rule: "All commands that can write must default to dry-run unless --allow-write is explicitly supplied."
```


#

# LLM Integration Rules
```yaml
llm_integration_rules:
  when_to_run_preflight:
    - before_ingest_phase_1
    - before_ingest_phase_2_when_source_status_may_have_changed
    - before_manifest_update
    - before_operator_requests_health_check
  when_to_run_index:
    - after_ingest_phase_2
    - before_query_when_index_status_is_unknown
    - during_lint
    - when stale_index is reported
  when_to_run_lint:
    - after_ingest_phase_2
    - before declaring KB healthy
    - before handing KB context to another Apex package
    - when broken_links_or_orphans_are_suspected
  when_to_run_audit:
    - when operator asks for audit review
    - after full_lint reports audit_shape_issues
    - when contradictions or quality flags need grouping
  llm_must_not:
    - invent_script_output
    - ignore_failed_preflight
    - treat_passed_with_flags_as_clean_pass
    - proceed_to_phase_2_when_script_reports_source_missing
    - overwrite_python_generated_index_section_manually
  llm_may:
    - summarize script reports for the operator
    - use script reports to decide which pages to read
    - draft semantic wiki changes after preflight passes
    - propose fixes for lint findings
    - request operator approval for deterministic writes
```


#

# Completion Gate
```yaml
completion_gate:
  valid_contract_file:
    required:
      - script_path_defined
      - runtime_policy_defined
      - write_policy_defined
      - command_surface_defined
      - subcommand_contracts_defined
      - output_contracts_defined
      - exit_code_policy_defined
      - safety_and_boundary_rules_defined
      - llm_integration_rules_defined
  command_coverage_required:
    - scaffold
    - hash
    - preflight
    - manifest
    - index
    - lint
    - audit
  forbidden_content_absent:
    - script_implementation_code
    - bash_commands_as_runtime_requirement
    - external_dependency_installation
    - semantic_generation_by_script
    - network_access
    - repo_write_instruction
```

## JSON Output Compatibility Notes

```yaml
json_output_compatibility_notes:
  known_actual_fields:
    common:
      - artifact_name
      - status
      - kb_root
      - findings
    scaffold:
      - dry_run
      - writes_performed
      - created_paths
      - skipped_paths
    hash:
      - path
      - path_type
      - hash_algorithm
      - hash_value
      - file_count
      - bytes_total
    preflight:
      - source_path
      - source_slug
      - source_hash
      - existing_manifest_entry
      - existing_phase_1_analysis
      - index_status
    index:
      - index_path
      - dry_run
      - writes_performed
      - machine_index_section_present
      - llm_summary_section_preserved
      - semantic_content_generated_by_python
      - page_count
      - orphan_pages_count
    lint:
      - checks_run
      - missing_required_paths
      - malformed_frontmatter
      - broken_links
      - orphan_pages
      - missing_source_pointers
      - stale_index
      - manifest_issues
      - audit_shape_issues
    audit:
      - open_count
      - resolved_count
      - deferred_count
      - rejected_count
      - grouped_items
      - malformed_items
      - missing_targets

  compatibility_rule: >
    If this contract and actual apex_kb.py output diverge, update this contract
    or the script in a dedicated reconciliation patch before relying on tests as
    proof of package correctness.
```
