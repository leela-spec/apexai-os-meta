# Task Assignment: Milestone 1 Forensic Auditor

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m1_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Target Deliverables: `rule-02-product-first.md` through `rule-08-context.md`
- Prototype: `rule-01-target.md`
- Worker Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_1\handoff.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Perform forensic integrity checks on `rule-02-product-first.md` through `rule-08-context.md`:
   - Static analysis: Are these genuine, human-readable, thorough analytical documents? Or did the worker generate placeholder/dummy text or truncated stubs?
   - Token & character depth: Do the files contain detailed reasoning (~2,500–3,500 BPE tokens each) consistent with prototype `rule-01-target.md`?
   - Provenance authenticity: Are the research links and Plane 4 citations real, substantive references?
   - Test integrity: Are pytest results genuine?
3. Report verdict: CLEAN or INTEGRITY VIOLATION.
4. Record full evidence report in `handoff.md` and send message to Orchestrator (`a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).

## 2026-10-22T11:41:53Z
You are the Forensic Auditor for Milestone 1 (Rules 02-08).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m1_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m1_1\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Perform forensic integrity verification on rule-02-product-first.md through rule-08-context.md in apex-meta/informatics/final/research/06-layered-rule-kb/:
- Verify that these are genuine, substantive, full-depth analytical files (~2,500-3,500 BPE tokens each) matching rule-01-target.md rigor.
- Check for dummy stubs, placeholder text, or hardcoded cheating.
- Verify authenticity of pytest execution.
Write handoff.md with full evidence and binary verdict (CLEAN or INTEGRITY VIOLATION) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.

