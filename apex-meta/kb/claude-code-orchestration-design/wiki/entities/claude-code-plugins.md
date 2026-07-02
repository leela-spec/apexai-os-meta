---
title: "Claude Code Plugins"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-plugins"
entity_type: "distribution_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C012 through B02-C013; entities extracted"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 69-74; project skills now, plugins later"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code Plugins

```yaml
role: "Distribution bundle for multiple Claude Code components."
used_when:
  - "A stable capability must be packaged beyond one project."
not_used_when:
  - "A project skill or local reference is sufficient."
reads:
  - "component set"
  - "trust policy"
writes:
  - "packaged extension outside S6"
token_efficiency:
  - "Defer packaging until surfaces stabilize."
drift_controls:
  - "Trust-sensitive bundles are not promoted prematurely."
deferred:
  - "Plugin packaging is later work."
```
