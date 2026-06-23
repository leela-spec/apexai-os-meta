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
    - claim_label
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

  claim_label_allowed:
    - raw_source
    - source_backed_summary
    - behavioral_inference
    - working_hypothesis
    - operator_question
    - practitioner_question
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
    - source_storage_mode
```

# Template A - Summary Page

```markdown
---
title: "<Source or topic summary title>"
page_type: summary
kb_slug: "<kb-slug>"
summary_slug: "<source-or-topic-slug>"
source_refs:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts:
  - "<concept-slug>"
related_entities:
  - "<entity-slug>"
review_flags: []
---

# <Source or Topic Summary Title>

## Core Summary

<Write a dense, source-grounded summary of the source or topic. Preserve structure, claims, mechanisms, and limitations. Do not generalize beyond evidence.>

## What This Source Adds to the KB

```yaml
adds:
  - "<Specific reusable knowledge contribution.>"
clarifies:
  - "<Concept, process, entity, or decision this source clarifies.>"
limits:
  - "<What this source does not establish.>"
```

## Key Claims

```yaml
key_claims:
  - claim_id: "C001"
    claim: "<Specific source-grounded claim>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/<concept-slug>.md"
```

## Open Questions

```yaml
open_questions:
  - question_id: "Q001"
    question: "<Open knowledge question>"
    proposed_handling: "audit_item | planning_task_candidate | leave_as_gap | ask_operator"
    source_pointer: "<source pointer or NA>"
```
```

# Template B - Concept Page

```markdown
---
title: "<Concept Label>"
page_type: concept
kb_slug: "<kb-slug>"
concept_slug: "<concept-slug>"
source_refs:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
status: "draft | active | needs_review | deprecated | superseded"
aliases:
  - "<alias>"
related_concepts:
  - "<related-concept-slug>"
related_entities:
  - "<related-entity-slug>"
review_flags: []
---

# <Concept Label>

## Definition

<Define the concept using only source-grounded evidence. If sources disagree, present competing definitions instead of merging silently.>

## Source-Grounded Notes

```yaml
source_grounded_notes:
  - note_id: "N001"
    note: "<Specific note>"
    source_id: "<source-id>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```

## Relationships

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

## Usage Patterns

```yaml
usage_patterns:
  - pattern_id: "P001"
    pattern: "<How this concept is used operationally or analytically>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    claim_label: "behavioral_inference | source_backed_summary | working_hypothesis"
```

## Applied Card

```yaml
applied_card:
  shortest_useful_summary: "<One or two sentences for fast practical use.>"
  when_this_pattern_appears:
    - "<Observable situation or cue.>"
  questions_to_ask:
    - "<Precise applied question.>"
  do_not_do:
    - "<Common misuse, overreach, or bypass.>"
  next_clean_action: "<Smallest practical action if this concept is active.>"
```

## Contradictions and Variants

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

## Open Questions

```yaml
open_questions:
  - question_id: "Q001"
    question: "<Open question>"
    blocks_use: false
    proposed_handling: "audit_item | ingest_more_sources | ask_operator | practitioner_review"
```
```

# Template C - Entity Page

```markdown
---
title: "<Entity Label>"
page_type: entity
kb_slug: "<kb-slug>"
entity_slug: "<entity-slug>"
entity_type: "person | organization | project | tool | framework | file | artifact | other"
source_refs:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
status: "draft | active | needs_review | deprecated | superseded"
aliases: []
related_concepts: []
review_flags: []
---

# <Entity Label>

## Entity Summary

<Describe the entity only from source-grounded evidence.>

## Source-Grounded Facts

```yaml
source_grounded_facts:
  - fact_id: "F001"
    fact: "<Specific fact>"
    source_id: "<source-id>"
    source_pointer: "<source pointer>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```
```

# Template D - Wiki Index

```markdown
---
title: "<KB Title> Index"
page_type: index
kb_slug: "<kb-slug>"
source_refs: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "mixed"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# <KB Title> Index

<!-- BEGIN AUTO-GENERATED INDEX -->

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
  stale_index_hash: "NA"
```

<!-- END AUTO-GENERATED INDEX -->

<!-- BEGIN LLM SUMMARY -->

## LLM Summary

<LLM-owned semantic overview. Do not overwrite the machine-generated section.>

<!-- END LLM SUMMARY -->
```

# Template E - Query Output

```markdown
---
title: "<Query Title>"
page_type: query_output
kb_slug: "<kb-slug>"
query_slug: "<query-slug>"
source_refs:
  - source_id: "<source-id-or-page-path>"
    source_path: "<wiki/page/path>"
    source_hash: "NA"
    source_pointer: "<section anchor>"
    source_storage_mode: "pointer_only"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary | behavioral_inference | working_hypothesis"
status: "draft | active | needs_review"
review_flags: []
---

# <Query Title>

## Answer

<Answer from compiled KB pages and explicit source pointers. Preserve uncertainty.>

## Evidence Pages

```yaml
evidence_pages:
  - page_path: "wiki/<path>.md"
    relevant_sections:
      - "<section heading>"
    supports:
      - "<answer claim>"
```
```

# Template F - Audit Item

```markdown
---
title: "<Audit Item Title>"
page_type: audit_item
kb_slug: "<kb-slug>"
audit_id: "<audit-id>"
source_refs:
  - source_id: "<source-id-or-page-path>"
    source_path: "<source/page/path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "operator_question | practitioner_question | working_hypothesis"
status: "draft | active | needs_review | deprecated | superseded"
review_flags: []
---

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

## Summary

<Short description of the issue, feedback, contradiction, quality concern, or gap.>
```

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
      - claim_label_and_confidence_separated
```
