# Transcript-to-Knowledge V3 — START HERE

**Status:** PRIME ARCHITECTURE SELECTED — READY FOR IMPLEMENTATION PLAN REVIEW  
**Date:** 2026-08-19  
**Repository:** `leela-spec/apexai-os-meta`  
**Branch policy:** `main` only unless the operator explicitly changes it

## Mission

Implement the selected proven-component transcript-to-knowledge path with the **smallest custom integration necessary** and prove it on real EN/DE sources.

Architecture discovery is complete. Do not restart the old V3 candidate-discovery modules unless a real implementation reversal trigger is reached.

## Authority order

1. current explicit operator instruction;
2. `../00-CURRENT-AUTHORITY.md`;
3. this file;
4. `06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md`;
5. `CURRENT-WORK.md`;
6. `01-V3-ARCHITECTURE.md` for target/anti-drift rationale;
7. `03-V3-BENCHMARK-AND-TEST-SPEC.yaml` for the retained three-source product corpus and product-quality concepts;
8. all earlier V3 discovery files and V1/V2/V2.1 material as historical evidence only.

## Selected production path

```text
URL / local media / existing transcript
  -> yt-dlp when remote
  -> FFmpeg only when normalization is needed
  -> trustworthy transcript OR ElevenLabs Scribe v2
  -> thin canonical source/text/time contract
  -> LangExtract 1.6.0 targeted multi-pass grounded extraction
  -> Gemini 3.7 Flash full-source global synthesis
  -> deterministic span checks + bounded semantic support review
  -> optional separate external verification
  -> deterministic Markdown/JSON compiler
```

Conditional only when real video content requires it: Gemini visual-evidence pass.

NotebookLM is a whole-product baseline for comparison, not the production dependency.

## Executor

Use **Antigravity CLI directly** for implementation.

Do not block product implementation on OpenClaw. OpenClaw may later invoke the proven CLI mechanically, but relay/orchestration work is deferred until the CLI product itself works.

## Non-negotiable implementation rules

1. **TARGET dominates.** Optimize for the efficient, resilient and credible path to the user-facing knowledge artifact.
2. **Reuse before build.** Try the selected existing system or existing repo utility before creating a replacement abstraction.
3. **Product before infrastructure.** Before the first real vertical slice, fix only blockers, product corruption, experiment invalidation, or material safety/data-loss risk.
4. **Two-strike rule.** Two corrective iterations on the same subsystem without product advancement => stop repairing and reconsider/replace/simplify.
5. **No sunk-cost authority.** Existing TTK/V2/V3 code survives only if it fits the selected responsibility.
6. **Every work unit advances product.** Run something real, learn something material about product quality, or directly move toward the target.
7. **Evidence proportionality.** Do not build more verification machinery than the risk/value justifies.
8. **Stop on drift.** If work becomes mainly orchestration, schemas, wrappers, provenance, receipts or test infrastructure, stop and return to the shortest product path.
9. **Minimalism.** Do only what the active work package requires.

## Current execution sequence

Implementation work packages are defined in `06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md`:

- `P00` — provider/runtime preflight + ruthless existing-code reuse audit;
- `P01` — first real existing-transcript -> knowledge vertical slice;
- `P02` — source-support gate + targeted repair;
- `P03` — add Scribe v2 media input + deterministic span-to-time mapping;
- `P04` — add URL acquisition with yt-dlp; FFmpeg only if needed;
- `P05` — add the smallest useful resumability manifest;
- `P06` — conditional visual evidence only when a real source proves the need;
- `P07` — optional external factual verification only after source-grounded product passes;
- `P08` — three-source E2E product proof + NotebookLM comparison.

One work package = one fresh Antigravity context. Do not execute all packages in one giant context.

## Required final product

One command must accept a supported URL, local media file, or existing transcript and produce at minimum:

```text
manifest.json
source/source.json
source/source.txt
source/transcript.json
evidence/evidence.jsonl
synthesis/synthesis.json
synthesis/support-review.json
output/knowledge.json
output/knowledge.md
```

The product succeeds only if the actual knowledge artifact is useful, source-specific, traceable, preserves important mechanisms/caveats/corrections/uncertainty, works in EN and DE, and reruns without manual surgery.

## Current next action

Review the implementation plan. After operator approval, start `P00` only in a fresh Antigravity CLI context.
