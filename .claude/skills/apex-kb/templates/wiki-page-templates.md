# Apex KB Wiki Page Templates
```yaml
template_metadata:
  artifact_name: apex_kb_wiki_page_templates
  file_role: phase_2_wiki_page_templates
  package_path: ".claude/skills/apex-kb/templates/wiki-page-templates.md"
  canonical_rules:
    kb_contract: ".claude/skills/apex-kb/references/kb-contract.md"
    operation_rules: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    ingest_analysis_template: ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
  phase: ingest_phase_2
  phase_2_requires_operator_phrase: "approve ingest"
  source_basis:
    copied_blueprint_behaviors:
      - persistent_compiled_wiki
      - source_grounded_pages
      - concept_entity_summary_separation
      - wikilinks
      - contradiction_callouts
      - index_first_query_support
    adapted_blueprint_behaviors:
      - page_schema_to_apex_kb_paths
      - CLAUDE_md_schema_to_kb_schema_md
      - source_manifest_to_visible_manifests_folder
  page_types:
    - summary
    - concept
    - entity
    - index
    - query_output
    - audit_item
  global_page_rules:
    source_pointers_required: true
    frontmatter_required: true
    wikilinks_allowed: true
    unresolved_contradictions_visible: true
    missing_source_means_no_claim: true
    do_not_write_without_phase_2_approval: true
```


#

# Shared Frontmatter Rules
```yaml
shared_frontmatter_rules:
  required_fields:
    - title
    - page_type
    - kb_slug
    - source_refs
    - created_at
    - updated_at
    - confidence
    - status
  page_type_allowed:
    - summary
    - concept
    - entity
    - index
    - query_output
    - audit_item
  confidence_allowed:
    - high
    - medium
    - low
    - mixed
    - unknown
  status_allowed:
    - draft
    - active
    - needs_review
    - deprecated
    - superseded
  source_ref_shape:
    - source_id
    - source_path
    - source_hash
    - source_pointer
```

# Template A — Summary Page
```markdown
---title: "<Source or topic summary title>"page_type: summarykb_slug: "<kb-slug>"summary_slug: "<source-or-topic-slug>"source_refs:  - source_id: "<source-id>"    source_path: "<raw/source/path/or/pointer>"    source_hash: "<sha256-or-NA>"    source_pointer: "<heading/page/anchor/line/passage reference>"created_at: "YYYY-MM-DDTHH:MM:SSZ"updated_at: "YYYY-MM-DDTHH:MM:SSZ"confidence: "high | medium | low | mixed | unknown"status: "draft | active | needs_review | deprecated | superseded"related_concepts:  - "<concept-slug>"related_entities:  - "<entity-slug>"review_flags: []---

# <Source or Topic Summary Title>
```yaml
page_metadata:
  page_type: summary
  intended_use: "Fast source-level context retrieval for future AI work."
  source_grounding: "All substantive claims require source_refs or inline source pointers."
```


#

# Core Summary<Write a dense, source-grounded summary of the source or topic. Preserve the source’s actual structure, claims, mechanisms, and limitations. Do not generalize beyond the available evidence.>

## What This Source Adds to the KB- **Adds:** <Specific reusable knowledge contribution.>- **Clarifies:** <Concept, process, entity, or decision this source clarifies.>- **Limits:** <What this source does not establish.>

## Key Claims
```yaml
key_claims:
  - claim_id: "C001"
    claim: "<Specific source-grounded claim>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    used_in_pages:
      - "wiki/concepts/<concept-slug>.md"
```


#

# Extracted Concepts
```yaml
extracted_concepts:
  - concept_slug: "<concept-slug>"
    concept_label: "<Concept label>"
    page_path: "wiki/concepts/<concept-slug>.md"
    source_pointer: "<heading/page/anchor/line/passage reference>"
```


#

# Extracted Entities
```yaml
extracted_entities:
  - entity_slug: "<entity-slug>"
    entity_label: "<Entity label>"
    entity_type: "person | organization | project | tool | framework | file | artifact | other"
    page_path: "wiki/entities/<entity-slug>.md"
    source_pointer: "<heading/page/anchor/line/passage reference>"
```


#

# Contradictions and Tensions
```yaml
contradictions:
  status: "none_detected | possible | confirmed"
  items:
    - contradiction_id: "X001"
      severity: "low | medium | high"
      summary: "<Visible contradiction or tension>"
      source_pointer: "<current source pointer>"
      related_page: "<existing page path or NA>"
      handling: "callout_added | audit_item_needed | operator_review_needed"
```


#

# Open Questions
```yaml
open_questions:
  - question_id: "Q001"
    question: "<Open knowledge question>"
    proposed_handling: "audit_item | planning_task_candidate | leave_as_gap | ask_operator"
    source_pointer: "<source pointer or NA>"
```


#

# Backlinks
```yaml
backlinks:
  concepts:
    - "[[<concept-slug>]]"
  entities:
    - "[[<entity-slug>]]"
  related_summaries:
    - "[[<summary-slug>]]"
``````

# Template B — Concept Page
```markdown
---title: "<Concept Label>"page_type: conceptkb_slug: "<kb-slug>"concept_slug: "<concept-slug>"source_refs:  - source_id: "<source-id>"    source_path: "<raw/source/path/or/pointer>"    source_hash: "<sha256-or-NA>"    source_pointer: "<heading/page/anchor/line/passage reference>"created_at: "YYYY-MM-DDTHH:MM:SSZ"updated_at: "YYYY-MM-DDTHH:MM:SSZ"confidence: "high | medium | low | mixed | unknown"status: "draft | active | needs_review | deprecated | superseded"aliases:  - "<alias>"related_concepts:  - "<related-concept-slug>"related_entities:  - "<related-entity-slug>"review_flags: []---

# <Concept Label>
```yaml
page_metadata:
  page_type: concept
  intended_use: "Reusable concept page for fast context loading and crosslinking."
  concept_slug: "<concept-slug>"
```


#

# Definition<Define the concept using only source-grounded evidence. If multiple sources disagree, present the competing definitions instead of merging them silently.>

## Why It Matters<Explain why this concept matters inside the KB’s domain and future Apex/AI work. Keep it short and source-grounded.>

## Source-Grounded Notes
```yaml
source_grounded_notes:
  - note_id: "N001"
    note: "<Specific note>"
    source_id: "<source-id>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
```


#

# Relationships
```yaml
relationships:
  parent_concepts:
    - "[[<parent-concept-slug>]]"
  child_concepts:
    - "[[<child-concept-slug>]]"
  related_concepts:
    - "[[<related-concept-slug>]]"
  related_entities:
    - "[[<entity-slug>]]"
  source_summaries:
    - "[[<summary-slug>]]"
```


#

# Usage Patterns
```yaml
usage_patterns:
  - pattern_id: "P001"
    pattern: "<How this concept is used operationally or analytically>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
```


#

# Contradictions and Variants
```yaml
contradictions_and_variants:
  status: "none_detected | possible | confirmed"
  items:
    - item_id: "X001"
      type: "contradiction | variant | unresolved_tension"
      summary: "<What differs between sources>"
      source_refs:
        - "<source pointer A>"
        - "<source pointer B>"
      handling: "preserve_both | audit_item_needed | operator_review_needed"
```


#

# Open Questions
```yaml
open_questions:
  - question_id: "Q001"
    question: "<Question about the concept>"
    blocks_use: false
    proposed_handling: "audit_item | planning_task_candidate | leave_as_gap | ask_operator"
```


#

# Source Pointers
```yaml
source_pointers:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    supports:
      - "definition"
      - "usage_patterns"
      - "relationships"
``````

# Template C — Entity Page
```markdown
---title: "<Entity Label>"page_type: entitykb_slug: "<kb-slug>"entity_slug: "<entity-slug>"entity_type: "person | organization | project | tool | framework | file | artifact | other"source_refs:  - source_id: "<source-id>"    source_path: "<raw/source/path/or/pointer>"    source_hash: "<sha256-or-NA>"    source_pointer: "<heading/page/anchor/line/passage reference>"created_at: "YYYY-MM-DDTHH:MM:SSZ"updated_at: "YYYY-MM-DDTHH:MM:SSZ"confidence: "high | medium | low | mixed | unknown"status: "draft | active | needs_review | deprecated | superseded"aliases:  - "<alias>"related_concepts:  - "<concept-slug>"related_entities:  - "<related-entity-slug>"review_flags: []---

# <Entity Label>
```yaml
page_metadata:
  page_type: entity
  intended_use: "Reusable entity page for people, organizations, projects, tools, files, or artifacts."
  entity_slug: "<entity-slug>"
  entity_type: "<entity-type>"
```


#

# Entity Summary<Describe what the source material establishes about this entity. Do not add biographical, organizational, or tool claims not present in the KB sources.>

## Role in This KB
```yaml
role_in_kb:
  role_summary: "<Why this entity matters here>"
  appears_in:
    - "wiki/summaries/<summary-slug>.md"
  connected_concepts:
    - "wiki/concepts/<concept-slug>.md"
```


#

# Source-Grounded Facts
```yaml
source_grounded_facts:
  - fact_id: "F001"
    fact: "<Specific fact about the entity>"
    source_id: "<source-id>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
```


#

# Relationships
```yaml
relationships:
  related_entities:
    - entity: "[[<entity-slug>]]"
      relationship: "<relationship label>"
      source_pointer: "<source pointer>"
  related_concepts:
    - concept: "[[<concept-slug>]]"
      relationship: "<relationship label>"
      source_pointer: "<source pointer>"
  source_summaries:
    - "[[<summary-slug>]]"
```


#

# Known Ambiguities
```yaml
known_ambiguities:
  - ambiguity_id: "A001"
    summary: "<Ambiguity, naming collision, incomplete source, or uncertainty>"
    source_pointer: "<source pointer or NA>"
    proposed_handling: "alias | audit_item | operator_review | leave_flagged"
```


#

# Contradictions
```yaml
contradictions:
  status: "none_detected | possible | confirmed"
  items:
    - contradiction_id: "X001"
      summary: "<Contradiction involving this entity>"
      source_refs:
        - "<source pointer A>"
        - "<source pointer B>"
      handling: "preserve_both | audit_item_needed | operator_review_needed"
```


#

# Source Pointers
```yaml
source_pointers:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    supports:
      - "entity_summary"
      - "facts"
      - "relationships"
``````

# Template D — Wiki Index
```markdown
---title: "<KB Title> Index"page_type: indexkb_slug: "<kb-slug>"source_refs: []created_at: "YYYY-MM-DDTHH:MM:SSZ"updated_at: "YYYY-MM-DDTHH:MM:SSZ"confidence: "mixed"status: "active"review_flags: []---

# <KB Title> Index
```yaml
index_metadata:
  kb_slug: "<kb-slug>"
  kb_schema: "kb-schema.md"
  index_role: "Entry point for index-first query and fast AI context loading."
  machine_section_owner: python
  llm_section_owner: llm
```


#

# How to Use This KB1. Start with this index.2. Select the smallest relevant set of pages.3. Read selected pages fully before answering.4. Preserve contradictions and gaps.5. Save important query outputs under `outputs/queries/` when useful.

## KB Scope
```yaml
kb_scope:
  kb_topic_title: "<from kb-schema.md>"
  language_policy: "<from kb-schema.md>"
  source_authority_policy: "<from kb-schema.md>"
```<!-- BEGIN AUTO-GENERATED INDEX -->
```yaml
machine_generated_index:
  generated_at: "YYYY-MM-DDTHH:MM:SSZ"
  generated_by: "apex_kb.py index"
  page_count: 0
  pages:
    summaries: []
    concepts: []
    entities: []
  detected_links: []
  orphan_pages: []
  stale_index_hash: "<hash-or-NA>"
```<!-- END AUTO-GENERATED INDEX --><!-- BEGIN LLM SUMMARY -->

## LLM Summary<LLM-owned semantic overview of the KB. Include major categories, central concepts, source clusters, contradictions, and knowledge gaps. Do not overwrite the machine-generated section.>

## Major Concept Clusters
```yaml
major_concept_clusters:
  - cluster_id: "CL001"
    label: "<Cluster label>"
    concepts:
      - "[[<concept-slug>]]"
    summaries:
      - "[[<summary-slug>]]"
    notes: "<Short semantic note>"
```


#

# Knowledge Gaps
```yaml
knowledge_gaps:
  - gap_id: "G001"
    gap: "<Known gap>"
    related_pages:
      - "wiki/concepts/<concept-slug>.md"
    proposed_handling: "ingest_more_sources | audit_item | planning_task_candidate | leave_as_gap"
```


#

# Active Contradictions
```yaml
active_contradictions:
  - contradiction_id: "X001"
    summary: "<Contradiction summary>"
    related_pages:
      - "wiki/concepts/<concept-slug>.md"
    handling: "audit_item_needed | operator_review_needed | preserved_variant"
```<!-- END LLM SUMMARY -->```

# Template E — Query Output
```markdown
---title: "<Query Title>"page_type: query_outputkb_slug: "<kb-slug>"query_slug: "<query-slug>"source_refs:  - source_id: "<source-id-or-page-path>"    source_path: "<wiki/page/path>"    source_hash: "NA"    source_pointer: "<section anchor>"created_at: "YYYY-MM-DDTHH:MM:SSZ"updated_at: "YYYY-MM-DDTHH:MM:SSZ"confidence: "high | medium | low | mixed | unknown"status: "draft | active | needs_review"review_flags: []---

# <Query Title>
```yaml
query_metadata:
  query: "<operator query>"
  kb_slug: "<kb-slug>"
  query_mode: "index_first"
  pages_read:
    - "wiki/index.md"
    - "wiki/concepts/<concept-slug>.md"
  saved_because: "<Why this query output is useful to preserve>"
```


#

# Answer<Answer the query using only the compiled KB pages and explicit source pointers. Preserve uncertainty.>

## Evidence Pages
```yaml
evidence_pages:
  - page_path: "wiki/<path>.md"
    relevant_sections:
      - "<section heading>"
    supports:
      - "<answer claim>"
```


#

# Confidence
```yaml
confidence_assessment:
  confidence: "high | medium | low | mixed | unknown"
  rationale: "<Why this confidence level is appropriate>"
```


#

# Contradictions
```yaml
contradictions:
  status: "none_detected | possible | confirmed"
  items:
    - contradiction_id: "X001"
      summary: "<Contradiction relevant to the answer>"
      related_pages:
        - "wiki/<path>.md"
      impact_on_answer: "<How it affects the answer>"
```


#

# Knowledge Gaps
```yaml
knowledge_gaps:
  - gap_id: "G001"
    gap: "<Missing knowledge needed for stronger answer>"
    proposed_handling: "ingest_more_sources | audit_item | planning_task_candidate | leave_as_gap"
```


#

# Suggested Followups
```yaml
suggested_followups:
  - "<Followup query, source ingest, or audit action>"
``````

# Template F — Audit Item
```markdown
---title: "<Audit Item Title>"page_type: audit_itemkb_slug: "<kb-slug>"audit_id: "<audit-id>"source_refs:  - source_id: "<source-id-or-page-path>"    source_path: "<source/page/path>"    source_hash: "<sha256-or-NA>"    source_pointer: "<heading/page/anchor/line/passage reference>"created_at: "YYYY-MM-DDTHH:MM:SSZ"updated_at: "YYYY-MM-DDTHH:MM:SSZ"confidence: "high | medium | low | mixed | unknown"status: "draft | active | needs_review | deprecated | superseded"review_flags: []---

# <Audit Item Title>
```yaml
audit_item:
  audit_id: "<audit-id>"
  type: "contradiction | quality | staleness | gap | naming | source_authority | broken_link | missing_source_pointer | duplicate_page | operator_note"
  severity: "low | medium | high"
  status: "open | resolved | deferred | rejected"
  target_path: "<wiki/page/path>"
  target_anchor: "<heading-or-anchor-or-NA>"
  source_ref: "<source pointer or NA>"
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
```


#

# Summary<Short description of the issue, feedback, contradiction, quality concern, or gap.>

## Evidence
```yaml
evidence:
  - evidence_id: "E001"
    source_path: "<source/page/path>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    note: "<What this evidence shows>"
```


#

# Proposed Resolution
```yaml
proposed_resolution:
  recommendation: "accept | partial | reject | defer"
  action:
    - "<Proposed page edit, source ingest, link fix, naming change, or operator decision>"
  reason: "<Why this resolution is appropriate>"
```


#

# Operator Decision
```yaml
operator_decision:
  decision: "pending | accept | partial | reject | defer"
  decided_at: "YYYY-MM-DDTHH:MM:SSZ | NA"
  decision_note: "<Operator note or NA>"
  move_to_resolved_when_complete: false
``````


#

# Completion Gate
```yaml
completion_gate:
  valid_wiki_page_templates_file:
    required:
      - summary_template_present
      - concept_template_present
      - entity_template_present
      - index_template_present
      - query_output_template_present
      - audit_item_template_present
      - shared_frontmatter_rules_present
      - source_pointer_policy_present
      - contradiction_visibility_present
  invalid_if:
    - source_pointers_optional_for_substantive_claims
    - contradiction_sections_removed
    - index_machine_and_llm_sections_collapsed
    - phase_2_gate_removed
    - generated_claims_allowed_without_sources
    - script_generated_semantic_sections
```
