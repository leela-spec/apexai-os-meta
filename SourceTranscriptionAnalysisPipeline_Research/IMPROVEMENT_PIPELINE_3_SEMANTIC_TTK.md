# Pipeline 3 & Harness Improvement & Implementation Plan: Genuine Semantic Extraction & Fail-Closed Benchmark

**Target Subsystem:** `.claude/skills/transcript-to-knowledge/` & `scripts/Run-BatchMultiPipelineBenchmark.ps1`  
**Focus:** Eliminating Pseudo-Semantic Transcript Copying, Full Window Reduction Coverage, and Honest Benchmark Telemetry

---

## 1. Deficiencies Identified in GPT-Evaluation

1. **Pseudo-Semantic Lifecycle Driver:** `execute_ttk_lifecycle.py` bypassed actual semantic reasoning by blindly copying the first 3 lines of each window, marking them all `fact`/`SUPPORTED`, and synthesizing a generic title-derived summary.
2. **Artificial Reduce Truncation:** Reduce stopped after 10 claims and generated a single Meso module using only segments 1–10, ignoring the remaining 95% of Map windows.
3. **Benchmark Receipt Dishonesty:**
   - Harness marked `all_passed = true` even when P2 had `SYNTHESIS_PENDING` on 3/4 sources.
   - P1 benchmark only tested ASR presence, not synthesis.
   - Git commit in receipt was stale (`6c2f1b70`) rather than the active HEAD + dirty indicator.

---

## 2. Technical Implementation Specifications

### 2.1. True Semantic Extraction Engine in TTK
* Replace naive line-copying in `execute_ttk_lifecycle.py` with genuine semantic extraction:
  * **Map Stage:** For each window, extract key propositions, distinguish between `fact`, `opinion`, `recommendation`, `anecdote`, and extract exact verbatim quote evidence with matching segment IDs.
  * **Reduce Stage (Full Coverage):**
    * Process **all** Map window outputs rather than truncating at 10 claims.
    * Synthesize comprehensive Meso modules covering the full duration of the video (intro, core technical/scientific mechanisms, arguments, conclusions).
    * Extract genuine Macro thesis reflecting actual content (e.g. Neuroscience of emotions & emotion regulation, Elliott wave algorithmic counting, German tech stock rotation and rate sensitivity, Market cycle spectrum peaks & stability criteria).
  * **Coverage Accountability:** Record `total_windows_processed`, `windows_represented_in_reduce`, and ensure 100% window coverage.

### 2.2. Benchmark Harness (`Run-BatchMultiPipelineBenchmark.ps1`) Refactor
* **Honest Aggregation (`all_passed`):**
  * `all_passed` is `true` **only** if all requested pipelines (P1, P2, P3) complete with `OPERATOR_ARTIFACT_COMPLETE` / `SYNTHESIS_COMPLETE`.
  * If any pipeline is `SYNTHESIS_PENDING` or `FAILED`, mark `all_passed = false` and report the exact incomplete count.
* **Accurate Code Provenance:**
  * Read `git rev-parse HEAD` and check `git status --porcelain` to record `git_commit` and `git_dirty: true/false`.
* **Forced Fresh ASR Execution:**
  * Support `-ForceTranscribe` flag to regenerate fresh ASR JSON files with word-level timestamps and diagnostics.

---

## 3. Verification & Acceptance Criteria
* [ ] TTK outputs for all 4 benchmark sources contain rich, non-generic Macro theses and substantive multi-chapter Meso modules covering the entire video length.
* [ ] TTK validation passes (`ttk.validate_run(output_dir)["complete"] == True`).
* [ ] Benchmark receipt honestly reflects stage states and clean Git commit SHA.
