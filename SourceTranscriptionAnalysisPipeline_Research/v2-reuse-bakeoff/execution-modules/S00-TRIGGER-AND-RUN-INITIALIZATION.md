# S00 — Trigger and Run Initialization

**Execute only S00, then stop.**  
**Previous:** none  
**Next after orchestrator approval:** S01

## Outcome

Create one explicit V2.1 run request and run directory from a real operator/APEX/OpenClaw-style source request. This stage establishes identity/state only; it must not acquire media, transcribe, or perform semantics.

## Context to load

Read only:

- this file;
- `../10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md` sections covering product target and S0;
- current `scripts/transcript_pipeline_v2/runner.py`;
- current `git status`.

Do not load V1, future stage files, failed-run reports, or the full benchmark plan.

## Input

One request containing at least one source locator:

- URL; or
- local media path; or
- transcript path when running transcript-only semantic regression.

Also accept optional source ID, requested language, title, and mode (`fresh_e2e|existing_transcript|regression`).

## Tool / implementation

Use the thin deterministic V2 runner. No LLM is required.

Implement or repair a command such as:

```powershell
python scripts/transcript_pipeline_v2/runner.py init-run --source <locator> --mode <mode>
```

The exact CLI spelling may differ if the current runner already has a suitable interface; prefer extending the existing runner rather than creating a second orchestration framework.

The runner must:

1. verify repository/branch assumptions needed for a run;
2. create a unique `run_id`;
3. create `artifacts/transcript_pipeline_v2/runs/<run_id>/`;
4. write `request.json` containing only operator-declared/request-derived facts;
5. create the standard subdirectories required by later stages, without creating fake outputs;
6. record start Git SHA and any pre-existing unrelated dirty paths;
7. write S00 handoff.

Do not invent source metadata not yet acquired.

## Tests

Add/run focused tests for:

- URL request accepted;
- local-path request accepted only when path exists;
- missing source rejected;
- invalid mode rejected;
- run IDs do not collide;
- initialization does not create ASR/Map/Reduce fake result files;
- request serialization round-trips.

Run the relevant V2 harness tests and `git diff --check`.

## Acceptance

PASS only if a real run directory exists and `request.json` accurately represents the supplied request with no later-stage claims.

## Outputs to save

- `artifacts/transcript_pipeline_v2/runs/<run_id>/request.json`
- `artifacts/transcript_pipeline_v2/runs/<run_id>/handoffs/S00.yaml`
- `artifacts/transcript_pipeline_v2/runs/<run_id>/handoffs/S00-HANDOVER.md`

The S00 handoff must include `run_id`, source locator/type, mode, start HEAD, dirty paths, and the exact request path.

## Git

If runtime code changed and tests pass, commit/push only S00 changes with a message such as:

`feat(transcript): implement V2.1 run initialization`

## Final response to operator

Return only: stage status, run ID, commit SHA if any, tests, output paths, blocker/limitation, handoff path.

Then **STOP. Do not acquire the source.**