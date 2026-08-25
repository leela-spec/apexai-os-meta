---
name: SourceTranscriptionAnalysisPipeline
description: End-to-end automated YouTube audio extraction, local free Whisper transcription, state tracking, and Macro-Meso-Micro knowledge synthesis pipeline.
---

# SourceTranscriptionAnalysisPipeline

## 1. Overview
The **SourceTranscriptionAnalysisPipeline** skill automates the detection of new media from configured YouTube channels/playlists, downloads audio-only streams (zero video bandwidth waste), performs 100% offline local Whisper transcription via CTranslate2 (`faster-whisper`), and structures raw transcripts into a 3-tier **Macro $\rightarrow$ Meso $\rightarrow$ Micro** knowledge graph.

### Core Capabilities
* **Zero Cost / 100% Local**: Uses open-source Whisper (`faster-whisper`) running locally on CPU (`int8`) or GPU (`float16`). Consumes 0 cloud API tokens for transcription.
* **Audio-Only Stream Extraction**: Bypasses heavy video downloads using `yt-dlp` + `ffmpeg`.
* **State Management & Idempotency**: Tracks watched sources and processed videos to prevent duplicate processing.
* **Macro $\rightarrow$ Meso $\rightarrow$ Micro Extraction**: Decomposes transcripts into Executive Thesis (Macro), Thematic Modules (Meso), and Fact-Checked Atomic Claims (Micro).

---

## 2. Directory Layout

```
.claude/skills/SourceTranscriptionAnalysisPipeline/
├── SKILL.md                               # This skill definition and operator manual
├── config/
│   └── watched_sources.json               # Configured channels and playlists to monitor
├── state/
│   ├── watched_sources.json               # Runtime source configuration
│   ├── latest_discovered_videos.json      # Latest discovered video links & metadata
│   └── processed_videos.json              # Ledger of processed video IDs and timestamps
├── scripts/
│   ├── Run-YouTubeWhisperPipeline.ps1     # Master pipeline orchestrator
│   ├── Sync-WatchedSources.ps1            # Channel & playlist metadata sync
│   └── transcribe_audio.py                # Local faster-whisper CTranslate2 engine
├── docs/
│   └── TRANSCRIPT-EXTRACTION-MACRO-MESO-MICRO-RESEARCH.md  # Deep research & OKR framework
└── artifacts/
    ├── pending_ai_task.json               # Downstream AI trigger payload
    └── transcripts/                       # Output directory for transcripts
        └── <video_id>/                    # Per-video artifact folder (.md, .srt, .json, .txt)
```

---

## 3. Global Tools Architecture
Binaries are stored in the universal system directory:
* **Global Path:** `C:\ProgramData\AI-Tools\bin\`
* **Binaries:** `yt-dlp.exe`, `ffmpeg.exe`, `ffprobe.exe`
* **Path Registration:** Added to the Windows User `PATH` environment variable. Accessible globally by all repositories and agents.

---

## 4. Usage & Execution Instructions

### A. Sync Watched Channels / Playlists
Discovers the latest video IDs and updates `state/latest_discovered_videos.json`:
```powershell
powershell -ExecutionPolicy Bypass -File ".claude\skills\SourceTranscriptionAnalysisPipeline\scripts\Sync-WatchedSources.ps1"
```

### B. Transcribe a Specific Video
Downloads audio stream only, executes local Whisper transcription, and generates artifacts:
```powershell
powershell -ExecutionPolicy Bypass -File ".claude\skills\SourceTranscriptionAnalysisPipeline\scripts\Run-YouTubeWhisperPipeline.ps1" -VideoUrl "https://www.youtube.com/watch?v=VIDEO_ID" -Model "base"
```
*Supported Models:* `tiny`, `base`, `small`, `medium`, `large-v3-turbo`.

---

## 5. Macro-Meso-Micro Extraction Framework

When processing raw transcripts for wiki or project updates:

1. **Macro Level (Synthesis & Taxonomy)**:
   * Core Thesis Statement (<100 words).
   * 3–5 High-Impact Takeaways.
   * Category Ontology & `[[Wikilinks]]`.
2. **Meso Level (Thematic Deep Dives & Modules)**:
   * Timestamped Chapters `[HH:MM:SS - HH:MM:SS]`.
   * Argument structures, theoretical models, and step-by-step protocols.
3. **Micro Level (Atomic Claims & Verification)**:
   * Falsifiable atomic propositions with verbatim quotes and `[HH:MM:SS]` anchors.
   * Live web search verification verdict: `[CONFIRMED]`, `[CONTRADICTED]`, `[UNVERIFIED]`.
   * Contextual nuance and subsequent research notes.

---

## 6. Autonomous AI Ingestion OKR Prompt

```markdown
# OKR Research & Implementation Mission: Autonomous Transcript-to-Knowledge Engine

## Objective (O)
Build and deploy a deterministic, multi-tiered (Macro -> Meso -> Micro) knowledge extraction engine that transforms raw Whisper transcripts into verified, anchor-linked, fact-checked knowledge wiki artifacts with zero cloud API token waste.

## Key Results (KRs)
- KR 1: Identify, clone, and benchmark at least 3 state-of-the-art open-source transcript processing repositories (e.g. Fabric patterns, WhisperX, RAPTOR, Chain-of-Density).
- KR 2: Implement a deterministic 3-tier parsing skill (Macro overview, Meso modules, Micro verified claims with [HH:MM:SS] anchors).
- KR 3: Structure output artifacts as bidirectional Wiki-linked Markdown notes ([[Topic]], [[Claim]]) ready for Obsidian / Knowledge Graph ingestion.
- KR 4: Deliver a self-contained PowerShell / CLI tool package with end-to-end unit tests and zero external proprietary dependencies.
```
