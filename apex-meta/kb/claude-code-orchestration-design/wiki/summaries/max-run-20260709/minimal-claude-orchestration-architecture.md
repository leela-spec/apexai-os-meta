---
title: "Minimal Claude Orchestration Architecture"
page_type: summary
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: needs_review
created_at: "2026-07-09"
updated_at: "2026-07-11"
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: .claude/skills/apex-kb/SKILL.md
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
---

# Minimal Claude Orchestration Architecture

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Defines the Apex KB semantic/deterministic boundary and execution surface policy."
    coverage: "KB ownership, allowed writes, semantic compile, and non-mutation rules."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    rationale: "Defines skills as repeatable procedure packages with progressive disclosure."
    coverage: "Skill creation, scope, invocation, supporting files, and dynamic context injection."
  - rank: 3
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
    rationale: "Defines deterministic lifecycle enforcement points."
    coverage: "Hook events, matchers, decisions, and tool-call lifecycle."
  - rank: 4
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    rationale: "Defines context-isolated side-worker behavior."
    coverage: "Subagent context windows, permissions, models, and delegation triggers."
```

## Macro / Meso / Micro

### Macro

The minimal architecture is a ladder: current assistant/chat LLM for semantic synthesis, compiled KB pages for durable source-backed memory, skills for repeatable procedures, hooks/scripts for deterministic enforcement, subagents for bounded context isolation, plugins for distribution, and MCP only for external system connectivity.

### Meso

The default is not a swarm. Escalation is justified only when a lower-cost mechanism cannot preserve context, enforce a boundary, or connect to a required external surface.

### Micro

The run-specific policy is: current assistant/chat LLM owns Phase 1/2 semantic work; Agent Mode/Codex are deterministic executors by default; source-payload custody remains a postflight warning because the committed manifest content is empty.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A small mechanism ladder is safer than defaulting to agents, plugins, or MCP."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "Skills are the first escalation point for repeatable procedures that should not remain in CLAUDE.md."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Hooks enforce lifecycle events; subagents preserve context; MCP connects external tools."
    source_pointer: Claude Code hooks/subagents/MCP raw docs under kb_root/raw/
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What is the safest minimal Claude orchestration architecture?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/minimal-claude-orchestration-architecture.md
    rationale: "This page gives the high-level mechanism ladder."
  - related_page: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
    relation: "Decision model for choosing among mechanisms."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Do not convert this architecture into runtime hooks, plugins, agents, or MCP config without fresh raw-source checks and operator approval."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    proposed_handling: ask_operator
  - id: U002
    description: "Source-payload-manifest is empty in connector read, so query-ready closure needs terminal postflight."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
    proposed_handling: revisit_source
```
