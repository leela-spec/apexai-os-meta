---
name: apex-kb
description: >
  Use this skill when the operator asks to scaffold, ingest, compile, query, lint, or
  audit a durable Apex knowledge base under apex-meta/kb/<kb-slug>/. Accepts a kb_slug,
  raw source paths, existing KB files, operator review decisions, and Apex context.
  Produces source-preserving KB artifacts, phase-1 ingest analysis, wiki pages, saved
  query outputs, deterministic health reports, or audit review flags. Does not plan
  projects, mutate task status, rank next tasks, rebuild Apex task registries, or write
  outside the KB root without explicit operator approval.
---

# Apex KB

## Skill Contract
```yaml
skill_contract:
  primary_output: apex_kb_artifact
  output_role: durable_knowledge_base_compiler
  package_path: ".claude/skills/apex-kb/"
  data_root: "apex-meta/kb/"
  one_kb_slug_per_invocation: true
  modes:
    - scaffold
    - ingest_phase_1
    - ingest_phase_2
    - query
    - lint
    - audit
  validated_decisions:
    kb_schema_file:
      filename: "kb-schema.md"
      reject:
        - "CLAUDE.md inside KB root"
      location_template: "apex-meta/kb/<kb-slug>/kb-schema.md"
      owns:
        - kb_topic_title
        - kb_source_authority_list
        - kb_concept_taxonomy_top_level
        - kb_language_policy
        - kb_operator_review_policy
    ingest_analysis_folder:
      required: true
      path_template: "apex-meta/kb/<kb-slug>/ingest-analysis/"
      role: "Phase 1 analysis outputs before operator approval and Phase 2 wiki generation."
    index_rebuild_ownership:
      deterministic_structure_owner: python
      semantic_enrichment_owner: llm
      machine_index_marker: "<!-- BEGIN AUTO-GENERATED INDEX -->"
      llm_summary_marker: "<!-- BEGIN LLM SUMMARY -->"
    script_runtime:
      v1_language: python
      external_dependencies_allowed: false
      shell_out_allowed: false
      bash_allowed: false
      javascript_allowed: false
      typescript_allowed: false
  data_layout:
    root: "apex-meta/kb/<kb-slug>/"
    required_paths:
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
  owns:
    - source_root_contract
    - raw_source_preservation
    - source_pointer_creation
    - source_hashing_request
    - source_manifest_update
    - ingest_phase_1_analysis
    - operator_review_gate
    - ingest_phase_2_wiki_generation
    - summary_page_generation
    - concept_page_generation
    - entity_page_generation
    - crosslink_generation
    - contradiction_capture
    - open_question_capture
    - wiki_index_update
    - wiki_grounded_query
    - deterministic_lint_report
    - audit_feedback_capture
    - audit_review_grouping
  hands_off_to:
    apex_plan:
      - knowledge_gap_as_planning_task_candidate
      - unresolved_scope_question
      - candidate_followup_task
    apex_session:
      - kb_ingest_summary
      - raw_source_path_preservation
      - source_conflict_or_audit_item
      - next_session_kb_context
    apex_sync:
      - deterministic_task_or_registry_validation_only
  boundaries:
    must_not_create:
      - project_decomposition
      - task_status_mutation
      - exact_next_task_ranking
      - dependency_graph_traversal
      - blocker_scan
      - apex_task_registry_rebuild
      - session_handoff_files_outside_kb
      - personal_material_fusion_without_operator_request
      - obsidian_folder_write_without_operator_approval
      - public_web_research_without_operator_request
      - external_author_contact
      - repository_write_without_operator_approval
  source_policy:
    raw_sources_are_immutable: true
    preserve_exact_source_filename: true
    preserve_exact_source_path: true
    never_treat_missing_source_as_verified: true
    source_pointer_required_on_generated_pages: true
    source_storage_modes:
      pointer_only:
        use_when: "Source already exists durably inside this repository and should not be duplicated."
        required_fields:
          - source_path
          - source_hash
          - source_storage_mode
      copy_into_kb:
        use_when: "Source is external, uploaded, temporary, or not durably stored in this repository."
        required_fields:
          - source_path
          - source_hash
          - copied_to
          - source_storage_mode
      snapshot_copy:
        use_when: "Source may change and the KB requires a frozen evidence version."
        required_fields:
          - source_path
          - source_hash
          - snapshot_path
          - source_storage_mode
    default_for_repo_internal_sources: pointer_only
    default_for_external_or_uploaded_sources: copy_into_kb

  phase_gate_policy:
    normal_mode:
      same_prompt_approval_allowed: false
      requires_separate_operator_turn: true
    explicit_test_mode:
      same_prompt_approval_allowed: true
      condition: "Phase 1 artifacts must exist before Phase 2 generation begins."
    required_phrase: "approve ingest"

  epistemic_labels:
    confidence:
      allowed:
        - high
        - medium
        - low
        - mixed
        - unknown
    claim_label:
      allowed:
        - raw_source
        - source_backed_summary
        - behavioral_inference
        - working_hypothesis
        - operator_question
        - practitioner_question
```


#

# Supporting Files

```yaml
supporting_files:
  - path: "references/kb-contract.md"
    read_when:
      - validating_apex_kb_scope
      - scaffold_mode
      - checking_data_layout
      - routing_to_apex_plan_session_sync
      - validating_forbidden_behavior

  - path: "references/ingest-query-lint-audit-rules.md"
    read_when:
      - ingest_phase_1
      - ingest_phase_2
      - query_mode
      - lint_mode
      - audit_mode
      - checking_operator_review_gate
      - validating_semantic_vs_deterministic_ownership
      - checking_source_storage_mode

  - path: "references/script-command-contract.md"
    read_when:
      - scaffold_mode
      - lint_mode
      - index_rebuild_needed
      - hash_source_needed
      - audit_file_listing_needed
      - operator_asks_about_apex_kb_py
      - reconciling_cli_arguments

  - path: "templates/ingest-analysis-template.md"
    read_when:
      - writing_ingest_phase_1_analysis
      - operator_requests_blank_phase_1_template
      - phase_1_output_shape_is_unclear

  - path: "templates/wiki-page-templates.md"
    read_when:
      - creating_summary_page
      - creating_concept_page
      - creating_entity_page
      - checking_generated_page_shape
      - checking_claim_label_vs_confidence

  - path: "package-manifest.md"
    read_when:
      - operator_inspects_package_structure
      - validating_file_inventory
      - checking_v1_scope
```

# Procedure

1. **Resolve mode and KB root.** Identify the requested mode, `kb_slug`, target KB root, and whether the operator is asking for scaffold, ingest, query, lint, or audit; stop if `kb_slug` or source path requirements are missing.
2. **Load the KB control files.** Read `kb-schema.md`, `wiki/index.md`, `manifests/source-manifest.json`, and relevant pages under `wiki/`; if the KB root does not exist, route to scaffold mode.
3. **Run deterministic preparation where relevant.** For scaffold, hash, index, lint, stale-index, dead-link, orphan, or audit-listing needs, use the Python script contract instead of re-implementing exact file scans through reasoning.
4. **Perform semantic work with the LLM only.** Use reasoning for source interpretation, concept extraction, entity synthesis, contradiction interpretation, open-question capture, page drafting, query synthesis, and operator-facing judgment.
5. **Execute ingest as a two-phase gate.** In `ingest_phase_1`, write or return one analysis under `ingest-analysis/<source-slug>.analysis.md` and halt. Only proceed to `ingest_phase_2` when the operator explicitly approves the ingest.
6. **Generate or update wiki pages.** In `ingest_phase_2`, create or update summary, concept, and entity pages with source pointers, crosslinks, contradiction callouts, and open questions; preserve raw source identity and update the source manifest.
7. **Answer queries index-first.** For `query`, read `wiki/index.md` first, select the smallest sufficient set of relevant pages, answer from compiled KB pages, mark confidence, cite source-page evidence, and save query output when requested.
8. **Validate and report.** For `lint` or after page generation, separate deterministic health findings from semantic review flags; do not silently repair uncertain contradictions, missing authority, or ambiguous source claims.

#

# Failure Modes

```yaml
failure_modes:
  missing_kb_slug:
    response: "Stop and request a kb_slug before touching files."

  missing_kb_root:
    response: "Route to scaffold mode and propose the required KB root paths."

  missing_kb_schema:
    response: "Create or request kb-schema.md; do not substitute CLAUDE.md."

  missing_raw_source:
    response: "Stop. Do not infer source content from filename, title, or prior summaries."

  duplicate_source_hash:
    response: "Report prior ingest record and ask whether to skip, compare, or re-ingest as a new version."

  phase_2_without_approval:
    response: "Stop after Phase 1. Require the exact operator approval phrase before generating wiki pages."

  same_prompt_phase_2_approval_in_normal_mode:
    response: "Treat as not approved. Require a separate operator turn unless explicit test mode is declared."

  stale_index_detected:
    response: "Run or request Python index rebuild for the machine section before relying on index completeness."

  broken_links_or_orphans:
    response: "Return deterministic lint findings and keep semantic page repair separate."

  contradiction_detected:
    response: "Preserve the contradiction as a review flag or callout; do not silently collapse conflicting claims."

  source_authority_unclear:
    response: "Mark authority as uncertain in the ingest analysis and request operator review."

  source_storage_mode_unclear:
    response: "Default repo-internal durable sources to pointer_only; default external or uploaded sources to copy_into_kb."

  write_outside_kb_root_requested:
    response: "Require explicit operator approval and identify the exact target path before writing."

  external_contact_requested_or_implied:
    response: "Do not contact external authors, maintainers, contributors, recipients, or third parties."
```

# Completion Gate

```yaml
completion_gate:
  valid_completion_requires:
    - requested_mode_identified
    - kb_slug_resolved
    - kb_root_policy_followed
    - source_storage_mode_resolved
    - raw_source_policy_followed_when_ingesting
    - deterministic_vs_semantic_ownership_respected
    - operator_gate_respected_for_ingest_phase_2
    - output_artifact_matches_requested_mode
    - confidence_and_claim_label_not_conflated
    - review_flags_returned_when_uncertainty_exists

  valid_outputs_by_mode:
    scaffold:
      - kb_root_scaffold_plan_or_created_paths
      - kb-schema.md
      - initial_wiki_index
      - initial_source_manifest

    ingest_phase_1:
      - ingest_analysis
      - operator_review_required

    ingest_phase_2:
      - generated_or_updated_wiki_pages
      - updated_manifest
      - updated_index_sections
      - postflight_review_flags

    query:
      - wiki_grounded_answer
      - evidence_pages
      - confidence
      - claim_label
      - knowledge_gaps
      - optional_saved_query_output

    lint:
      - deterministic_health_report
      - semantic_review_flags

    audit:
      - grouped_audit_items
      - proposed_accept_partial_reject_defer_actions
```
