---
title: "Fable-Mode Handover — Discovery Continuation"
purpose: "Self-contained prompt to hand to a Claude session in Fable mode to continue and verify the discovery track (milestones 1-2), independent of the separate APEX_Orchestration_User_Stories/ track."
created: 2026-07-11
---

# Prompt

Read first, in this order: `apex-meta/fable-orchestrator/README.md` (the core problem), `apex-meta/fable-orchestrator/decisions.md` (D1: full final system, D2: orchestrator-worker only), `apex-meta/fable-orchestrator/target-log.md` (the milestone list and current state), and `apex-meta/fable-orchestrator/discovery-notes.md` (a first research pass across the four source materials — already written, **not yet operator-verified**).

**Context:** `discovery-notes.md` was seeded by four parallel research reads (one per source: old orchestration v1, old orchestration v2, `apex-plan-sync-session-workflow-v2`, `claude-code-orchestration-design`). It is real, cited findings — not placeholder scaffolding — but it has not been checked against the raw sources by you or the operator yet. Treat every claim in it as a hypothesis to verify, not settled fact.

`APEX_Orchestration_User_Stories/` (7 complete stories, package manifest, connection ledger) is **input material** for milestone 1 and later milestone 5 — not this initiative's final deliverable (the final deliverable is the built orchestration system, milestone 6). It is a separate, already-finished track — read it for context if useful, but it is not your job here and not something to reopen or re-verify.

**Your task:**

1. **Verify, don't re-derive.** For each of the four sections in `discovery-notes.md`, spot-check the cited file paths against the actual KB content. Confirm or correct each claim in place — edit `discovery-notes.md` directly, don't create a parallel file. Where you correct something, say what changed and why in a short note at the point of correction (not a separate changelog).
2. **Resolve the "Open items for the operator" section first** — in particular the v2 Phase-1-vs-Phase-2 discrepancy. Read `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/wiki/index.md` yourself and state plainly whether the 17 Phase 2 pages are real, current, and citable, or provisional/stale.
3. **Then move to milestone 2** (`target-log.md` milestone 2: resilience best-practice) — go deeper into `claude-code-orchestration-design`'s skill-package pages than the first pass did, since that KB is the largest (106 pages) and the first pass was necessarily selective. Where the KB itself is thin on a question you need answered, produce an external-research prompt (following the `fable-execution-best-practices.md` model-routing table — ChatGPT/Gemini/Perplexity for external reasoning) rather than guessing.
4. **Write everything back into `discovery-notes.md` as you go** — this file is meant to be rechecked and updated through the whole process, not written once and left. Add a dated entry to `target-log.md`'s Log section when you reach a milestone gate, per the existing log convention (short, factual, no narrative).
5. **Stop at the milestone 1/2 gate.** Per `target-log.md`, both milestones require operator verification before milestone 3 (evaluating soundness/impact/resilience) begins. Do not proceed past the gate — summarize what's ready for review and what's still open.

**Constraints (from `apex-meta/.claude/CLAUDE.md`):** never overwrite `state/` files — append or flag conflicts only; never batch-write multiple output files without operator confirmation (this handover pre-authorizes edits to `discovery-notes.md` and `target-log.md` specifically — anything beyond those two, confirm first); on hard-required missing input, halt and report rather than guessing.
