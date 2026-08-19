# S02 — ASR and ASR Selection

**Execute only S02, then stop.**  
**Input from:** S01  
**Next:** S03

## Outcome

Produce a genuine timestamped transcript from the real S01 audio and make a bounded, evidence-based first ASR choice for this hardware/source mix.

## Context to load

- this file;
- S01 handoff and real audio;
- existing P1 `transcribe_audio.py` and its direct helpers;
- only the `asr_faster_whisper` and `asr_parakeet` registry entries;
- existing ASR gold/difficult slices only if already present and trustworthy.

Do not read semantic Map/Reduce plans.

## Recommended route

**Reference:** calibrated faster-whisper.  
**Required bounded challenger:** NVIDIA Parakeet TDT 0.6B v3 when it can be installed/run on this Windows/Intel machine without destructive changes.

Do not install every ASR technology. OpenVINO/whisper.cpp are later triggers, not first-stage requirements.

## Input

Real audio path/hash from S01.

## Work

1. Verify audio SHA matches S01 handoff.
2. Reuse or isolate the existing faster-whisper environment.
3. On a short representative/difficult slice, compare the smallest practical faster-whisper configurations required by existing V2 research (at minimum current reference plus the next quality step; base/small/medium where feasible).
4. If Parakeet is practical in an isolated environment, run the same slice. If not, record `BLOCKED` for the challenger with the actual install/runtime reason; do not simulate it.
5. Compare observable transcript quality on named/domain terms, numbers, EN/DE fidelity, timestamps, and runtime. Use human/source gold only where it exists; otherwise label quality judgments qualitative/UNMEASURED rather than inventing WER.
6. Choose the smallest/fastest configuration that is adequate for the first implementation.
7. Transcribe the full S01 audio with the selected engine/config.

## Required transcript artifacts

Prefer:

```text
<run>/asr/transcript.json   # segments + timestamps + diagnostics
<run>/asr/transcript.srt
<run>/asr/transcript.txt
<run>/asr/selection.yaml
```

For faster-whisper, preserve available diagnostics such as word timestamps/probabilities, avg_logprob, no_speech_prob, compression_ratio, temperature, VAD/config. Do not invent fields the selected engine did not expose.

## Tests

- transcript is produced by a real ASR invocation against S01 audio;
- transcript text is not copied from the old benchmark SRT;
- segment timestamps are monotonic and within audio duration tolerance;
- transcript contains meaningful speech, not a header/placeholder;
- JSON/SRT/TXT represent the same run;
- selected engine/model/config and version are recorded;
- source audio SHA is linked in ASR metadata;
- a known difficult slice is manually/algorithmically inspected for names/numbers/domain terms;
- failure does not create a fake completed transcript.

## Acceptance

PASS requires a real full transcript suitable for TTK ingestion plus an explicit first ASR selection rationale. The challenger may be BLOCKED without failing the core stage if faster-whisper is real and adequate.

## Outputs / handoff

Save transcript files, calibration notes/scorecard, selection, and `S02.yaml`/`S02-HANDOVER.md`.

Handoff must state selected engine/model/config, transcript path/hash, language, segment count, audio hash, runtime if measured, challenger status, known transcription weaknesses, and the exact artifact S03/S04 should consume.

## Git

Commit code/config/test changes and small scorecards; preserve large model/audio artifacts according to repo policy. Push before handover.

Then **STOP. Do not run WhisperX or TTK.**