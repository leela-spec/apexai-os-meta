---
title: "Ephemeral Subagent Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "ephemeral-subagent-boundary"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C008 through B02-C009; subagent context isolation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 76-87; ephemeral subagent policy"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Ephemeral Subagent Boundary

```yaml
pattern: "Use an ephemeral subagent for isolated temporary research, comparison, or exploration."
used_when:
  - "The task benefits from a separate context window and compact returned summary."
not_used_when:
  - "The role repeats enough to justify persistent doctrine and validation."
reads:
  - "task prompt"
  - "limited source refs"
writes:
  - "summary result"
  - "candidate findings"
token_efficiency:
  - "Main context receives only the result, not all exploration traces."
drift_controls:
  - "Ephemeral subagent findings remain candidate until reviewed."
unresolved_or_deferred:
  - "No subagent definition is written in S6."
```
