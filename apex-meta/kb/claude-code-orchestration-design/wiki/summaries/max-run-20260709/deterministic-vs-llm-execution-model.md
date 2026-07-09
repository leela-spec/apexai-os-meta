---
title: "Deterministic vs LLM Execution Model"
page_type: summary
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/06-deterministic-vs-llm-execution-model.md
---

# Deterministic vs LLM Execution Model

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/06-deterministic-vs-llm-execution-model.md
    rationale: "Run-specific boundary analysis."
    coverage: "Semantic versus deterministic ownership."
  - rank: 2
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Defines ownership policy."
    coverage: "LLM-owned and Python-owned duties."
```

## Macro / Meso / Micro

### Macro

LLMs synthesize; deterministic tools verify, index, apply patches, and preserve custody.

### Meso

The current assistant/chat LLM owns Phase 1 and Phase 2 semantics by default. External agents and Codex are deterministic executors unless the operator overrides semantic delegation.

### Micro

This max-run used GitHub connector writes, but still needs terminal postflight for index, retrieval, status, lint, and source-payload checks.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Semantic drafting and deterministic execution must remain separate by default."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/06-deterministic-vs-llm-execution-model.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "When should Agent/Codex be used versus current assistant LLM?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/deterministic-vs-llm-execution-model.md
    rationale: "Primary execution-boundary route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen if the operator explicitly delegates semantic drafting to another agent."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    proposed_handling: ask_operator
```
