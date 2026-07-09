---
title: "Current Assistant Semantic Owner"
page_type: concept
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: .claude/skills/apex-kb/SKILL.md
---

# Current Assistant Semantic Owner

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Primary source for the execution surface policy."
    coverage: "Current assistant/chat LLM ownership of semantic compile."
```

## Macro / Meso / Micro

### Macro

The current assistant/chat LLM is the default surface for semantic Apex KB work.

### Meso

It owns Phase 1 semantic analysis, Phase 2 wiki drafting, synthesis, concept/entity extraction, contradiction handling, and query answer synthesis when it can perform the work directly.

### Micro

This max-run preserved that rule by writing semantic pages directly through the GitHub connector rather than asking Codex or a terminal agent to draft them.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "default_semantic_execution_surface is current_assistant_chat_llm."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Who owns Apex KB Phase 1 and Phase 2 semantic work?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/current-assistant-semantic-owner.md
    rationale: "Core semantic ownership rule."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "If a future operator delegates semantic drafting externally, create a new decision record."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    proposed_handling: ask_operator
```
