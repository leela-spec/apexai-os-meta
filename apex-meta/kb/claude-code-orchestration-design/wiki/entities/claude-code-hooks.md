---
title: "Claude Code Hooks"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-hooks"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C005 through B02-C007; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code Hooks

```yaml
role: "Lifecycle event mechanism for enforcement, verification, logging, or automation around turns and tool use."
used_when:
  - "A boundary needs tool/event-level enforcement."
not_used_when:
  - "A prose instruction is sufficient."
reads:
  - "event payload"
  - "policy rule"
writes:
  - "gate result or log"
token_efficiency:
  - "Hooks can replace repeated gate reminders."
drift_controls:
  - "Hard boundaries are not left only to instructions."
deferred:
  - "No hook files are created in S6."
```
