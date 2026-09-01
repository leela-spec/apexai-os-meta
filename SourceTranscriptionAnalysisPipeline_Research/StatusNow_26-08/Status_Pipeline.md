### 1. What Our Pipeline Is at the Moment

Our active production system is **Transcript Pipeline V4**. It is an unbroken 4-stage pipeline that combines deterministic local media acquisition & transcription with the **`Ar9av/obsidian-wiki`** (PyPI `obsidian-wiki` v2026.8.4) cumulative knowledge compiler.

[STAGE 1: ACQUISITION]

  Media URL / File ──> yt-dlp + FFmpeg (audio-only stream)

                              │

[STAGE 2: LOCAL ASR]          ▼

  transcribe.py ─────> faster-whisper (large-v3-turbo, CPU/int8, Silero VAD)

                              │

                              ▼

  artifacts/transcript_pipeline_v4/<source_id>/

  ├── transcript.txt (normalized clean text)

  ├── transcript.srt (timestamped cues)

  └── run.log

                              │

[STAGE 3: KNOWLEDGE COMPILATION]

  obsidian-wiki (wiki-ingest)

  ├── Bounded progressive chunk reading (no context overflow)

  ├── Entity & concept extraction + contradiction preservation

  └── Bidirectional [[wikilinks]] cross-referencing

                              │

[STAGE 4: LIVE VAULT PERSISTENCE]

  knowledge/transcript-wiki/

  ├── concepts/ (interconnected markdown concept notes)

  ├── entities/ (people, organizations, tools)

  ├── references/ (source attribution & transcript anchors)

  ├── .manifest.json (SHA-256 cache for instant incremental skips)

  ├── index.md (search index)

  └── log.md (audit log)

---

### 2. Where That Is Defined

The current pipeline and its governing decisions are defined in the following locations across the repository:

#### A. Executable Code & Operational Runners

- **`scripts/transcript_pipeline_v4/run_v4.ps1`**  
    _Main deterministic entrypoint script._ Orchestrates `yt-dlp` media download, `faster-whisper` transcription, artifact normalization, and downstream invocation.
- **`scripts/transcript_pipeline_v4/transcribe.py`**  
    _Local ASR engine._ Runs `faster-whisper` (`large-v3-turbo`) with CPU int8 quantization and Silero VAD.
- **`scripts/transcript_pipeline_v4/README.md`**  
    _Operational manual._ Contains CLI usage examples, test execution commands, and vault doctor/lint invocations.

#### B. Integration Authority & Bake-Off Decisions

- **`SourceTranscriptionAnalysisPipeline_Research/v4-obsidian-wiki-integration/INTEGRATION-DECISION.md`**  
    _Authoritative integration contract._ Details the decision to adopt `Ar9av/obsidian-wiki` (replacing the previous Fabric `extract_wisdom` single-shot prompt bottleneck that timed out on long transcripts).
- **`SourceTranscriptionAnalysisPipeline_Research/v4-obsidian-wiki-integration/INSTALL-AND-RUN.md`**  
    _Step-by-step runtime protocol._ Specifies dependency management, wheel installation, and vault paths.
- **`SourceTranscriptionAnalysisPipeline_Research/v4-obsidian-wiki-integration/BAKEOFF-RESULT.md`**  
    _Empirical test evidence._ Documents the bake-off results across the benchmark corpus.

#### C. Governing Policy & Operating Rules

- **`SourceTranscriptionAnalysisPipeline_Research/current-decision-workspace/02-DECISIONS.md`**  
    _Operator decisions._ Sets binding rules (e.g., deterministic code owns workflow state, external APIs must earn promotion over local routes, no single-shot context overflows).
- **`SourceTranscriptionAnalysisPipeline_Research/00-INDEX.md`**  
    _Master index._ Routes between active workspace documents and historical V1/V2/V3 archives.

#### D. The Live Target Knowledge Base

- **`knowledge/transcript-wiki/`**  
    The persistent destination vault where compiled `concepts/`, `entities/`, `references/`, and `.manifest.json` reside.