---
title: "Fable Orchestrator Initiative"
purpose: "Lock the decisions and process for the final Claude-Code multi-agent orchestration build, run by Claude Fable 5 as the orchestrating brain, with heavy reasoning/execution outsourced to external models."
created: 2026-07-11
status: decisions_not_yet_locked
---

# Fable Orchestrator Initiative

## What this folder is

This is the decision-lock and process-definition folder for the initiative to build **the final agent orchestration system in Claude Code** in this repo (`apexai-os-meta`), reconciling the multiple existing orchestration KBs/systems (see `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`) into one working multi-agent build.

The operating model, as stated by the operator:

- **Claude Fable 5** is the orchestrator, running inside Claude Code. It holds the context, makes decisions, writes/moves files directly, and authors prompts for other models.
- **Heavy reasoning/research** (deep research, pro-thinking analysis) is outsourced to external frontier models via hand-authored prompts the operator copies in and results the operator copies back: ChatGPT (deep research / pro-thinking), Gemini (deep research / pro-thinking — standard research use only), Perplexity (has a working GitHub connector, so it's the one reliable option for live-repo-file research).
- **Heavy execution** (actual repo commands, patches, commits) is outsourced to **Codex**, per the already-existing `apex-meta/CODEX_EXECUTION_STANDARD.md` — do not redefine this, just reuse it.
- The point of this split: Fable's own tokens are reserved for orchestration judgment (what to ask for, how to integrate results, what to decide), not for doing the heavy lifting itself.

## Files here

- `process-blueprint-qa.md` — decision-forcing Q&A over `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/ProcessRanking_GPT&MasterOA.md`, to pick which of its ranked processes/stacks become the actual blueprint for this build.
- `fable-execution-best-practices.md` — token-efficient, machine-readable operating doc for the Fable-run session itself: how to author prompts for each external model, how to integrate results, and real-world execution discipline (grounded in current web research on Fable 5's own capabilities and multi-model delegation practice).
- `decisions.md` — **not created yet.** Once `process-blueprint-qa.md` is answered, lock the answers here, following the same locked-decision format as `apex-meta/harmonization/decisions.md`.

## Sequencing

1. Answer `process-blueprint-qa.md`.
2. Lock answers into `decisions.md`.
3. Use `fable-execution-best-practices.md` as the standing operating doc for the actual Fable-led run.
4. Begin the real reconciliation/build work across the systems named in `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`.

Do not skip straight to step 4 without steps 1–2 — the whole point of this folder is to avoid re-deciding the same architecture questions mid-run.
