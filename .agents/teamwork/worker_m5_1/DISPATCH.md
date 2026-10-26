# DISPATCH: worker_m5_1

## Identity
- Role: Implementation Worker (Candidate 16 & Index Integration)
- Working directory: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m5_1

## Mandatory References
- Authoritative User Request: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
- Scope Document: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md
- Explorer Reports:
  - Option B & Contract XML text: `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_1\handoff.md`
  - Candidate 16 Blueprint & Metrics: `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1\handoff.md`
  - Index Specifications & Conformance Fixes: `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2\handoff.md`

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Write Ownership Boundaries
You have exclusive write ownership of:
1. `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`
2. `apex-meta/informatics/final/research/06-layered-rule-kb/index.md`
3. `apex-meta/informatics/final/index.md`
4. Surgical fixes in:
   - `apex-meta/informatics/final/research/06-layered-rule-kb/audit-module-01-writing-profile.md`
   - `apex-meta/informatics/final/research/06-layered-rule-kb/audit-module-02-file-architecture.md`
   - `apex-meta/informatics/final/research/06-layered-rule-kb/rule-01-target.md` (relative links)
NEVER modify root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.
NEVER modify frozen upstream research files in `01-universal-instruction-research/` or `03-research-of-file-10/`.

## Tasks
1. **Author `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`**:
   - Use the exact blueprint and specifications from `spec_miner_m5_1/handoff.md` and `explorer_m5_1/handoff.md`.
   - Root wrapper: `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">` ... `</apex_contract>`.
   - All 22 Option B snippets in exact sequence `<target>` through `<pointers>`.
   - Complete metric tables (Lines 65, Words 769, Chars 5,917, Repo tokens 1,479, BPE `cl100k_base` 1,225 BPE tokens). Document rationale for ~950 BPE prompt estimate vs 1,225 BPE empirical Option B realization under R2/WP-25 invariant preservation.
   - Complete 22-rule delta table against `13-candidate-3A-xml.md`.
   - Canonical Provenance Map.

2. **Author `apex-meta/informatics/final/research/06-layered-rule-kb/index.md`**:
   - Use the complete design from `explorer_m5_2/handoff.md` Section 4.1.
   - Declare `okf_version: "0.2"`, `type: Index`, `id: V2-LAYERED-RULE-KB-INDEX`.
   - Include the comprehensive 22-rule rollup table and 5 module audit summary table.

3. **Update `apex-meta/informatics/final/index.md`**:
   - Apply the 5 updates specified in `explorer_m5_2/handoff.md` Section 4.2.
   - Update header callout, Candidate suite table (add candidate 16), ASCII tree, Section 2.1 table, and Section 3 matrix (hyperlink rule tags and repair the 2 path typos).

4. **Apply Surgical Fixes in M4 Audits & Rule 01**:
   - In `audit-module-01-writing-profile.md`: escape/backtick dummy link examples `[Name](path)` (lines 60, 134) and set heading `### 2.1 Rules Canonically Owned by writing-profile.md`.
   - In `audit-module-02-file-architecture.md`: escape/backtick dummy link example `[Target](path/to/file.md)` (line 237).
   - In `rule-01-target.md`: standardize relative link paths to `../../candidates/13-candidate-3A-xml.md` and `../../../anti-drift-rules.md`.

5. **Run Verification Commands**:
   - Run `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (must be 0 OKF Errors, 0 Apex Profile Errors).
   - Run `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics/final/research/06-layered-rule-kb` (must be 0 errors).
   - Run `python -m pytest apex-meta/informatics/tests/ -q` (must be 100% pass, e.g. 309/309).
   - Run `git status --porcelain AGENTS.md CLAUDE.md GEMINI.md` (must be empty).

Document all commands, exact outputs, and results in your `handoff.md` at `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m5_1\handoff.md`.
Send completion message to orchestrator parent when done.


## 2026-10-22T15:47:51Z
You are worker_m5_1.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m5_1
MANDATORY: Read c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md before starting work.
Also read your full dispatch instructions at: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m5_1\DISPATCH.md
And review the explorer handoffs:
- c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_1\handoff.md
- c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1\handoff.md
- c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2\handoff.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your task is to implement Milestone 5 deliverables:
1. Author `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md` using the exact blueprint from spec_miner_m5_1/handoff.md and contract block from explorer_m5_1/handoff.md.
2. Author `apex-meta/informatics/final/research/06-layered-rule-kb/index.md` using the design from explorer_m5_2/handoff.md Section 4.1.
3. Update `apex-meta/informatics/final/index.md` per explorer_m5_2/handoff.md Section 4.2.
4. Apply surgical fixes in `audit-module-01-writing-profile.md`, `audit-module-02-file-architecture.md`, and `rule-01-target.md` per explorer_m5_2/handoff.md Section 4.3.
5. Run builds, OKF validation (`python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`), and full pytest test suite (`python -m pytest apex-meta/informatics/tests/ -q`). Confirm 100% pass.
6. Verify root carrier files (AGENTS.md, CLAUDE.md, GEMINI.md) are completely unmutated.

Write a complete handoff report to `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m5_1\handoff.md`.
Update progress.md in your working directory.
When finished, send a message to your parent orchestrator with your results and handoff path.
