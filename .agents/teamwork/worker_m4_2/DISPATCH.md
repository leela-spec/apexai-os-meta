# Dispatch: Worker M4_2 (Challenger 2 Remediation Specialist)

## Role
Remediation Worker (Iteration 2)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m4_2`

## Parent
Orchestrator 3 (`736cd41c-7e37-43d2-b265-c5d4f71a370c`)

## Authoritative Instructions
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically `## 2026-10-21T16:45:38Z`).

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Challenger 2 Input & Remediation Requirements
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_2\handoff.md` and `challenge_report.md`.

Execute the following 3 concrete remediations:
1. **Remediation 1 (Close Escalation Vacuum in `<editing>` and `<schemas>`)**:
   In `13-candidate-3A-xml.md`:
   - In `<editing>`: append: ` For multi-block edits, AST patches, or deterministic executors, open ref for exact protocols.`
   - In `<schemas>`: append: ` For exact JSON schemas or frontmatter specifications, open ref.`
   - Update header comment in `13-candidate-3A-xml.md` to reflect new live counts.
2. **Remediation 2 (Carrier Synchronization Guidance in `DEC-21`)**:
   In `01-decision-register.md` (`DEC-21`) and `FinalizationDossier/07-teamwork-independent-validation.md`:
   - Document the empirical finding that Option C "stubs" fail in standalone CLIs (Claude Code CLI ignores AGENTS.md when CLAUDE.md exists; Gemini CLI ignores AGENTS.md by default). Option A (byte-identical sync via pytest) remains the sole safe universal baseline today, with an explicit WARN for Antigravity dual-carrier injection and harness configuration guidance (`context.fileName: AGENTS.md`).
3. **Remediation 3 (Ratify Candidate 3A as Sole Production Blueprint Default in `DEC-23`)**:
   In `01-decision-register.md` (`DEC-23`) and `FinalizationDossier/07-teamwork-independent-validation.md`:
   - Formally ratify Candidate 3A as the exclusive production blueprint default for `AGENTS.md` (empirically supported by 3B saving only 36 BPE tokens / 0 cache blocks while collapsing under 80-col word-wrapping). Relegate 3B to experimental benchmark Arm B2 in `04-empirical-test-protocol.md`.
4. **Update Metrics in `07-teamwork-independent-validation.md`**:
   - Recompute live byte metrics for Table 1 and Table 2 to reflect the post-remediation files.
5. **Strict Boundary**:
   - ZERO changes to live root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`.
6. **Verify Conformance**:
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (0 errors)
   - `python -m pytest apex-meta/informatics/tests/ -q` (100% pass)
   - `git diff AGENTS.md CLAUDE.md GEMINI.md` (zero diff)
7. Produce `changes.md` and `handoff.md` in your working directory and notify parent orchestrator via `send_message`.

## 2026-10-21T17:21:34Z
You are assigned as Worker M4_2 (Challenger 2 Remediation Specialist).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m4_2
Your task assignment is in: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m4_2\DISPATCH.md
Authoritative request is in: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically section ## 2026-10-21T16:45:38Z).
Input feedback from Challenger 2: c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_2\handoff.md and challenge_report.md
Your parent orchestrator conversation ID is: 736cd41c-7e37-43d2-b265-c5d4f71a370c

