# Phase 1 Analysis — Orchestration Workflows and Agent Boundaries

## Run Metadata

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
phase: ingest_phase_1_analysis
batch: 03-orchestration-workflows-and-agent-boundaries
status: new_parallel_compile
created_at: 2026-07-10T00:00:00Z
source_policy: source_preserving
```

## Source Scope

This batch covers orchestration workflow boundaries, agent delegation, small curated source selection, and when external agent frameworks should remain reference material instead of Apex runtime doctrine.

## Source Files Read

```yaml
sources_read:
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/SubskillsVsAgents_CC.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/repo-example-raw-githubusercontent-com-FlorianBruniaux-claude-code-ultimate-guide-main-guide-workflows-agent-teams.md.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/source-priority-candidates.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/process-flow-graph-summary.md
```

## Source-Grounded Claims

```yaml
claims:
  - id: P1-WORK-001
    claim: "Apex should prioritize Claude-native repos and official Claude docs over generic multi-agent frameworks when designing Claude Code orchestration."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-WORK-002
    claim: "Large plugin, skill, and agent libraries should be mined selectively rather than ingested wholesale because catalog size creates token noise and source sprawl."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
    confidence: medium
    claim_label: source_backed_summary
  - id: P1-WORK-003
    claim: "Subagent libraries can be useful as templates, but production agent rosters should stay small and explicit."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-WORK-004
    claim: "The process-flow graph records 10,931 deterministic edges across markdown links, process sequences, repo path references, wikilinks, and YAML path references."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/phase0/process-flow-graph-summary.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-WORK-005
    claim: "Phase 0 priority candidates identify Claude Code skills, hooks, plugins, MCP, and subagents docs as high-signal sources for this KB."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/phase0/source-priority-candidates.md
    confidence: high
    claim_label: source_backed_summary
```

## Extracted Concepts

```yaml
concepts:
  - minimal-claude-orchestration-architecture
  - production-agent-readiness-and-risk-model
  - deterministic-executor-only-boundary
  - old-output-comparison-policy
  - low-token-handoff-design
```

## Extracted Entities

```yaml
entities:
  - claude-code
  - apex-kb
  - claude-code-subagents
```

## Contradictions / Tensions

```yaml
tensions:
  - id: T-WORK-001
    tension: "External multi-agent frameworks provide vocabulary and examples, but their SDK/control-plane assumptions can distort Apex's file-native operating model."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
    handling: "Use external frameworks as comparison sources only unless an operator explicitly promotes a pattern."
```

## Open Questions

```yaml
open_questions:
  - id: O-WORK-001
    question: "Which candidate agent/team patterns should become persistent Apex runtime components rather than remain KB concepts?"
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
```

## Phase 2 Candidates

```yaml
phase2_candidates:
  summaries:
    - minimal-claude-orchestration-architecture.md
    - production-agent-readiness-and-risk-model.md
  concepts:
    - persistent-agent-vs-ephemeral-subagent.md
    - deterministic-executor-only-boundary.md
    - low-token-handoff-design.md
  entities:
    - claude-code-subagents.md
```

## Source Gaps / Reopen Triggers

```yaml
source_gaps:
  - id: G-WORK-001
    trigger: "Reopen raw repo sources before copying any `.claude/agents`, workflow, hook, or plugin file into runtime."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
```
