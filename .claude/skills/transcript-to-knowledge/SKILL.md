---
name: transcript-to-knowledge
description: Deterministically prepare Whisper, faster-whisper, WhisperX, SRT, VTT, or plain-text transcripts for Macro/Meso/Micro knowledge compilation with stable quote/timestamp anchors, bounded chunks, semantic task planning, Obsidian-style wiki links, and fact-verification hooks. Use when converting transcripts, podcasts, interviews, meetings, lectures, or videos into source-grounded Apex KB/wiki knowledge while preserving exact provenance and avoiding duplicated raw context.
---

# Transcript To Knowledge

Normalize first; reason second. Keep source evidence deterministic and semantic synthesis explicitly model-owned.

## Workflow

1. **Prepare the transcript deterministically.**
   - Run `scripts/prepare_transcript.py prepare <input> --output <dir>`.
   - On Windows, prefer `scripts/prepare-transcript.ps1`.
   - Preserve generated `manifest.json`, `transcript.json`, `transcript.md`, `chunk-index.json`, `task-plan.json`, and `chunks/` unchanged as source evidence.

2. **Inspect the manifest before semantic work.**
   - If `timestamp_quality` is `none` or partial, never invent missing timing.
   - If speaker labels are absent, do not infer speaker identity from style alone.
   - If the source is too large, work chunk-first instead of loading the whole transcript.

3. **Compile Meso and Micro from bounded chunks.**
   - Read `references/knowledge-contract.md` for the epistemic/output contract.
   - Read `references/prompt-templates.md` and apply the **Meso** and **Micro** sections.
   - Preserve exact `seg-XXXXXX` anchors in every important derived statement and claim.
   - Deduplicate overlapping-chunk outputs before promotion.

4. **Compile Macro after Meso exists.**
   - Use validated Meso modules as the default Macro input.
   - Reopen raw transcript segments only for gaps, contradictions, or quote verification.
   - Apply the **Macro** section in `references/prompt-templates.md`.

5. **Verify only factual Micro claims that need verification.**
   - Use live web/research tools when available; otherwise keep `[UNVERIFIED]`.
   - Never fabricate URLs, DOIs, source titles, dates, quotes, timestamps, or verdicts.
   - Preserve disagreement and added context.

6. **Integrate with Apex KB without changing lifecycle authority.**
   - Treat prepared transcript artifacts as source inputs.
   - If Apex KB generated a semantic task packet, obey its allowlist and output path first.
   - Do not choose lifecycle stages, mutate Apex KB run state, or build a parallel KB compiler.

## Deterministic boundary

Use code for:
- source hashing;
- format parsing;
- timestamp/speaker preservation;
- stable anchors;
- chunk windows/overlap;
- task-plan generation.

Use a semantic worker for:
- thesis/taxonomy synthesis;
- thematic chaptering;
- argument/mechanism interpretation;
- atomic factual-claim identification;
- external verification judgments.

Do not describe semantic outputs or live search as deterministic.

## Validation

Run:

```bash
python scripts/test_prepare_transcript.py -v
```

Use `references/evals.md` for semantic and boundary regression scenarios.
