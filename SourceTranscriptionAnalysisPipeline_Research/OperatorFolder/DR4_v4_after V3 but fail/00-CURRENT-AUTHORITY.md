# CURRENT TRANSCRIPT-PIPELINE AUTHORITY

**Current architecture:** V3 — PRIME RECOMMENDATION SELECTED  
**Date:** 2026-08-19  
**Execution status:** IMPLEMENTATION PLAN READY FOR OPERATOR REVIEW

## Current implementation authority

Start here:

`SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/00-START-HERE.md`

The current implementation authority is:

1. current explicit operator instruction;
2. `v3-proven-infrastructure/00-START-HERE.md`;
3. `v3-proven-infrastructure/06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md`;
4. `v3-proven-infrastructure/CURRENT-WORK.md`;
5. `v3-proven-infrastructure/01-V3-ARCHITECTURE.md` for the product target and anti-drift rationale only;
6. `v3-proven-infrastructure/03-V3-BENCHMARK-AND-TEST-SPEC.yaml` where it does not conflict with the selected production plan.

## Architecture selection is complete

The supplied 2026-08-19 Transcript -> Knowledge Production Decision Package selected the production direction:

```text
yt-dlp / local input
  -> FFmpeg only when needed
  -> trustworthy transcript OR ElevenLabs Scribe v2
  -> canonical source package
  -> LangExtract 1.6.0 multi-pass grounded extraction
  -> Gemini 3.7 Flash global synthesis
  -> source-support gate
  -> optional external factual verification
  -> deterministic compiler
  -> knowledge.md + knowledge.json + evidence.jsonl + source.json
```

NotebookLM is the whole-product comparison baseline, not the production engine.

## Superseded execution authority

Do **not** execute:

- V2/V2.1 `S00-S14`;
- V3 discovery/orchestration modules `M00-M05` before implementation;
- the old `02-V3-IMPLEMENTATION-PLAN.md` as an active discovery sequence;
- `04-V3-COMPONENT-REGISTRY.yaml` as an invitation to reopen candidate selection.

Those files remain historical research/evidence only.

The implementation executor is **Antigravity CLI directly on `main`**. OpenClaw is not a prerequisite; it may be added later only as a thin mechanical invocation layer after the product CLI works.
