# Apex KB Contract

```yaml
kb_contract:
  package_name: apex-kb
  package_path: ".claude/skills/apex-kb/"
  data_root: "apex-meta/kb/"
  purpose: >
    Define the minimum durable knowledge-base process for Apex project knowledge.
    This contract adapts the LLM-Wiki raw-source-to-compiled-wiki pattern while
    preserving Apex package boundaries.

  v1_scope:
    included:
      - scaffold_kb_root
      - preserve_raw_sources
      - write_source_manifest_entries
      - write_phase_1_ingest_analysis
      - halt_for_operator_review
      - generate_approved_summary_concept_entity_pages
      - update_wiki_index
      - answer_queries_from_compiled_pages
      - produce_lightweight_lint_or_audit_reports
    excluded:
      - slash_commands
      - obsidian_plugin
      - web_viewer
      - graph_visualization
      - automatic_hashing_script
      - automatic_lint_script
      - full_text_search_engine
      - task_registry_rebuild
      - task_status_mutation
      - project_planning
```

## Data layout

```text
apex-meta/kb/<kb-slug>/
  README.md
  raw/
    articles/
    papers/
    notes/
    refs/
  ingest-analysis/
  wiki/
    index.md
    concepts/
    entities/
    summaries/
  manifests/
    source-manifest.md
  audit/
    resolved/
  outputs/
    queries/
  log/
```

```yaml
data_layout_rules:
  kb_slug:
    type: lowercase_kebab_case
    required: true
  raw:
    owner: operator_or_source
    rule: "Never rewrite raw source content."
  ingest_analysis:
    owner: apex-kb
    rule: "Phase-1 review artifacts live here and must be reviewed before page generation."
  wiki:
    owner: apex-kb
    rule: "Generated summaries, concepts, entities, and index live here."
  manifests:
    owner: apex-kb
    rule: "Track source IDs, raw paths, ingest status, and generated pages."
  audit:
    owner: operator_and_apex-kb
    rule: "Capture feedback or source conflicts; resolved feedback moves to audit/resolved/."
  outputs_queries:
    owner: apex-kb
    rule: "Store durable answers produced from compiled KB pages."
  log:
    owner: apex-kb
    rule: "Append concise operation records."
```

## Source manifest

```yaml
source_manifest_entry:
  source_id: "src_001"
  title: ""
  raw_source_path: "apex-meta/kb/<kb-slug>/raw/<type>/<filename>"
  source_type: "article | paper | note | ref"
  source_status: "placed | path_only | analyzed | compiled | needs_review | conflict"
  ingest_analysis_path: ""
  summary_page: ""
  concept_pages: []
  entity_pages: []
  review_flags: []
```

## Ingest phases

```yaml
ingest_phase_1:
  purpose: "Analyze exactly one source before generated wiki pages are written."
  input_required:
    - kb_slug
    - source_id_or_new_source
    - raw_source_path_or_source_text
  output_required:
    - source_manifest_entry
    - ingest_analysis_file
  must_extract:
    - source_summary
    - key_claims
    - candidate_concepts
    - candidate_entities
    - contradiction_or_uncertainty_flags
    - recommended_generated_pages
    - operator_review_questions
  hard_stop: true
  next_allowed_action: "approve ingest"

ingest_phase_2:
  purpose: "Generate only the pages approved by the operator after phase 1."
  requires:
    - approved_phase_1_analysis
    - operator_phrase_approve_ingest
  may_create:
    - wiki/summaries/<source-slug>.md
    - wiki/concepts/<concept-slug>.md
    - wiki/entities/<entity-slug>.md
  must_update:
    - manifests/source-manifest.md
    - wiki/index.md
    - log/YYYY-MM-DD.md
```

## Page contracts

```yaml
summary_page:
  required_frontmatter:
    page_type: summary
    source_id: string
    raw_source_path: string
    confidence: "high | medium | low"
  required_sections:
    - Summary
    - Key claims
    - Concepts
    - Entities
    - Source pointers

concept_page:
  required_frontmatter:
    page_type: concept
    concept_id: string
    source_ids: array
    related_pages: array
  required_sections:
    - Definition
    - Source-backed notes
    - Related concepts
    - Open questions
    - Source pointers

entity_page:
  required_frontmatter:
    page_type: entity
    entity_type: "person | project | tool | source | organization | other"
    source_ids: array
  required_sections:
    - Summary
    - Known facts
    - Related pages
    - Source pointers

query_output:
  required_frontmatter:
    page_type: query_output
    question: string
    pages_read: array
    answer_confidence: "high | medium | low | insufficient"
  required_sections:
    - Question
    - Pages read
    - Answer
    - Evidence notes
    - Follow-up ingest candidates
```

## Query rules

```yaml
query_rules:
  read_order:
    1: "apex-meta/kb/<kb-slug>/wiki/index.md"
    2: "relevant summary/concept/entity pages"
    3: "one level of linked pages when needed"
  answer_policy:
    must_ground_in_compiled_kb: true
    if_insufficient: "Say the KB is insufficient and suggest sources to ingest."
    may_save_query_output: true
    save_path: "apex-meta/kb/<kb-slug>/outputs/queries/<YYYY-MM-DD>-<question-slug>.md"
```

## Apex integration rules

```yaml
apex_integration:
  apex_plan:
    send_only:
      - knowledge_gap_as_planning_task_candidate
      - unresolved_scope_question
      - candidate_source_ingest_decision
  apex_session:
    send_only:
      - kb_ingest_summary
      - raw_source_path
      - source_conflict
      - next_session_kb_context
  apex_sync:
    send_only:
      - deterministic_validation_request
      - related_task_ids_if_operator_requests_sync

  forbidden_cross_package_actions:
    - project_decomposition
    - task_status_mutation
    - exact_next_task_ranking
    - blocker_scan
    - apex_registry_rebuild
    - session_handoff_write_outside_kb
```
