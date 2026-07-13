# Fable Orchestration — Completion Plan (lean)

## What this system is

The APEX orchestration system under `apex-meta/orchestration/` is a **deliverable**: agent
role-contracts, skills, workflows, schemas, and deterministic checks that the operator *activates*
to run real projects. When activated, the system dispatches its own agents — Alfred, Meta Strategy,
Meta Ops, Meta Detective, specialist lanes, and domain workers — in the designed way.

## Working mode for completing it

Whoever finishes this build is a **lean, token-aware, single-context working agent** that follows
this plan and the handover. It does **not** spawn the system's own agents to demonstrate or verify
the system — running the fleet live is what the operator does at activation time, not a build-time
task. Build-time validation is done by:

- inspection of the artifacts against their contracts, and
- the deterministic checks (`scripts/orchestration_check.py`, the negative fixtures under
  `apex-meta/orchestration/tests/negative/`, the resume test), and
- the behavioral evidence already captured in the two completed live simulations.

## Status

- **Built:** architecture; doctrine migration with distilled `CORE.md` operational cores; plan /
  sync / session integration; the review + correction loop; the enforcement script with five
  fail-closed negative fixtures and the resume test (all green).
- **Live behavioral evidence (sufficient):** `US-IDEA-01` and `US-SEQ-01` each ran the real
  dispatch → review → repair → operator-gate path once. The US-SEQ-01 review loop caught 3 genuine
  defects and forced a diff-proven v2. This proves the runtime pattern works.
- **Specified as validated designs:** the other five stories (MEDIA, LEELA, WORKSHOP, OFFER, COMP)
  are fully written, source-grounded workflows in `apex-meta/orchestration/user-stories/user-stories.md`.
- **Not done:** the final acceptance report; a manifest refresh.

## Remaining work (cheap, single-context, no fleet)

1. **Coverage check — inspection only.** For the five unexecuted stories, confirm each is
   contract-complete against `orchestrator-run.md` + `detective-review.md`: an owner per stage, a
   valid handoff shape, review-before-consequence, an operator gate, and named repair routes. Record
   honestly any capability a story *claims* that the two live runs do not yet evidence (e.g. parallel
   fan-out, a safety-gate hold, a cross-asset consistency report) as a stated limitation — do not
   run the fleet to close it.
2. **Acceptance report.** Write it honestly: two stories live-executed, five validated as designs;
   deterministic checks green; live execution of any story is an operator activation, not a build
   gate. No `true` without a file path behind it.
3. **Manifest refresh.** Regenerate `CURRENT-SYSTEM-MANIFEST.yaml` from the final files; validate
   every path.

## What NOT to do

- Do not spawn `meta-detective` / `meta-strategy` / lane / worker subagents to "run" or "measure"
  the system. That is runtime, and it is what burned the budget before.
- Do not re-run stories as live fleet orchestration to produce build-time evidence.
- No model-tier or per-role effort ceremony, and no token-budget "verification" of the fleet — those
  existed only to make expensive fleet runs affordable, and there are no expensive fleet runs.

## Local-only, autonomous

Save all outputs to the local filesystem under `apex-meta/orchestration/`. No git commit or push
unless the operator asks. Run to completion without stopping for per-step approval or model switches;
halt only for a genuinely missing required input or an unsafe write.
