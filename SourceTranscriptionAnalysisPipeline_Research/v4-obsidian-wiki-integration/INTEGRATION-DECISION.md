# Integration Decision: Ar9av/obsidian-wiki Integration

## 1. Upstream Metadata
- **Package**: `obsidian-wiki` (GitHub: `Ar9av/obsidian-wiki`, https://github.com/Ar9av/obsidian-wiki)
- **Version Integrated**: `2026.8.4` (PyPI release)
- **Distribution Format**: Wheel / Pip (`obsidian_wiki-2026.8.4-py3-none-any.whl`)
- **Execution Runtime**: Python 3.12+ (Windows / POSIX compatible)

## 2. Decision & Verdict
- **Verdict**: **ADOPT**
- **Rationale**:
  1. Replaces the failing single-shot Fabric `extract_wisdom` / `qwen3.5:9b` bottleneck that timed out on long multi-speaker transcripts (`P-h5WSQG1Sw`).
  2. Demonstrates robust, cumulative knowledge accumulation across disparate domains (English financial interview, German market broadcast, and 140k-character neuroscience dialogue).
  3. Preserves fine-grained claims, exact numerical figures (e.g. 5.33% 30y yields, <3.5% cash reserves), and subtle qualifications without loss or hallucination.
  4. Provides instant deterministic incremental skip via SHA-256 manifest caching (`obsidian-wiki cache-check`).
  5. Built-in linting and trust ledger verification (`obsidian-wiki lint`, `obsidian-wiki doctor`) guarantee vault health with 0 broken links and 0 schema violations.

## 3. Architecture & Boundary Specification

### Unchanged Layers (Authoritative)
- **Acquisition**: `yt-dlp` / `ffmpeg` media intake.
- **ASR Transcription**: `faster-whisper` generating canonical `transcript.txt` and `transcript.srt`.
- **Artifact Custody**: `artifacts/transcript_pipeline_v4/<source_id>/` hierarchy.

### Replaced / Retired Layers
- **Retired**: Fabric `extract_wisdom` monolithic prompt.
- **Retired**: Hard dependency on local Ollama `qwen3.5:9b` execution for large document extraction.
- **Retired**: Isolated single-file `knowledge.md` summary dumps without cross-source linking.

### Integrated Target Pipeline
```
Media / URL
    ↓
V4 Acquisition (yt-dlp / ffmpeg)
    ↓
V4 ASR (faster-whisper)
    ↓
canonical transcript.txt / transcript.srt
    ↓
obsidian-wiki / wiki-ingest
    ↓
knowledge/transcript-wiki/
    ├── concepts/ (interconnected markdown notes)
    ├── entities/ (people, organizations, tools)
    ├── references/ (source attribution notes)
    ├── .manifest.json (SHA-256 delta cache)
    ├── index.md (content index)
    ├── log.md (audit log)
    └── hot.md (session cache)
```

## 4. Scope of Changes
- **Files Added**:
  - `knowledge/transcript-wiki/` (canonical knowledge base with 33 distilled markdown pages, manifest, trust ledger, index, and hot cache).
  - `SourceTranscriptionAnalysisPipeline_Research/v4-obsidian-wiki-integration/INTEGRATION-DECISION.md`
  - `SourceTranscriptionAnalysisPipeline_Research/v4-obsidian-wiki-integration/INSTALL-AND-RUN.md`
  - `SourceTranscriptionAnalysisPipeline_Research/v4-obsidian-wiki-integration/BAKEOFF-RESULT.md`
- **Files Modified**:
  - Project configuration and environment variables configured for vault path `knowledge/transcript-wiki`.
- **Preserved**:
  - All existing V1/V2/V3 research and V4 audio/transcript artifacts.
