---
title: "BMAD-METHOD"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "bmad-method"
entity_type: "external_repo"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C005 through B03-C007; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# BMAD-METHOD

```yaml
role: "Comparative source for skill migration, validation, and package encapsulation patterns."
used_when:
  - "Retrieving external examples of deterministic-first validation or package boundaries."
not_used_when:
  - "Treating BMAD-specific naming rules as Apex doctrine."
reads:
  - "migration checklist"
  - "skill validator"
writes:
  - "comparative pattern only"
token_efficiency:
  - "Use extracted validation concepts instead of full repo scans."
drift_controls:
  - "External repo patterns do not override Apex gates."
deferred:
  - "No BMAD runtime or naming policy is adopted in S6."
```
