---
title: "Phase 1 Prompt — Real User Stories / Workflow Records"
purpose: "Self-contained prompt to hand to another chat/session to produce user-stories.md for real."
created: 2026-07-11
---

# Prompt

Read first, in this order: `apex-meta/fable-orchestrator/README.md` (the core problem), `apex-meta/fable-orchestrator/decisions.md` (D1: full final system, D2: orchestrator-worker only), `apex-meta/fable-orchestrator/process-blueprint.md`, `apex-meta/fable-orchestrator/target-log.md` (the milestone list), and `apex-meta/handoff/agent-skill-system-research/design-lock-qa.md` (the open architecture questions).

**Your task:** write `apex-meta/fable-orchestrator/user-stories.md` — concrete workflow records for the final merged Apex orchestration system (old Apex agent-swarm system + `apex-plan`/`apex-sync`/`apex-session`), not abstract capability bullets.

**Use as a realism template only, not content to adopt:** `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/ProcessRanking_GPT&MasterOA.md` and `Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md` in that same folder. Both describe a different domain (personal Master-of-Arts workflows), and the specific processes they rank were already eliminated (`decisions.md` D2). What's reusable is only the *shape* of a well-specified workflow record — real trigger, real inputs, real mechanism, real output, real handoff, real validation — not their content.

**For each workflow record, write:**
- **Trigger**: what starts this workflow.
- **Inputs**: the real files/context needed (name them).
- **Mechanism**: which of Fable / ChatGPT / Gemini / Perplexity / Codex does what, per `process-blueprint.md`.
- **Output**: the real artifact produced.
- **Handoff/validation**: how the result gets checked before it's trusted, and by whom.

**Starting use cases** (adjust or add as the real systems demand it — don't treat this as exhaustive):
1. Reconciling the old Apex agent-swarm system with `apex-plan`/`apex-sync`/`apex-session` into one target architecture (resolves `design-lock-qa.md`).
2. Deciding subagent-vs-inline-work for a given task, using `claude-code-orchestration-design`.
3. Checking a proposed workflow's resilience against best practice before building it.
4. Handing a messy multi-KB reconciliation task to Fable and getting back one decision document that resolves every named conflict with real citations.

**Output requirement:** real workflow records, each one runnable in principle — not a list of things the system "should" be able to do.
