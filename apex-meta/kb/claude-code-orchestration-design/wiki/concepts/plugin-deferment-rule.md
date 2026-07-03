---
title: "Plugin Deferment Rule"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "plugin-deferment-rule"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C012 through B02-C013; plugins and MCP"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 69-74 and 88-91; plugins and MCP deferred"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Plugin Deferment Rule

```yaml
pattern: "Use project skills first; defer plugins and MCP packaging until reusable project surfaces stabilize."
used_when:
  - "A capability may later need distribution or external connectivity."
not_used_when:
  - "A simple project skill or reference file is sufficient now."
reads:
  - "reuse scope"
  - "trust risk"
  - "packaging need"
writes:
  - "deferment note"
  - "open policy question"
token_efficiency:
  - "Avoids loading or maintaining broader plugin surfaces prematurely."
drift_controls:
  - "Trust-sensitive packaging is not promoted before policy exists."
unresolved_or_deferred:
  - "Plugin and MCP policy are explicit future work."
```
