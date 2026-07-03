---
title: "Claude Code Subagents"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-subagents"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C008 through B02-C009; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code Subagents

```yaml
role: "Context-isolated worker sessions with custom prompts, tools, models, and permissions."
used_when:
  - "A task needs separate context and compact return."
not_used_when:
  - "A static skill or page can carry the work."
reads:
  - "delegated prompt"
  - "bounded sources"
writes:
  - "summary result"
token_efficiency:
  - "Main thread receives the result, not the full exploration."
drift_controls:
  - "Returned findings remain candidate until validated."
deferred:
  - "No subagent definitions are created in S6."
```
