---
title: "Semantic Planning Layer"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "semantic-planning-layer"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; semantic planning vs deterministic computation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007, B04-C008, B04-C017; bounded execution and source authority"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Semantic Planning Layer

```yaml
pattern: "Semantic planning interprets goals, constraints, and source authority before deterministic work or mutation."
used_when:
  - "The next action requires judgment, prioritization, or synthesis."
not_used_when:
  - "A deterministic script can compute the answer without semantic interpretation."
reads:
  - "operator intent"
  - "source authority"
  - "current state"
writes:
  - "plan candidate"
  - "task frame"
  - "open questions"
token_efficiency:
  - "Plan from compact source-routed context instead of raw corpus rereads."
drift_controls:
  - "Planning does not equal state mutation."
unresolved_or_deferred:
  - "Runtime planner implementation is outside S6."
```
