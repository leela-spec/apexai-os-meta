---
title: "System Audit vs. claude-code-orchestration-design KB"
purpose: >
  Evaluation of the built orchestration system against the reference KB's testable
  design rules, run 2026-07-11 by an independent audit pass over the KB's load-bearing
  pages (minimal-claude-orchestration-architecture, agent-skill-orchestration-resilient-
  workflows, apex-application-orchestration-patterns, agent-vs-subagent-vs-skill,
  skill-package-design-contract, token-efficient-information-design,
  agent-subagent-design-patterns) and every file of the built system.
created: 2026-07-11
result: "15 PASS, 3 PARTIAL, 1 FAIL, 3 N/A — all 5 optimizations applied same session (see §3)"
---

# System Audit vs. Orchestration-Design KB

## 1. Scoreboard

| Area | Rules | Result |
|---|---|---|
| Mechanism selection (ladder, no premature plugins/MCP/persistent agents) | R1–R3 | 3 PASS |
| Resilience (state location, adversarial review, isolation, fail-fast chaining) | R4–R7 | 3 PASS, 1 PARTIAL (R4: loop is conversation-held; file-state is the compensating control) |
| Subagent definitions (tool allowlists, spawn scope, main-conv criterion, self-containment, descriptions) | R8–R12 | 3 PASS, 1 FAIL (R9 spawn wiring undocumented), 1 PARTIAL (R10 invocation modes unstated) |
| Context economy (compact anchors, refs-not-copies, YAML-first, thin scaffold, no invented budgets) | R13–R17 | 5 PASS |
| Deterministic boundary (scripts for deterministic work, LLM only for semantics) | R18 | PASS |
| Out of scope | R19–R21 | 3 N/A |

Auditor's overall: "the built system is strongly aligned with the KB — mechanism-ladder discipline, deferment-with-reasons, file-state resilience, adversarial review, deterministic boundaries, and context economy are genuinely implemented, not asserted. The one real defect cluster is invocation-mode ambiguity."

## 2. The one FAIL (R9), verbatim finding

No agent definition included `Agent` in its tools, yet the workflows had Meta Ops spawning detective lenses and lane workers — unexecutable if Meta Ops were itself spawned as a subagent (spawn scope is not inherited). The system was only coherent if Meta Ops ran in the main conversation, and no file said so.

## 3. Optimizations applied (same session, all five)

| # | Fix | Where |
|---|---|---|
| P1 | Declared invocation modes: Alfred + Meta Ops = **main-conversation contracts** (adopted, never spawned); Strategy/Detective/lanes/workers = spawned ephemerals | `ARCHITECTURE.md` §2 (new load-bearing paragraph), `workflows/orchestrator-run.md` header, `workflows/detective-review.md` invocation note |
| P2 | Meta Ops reaches skills + spawning because it runs in the main conversation — stated in its definition | `.claude/agents/meta-ops.md` description (INVOCATION MODE) |
| P3 | Alfred marked main-conversation contract (operator back-and-forth impossible from an isolated subagent) | `.claude/agents/alfred.md` description (INVOCATION MODE) |
| P4 | Script-held-loop escalation trigger recorded: promote to a Workflow script IF a simulation shows interruption losing in-flight work file-state didn't capture | `ARCHITECTURE.md` §7.4 |
| P5 | Lane write boundaries honestly labeled guidance-not-enforcement, with permission settings named as the enforcement rung if ever needed | `ARCHITECTURE.md` §6 (new row) |

## 4. Standing PARTIALs (accepted, with triggers)

- **R4** conversation-held loop: accepted per mechanism ladder (don't escalate without observed failure); trigger recorded as §7.4.
- **R10**: resolved by P1/P3 documentation; the deeper version (main conversation re-gathering context across phases) is mitigated by file-held packets — same trigger as R4.
