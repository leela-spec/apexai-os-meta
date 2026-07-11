---
title: "Fable Orchestrator Initiative"
purpose: "Lock the decisions and process for the final Claude-Code multi-agent orchestration build, run by Claude Fable 5 as the orchestrating brain, with heavy reasoning/execution outsourced to external models."
created: 2026-07-11
status: decisions_locked
---

# Fable Orchestrator Initiative

## The core problem

Fable's central job is to deeply understand the systems being merged — not assume, actually understand — before deciding how to merge them:

- **`apex-plan` / `apex-sync` / `apex-session`** — the three-package planning/computation/mutation system, real skill contracts, real current behavior.
- **The old Apex agent-swarm system** (`old-apex-full-orchestration-agent-kb` + `-v2`) — its role model, handoff rules, and failure-mode lessons.
- **`claude-code-orchestration-design`** — the best-practice reference KB guiding how the two above should actually come together in Claude Code.

The concrete open architecture questions this understanding must resolve are in `apex-meta/handoff/agent-skill-system-research/design-lock-qa.md` (topology, how the systems relate, subagent scoping, and more). Fable answers those from real evidence in the three sources above — not from a pre-picked default.

## Operating model

- **Claude Fable 5** is the orchestrator, running inside Claude Code. It holds the context, makes decisions, writes/moves files directly, and authors prompts for other models.
- **Heavy reasoning/research** (deep research, pro-thinking analysis) is outsourced to external frontier models via hand-authored prompts the operator copies in and results the operator copies back: ChatGPT (deep research / pro-thinking), Gemini (deep research / pro-thinking — standard research use only), Perplexity (has a working GitHub connector, so it's the one reliable option for live-repo-file research).
- **Heavy execution** (actual repo commands, patches, commits) is outsourced to **Codex**, per the already-existing `apex-meta/CODEX_EXECUTION_STANDARD.md` — do not redefine this, just reuse it.
- The point of this split: Fable's own tokens are reserved for orchestration judgment (what to ask for, how to integrate results, what to decide), not for doing the heavy lifting itself.

## Files here

See `00-START-HERE.md` for the full index and reading order.

## Sequencing

Decisions are locked (`decisions.md`) and the execution flow is defined (`process-blueprint.md`, `build-plan.md`). Begin the real reconciliation/build work across the systems named above and in `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`, using `fable-execution-best-practices.md` as on-demand reference during the run.
