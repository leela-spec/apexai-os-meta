# Dispatch for worker_remediation

## Mission
Remediate the zero-byte files identified by reviewer_staging_contracts in MetaDetective\90_SUPERSEDED\, fix the line 209 typo in ALL_AGENTS_DEEP_AUDIT_INDEX.md, update byte sizes in INDEX.md and master index, and ensure 100% of staged files are non-zero bytes with automated verification.

## 2026-09-30T07:40:42Z
You are worker_remediation, a teamwork_preview_worker subagent.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\worker_remediation\

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

MANDATORY: You MUST read c:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md (specifically the section under header ## 2026-09-29T20:18:23Z) before beginning work.

Your mission is to resolve the findings identified during the Milestone 4 review:
1. Reviewer Feedback from `c:\GitDev\apexai-os-meta\.agents\reviewer_staging_contracts\handoff.md`:
   - Found 2 zero-byte files in `C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\MetaDetective\90_SUPERSEDED\`:
     - `newprocess4audio2ssot_empty.md` (0 bytes)
     - `Unbenannt_empty.md` (0 bytes)
   - These files must NOT be 0 bytes. Populate each file with a formal quarantine tombstone header:
     - Document that they were 0-byte abandoned template stubs in legacy OpenClaw mirror `NewFinals\MetaHeadsKBUpdateState\mirror\`.
     - State their lifecycle status: `Empty Scaffold / Stub (Quarantined)`.
     - State the quarantine reason: isolated to prevent poisoning active agents.
2. Update `C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\MetaDetective\00_INDEX\INDEX.md`:
   - Update the file sizes for these two files and the total byte size for `MetaDetective\`.
3. Reviewer Feedback from `c:\GitDev\apexai-os-meta\.agents\reviewer_dossiers\handoff.md`:
   - Line 209 in `c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\ALL_AGENTS_DEEP_AUDIT_INDEX.md` contains a slight path typo for `weekly-orchestrator.md`. Fix it to point to the verified physical path `c:\GitDev\apexai-os-meta\.claude\skills\weekly-orchestrator\references\roles\meta-ops.md` or as verified.
4. Update `ALL_AGENTS_DEEP_AUDIT_INDEX.md`:
   - Synchronize the Section 5.1 table for `MetaDetective` byte size and the grand total byte size to reflect the updated non-zero bytes.
   - In Section 9 (the embedded Python verification script), ensure it explicitly asserts:
     `assert os.path.getsize(f) > 0, f"Zero-byte file: {f}"` for every single staged file.
5. Verification:
   - Run the Python verification script to confirm that 100% of all 249 staged files exist, are strictly non-zero bytes, and line counts match.

Write your self-contained handoff to `c:\GitDev\apexai-os-meta\.agents\worker_remediation\handoff.md` and send a completion message to parent when done.

