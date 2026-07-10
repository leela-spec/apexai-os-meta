---
title: "Owner Validator Split"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "owner-validator-split"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; validator or operator review required"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C006 through B03-C007; validation split"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C004 through B04-C017; operator gates and closure proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "validator-as-non-executor"
  - "role-boundary-and-non-ownership"
  - "gated-write-side-mutation"
related_entities:
  - "bmad-method"
review_flags: []
---

# Owner Validator Split

## Definition

The role that produces or owns an artifact is kept separate from the role that validates its acceptance. This concept is a synthesis, not a single literal claim: it combines BMAD's deterministic-then-inference validation pattern (B03-C006, B03-C007 — mechanical checks run first, LLM/inference judgment is reserved only for what remains ambiguous after the deterministic pass) with Apex's own primary-source doctrine on artifact-contract handoff (B04-C004), operator gates (B04-C005), and verification-before-completion discipline (B04-C011, B04-C017). Naming this combination an "owner/validator split" goes beyond the literal text of any single source, so the generalized framing itself is treated as a `working_hypothesis` even though its component claims are individually source-backed.

## Operating Rules

```yaml
rules:
  - "The role that owns production is separate from the role that validates acceptance."
  - "Used when an artifact may be correct structurally but risky semantically or operationally."
  - "Not used when the operation is read-only and has no downstream commitment."
  - "The validator reads owner output, acceptance criteria, and source_refs; it does not re-derive the whole source corpus."
  - "The validator writes a verdict (accepted, needs_review, or blocked), not new production content."
  - "The producer cannot self-promote high-impact work without review (B04-C005 operator gate discipline)."
  - "Exact validator roles remain deferred beyond the current compile cycle."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary-authority Apex doctrine on artifact contracts, operator gates, and verification discipline; ranked highest because it is the direct source of the owner/production side of the split and of the gating mechanism."
    coverage: "B04-C004 (artifact contract handoff), B04-C005 (operator gates), B04-C011 (state discipline), B04-C013 through B04-C017 (HALT/CLARIFY, file-output and task-closure proof)."
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Secondary/comparative source that supplies the concrete two-pass validation mechanic this concept borrows; ranked second because it is explicitly non-authoritative external-repo material (BMAD)."
    coverage: "B03-C006 (deterministic-first, inference-second validation), B03-C007 (encapsulation checks as part of the deterministic pass)."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Internal Phase 2 planning note that first proposed treating validator/operator review as a distinct routing surface; used for continuity with the compile plan rather than as new evidentiary content."
    coverage: "Lines 72-85 on validator-or-operator review as a required step before downstream use."
```

## Macro / Meso / Micro

### Macro

Apex orchestration design separates whoever produces an artifact from whoever certifies it as ready for downstream use. This is a general pattern reinforced from two directions: comparative external-repo evidence (BMAD's validator) showing that mechanical checks and judgment checks are different kinds of work best done in different passes, and Apex's own primary doctrine that requires operator gates and verification proof rather than trusting an actor's self-report of completion.

### Meso

BMAD's `skill-validator.md` (B03-C006) runs deterministic checks first, skips whatever already passed mechanically, and reserves LLM/inference judgment only for semantic or ambiguous rules (B03-C007 covers the encapsulation checks that are part of that deterministic pass). Apex's own application patterns generalize this into a role-level rule rather than a single validator script: B04-C004 establishes that skills hand off through artifacts rather than direct calls, B04-C005 makes operator approval a first-class gate before downstream use, and B04-C011/B04-C017 require explicit state frames, atomic task packets, and fetch-back/closure proof instead of trusting conversational continuity. Read together, these sources support an owner (producer) / validator (reviewer) split where the validator's authority is bounded to review, not production.

### Micro

- B03-C006: "BMAD's validation pattern uses deterministic checks first and inference validation second, skipping rules that passed deterministically and reserving LLM judgment for semantic or ambiguous rules." (`skill-validator.md` lines 3-28)
- B04-C004: "Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical/logical slot and downstream skills read that artifact." (`Apex_Alfred_Skill_Definition_Guide.md` lines 94-107)
- B04-C005: "Operator gates are a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required." (`Apex_Alfred_Skill_Definition_Guide.md` lines 108-120)

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C006
    claim: "BMAD's validation pattern uses deterministic checks first and inference validation second, skipping rules that passed deterministically and reserving LLM judgment for semantic or ambiguous rules."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; skill-validator.md lines 3-28"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B04-C004
    claim: "Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical/logical slot and downstream skills read that artifact."
    source_pointer: "phase1-batch04-apex-application-patterns.md; Apex_Alfred_Skill_Definition_Guide.md lines 94-107"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: B04-C005
    claim: "Operator gates are a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required."
    source_pointer: "phase1-batch04-apex-application-patterns.md; Apex_Alfred_Skill_Definition_Guide.md lines 108-120"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "OVS-WH001"
    claim: "The 'owner/validator split' is a generalization, beyond any single literal source claim, that reframes BMAD's deterministic-then-inference two-pass validation as an Apex role-level separation between the artifact producer and the artifact reviewer, with reviewer authority bounded by operator gating rather than producer self-certification."
    source_pointer: "synthesis of B03-C006, B03-C007, B04-C004, B04-C005, B04-C011, B04-C017"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Should the same role that produces a KB artifact also be allowed to mark it accepted?"
    leads_to: "claude-code-orchestration-design/concepts/validator-as-non-executor.md"
    rationale: "Validator-as-non-executor narrows this split to the constraint that validation must not become execution authority."
  - related_page: "claude-code-orchestration-design/concepts/role-boundary-and-non-ownership.md"
    relation: "Both pages describe boundaries between roles; role-boundary-and-non-ownership generalizes the non-ownership rule this concept applies specifically to validation."
  - related_page: "claude-code-orchestration-design/concepts/gated-write-side-mutation.md"
    relation: "Owner/validator split is one reason write-side mutation stays gated: the owner cannot unilaterally promote its own output to accepted state."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "skill-validator.md lines 3-28 (B03-C006)"
    supports: "Deterministic-then-inference two-pass validation mechanic"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "Apex_Alfred_Skill_Definition_Guide.md lines 94-120 (B04-C004, B04-C005)"
    supports: "Artifact-contract handoff and operator-gate discipline that generalize the split to Apex roles"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "BEST_PRACTICES_v_old.md lines 190-230; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-221 (B04-C011, B04-C017)"
    supports: "Verification-before-completion discipline that motivates a non-self-certifying validator role"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "BMAD's validator has BMAD-specific naming rules (e.g. bmad- prefix) that should not be imported into Apex without an explicit Apex prefix policy decision."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-T002, skill-validator.md lines 69-83"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Which BMAD validator rules generalize to Apex skill packages without importing BMAD-specific assumptions remains an open question."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "Exact validator roles (who validates what, and with what authority) are deferred beyond the current compile cycle; this page names the pattern, not a finalized role roster."
    source_pointer: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md lines 72-85"
    proposed_handling: "revisit_source"
```
