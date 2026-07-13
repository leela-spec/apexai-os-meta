# Apex KB Wiki Page Templates

## Phase 2 adaptive page value rules


- Use the exact required headings: Target Questions Answered, Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and Uncertainty / Raw Source Reopen Triggers.
- Declare only target-query IDs this page directly answers. A broad page must answer the material sub-questions, not merely state boundaries.
- Include only sources actually reviewed and materially used. Preserve unopened candidates in the topic ledger, never in page evidence.
- Scale sources and depth to answer requirements. `compiled_minimal` minimizes topology, not content.
- Do not duplicate frontmatter claims/source lists in prose or add numeric page-value scores.
- Create concept/entity pages only for independent project-specific retrieval value; otherwise preserve an embed/reject disposition.
- Run clean-context page-only and claim-entailment acceptance before `compiled_unvalidated`.
## Shared frontmatter


```yaml
required_fields:
  title: "<page title>"
  page_type: "summary | concept | entity | index | query_output | audit_item"
  kb_slug: "<kb-slug>"
  semantic_contract_version: "2"
  semantic_run_id: "<run-id>"
  target_query_ids: []
  source_refs:
    - source_id: "<source-id>"
      source_path: "<raw/source/path/or/pointer>"
      source_hash: "<sha256-or-NA>"
      source_pointer: "<heading/page/line/passage reference>"
      source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
  updated_at: "YYYY-MM-DDTHH:MM:SSZ"
  confidence: "high | medium | low | mixed | unknown"
  claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
  status: "draft | active | needs_review | deprecated | superseded"
```
## Summary page

```markdown
---
title: "<Source or Topic Summary>"
page_type: summary
kb_slug: "<kb-slug>"
summary_slug: "<summary-slug>"
semantic_contract_version: "2"
semantic_run_id: "<run-id>"
target_query_ids: []
source_refs:
  - source_id: "<source-id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts: []
related_entities: []
review_flags: []
---

# <Source or Topic Summary>

## Core Summary

<Direct source-grounded synthesis that answers the declared target questions.>

## Target Questions Answered

```yaml
target_questions_answered:
  - query_id: "<stable query id>"
    direct_answer: "<answer sufficient for compiled-first retrieval>"
    answer_section: "<this page heading or related page>"
```

## What This Adds

```yaml
adds: []
clarifies: []
limits: []
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Include only sources actually reviewed and materially used.
  - source_id: "<source-id>"
    source_path: "<path>"
    phase0_rank: 1 | NA
    analysis_ref: "ingest-analysis/<source>.analysis.md"
    reviewed_status: "complete | targeted"
    supported_query_ids: []
    claim_ids: []
    rationale: "<authority and relevance>"
    coverage: "<material contribution>"
```

## Macro / Meso / Micro

```markdown
### Macro

<High-level synthesis across all relevant sources.>

### Meso

<Medium-level synthesis capturing key patterns or themes.>

### Micro

<Specific details anchored to source pointers.>
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<pointer>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  # Describe how a user or question might arrive at this page and where it may lead next.
  - question: "<example question that leads here>"
    leads_to: "<target page path>"
    rationale: "<why this route exists>"
  - related_page: "<kb-slug>/concepts/<concept>.md"
    relation: "<relation description>"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  # Consolidate contradictions, open questions, and reasons to revisit the raw source.
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<pointer>"
    proposed_handling: "<audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator>"
```
```

## Concept page

```markdown
---
title: "<Concept Label>"
page_type: concept
kb_slug: "<kb-slug>"
concept_slug: "<concept-slug>"
semantic_contract_version: "2"
semantic_run_id: "<run-id>"
target_query_ids: []
source_refs:
  - source_id: "<source-id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts: []
related_entities: []
review_flags: []
---

# <Concept Label>

## Definition

<Project-specific definition and operating consequences grounded in exact source pointers.>

## Target Questions Answered

```yaml
target_questions_answered:
  - query_id: "<stable query id>"
    direct_answer: "<answer sufficient for compiled-first retrieval>"
    answer_section: "<this page heading or related page>"
```

## Operating Rules

```yaml
rules: []
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Include only sources actually reviewed and materially used.
  - source_id: "<source-id>"
    source_path: "<path>"
    phase0_rank: 1 | NA
    analysis_ref: "ingest-analysis/<source>.analysis.md"
    reviewed_status: "complete | targeted"
    supported_query_ids: []
    claim_ids: []
    rationale: "<authority and relevance>"
    coverage: "<material contribution>"
```

## Macro / Meso / Micro

```markdown
### Macro

<High-level synthesis of the concept across all sources.>

### Meso

<Medium-level synthesis capturing patterns or themes.>

### Micro

<Specific details anchored to source pointers.>
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<pointer>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "<example question that leads here>"
    leads_to: "<target page path>"
    rationale: "<why this route exists>"
  - related_page: "<kb-slug>/entities/<entity>.md"
    relation: "<relation description>"
```

## Evidence

```yaml
evidence:
  - source_id: "<source-id>"
    source_pointer: "<pointer>"
    supports: "<claim or section>"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<pointer>"
    proposed_handling: "<audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator>"
```
```

## Entity page

```markdown
---
title: "<Entity Label>"
page_type: entity
kb_slug: "<kb-slug>"
entity_slug: "<entity-slug>"
semantic_contract_version: "2"
semantic_run_id: "<run-id>"
target_query_ids: []
entity_type: "person | organization | tool | project | artifact | source | other"
source_refs:
  - source_id: "<source-id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts: []
review_flags: []
---

# <Entity Label>

## Identity

```yaml
entity:
  label: "<Entity Label>"
  type: "<entity_type>"
  aliases: []
```

## Source-Grounded Summary

<Project-specific identity, fields, rules, lifecycle, and relationships grounded in exact source pointers.>

## Target Questions Answered

```yaml
target_questions_answered:
  - query_id: "<stable query id>"
    direct_answer: "<answer sufficient for compiled-first retrieval>"
    answer_section: "<this page heading or related page>"
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Include only sources actually reviewed and materially used.
  - source_id: "<source-id>"
    source_path: "<path>"
    phase0_rank: 1 | NA
    analysis_ref: "ingest-analysis/<source>.analysis.md"
    reviewed_status: "complete | targeted"
    supported_query_ids: []
    claim_ids: []
    rationale: "<authority and relevance>"
    coverage: "<material contribution>"
```

## Macro / Meso / Micro

```markdown
### Macro

<High-level synthesis of the entity across all sources.>

### Meso

<Medium-level synthesis capturing patterns or themes.>

### Micro

<Specific details anchored to source pointers.>
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<pointer>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "<example question that leads here>"
    leads_to: "<target page path>"
    rationale: "<why this route exists>"
  - related_page: "<kb-slug>/summaries/<summary>.md"
    relation: "<relation description>"
```

## Evidence

```yaml
evidence: []
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<pointer>"
    proposed_handling: "<audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator>"
```
```
