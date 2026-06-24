# Apex KB Contract
```yaml
kb_contract:
  artifact_name: apex_kb_artifact
  file_role: durable_knowledge_base_contract
  package_path: ".claude/skills/apex-kb/"
  data_root: "apex-meta/kb/"
  one_kb_slug_per_invocation: true
  source_trace:
    governing_map: "APEX KB — LLM-Wiki Blueprint Capability Map.md"
    blueprint_files:
      operational_entrypoint: "B01: llm-wiki-main/llm-wiki/SKILL.md"
      ingest_workflow: "B02: llm-wiki-main/llm-wiki/workflows/ingest.md"
      query_workflow: "B03: llm-wiki-main/llm-wiki/workflows/query.md"
      lint_workflow: "B04: llm-wiki-main/llm-wiki/workflows/lint.md"
      review_workflow: "B06: llm-wiki-main/llm-wiki/workflows/review.md"
      wiki_schema: "B07: llm-wiki-main/llm-wiki/WIKI_SCHEMA.md"
      scaffold_python: "C04: llm-wiki-skill-main/scripts/scaffold.py"
      lint_python: "C05: llm-wiki-skill-main/scripts/lint_wiki.py"
      audit_python: "C06: llm-wiki-skill-main/scripts/audit_review.py"
    copied_core_mechanisms:
      - persistent_compiled_wiki
      - raw_source_to_wiki_page_architecture
      - two_phase_ingest
      - index_first_query
      - source_hashing
      - source_manifest_update
      - contradiction_detection
      - review_queue_processing
      - file_based_audit_surface
      - concept_entity_summary_separation
    adapted_mechanisms:
      - bash_helpers_to_python
      - llm_wiki_paths_to_apex_meta_kb_paths
      - CLAUDE_md_schema_to_kb_schema_md
      - hidden_llm_wiki_manifest_to_visible_manifests_folder
    omitted_v1_mechanisms:
      - graph_html_generation
      - D3_visualization
      - Obsidian_plugin_UI
      - web_viewer_feedback_UI
      - setup_project_hooks
      - bilingual_specific_behavior
    not_found_or_unverified:
      - wiki_search.py
      - update-index.py
      - init_wiki.py
  primary_purpose: >
    Maintain a durable, source-preserving, compiled knowledge base that lets
    Claude and other AI agents answer from reusable wiki context instead of
    repeatedly rereading raw sources.
  non_purpose: >
    Apex KB is not a planner, task mutator, ranking engine, blocker scanner,
    status merger, or session handoff engine. Other Apex packages may consume
    KB outputs, but they do not define KB behavior.
```


#

# Data Root Contract

```
data_root_contract:  root_template: "apex-meta/kb/<kb-slug>/"  required_root_files:    - path: "README.md"      role: "Human orientation for this KB instance."    - path: "kb-schema.md"      role: "KB-local schema and operating policy. Replaces blueprint CLAUDE.md inside KB roots."  required_directories:    raw:      path: "raw/"      role: "Immutable or pointer-preserved source intake."      children:        - "articles/"        - "papers/"        - "notes/"        - "refs/"    ingest_analysis:      path: "ingest-analysis/"      role: "Phase 1 ingest analysis outputs before operator approval."    wiki:      path: "wiki/"      role: "Compiled AI-consumable knowledge pages."      children:        - "index.md"        - "concepts/"        - "entities/"        - "summaries/"    manifests:      path: "manifests/"      role: "Source manifest, hash records, and deterministic state metadata."      required_files:        - "source-manifest.json"    audit:      path: "audit/"      role: "Open human feedback, correction, contradiction, and quality items."      children:        - "resolved/"    outputs:      path: "outputs/"      role: "Saved query outputs and reusable synthesis artifacts."      children:        - "queries/"    log:      path: "log/"      role: "Operation history and durable maintenance notes."  forbidden_root_files:    - path: "CLAUDE.md"      reason: "Reserved Claude Code root-context convention; KB-local schema must be kb-schema.md."    - path: "SKILL.md"      reason: "Skill entrypoint belongs in .claude/skills/apex-kb/, not in a KB data root."
```


#

# KB Schema Contract

```
kb_schema_contract:  file: "apex-meta/kb/<kb-slug>/kb-schema.md"  role: "KB-local schema, authority, language, taxonomy, and operator-review policy."  required_fields:    kb_topic_title:      type: string      required: true      purpose: "Human-readable topic or domain represented by this KB."    kb_source_authority_list:      type: list      required: true      purpose: "Ordered source-authority rules for resolving conflicts."    kb_concept_taxonomy_top_level:      type: list      required: true      purpose: "Top-level concept buckets used to organize concept pages."    kb_language_policy:      type: string_or_map      required: true      purpose: "Defines output language, source-language handling, and translation behavior."    kb_operator_review_policy:      type: map      required: true      purpose: "Defines when Phase 1, contradictions, source conflicts, and audit items require operator review."  must_not_contain:    - repo_global_claude_instructions    - model_identity_rules    - project_wide_agent_behavior    - unrelated_apex_package_rules
```


#

# Source Policy

```
source_policy:  raw_sources_are_immutable: true  preserve_exact_source_filename: true  preserve_exact_source_path: true  source_pointer_required_on_generated_pages: true  source_manifest_required: true  source_hash_required_when_possible: true  accepted_source_forms:    local_markdown_or_text:      action: "Copy or preserve under raw/ with exact filename."    local_large_or_binary_file:      action: "Create pointer reference under raw/refs/ with path, metadata, and operator-provided context."    url_or_external_reference:      action: "Store as source pointer only unless operator supplies local content."    prior_kb_page:      action: "Treat as compiled context, not raw source."  forbidden_source_behavior:    - infer_content_from_filename_only    - treat_missing_source_as_verified    - overwrite_raw_source_without_operator_instruction    - erase_old_source_identity_on_reingest    - silently_collapse_conflicting_sources
```


#

# Wiki Page Contract

```
wiki_page_contract:  page_families:    summaries:      path: "wiki/summaries/"      role: "Source-level or synthesis-level summaries grounded in preserved sources."    concepts:      path: "wiki/concepts/"      role: "Reusable concept, framework, method, tool, or idea pages."    entities:      path: "wiki/entities/"      role: "People, organizations, projects, products, repositories, or named systems."    index:      path: "wiki/index.md"      role: "Primary navigation and query-entry surface."  required_generated_page_properties:    - stable_slug    - clear_title    - page_type    - source_pointers    - outbound_wikilinks    - contradiction_or_uncertainty_section_when_needed    - open_questions_when_needed    - last_review_or_update_note  page_generation_rules:    preserve_source_pointers: true    use_wikilinks_for_internal_links: true    expose_contradictions: true    expose_open_questions: true    prefer_update_over_duplicate_page: true    do_not_synthesize_without_source_basis: true
```


#

# Index Contract

```
index_contract:  file: "apex-meta/kb/<kb-slug>/wiki/index.md"  role: "Index-first query surface and compiled KB navigation layer."  ownership_split:    deterministic_structure:      owner: python      section_marker: "<!-- BEGIN AUTO-GENERATED INDEX -->"      may_update:        - page_file_list        - frontmatter_extraction        - page_type_grouping        - link_validation_status        - orphan_status        - stale_index_status    semantic_enrichment:      owner: llm      section_marker: "<!-- BEGIN LLM SUMMARY -->"      may_update:        - category_summaries        - concept_descriptions        - knowledge_gap_callouts        - contradiction_summary        - query_guidance_notes  rules:    query_reads_index_first: true    generated_file_list_is_deterministic: true    semantic_summary_must_not_claim_unread_sources: true    stale_index_must_be_reported_before_query_confidence: true
```


#

# Operation Boundary Contract

```
operation_boundary_contract:  scaffold:    owns:      - create_kb_root_structure      - create_initial_kb_schema      - create_initial_index      - create_initial_manifest      - create_initial_audit_and_log_paths    must_not:      - ingest_sources_without_request      - create_repo_global_CLAUDE_md      - install_hooks_or_settings  ingest:    owns:      - phase_1_source_analysis      - operator_review_gate      - phase_2_page_generation_after_approval      - source_manifest_update      - source_hash_record      - contradiction_capture      - crosslink_generation    must_not:      - skip_phase_1_when_review_required      - generate_wiki_pages_before_operator_approval      - silently_resolve_contradictions  query:    owns:      - index_first_retrieval      - selected_page_reading      - wiki_grounded_answer      - evidence_and_confidence_reporting      - knowledge_gap_reporting      - optional_saved_query_output    must_not:      - answer_from_raw_memory_when_relevant_pages_exist      - read_entire_kb_when_3_to_5_pages_are_sufficient      - hide_stale_index_status  lint:    owns:      - deterministic_health_report      - frontmatter_validation      - dead_link_detection      - orphan_detection      - stale_index_detection      - semantic_review_flags_when_full_lint_requested    must_not:      - silently_rewrite_pages      - treat_semantic_judgment_as_python_output  audit:    owns:      - audit_file_listing      - audit_grouping      - target_anchor_review      - accept_partial_reject_defer_options      - resolved_audit_archival    must_not:      - resolve_human_feedback_without_operator_decision      - delete_resolved_feedback_history
```


#

# Apex Package Boundary

```
apex_package_boundary:  apex_kb_owns:    - durable_knowledge_base_compilation    - raw_source_preservation    - semantic_extraction    - source_summary_generation    - concept_page_generation    - entity_page_generation    - contradiction_detection    - open_question_capture    - index_first_query    - knowledge_gap_detection    - audit_feedback_surface    - lint_health_surface  apex_plan_consumes:    - knowledge_gap_as_planning_task_candidate    - unresolved_scope_question    - candidate_followup_task  apex_session_consumes:    - kb_ingest_summary    - raw_source_path_preservation    - source_conflict_or_audit_item    - next_session_kb_context  apex_sync_consumes:    - deterministic_task_or_registry_validation_only  apex_kb_must_not_perform:    - project_decomposition    - task_status_mutation    - exact_next_task_ranking    - dependency_graph_traversal    - blocker_scan    - apex_task_registry_rebuild    - session_handoff_files_outside_kb    - calendar_or_schedule_writes    - public_web_research_without_operator_request    - external_contact
```


#

# Acceptance Contract

```
acceptance_contract:  valid_kb_instance_requires:    - kb_root_exists    - kb_schema_md_exists    - raw_tree_exists    - ingest_analysis_folder_exists    - wiki_index_exists    - wiki_concepts_entities_summaries_exist    - source_manifest_exists    - audit_and_resolved_folders_exist    - outputs_queries_folder_exists    - log_folder_exists  valid_ingest_requires:    - raw_source_or_source_pointer_preserved    - source_hash_or_no_hash_reason_recorded    - phase_1_analysis_created    - operator_gate_respected    - generated_pages_have_source_pointers    - contradictions_or_uncertainties_flagged    - index_updated_or_stale_index_flagged    - manifest_updated_or_update_failure_reported  valid_query_requires:    - index_read_first    - relevant_pages_selected    - answer_grounded_in_compiled_pages    - evidence_pages_named    - contradictions_and_gaps_reported    - confidence_stated  valid_lint_requires:    - deterministic_findings_separated_from_semantic_flags    - broken_links_reported    - orphan_pages_reported    - stale_index_status_reported    - malformed_frontmatter_reported  valid_audit_requires:    - open_items_grouped    - target_pages_identified    - operator_decision_required_for_resolution    - resolved_items_archived_not_deleted
```
