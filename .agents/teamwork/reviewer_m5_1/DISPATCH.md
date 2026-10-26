# DISPATCH: reviewer_m5_1

## Identity
- Role: Reviewer (Candidate 16 XML & Contract Architecture)
- Working directory: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m5_1

## Mandatory References
- Authoritative User Request: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
- Scope Document: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md
- Worker Handoff: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m5_1\handoff.md
- Candidate File: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\16-candidate-3A-ultra.md`
- Rule KB Index: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\index.md`

## Tasks
1. Review `16-candidate-3A-ultra.md`:
   - Verify frontmatter schema compliance (`type: Reference`, `id: V2-CANDIDATE-3A-ULTRA-v1.0`, etc.).
   - Verify XML block: root tags `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">` and `</apex_contract>`.
   - Verify all 22 semantic tags are present in exact order: `<target>` through `<pointers>`.
   - Verify gated attributes on tags 13–21 match baseline `13-candidate-3A-xml.md`.
   - Review architectural rationale, delta table, and provenance mapping.
2. Review `06-layered-rule-kb/index.md`:
   - Verify frontmatter (`okf_version: "0.2"`, `type: Index`, `id: V2-LAYERED-RULE-KB-INDEX`).
   - Verify 22-rule rollup table and 5 module audit summary table.
3. Run verification:
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
   - `python -m pytest apex-meta/informatics/tests/ -q`
4. Provide a clear verdict: **APPROVE** or **REQUEST_CHANGES** with concrete rationale in `handoff.md`.

## 2026-10-22T16:58:16Z
You are reviewer_m5_1.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m5_1
MANDATORY: Read c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md before starting work.
Also read your full dispatch instructions at: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m5_1\DISPATCH.md
And scope at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md

Tasks:
1. Review `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`: XML structure, root tags, all 22 semantic tags in sequence, gated attributes on tags 13-21, rationale, and delta table.
2. Review `apex-meta/informatics/final/research/06-layered-rule-kb/index.md`: frontmatter, 22-rule rollup, 5 module audits summary.
3. Run OKF validator and pytest test suite.
4. Output a clear verdict: APPROVE or REQUEST_CHANGES with detailed evidence in `handoff.md`.
Notify your parent orchestrator when complete.
