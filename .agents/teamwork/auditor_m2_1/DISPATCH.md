# Task Assignment: Milestone 2 Forensic Auditor

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m2_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Target Deliverables: `rule-09-recovery.md` through `rule-15-detour.md`
- Prototype: `rule-01-target.md`
- Worker Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m2_1\handoff.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Perform forensic integrity checks on `rule-09-recovery.md` through `rule-15-detour.md`:
   - Static analysis: Are these genuine, human-readable, thorough analytical documents? Or did the worker generate placeholder/dummy text or truncated stubs?
   - Provenance authenticity: Are the research links and Plane 4 citations real, substantive references?
   - Test integrity: Are pytest results genuine?
   - Invariants: Zero live carrier mutations (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`).
3. Report verdict: CLEAN or INTEGRITY VIOLATION.
4. Record full evidence report in `handoff.md` and send message to Orchestrator (`a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).

## 2026-10-22T12:18:01Z
You are the Forensic Auditor for Milestone 2 (Rules 09-15).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m2_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_m2_1\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Perform forensic integrity verification on rule-09-recovery.md through rule-15-detour.md in apex-meta/informatics/final/research/06-layered-rule-kb/:
- Verify that these are genuine, substantive, full-depth analytical files matching prototype rigor.
- Check for dummy stubs, placeholder text, or hardcoded cheating.
- Verify authenticity of pytest execution and zero live carrier mutations.
Write handoff.md with full evidence and binary verdict (CLEAN or INTEGRITY VIOLATION) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
