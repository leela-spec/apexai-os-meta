# M02 — ASR and Transcript Baseline (Conditional)

## RUN THIS MODULE ONLY IF

R1 concluded that the selected existing system/composition still needs a separately controlled transcript layer, or ASR quality is a measured product blocker.

If not needed, write `../results/M02-RESULT.md` with `SKIPPED_NOT_NEEDED` and the R1 evidence reference. Do not benchmark ASR for curiosity.

## TARGET

Select the simplest reliable EN/DE ASR/transcript path that is good enough for the final knowledge product.

## Read only

- `../CURRENT-WORK.md`
- `../03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- ASR entries from `../04-V3-COMPONENT-REGISTRY.yaml`
- M01 result and R1 decision
- exact current acquisition/ASR code only when needed

## Candidates

Required if M02 runs:

- faster-whisper reference;
- NVIDIA Parakeet TDT 0.6B v3 challenger.

Conditional:

- WhisperX only when multi-speaker attribution or alignment is demonstrated to matter.

## Fixture

Use 9 difficult clips by default:

- 3 from `P-h5WSQG1Sw`;
- 3 from `CygwqaNg2PY`;
- 3 from `vFTuLylvYnA`.

Include names/domain terms/numbers/difficult acoustics where applicable.

Do not run the full knowledge pipeline for each ASR candidate.

## Required evidence

- actual installed package/model revision;
- identical audio clips per comparison;
- language/VAD/decoding settings;
- human-checked domain terms and numbers;
- timestamp utility;
- measured runtime;
- install/runtime stability.

WER is optional unless a real human reference is good enough.

## Selection rule

Choose the smallest/most reliable candidate that clears the product-relevant quality floor. Speed cannot compensate for material term/number errors.

A more complex ASR wins only if the quality gain is visible in the benchmark.

## Output

- `../results/M02-ASR-COMPARISON.md`
- exact transcript/clip outputs used for scoring
- `../results/M02-RESULT.md`

End with one:

- `PASS: SELECT_FASTER_WHISPER`
- `PASS: SELECT_PARAKEET`
- `PASS: SELECT_OTHER_PROVEN_ASR`
- `APPROACH_SUSPECT`
- `BLOCKED`
- `SKIPPED_NOT_NEEDED`

## Two-strike rule

Two integration repair rounds on one candidate without producing comparable transcript output => stop repairing that candidate and record the failure.
