# Phase 1 Analysis — Claude Code Mechanisms and Surfaces

## Run Metadata

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
phase: ingest_phase_1_analysis
batch: 02-claude-code-mechanisms-and-surfaces
status: new_parallel_compile
created_at: 2026-07-10T00:00:00Z
source_policy: source_preserving
```

## Source Scope

This batch covers Claude Code skills, hooks, subagents, plugins, MCP, and the `.claude` directory as mechanism surfaces for orchestration design.

## Source Files Read

```yaml
sources_read:
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
```

## Source-Grounded Claims

```yaml
claims:
  - id: P1-MECH-001
    claim: "Skills are the preferred repeatable procedure unit when instructions would otherwise be repeatedly pasted or bloated inside CLAUDE.md."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-MECH-002
    claim: "Hooks are lifecycle-triggered commands, HTTP endpoints, LLM prompts, MCP tool calls, or agents that can automatically run at events such as UserPromptSubmit, PreToolUse, PostToolUse, SubagentStart, and Stop."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-MECH-003
    claim: "Subagents are context-isolated workers with their own prompts, tool access, permissions, and model selection; they are useful when exploration would flood the main context."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-MECH-004
    claim: "Plugins package multiple Claude Code components, including skills, agents, hooks, MCP servers, LSP servers, and monitors."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-MECH-005
    claim: "MCP connects Claude Code to external tools, databases, APIs, and event channels, and each server must be trusted because external-content access introduces prompt-injection risk."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-MECH-006
    claim: "The `.claude` directory is the project-level configuration surface for CLAUDE.md, settings, hooks, skills, commands, subagents, workflows, rules, and memory."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Extracted Concepts

```yaml
concepts:
  - skill-boundary
  - hook-vs-skill-instruction
  - mcp-allowlist-and-injection-risk
  - persistent-agent-vs-ephemeral-subagent
  - low-token-handoff-design
```

## Extracted Entities

```yaml
entities:
  - claude-code
  - claude-code-skills
  - claude-code-hooks
  - claude-code-plugins
  - claude-code-subagents
  - mcp
```

## Contradictions / Tensions

```yaml
tensions:
  - id: T-MECH-001
    tension: "Skills and commands have converged in Claude Code, but legacy command files may still exist."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
      - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
    handling: "Prefer skills for new workflows while preserving legacy command compatibility as migration context."
```

## Open Questions

```yaml
open_questions:
  - id: O-MECH-001
    question: "Which mechanism should become runtime configuration versus remain KB doctrine?"
    source: apex-meta/kb/claude-code-orchestration-design/wiki/index.md
```

## Phase 2 Candidates

```yaml
phase2_candidates:
  summaries:
    - claude-code-mechanism-decision-model.md
    - skill-hook-plugin-mcp-boundaries.md
  concepts:
    - skill-boundary.md
    - hook-vs-skill-instruction.md
    - mcp-allowlist-and-injection-risk.md
    - persistent-agent-vs-ephemeral-subagent.md
  entities:
    - claude-code.md
    - claude-code-skills.md
    - claude-code-hooks.md
    - claude-code-plugins.md
    - claude-code-subagents.md
    - mcp.md
```

## Source Gaps / Reopen Triggers

```yaml
source_gaps:
  - id: G-MECH-001
    trigger: "Reopen raw docs before writing actual plugin, hook, MCP, or subagent config, because this run compiles doctrine only."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md
```
