---
title: "Chosen Blueprint Processes for Fable's Orchestration Build"
purpose: "The decided, ranked selection from ProcessRanking_GPT&MasterOA.md to actually use — not a question, a chosen answer."
source: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/ProcessRanking_GPT&MasterOA.md"
created: 2026-07-11
status: finalized_input — Fable and the operator treat this as the blueprint unless explicitly revised
---

# Chosen Blueprint Processes

The source file ranks 20 process/methodology patterns for a different domain (personal Master-of-Arts workflows). Below is the actual re-ranking for *this* build — building the final Claude Code multi-agent orchestration system — with each process's role decided, not left open.

## Ranked and chosen (in build priority order)

| Rank | Process | Role in this build | Status |
|--:|---|---|---|
| 1 | `PRC-MULTI-001` Orchestrator-Worker Fan-Out/Fan-In | **Core mechanism.** This is the literal Fable → {ChatGPT deep research, Gemini deep research, Perplexity+GitHub, Codex execution} split. Everything else in this list supports this one. | **chosen** |
| 2 | `PRC-HANDOFF-001` Handoff With Guardrails | **Core mechanism.** Governs the prompt-out/result-in packet shape between Fable and each external model — see `fable-execution-best-practices.md` §3 for the concrete prompt frame. | **chosen** |
| 3 | `PRC-VERIFY-001` Chain-of-Verification Gate | **Mandatory.** Every external-model result is unverified input until Fable grounds it against real repo state — see `fable-execution-best-practices.md` §4. Ranked above the source file's own placement because outsourced reasoning makes this more critical here than in the original domain. | **chosen, elevated** |
| 4 | `PRC-CORE-001` Goal-to-Verified-Artifact Loop | **Per-task backbone.** Applies inside each individual build/reconciliation task: intake → goal → source map → draft → verify → revise. | **chosen** |
| 5 | `PRC-RISK-001` Govern-Map-Measure-Manage | **Reused, not rebuilt.** Mapped onto the existing `.claude/CLAUDE.md` operator-constraint set (batch-write confirmation, no destructive ops without approval, gated mutation) rather than a new risk framework. | **chosen, reused as-is** |
| 6 | `TEMPLATE-KANBAN-001` Durable Multi-Agent Task Graph | **Scoped down.** Not a full Kanban board — a single `decisions.md` + plain running task list inside `apex-meta/fable-orchestrator/`, since this is one continuous Fable-led effort, not a distributed human team. | **chosen, lightweight** |
| 7 | `PRC-DIV-001` Diverge-Converge Diamond | **One-time phase only.** Used once, for reconciling the multiple existing orchestration KBs/systems into a single target architecture — not a standing process applied per task. | **chosen, scoped to one phase** |
| 8 | `PRC-SYS-001` Systems Engineering Flow | **Same one-time phase as #7**, for the specific act of turning "many systems" into "one target architecture" (requirements → architecture → verification). Largely overlaps with #4 at this build's scale — use only if #4 alone proves insufficient during that phase. | **conditional** |
| 9 | `PRC-DATA-001` CRISP-DM Evidence/Data Flow | **Situational.** Applies only to the KB-reconciliation sub-work (structuring the merged, messy corpus in `claude-code-orchestration-design/`), not the build as a whole. | **situational** |
| 10 | `PRC-SCRUM-001` Sprint Artifact Loop | **Dropped.** Designed for recurring human-team cycles; this build is one continuous session-based effort, not a sprint cadence. | **dropped** |

## Explicitly not used, with reason

| Process | Why not |
|---|---|
| `PRC-SUPERVISOR-001` Supervisor Tool-Calling | Not a gap to fill — already covered by Fable's own direct tool calls and Codex handovers inside Claude Code. Re-examined specifically for this build (source file's original reasoning predates the Fable/external-model/Codex split) and confirmed redundant, not deprioritized by default. |
| `PRC-BRANCH-001` Tree-of-Thoughts Search | Token-expensive; reserve only for a genuinely hard, otherwise-unresolvable architecture choice, not standard use. |
| `PRC-MULTI-002` Group Chat Review | Noisy; not needed given #3 (Chain-of-Verification) already covers the verification need. |
| `PRC-DRAFT-001` Chain-of-Draft | Correctness and workflow coverage matter more than draft-token-efficiency for this build. |
| `PRC-PLAN-001` Plan-and-Solve | Absorbed by #4 (`PRC-CORE-001`). |
| Everything ranked 11–20 in the source file not listed above | Designed for the source file's own domain (workshops, recurring personal-business cycles, dependency/idea graphs); no clear mapping to this build — not adopted. |

## How this connects to the rest of the initiative

- Ranks 1–3 are already operationalized in `fable-execution-best-practices.md`.
- Rank 6 (lightweight task graph) is `decisions.md` + a plain task list, per `process-blueprint-qa.md` Q8.
- Ranks 7–8 are the single "phase 0.5" step in `build-plan-recommendation.md` §2 (architecture reconciliation), run once before phase 1's user stories.
- This file supersedes `process-blueprint-qa.md` as the operative answer — that file remains as the reasoning trail, this file is the decision.
