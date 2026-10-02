# Task Assignment: Forensic Integrity Auditor

## 2026-09-29T10:04:33Z

<USER_REQUEST>
You are `auditor_integrity`, the Forensic Integrity Auditor.
Your working directory is: `c:\GitDev\apexai-os-meta\.agents\auditor_integrity`
Your parent is: `orchestrator_3` (conversation ID: `6ddb3813-515a-42e2-a565-70b43dfc69f4`)

Authoritative User Request:
Read `c:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md` (specifically request 2026-09-29T09:38:08Z).

MANDATORY AUDIT RULES:
You have BINARY VETO POWER over this mission. If you find any cheating, fake data, simulated checks, or integrity violations, you MUST report `INTEGRITY VIOLATION`. If everything is authentic and verified on disk, report `CLEAN`.

Your Mission:
Perform rigorous forensic integrity checks on `c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\`:
1. Ground Truth Forensics: Verify that all 1,153 absolute paths in `agent_knowledge_matrix.csv` and `agent_knowledge_matrix.json` are genuine physical files on disk with matching byte sizes and line counts. Ensure 0 phantom files exist.
2. Evaluation Forensics: Ensure that scores are authentic human/agent evaluations and not hardcoded fake loops or dummy values. Check distribution of scores across domains and statuses.
3. Schema & Syntax Forensics: Verify RFC 4180 compliance, clean JSON parsing, and exact 11 columns.
4. Historical & Lineage Forensics: Verify authenticity of the 7 omitted doctrine files and the empty scaffold findings.
5. Deliverables Verification: Verify `README.md` completeness and accuracy.

Write your complete forensic audit report, evidentiary findings, and explicit verdict (`CLEAN` or `INTEGRITY VIOLATION`) to:
`c:\GitDev\apexai-os-meta\.agents\auditor_integrity\handoff.md`
Send a completion message back to parent (`orchestrator_3`).
</USER_REQUEST>
