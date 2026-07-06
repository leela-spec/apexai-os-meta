---
title: "Executor Routing and Lifecycle State Lock"
page_type: concept
kb_slug: "llm-wiki-project-repos"
concept_slug: "executor-routing-and-lifecycle-state-lock"
created_at: "2026-07-06"
status: "active"
confidence: "high"
claim_label: "source_backed_summary"
---

# Executor Routing and Lifecycle State Lock

## Definition

Lifecycle state lock is the rule that an Apex KB assistant must preserve the latest known lifecycle phase and advance from it, rather than reopening earlier phases or emitting partial artifacts. Executor routing selects exactly one owner for the next action: Codex, deterministic tool, LLM, or human operator.

## Failure Pattern

```yaml
failure:
  canonical_summary: "Apex KB was treated as local prompt tasks instead of one stateful lifecycle."
  symptoms:
    - "partial Codex packets"
    - "options offered when a single next step was required"
    - "deterministic validation loops after PASS"
    - "phase rewind to earlier decisions"
    - "executor boundaries blurred"
```

## Corrected Protocol

```yaml
protocol:
  before_next_artifact:
    state_lock:
      - kb_root
      - latest_commit_or_source_state
      - completed_phase_or_gate
      - hard_failures
      - next_lifecycle_phase
    executor_select_one:
      - CODEX
      - DETERMINISTIC_TOOL
      - LLM
      - HUMAN_OPERATOR
    artifact_select_one:
      - codex_patch_prompt
      - deterministic_execution_report
      - llm_semantic_compile
      - operator_approval_packet
      - final_status_report
  rule: "one chunk equals one usable artifact"
```

## Patch Ideas

```yaml
patches:
  - id: ER-001
    title: "State-lock header for Apex KB handovers"
    target: "handover templates and runbooks"
    priority: P0
    acceptance: "Every handover states lifecycle_position, executor, output_path, and stop_condition."
  - id: ER-002
    title: "No-option-sprawl rule"
    target: "assistant/Codex prompt conventions"
    priority: P1
    acceptance: "When the next lifecycle step is defined, the prompt emits one executable artifact, not alternatives."
  - id: ER-003
    title: "No deterministic loop after PASS"
    target: "Apex KB process guidance"
    priority: P1
    acceptance: "After deterministic PASS/PASS_WITH_WARNINGS, route to semantic compile or next declared phase unless a hard failure exists."
```

## Routes Here

Read before producing any Codex prompt, deterministic validation handoff, semantic compile handoff, or final status report for Apex KB.
