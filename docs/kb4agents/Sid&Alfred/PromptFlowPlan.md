# Browser Chat Prompt Plan: Build Apex AI KB Bases From Master Of Arts Indexes

## Summary

Use one extended-thinking browser chat to build each holistic KB bases for all heads/agents named in:

- ALFRED_KB_BASE_BUILD_INDEX.md
- META_HEADS_KB_BASE_BUILD_INDEX.md
- SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

The browser chat may read both repos, but **all writes must land only in the new Apex AI repo**. Master Of Arts is source-only. The process must repeatedly check for repo-mixing drift, source coverage gaps, and token-loss artifacts.

## Target KB Outputs In Apex AI Repo

Create or update one KB folder per head/agent using the Apex AI repo’s existing conventions. If no stronger convention exists, use:

- managed/agent_kb/alfred/
- managed/agent_kb/meta_strategy/
- managed/agent_kb/meta_detective/
- managed/agent_kb/special_ops__knowledge_bank/
- managed/agent_kb/special_ops__prompts_workflows/
- managed/agent_kb/special_ops__ai_handling_routing/
- managed/agent_kb/special_ops__hygiene_clean/
- managed/agent_kb/special_ops__informatics_design/

Each folder should contain:

- AGENT_CARD.md
- ESSENCE.md
- BEST_PRACTICES.md
- MISTAKES_FAILURES.md
- LEARNING_QUEUE.md
- TEMPLATES.md
- SOURCE_MANIFEST.md
- COVERAGE_AUDIT.md

## General Browser Chat Prompt

``You are operating in an extended-thinking, iterative prompt flow. Your goal is to create holistic, detail-covering KB bases in the Apex AI repo, using Master Of Arts only as a read-only source repository. Critical repo rule: - Master Of Arts is source-only. - Apex AI is the only write target. - Do not create, modify, move, rename, or delete anything in Master Of Arts. - Before every write step, say which repo you are about to write to and confirm it is Apex AI. - After every major phase, run a repo-mixing drift check: list every file changed and confirm all changed paths are inside Apex AI. Available source indexes in Master Of Arts: - `agent_kb_source_indexes/ALFRED_KB_BASE_BUILD_INDEX.md` - `agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md` - `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` Operating method: 1. First inspect the Apex AI repo structure and identify existing KB/agent conventions. 2. Read the three Master Of Arts index files fully. 3. Build a source coverage matrix: - head/agent name - source file - source repo/path - role: primary/supporting/evidence/duplicate - read mode - extraction status - output files informed 4. Process one head/agent at a time. 5. For each head/agent, read all `primary` sources fully, then supporting sources as needed, then evidence-only sources only for failures, examples, anti-drift, and validation. 6. Do not paste raw source dumps. Distill into reusable KB doctrine, operating rules, examples, templates, and known failure modes. 7. Use source-grounded synthesis. If a detail is inferred, mark it as inferred. 8. Preserve contradictions in `COVERAGE_AUDIT.md`; do not silently smooth over them. 9. If source material is too large, do not produce a shallow summary. Iterate by source clusters and maintain a running extraction ledger. 10. At the end of each head/agent, run: - source coverage check - repo-mixing drift check - role boundary check - duplicate/contradiction check - missing-source check 11. At the end of the whole run, create a final root-level manifest in Apex AI: - `managed/agent_kb/KB_BUILD_MANIFEST.md` Private reasoning: - Use extended private reasoning for synthesis and conflict resolution. - Do not expose full hidden chain-of-thought. - Instead, expose concise checkpoints: decisions made, source groups covered, uncertainties, and validation results. Output quality bar: - The KB must be useful for future agents without rereading all source files. - Each file must be dense, operational, and specific. - Avoid generic AI advice. - Prefer stable rules, role boundaries, workflows, failure patterns, source authority rules, examples, and templates. - Every KB folder must include a `SOURCE_MANIFEST.md` proving which sources were read or skipped and why. Hard stop conditions: - Stop if you are about to write to Master Of Arts. - Stop if Apex AI repo path is unclear. - Stop if a required source index cannot be accessed. - Stop if a generated artifact is only a short summary instead of a usable KB base.``

## Individual Prompt Part 1: Alfred

`` Build the KB base for `alfred`. Source index: - `agent_kb_source_indexes/ALFRED_KB_BASE_BUILD_INDEX.md` Agent purpose: Alfred is the user-facing executive aligner and recommendation/training interface. Alfred must help the user navigate life and work through Leela’s gamified sequencing logic. Primary synthesis focus: - Alfred identity, boundaries, and first-contact behavior - holding/orchestration role - recommendation vs delegation - user priority intake - Skill Tree / Epics / Chunks -> Path -> Sequencing -> Rhythm - daily and weekly training logic - gamified life-flow recommendations - relationship to Sid, Algorithm, Meta Ops, and other agents - when Alfred coaches directly vs routes to another agent Required extra care: - Treat Night4 local/manual sources as current product reasoning when available to the chat. - Keep raw chats as reasoning sources, not final doctrine unless they contain the only available detail. - Build Alfred as practical operator support, not a generic assistant. - Include templates for: - first contact intake - weekly alignment - day-start sequencing - rhythm repair - recommendation handoff - escalation to other agents Required output folder: - `managed/agent_kb/alfred/` ``