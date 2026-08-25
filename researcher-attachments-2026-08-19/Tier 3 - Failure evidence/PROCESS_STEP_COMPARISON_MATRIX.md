# End-to-End Pipeline Process Step Comparison Matrix

## 1. Executive Summary

This document archives the comprehensive step-by-step lifecycle comparison across the three independently developed transcript processing systems:
1. **Pipeline A (`SourceTranscriptionAnalysisPipeline`)**: The Media Acquisition & Whisper Transcription Engine.
2. **Pipeline B (`transcript_engine.py` / Research Engine)**: The Epistemic Dataclass Model & Knowledge Wiki Renderer.
3. **Pipeline C (`transcript-to-knowledge` / TTK Skill)**: The Resumable Map-Reduce Chunking & Integrity Protocol.

---

## 2. End-to-End Process Step Matrix

| # | Step in Pipeline Lifecycle | Pipeline A: `SourceTranscriptionAnalysisPipeline` (Frontend Ingestion) | Pipeline B: `transcript_engine.py` (Research Dataclass Engine) | Pipeline C: `transcript-to-knowledge` / `ttk.py` (Industrial TTK Protocol) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Channel & Playlist Watchlist Polling** | **Executed by:** `Sync-WatchedSources.ps1`<br>**Output:** `latest_discovered_videos.json` (20 latest video links) | — *(Does not monitor web sources)* | — *(Does not monitor web sources)* |
| **2** | **Audio-Only Stream Extraction** | **Executed by:** `yt-dlp.exe` + `ffmpeg.exe`<br>**Output:** `P-h5WSQG1Sw.mp3` (78.89 MB audio, 0 video bytes) | — *(Expects text input)* | — *(Expects text file input)* |
| **3** | **Local Offline Speech-to-Text (ASR)** | **Executed by:** `transcribe_audio.py` (`faster-whisper` on CPU `int8`)<br>**Output:** Transcribed in 504s (15.4x real-time) | — *(No ASR engine)* | — *(No ASR engine)* |
| **4** | **Raw Multi-Format Transcript Export** | **Executed by:** `transcribe_audio.py`<br>**Output:** `.srt`, `.json`, `.txt`, `.md` in `artifacts/transcripts/` | — | — |
| **5** | **Transcript Ingestion & SHA256 Integrity** | — | **Executed by:** `KnowledgeEngine()` in memory<br>**Output:** In-memory Python objects | **Executed by:** `ttk.py init`<br>**Output:** Cryptographic SHA256 recorded in `run.json` |
| **6** | **Token Chunking & Window Slicing** | — *(Passes raw 25k words monolithically)* | — *(Passes raw text without chunking)* | **Executed by:** `ttk_windows.py`<br>**Output:** 23 bounded Map windows (`window-0001.json` - `0023.json`, 700–1500 words each) |
| **7** | **Macro Synthesis Extraction** *(Thesis, Taxonomy, Speakers)* | **Executed by:** `synthesize_transcript.py`<br>**Output:** `MacroResult` header with `[[Wikilinks]]` | **Executed by:** `MacroResult` dataclass<br>**Output:** Structured Markdown header with `[[Wikilinks]]` | **Executed by:** `ttk_map.py` + `ttk_compile.py`<br>**Output:** Semantic Map/Reduce packets |
| **8** | **Meso Module & Protocol Extraction** *(Thematic Chapters & Steps)* | **Executed by:** `synthesize_transcript.py`<br>**Output:** Numbered protocol steps, arguments, and caveats | **Executed by:** `MesoModule` dataclass<br>**Output:** Numbered protocol steps, arguments, and caveats | **Executed by:** `ttk_map.py` + `ttk_compile.py`<br>**Output:** Structured Meso module blocks |
| **9** | **Micro Claim & Verbatim Grounding** *(Atomic Claims + `[HH:MM:SS]`)* | **Executed by:** `synthesize_transcript.py`<br>**Output:** `[[Claim-X]]` blocks with quotes and timecodes | **Executed by:** `MicroClaim` dataclass<br>**Output:** `[[Claim-X]]` blocks with quotes and timecodes | **Executed by:** `ttk_map.py`<br>**Output:** Bounded atomic claims from core segments |
| **10** | **Quote Validation & Anti-Hallucination Gate** | **Executed by:** `parse_timestamp_to_seconds`<br>**Output:** Flexible format validation (`MM:SS` & `HH:MM:SS`) | **Executed by:** `MicroClaim.__post_init__`<br>**Output:** Regex validation of timestamp format | **Executed by:** `ttk.py validate`<br>**Output:** **Strict Gate**: Fails build if quotes do not match source text verbatim |
| **11** | **Fact Check-Worthiness Routing** | — | — *(Verifies all claims indiscriminately)* | **Executed by:** `ttk.py make-verify`<br>**Output:** Filters only verifiable factual claims for search |
| **12** | **External Search & Fact Verification** | **Executed by:** Search queries + DOI citations<br>**Output:** `[CONFIRMED]` / `[CONTRADICTED]` verdicts | **Executed by:** `VerificationHook` callable<br>**Output:** Injects top 3 URLs + `[CONFIRMED]` / `[CONTRADICTED]` verdict | **Executed by:** `ttk_verify.py`<br>**Output:** Structured verification ledger with evidence status |
| **13** | **Final Knowledge Wiki & Graph Generation** | **Executed by:** `synthesize_transcript.py`<br>**Output:** `[id]_knowledge_wiki.md` and `.json` | **Executed by:** `engine.render_wiki_markdown()`<br>**Output:** `P-h5WSQG1Sw_knowledge_wiki.md` and `.json` | **Executed by:** `ttk_wiki.py` + `ttk_compile.py`<br>**Output:** Structured wiki markdown tree in `wiki/` |
| **14** | **Downstream Event Handoff & State Ledger** | **Executed by:** `Run-YouTubeWhisperPipeline.ps1`<br>**Output:** `pending_ai_task.json` + `processed_videos.json` | — | **Executed by:** `ttk.py next`<br>**Output:** Resumable state lifecycle tracking |

---

## 3. Storage Locations

* **Research Folder:** `c:\GitDev\apexai-os-meta\SourceTranscriptionAnalysisPipeline_Research\`
* **Skill Package:** `c:\GitDev\apexai-os-meta\.claude\skills\SourceTranscriptionAnalysisPipeline\`
* **Global Tools Bin:** `C:\ProgramData\AI-Tools\bin\`
