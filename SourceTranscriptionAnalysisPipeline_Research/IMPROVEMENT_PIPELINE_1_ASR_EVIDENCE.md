# Pipeline 1 Improvement & Implementation Plan: ASR Evidence & Ingestion

**Target Subsystem:** `.claude/skills/SourceTranscriptionAnalysisPipeline/`  
**Focus:** Fresh ASR Evidence, Word-Level Diagnostics, Grounding Terminology & Verification Status

---

## 1. Deficiencies Identified in GPT-Evaluation

1. **Unexercised ASR Evidence Schema:** The benchmark reused pre-existing `.srt` files and never executed `transcribe_audio.py` fresh. Existing JSON files in `artifacts/transcripts/` still lack `words` array and segment diagnostics (`avg_logprob`, `no_speech_prob`, `compression_ratio`, `temperature`).
2. **Grounding Terminology Overstatement:** `synthesize_transcript.py` renders `Source Grounding: VALIDATED (100% exact verbatim match)`, which overstates what is proven (it proves quote existence, not full Macro/Meso entailment). Should be labeled `QUOTE_GROUNDING_VALID`.
3. **Verification Status Bug:** `synthesize_transcript.py` marked external fact-checking as `COMPLETED` if `external_sources` URL array was non-empty, even when all claims had `verdict = UNVERIFIED`.
4. **Timestamp-to-Segment Alignment Gap:** Global quote substring matching does not verify whether the cited timestamp falls within the spoken range of that specific quote.

---

## 2. Technical Implementation Specifications

### 2.1. `transcribe_audio.py`
* Ensure the JSON serialization format emits standard schema:
  ```json
  {
    "segments": [
      {
        "id": 1,
        "start": 0.0,
        "end": 4.54,
        "text": "...",
        "avg_logprob": -0.18,
        "no_speech_prob": 0.002,
        "compression_ratio": 1.25,
        "temperature": 0.0,
        "words": [
          { "word": "Hello", "start": 0.0, "end": 0.45, "probability": 0.98 }
        ]
      }
    ]
  }
  ```
* Synchronize binary to `C:\ProgramData\AI-Tools\bin\transcribe_audio.py`.

### 2.2. `synthesize_transcript.py`
* **Fix Verification Status Logic:**
  ```python
  # Only count decisive verdicts (CONFIRMED / CONTRADICTED) as fact-checked
  decisive = [c for c in self.micro_claims if c.verdict in ("CONFIRMED", "CONTRADICTED", "MIXED")]
  if len(decisive) == len(self.micro_claims) and len(self.micro_claims) > 0:
      return "COMPLETED"
  elif len(decisive) > 0:
      return "PARTIAL"
  return "NOT_RUN"
  ```
* **Correct Grounding Badge:**
  Update header to:
  `> - **Quote Grounding:** VALIDATED (Verbatim Substring Match)`
  `> - **External Fact-Checking:** NOT_RUN | PARTIAL | COMPLETED`
* **Enforce Timestamp Alignment:**
  Verify that the claimed `timestamp` falls within $\pm 30$ seconds of the matching source segment in the transcript.

### 2.3. Fresh ASR Re-execution
* Provide a forced fresh execution mode (`--force-transcribe`) that executes faster-whisper on all 4 benchmark sources to generate new JSON files containing full word timestamps and diagnostics.

---

## 3. Verification & Acceptance Criteria
* [ ] Unit tests in `test_synthesize_transcript.py` pass and assert `QUOTE_GROUNDING_VALID` badge.
* [ ] Verification status remains `NOT_RUN` when claims only have search URLs.
* [ ] Fresh JSON transcripts contain `words` array and segment diagnostics.
