---
title: "Orchestration design benchmark — Fable vs Weekly Orchestrator vs KB best practice"
date: 2026-07-12
method: "Single Explore-agent read-only pass over apex-meta/kb/claude-code-orchestration-design/ (13 named practices, P1-P13) cross-checked against apex-meta/orchestration/ (System A, 'Fable') and .claude/skills/weekly-orchestrator/ + .claude/CLAUDE.md (System B, 'Weekly Orchestrator'). No agents from either system were spawned to produce this comparison — inspection only, per the lean-working-agent mode."
verdict: "Both systems independently and closely implement the KB's practices. No practice is unimplemented by both. Three narrow, fixable gaps found; one documented and harmless divergence found."
---

# Orchestration design benchmark

## Headline

Both orchestration systems on `main` were built as close, largely independent implementations of
the same best-practice KB (`apex-meta/kb/claude-code-orchestration-design/`). They converge on the
same handoff-packet shape, the same ephemeral/persistent agent boundary, the same state-in-files
invariant, and the same owner/validator review split — this is real, load-bearing agreement, not
duplication for its own sake.

## The 13 KB practices, compliance at a glance

| # | Practice | System A (Fable) | System B (Weekly Orchestrator) |
|---|---|---|---|
| P1 | 3-layer separation (plan/sync/session) | Compliant | Compliant |
| P2 | Gated write, dry-run default | Compliant | Compliant |
| P3 | Artifact-contract handoff | Compliant | Compliant |
| P4 | Gate + closure/fetch-back proof | Compliant | Compliant |
| P5 | Standard handoff packet fields | Compliant | Compliant |
| P6 | Owner/validator split | Compliant | Compliant |
| P7/P8 | Progressive disclosure, thin scaffold | Compliant (CORE.md) | Compliant (role-doctrine files) |
| P9 | Packet size budget | Partial (KB itself unresolved) | Partial (KB itself unresolved) |
| P10 | Ephemeral vs persistent agent boundary | Compliant | Compliant |
| P11 | Falsification-first, bounded reviewer authority | Compliant, schema-enforced | Partial — instructed, not schema-enforced |
| P12 | State in files, fetch-back, HALT/CLARIFY | Compliant | Compliant |
| P13 | Candidate never auto-promotes | Compliant | Compliant |

## Three concrete, decidable gaps

1. **Review-verdict vocabulary divergence.** System A: 5 values
   (`escalate/needs_input/hold/revise/pass`), with a required `falsification_attempt` object and an
   `evidence_free_pass_gate` structural check per criterion — a malformed or skipped falsification
   cannot silently pass. System B: 4 values (`pass/needs_revision/fail/blocked`), falsification
   *instructed* narratively in `apex-review-validity.md` but with no equivalent structural field.
   Both converge on "no LLM tiebreak, reviewer never fixes." Nowhere is this divergence recorded as
   an intentional product decision (unlike the macro-topology divergence below) — it reads as
   parallel, uncoordinated instantiation of the same KB practice (P11).

2. **No measured token/cost telemetry anywhere.** The KB names token economy as a first-class
   objective (P7-P9). System A's simulation records (`US-IDEA-01`, `US-SEQ-01`) contain qualitative
   behavioral evidence and file-size proxies (the CORE.md line-count reduction: 325-1135 lines → 55-137,
   ~82-93%) but zero actual token counts from a real run. System B has an operational proxy (a
   ≤12-line stage-return cap) but likewise no measured token cost. Design intent for efficiency exists
   in both; the loop from "designed to be efficient" to "measured to be efficient" is not closed in
   either.

3. **No numeric packet-size ceiling (P9).** Both systems correctly inherit the KB's own unresolved
   question rather than inventing an arbitrary number — this is not a system defect, but it does mean
   the repo has no answer to "how big is too big" anywhere.

## One divergence that is fine as-is

System B's macro architecture was decided against a *different* evidence chain than this KB, by
explicit operator priority (`apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md`
line 3). The resulting topology — main-thread orchestrator + ephemeral stage subagents, one write
path, dual `authority.state`/`operator_validation` gate — ended up structurally identical to System
A's anyway. Different evidence trail, same destination. Nothing to fix here.

## Recommendation options (decisions for the operator, not defaults)

See the three questions asked directly in the session that produced this report. Recorded here for
continuity if this file is read cold in a future session.
