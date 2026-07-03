---
title: "Workflow Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "workflow-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; process becomes workflow"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C008; stage-gated workflow"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Workflow Boundary

```yaml
pattern: "Use a workflow when multiple staged artifacts, gates, or roles must execute in order."
used_when:
  - "A process is larger than one skill and has stage-specific reads and writes."
not_used_when:
  - "One concise skill can safely produce the artifact."
reads:
  - "stage inputs"
  - "prior artifacts"
writes:
  - "stage outputs"
  - "handoff packets"
token_efficiency:
  - "Each stage reads only its packet and emits a bounded artifact."
drift_controls:
  - "Gates prevent stage collapse and premature downstream use."
unresolved_or_deferred:
  - "No workflow files are written during S6."
```
