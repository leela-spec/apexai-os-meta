# Source Artifact Audit: NpxV8I8ZxXA

## 1. Source Metadata
- **Source ID**: `NpxV8I8ZxXA`
- **Title**: 3 Hours of NEVILLE GODDARD Wisdom To Fall Asleep To
- **URL**: `https://www.youtube.com/watch?v=NpxV8I8ZxXA&pp=ygUhMyBob3VycyBvZiBuZXZpbGxlIGdvZGRhcmQgd2lzZG9t`
- **Channel / Uploader**: `Neville Goddard Explained`
- **Upload Date**: `2026-06-20`
- **Duration**: `11,419` seconds (~190.32 minutes / 3.17 hours)
- **Language**: English (`en`)
- **Format**: Long-Form Philosophical & Metaphysical Lecture Collection
- **Transcript Metrics**: 3,568 lines, 33,776 words, 193.8 KB (193,771 bytes)

---

## 2. ASR Transcription Details
- **Engine / Model**: `faster-whisper` (`large-v3-turbo`, device `cpu`, compute_type `int8`, `vad_filter=True`) via `scripts/transcript_pipeline_v4/transcribe.py`.
- **Acquisition Tool**: `yt-dlp` extracting audio stream converted to `m4a` via `FFmpeg`.
- **Performance Metrics**:
  - Download & FFmpeg Conversion: 3m 30s (`source/source.m4a`, 50.9 MB).
  - ASR Offline Transcription: ~75 minutes on CPU int8.
  - Zero Cloud Tokens Spent (100% local free execution).
- **Output Files**:
  - `transcript.txt` — Clean UTF-8 text (3,568 lines, 193.8 KB).
  - `transcript.srt` — Timestamped subtitle cues (3,568 cues, 331.8 KB).
  - `run.log` — Detailed stage execution log.
  - `source/source.m4a` & `source/source.info.json` — Media & yt-dlp metadata.

---

## 3. Transformation History & Tool Comparisons

### Mechanism 1: Legacy Fabric + Ollama (`qwen3.5:9b`)
- **Status**: Retired prior to this run due to proven 60m timeout failure on long sources (>100k characters).

### Mechanism 2: Adopted Production `obsidian-wiki` (`wiki-ingest`)
- **Target Vault**: `knowledge/transcript-wiki/`
- **Artifacts Produced**: 11 pages (1 reference, 2 entities, 8 concepts).
  - Reference: [`references/neville-goddard-wisdom-compilation.md`](file:///c:/GitDev/apexai-os-meta/knowledge/transcript-wiki/references/neville-goddard-wisdom-compilation.md)
  - Entities: `neville-goddard`, `abdullah`
  - Concepts: `law-of-assumption`, `falling-backward-technique`, `state-akin-to-sleep`, `morning-revision-protocol`, `inner-conversations`, `feeling-as-causal-state`, `bridge-of-incidents`, `sabbath-of-assumption`
- **Multi-Region Coverage Verification**:
  - **Early Region** (Lines 0–713): Somatic falling backward technique, sensory ego surrender, Abdullah's Barbados instruction.
  - **Middle Region** (Lines 713–2139): 20-minute morning revision protocol, emotional naturalization, daytime inner conversations.
  - **Late Region** (Lines 2139–3568): Feeling as causal state, autonomous bridge of incidents, Sabbath of assumption (refraining from checking bank accounts or testing the law).
- **Idempotency & Reuse Verification**:
  - Rerun of `run_v4.ps1` completes in **5 seconds** (reusing existing media and transcript).
  - `obsidian-wiki cache-check` returns `unchanged`, skipping LLM inference with **0 duplicate pages created**.

---

## 4. Vault Health & Retrieval Audit
- `python -m obsidian_wiki lint knowledge/transcript-wiki`: **PASS** (44 pages, 319 links, 0 broken links, 0 schema errors).
- `python -m obsidian_wiki doctor`: **PASS** (all 12 agent installs provisioned).
- `obsidian-wiki query` Retrieval Precision: **100% (6/6)** across targeted multi-region queries.
