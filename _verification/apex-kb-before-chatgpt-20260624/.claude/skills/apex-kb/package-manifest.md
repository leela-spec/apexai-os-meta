# Apex KB Package Manifest
```yaml
package_manifest:
  package_name: apex-kb
  package_path: ".claude/skills/apex-kb/"
  primary_artifact: apex_kb_artifact
  package_role: durable_knowledge_base_compiler
  read_when: "operator_inspects_package_structure_or_validates_apex_kb_files"
  source_trace:
    governing_map: "APEX KB ÔÇö LLM-Wiki Blueprint Capability Map.md"
    validated_decisions: "APEX KB ÔÇö Validated Decision Addendum"
    copied_blueprint_core:
      - persistent_compiled_wiki
      - raw_source_to_wiki_page_architecture
      - two_phase_ingest
      - index_first_query
      - source_hashing
      - source_manifest
      - contradiction_detection
      - review_queue_processing
      - concept_entity_summary_page_separation
    adapted_blueprint_core:
      - bash_helpers_to_python
      - llm_wiki_paths_to_apex_meta_kb_paths
      - CLAUDE_md_schema_to_kb_schema_md
      - hidden_llm_wiki_metadata_to_visible_manifests_folder
    omitted_v1:
      - graph_html_generation
      - D3_visualization
      - Obsidian_plugin_UI
      - web_viewer_feedback_UI
      - setup_project_hooks
      - bilingual_specific_behavior
  package_scope:
    owns:
      - scaffold_mode
      - ingest_phase_1
      - ingest_phase_2
      - query_mode
      - lint_mode
      - audit_mode
      - deterministic_kb_python_interface_contract
      - phase_1_ingest_analysis_template
      - phase_2_wiki_page_templates
    does_not_own:
      - project_planning
      - task_status_mutation
      - exact_next_task_ranking
      - Apex_task_registry_rebuild
      - blocker_scan
      - dependency_graph_traversal
      - session_handoff_files_outside_kb_root
      - external_contact
      - public_web_research_without_operator_request
  data_root:
    path_template: "apex-meta/kb/<kb-slug>/"
    required_runtime_paths:
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
      - "audit/"
      - "audit/resolved/"
      - "outputs/queries/"
      - "log/"
  runtime_script:
    path: "apex-meta/scripts/apex_kb.py"
    status: "specified_by_contract_not_in_package_folder"
    governing_contract: ".claude/skills/apex-kb/references/script-command-contract.md"
    runtime_policy:
      language: python
      standard_library_only: true
      external_dependencies_allowed: false
      shell_out_allowed: false
      bash_allowed: false
      javascript_allowed: false
      typescript_allowed: false
```


#

# File Inventory
```yaml
file_inventory:
  required_entrypoint:
    - path: ".claude/skills/apex-kb/SKILL.md"
      role: "Skill entrypoint, routing, supported modes, boundaries, procedure, failure modes, and completion gates."
      read_when:
        - skill_invocation
        - operator_reviews_apex_kb_scope
        - checking_mode_routing
      validates:
        - "The package is an independent durable knowledge-base compiler."
        - "Phase 1 ingest halts before Phase 2 generation."
        - "Python/LLM ownership split is explicit."
        - "Apex plan/session/sync boundaries are preserved."
  references:
    - path: ".claude/skills/apex-kb/references/kb-contract.md"
      role: "Canonical data, source, page, index, and package-boundary contract."
      read_when:
        - validating_apex_kb_scope
        - scaffold_mode
        - checking_data_root_layout
        - checking_page_contract
        - checking_source_policy
        - routing_to_apex_plan_session_sync
      validates:
        - "KB data lives under apex-meta/kb/<kb-slug>/."
        - "KB root uses kb-schema.md, not CLAUDE.md."
        - "Raw sources are preserved or explicitly pointed to."
        - "Generated pages require source pointers."
        - "Index is the entry point for query."
    - path: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
      role: "Operational rules for ingest, query, lint, audit, review flags, and failure modes."
      read_when:
        - ingest_phase_1
        - ingest_phase_2
        - query_mode
        - lint_mode
        - audit_mode
        - contradiction_detected
        - source_authority_unclear
        - operator_review_needed
      validates:
        - "Ingest uses Phase 0 preflight, Phase 1 analysis, Phase 2 generation, and Phase 3 postflight."
        - "Queries are index-first and evidence-page grounded."
        - "Lint separates deterministic checks from semantic quality review."
        - "Audit items are file-based and operator-resolvable."
    - path: ".claude/skills/apex-kb/references/script-command-contract.md"
      role: "Deterministic Python command interface contract for future apex_kb.py."
      read_when:
        - preparing_scaffold_command
        - preparing_hash_command
        - preparing_preflight_command
        - preparing_manifest_command
        - preparing_index_command
        - preparing_lint_command
        - preparing_audit_command
        - validating_script_output
      validates:
        - "Python script owns deterministic structure and validation only."
        - "Script must not synthesize concepts, entities, contradictions, page prose, or query answers."
        - "Default script behavior is dry-run."
        - "Writes are bounded to the KB root."
  templates:
    - path: ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
      role: "Copy-paste Phase 1 semantic analysis template."
      read_when:
        - creating_phase_1_ingest_analysis
        - operator_requests_phase_1_template
        - phase_1_analysis_shape_is_unclear
      validates:
        - "Phase 1 writes only ingest-analysis/<source-slug>.analysis.md."
        - "Phase 1 captures source identity, summary, candidates, contradictions, proposed changes, open questions, and operator gate."
        - "Phase 2 remains blocked until operator approval."
    - path: ".claude/skills/apex-kb/templates/wiki-page-templates.md"
      role: "Copy-paste Phase 2 wiki page templates."
      read_when:
        - creating_summary_page
        - creating_concept_page
        - creating_entity_page
        - creating_index_page
        - saving_query_output
        - creating_audit_item
      validates:
        - "Summary, concept, entity, index, query output, and audit item pages have consistent frontmatter."
        - "Substantive claims require source pointers."
        - "Contradictions and gaps remain visible."
        - "Machine-generated index and LLM semantic index sections remain separate."
  external_script:
    - path: "apex-meta/scripts/apex_kb.py"
      role: "Future deterministic Python implementation for scaffold, hash, preflight, manifest, index, lint, and audit operations."
      status: "next_file_to_generate"
      read_when:
        - running_apex_kb_deterministic_operations
        - validating_python_implementation_against_contract
      validates:
        - "Script conforms to script-command-contract.md."
        - "Script uses Python standard library only."
        - "Script does not perform semantic synthesis."
```


#

# Load Strategy
```yaml
load_strategy:
  default_invocation:
    always_load:
      - ".claude/skills/apex-kb/SKILL.md"
    load_only_when_needed:
      - ".claude/skills/apex-kb/references/kb-contract.md"
      - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
      - ".claude/skills/apex-kb/references/script-command-contract.md"
      - ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
      - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
      - ".claude/skills/apex-kb/package-manifest.md"
  by_mode:
    scaffold:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/script-command-contract.md"
      optional:
        - "package-manifest.md"
    ingest_phase_1:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/ingest-query-lint-audit-rules.md"
        - "references/script-command-contract.md"
        - "templates/ingest-analysis-template.md"
    ingest_phase_2:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/ingest-query-lint-audit-rules.md"
        - "templates/ingest-analysis-template.md"
        - "templates/wiki-page-templates.md"
      required_condition:
        operator_phrase: "approve ingest"
    query:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/ingest-query-lint-audit-rules.md"
        - "templates/wiki-page-templates.md"
    lint:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/ingest-query-lint-audit-rules.md"
        - "references/script-command-contract.md"
    audit:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/ingest-query-lint-audit-rules.md"
        - "references/script-command-contract.md"
        - "templates/wiki-page-templates.md"
```


#

# Validation Roles
```yaml
validation_roles:
  machine_readability:
    checks:
      - YAML blocks use 2-space indentation.
      - File paths are explicit and stable.
      - read_when conditions prevent unnecessary loading.
      - Mode names are consistent across files.
      - Ownership split uses python and llm consistently.
  token_efficiency:
    checks:
      - Manifest indexes files only and does not duplicate full contracts.
      - Source ledger details are summarized, not reprinted in full.
      - Templates remain in templates, not in SKILL.md.
      - Script command details remain in script-command-contract.md.
  resilient_simplicity:
    checks:
      - Missing KB root routes to scaffold or stop.
      - Missing kb-schema.md stops non-scaffold modes.
      - Phase 2 cannot run without approve ingest.
      - Broken links, orphan pages, stale index, and malformed audit items are reported.
      - Semantic synthesis is never assigned to Python.
      - Deterministic checks are never assigned only to LLM memory.
```


#

# Package-Level Failure Modes
```yaml
package_failure_modes:
  missing_skill_entrypoint:
    severity: critical
    detection: ".claude/skills/apex-kb/SKILL.md not present"
    correction: "Create SKILL.md before installing or invoking package."
  missing_kb_contract:
    severity: critical
    detection: "references/kb-contract.md not present"
    correction: "Create kb-contract.md before scaffold, ingest, query, lint, or audit."
  missing_operation_rules:
    severity: high
    detection: "references/ingest-query-lint-audit-rules.md not present"
    correction: "Create operation rules before ingest/query/lint/audit use."
  missing_script_contract:
    severity: high
    detection: "references/script-command-contract.md not present"
    correction: "Create script command contract before writing or running apex_kb.py."
  missing_ingest_template:
    severity: medium
    detection: "templates/ingest-analysis-template.md not present"
    correction: "Create template before standardizing Phase 1 ingest output."
  missing_wiki_templates:
    severity: medium
    detection: "templates/wiki-page-templates.md not present"
    correction: "Create templates before standardized Phase 2 page generation."
  manifest_drift:
    severity: medium
    detection: "Manifest file inventory does not match actual package files."
    correction: "Update package-manifest.md after package file additions, deletions, or renames."
  source_mapping_leak:
    severity: medium
    detection: "Source map, mechanism ledger, or draft audit files are placed inside final package."
    correction: "Keep source-mapping artifacts outside final .claude/skills/apex-kb/ package."
```


#

# Installation Checklist
```yaml
installation_checklist:
  required_package_files:
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
    - ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    - ".claude/skills/apex-kb/package-manifest.md"
  required_external_files:
    - "apex-meta/scripts/apex_kb.py"
  forbidden_package_files:
    - ".claude/skills/apex-kb/source-map.md"
    - ".claude/skills/apex-kb/mechanism-ledger.md"
    - ".claude/skills/apex-kb/script-ledger.md"
    - ".claude/skills/apex-kb/development-options.md"
    - ".claude/skills/apex-kb/CLAUDE.md"
    - ".claude/skills/apex-kb/settings.json"
    - ".claude/skills/apex-kb/workflow-index.md"
    - ".claude/skills/apex-kb/ci/"
    - ".claude/skills/apex-kb/.github/"
    - ".claude/skills/apex-kb/node_modules/"
```


#

# Completion Gate
```yaml
completion_gate:
  valid_package_manifest:
    required:
      - package_name_is_apex_kb
      - package_path_is_correct
      - primary_artifact_declared
      - file_inventory_complete
      - read_when_conditions_present
      - runtime_script_path_declared
      - package_scope_boundaries_present
      - load_strategy_present
      - validation_roles_present
      - package_failure_modes_present
      - installation_checklist_present
  invalid_if:
    - manifest_duplicates_full_contract_content
    - manifest_declares_uncreated_files_as_existing_without_status
    - manifest_places_source_maps_inside_final_package
    - manifest_moves_runtime_script_into_skill_package
    - manifest_removes_phase_2_operator_gate
    - manifest_assigns_semantic_synthesis_to_python
    - manifest_omits_script_contract
```
