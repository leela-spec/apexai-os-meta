# Pipeline 2 Improvement & Implementation Plan: Typed Schema & Representation

**Target Subsystem:** `SourceTranscriptionAnalysisPipeline_Research/` (`transcript_engine.py`, `synthesize_p2.py`)  
**Focus:** Segment Provenance Custody, Schema Alignment with TTK, and Reference Role

---

## 1. Deficiencies Identified in GPT-Evaluation

1. **Empty Segment Provenance Fields:** In the generated `P-h5WSQG1Sw_engine_wiki.json`, `source_segment_ids`, `source_start`, and `source_end` were present in the dataclass but left empty (`[]`, `""`).
2. **Coverage/Completeness Gap:** P2 could produce a structurally "complete" wiki from a tiny 30-second slice of a 2-hour audio file without flagging that 99% of the transcript was omitted.
3. **Role Clarification:** P2 should act as a typed domain library and schema contract rather than an artificial standalone pipeline that competes with TTK.

---

## 2. Technical Implementation Specifications

### 2.1. `transcript_engine.py`
* **Populate & Validate Segment Provenance:**
  When parsing spoken text from SRT or JSON, maintain segment mapping:
  ```python
  @dataclass
  class MicroClaim:
      claim_id: str
      proposition: str
      quote: str
      timestamp: str
      claim_type: str = "FACT"
      internal_confidence: str = "hypothesis"
      source_support: str = "SUPPORTED"
      verdict: str = "UNVERIFIED"
      source_segment_ids: list[str] = field(default_factory=list)
      source_start: str = ""
      source_end: str = ""
      search_query: Optional[str] = None
      external_sources: list = field(default_factory=list)
      added_context: Optional[str] = None
  ```
  In `KnowledgeEngine.from_semantic_result(data, spoken_text, segments)`:
  * Require that `source_segment_ids` is non-empty for every Micro claim.
  * Validate that the quote exists in those specific segments.
  * Populate `source_start` and `source_end` from the matching segments.

* **Add Coverage Metric:**
  Add `calculate_source_coverage(total_duration_sec, total_segments)`:
  * Emits coverage percentage (e.g. `Analyzed 45 of 5,752 segments (0.78% of total source duration)`).
  * If coverage is below 80%, render a `Coverage Warning` banner in the generated Markdown.

### 2.2. Schema Harmonization with TTK
* Ensure `transcript_engine.py` export and import contracts are drop-in compatible with TTK's `REDUCE_RESULT_SCHEMA`.

---

## 3. Verification & Acceptance Criteria
* [ ] Unit tests in `test_transcript_engine.py` verify that claims with empty `source_segment_ids` or unmatched segment ranges fail validation.
* [ ] Coverage percentage is calculated and rendered in output markdown.
* [ ] Tests in `run_tests.py` pass 100%.
