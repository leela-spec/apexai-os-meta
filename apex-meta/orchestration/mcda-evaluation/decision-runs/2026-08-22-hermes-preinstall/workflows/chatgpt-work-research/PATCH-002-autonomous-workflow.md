# PATCH-002 — Autonomous ChatGPT Work research program

Status: **PATCH SPECIFICATION / APPLIED IN SAME CHANGESET**

This patch corrects the prior operator-in-the-loop workflow. R01/R02 are dependency roots, not approval checkpoints. The Work program now executes R01-R07 autonomously and pauses only for genuine decision gates or unavoidable product permission prompts.

## PATCH INSTRUCTION FORMAT — EXACT-MATCH BLOCK REPLACEMENT

### PROJECT-INSTRUCTIONS.md

```text
/Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/PROJECT-INSTRUCTIONS.md
<OLD>
Before execution:

1. inspect the task specification;
2. enter Plan mode when available;
3. propose a concise plan covering repo inputs, official sources, decision questions and output;
4. identify any ambiguity that would materially change the result;
5. wait for operator approval before doing consequential work.
</OLD>
<NEW>
At program start:

1. inspect all seven R01-R07 specifications;
2. build the dependency graph;
3. use Plan mode internally when available;
4. continue execution without waiting for routine plan approval;
5. run independent roots in parallel when Work natively supports it, otherwise sequence them autonomously.
</NEW>
```

```text
/Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/PROJECT-INSTRUCTIONS.md
<OLD>
After evidence review and operator acceptance, write the accepted result through the GitHub plugin under:

`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/`

Do not modify architecture state, authorize installation or change other project files unless the operator explicitly asks.
</OLD>
<NEW>
After a track passes its evidence review, write the accepted result through the GitHub plugin under:

`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/`

This designated result persistence is autonomous unless the product UI itself requires explicit confirmation.

Do not modify ADR-002, authorize installation, install software, migrate project data, or change production architecture without an explicit operator decision.
</NEW>
```

### state.yaml

The existing `state.yaml` is replaced by schema version 2 because the control semantics change from per-track human approval to an autonomous dependency-graph program. The exact replacement is the committed file body. No research result, ADR, installation state, or production system is changed by this patch.

## New authoritative launcher

Added:

`Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/AUTONOMOUS-PROGRAM-LAUNCHER.md`

The previous `WORK-RESEARCH-LAUNCHERS.md` remains available only for recovery/manual reruns of an individual track.