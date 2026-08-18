# Evaluation Scenarios

Run these after changes to the skill or parser.

1. **WhisperX JSON:** word timestamps and speaker labels survive normalization exactly.
2. **SRT:** cue start/end become stable segment anchors; speaker prefixes are preserved when present.
3. **Untimed text:** no timestamp is invented; manifest reports partial/none timing.
4. **Overlap:** adjacent chunks share only the configured tail context and preserve source segment IDs.
5. **Determinism:** same input bytes + same chunk parameters produce byte-identical normalized artifacts.
6. **Quote grounding:** a Micro claim quote must be a verbatim substring of the cited segment or word span.
7. **Contradiction:** two speakers making opposing factual claims remain separate claims; no silent reconciliation.
8. **Opinion:** advice or preference does not become `[CONFIRMED]` merely because external sources agree.
9. **Verification unavailable:** all factual claims remain `[UNVERIFIED]`; no synthetic URLs/DOIs appear.
10. **Apex boundary:** when a generated Apex KB task packet limits sources/output paths, the skill does not widen them.
