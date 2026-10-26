# Task Assignment: Milestone 1 Reviewer 2 (Provenance, Research Links & Failure Modes)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m1_2`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Prototype: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-01-target.md`
- Target Deliverables Authored by `worker_m1_1`: `rule-02-product-first.md` through `rule-08-context.md`
- Worker Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_1\handoff.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Inspect bidirectional research links (§4) across all 7 files: verify links to `RESULTS-01..11`, `RP-01..10`, Plane 4 rules (`AD`, `WP`, `EM`, `FA`, `GS`), and external literature.
3. Check §5 Failure Modes & Not-To-Dos (`WP-25`) across all 7 files for technical depth and non-default constraints.
4. Run `python -m pytest apex-meta/informatics/tests/ -q`.
5. Provide structured verdict (APPROVE or REQUEST_CHANGES) in `handoff.md` and send message to Orchestrator (`a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).


## 2026-10-22T11:41:53Z
Sender: a1918f04-9801-41c9-a8a4-6cebbbfab6ed
Priority: MESSAGE_PRIORITY_HIGH
Content:
You are Reviewer 2 for Milestone 1 (Rules 02-08).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m1_2
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m1_2\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Inspect the 7 files authored by worker_m1_1 in apex-meta/informatics/final/research/06-layered-rule-kb/: rule-02 through rule-08.
Verify bidirectional research links (§4) and failure modes & not-to-dos (§5 WP-25) across all 7 files.
Run pytest suite: python -m pytest apex-meta/informatics/tests/ -q.
Write handoff.md with structured verdict (APPROVE or REQUEST_CHANGES) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
