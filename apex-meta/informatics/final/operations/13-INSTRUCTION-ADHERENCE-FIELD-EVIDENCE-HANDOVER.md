---
type: Handover
id: OPS-13-ADHERENCE-FIELD-EVIDENCE
title: Handover 13 — Field evidence on instruction adherence: what changed agent behaviour and what did not
description: Answers: across one long multi-turn session governed by the v1.0-ultra contract, which instructions were actually followed, which were violated repeatedly, what mechanism caught each violation, and what does that imply for JIT module dispatch?
tags: [handover, adherence, dispatch, jit-modules, field-evidence, rp-01, fa-10]
status: current
---

# Handover 13 — Field evidence on instruction adherence

Observational field data from a single long session on the `Leela-Cloud-2026` repository
(2026-10-28), governed by `v1.0-ultra` plus a repo Layer 2. **Not a controlled experiment** — one
agent, one session, no arm. It is recorded because the corpus's adherence claims are otherwise
supported by published benchmarks and no in-house observation.

## 1. The observation

The same operator correction was issued **five times**: repo-specific rules must not live in a
Claude-only carrier. Each time the agent agreed, acted, and then re-derived a different wrong
placement on the next turn. Separately, the agent **invented** a bundle layout, a module naming
scheme and a formatting convention that were already specified in `specs/file-architecture.md`
(`FA-10`, `FA-12`, `FA-13`) and `specs/writing-profile.md`.

## 2. The mechanism, as diagnosed

- **The violated rules were all in JIT modules**, reachable only through a `ref=` on a Layer 1 tag.
  Nothing forced the open.
- **`<authoring ref="index.md">` was present the whole time.** The pointer existed and was not
  honoured, repeatedly, by an agent that had read the contract.
- **The failure is not forgetting — it is substitution.** When a needed convention was not in the
  always-loaded surface, the agent generated a plausible one rather than retrieving the real one.
  Generating is immediate and reads as progress; retrieval costs a call and requires admitting
  ignorance.

This is the behaviour `RP-01` predicts. A `ref=` is a model-discretionary conditional, and no
controlled test shows one causes a file to be opened.

## 3. What actually caught the violations

Counted over the session:

- **Deterministic checks: 7 catches.** A ledger-to-destination join caught three rules being
  silently dropped during a rewrite, including one invariant that had been lost twice before. A
  citation check caught two stale `path:line` references created by the agent's own edits. A
  frontmatter check and an allowlist check caught two placement errors.
- **Prose rules: 0 catches.** No written rule prevented a violation before the fact in this
  session.
- **Operator correction: 5 catches**, all of the same error.

A sabotage harness also surfaced a **rotted scenario** — a check whose planted defect had stopped
being a defect, so it passed for the wrong reason. Self-tests decay against a moving target; a
green suite is not evidence that a given scenario still tests anything.

## 4. Conclusion

**Within this observation, adherence tracked enforceability, not clarity.** The violated rules were
well written, correctly placed and correctly pointed at. What they lacked was a mechanism that did
not depend on the agent choosing to retrieve them.

The practical ordering this suggests — strongest first:

- **A deterministic check** that fails at the moment of violation, carrying the rule in its error
  message.
- **Harness-enforced injection** where the runtime provides it (path-scoped loading was measured
  6/6 in the same repository, but is vendor-specific and therefore not portable).
- **A `ref=` pointer**, which is a hint.
- **More prose**, which `RP-07` already measures as costly and non-improving.

## 5. Caveats — read before citing this

- **n=1, single agent, single session, no control arm.** This cannot distinguish "modules do not
  dispatch" from "this agent did not dispatch them".
- Counts were taken from the session record by hand, not instrumented.
- The agent diagnosing the failure is the agent that committed it, so the mechanism in §2 is
  self-report, not measurement.
- It does **not** follow that JIT modules should be abandoned. The corpus's own sizing research
  (`RP-03`, `RP-09`) and `A06` make the opposite case on cost grounds, and `A06` warns that
  "context economy must not become context starvation."

## 6. Prior work this joins — read these first

- **`RP-01`** — conditional prose gating is an unverified dispatch mechanism. **This handover is
  field evidence consistent with it.**
- **`RP-07`** (`research/03-research-of-file-10/.../RESULTS-07-over-building.md`) — over-building
  as an objective/completion failure; carries Gloaguen et al., *Evaluating AGENTS.md* (2026),
  measuring repo context files at **>20% cost with no success gain**.
- **`RP-10`** (`RESULTS-10-surface-layering.md`) — the two-layer carrier architecture.
- **`A06`** (`research/01-universal-instruction-research/module-deepening/A06-context-engineering-progressive-disclosure/`)
  — progressive disclosure, JIT retrieval, and the context-starvation guard. Carries OpenAI's
  Harness Engineering report: a single large `AGENTS.md` failed at ~1M lines.
- **`DEC-16`** — file-boundary splitting, with its own falsifier: *"the read-trace test shows
  agents open non-matching module files anyway."* **Still unrun, and it is the decisive test for
  this handover too.**
- **`candidates/04-empirical-test-protocol.md`** — the pre-registered 16-task, 9-arm harness built
  for exactly this question.

## 7. The test that would settle it

`DEC-16`'s read-trace arm and `04-empirical-test-protocol.md` already specify it: place a marker
only a module can answer, give the agent a task whose contract tag refs that module, and record
whether the module is opened without instruction. Run it across Claude, Codex and Gemini, since
dispatch availability differs by runtime.

Until that runs, treat §4's ordering as a **working hypothesis supported by one session**, not a
finding.
