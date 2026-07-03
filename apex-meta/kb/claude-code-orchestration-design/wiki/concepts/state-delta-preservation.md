---
title: "State Delta Preservation"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "state-delta-preservation"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 95-98; execution evidence to state delta to next context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C014; clean handoffs and closure"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# State Delta Preservation

```yaml
pattern: "Preserve what changed, why it changed, and which evidence supports it, instead of rewriting full state from memory."
used_when:
  - "Execution evidence changes project state or next-session context."
not_used_when:
  - "No accepted change occurred."
reads:
  - "previous state"
  - "execution evidence"
  - "validation result"
writes:
  - "state delta"
  - "next-context input"
token_efficiency:
  - "Deltas keep future context small and auditable."
drift_controls:
  - "Accepted deltas preserve source refs and prevent chat-memory reconstruction."
unresolved_or_deferred:
  - "Canonical state file format is outside S6."
```
