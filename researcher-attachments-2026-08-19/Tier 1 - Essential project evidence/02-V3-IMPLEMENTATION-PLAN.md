# Transcript-to-Knowledge V3 — Implementation Plan

**Status:** AUTHORITATIVE IMPLEMENTATION PLAN  
**Date:** 2026-08-19  
**Architecture:** `01-V3-ARCHITECTURE.md`

## 0. Implementation philosophy

This plan is intentionally **module-level, not micro-stage-level**.

One module = one fresh Antigravity context. Within that module the executor is expected to perform normal software/research iteration until the module succeeds, hits a real blocker, or triggers the two-strike stop-loss.

Do not return to ChatGPT after every test failure.

Do not implement modules merely because they exist. If a proven end-to-end system wins early, skip unnecessary component work.

## 1. Module/result contract

Each module produces:

```text
SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/results/Mxx-RESULT.md
```

Minimal result content:

- module ID/status;
- exact product/research target;
- what real systems/tools were run;
- exact versions/commits when observable;
- artifacts produced;
- tests/benchmarks actually executed;
- product-relevant findings;
- blocker/limitations;
- `NEXT: <module|REVIEW_GATE|STOP>`.

No large handoff schema is required.

Git commit(s) are the durable handoff.

## M00 — Prove OpenClaw -> Antigravity relay while doing useful work

### Goal

Prove the relay can supervise Antigravity **and** produce one real product-advancing artifact.

### Required actions

1. Inspect installed OpenClaw and `agy` versions; do not assume repository docs equal machine state.
2. Verify OpenClaw has usable `exec`/`process` semantics, including PTY if needed.
3. Run non-mutating Antigravity headless smoke:
   - prompt supplied explicitly;
   - output captured;
   - exit status captured;
   - no hanging permission prompt.
4. If headless is safe, use it. Otherwise start normal `agy` with PTY and supervise it through OpenClaw process controls.
5. Use that same Antigravity session to create a small **current-proven-systems inventory** from live primary-source research and save it under V3 results.
6. Commit the useful inventory on `main`.

### Guardrails

- No custom ACP adapter.
- No browser relay to ChatGPT.
- No new queue/state database.
- Do not alter the existing protected `apex-executor` role unless an explicit operator decision says so; prefer a separate narrow relay profile/agent or bounded direct OpenClaw invocation.
- One relay repair cycle only.

### Acceptance

PASS only if:

- OpenClaw actually launched/supervised Antigravity;
- Antigravity produced a useful repo artifact from real research;
- a real commit exists on `main`;
- no dangerous global permission bypass was required.

If relay fails twice, mark `RELAY_FALLBACK_DIRECT_AGY` and continue later modules by direct Antigravity launch using the same module files.

## M01 — Proven systems landscape + runnable baseline bake-off

### Goal

Answer the question V2.1 skipped:

> Is there already a maintained end-to-end or near-end-to-end system we can adopt/fork instead of composing our own pipeline?

### Research scope

Search current primary repositories/documentation broadly for systems covering substantial portions of:

`video/audio -> transcript -> grounded notes/knowledge/wiki -> citations/timestamps`

Do not limit discovery to the V2 component list.

### Required evidence

Build a landscape of roughly 10-20 credible candidates if the ecosystem supports it, then shortlist 3-5 based on:

- runnable path;
- maintenance/current activity;
- actual output examples;
- source/timestamp grounding;
- EN/DE viability;
- Windows/local viability where relevant;
- dependency burden;
- model/provider constraints;
- license;
- adaptation surface.

### Real run requirement

Run the strongest 2-3 candidates on **one representative source first**. Prefer `CygwqaNg2PY` because it is compact enough for fast iteration but technically specific enough to reveal generic-summary failure.

Only expand a candidate to the other two primary sources if its one-source result is genuinely promising.

### Existing baselines to include if still current/runnable

- Fabric transcript/wisdom patterns;
- Open Notebook as product/UI baseline;
- any near-complete transcript/video distillation project found/reverified in current search.

These are baselines, not automatic winners.

### Review Gate R1

ChatGPT independently reviews Git evidence and chooses exactly one path:

- **ADOPT/FORK EXISTING** -> skip M02-M04 as much as possible and go toward M05/M06;
- **SMALL COMPOSITION REQUIRED** -> run only the component modules needed by observed gaps;
- **INSUFFICIENT EVIDENCE** -> one bounded additional candidate run, not an architecture rewrite.

## M02 — ASR/transcript layer benchmark (conditional)

### Run only if

The selected near-complete system does not already provide an acceptable transcript layer, or ASR quality is a measured blocker.

### Candidates

Reference:
- faster-whisper, calibrated with word timestamps/VAD and source-specific hotword experiment where justified.

Challenger:
- NVIDIA Parakeet TDT 0.6B v3.

Conditional:
- WhisperX only when word alignment/speaker attribution materially improves the target artifact.

### Test scope

Use difficult **clips**, not full knowledge runs, from all 3 primary videos.

Default fixture budget:
- 3 clips per source = 9 clips total;
- include at least one proper-name/domain-heavy and one numeric/difficult-acoustic slice per source where applicable.

Measure only what has defensible references:
- manually reviewed word/domain-term accuracy;
- numbers/percentages;
- timestamps availability/utility;
- runtime;
- install/runtime stability.

### Decision

Promote the smallest/most reliable option that clears the product-relevant quality floor. Do not select by speed alone.

## M03 — Grounded extraction bake-off (conditional)

### Run only if

The chosen system still needs a grounded semantic extraction layer.

### Required lanes

1. direct strong CLI extraction control;
2. LangExtract with a real supported provider path/adapter if practical;
3. GLiNER2-assisted lane only if cheap pre-extraction plausibly reduces cost or increases recall.

Optional only after measured need:
- Instructor if typed/schema retry is brittle without it;
- NuExtract if GLiNER2 does not satisfy the intended auxiliary role.

### Fixture scope

Use **12 representative transcript windows total**:
- 4 from each primary video;
- include early/middle/late coverage plus one known difficult/domain-heavy window.

Use identical text packets across lanes.

### Evaluate

- important insight recall;
- exact/source grounding quality;
- unsupported overreach;
- uncertainty/caveat retention;
- entity/relation usefulness where relevant;
- retries/failures;
- integration/custom-code burden;
- token/runtime when actually measurable.

### Stop rule

If direct CLI is already strong and the extra framework does not materially improve quality, resilience, or custom-code reduction, remove the extra layer.

## M04 — Global synthesis / knowledge product bake-off (conditional)

### Run only if

A component composition remains necessary after M01/M03.

### Required comparison

Reference:
- direct strong CLI global synthesis over the same validated evidence/transcript material.

Challenger:
- DocETL fixed Map/Reduce or Reduce path **only if a compliant provider route is practical**.

Do not enable automatic optimizer/rewrite behavior in the first comparison.

### Full-product scope

Use one complete source first (`CygwqaNg2PY`). Expand to `P-h5WSQG1Sw` and `vFTuLylvYnA` only for finalists.

### Product dimensions

- source-specific thesis usefulness;
- important insight recall;
- semantic chapter/module coherence;
- procedures/mechanisms/warnings/examples retained;
- uncertainty preserved;
- timestamp/evidence traceability;
- generic boilerplate rate;
- unsupported claims;
- operator reading efficiency;
- operational complexity.

## M05 — Evaluation and architecture selection

### Goal

Select the **smallest proven production composition**.

### Evidence hierarchy

1. hard source/product failures;
2. human-checked important-insight/source-fidelity evidence;
3. repeatability/runtime/operational evidence;
4. semantic eval framework signals;
5. architectural elegance last.

### Evaluation tools

Use deterministic checks for deterministic properties.

Use human/gold review for product meaning.

Use DeepEval or another existing framework only as an auxiliary scoreboard where the judge/provider/language path is valid. It is never the sole pass authority.

Use Fabric/Open Notebook or other current turnkey outputs as product baselines when runnable.

### Review Gate R2

ChatGPT reviews the actual artifacts and freezes:

- selected system/project or composition;
- components retained;
- components explicitly rejected with evidence;
- exact remaining custom integration;
- final E2E acceptance command/runbook.

No further architecture expansion after R2 unless M07 reveals a genuine product blocker.

## M06 — Production integration

### Goal

Implement **only** what R2 selected.

### Rules

- delete/disable abandoned experimental hot-path code where safe;
- do not carry every benchmark candidate into production;
- preserve isolated benchmark environments only if still useful for regression;
- one thin user-facing runner/command;
- inputs: URL/media/transcript;
- outputs: canonical knowledge artifact + source references;
- normal implement -> run -> inspect -> repair loop inside the module.

### Custom-code gate

Every new abstraction must document:

- existing solution tried;
- observed gap;
- why configuration/forking was insufficient;
- smallest custom code added.

## M07 — Fresh three-source E2E and regression

### Goal

Prove the selected production path works from real source to final knowledge on the 3 primary videos.

### Required sources

- `P-h5WSQG1Sw`;
- `CygwqaNg2PY`;
- `vFTuLylvYnA`.

### Required checks

- fresh/current source acquisition or explicitly justified current transcript input according to the selected production design;
- no historical artifact passed off as fresh;
- real ASR if the production design owns ASR;
- real semantic execution;
- final knowledge artifact opens and is source-specific;
- source/timestamp references resolve;
- key expected insights/caveats/mechanisms are present;
- German output path works;
- rerun/recovery does not require manual artifact surgery.

### Optional fourth source

Run `oZIsMX6WgFs` only if:

- three-source evidence is ambiguous;
- procedural-recall coverage is a specific unresolved risk;
- or the final reviewer requests one holdout.

### Review Gate R3

Final verdict:

- `PRODUCTION_ACCEPTED`;
- `ONE_PRODUCT_REPAIR`;
- `ARCHITECTURE_REJECTED`.

If the same subsystem would require a third correction, prefer replacement/simplification over another patch.

## 2. Review cadence summary

| Module | Fresh Antigravity context | Default ChatGPT review? |
|---|---:|---:|
| M00 | yes | only if relay blocks |
| M01 | yes | **YES — R1** |
| M02 | yes | no unless blocker |
| M03 | yes | no unless blocker |
| M04 | yes | no unless blocker |
| M05 | yes | **YES — R2** |
| M06 | yes | no unless blocker |
| M07 | yes | **YES — R3** |

This keeps the context modular without making the operator a message bus after every small step.
