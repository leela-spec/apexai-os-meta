# V2.1 Trial 1 Production Architecture Selection Report

**Status:** COMPLETE — DERIVED FROM MEASURED BENCHMARK EVIDENCE  
**Repository:** `leela-spec/apexai-os-meta`  
**Branch:** `main`

---

## 1. Selected Production Composition

| Pipeline Stage | Selected Component / Engine | Execution Mode | Evidence Status |
| :--- | :--- | :--- | :--- |
| **Source Acquisition** | `source_existing` | `yt-dlp` / `ffmpeg` | Retained (P1 path) |
| **ASR Transcription** | `faster_whisper_small` | Local CPU (`int8` CTranslate2) | Measured PASS |
| **Alignment / Diarization** | `NONE` | Single-speaker default | Not Triggered |
| **Canonical Custody** | `custody_ttk` | Deterministic TTK Python spine | Locked Core |
| **Pre-Extraction** | `NONE` | Direct agent extraction | Not Triggered |
| **Map Stage** | `direct_agent_map` | Grounded agent/subagent extraction | Measured PASS |
| **Structured Output** | `native_schema_plus_ttk_validation` | Strict JSON schema + TTK validators | Measured PASS |
| **Support Advisory** | `NONE` | Agent semantic support judgment | Measured PASS |
| **Reduce Stage** | `direct_agent_reduce` | Hierarchical Macro/Meso/Micro synthesis | Measured PASS |
| **External Verification** | `verify_ttk_queue` | Selective factual routing | Retained Core |
| **Obsidian Compiler** | `custody_ttk` | Deterministic Wiki compilation | Locked Core |

---

## 2. Decision Rationale & Measured Evidence
- **ASR**: `faster-whisper` (`small` model, `int8` on CPU) clears quality floor with word-level timestamps and zero cloud API dependencies.
- **Map & Reduce**: Agent/subagent semantic workers produce 100% compliant `ttk.map-result.v2` and `ttk.reduce-result.v2` outputs without falling back to regex or heuristic pseudo-semantics.
- **Evidence Integrity**: All metrics in `SELECTION.yaml` reference raw per-case JSON output artifacts and execution receipts verified by `verify_evidence_closure.py`.
