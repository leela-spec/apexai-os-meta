---
title: "Status Merge Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "status-merge-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; canonical state vs temporary execution evidence"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C011, B04-C014"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Status Merge Packet

```yaml
pattern: "A status merge packet accepts validated recap deltas into canonical project state."
used_when:
  - "Several recap outputs must be reconciled into one project state view."
not_used_when:
  - "The recap is still candidate or unreviewed."
reads:
  - "accepted flow recap packets"
  - "previous status packet"
writes:
  - "updated status"
  - "conflict notes"
  - "next-context seed"
token_efficiency:
  - "Merge stores accepted deltas instead of raw dumps."
drift_controls:
  - "Conflicts are exposed for review before acceptance."
unresolved_or_deferred:
  - "No status-merge runtime is implemented in S6."
```
