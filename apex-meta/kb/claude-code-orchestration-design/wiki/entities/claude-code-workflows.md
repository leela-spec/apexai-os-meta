---
title: "Claude Code Workflows"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-workflows"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "source scope; Claude Code control plane"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C008; staged processes"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code Workflows

```yaml
role: "Multi-stage orchestration surface for processes larger than one skill."
used_when:
  - "A process needs ordered stages, gates, or multiple outputs."
not_used_when:
  - "One skill or static artifact is enough."
reads:
  - "stage inputs"
  - "prior outputs"
writes:
  - "stage artifacts"
token_efficiency:
  - "Stage packets localize context."
drift_controls:
  - "Gates separate planning, work, and review."
deferred:
  - "No workflow definitions are created in S6."
```
