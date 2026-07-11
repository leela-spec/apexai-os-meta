---
title: "Orchestrator Run Loop (macro → meso → micro)"
purpose: >
  The canonical run loop every user story instantiates — the Meta Ops workflow-backbone
  contract. State always in files; subagents ephemeral; one mutation surface; one gate
  primitive; Detective review before consequence.
created: 2026-07-11
---

# Orchestrator Run Loop

## Invariants (break any of these = the run is invalid)

1. **State lives in files**, never in a context window. Plan, packets, verdicts, deltas — all on disk before the turn ends. (Resilience = where the plan lives.)
2. **One mutation surface**: durable state changes only through the apex-session gated path; registry writes only through `scripts/apex_sync.py --dry-run false` after a drift report.
3. **One gate primitive**: `operator_validation: confirmed` — required for every consequential mutation; never implied, never defaulted.
4. **Independent review before consequence**: consequential artifacts pass `detective-review.md` and reach `authority.state: verified` before feeding a confirmed write.
5. **Candidate never auto-promotes**: after-action learning stays `candidate` until independently reviewed and operator-accepted; no agent rewrites its own doctrine.

## The loop

| Phase | Accountable | Mechanism | Output (all handoff-packet schema) |
|---|---|---|---|
| 1. Intake | **Alfred** | conversation + Read | intake packet: operator intent, constraints, explicit decisions needed (`lifecycle_stage: proposal`) |
| 2. Macro framing | **Meta Strategy** | subagent, read-only | 2–3 direction options with leverage/timing/risk; operator SELECTS (Strategy never self-validates) |
| 3. Meso skeleton | **Meta Ops** | `apex-plan` skill | candidate execution skeleton, dependencies, proposed batches (`proposal`) |
| 4. Deterministic checks | **Meta Ops** | `apex-sync` / `scripts/apex_sync.py` | next-actions/blockers/drift report (`computed`, reproduction command recorded) |
| 5. Bounded execution | specialist lanes / domain workers | ephemeral subagents, narrow allowlists | one artifact per packet, `authority.state: candidate`; workers get only source slice + acceptance criteria + tools + stop condition |
| 6. Integration | **Meta Ops** | Read/Write | integrated artifact set, integration notes; conflicts surfaced, not absorbed |
| 7. Review | **Meta Detective** ×2 lenses | `detective-review.md` | verdicts; defects routed to named owners; pass ⇒ `verified` |
| 8. Operator gate | **Alfred** presents, **operator** decides | conversation | `operator_validation` recorded per decision (approve / revise / reject / split / defer) |
| 9. Confirmed mutation | **Meta Ops** | `apex-session` skill | status mutation records + H6 handoff (`confirmed`; every authoritative input `verified`) |
| 10. Close | **Meta Ops** | `apex-session` | state delta + next-session packet + candidate learning queue |

Phases 3–7 iterate per batch. The **milestone rule** governs depth: full loop for consequential outputs; low-consequence intermediates may collapse phases 5–7 into direct Meta Ops work — but never phase 8–9's gate.

## Failure & repair behavior

- A worker exceeding its stop condition hands back — it does not widen its own scope.
- A packet the receiver can't act on inside its accountability is routed back, not reinterpreted.
- Detective `revise` verdicts go to the named owner; `escalate`/repeated `hold` go to the operator with the concrete blocker.
- Interrupted run: the next session resumes from the files (packets + registry + H6), never from memory of the conversation.

## Regression rule

Any change to the schemas, workflows, agent definitions, or the three apex skills re-runs the affected user stories (`../user-stories/user-stories.md`) and records the result in `../simulations/`.
