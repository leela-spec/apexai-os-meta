# S08 — Structured Output and Retry Seam

**Execute only S08, then stop.**  
**Input:** real S07 semantic route/results  
**Next:** S09

## Outcome

Make the real semantic worker seam reliable and explicit: native CLI structured output where available, bounded retry, deterministic validation, and **no heuristic/internal-agent fallback**.

## Context to load

- this file;
- S07 handoff;
- current `scripts/transcript_pipeline_v2/adapters/semantic_cli.py` and its tests;
- TTK Map/Reduce schemas/contracts;
- `06-TRIAL1-TRANSPORT-LOCK.yaml`;
- Instructor registry entry only if the trigger below fires.

Do not load ASR or future Reduce/evaluation history.

## Default design

Use provider-native structured output plus TTK validation:

- Claude Code CLI: strict JSON/schema mode when actually supported by the installed version;
- Codex CLI: `exec` plus output schema when actually supported;
- Antigravity: only after real headless smoke PASS, with truthful capabilities recorded.

The runtime must use subprocess argv arrays, bounded timeout, captured exit status, and a sanitized child environment that avoids unintended API-key/pay-as-you-go routing.

## Trigger for Instructor

Instructor is **not automatically added**. Test/add it only if one of these is demonstrated in the real seam:

- provider-native schema support is insufficient;
- retry/shape handling is duplicated across multiple selected providers;
- the adapter is materially simpler/safer with Instructor while still preserving the allowed CLI transport.

If Instructor cannot operate through the selected subscription CLI without changing transport, do not add it.

## Work

1. Audit the S07 route and remove/disable any production path that can report semantic success without launching an allowed external CLI.
2. Specifically ensure `antigravity_agent`, `agent_worker`, regex/template pseudo-semantics, or internal coding-agent routes cannot be selected as Trial-1 semantic providers.
3. Define one bounded retry policy: initial call plus at most one validation-informed retry for invalid JSON/schema/TTK invariant failure.
4. Append the exact validator error to retry context; do not broaden the task or silently switch providers.
5. On repeated failure, mark the packet failed/incomplete.
6. Preserve only compact execution metadata needed for diagnosis and proof of real transport.

## Tests

Unit/negative tests must prove:

- real-provider adapter builds subprocess argv rather than calling internal semantic functions;
- non-zero exit does not create PASS/result;
- malformed JSON triggers at most one retry;
- schema-invalid output triggers at most one retry;
- TTK invariant failure triggers at most one targeted retry;
- second failure remains failure;
- unavailable provider is BLOCKED, not replaced with heuristics;
- forbidden/missing transport cannot pass semantic execution;
- secrets are not written to logs/receipts.

Also rerun one small real S07 packet through the hardened seam and verify the output remains useful.

## Outputs

- hardened semantic adapter/tests;
- any synchronized schema files genuinely needed by the CLI;
- compact seam decision note under `<run>/evaluation/S08-structured-output.yaml`;
- S08 handoff.

Handoff must say actual provider/executable, structured-output mechanism actually used, retry policy, whether Instructor was triggered, negative tests executed, and exact production provider identifiers still allowed.

## Acceptance

PASS means **there is no production semantic success path that bypasses a real allowed CLI** and the real packet still works through the hardened seam.

Commit/push, return handoff, **STOP.**