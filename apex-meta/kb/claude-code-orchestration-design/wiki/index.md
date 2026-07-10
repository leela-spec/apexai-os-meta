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

Generated: `2026-07-10T19:31:53Z`

Compiled page count: `98`

## Concept Pages

- [Agent Learning Queue Candidate Only](concepts/agent-learning-queue-candidate-only.md) - `needs_review` / `medium`
- [Agent-Specific Knowledge Base](concepts/agent-specific-knowledge-base.md) - `active` / `medium`
- [Candidate Is Not Accepted Truth](concepts/candidate-is-not-accepted-truth.md) - `active` / `high`
- [Compact Activation File](concepts/compact-activation-file.md) - `active` / `high`
- [Compact Activation Seed](concepts/compact-activation-seed.md) - `active` / `high`
- [Compiled KB Before Raw Source](concepts/compiled-kb-before-raw-source.md) - `active` / `high`
- [Current State vs Target State](concepts/current-state-vs-target-state.md) - `active` / `high`
- [Deterministic Read-Side Report](concepts/deterministic-read-side-report.md) - `active` / `high`
- [Deterministic Script Boundary](concepts/deterministic-script-boundary.md) - `active` / `high`
- [Dry-Run First State Policy](concepts/dry-run-first-state-policy.md) - `active` / `medium`
- [Ephemeral Subagent Boundary](concepts/ephemeral-subagent-boundary.md) - `active` / `high`
- [EVD IMP RSK Thresholds](concepts/evd-imp-rsk-thresholds.md) - `needs_review` / `medium`
- [File State over Chat State](concepts/file-state-over-chat-state.md) - `active` / `high`
- [Flow Packet](concepts/flow-packet.md) - `active` / `medium`
- [Flow Recap Packet](concepts/flow-recap-packet.md) - `active` / `medium`
- [Gated Write-Side Mutation](concepts/gated-write-side-mutation.md) - `active` / `high`
- [Handoff Stop Conditions](concepts/handoff-stop-conditions.md) - `active` / `high`
- [Hook vs Skill Instruction](concepts/hook-vs-skill-instruction.md) - `active` / `high`
- [Low-Token Handoff Design](concepts/low-token-handoff-design.md) - `active` / `high`
- [Current Assistant Semantic Owner](concepts/max-run-20260709/current-assistant-semantic-owner.md) - `new_parallel_compile` / `high`
- [Deterministic Executor Only Boundary](concepts/max-run-20260709/deterministic-executor-only-boundary.md) - `new_parallel_compile` / `high`
- [Hook vs Skill Instruction](concepts/max-run-20260709/hook-vs-skill-instruction.md) - `new_parallel_compile` / `high`
- [Low-Token Handoff Design](concepts/max-run-20260709/low-token-handoff-design.md) - `new_parallel_compile` / `high`
- [MCP Allowlist and Injection Risk](concepts/max-run-20260709/mcp-allowlist-and-injection-risk.md) - `new_parallel_compile` / `high`
- [Old Output Comparison Policy](concepts/max-run-20260709/old-output-comparison-policy.md) - `new_parallel_compile` / `high`
- [Persistent Agent vs Ephemeral Subagent](concepts/max-run-20260709/persistent-agent-vs-ephemeral-subagent.md) - `new_parallel_compile` / `high`
- [Phase 2 Value Contract](concepts/max-run-20260709/phase2-value-contract.md) - `new_parallel_compile` / `high`
- [Skill Boundary](concepts/max-run-20260709/skill-boundary.md) - `new_parallel_compile` / `high`
- [Source-Preserving KB Compile](concepts/max-run-20260709/source-preserving-kb-compile.md) - `new_parallel_compile` / `high`
- [MCP Allowlist and Injection Risk](concepts/mcp-allowlist-and-injection-risk.md) - `needs_review` / `high`
- [MCP Config Boundary](concepts/mcp-config-boundary.md) - `active` / `high`
- [MCP Decision Model](concepts/mcp-decision-model.md) - `active` / `high`
- [Mechanism Ladder](concepts/mechanism-ladder.md) - `active` / `high`
- [Next-Cycle Context](concepts/next-cycle-context.md) - `active` / `medium`
- [Next-Day Plan](concepts/next-day-plan.md) - `active` / `medium`
- [Operator-Confirmed Mutation](concepts/operator-confirmed-mutation.md) - `active` / `high`
- [Owner Validator Split](concepts/owner-validator-split.md) - `active` / `high`
- [Packet Size Budget](concepts/packet-size-budget.md) - `active` / `medium`
- [Persistent Agent Boundary](concepts/persistent-agent-boundary.md) - `active` / `medium`
- [Persistent Agent vs Ephemeral Subagent](concepts/persistent-agent-vs-ephemeral-subagent.md) - `active` / `high`
- [Plugin Deferment Rule](concepts/plugin-deferment-rule.md) - `active` / `high`
- [Production Agent Readiness Gate](concepts/production-agent-readiness-gate.md) - `needs_review` / `medium`
- [Production Agent Roster Candidate Boundary](concepts/production-agent-roster-candidate-boundary.md) - `needs_review` / `medium`
- [Productive Agent Redundancy](concepts/productive-agent-redundancy.md) - `active` / `medium`
- [Progressive Disclosure for Agent KBs](concepts/progressive-disclosure-for-agent-kbs.md) - `active` / `high`
- [Raw Flow Dump](concepts/raw-flow-dump.md) - `active` / `medium`
- [Refs Not Copies](concepts/refs-not-copies.md) - `active` / `high`
- [Role Boundary and Non-Ownership](concepts/role-boundary-and-non-ownership.md) - `active` / `high`
- [Scheduler Boundary](concepts/scheduler-boundary.md) - `needs_review` / `medium`
- [Scheduler Deferment Rule](concepts/scheduler-deferment-rule.md) - `active` / `high`
- [Semantic Planning Layer](concepts/semantic-planning-layer.md) - `active` / `high`
- [Session Memory and Next Context](concepts/session-memory-and-next-context.md) - `active` / `high`
- [Skill Boundary](concepts/skill-boundary.md) - `active` / `high`
- [Standard Handoff Packet](concepts/standard-handoff-packet.md) - `active` / `high`
- [State Delta Preservation](concepts/state-delta-preservation.md) - `active` / `high`
- [Status Merge Packet](concepts/status-merge-packet.md) - `active` / `medium`
- [Stop Condition as Context Saver](concepts/stop-condition-as-context-saver.md) - `active` / `high`
- [Validator as Non-Executor](concepts/validator-as-non-executor.md) - `active` / `high`
- [Weekly Plan Packet](concepts/weekly-plan-packet.md) - `active` / `medium`
- [Weekly Routine Workflow Case](concepts/weekly-routine-workflow-case.md) - `active` / `medium`
- [Workflow Boundary](concepts/workflow-boundary.md) - `active` / `medium`
- [YAML-First Artifact Design](concepts/yaml-first-artifact-design.md) - `active` / `high`

## Entity Pages

- [Agent Skills Standard](entities/agent-skills-standard.md) - `active` / `high`
- [Aider](entities/aider.md) - `active` / `medium`
- [BMAD-METHOD](entities/bmad-method.md) - `active` / `medium`
- [Claude Code Hooks](entities/claude-code-hooks.md) - `active` / `high`
- [Claude Code Plugins](entities/claude-code-plugins.md) - `active` / `high`
- [Claude Code Skills](entities/claude-code-skills.md) - `active` / `high`
- [Claude Code Subagents](entities/claude-code-subagents.md) - `active` / `high`
- [Claude Code Workflows](entities/claude-code-workflows.md) - `active` / `medium`
- [Claude Code](entities/claude-code.md) - `active` / `high`
- [Apex KB](entities/max-run-20260709/apex-kb.md) - `new_parallel_compile` / `high`
- [Claude Code Hooks](entities/max-run-20260709/claude-code-hooks.md) - `new_parallel_compile` / `high`
- [Claude Code Plugins](entities/max-run-20260709/claude-code-plugins.md) - `new_parallel_compile` / `high`
- [Claude Code Skills](entities/max-run-20260709/claude-code-skills.md) - `new_parallel_compile` / `high`
- [Claude Code Subagents](entities/max-run-20260709/claude-code-subagents.md) - `new_parallel_compile` / `high`
- [Claude Code](entities/max-run-20260709/claude-code.md) - `new_parallel_compile` / `high`
- [Model Context Protocol](entities/max-run-20260709/mcp.md) - `new_parallel_compile` / `high`
- [Model Context Protocol](entities/mcp.md) - `active` / `high`
- [Scheduler](entities/scheduler.md) - `needs_review` / `medium`
- [SWE-agent](entities/swe-agent.md) - `active` / `medium`

## Summary Pages

- [Agent Handoff and Contract System](summaries/agent-handoff-and-contract-system.md) - `active` / `high`
- [Claude Mechanism Decision Model](summaries/claude-mechanism-decision-model.md) - `active` / `high`
- [Apex KB as Source-Preserving Agent Memory](summaries/max-run-20260709/apex-kb-as-source-preserving-agent-memory.md) - `new_parallel_compile` / `high`
- [Claude Code Mechanism Decision Model](summaries/max-run-20260709/claude-code-mechanism-decision-model.md) - `new_parallel_compile` / `high`
- [Deterministic vs LLM Execution Model](summaries/max-run-20260709/deterministic-vs-llm-execution-model.md) - `new_parallel_compile` / `high`
- [Failure Analysis and Feedback Loop](summaries/max-run-20260709/failure-analysis-and-feedback-loop.md) - `new_parallel_compile` / `high`
- [Minimal Claude Orchestration Architecture](summaries/max-run-20260709/minimal-claude-orchestration-architecture.md) - `new_parallel_compile` / `high`
- [Production Agent Readiness and Risk Model](summaries/max-run-20260709/production-agent-readiness-and-risk-model.md) - `new_parallel_compile` / `medium`
- [Skill, Hook, Plugin, and MCP Boundaries](summaries/max-run-20260709/skill-hook-plugin-mcp-boundaries.md) - `new_parallel_compile` / `high`
- [Subscription, Seat, Terminal, and Machine Model](summaries/max-run-20260709/subscription-seat-terminal-machine-model.md) - `new_parallel_compile` / `medium`
- [MCP Configuration and Trust Boundary](summaries/mcp-configuration-and-trust-boundary.md) - `active` / `high`
- [Minimal Claude Orchestration Architecture](summaries/minimal-claude-orchestration-architecture.md) - `active` / `high`
- [Production Agent Readiness and Roster Boundary](summaries/production-agent-readiness-and-roster-boundary.md) - `needs_review` / `medium`
- [Project Execution State Safety Model](summaries/project-execution-state-safety-model.md) - `active` / `high`
- [Scheduler Boundary and Deferment](summaries/scheduler-boundary-and-deferment.md) - `needs_review` / `medium`
- [Token-Efficient Information Design](summaries/token-efficient-information-design.md) - `active` / `high`
- [Weekly Routine as Orchestration Case Study](summaries/weekly-routine-as-orchestration-case-study.md) - `active` / `medium`

<!-- END AUTO-GENERATED INDEX -->

<!-- BEGIN LLM SUMMARY -->

Phase 2 compiled the Claude Code orchestration design KB around six specialized indexes: agent orchestration, handoff contracts, project execution safety, weekly routine case study, Claude mechanism mapping, and token-efficient information design.

The compiled doctrine is intentionally non-runtime: it defines patterns, boundaries, reads/writes, token-efficiency rules, drift controls, and unresolved questions without creating hooks, skills, workflows, plugins, MCP config, schedulers, production agents, raw-source edits, manifest edits, or deterministic indexes.

<!-- END LLM SUMMARY -->
