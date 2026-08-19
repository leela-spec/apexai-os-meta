# S03 — Conditional Alignment and Diarization

**Execute only S03, then stop.**  
**Input:** S02 transcript + S01 audio  
**Next:** S04

## Outcome

Decide whether this source needs a separate alignment/speaker-attribution stage. If yes, test/use real WhisperX; if no, explicitly pass the S02 transcript through without adding a dependency.

## Context to load

- this file;
- S02 handoff/transcript;
- S01 audio path;
- only the WhisperX component-registry entry;
- current transcript/source metadata needed to determine speaker structure.

## Decision

WhisperX is **conditional**, not mandatory.

Run it when speaker identity or timing materially improves provenance for this source, especially interviews/multiple speakers. Single-speaker material may correctly produce `SKIPPED_CONDITIONAL`.

## Work if skipped

1. Record why speaker/alignment enrichment is unnecessary.
2. Set `canonical_transcript_candidate` to the S02 transcript.
3. Write the handoff. Do not create fake aligned output.

## Work if executed

1. Use an isolated WhisperX environment.
2. Run real forced alignment against the S01 audio and S02 transcript/ASR output as appropriate.
3. Enable diarization only when required and credentials/model access are legitimately available; never invent speaker names.
4. Preserve model/version/configuration.
5. Compare alignment/speaker output to S02 on a representative section.
6. Promote the aligned output only if it is actually more useful/reliable for downstream provenance.

## Tests

- timestamps remain monotonic/in audio bounds;
- words/segments map to actual audio/transcript content;
- speaker labels, if produced, are IDs unless identity is independently known;
- overlapping/ambiguous speech is not falsely presented as certain;
- no transcript content is silently rewritten semantically;
- if skipped, no WhisperX artifact is labeled PASS.

## Output

If promoted:

`<run>/alignment/aligned-transcript.json`

Always save:

`<run>/alignment/decision.yaml`
`<run>/handoffs/S03.yaml`
`<run>/handoffs/S03-HANDOVER.md`

Handoff must name exactly one `canonical_transcript_candidate` for S04 and state whether it is S02 ASR or promoted aligned output.

## Git

Commit only stage-specific adapter/test/config changes and decision artifact where appropriate. Push, return handoff, **STOP.**