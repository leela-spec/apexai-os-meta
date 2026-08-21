---
name: SourceTranscriptionAnalysisPipeline
description: End-to-end automated audio acquisition (yt-dlp), offline faster-whisper transcription, and obsidian-wiki cumulative knowledge compilation pipeline.
---

# SourceTranscriptionAnalysisPipeline

## 1. Overview
The **SourceTranscriptionAnalysisPipeline** orchestrates the end-to-end transformation of media URLs, local video/audio recordings, or raw caption files into a structured, interconnected Obsidian knowledge graph in `knowledge/transcript-wiki/`.

### Architecture & Runtime Separation
1. **Deterministic Layer (PowerShell & Python)**:
   - **Acquisition**: `yt-dlp` + `ffmpeg` for media stream extraction.
   - **ASR Transcription**: `faster-whisper` (`large-v3-turbo`, CPU `int8`, VAD enabled) via `scripts/transcript_pipeline_v4/transcribe.py`.
   - **Artifact Custody**: `artifacts/transcript_pipeline_v4/<source_id>/` storing canonical `transcript.txt`, `transcript.srt`, `run.log`, and source media.
2. **Semantic Layer (Host AI via `wiki-ingest` Skill)**:
   - **Knowledge Compilation**: Progressive distillation of concepts, entities, and source references into `knowledge/transcript-wiki/`.
   - **Delta Cache & Idempotency**: SHA-256 caching via `obsidian-wiki cache-check` / `cache-update`.
   - **Vault Health**: Automatic link integrity and schema validation via `obsidian-wiki lint` and `obsidian-wiki doctor`.

---

## 2. Directory Layout

```
.claude/skills/SourceTranscriptionAnalysisPipeline/
└── SKILL.md                               # This skill definition and operator manual

scripts/transcript_pipeline_v4/
├── run_v4.ps1                             # Deterministic acquisition and ASR runner
├── transcribe.py                          # Local faster-whisper engine
├── README.md                              # Runner documentation
└── tests/
    ├── test_run_v4.ps1                    # Deterministic behavioral test suite
    └── test_transcribe.py                 # Fast CLI interface test

artifacts/transcript_pipeline_v4/
└── <source_id>/                           # Per-source artifact directory
    ├── source/                            # Downloaded media and metadata JSON
    ├── transcript.txt                     # Canonical normalized UTF-8 text
    ├── transcript.srt                     # Subtitle cues with timestamps
    └── run.log                            # Stage and execution log

knowledge/transcript-wiki/                 # Cumulative Obsidian Knowledge Base
├── concepts/                              # Distilled concept notes
├── entities/                              # People, tools, organizations
├── references/                            # Source attribution notes
├── .manifest.json                         # SHA-256 source tracking manifest
├── index.md                               # Vault content index
├── log.md                                 # Cumulative ingestion log
└── hot.md                                 # Active session cache
```

---

## 3. Prerequisites & Tools
- **Python 3.10+** (with `faster-whisper` installed in environment)
- **`yt-dlp` & `ffmpeg`** (accessible on system `PATH` or in standard tools directory)
- **`obsidian-wiki` (v2026.8.4)**: `pip install -U obsidian-wiki`

---

## 4. End-to-End Execution Protocol

When a user requests to process a video or audio source into the knowledge base:

### Step 1: Deterministic Acquisition & ASR
Execute `scripts/transcript_pipeline_v4/run_v4.ps1`:
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\transcript_pipeline_v4\run_v4.ps1 -Source "<URL-or-Path>"
```

### Step 2: Verify Canonical Transcript
Ensure `artifacts/transcript_pipeline_v4/<source_id>/transcript.txt` exists and is non-empty.

### Step 3: Deterministic Cache Check
Check whether the source transcript has already been compiled into the vault:
```powershell
python -m obsidian_wiki cache-check "knowledge/transcript-wiki" "artifacts/transcript_pipeline_v4/<source_id>/transcript.txt"
```
- If status is `unchanged`: skip semantic processing and report existing pages from `.manifest.json`.
- If status is `new` or `modified`: proceed to Step 4.

### Step 4: Semantic Knowledge Compilation (`wiki-ingest`)
Invoke the host `wiki-ingest` skill on `artifacts/transcript_pipeline_v4/<source_id>/transcript.txt`:
1. Read the transcript progressively across its full length (early, middle, late sections).
2. Distill key concepts into `concepts/`, entities into `entities/`, and create the source note in `references/`.
3. Apply proper epistemic attribution and provenance markers (`^[inferred]`, `^[ambiguous]`).
4. Update `.manifest.json` using `obsidian-wiki cache-update`:
   ```powershell
   python -m obsidian_wiki cache-update "knowledge/transcript-wiki" "artifacts/transcript_pipeline_v4/<source_id>/transcript.txt" --pages <list-of-created-and-updated-pages>
   ```
5. Update `index.md`, append to `log.md`, and refresh `hot.md`.

### Step 5: Vault Health Validation
Verify vault integrity:
```powershell
python -m obsidian_wiki lint knowledge/transcript-wiki
python -m obsidian_wiki doctor
```
Ensure 0 broken links and clean schema compliance.

### Step 6: Reporting
Return a concise summary with created/updated pages and key insights.
