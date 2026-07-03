---
title: "Session Memory and Next Context"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "session-memory-and-next-context"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 95-98; state delta and next session context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C017; clean handoffs and state frames"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Session Memory and Next Context

```yaml
pattern: "Session memory is externalized into compact next-context artifacts rather than left in chat history."
used_when:
  - "A future session must continue project work from a known state."
not_used_when:
  - "The interaction is disposable and has no durable consequence."
reads:
  - "latest accepted state"
  - "validated deltas"
  - "open questions"
writes:
  - "next-context packet"
token_efficiency:
  - "Future sessions read compact state, not old chat logs."
drift_controls:
  - "Only accepted deltas enter next context."
unresolved_or_deferred:
  - "This page does not create session files or schedulers."
```
