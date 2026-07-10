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
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "apex-artifact-contract-handoff"
  - "operator-gated-orchestration"
  - "standard-handoff-packet"
  - "handoff-stop-conditions"
related_entities: []
review_flags: []
---

# Agent Handoff and Contract System

## Core Summary

Apex agents and skills exchange work through explicit artifact contracts
rather than direct calls or assumed chat continuity. Claim B01-C009
(`phase1-batch01-skill-package-contracts.md`) establishes this at the
skill-package level: "Apex's operator-supplied skill guide maps the
orchestration loop into discrete skills connected by artifact contracts, not
direct calls" (`Apex_Alfred_Skill_Definition_Guide.md` lines 5-18, 94-107).
Claim B04-C004 (`phase1-batch04-apex-application-patterns.md`) confirms and
sharpens this at the Apex application-pattern level: skills are connected by
artifact contracts rather than direct calls — one skill writes an artifact to
a canonical/logical slot and downstream skills read that artifact (lines
94-107).

That writer/reader pairing is not the whole contract, though. B04-C005 adds
operator gates as a first-class design rule: skills must pause for explicit
approval before downstream use when validation is required (lines 108-120).
B04-C009 requires clean handoffs to carry settled state, source priority, a
non-redo list, the exact next job, risks, and a success condition
(`BEST_PRACTICES_v_old.md` lines 114-149). B04-C011 and B04-C017 require
explicit state frames and atomic task packets rather than reliance on
conversational memory (`BEST_PRACTICES_v_old.md` lines 190-230). B04-C013
adds HALT/CLARIFY as routing controls against guessing, scope expansion, and
silent failure (execution-control-contracts continuation lines 1-51). B04-C014
requires file-output and task-closure contracts — complete content, scope
proof, target-root validation, fetch-back, and explicit validation status —
before a handoff can be treated as closed (execution-control-contracts
continuation lines 52-94, 125-153). Together, the artifact-writer/reader
pairing (B01-C009, B04-C004) plus the gate/state/closure discipline
(B04-C005, B04-C009, B04-C011, B04-C013, B04-C014) form one system-level
handoff pattern, not two separate ideas.

## What This Adds

```yaml
adds:
  - "Combines B01's skill-package-level artifact-contract-handoff concept with B04's Apex-application-pattern instantiation of it (writer/reader skill pairing, operator gate, state/closure discipline)."
  - "Positions operator gates and HALT/CLARIFY/fetch-back controls as required parts of a valid handoff, not optional extras layered on top of an artifact reference."
clarifies:
  - "'Contract' in this KB means an artifact schema plus a gate plus state/closure discipline together — not an API/RPC-style direct call between skills."
limits:
  - "Does not specify one universal handoff-packet schema; that remains a reusable-contract target per B01-Q003 and B04-Q003 (see Uncertainty)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Most direct instantiation of the pattern in Apex-specific terms — supplies the writer/reader artifact rule, the operator-gate rule, and the state/closure controls."
    coverage: "Claims B04-C004, B04-C005, B04-C009, B04-C011, B04-C013, B04-C014, B04-C017; concepts apex-artifact-contract-handoff, operator-gated-orchestration, atomic-task-payload, halt-clarify-routing-controls, fetch-back-validation."
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Origin of the artifact-contract-handoff concept at the portable skill-package level, prior to Apex-specific elaboration."
    coverage: "Claim B01-C009; concept artifact-contract-handoff; open question B01-Q003."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the abstract need this pattern answers via the handoff_contract_index question set."
    coverage: "handoff_contract_index core questions: smallest valid handoff packet, required fields, authority-basis visibility, mandatory stop conditions."
```

## Macro / Meso / Micro

### Macro

The compile plan treats "how agents exchange work with minimal context cost"
as a cross-cutting design axis independent of any single Claude Code
mechanism (compile plan section 3). Its `handoff_contract_index` (lines
70-83) asks for a smallest valid handoff packet, required fields, authority
basis visibility, and mandatory stop conditions. B01 and B04 together supply
the concrete Apex-grounded answer: artifact-contract handoffs gated by
explicit operator approval and closed only after state/proof discipline is
satisfied.

### Meso

The pattern decomposes into four linked moves. First, a skill writes an
artifact to a canonical or logical slot instead of calling the next skill
directly (B01-C009, B04-C004). Second, some transitions require an operator
gate — the downstream skill or agent must not consume the artifact until
explicit approval is given (B04-C005). Third, the handoff is made auditable
and safe through explicit state frames, atomic task packets, and HALT/CLARIFY
controls, so its validity does not depend on the requesting agent's
conversational memory (B04-C009, B04-C011, B04-C013, B04-C017). Fourth, a
handoff is not complete until file-output and task-closure contracts —
including fetch-back proof — are satisfied (B04-C014).

### Micro

- B01-C009: `Apex_Alfred_Skill_Definition_Guide.md` lines 5-18, 94-107 —
  orchestration loop mapped into discrete skills connected by artifact
  contracts, not direct calls.
- B04-C004: `Apex_Alfred_Skill_Definition_Guide.md` lines 94-107 — writer
  skill writes to a canonical/logical slot; downstream skill reads it.
- B04-C005: lines 108-120 — operator gates as a first-class design rule.
- B04-C009: `BEST_PRACTICES_v_old.md` lines 114-149 — clean-handoff field
  list (settled state, source priority, non-redo list, next job, risks,
  success condition).
- B04-C011 / B04-C017: `BEST_PRACTICES_v_old.md` lines 190-230 — explicit
  state frames and atomic task packets instead of chat-history
  reconstruction.
- B04-C013: execution-control-contracts continuation lines 1-51 — HALT and
  CLARIFY as routing controls.
- B04-C014: execution-control-contracts continuation lines 52-94, 125-153 —
  file-output and task-closure contracts with fetch-back.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: >
      Apex's operator-supplied skill guide maps the orchestration loop into
      discrete skills connected by artifact contracts, not direct calls.
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C009"
    confidence: medium
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C002
    claim: >
      Apex skills are connected by artifact contracts rather than direct
      calls: one skill writes an artifact to a canonical/logical slot and
      downstream skills read that artifact.
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C004"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C003
    claim: >
      Operator gates are a first-class Apex design rule: skills must pause
      for explicit approval before downstream use when validation is
      required.
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C005"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C004
    claim: >
      A handoff is only valid when it carries an artifact reference, a gate
      status, and closure/fetch-back proof together — the artifact-writer
      pairing alone is not sufficient without the gate and closure discipline.
    source_pointer: "synthesis of B01-C009, B04-C004, B04-C005, and B04-C014"
    confidence: medium
    claim_label: working_hypothesis
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "How do two Apex skills exchange an artifact without a direct call?"
    leads_to: "claude-code-orchestration-design/wiki/concepts/standard-handoff-packet.md"
    rationale: "The standard-handoff-packet concept is the natural next stop after this system-level synthesis."
  - related_page: "claude-code-orchestration-design/wiki/concepts/handoff-stop-conditions.md"
    relation: "The operator-gate and HALT/CLARIFY controls referenced in this summary are detailed further in that concept page."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      Should Apex treat artifact-contract handoffs as mandatory for all
      orchestration skills, including lightweight prompt/reference skills, or
      only for state-bearing ones?
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q003"
    proposed_handling: ask_operator
  - id: U002
    description: >
      Whether HALT/CLARIFY/file-output/task-closure schemas become reusable
      Apex-wide contracts or stay local to prompt/workflow execution lanes was
      an open question in Phase 1; the operator review (Q008) has since
      validated an Apex-wide minimal core with local extensions, so this
      should be treated as resolved-but-not-yet-implemented rather than fully
      open.
    source_pointer: "phase1-batch04-apex-application-patterns.md open question B04-Q003; operator-phase1-review-decisions-20260702.md Q008"
    proposed_handling: planning_task_candidate
  - id: U003
    description: >
      Rich execution contracts must not bloat activation files, yet the
      handoff system above depends on carrying several required fields; the
      exact split between what lives in a compact skill file versus a
      referenced contract/appendix is not finalized.
    source_pointer: "phase1-batch04-apex-application-patterns.md tension B04-T001"
    proposed_handling: revisit_source
```
