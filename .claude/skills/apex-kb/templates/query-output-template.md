---
title: "Query: <query>"
page_type: query_output
kb_slug: "<kb-slug>"
source_refs: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary | working_hypothesis | operator_question"
status: "active"
query:
  text: "<query>"
  backend: "index_first_markdown | sqlite_fts5_bm25 | json_fallback"
  stale_status: "fresh | stale | missing | unknown"
---

# Query: <query>

## Answer

<Compact answer synthesized from compiled KB pages only.>

## Evidence Pages

```yaml
evidence_pages:
  - rel_path: "wiki/<type>/<page>.md"
    heading: "<heading>"
    lines: "<start>-<end>"
    confidence: "high | medium | low | mixed | unknown"
    claim_label: "<claim_label>"
    source_refs:
      - source_id: "<source-id>"
        source_pointer: "<pointer>"
```

## Citations

- `<wiki/path.md#heading>` - `<source pointer>`

## Gaps / Open Questions

```yaml
open_questions: []
contradictions: []
```

## Reuse Notes

```yaml
reuse:
  suitable_for_future_context: true
  planning_mutation_allowed: false
  session_mutation_allowed: false
```
