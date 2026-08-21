# Source Artifact Audit: CygwqaNg2PY

## 1. Source Metadata
- **Source ID**: `CygwqaNg2PY`
- **Title**: Elliott Prechter Interview on Elliott Wave Theory, E-Waves, and Market Regimes
- **URL**: `https://www.youtube.com/watch?v=CygwqaNg2PY`
- **Language**: English (`en`)
- **Format**: Technical / Financial Interview Dialogue
- **Transcript Metrics**: 343 lines, 3,742 words, 21.3 KB (21,806 bytes)

---

## 2. ASR Transcription Details
- **Engine / Model**: `faster-whisper` (`large-v3-turbo`, device `cpu`, compute_type `int8`, `vad_filter=True`)
- **Acquisition Tool**: `yt-dlp` extracting audio stream converted to `m4a` via `FFmpeg`
- **Output Files**:
  - `transcript.txt` — Clean UTF-8 text strip of timestamps and cue numbers.
  - `transcript.srt` — Timestamped subtitle cues.
  - `run.log` — Timestamped execution facts log.
  - `source/source.m4a` & `source/source.info.json` — Raw media and yt-dlp metadata.

---

## 3. Transformation History & Tool Comparisons

### Mechanism 1: Legacy Fabric + Ollama (`qwen3.5:9b`)
- **Artifact**: [`knowledge_fabric_ollama.md`](./knowledge_fabric_ollama.md)
- **Configuration**: Fabric pattern `extract_wisdom`, vendor `Ollama`, model `qwen3.5:9b`, context length `65536`, `OLLAMA_HTTP_TIMEOUT=60m`.
- **Execution Time**: ~90 seconds.
- **Strengths**: Extracted structured sections (Summary, Ideas, Quotes, Facts) cleanly for short narrative.
- **Weaknesses**: Isolated Markdown file; no cross-source linking, no entity/concept decomposition, no frontmatter metadata, no incremental SHA-256 skip caching.

### Mechanism 2: Adopted Production `obsidian-wiki` (`wiki-ingest`)
- **Target Vault**: `knowledge/transcript-wiki/`
- **Artifacts Produced**: 11 pages (1 reference, 4 entities, 6 concepts).
  - Reference: [`references/elliott-prechter-interview-2026.md`](file:///c:/GitDev/apexai-os-meta/knowledge/transcript-wiki/references/elliott-prechter-interview-2026.md)
  - Entities: `elliott-prechter`, `robert-prechter`, `ralph-nelson-elliott`, `elliott-wave-international`
  - Concepts: `elliott-wave-principle`, `e-waves`, `fifth-wave-characteristics`, `flat-pattern`, `market-stationarity`, `nasdaq-bitcoin-divergence`
- **Strengths**: Atomic conceptual notes, typed frontmatter relationships (`implements`, `extends`), provenance tracking (`^[inferred]`), SHA-256 incremental skip (`cache-check`), zero broken links (`obsidian-wiki lint`).

---

## 4. Strengths, Weaknesses & Comparative Audit

| Evaluation Dimension | Legacy Fabric + Ollama | Production obsidian-wiki | Verdict |
| :--- | :--- | :--- | :--- |
| **Output Structure** | Single isolated `knowledge.md` summary | 11 interconnected wiki pages | **obsidian-wiki Superior** |
| **Cross-Source Knowledge** | Impossible (siloed per run) | Compounds across vault notes | **obsidian-wiki Superior** |
| **Incremental Caching** | Re-executes LLM on every run | SHA-256 manifest skip (`cache-check`) | **obsidian-wiki Superior** |
| **Vault Integrity** | Unvalidated markdown text | Validated via `lint` and `doctor` | **obsidian-wiki Superior** |
