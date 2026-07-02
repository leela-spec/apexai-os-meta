---
title: "Candidate Is Not Accepted Truth"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "candidate-is-not-accepted-truth"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 78-83; evidence, candidate, validated, accepted truth"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 124-145; doctrine vs deferred boundary"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C015 through B04-C017; promotion caution"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Candidate Is Not Accepted Truth

```yaml
pattern: "Candidate outputs, inferred lessons, and proposed state deltas remain non-authoritative until validated and accepted."
used_when:
  - "A model, agent, or workflow proposes doctrine, status, or next action."
not_used_when:
  - "A source quote is being preserved as raw source, not promoted."
reads:
  - "candidate output"
  - "source_refs"
  - "validation result"
writes:
  - "accepted claim only after gate"
  - "otherwise needs_review or open_question"
token_efficiency:
  - "Claim status prevents future agents from re-litigating authority."
drift_controls:
  - "No silent promotion from generated candidate to doctrine."
unresolved_or_deferred:
  - "S7 deterministic validation may catch shape issues but cannot decide semantic truth."
```
