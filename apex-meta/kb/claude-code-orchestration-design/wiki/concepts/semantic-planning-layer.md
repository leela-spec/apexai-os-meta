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
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "deterministic-read-side-report"
  - "gated-write-side-mutation"
  - "standard-handoff-packet"
related_entities: []
review_flags:
  - "layer naming is a Phase 2 synthesis of the compile-plan's project_execution_index question, not a verbatim Phase 1 term"
---

# Semantic Planning Layer

## Definition

The semantic planning layer is the first of three layers used by this KB's `project_execution_index` to describe how project work moves through Apex orchestration: `semantic_planning_vs_deterministic_read_side_computation_vs_gated_write_side_mutation`. It is the stage where goals, operator intent, constraints, and source authority are interpreted into a plan candidate — before any deterministic computation runs and before any state mutation is proposed or committed. Batch 04 does not name this layer verbatim; it grounds the *behavior* the layer performs (naming target, source authority, non-goals, output contract, and stop condition before execution) in claims B04-C007, B04-C008, and B04-C017.

## Operating Rules

```yaml
rules:
  - "Semantic planning may propose a plan candidate, task frame, or open question set, but must not itself perform deterministic computation or write-side mutation."
  - "Planning must read operator intent, ranked source authority, and current state before producing an output (B04-C007)."
  - "Planning output must be bounded and stage-gated rather than a broad, open-ended autonomy grant (B04-C008)."
  - "Planning output must be handed off as an explicit artifact (task frame, plan candidate, open questions) rather than left implicit in conversation, consistent with B04-C017's rejection of relying on conversational continuity for high-risk work."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary source for the planning-before-execution and explicit-artifact claims this layer is built from (B04-C007, B04-C008, B04-C017)."
    coverage: "Direct claims about naming target/source/output-contract/stop-condition before execution, bounded stage-gated execution, and preserving Apex lifecycle safety through explicit artifacts."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Defines the three-layer project_execution_index framing that gives this concept its name and its boundary against deterministic computation and mutation."
    coverage: "project_execution_index core question naming the three-layer split and the questions about which components may propose vs compute vs write."
```

## Macro / Meso / Micro

### Macro

Apex project execution is organized into layers so that judgment-based interpretation of goals and constraints is kept separate from deterministic computation, which is kept separate again from confirmed state mutation. This separation prevents an interpretive step from silently becoming an unreviewed state change, and it is the framing the compile plan uses to organize the whole `project_execution_index`.

### Meso

B04-C007 requires that target, source authority, non-goals, output contract, and stop condition be named before execution begins — this is exactly the work of semantic planning. B04-C008 prefers bounded, stage-gated, artifact-centered execution over broad autonomy or giant multi-phase prompts, which means a planning output must be scoped tightly enough for a downstream deterministic or mutation stage to consume safely. B04-C017 recommends that Apex preserve lifecycle safety through explicit artifacts, state blocks, and gates rather than relying on conversational continuity — so a plan produced by this layer must be written down as a handoff artifact, not just reasoned about in a live turn.

### Micro

The specific three-layer vocabulary ("semantic planning layer" vs "deterministic read-side computation" vs "gated write-side mutation") comes from the compile plan's `project_execution_index` core question at lines 86-98, not from a named concept in Batch 04. This page maps that index question onto the closest matching Batch 04 claims (B04-C007, B04-C008, B04-C017), which describe planning-adjacent behavior without using the layer terminology itself.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Execution must name target, source authority, non-goals, output contract, and stop condition before it begins; verification follows execution before completion is reported."
    source_pointer: "B04-C007 (ESSENCE.md lines 34-45, 55-63; BEST_PRACTICES_v_old.md lines 53-72, 94-112)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Bounded, stage-gated, artifact-centered execution is preferred over broad autonomy or giant multi-phase prompts."
    source_pointer: "B04-C008 (BEST_PRACTICES_v_old.md lines 74-92)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Apex should preserve lifecycle safety through explicit artifacts, state blocks, gates, and HALT/CLARIFY signals rather than relying on conversational continuity."
    source_pointer: "B04-C017 (BEST_PRACTICES_v_old.md lines 190-230; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-221, continuation lines 1-94)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "The three-layer split (semantic planning / deterministic read-side computation / gated write-side mutation) used to name and scope this concept is a Phase 2 synthesis of the compile plan's index question, not a verbatim Batch 04 concept."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 86-98"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What layer interprets goals and constraints before any state changes happen?"
    leads_to: "claude-code-orchestration-design/concepts/deterministic-read-side-report.md"
    rationale: "Deterministic read-side computation is the next layer downstream of semantic planning in the project_execution_index model."
  - related_page: "claude-code-orchestration-design/concepts/gated-write-side-mutation.md"
    relation: "The third layer that semantic planning must not perform directly; planning may only propose, never mutate."
  - related_page: "claude-code-orchestration-design/concepts/standard-handoff-packet.md"
    relation: "The artifact type a semantic planning output is typically expressed as when handed to a downstream stage."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C007"
    supports: "Naming target/source authority/output contract/stop condition before execution is the substance of semantic planning."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C008"
    supports: "Bounded, stage-gated execution constrains what a planning output may authorize downstream."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C017"
    supports: "Planning outputs must be explicit artifacts, not conversational continuity."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 86-98"
    supports: "Defines the three-layer project_execution_index framing this concept is named after."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact three-layer name ('semantic planning layer') is a Phase 2 synthesis of the compile plan's index question, not a term used verbatim in Phase 1 Batch 04 claims."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 86-98"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Which concrete Apex component (skill, ephemeral subagent, or persistent agent) implements the semantic planning layer remains an open question."
    source_pointer: "B04-Q002"
    proposed_handling: "revisit_source"
```
