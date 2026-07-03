---
title: "Agent-Specific Knowledge Base"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "agent-specific-knowledge-base"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 67-70; agent KB design questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C011; progressive disclosure and references"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C006 through B04-C017; source authority and state contracts"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Agent-Specific Knowledge Base

```yaml
pattern: "A durable agent may have its own doctrine root when its role repeats and needs stable validation knowledge."
used_when:
  - "An agent must remember domain rules without loading raw sources every session."
  - "Verifier quality depends on role-specific mistakes, templates, and evidence rules."
not_used_when:
  - "The capability is a one-off subagent task or a simple skill reference."
reads:
  - "activation seed"
  - "compiled agent KB pages"
  - "source_refs for disputed claims"
writes:
  - "candidate learning notes only after review"
  - "no autonomous doctrine promotion"
token_efficiency:
  - "Activation seed stays compact; deeper KB pages load on demand."
drift_controls:
  - "Source authority and claim status prevent agent doctrine from becoming self-referential."
unresolved_or_deferred:
  - "Exact agent KB folder taxonomy remains implementation work after S6."
```
