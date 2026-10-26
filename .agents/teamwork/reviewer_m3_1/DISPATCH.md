# Task Assignment: Milestone 3 Reviewer 1 (Architecture & Sections)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m3_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Prototype: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-01-target.md`
- Target Deliverables Authored by `worker_m3_1`:
  - `rule-16-authoring.md`
  - `rule-17-trade-off.md`
  - `rule-18-handover.md`
  - `rule-19-iterative.md`
  - `rule-20-schemas.md`
  - `rule-21-sync.md`
  - `rule-22-pointers.md`
- Worker Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m3_1\handoff.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Inspect all 7 authored rule files.
3. Verify each file conforms to the 5 mandatory sections and OKF v0.2 frontmatter (`status: current_truth`).
4. Run `python -m pytest apex-meta/informatics/tests/ -q` and verify all tests pass.
5. Provide structured verdict (APPROVE or REQUEST_CHANGES) in `handoff.md` and send message to Orchestrator (`a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).

## 2026-10-22T12:40:18Z
You are Reviewer 1 for Milestone 3 (Rules 16-22).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m3_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m3_1\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Inspect the 7 files authored by worker_m3_1 in apex-meta/informatics/final/research/06-layered-rule-kb/: rule-16-authoring.md through rule-22-pointers.md.
Verify all 5 mandatory sections and OKF v0.2 frontmatter exist in each file.
Run pytest suite: python -m pytest apex-meta/informatics/tests/ -q.
Write handoff.md with structured verdict (APPROVE or REQUEST_CHANGES) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
