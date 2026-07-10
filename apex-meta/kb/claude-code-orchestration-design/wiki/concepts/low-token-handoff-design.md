---
title: "Low-Token Handoff Design"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "low-token-handoff-design"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; refs replace full context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C002 and B01-C010; progressive disclosure"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C014; clean handoff and state frames"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "progressive-disclosure-for-agent-kbs"
  - "compact-activation-file"
related_entities: []
review_flags: []
---

# Low-Token Handoff Design

## Definition

Low-token handoff design is the practice of transferring work between skills, agents, or
sessions using compact, pointer-based packets — explicit state, source priority, artifact refs,
and next-action fields — instead of replaying full conversational history or raw evidence. It
draws on Apex's clean-handoff requirements (settled state, source priority, non-redo list, next
job, risks, success condition; B04-C009), the requirement for explicit state frames and atomic
task packets over chat-history reconstruction (B04-C011), and file-output/task-closure
contracts requiring fetch-back verification before success is claimed (B04-C014), combined with
the general progressive-disclosure principle that references should replace copies
(B01-C002, B01-C010).

## Operating Rules

```yaml
rules:
  - "A handoff packet should name settled state, source priority, non-redo list, exact next job, risks, and success condition explicitly rather than relying on chat memory (B04-C009)."
  - "High-risk execution should carry explicit state frames and atomic task packets instead of reconstructing context from history (B04-C011)."
  - "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed (B04-C014)."
  - "Prefer source_refs / artifact pointers over inline copies of evidence to keep handoff packets small (B01-C002, B01-C010)."
  - "Out-of-mode improvements should be captured explicitly in the handoff, not applied silently (B04-C009)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary source for the concrete handoff-packet fields (state, source authority, non-redo list, next job, risk, success condition) and the fetch-back closure requirement."
    coverage: "Claims B04-C009, B04-C011, B04-C013, B04-C014; concepts atomic-task-payload, fetch-back-validation, halt-clarify-routing-controls."
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Supplies the general refs-not-copies / progressive-disclosure principle a handoff packet inherits."
    coverage: "Claims B01-C002, B01-C010."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the handoff design goal directly as a specialized index (handoff_contract_index) and names 'how input refs replace full context' as a core question."
    coverage: "handoff_contract_index core questions, lines 70-85."
```

## Macro / Meso / Micro

### Macro

Across both the skill-package material and the Apex prompt/workflow material, the same
principle recurs: pass pointers and explicit status fields between stages, not full context
dumps. This keeps handoffs cheap in tokens while making the receiving side's obligations
unambiguous.

### Meso

Concretely, a handoff packet should include: current/target state, source authority (what
outranks what), an explicit non-redo list, the exact next job, named risks, and a success
condition (B04-C009); it should be expressed as an atomic task packet rather than reconstructed
from chat history (B04-C011); and closing it out requires fetch-back verification — reading the
written artifact back and confirming scope, content, and validation status — before success is
reported (B04-C014). The same refs-not-copies discipline that keeps skill packages small
(B01-C002, B01-C010) applies to what a handoff carries: pointers into artifacts and source_refs
rather than restated evidence.

### Micro

- B04-C009: clean handoffs include settled state, source priority, non-redo list, exact next
  job, risks, and success condition; out-of-mode improvements are captured, not silently applied.
- B04-C011: high-risk execution needs explicit state frames and atomic task packets rather than
  chat-history reconstruction.
- B04-C013: HALT and CLARIFY are routing controls that stop guessing, scope expansion, unsafe
  continuation, and silent failure — a handoff should surface these rather than absorb them silently.
- B04-C014: file-output and task-closure contracts require complete content, scope proof,
  target-root validation, fetch-back, and explicit validation status before success is claimed.
- B01-C002/B01-C010: progressive disclosure and concise-entrypoint principles generalize to
  "pointers over copies" in a handoff packet.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Clean handoffs should include settled state, source priority, a non-redo list, the exact next job, risks, and a success condition; out-of-mode improvements should be captured explicitly rather than applied silently."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C009"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C011"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Agent Skills rely on progressive disclosure (catalog, activated instructions, on-demand resources), which generalizes to preferring pointers/refs over inline copies in any handoff packet."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C002"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What is the smallest valid packet for handing work from one skill or agent to another?"
    leads_to: "claude-code-orchestration-design/summaries/token-efficient-information-design.md"
    rationale: "The summary page ties this concept's packet design into the KB-wide token-economy rule."
  - question: "How does an agent keep its own KB small while still handing off enough context?"
    leads_to: "claude-code-orchestration-design/concepts/progressive-disclosure-for-agent-kbs.md"
    rationale: "Shares the refs-not-copies mechanism this concept applies to handoffs specifically."
  - related_page: "claude-code-orchestration-design/concepts/compact-activation-file.md"
    relation: "Both concepts rely on the same concise-entrypoint / pointer-based design rule (B01-C010)."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C009"
    supports: "Required handoff fields for a clean handoff."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Explicit state frames and atomic task packets over chat-history reconstruction."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Fetch-back and task-closure validation requirement."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claims B01-C002, B01-C010"
    supports: "Refs-not-copies / progressive-disclosure principle underlying compact handoffs."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact packet size budget for a handoff has not yet been compiled; this page states the required fields but not a token ceiling."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 72-85 (handoff_contract_index: smallest_valid_handoff_packet)"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Whether HALT/CLARIFY/file-output/task-closure schemas should become reusable Apex-wide contracts or stay local to the prompt/workflow lane is an open question that affects how standardized handoff packets can be."
    source_pointer: "phase1-batch04-apex-application-patterns.md open question B04-Q003"
    proposed_handling: "ask_operator"
  - id: U003
    description: "Chat continuity is explicitly insufficient for high-risk work per the sources, which is a hard constraint this concept depends on; any workflow claiming completion from conversational memory alone should be treated as non-compliant."
    source_pointer: "phase1-batch04-apex-application-patterns.md contradiction B04-T002"
    proposed_handling: "leave_as_gap"
```
