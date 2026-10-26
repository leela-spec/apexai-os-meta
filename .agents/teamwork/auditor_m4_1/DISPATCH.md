# Task Assignment: Milestone 4 Forensic Integrity Auditor

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m4_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (see Section `## 2026-10-22T11:10:20Z`, specifically R2)
- Target Deliverables in `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`:
  1. `audit-module-01-writing-profile.md`
  2. `audit-module-02-file-architecture.md`
  3. `audit-module-03-execution-modes.md`
  4. `audit-module-04-anti-drift-rules.md`
  5. `audit-module-05-governance-schemas.md`
- Prototype Reference: `rule-01-target.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Perform comprehensive forensic integrity verification on all 5 module audit files:
   - Verify that these are genuine, substantive, full-depth analytical documents (~2,000–3,500+ BPE tokens each, 25–35 KB each), not facades, stubs, or placeholder text.
   - Deep-scan for forbidden placeholder tokens (`TODO`, `FIXME`, `TBD`, `XXX`, `lorem ipsum`, `placeholder`, `dummy`, `coming soon`).
   - Check all 5 chapters are present in every file.
   - Verify that all 97 governed rules are genuinely inventoried and analyzed.
   - Verify authenticity of test execution: run `python -m pytest apex-meta/informatics/tests/ -q` and `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`.
   - Verify zero live carrier mutations (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) and research bytes preservation.
3. Formulate binary verdict: **CLEAN** or **INTEGRITY VIOLATION**.
4. Write full evidence report in `handoff.md` and notify orchestrator via `send_message` to Recipient `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`.


## 2026-10-22T13:09:13Z
Sender: a1918f04-9801-41c9-a8a4-6cebbbfab6ed
Priority: MESSAGE_PRIORITY_HIGH
Content:
You are the Forensic Auditor for Milestone 4 (Plane 4 Infrastructure Module Audits).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m4_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m4_1\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Perform forensic integrity verification on audit-module-01-writing-profile.md through audit-module-05-governance-schemas.md in apex-meta/informatics/final/research/06-layered-rule-kb/:
- Verify that these are genuine, substantive, full-depth analytical files (~2,000-3,500+ BPE tokens, 25-35 KB each) covering all 5 chapters and all 97 rules.
- Check for dummy stubs, placeholder text, or hardcoded cheating.
- Verify authenticity of pytest execution and zero live carrier mutations.
Write handoff.md with full evidence and binary verdict (CLEAN or INTEGRITY VIOLATION) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
