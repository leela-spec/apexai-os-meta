# Apex KB Wiki Page Templates

## Phase 2 adaptive page value rules

- Use the exact required headings: Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and Uncertainty / Raw Source Reopen Triggers.
- Do not impose a fixed source count. Carry every materially relevant Phase 1 source for broad pages; narrow pages may need only one or a few sources.
- Do not require a separate source cluster map on every page.
- Do not add a `page_value_score` metric.
- Prefer warnings/reporting for missing value sections before hard failures.

## Shared frontmatter

```yaml
required_fields:
  title: "<page title>"
  page_type: "summary | concept | entity | index | query_output | audit_item"
  kb_slug: "<kb-slug>"
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

<Source-grounded summary. Do not generalize beyond evidence.>

## What This Adds

```yaml
adds: []
clarifies: []
limits: []
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Provide a ranked list of sources supporting this summary.
  # Scale the number of sources with KB size, topic breadth, and source diversity.
  # Each entry should include a rationale for its rank and coverage description.
  - source_id: "<source-id>"
    rationale: "<why this source is ranked here relative to others>"
    coverage: "<brief description of what the source covers>"
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

<Definition grounded in cited source pointers.>

## Operating Rules

```yaml
rules: []
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Ranked list of sources supporting this concept.
  # Scale the number of sources with KB size, topic breadth, and source diversity.
  - source_id: "<source-id>"
    rationale: "<why this source is ranked here>"
    coverage: "<brief description of the source's coverage>"
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

<Summary grounded in source pointers.>

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Ranked list of sources supporting this entity.
  # Scale the number of sources with KB size, topic breadth, and source diversity.
  - source_id: "<source-id>"
    rationale: "<why this source is ranked here>"
    coverage: "<brief description of the source's coverage>"
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
