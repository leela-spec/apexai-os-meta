# Task Assignment: Milestone 4 Challenger 2 (Link Resolution & Ecosystem Invariants)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_m4_2`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Target Deliverables in `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`:
  `audit-module-01-writing-profile.md` through `audit-module-05-governance-schemas.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Empirically verify relative markdown link resolution across all 5 audit files:
   - Extract every markdown link `[Text](Path)`.
   - Resolve relative to each audit file directory.
   - Verify that 100% of links resolve to existing files on disk. Zero broken links. Zero machine-specific `file://` or `c:\` links.
3. Verify Zero Live Mutation:
   - Check `git diff AGENTS.md CLAUDE.md GEMINI.md`. Confirm zero contract injections or live carrier mutations introduced.
4. Verify Research Preservation:
   - Confirm zero files modified in `01-universal-instruction-research/` or `03-research-of-file-10/`.
5. Run pytest suite: `python -m pytest apex-meta/informatics/tests/ -q`.
6. Formulate structured verdict (**APPROVE** or **REQUEST_CHANGES**).
7. Write `handoff.md` with empirical test evidence and notify orchestrator via `send_message` to Recipient `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`.


## 2026-10-22T13:09:13Z
You are Challenger 2 for Milestone 4 (Plane 4 Infrastructure Module Audits).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_m4_2
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_m4_2\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Inspect relative markdown links in audit-module-01 through audit-module-05 to verify 100% link resolution on disk.
Verify Zero Live Mutation: confirm no new modifications to AGENTS.md, CLAUDE.md, GEMINI.md.
Verify Research Preservation: confirm zero modifications to 01-universal-instruction-research/ and 03-research-of-file-10/.
Run pytest suite: python -m pytest apex-meta/informatics/tests/ -q.
Write handoff.md with empirical evidence and structured verdict (APPROVE or REQUEST_CHANGES) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
