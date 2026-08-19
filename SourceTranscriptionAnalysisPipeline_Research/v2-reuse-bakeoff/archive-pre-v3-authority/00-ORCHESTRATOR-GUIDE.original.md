# V2.1 Orchestrator Guide — One Module Per CLI Session

## Role split

**Operator:** starts a CLI session with the module packet and returns the result.  
**Execution CLI AI:** implements exactly one stage.  
**Orchestrator (ChatGPT):** decides whether the stage is accepted, requires repair, or is blocked; only the orchestrator authorizes moving to the next stage.

The execution AI is never allowed to self-promote to the next module.

## Why this exists

Prior attempts loaded too much architecture, test, corrective, and historical context into one agent session. The agent then optimized for finishing the giant instruction set rather than producing the real stage output. This protocol makes the file boundary enforce the context boundary.

## Session packet

For stage `Sxx`, give the execution AI only:

1. the full text/path of `execution-modules/Sxx-*.md`;
2. the previous stage handover `artifacts/transcript_pipeline_v2/runs/<run_id>/handoffs/Sxx-1.yaml` and its human summary, when one exists;
3. the exact files listed under **Context to load** in that module.

Do not preload:

- V1 architecture;
- all of `01-ARCHITECTURE-ANALYSIS.md`;
- all of `02-IMPLEMENTATION-PLAN.yaml`;
- all benchmark/evaluator artifacts;
- all failed-run reports;
- future stage files.

A module may explicitly request one narrow section/file when needed.

## Standard opening instruction to the CLI

Use this with every stage:

> You are executing exactly one V2.1 Transcript-to-Knowledge module. Read the supplied module completely and treat it as the direct execution authority for this session. Load only the context it names. Implement and test the stage on `main`, save the declared outputs and handoff, commit/push only stage-scoped changes when acceptance criteria pass, then STOP. Do not execute or plan the next stage. Do not substitute simulated software, internal-agent semantics, or synthetic inputs for a required real tool/model/CLI. If blocked, preserve the blocker truthfully and stop with the handover.

## Handoff contract

Every module must write:

`artifacts/transcript_pipeline_v2/runs/<run_id>/handoffs/Sxx.yaml`

and, for operator readability:

`artifacts/transcript_pipeline_v2/runs/<run_id>/handoffs/Sxx-HANDOVER.md`

Minimum machine handoff:

```yaml
schema: ttk.v2_1.stage-handoff.v1
stage: Sxx
status: PASS|FAIL|BLOCKED|SKIPPED_CONDITIONAL
run_id: <id>
start_head: <sha>
end_head: <sha-or-null>
inputs:
  - path: ...
    sha256: ...
components:
  - id: ...
    version: ...
    config: ...
outputs:
  - path: ...
    sha256: ...
tests:
  - command: ...
    result: PASS|FAIL
product_check: <what was inspected in the actual output>
limitations: []
unrelated_dirty_paths: []
next_stage_input:
  paths: []
  facts: []
```

No invented token counts, scores, versions, hashes, or PASS states.

## Orchestrator review after every stage

The orchestrator checks four things:

1. **Target:** did the required real output get created?
2. **Tool identity:** did the required actual external software/model/CLI run, rather than a substitute?
3. **Tests:** do the stage-specific tests exercise the real target rather than only a validator?
4. **Handoff:** is the exact output needed by the next stage present and clearly identified?

Possible orchestrator verdicts:

- `ACCEPT -> NEXT Sxx`
- `REPAIR SAME STAGE`
- `BLOCKED / OPERATOR DECISION`

## Git policy

- Work directly on `main`.
- Pull/fetch current `main` at module start.
- Preserve unrelated user changes.
- One module may produce one stage-scoped commit after its acceptance checks pass.
- A failed stage may commit useful diagnostic/code work only when the handoff clearly records `FAIL` or `BLOCKED`; never commit a fake final PASS to make progress look complete.
- Push before returning the handover so the orchestrator can inspect remote truth.

## First implementation strategy

The first pass is a **single real vertical slice** through S00-S14. Do not immediately multiply work across all four benchmark sources.

Once S14 accepts the vertical slice, reuse the same modules for:

- four-source semantic regression;
- fresh English E2E;
- fresh German E2E;
- real resume/invalidation demonstration.

These are repeated acceptance runs of the same production chain, not a second architecture implementation.