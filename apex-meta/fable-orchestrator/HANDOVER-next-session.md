---
title: "Handover — Next Fable Session"
purpose: "Entry point for a fresh Fable session picking up this initiative. Read this file first, before 00-START-HERE.md."
created: 2026-07-11
status: active_handover
---

# Handover to next Fable session

## Read order for this session

1. This file (you're reading it)
2. `00-START-HERE.md` — the full reading order for the initiative
3. Everything `00-START-HERE.md` lists, in the order it lists them

Do not skip to `build-plan.md` or start building anything. Milestones 1–5 in `target-log.md` are not done.

## Where things actually stand right now

- `discovery-notes.md` (milestone 1) is **written but not yet operator-verified.** Treat every claim in it as a hypothesis to re-check against the real source files, not as settled ground truth.
- `simulations/` does not exist. Milestone 6 (build) has not started. Do not create it or start build work this session.
- Milestone 2 (resilience dimensions from `claude-code-orchestration-design`) has not been done yet.
- Nothing has been decided beyond what's already locked in `decisions.md`.

## What this session's job actually is

Work milestone 1 → milestone 2 in `target-log.md`, for real, against the real files (not from memory or assumption):

1. Operator-verify `discovery-notes.md`: re-check its claims against the real source KBs it cites (`operator-research-orchestration-20260711`, `old-apex-full-orchestration-agent-kb`, `old-apex-full-orchestration-agent-kb-v2`, `apex-plan-sync-session-workflow-v2`). Resolve or explicitly flag the known discrepancy noted in its own "Open items for the operator" section.
2. Move into milestone 2: read `claude-code-orchestration-design`'s mechanism-ladder, resilience, and deterministic/LLM-split pages, and extract the concrete resilience dimensions milestone 3 will need.
3. **Stop as soon as you hit a question that genuinely needs an external model** (per the routing table in `fable-execution-best-practices.md` — ChatGPT/Gemini/Perplexity). At that point, write the exact, ready-to-paste prompt for that model into a file (not just chat), state clearly which model it's for and why, and end the session there. Do not try to answer it yourself from training data.

That external-research-prompt handoff point is the intended stopping line for this run — not milestone 2's full completion if a real external-input dependency comes up first.

## Operating rules to actually follow (not just acknowledge)

- Work from the filesystem, not memory — read the real current file before acting on any claim about it.
- Every material claim from a source KB gets checked against that KB's real content before it's used. No claim gets treated as verified just because it reads confidently.
- Write extracts to real files immediately (a KB page, `discovery-notes.md`, `decisions.md`) — don't let raw source text pile up in chat context.
- Never delete or overwrite a file on a "looks superseded" assumption — grep the whole repo for its path first, report what you find before acting.
- Update `target-log.md`'s Log section at the point you stop, so the next session (or the operator) can see exactly where this one ended and why.

## Mode

Run in Auto permission mode for this session — full autonomy over reads/edits/exploration, no manual accept-clicking expected from the operator, but background safety checks still apply and may still surface a prompt; that's expected and fine, not a sign anything is wrong.
