# Historical Archive: V4 Pipeline Mechanism with Fabric + Ollama (qwen3.5:9b)

## 1. Purpose of this Archive
This directory (`SourceTranscriptionAnalysisPipeline_Research/tests_mechanisms_v4_with_ollama_qwen/`) preserves the exact state of the V4 pipeline as implemented prior to the production adoption of `obsidian-wiki` (v2026.8.4). It contains:
- The exact PowerShell scripts and test suites (`code/`) that executed Fabric with local Ollama.
- Snapshots of the raw artifacts (`artifacts_snapshot/`) generated during historical benchmark runs (`CygwqaNg2PY`, `vFTuLylvYnA`, `P-h5WSQG1Sw`).
- Detailed operational notes on the failure modes, throughput bottlenecks, and monolithic prompt limits.

---

## 2. Architecture & Runtime Parameters
The historical mechanism was configured as follows:
- **Acquisition**: `yt-dlp` extracting audio stream into `source/source.m4a` with `--write-info-json`.
- **ASR**: `transcribe.py` invoking `faster-whisper` (`large-v3-turbo`, CPU `int8`, VAD enabled) $\rightarrow$ `transcript.txt`, `transcript.srt`.
- **Semantic Extraction**: `fabric.exe`
  - Pattern: `extract_wisdom`
  - Vendor: `Ollama`
  - Model: `qwen3.5:9b`
  - Parameters: `--modelContextLength=65536`, `--thinking=off`
  - Timeout: `OLLAMA_HTTP_TIMEOUT=60m`
  - Input: Stdin piped from `transcript.txt`
  - Output: `knowledge.md`

---

## 3. Test Runs & Performance Baseline

### Source 1: `CygwqaNg2PY` (Elliott Prechter Interview)
- **Audio / Text**: ~343 lines, 21.3 KB
- **Outcome**: Succeeded in ~90s. Generated standard `extract_wisdom` sections (Summary, Ideas, Quotes, Facts).
- **Limitation**: Output was isolated in `knowledge.md` without cross-source wikilinks or conceptual dedup.

### Source 2: `vFTuLylvYnA` (Markus Koch Opening Bell)
- **Audio / Text**: ~274 lines, 17.5 KB (German monologue)
- **Outcome**: Succeeded. Output retained German key points, but lacked integration with financial concept nodes.

### Source 3: `P-h5WSQG1Sw` (Huberman Lab x Dr. Ralph Adolphs)
- **Audio / Text**: 1,471 lines, 141.9 KB (Long Academic Stress Test)
- **Outcome**: **FAILED / TIMED OUT**. Local `qwen3.5:9b` execution over a single monolithic context window exceeded practical CPU latency limits, exhausted memory, and failed to complete extraction within the 60-minute window.

---

## 4. Preserved Artifact Hierarchy
```
SourceTranscriptionAnalysisPipeline_Research/tests_mechanisms_v4_with_ollama_qwen/
├── HANDOVER-FABRIC-OLLAMA-V4-STATE.md
├── code/
│   ├── run_v4_fabric_ollama.ps1
│   ├── test_run_v4_fabric_ollama.ps1
│   └── README_v4_fabric_ollama.md
└── artifacts_snapshot/
    ├── CygwqaNg2PY/
    │   ├── transcript.txt
    │   ├── transcript.srt
    │   ├── knowledge.md
    │   └── run.log
    ├── vFTuLylvYnA/
    │   ├── transcript.txt
    │   ├── transcript.srt
    │   ├── knowledge.md
    │   └── run.log
    └── P-h5WSQG1Sw/
        ├── transcript.txt
        ├── transcript.srt
        └── run.log
```
