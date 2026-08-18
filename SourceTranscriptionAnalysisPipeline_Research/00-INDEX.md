# SourceTranscriptionAnalysisPipeline Research: Master Index (00-INDEX)

## 1. Directory Mission & Scope
This directory serves as the centralized research, benchmarking, and multi-AI evaluation archive for the **SourceTranscriptionAnalysisPipeline** subsystem. It documents all architectural experiments, code deliverables, comparative evaluations, and integration roadmaps.

---

## 2. Master Document Index

| Priority | Document / Asset | Type | Purpose & Summary |
| :---: | :--- | :--- | :--- |
| **00** | [`00-INDEX.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/00-INDEX.md) | Index | Master catalog and document map. |
| **01** | [`PROCESS_STEP_COMPARISON_MATRIX.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/PROCESS_STEP_COMPARISON_MATRIX.md) | Comparison Matrix | Step-by-step lifecycle matrix comparing all 3 pipelines across 14 discrete steps. |
| **02** | [`THREE_SYSTEM_COMPARATIVE_BENCHMARK.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/THREE_SYSTEM_COMPARATIVE_BENCHMARK.md) | Benchmark Report | 3-way evaluation of Ingestion, Dataclass Engine, and TTK Protocol. |
| **03** | [`AI_WORK_ANALYSIS_AND_IMPROVEMENTS.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/AI_WORK_ANALYSIS_AND_IMPROVEMENTS.md) | Technical Report | Deep comparative evaluation of the external AI's codebase (`transcript_engine.py`), flaws, and solutions. |
| **04** | [`NEXT_STEPS.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/NEXT_STEPS.md) | Roadmap | Phased implementation plan for bridging local Whisper ingestion with the Macro-Meso-Micro engine. |
| **05** | [`README.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/README.md) | Manifest | Folder description and test verification status. |
| **06** | [`transcript_engine.py`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/transcript_engine.py) | Python Module | The deterministic Macro $\rightarrow$ Meso $\rightarrow$ Micro `KnowledgeEngine` dataclass models and renderer. |
| **07** | [`test_transcript_engine.py`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/test_transcript_engine.py) | Unit Tests | 10 unit tests covering timestamp validation, verdict enums, and serialization. |
| **08** | [`run_tests.py`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/run_tests.py) | Test Runner | Zero-dependency local test execution runner. |

---

## 3. Related Production Assets

* **Active Skill Package:** [`c:\GitDev\apexai-os-meta\.claude\skills\SourceTranscriptionAnalysisPipeline\`](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/)
* **Deep Research & OKR Prompt:** [`c:\GitDev\apexai-os-meta\.claude\skills\SourceTranscriptionAnalysisPipeline\docs\TRANSCRIPT-EXTRACTION-MACRO-MESO-MICRO-RESEARCH.md`](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/docs/TRANSCRIPT-EXTRACTION-MACRO-MESO-MICRO-RESEARCH.md)
* **Global Tools Bin (Universal):** `C:\ProgramData\AI-Tools\bin\` (`yt-dlp.exe`, `ffmpeg.exe`, `transcribe_audio.py`)
* **Multi-Video Benchmark Runs (Executed Across All 3 Pipelines):**
  1. **Andrew Huberman (`P-h5WSQG1Sw` - 2h 09m):** Neuroscience of Emotions
     - [Pipeline 1 Knowledge Wiki](file:///c:/GitDev/apexai-os-meta/artifacts/transcripts/P-h5WSQG1Sw/P-h5WSQG1Sw_knowledge_wiki.md)
     - [Pipeline 3 TTK Run Ledger (23 Windows)](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_run_huberman/manifest.json)
  2. **Elliott Prechter (`CygwqaNg2PY` - 23m):** Teaching a Machine to Count Elliott Waves
     - [Pipeline 1 Knowledge Wiki](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/CygwqaNg2PY/CygwqaNg2PY_knowledge_wiki.md)
     - [Pipeline 2 Engine Wiki](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/outputs/CygwqaNg2PY/CygwqaNg2PY_engine_wiki.md)
     - [Pipeline 3 TTK Run Ledger (4 Windows)](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/CygwqaNg2PY/manifest.json)
  3. **Markus Koch (`vFTuLylvYnA` - 21m):** Tech unter Druck. Zinsen werden zum Risiko
     - [Pipeline 1 Knowledge Wiki](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/vFTuLylvYnA/vFTuLylvYnA_knowledge_wiki.md)
     - [Pipeline 2 Engine Wiki](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/outputs/vFTuLylvYnA/vFTuLylvYnA_engine_wiki.md)
     - [Pipeline 3 TTK Run Ledger (3 Windows)](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/vFTuLylvYnA/manifest.json)
  4. **Foundation for Cycles (`oZIsMX6WgFs` - 53m):** Market Cycles Jam
     - [Pipeline 1 Knowledge Wiki](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/oZIsMX6WgFs/oZIsMX6WgFs_knowledge_wiki.md)
     - [Pipeline 2 Engine Wiki](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/outputs/oZIsMX6WgFs/oZIsMX6WgFs_engine_wiki.md)
     - [Pipeline 3 TTK Run Ledger (7 Windows)](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/oZIsMX6WgFs/manifest.json)

---

## 4. Key Architectural Insights Summary

1. **Local Compute & Zero Token Cost**: Running `faster-whisper` locally with `int8` CPU quantization achieves **15.4x real-time speed** (transcribed a 2h 9m audio file in 8.4 minutes) with 0 API tokens spent.
2. **Deterministic Data Modeling**: The external AI's dataclass architecture (`MacroResult`, `MesoModule`, `MicroClaim`) provides a clean schema for structured Markdown output with bidirectional `[[wikilinks]]`.
3. **Pluggable Fact-Checking**: The `VerificationHook` callable model allows search providers (Google, Tavily, SearxNG, local scraping) to be swapped without changing core parsing logic.
4. **Required Bridges**: The next iteration must implement flexible timestamp parsing (`MM:SS` and `HH:MM:SS`), automated LLM prompt extraction (Fabric-style patterns), and two-pass verification evaluation.
