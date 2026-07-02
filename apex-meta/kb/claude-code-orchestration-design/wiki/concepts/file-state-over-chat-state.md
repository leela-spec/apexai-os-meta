---
title: "File State over Chat State"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "file-state-over-chat-state"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; file_state_over_chat_state"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C011, B04-C014 and tension B04-T002"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# File State over Chat State

```yaml
pattern: "Durable work state belongs in files or file-like artifacts, not in conversational memory."
used_when:
  - "A future session must verify, continue, or audit the work."
not_used_when:
  - "The conversation is purely transient."
reads:
  - "current files"
  - "accepted packets"
writes:
  - "state artifact"
  - "fetch-back proof"
token_efficiency:
  - "Future agents read current files rather than reconstructing old messages."
drift_controls:
  - "Fetch-back validation anchors claims to written artifacts."
unresolved_or_deferred:
  - "S6 writes KB wiki/log artifacts only."
```
