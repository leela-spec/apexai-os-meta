# Phase 1 Analysis — Deterministic vs LLM Execution Model

## Run Metadata

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
phase: ingest_phase_1_analysis
batch: 06-deterministic-vs-llm-execution-model
status: new_parallel_compile
created_at: 2026-07-10T00:00:00Z
source_policy: source_preserving
```

## Source Scope

This batch defines the boundary between semantic synthesis and deterministic execution for this KB run and for future Claude Code orchestration design.

## Source Files Read

```yaml
sources_read:
  - .claude/skills/apex-kb/SKILL.md
  - .claude/skills/apex-kb/references/kb-contract.md
  - .claude/skills/apex-kb/references/retrieval-contract.md
  - .claude/skills/apex-kb/examples/lifecycle-runbook.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/phase0-navigation-report.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/process-flow-graph-summary.md
```

## Source-Grounded Claims

```yaml
claims:
  - id: P1-EXEC-001
    claim: "Phase 0 must remain deterministic navigation only and must not create semantic analysis, wiki pages, embeddings, vector stores, or Apex Plan/Sync/Session/PreCap/FlowRecap/APSU state."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/phase0/phase0-navigation-report.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-EXEC-002
    claim: "The current assistant/chat LLM is the default semantic execution surface for Phase 1 analysis and Phase 2 wiki drafting."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-EXEC-003
    claim: "Agent Mode and Codex are reserved by default for live worktree script execution, Git-native patch application, deterministic validation, and commit/push operations."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-EXEC-004
    claim: "Derived retrieval indexes are rebuildable and never canonical; stale retrieval must be rebuilt or explicitly marked bounded."
    source: .claude/skills/apex-kb/references/retrieval-contract.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-EXEC-005
    claim: "The graph/process-flow artifact is deterministic routing support, not semantic interpretation."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/phase0/process-flow-graph-summary.md
    confidence: high
    claim_label: source_backed_summary
```

## Extracted Concepts

```yaml
concepts:
  - deterministic-executor-only-boundary
  - current-assistant-semantic-owner
  - source-preserving-kb-compile
  - low-token-handoff-design
```

## Extracted Entities

```yaml
entities:
  - apex-kb
  - claude-code
```

## Contradictions / Tensions

```yaml
tensions:
  - id: T-EXEC-001
    tension: "GitHub connector commits are deterministic repository writes, but they do not replace terminal postflight commands or retrieval rebuilds."
    sources:
      - .claude/skills/apex-kb/examples/lifecycle-runbook.md
      - .claude/skills/apex-kb/references/retrieval-contract.md
    handling: "Mark needs_terminal_postflight true in final report."
```

## Open Questions

```yaml
open_questions:
  - id: O-EXEC-001
    question: "Should future max-run semantic compiles use GitHub connector writes, local Agent Mode writes, or a hybrid?"
    source: .claude/skills/apex-kb/SKILL.md
```

## Phase 2 Candidates

```yaml
phase2_candidates:
  summaries:
    - deterministic-vs-llm-execution-model.md
  concepts:
    - deterministic-executor-only-boundary.md
    - current-assistant-semantic-owner.md
    - low-token-handoff-design.md
```

## Source Gaps / Reopen Triggers

```yaml
source_gaps:
  - id: G-EXEC-001
    trigger: "Reopen if future operator explicitly delegates semantic drafting to Agent Mode or Codex."
    source: .claude/skills/apex-kb/SKILL.md
```
