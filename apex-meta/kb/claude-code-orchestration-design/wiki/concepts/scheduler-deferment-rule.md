---
title: "Scheduler Deferment Rule"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "scheduler-deferment-rule"
source_refs:
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "avoid_in_phase2: runtime implementation work deferred"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "compile objective: abstract source-grounded orchestration knowledge"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "scheduler-boundary"
  - "compiled-kb-before-raw-source"
related_entities:
  - "scheduler"
review_flags:
  - "the general deferment doctrine is explicit and high-confidence; its specific application to 'scheduler' is an extension since no dedicated scheduler source exists"
---

# Scheduler Deferment Rule

## Definition

The operator decision log states, at general policy level, that Phase 2 must avoid "turning deferred implementation work into current doctrine" and must not pretend the operational orchestration system has been built (`operator-phase1-review-decisions-20260702.md`, `phase2_implications.avoid_in_phase2`). That general rule is explicit and directly sourced (high confidence). Applying it specifically to scheduling is an interpretive extension: no batch file gives scheduler mechanics enough depth to compile as doctrine, so the correct Phase 2 treatment is to keep scheduler design deferred until workflow shape, state contract, gate model, and failure model are explicit for whatever scheduler proposal eventually arrives.

## Operating Rules

```yaml
rules:
  - "Scheduler design stays deferred until workflow shape, state contract, gate model, and failure model are explicit."
  - "Used when a recurring trigger is proposed for an Apex process."
  - "Not used when the proposal is only a semantic KB topic package (no runtime commitment implied)."
  - "Reads: workflow readiness, state authority, operator gate requirement, failure handling."
  - "Writes: defer_scheduler recommendation and a required_preconditions list — never a scheduler implementation."
  - "Recurring trigger behavior is not treated as current system behavior until validated outside this compile cycle."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Primary, explicit operator policy: names the general rule this concept applies (avoid turning deferred implementation work into current doctrine, avoid pretending the operational system is built)."
    coverage: "Section 3 phase2_implications.avoid_in_phase2 and phase2_implications.write_as_boundary_or_open_question."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Internal compile-scope statement clarifying that the objective is to abstract source-grounded knowledge, not to build runtime systems; used for continuity, not as new scheduler evidence."
    coverage: "Compile objective statement distinguishing KB indexing/compilation from orchestration-system build."
```

## Macro / Meso / Micro

### Macro

Apex's operator review explicitly separates "compiling the KB" from "building the operational orchestration system," and explicitly lists turning deferred implementation work into current doctrine as something Phase 2 must avoid. Scheduling is a clean example of implementation work that has not been evidenced deeply enough in Phase 1 to become doctrine, so the deferment rule applies to it by direct extension of that general policy.

### Meso

The operator decision log's `phase2_implications` section names two relevant buckets: `write_as_doctrine` (things confirmed enough to state as current Apex design) and `write_as_boundary_or_open_question` (things left as boundaries or open questions, including MCP policy and the tree-sitter/LSP repo-map extension). Scheduling is not explicitly listed in either bucket in the source text — it is absent, not merely deferred by name — which is itself informative: it means Phase 1 did not surface scheduling as a decision point at all. The safest and most honest Phase 2 treatment is to apply the same "avoid turning deferred work into doctrine" logic that the operator applied to items it did name, rather than to silently invent scheduler doctrine that was never reviewed.

### Micro

- Operator decision log, `phase2_implications.avoid_in_phase2`: "pretending the operational orchestration system has been built"; "turning deferred implementation work into current doctrine." (`operator-phase1-review-decisions-20260702.md` lines 139-143)
- Operator decision log, `kb_indexing_and_compilation` vs `orchestration_system_build` distinction. (lines 33-40)
- Q006 (`tree_sitter_lsp_repo_maps`, decision: `defer_phase0_v1_5_code_repo_map_extension`) is the one runtime-adjacent item the operator explicitly deferred by name — it concerns code repo maps, not scheduling, but its deferment pattern (name the trigger conditions for revisiting later) is the template this page reuses. (lines 91-97)

## Key Claims

```yaml
key_claims:
  - claim_id: "OPD-C001"
    claim: "Phase 2 must avoid turning deferred implementation work into current doctrine and must not present the operational orchestration system as already built."
    source_pointer: "operator-phase1-review-decisions-20260702.md; phase2_implications.avoid_in_phase2, lines 139-143"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "OPD-C002"
    claim: "KB indexing/compilation is explicitly distinguished from building the operational Apex orchestration system; the latter is later work that uses the compiled KB as source-grounded input."
    source_pointer: "operator-phase1-review-decisions-20260702.md; kb_indexing_and_compilation / orchestration_system_build, lines 33-40"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "SDR-WH001"
    claim: "Scheduling specifically should follow the same deferment treatment the operator applied to named items like the tree-sitter/LSP repo-map extension, even though scheduling itself was never named as a decision point in Phase 1."
    source_pointer: "extension of operator-phase1-review-decisions-20260702.md Q006 pattern; no direct scheduler-specific source"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Why doesn't this KB compile a scheduler implementation even though scheduling was mentioned in a source?"
    leads_to: "claude-code-orchestration-design/concepts/scheduler-boundary.md"
    rationale: "Scheduler-boundary states what a future scheduler must not be allowed to do; this page states why its design is deferred at all."
  - related_page: "claude-code-orchestration-design/summaries/scheduler-boundary-and-deferment.md"
    relation: "That summary page compiles this deferment rule together with the scheduler-boundary concept into one topic-level view."
```

## Evidence

```yaml
evidence:
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "phase2_implications.avoid_in_phase2 (lines 139-143)"
    supports: "General deferment doctrine this concept applies"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q006_tree_sitter_lsp_repo_maps (lines 91-97)"
    supports: "Template pattern for naming defer-trigger conditions, reused here by extension for scheduling"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "compile objective statement"
    supports: "Continuity framing that compilation is not system-build"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Scheduling was never named as an explicit operator decision point (unlike MCP policy or tree-sitter/LSP repo maps); this page's application of the deferment rule to scheduling is an extension, not a literal operator statement."
    source_pointer: "operator-phase1-review-decisions-20260702.md; absence in Section 2 operator_decisions"
    proposed_handling: "ask_operator"
  - id: U002
    description: "No source defines scheduler implementation surface, audit log shape, or recovery semantics; these remain unresolved per the original page's own unresolved_or_deferred list."
    source_pointer: "n/a — absence noted across phase1-batch03 and phase1-batch04"
    proposed_handling: "planning_task_candidate"
```
