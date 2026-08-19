# S01 — Source Acquisition

**Execute only S01, then stop.**  
**Input from:** S00  
**Next after orchestrator approval:** S02

## Outcome

Materialize the **real source media/audio and source metadata** needed by downstream ASR. No synthetic audio marker, copied transcript, or old artifact may be labeled fresh acquisition.

## Context to load

- this file;
- S00 handoff + `request.json`;
- the existing P1 acquisition/downloader code directly responsible for yt-dlp/ffmpeg;
- relevant `source_existing` component-registry entry only if implementation detail is unclear.

Do not load ASR/Map/Reduce files.

## Input

- source locator from S00;
- run root;
- mode.

For `fresh_e2e`, this stage must start from the declared URL/local media and create a new materialized source artifact for this run.

For `existing_transcript`, record `SKIPPED_CONDITIONAL` and point S02/S04 to the declared transcript path; do not pretend acquisition occurred.

## Recommended tool

Reuse the existing P1 path using real `yt-dlp` + `ffmpeg`. Do not write a downloader framework.

Recommended artifact layout:

```text
<run>/source/source.json
<run>/source/audio.<actual-ext>
<run>/source/acquisition.log
```

`source.json` should include observable values such as source locator/ID, acquired filename, bytes, SHA256, duration when measured, acquisition tool versions, and command mode with secrets absent.

## Work

1. Verify S00 handoff status is PASS.
2. Locate the existing acquisition implementation; reuse it where possible.
3. Execute the real external downloader/transcoder.
4. Preserve the actual produced audio file.
5. Hash the audio bytes.
6. Record source metadata obtained from the tool/source, not guessed from prior artifacts.
7. Save concise stdout/stderr or log sufficient to diagnose acquisition failure.

## Tests

- produced audio file exists and size is non-trivial;
- SHA256 is computed from that file;
- `ffprobe`/equivalent can decode metadata and duration where available;
- source ID/locator matches the request;
- rerunning into a new fresh run does not silently reuse a previous run's audio while claiming fresh acquisition;
- failure exits non-zero/records FAIL rather than creating placeholder bytes.

A byte string such as `FRESH_AUDIO_STREAM...` is an automatic FAIL.

## Acceptance

PASS only when downstream S02 can open the real media/audio file produced here.

## Outputs

- real audio/media artifact under `<run>/source/`;
- `<run>/source/source.json`;
- `<run>/source/acquisition.log` when useful;
- `<run>/handoffs/S01.yaml` and `S01-HANDOVER.md`.

Handoff must contain exact audio path, SHA256, byte size, measured duration if available, acquisition tool/version, and whether this was truly fresh or explicitly skipped for transcript-only mode.

## Git

Runtime code fixes may be committed after tests. Do not commit huge source media if repository policy intentionally excludes it; if media is untracked by design, handoff must still record its exact local path/hash and explain retention. Commit metadata/test/code required to reproduce the acquisition.

## Final response

Return status, source/audio path, hash, duration, tool/version, tests, commit SHA, handoff path. Then **STOP.**