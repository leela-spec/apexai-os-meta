# Phase 1 Analysis — Subscription, Seat, Terminal, and Machine Models

## Run Metadata

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
phase: ingest_phase_1_analysis
batch: 04-subscription-seat-terminal-and-machine-models
status: new_parallel_compile
created_at: 2026-07-10T00:00:00Z
source_policy: source_preserving
```

## Source Scope

This batch captures environment and execution-surface implications visible in the source set: project/user/plugin scope, machine-local configuration, worktree/session behavior, and why semantic KB drafting should not be delegated to an external terminal agent by default.

## Source Files Read

```yaml
sources_read:
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
  - .claude/skills/apex-kb/SKILL.md
```

## Source-Grounded Claims

```yaml
claims:
  - id: P1-SEAT-001
    claim: "Claude Code skill scope may be enterprise, personal, project, or plugin-level; name conflicts resolve through that scope model."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SEAT-002
    claim: "The `.claude` directory contains committed project configuration and local overrides; settings.local.json is explicitly personal/local."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SEAT-003
    claim: "Subagents run within a single session and separate context, whereas background agents or agent teams cover parallel/multi-session behavior."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SEAT-004
    claim: "For Apex KB max-run semantic work, the current assistant/chat LLM remains the default owner; external terminal/Agent/Codex surfaces are deterministic execution surfaces by default."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
```

## Extracted Concepts

```yaml
concepts:
  - current-assistant-semantic-owner
  - deterministic-executor-only-boundary
  - persistent-agent-vs-ephemeral-subagent
```

## Extracted Entities

```yaml
entities:
  - claude-code
  - claude-code-subagents
  - apex-kb
```

## Contradictions / Tensions

```yaml
tensions:
  - id: T-SEAT-001
    tension: "Claude Code supports multiple execution/config scopes, but Apex KB pages should not imply that all local machine/session features are portable across users or subscription tiers."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
      - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
    handling: "Represent scope as a decision model, not a universal guarantee."
```

## Open Questions

```yaml
open_questions:
  - id: O-SEAT-001
    question: "Which Claude Code features in the raw source set depend on exact version, plan, org settings, or trusted workspace status?"
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
```

## Phase 2 Candidates

```yaml
phase2_candidates:
  summaries:
    - subscription-seat-terminal-machine-model.md
  concepts:
    - current-assistant-semantic-owner.md
    - deterministic-executor-only-boundary.md
  entities:
    - claude-code.md
```

## Source Gaps / Reopen Triggers

```yaml
source_gaps:
  - id: G-SEAT-001
    trigger: "Reopen with current official docs before making subscription, availability, or pricing claims."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
```
