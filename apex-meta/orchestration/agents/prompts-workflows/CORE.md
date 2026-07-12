---
title: "Prompts & Workflows — operational core (distilled)"
purpose: >
  Single always-read doctrine core, replacing a fresh full re-read of ESSENCE+BEST_PRACTICES+
  MISTAKES (~508 lines; TEMPLATES and the ~1,600 lines of appendices stay separately on-demand) on
  every invocation. Drops YAML wrapper fields (refs/scores/owner/validator/review_due) and appendix
  pointers the manifest already says to ignore; keeps the practice/pattern payload.
distilled_from: "ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md (kept, verbatim, as
  on-demand references — not deleted)"
created: 2026-07-12
---

# Prompts & Workflows — core

Owns: reusable prompt structures, workflow-stage patterns, bounded execution sequences, handoff
templates. Does not own: orchestration authority, model/config routing authority, KB placement
authority, promotion approval, config mutation.

## Core doctrine
**Target first:** name exact deliverable, scope, non-goals, source authority, output contract, and
stop condition before execution. **Bounded execution:** one substantial deliverable or one closed
file set per pass — not broad autonomy. **Authority before action:** source authority is a pre-step
gate; verification is a post-step gate; fluent output is not evidence. **Verify before trust:**
read-back, diff, file-state check, or test before reporting completion. **Capture, don't smuggle:**
out-of-mode improvements go to a capture note, not into the current bounded run. **Examples are
regression tests**, not decorative reference. **Templates are not governance.**

Note on state: the manifest's "constant frame control" doctrine (explicit STATE_BLOCK relay) was
written for chat-continuity systems without durable file state. This system already carries state in
files (packets, run folders, `authority.state`) per `orchestrator-run.md` invariant 1 — the *discipline*
survives (explicit task contract, atomic scope, no implicit continuation, HALT/CLARIFY as routing
signals) but the literal state-block mechanics do not need to be replicated.

## Default sequence
1. Lock target and source authority. 2. Classify overload and non-goals. 3. Choose patch/full-body/
live-edit/research/handoff mode. 4. Execute one bounded deliverable. 5. Verify against source/file
state. 6. Record deferred candidates (not apply them). 7. Stop or hand off explicitly.

## Eleven practices (condensed — full entries with context/refs/scores in BEST_PRACTICES.md, on demand)
1. Full-body/live-edit for fragile diff transport; patch mode only for small, stable-anchor defects.
2. Freeze objective/target/source-authority/non-goals/output-contract/stop-condition before execution.
3. Bounded, stage-gated execution — not giant multi-phase prompts.
4. Source authority is the pre-step gate; verification is the post-step gate.
5. Capture out-of-mode improvements explicitly; never apply them silently.
6. Clean handoffs across chats/agents/lanes: settled state, source priority, non-redo list, exact
   next job, risks, success condition.
7. Record durable QA/gap/next-research findings somewhere durable, not chat-only.
8. Treat prompt/workflow examples as behavioral regression tests, not decoration.
9. Carry execution state explicitly (see note above); never reconstruct it from chat history alone.
10. Execute high-risk tasks as one atomic task: one target, explicit input refs, a gate check before
    write.
11. Treat HALT/CLARIFY/patch-check-failure/split-required as hard routing controls, not prose warnings.

## Eleven failure patterns to avoid (condensed — full entries with triggers in MISTAKES.md, on demand)
1. **Whole-document rewrite for a bounded defect** — causes silent compression/omissions. Patch the
   named section instead.
2. **Summaries/prior-chat claims treated as primary truth** when raw source is available.
3. **One prompt blends research+architecture+editing+QA+packaging** into one opaque pass. Split it.
4. **Approval by fluency** — no read-back/diff/test before claiming done.
5. **A reusable template treated as hidden runtime governance.**
6. **Out-of-mode improvements silently applied** during a bounded run.
7. **A named artifact treated as the whole task** even when the operator's intent was broader —
   check intent-vs-artifact-contract before reporting completion, don't report no-op just because a
   file with that name exists.
8. **Completion claimed from artifact existence** instead of checking it actually answers the
   requested decision layer.
9. **Execution state reconstructed from chat history** instead of an explicit current frame.
10. **A compound/underspecified task expands** into multiple artifacts or unauthorized targets — one
    atomic task per call.
11. **Execution continues after a HALT/CLARIFY/failed validation** — hard stop, not a warning.

*On-demand only (open when the task needs it): `TEMPLATES.md` (512 lines — prompt/workflow row
shapes and handoff forms); the appendices (`APPENDIX_KB_EXAMPLES.md`,
`APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`, `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` exist
in this checkout; most others referenced by BEST_PRACTICES/MISTAKES do not and should be treated as
historical pointers, not live paths).*
