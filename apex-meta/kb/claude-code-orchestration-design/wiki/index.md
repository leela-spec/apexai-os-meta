---
title: "Claude Code Orchestration Design Index"
page_type: index
kb_slug: "claude-code-orchestration-design"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "specialized indexes and S6 page plan"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-completion-report"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md"
    source_hash: "f604b3e31858da764eb2807084ca8282a1e4acc2"
    source_pointer: "Phase 1 completion state"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T12:18:37Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code Orchestration Design Index

<!-- BEGIN AUTO-GENERATED INDEX -->

```yaml
compiled_phase: "S6_ingest_phase_2_wiki_compile"
compiled_page_count: 62
summaries: 6
concepts: 45
entities: 11
next_step: "S7_deterministic_index_validation"
deterministic_script_needed_next: true
```

## Summaries

- [[summaries/minimal-claude-orchestration-architecture|Minimal Claude Orchestration Architecture]]
- [[summaries/agent-handoff-and-contract-system|Agent Handoff and Contract System]]
- [[summaries/project-execution-state-safety-model|Project Execution State Safety Model]]
- [[summaries/claude-mechanism-decision-model|Claude Mechanism Decision Model]]
- [[summaries/token-efficient-information-design|Token-Efficient Information Design]]
- [[summaries/weekly-routine-as-orchestration-case-study|Weekly Routine as Orchestration Case Study]]

## Specialized Concept Indexes

```yaml
agent_orchestration_index:
  - persistent-agent-vs-ephemeral-subagent
  - agent-specific-knowledge-base
  - compact-activation-seed
  - role-boundary-and-non-ownership
  - productive-agent-redundancy
  - validator-as-non-executor
  - agent-learning-queue-candidate-only
handoff_contract_index:
  - standard-handoff-packet
  - current-state-vs-target-state
  - candidate-is-not-accepted-truth
  - evd-imp-rsk-thresholds
  - handoff-stop-conditions
  - owner-validator-split
  - low-token-handoff-design
project_execution_index:
  - semantic-planning-layer
  - deterministic-read-side-report
  - gated-write-side-mutation
  - session-memory-and-next-context
  - dry-run-first-state-policy
  - operator-confirmed-mutation
  - state-delta-preservation
weekly_routine_case_index:
  - weekly-routine-workflow-case
  - weekly-plan-packet
  - next-day-plan
  - flow-packet
  - raw-flow-dump
  - flow-recap-packet
  - status-merge-packet
  - next-cycle-context
claude_mechanism_mapping_index:
  - mechanism-ladder
  - skill-boundary
  - workflow-boundary
  - ephemeral-subagent-boundary
  - persistent-agent-boundary
  - deterministic-script-boundary
  - hook-vs-skill-instruction
  - plugin-deferment-rule
token_economy_and_information_design_index:
  - yaml-first-artifact-design
  - refs-not-copies
  - compact-activation-file
  - progressive-disclosure-for-agent-kbs
  - compiled-kb-before-raw-source
  - packet-size-budget
  - file-state-over-chat-state
  - stop-condition-as-context-saver
```

## Entities

- [[entities/claude-code|Claude Code]]
- [[entities/agent-skills-standard|Agent Skills Standard]]
- [[entities/claude-code-skills|Claude Code Skills]]
- [[entities/claude-code-subagents|Claude Code Subagents]]
- [[entities/claude-code-hooks|Claude Code Hooks]]
- [[entities/claude-code-workflows|Claude Code Workflows]]
- [[entities/claude-code-plugins|Claude Code Plugins]]
- [[entities/mcp|Model Context Protocol]]
- [[entities/bmad-method|BMAD-METHOD]]
- [[entities/aider|Aider]]
- [[entities/swe-agent|SWE-agent]]

<!-- END AUTO-GENERATED INDEX -->

<!-- BEGIN LLM SUMMARY -->

Phase 2 compiled the Claude Code orchestration design KB around six specialized indexes: agent orchestration, handoff contracts, project execution safety, weekly routine case study, Claude mechanism mapping, and token-efficient information design.

The compiled doctrine is intentionally non-runtime: it defines patterns, boundaries, reads/writes, token-efficiency rules, drift controls, and unresolved questions without creating hooks, skills, workflows, plugins, MCP config, schedulers, production agents, raw-source edits, manifest edits, or deterministic indexes.

<!-- END LLM SUMMARY -->
