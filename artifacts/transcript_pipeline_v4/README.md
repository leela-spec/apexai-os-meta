# Production Transcript Pipeline Artifacts & Benchmark Comparative Audit

This directory contains the authoritative transcript artifacts, intermediate outputs, and comparative benchmark logs for sources processed through the **`SourceTranscriptionAnalysisPipeline`**.

---

## 1. Infrastructure Overview

The production pipeline separates source processing into two cleanly decoupled layers:

```
[ YouTube URL / Local Audio ]
           │
           ▼ (yt-dlp + FFmpeg)
   [ source.m4a ]
           │
           ▼ (faster-whisper large-v3-turbo CPU int8 + VAD)
   [ transcript.txt + transcript.srt ]   <-- DETERMINISTIC LAYER (run_v4.ps1)
           │
           ▼ (Ar9av/obsidian-wiki / wiki-ingest)
   [ knowledge/transcript-wiki/ ]        <-- SEMANTIC LAYER (Host AI Agent Skill)
```

1. **Deterministic ASR Layer (`scripts/transcript_pipeline_v4/run_v4.ps1`)**:
   - **Audio Acquisition**: `yt-dlp` + `FFmpeg` converting audio stream to `source.m4a`.
   - **ASR Engine**: `faster-whisper` (`large-v3-turbo`, device `cpu`, compute_type `int8`, `vad_filter=True`) via `transcribe.py`.
   - **Outputs**: Clean UTF-8 `transcript.txt`, timestamped `transcript.srt`, `run.log`, and `source.info.json`.
   - **Reuse**: 100% deterministic skip of media download and ASR transcription on existing outputs.

2. **Semantic Knowledge Layer (`Ar9av/obsidian-wiki` / `wiki-ingest`)**:
   - **Target Vault**: Cumulative Obsidian knowledge vault at `knowledge/transcript-wiki/`.
   - **Transformation**: Host AI agent distillations into atomic concept notes (`concepts/`), entity notes (`entities/`), and source reference notes (`references/`).
   - **Incremental Caching**: SHA-256 content hashing in `.manifest.json` via `obsidian-wiki cache-check` (skips LLM inference on unchanged sources).
   - **Vault Health**: Enforced via `obsidian-wiki lint` (0 broken links) and `obsidian-wiki doctor`.

---

## 2. Benchmark Source Index & Directory Sitemap

| Source ID | Title / Domain | Duration | Transcript Size | Side-by-Side Tool Outputs Available | Folder Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`CygwqaNg2PY`** | Elliott Prechter Interview (Quant / Finance) | 16.5 min | 343 lines, 21.3 KB | `transcript.txt`, `knowledge_fabric_ollama.md`, `references/`, `concepts/` | [`CygwqaNg2PY/`](./CygwqaNg2PY/) |
| **`vFTuLylvYnA`** | Markus Koch Opening Bell (Market Monologue, German) | 12.1 min | 274 lines, 17.5 KB | `transcript.txt`, `knowledge_fabric_ollama.md`, `references/`, `concepts/` | [`vFTuLylvYnA/`](./vFTuLylvYnA/) |
| **`P-h5WSQG1Sw`** | Huberman Lab x Dr. Ralph Adolphs (Neurobiology Stress Test) | 2.5 hours | 1,471 lines, 141.9 KB | `transcript.txt`, `knowledge_ttk_v2_wiki.md`, `run.log` (Fabric 60m Timeout), `concepts/` | [`P-h5WSQG1Sw/`](./P-h5WSQG1Sw/) |
| **`NpxV8I8ZxXA`** | 3 Hours of Neville Goddard Wisdom (Metaphysical Long-Form) | 3.17 hours | 3,568 lines, 193.8 KB | `transcript.txt`, `transcript.srt`, `run.log`, `references/`, `concepts/`, `entities/` | [`NpxV8I8ZxXA/`](./NpxV8I8ZxXA/) |

---

## 3. Comparative Tool Analysis (Strengths, Weaknesses, Tradeoffs)

### Tool Version 1: Legacy Fabric + Ollama (`qwen3.5:9b`)
- **Mechanic**: Single-shot monolithic prompt (`extract_wisdom`) passed to local Ollama `qwen3.5:9b` (65k context length, `OLLAMA_HTTP_TIMEOUT=60m`).
- **Intermediate Files**: [`CygwqaNg2PY/knowledge_fabric_ollama.md`](./CygwqaNg2PY/knowledge_fabric_ollama.md), [`vFTuLylvYnA/knowledge_fabric_ollama.md`](./vFTuLylvYnA/knowledge_fabric_ollama.md).
- **Strengths**:
  - Extremely simple standalone setup.
  - Good summary formatting for short to medium inputs (<350 lines).
- **Weaknesses**:
  - **Severe Scaling Failure**: Failed and timed out (>60 minutes CPU execution) on transcripts exceeding 100k characters (e.g. `P-h5WSQG1Sw`).
  - **Siloed Outputs**: Produces a single isolated `knowledge.md` file without cross-source concept linking or entity disambiguation.
  - **Lack of Caching**: Re-ran expensive LLM inference on every pipeline call regardless of file modifications.

### Tool Version 2: Historical TTK / V2 Pipeline
- **Mechanic**: Earlier transcript-to-knowledge relay script.
- **Intermediate Files**: [`P-h5WSQG1Sw/knowledge_ttk_v2_wiki.md`](./P-h5WSQG1Sw/knowledge_ttk_v2_wiki.md), [`P-h5WSQG1Sw/knowledge_ttk_v2_wiki.json`](./P-h5WSQG1Sw/knowledge_ttk_v2_wiki.json).
- **Strengths**: Structured JSON outputs for mid-length audio.
- **Weaknesses**: Missed late-source details and lacked typed link relationships.

### Tool Version 3: Adopted Production `obsidian-wiki` (`wiki-ingest`)
- **Mechanic**: Host AI agent skill performing bounded reading across transcript partitions, distilling atomic markdown notes directly into `knowledge/transcript-wiki/`.
- **Outputs**: 44 cumulative pages across `references/`, `entities/`, and `concepts/`.
- **Strengths**:
  - **100% Long-Source Pass Rate**: Successfully distilled 3.17-hour long-form transcript (`NpxV8I8ZxXA`) with full multi-region coverage.
  - **Cross-Source Knowledge Fusion**: Automatically merged recurring concepts (e.g., linking Markus Koch's BofA sentiment survey data into Elliott Prechter's 5th wave terminal advance concept).
  - **Deterministic Caching**: `obsidian-wiki cache-check` skips unchanged sources in **5 seconds**.
  - **Integrity Verification**: `obsidian-wiki lint` ensures 0 broken links and full schema compliance.
- **Weaknesses**:
  - Requires a capable host AI model for distillation turn.

---

## 4. Areas for Future Improvement & System Recommendations

1. **GPU Acceleration for ASR**:
   - *Current State*: `faster-whisper` runs on CPU int8, requiring ~75 minutes for a 3.17-hour audio.
   - *Recommendation*: Support optional CUDA device targeting (`-Device cuda`) when NVIDIA GPU drivers are detected to reduce ASR time to <3 minutes.
2. **Automated Subtitle Alignment**:
   - *Current State*: Subtitles (`transcript.srt`) are generated during ASR.
   - *Recommendation*: Add deep-link line numbers from `transcript.srt` directly into the provenance section of concept notes (e.g., `sources: ["artifacts/transcript_pipeline_v4/NpxV8I8ZxXA/transcript.srt#L140-L160"]`).
