---
name: apex-kb
description: >
  Use this skill when the operator asks to scaffold, ingest, query, lint, or audit
  a durable Apex project knowledge base under apex-meta/kb/<kb-slug>/. Accepts a
  kb_slug, raw source paths, existing KB files, and operator review decisions.
  Produces source-preserving KB artifacts, phase-1 ingest analysis, wiki pages,
  saved query outputs, or review flags. Does not plan projects, mutate task
  status, rank next tasks, rebuild Apex task registries, or write outside the KB
  root without explicit operator approval.
---

# Apex KB

## Skill Contract

```yaml
skill_contract:
  primary_output: apex_kb_artifact
  output_role: durable_project_knowledgebase_compiler
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

  required_operator_gate:
    phase_1_halts_before_phase_2: true
    phase_2_confirmation_phrase: "approve ingest"

  owns:
    - source_root_contract
    - raw_source_preservation
    - source_manifest_update
    - ingest_phase_1_analysis
    - operator_review_gate
    - summary_page_generation
    - concept_page_generation
    - entity_page_generation
    - wiki_index_update
    - wiki_grounded_query
    - lightweight_lint_report
    - audit_feedback_capture

  hands_off_to:
    apex_plan:
      - knowledge_gap_as_planning_task_candidate
      - unresolved_scope_question
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
```

## Supporting Files

```yaml
supporting_files:
  - path: references/kb-contract.md
    read_when:
      - validating_apex_kb_scope
      - scaffold_mode
      - ingest_phase_1
      - ingest_phase_2
      - query_mode
      - lint_mode
      - audit_mode
      - routing_to_apex_plan_session_sync

  - path: references/development-options.md
    read_when:
      - operator_asks_about_future_expansion
      - deciding_whether_to_add_scripts
      - deciding_whether_to_add_obsidian_or_external_feedback
      - planning_v2_or_later_apex_kb_work

  - path: templates/ingest-analysis-template.md
    read_when:
      - writing_ingest_phase_1_analysis
      - validating_phase_1_review_gate

  - path: templates/wiki-page-templates.md
    read_when:
      - writing_summary_page
      - writing_concept_page
      - writing_entity_page
      - writing_query_output

  - path: package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_file_inventory
```

## Procedure

1. **Classify mode.** Map the operator request to one mode: `scaffold`, `ingest_phase_1`, `ingest_phase_2`, `query`, `lint`, or `audit`; if the request belongs to planning, session mutation, or deterministic task sync, route to the owning Apex package.

2. **Load KB contract.** Read `references/kb-contract.md` and apply the data-root, raw-source, phase-gate, page, index, query, and handoff rules relevant to the selected mode.

3. **Scaffold KB root.** For `scaffold`, create or describe the minimal `apex-meta/kb/<kb-slug>/` data folders and initial empty index/manifest/log files; do not place `SKILL.md` or `CLAUDE.md` inside the KB data root.

4. **Analyze one source.** For `ingest_phase_1`, preserve the raw source path exactly, update or draft the source-manifest entry, write one reviewable ingest analysis from `templates/ingest-analysis-template.md`, then stop.

5. **Compile approved pages.** For `ingest_phase_2`, continue only after the operator uses `approve ingest`; generate the approved summary, concept, and entity pages from `templates/wiki-page-templates.md`, update `wiki/index.md`, and record a log entry.

6. **Query compiled knowledge.** For `query`, read `wiki/index.md` first, then relevant summary/concept/entity pages; answer only from compiled KB material and save durable answers to `outputs/queries/` when useful.

7. **Check or capture feedback.** For `lint` or `audit`, produce a lightweight report of missing index entries, orphan-like pages, unresolved source conflicts, malformed page metadata, or operator feedback; propose fixes but do not rewrite outside the KB root.

## Failure Modes

```yaml
failure_modes:
  missing_kb_slug:
    trigger: "No kb_slug is supplied."
    correction: "Ask for a kb_slug before creating or reading KB data paths."

  missing_raw_source:
    trigger: "Ingest is requested but no raw source path or source text is supplied."
    correction: "Stop and request one source path or one source document."

  phase_2_without_approval:
    trigger: "Page generation is requested before an approved phase-1 analysis exists."
    correction: "Return the phase-1 review gate and request the phrase approve ingest."

  source_path_uncertain:
    trigger: "The source path is inferred but not verified by the operator or repo."
    correction: "Mark source_status as unverified and do not claim the source exists."

  conflicting_sources:
    trigger: "Two sources make incompatible claims."
    correction: "Preserve both claims, add a source_conflict flag, and hand off to apex-session if needed."

  out_of_scope_request:
    trigger: "The request asks for planning, task mutation, ranking, blocker scan, or registry rebuild."
    correction: "Route to apex-plan, apex-session, or apex-sync instead of expanding apex-kb scope."
```

## Output Requirements

```yaml
output_requirements:
  allowed_outputs:
    - kb_root_scaffold
    - source_manifest_entry
    - ingest_phase_1_analysis
    - wiki_summary_page
    - wiki_concept_page
    - wiki_entity_page
    - wiki_index_update
    - query_output
    - lint_report
    - audit_report
    - apex_package_handoff

  required_properties:
    - preserve_raw_source_path
    - cite_source_id_on_generated_pages
    - keep_phase_1_and_phase_2_separate
    - read_index_before_query_answer
    - keep_data_under_apex_meta_kb_slug
```

## Completion Gate

```yaml
completion_gate:
  mode_classified: true
  kb_slug_resolved: true
  relevant_supporting_file_read: true
  raw_source_preserved_when_ingesting: true
  phase_gate_respected: true
  output_written_or_returned_in_declared_format: true
  forbidden_cross_package_behavior_avoided: true
```
