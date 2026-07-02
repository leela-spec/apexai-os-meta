---
title: "Agent Learning Queue Candidate Only"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "agent-learning-queue-candidate-only"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 47-48 and 67-70; agent-specific KBs, verifier loops, drift control"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C015, B04-C017; out-of-mode capture and promotion caution"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "needs_review"
---

# Agent Learning Queue Candidate Only

```yaml
pattern: "New lessons enter an agent learning queue as candidates, not accepted doctrine."
used_when:
  - "An execution reveals a reusable improvement, mistake, or template candidate."
not_used_when:
  - "The claim lacks source, validation, or clear owner."
reads:
  - "execution evidence"
  - "source_refs"
  - "current doctrine"
writes:
  - "candidate learning item"
  - "review status"
token_efficiency:
  - "Capture a short candidate pointer instead of appending long chat history."
drift_controls:
  - "Promotion requires validation; candidate is not accepted truth."
unresolved_or_deferred:
  - "Exact learning queue file layout is deferred beyond S6."
```
