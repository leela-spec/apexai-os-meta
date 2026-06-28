# Apex KB Wiki Page Templates

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

## Contradictions

```yaml
contradictions: []
```

## Open Questions

```yaml
open_questions: []
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

## Relationships

```yaml
related_concepts: []
related_entities: []
```

## Evidence

```yaml
evidence:
  - source_id: "<source-id>"
    source_pointer: "<pointer>"
    supports: "<claim or section>"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions: []
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

## Known Relationships

```yaml
relationships: []
```

## Evidence

```yaml
evidence: []
```

## Open Questions

```yaml
open_questions: []
```
```
