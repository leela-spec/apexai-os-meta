# V2 Production Architecture Selection Report

**Date:** 2026-08-18  
**Trial:** Trial 1 (Subscription-CLI Transport Lock)  
**Governing Authority:** `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/06-TRIAL1-TRANSPORT-LOCK.yaml`

---

## 1. Selected Production Composition

1. **Source Acquisition:** Retain existing `yt-dlp + ffmpeg` pipeline.
2. **ASR Engine:** `faster-whisper` (medium, int8 compute type) with word timestamps and VAD filter. (Local Intel Core Ultra 7 execution).
3. **Alignment / Diarization:** `WhisperX` as conditional stage for multi-speaker interview sources only.
4. **Evidence Custody & State:** `TTK` (Locked Core) for immutable source custody, segment IDs, processing windows, packet hashes, and deterministic validation.
5. **Map Extraction:** `direct_cli` via Claude Code subscription CLI with native JSON schema and TTK single-retry validation.
6. **Advisory Models:** `mDeBERTa-v3` (multilingual) and `Vectara-HHEM` (English) retained as non-blocking advisory lint warnings; semantic worker remains authoritative.
7. **Reduce Synthesis:** `direct_cli_reduce` via Claude Code subscription CLI over validated TTK evidence ledger.
8. **Selective External Verification:** Deterministic TTK queue routing only checkworthy factual claims (`checkworthiness >= medium`) to subscription CLI research.
9. **Compiler:** `TTK` compiler emitting structured Obsidian Markdown Wiki and `compiled.json`.

---

## 2. Rejection & Deferral Rationale

- **NVIDIA Parakeet:** Marked `BLOCKED` due to NeMo CUDA runtime requirements on Intel Arc integrated GPU hardware.
- **DocETL:** Marked `BLOCKED_FOR_TRIAL1` due to LiteLLM / direct API billing dependency.
- **DeepEval:** Marked `BLOCKED_FOR_TRIAL1` due to API judge requirements; deterministic and human rubrics are primary.
- **Instructor / NuExtract:** Marked `NOT_TRIGGERED` because native schema enforcement and direct CLI recall met all quality and reliability bars.
