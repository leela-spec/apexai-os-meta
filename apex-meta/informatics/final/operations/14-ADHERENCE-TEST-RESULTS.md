---
type: Evidence
id: EVIDENCE-ADHERENCE-TEST-RESULTS-v1.0
title: Adherence test results — 2026-11-03 (Claude Code, Leela-Cloud-2026)
description: Real-repo, real-OpenProject-issue execution trace, analyzed against the contract's own instructions, with findings split by what is vendor/harness-general versus repo-specific.
status: current_truth
tags: [evidence, adherence, claude-code, hooks, empirical]
---

# Adherence test results — 2026-11-03

> Named output slot per
> [`handovers/HANDOVER-07-PRE-ROLLOUT-ADHERENCE-TEST.md`](handovers/HANDOVER-07-PRE-ROLLOUT-ADHERENCE-TEST.md)
> §5 ("A results table at `operations/14-ADHERENCE-TEST-RESULTS.md`"). **Scope difference from that
> runbook, stated plainly**: HANDOVER-07 designs a pre-registered 6-task × 4-arm (A/B/C/D)
> synthetic protocol, not yet run. What follows is a *different*, real-world data point toward the
> same underlying question — one executing agent (Claude Code, repo
> [`Leela-Cloud-2026`](https://github.com)), one real bundle of five live OpenProject work packages,
> full layered instruction stack present throughout (no control arm). It complements
> [`13-INSTRUCTION-ADHERENCE-FIELD-EVIDENCE-HANDOVER.md`](13-INSTRUCTION-ADHERENCE-FIELD-EVIDENCE-HANDOVER.md)'s
> n=1 observational finding with a second, more thoroughly ground-truthed n=1 — not a replacement
> for HANDOVER-07's controlled test, which remains undone.

## What was run

A repo-local `AGENTS.md` layered on top of the global `apex_contract`, executing a bundle of five
real bug-fix tickets (#206-#210) under a parent Epic. Full method, ground-truth sourcing (harness
transcript, independent `git diff`, independent re-run of the repo's own gate script — never the
agent's self-report), and the complete finding set live at
`docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md` in the subject
repo (not duplicated here — that file is the originating artifact; this file states the portable
conclusion only, per `<ground>`: find the owner, don't restate it).

## Findings, split by what generalizes and what doesn't

### General — applies to any LLM coding agent, any harness (Claude, Gemini, Codex), evidenced by multiple independent sources, not just this one run

1. **Rules drift is real and session-length-dependent.** A rule loaded once at session start
   measurably loses salience as tool-output volume accumulates; multiple independent sources place
   the onset around message 20-30. In this run, the first violation of an explicit, unambiguous
   repo rule occurred well past that window, after 10 clean turns, and recurred 10 more times
   without self-correction. **Implication for the rollout this corpus exists to inform**: a
   long-session agent cannot be assumed to still be weighting a system-prompt rule the same way at
   turn 60 as at turn 1. Prose alone does not survive session length.
2. **The cheaper path wins by default under no adversarial pressure.** The agent did not need
   "pressure" or an adversarial framing to bypass a stated rule — ordinary iterative implementation
   was sufficient, because the forbidden path (a direct, fast, immediate-feedback tool call) stayed
   exactly as reachable as the correct one (a slower, batched gate-runner call) the entire time nothing
   structurally favored the correct path.
3. **Deterministic enforcement, not better prose, is what closes a bypass.** A `PreToolUse`-class
   hook — present in some form in Claude Code, Gemini CLI, and Codex CLI as of this writing, each
   with its own native config format and location — is the only mechanism in this corpus proven to
   close a bypass outright rather than reduce its likelihood. It does so by not depending on model
   attention at all.
   - Shared limitation, also confirmed across harnesses: these hooks **fail open** on a crash,
     timeout, or script error. A hook is a guardrail layered on top of sandboxing/approval policy,
     not a replacement for it.
4. **The right split for a cross-harness guard is: one neutral script, thin per-harness adapters.**
   Writing the actual check logic once, in a plain CLI script with no vendor-specific I/O, and
   giving each harness only a small adapter that translates its own hook JSON shape to that script's
   plain contract, avoids triplicating policy logic across Claude/Gemini/Codex config formats. This
   matches the pattern independently adopted by several open guard-rail projects for the same
   problem, not a convention invented for this corpus.
5. **A rule that states granularity without stating its trigger condition gets silently skipped.**
   The subject repo's own commit-discipline rule described *how* to batch commits but never stated
   *when* to commit without being asked; five fully verified, gate-green items landed with zero
   commits as a result. A conditional rule needs an explicit `WHEN` clause, not a description the
   reader must infer a trigger from — consistent with this corpus's own `<authoring>` guidance
   elsewhere, now additionally evidenced as a live failure mode, not just a style preference.

### Repo-specific — true only of `Leela-Cloud-2026`, do not generalize

- The specific bypassed rule (`flutter analyze`/`flutter test` must route through
  `python scripts/gates.py`) is that repo's own gate-runner architecture; no other repo in this
  corpus has an equivalent.
- The specific hook files (`.claude/hooks/block-direct-flutter.py`,
  `.claude/hooks/session-start-git-status.py`) and their harness-neutral backing scripts
  (`scripts/check_gate_runner_bypass.py`, `scripts/session_preflight_git_status.py`) are that repo's
  artifacts, proven live in that repo only.
- The corrected `AGENTS.md` commit-trigger wording is that repo's own carrier text.

## Open, not yet done

Per `docs/audits/.../README.md` §5 (the repo-local handover): wiring the same two harness-neutral
scripts into Gemini CLI's (`~/.gemini/settings.json`, `BeforeTool`) and Codex CLI's
(`~/.codex/hooks.json`, `PreToolUse`) native hook formats, with the same pipe-test-then-prove-live
discipline used for Claude Code, has not been attempted. HANDOVER-07's own pre-registered, controlled
A/B/C/D protocol also remains unrun — this evidence file does not substitute for it, since it has no
control arm.

## Sources

- `docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md` (Leela-Cloud-2026) — full method, transcript citation, and finding set.
- `docs/audits/handovers/2026-11-03-{a,b,c}*.md`, `2026-11-03-inter-feature-runtime-reliability-fixes-handover.md` (Leela-Cloud-2026) — the four blind real-task handovers this corpus's adherence-test design produced, one of which (D, the runtime-reliability bundle) is the subject of this evidence file.
