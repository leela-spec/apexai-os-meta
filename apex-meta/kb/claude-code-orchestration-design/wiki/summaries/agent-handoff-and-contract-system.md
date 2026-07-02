---
title: "Agent Handoff and Contract System"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "agent-handoff-and-contract-system"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; handoff_contract_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claim B01-C009; artifact-contract handoff concept"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C004 through B04-C014; concepts extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Agent Handoff and Contract System

```yaml
summary_id: agent_handoff_and_contract_system
specialized_indexes:
  - handoff_contract_index
  - token_economy_and_information_design_index
pattern: >
  Agents exchange bounded work through explicit artifact contracts, not through
  assumed chat memory or direct agent-to-agent ownership transfer.
used_when:
  - "A task result must move from one role, skill, or verifier to another."
  - "A future session must reconstruct state without rereading the full conversation."
not_used_when:
  - "The receiving role needs live runtime access or mutation authority not granted by the handoff."
reads:
  - "current state"
  - "target state"
  - "source refs"
  - "input artifact refs"
  - "risk and validation thresholds"
writes:
  - "handoff packet"
  - "status delta or candidate output"
  - "stop condition if blocked"
token_efficiency:
  - "Use refs, not copies."
  - "Carry claim status and authority basis instead of replaying source prose."
drift_controls:
  - "Distinguish candidate output from accepted truth."
  - "Split executor ownership from validator/operator acceptance."
  - "Include stop conditions when evidence, risk, or authority is insufficient."
unresolved_or_deferred:
  - "Exact universal handoff packet schema remains a reusable contract target, not a runtime implementation in S6."
```

Apex Phase 2 should represent handoff as doctrine for information exchange, not as a direct runtime scheduler or agent bus.
