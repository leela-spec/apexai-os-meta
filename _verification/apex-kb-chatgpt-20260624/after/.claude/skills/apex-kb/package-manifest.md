# Apex KB Package Manifest

```yaml
package_manifest:
  package_name: apex-kb
  package_path: ".claude/skills/apex-kb/"
  primary_artifact: apex_kb_artifact
  package_role: durable_knowledge_base_compiler
  read_when: "operator_inspects_package_structure_or_validates_apex_kb_files"
  current_hardening:
    - source_intake_lock_mode
    - skill_generation_and_research_base_custody_profiles
    - actual_file_read_ledger_for_strict_profiles
    - manifest_registration_not_comprehension_rule
    - nested_source_promotion_rule
  source_trace:
    governing_map: "APEX KB — LLM-Wiki Blueprint Capability Map.md"
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
      - strict_source_custody_overlay_for_skill_generation_kbs
  package_scope:
    owns:
      - scaffold_mode
      - source_intake_lock
      - ingest_phase_1
      - ingest_phase_2
      - query_mode
      - lint_mode
      - audit_mode
      - deterministic_kb_python_interface_contract
      - phase_1_ingest_analysis_template
      - phase_2_wiki_page_templates
      - source_custody_and_read_verification_policy
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

# File Inventory

```yaml
file_inventory:
  required_entrypoint:
    - path: ".claude/skills/apex-kb/SKILL.md"
      role: "Skill entrypoint, routing, supported modes, custody profiles, boundaries, procedure, failure modes, and completion gates."
      validates:
        - "The package is an independent durable knowledge-base compiler."
        - "Phase 1 ingest halts before Phase 2 generation."
        - "Source-intake lock is available for strict/high-risk KBs."
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
    - path: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
      role: "Operational rules for ingest, source-intake lock, query, lint, audit, review flags, and failure modes."
      read_when:
        - source_intake_lock
        - ingest_phase_1
        - ingest_phase_2
        - query_mode
        - lint_mode
        - audit_mode
        - contradiction_detected
        - source_authority_unclear
        - operator_review_needed
    - path: ".claude/skills/apex-kb/references/source-custody-and-read-verification.md"
      role: "Hardening policy for copied/snapshotted evidence custody, pointer-only exceptions, actual file read ledgers, and pseudo-validation prevention."
      read_when:
        - strict_custody_profile_selected
        - operator_rejects_pointer_only
        - nested_source_corpus_detected
        - source_read_evidence_is_unclear
        - skill_generation_kb
        - research_base_kb
    - path: ".claude/skills/apex-kb/references/script-command-contract.md"
      role: "Deterministic Python command interface contract for apex_kb.py."
      read_when:
        - preparing_scaffold_command
        - preparing_hash_command
        - preparing_preflight_command
        - preparing_manifest_command
        - preparing_index_command
        - preparing_lint_command
        - preparing_audit_command
        - validating_script_output

  templates:
    - path: ".claude/skills/apex-kb/templates/source-intake-lock-template.md"
      role: "Template for the single pre-ingest source-universe, custody, inventory, and exception lock."
      read_when:
        - creating_source_intake_lock
        - strict_custody_profile_selected
        - nested_source_promotions_needed
    - path: ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
      role: "Copy-paste Phase 1 semantic analysis template with source access ledger."
      read_when:
        - creating_phase_1_ingest_analysis
        - operator_requests_phase_1_template
        - phase_1_analysis_shape_is_unclear
        - source_access_ledger_needed
    - path: ".claude/skills/apex-kb/templates/wiki-page-templates.md"
      role: "Copy-paste Phase 2 wiki page templates."
      read_when:
        - creating_summary_page
        - creating_concept_page
        - creating_entity_page
        - creating_index_page
        - saving_query_output
        - creating_audit_item

  external_script:
    - path: "apex-meta/scripts/apex_kb.py"
      role: "Deterministic Python implementation for scaffold, hash, preflight, manifest, index, lint, and audit operations."
      status: "external_to_skill_folder"
```

# Load Strategy

```yaml
load_strategy:
  default_invocation:
    always_load:
      - ".claude/skills/apex-kb/SKILL.md"
    load_only_when_needed:
      - ".claude/skills/apex-kb/references/kb-contract.md"
      - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
      - ".claude/skills/apex-kb/references/source-custody-and-read-verification.md"
      - ".claude/skills/apex-kb/references/script-command-contract.md"
      - ".claude/skills/apex-kb/templates/source-intake-lock-template.md"
      - ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
      - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
      - ".claude/skills/apex-kb/package-manifest.md"
  by_mode:
    scaffold:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/script-command-contract.md"
    source_intake_lock:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/source-custody-and-read-verification.md"
        - "templates/source-intake-lock-template.md"
    ingest_phase_1:
      required:
        - "SKILL.md"
        - "references/kb-contract.md"
        - "references/ingest-query-lint-audit-rules.md"
        - "templates/ingest-analysis-template.md"
      required_when_strict_profile:
        - "references/source-custody-and-read-verification.md"
        - "templates/source-intake-lock-template.md"
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

# Validation Roles

```yaml
validation_roles:
  machine_readability:
    checks:
      - yaml_blocks_are_parseable_enough_for_agents
      - file_inventory_matches_package_files
      - mode_load_strategy_is_explicit
  token_efficiency:
    rule: "Keep SKILL.md as the routing/control plane; keep detailed custody and templates in references/templates."
  resilient_simplicity:
    rule: "Use one source-intake lock by default, not multiple bureaucratic reports."
  source_truthfulness:
    rule: "No actual files read means no source comprehension claim."
```

# Package Failure Modes

```yaml
package_failure_modes:
  stale_inventory:
    response: "Update this manifest when adding/removing package files."
  source_policy_conflict:
    response: "Apply strict custody profiles from SKILL.md and source-custody reference for skill-generation/research-base KBs."
  overgrown_skill_entrypoint:
    response: "Move detailed rules to references or templates and keep SKILL.md compact."
  pseudo_validation:
    response: "Require source-intake lock and/or source access ledger before treating an ingest as ready."
```
