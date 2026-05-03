# Browser Chat Prompt Plan: Build Apex AI KB Bases From Master Of Arts Indexes

## Summary

Use one extended-thinking browser chat to build holistic KB bases for all heads/agents named in:

- `ALFRED_KB_BASE_BUILD_INDEX.md`

- `META_HEADS_KB_BASE_BUILD_INDEX.md`

- `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`

The browser chat may read both repos, but **all writes must land only in the new Apex AI repo**. Master Of Arts is source-only. The process must repeatedly check for repo-mixing drift, source coverage gaps, and token-loss artifacts.

## Target KB Outputs In Apex AI Repo

Create or update one KB folder per head/agent using the Apex AI repo’s existing conventions. If no stronger convention exists, use:

- `managed/agent_kb/alfred/`

- `managed/agent_kb/meta_strategy/`

- `managed/agent_kb/meta_detective/`

- `managed/agent_kb/special_ops__knowledge_bank/`

- `managed/agent_kb/special_ops__prompts_workflows/`

- `managed/agent_kb/special_ops__ai_handling_routing/`

- `managed/agent_kb/special_ops__hygiene_clean/`

- `managed/agent_kb/special_ops__informatics_design/`

Each folder should contain:

- `AGENT_CARD.md`

- `ESSENCE.md`

- `BEST_PRACTICES.md`

- `MISTAKES_FAILURES.md`

- `LEARNING_QUEUE.md`

- `TEMPLATES.md`

- `SOURCE_MANIFEST.md`

- `COVERAGE_AUDIT.md`

## General Browser Chat Prompt

```markdown

You are operating in an extended-thinking, iterative prompt flow. Your goal is to create holistic, detail-covering KB bases in the Apex AI repo, using Master Of Arts only as a read-only source repository.

Critical repo rule:

- Master Of Arts is source-only.

- Apex AI is the only write target.

- Do not create, modify, move, rename, or delete anything in Master Of Arts.

- Before every write step, say which repo you are about to write to and confirm it is Apex AI.

- After every major phase, run a repo-mixing drift check: list every file changed and confirm all changed paths are inside Apex AI.

Available source indexes in Master Of Arts:

- `agent_kb_source_indexes/ALFRED_KB_BASE_BUILD_INDEX.md`

- `agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md`

- `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`

Operating method:

1. First inspect the Apex AI repo structure and identify existing KB/agent conventions.

2. Read the three Master Of Arts index files fully.

3. Build a source coverage matrix:

- head/agent name

- source file

- source repo/path

- role: primary/supporting/evidence/duplicate

- read mode

- extraction status

- output files informed

4. Process one head/agent at a time.

5. For each head/agent, read all `primary` sources fully, then supporting sources as needed, then evidence-only sources only for failures, examples, anti-drift, and validation.

6. Do not paste raw source dumps. Distill into reusable KB doctrine, operating rules, examples, templates, and known failure modes.

7. Use source-grounded synthesis. If a detail is inferred, mark it as inferred.

8. Preserve contradictions in `COVERAGE_AUDIT.md`; do not silently smooth over them.

9. If source material is too large, do not produce a shallow summary. Iterate by source clusters and maintain a running extraction ledger.

10. At the end of each head/agent, run:

- source coverage check

- repo-mixing drift check

- role boundary check

- duplicate/contradiction check

- missing-source check

11. At the end of the whole run, create a final root-level manifest in Apex AI:

- `managed/agent_kb/KB_BUILD_MANIFEST.md`

Private reasoning:

- Use extended private reasoning for synthesis and conflict resolution.

- Do not expose full hidden chain-of-thought.

- Instead, expose concise checkpoints: decisions made, source groups covered, uncertainties, and validation results.

Output quality bar:

- The KB must be useful for future agents without rereading all source files.

- Each file must be dense, operational, and specific.

- Avoid generic AI advice.

- Prefer stable rules, role boundaries, workflows, failure patterns, source authority rules, examples, and templates.

- Every KB folder must include a `SOURCE_MANIFEST.md` proving which sources were read or skipped and why.

Hard stop conditions:

- Stop if you are about to write to Master Of Arts.

- Stop if Apex AI repo path is unclear.

- Stop if a required source index cannot be accessed.

- Stop if a generated artifact is only a short summary instead of a usable KB base.

```

## Individual Prompt Part 1: Alfred

```markdown

Build the KB base for `alfred`.

Source index:

- `agent_kb_source_indexes/ALFRED_KB_BASE_BUILD_INDEX.md`

Agent purpose:

Alfred is the user-facing executive aligner and recommendation/training interface. Alfred must help the user navigate life and work through Leela’s gamified sequencing logic.

Primary synthesis focus:

- Alfred identity, boundaries, and first-contact behavior

- holding/orchestration role

- recommendation vs delegation

- user priority intake

- Skill Tree / Epics / Chunks -> Path -> Sequencing -> Rhythm

- daily and weekly training logic

- gamified life-flow recommendations

- relationship to Sid, Algorithm, Meta Ops, and other agents

- when Alfred coaches directly vs routes to another agent

Required extra care:

- Treat Night4 local/manual sources as current product reasoning when available to the chat.

- Keep raw chats as reasoning sources, not final doctrine unless they contain the only available detail.

- Build Alfred as practical operator support, not a generic assistant.

- Include templates for:

- first contact intake

- weekly alignment

- day-start sequencing

- rhythm repair

- recommendation handoff

- escalation to other agents

Required output folder:

- `managed/agent_kb/alfred/`

```

## Individual Prompt Part 2: Meta Heads

```markdown

Build KB bases for:

- `meta_strategy`

- `meta_detective`

Source index:

- `agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md`

`meta_strategy` synthesis focus:

- information architecture strategy

- file taxonomy and artifact choice

- strategic routing and system design decisions

- decision quality, prioritization, and tradeoff framing

- source authority for planning and durable structure

- how to turn messy material into coherent operating systems

- when to recommend architecture changes vs preserve current conventions

`meta_detective` synthesis focus:

- source authority verification

- audit procedure

- drift detection

- contradiction detection

- evidence handling

- failure pattern identification

- red-team posture

- validation gates

- when to escalate uncertainty or block a change

Shared meta-head care:

- Keep strategy and detective roles distinct.

- `meta_strategy` decides structure and direction.

- `meta_detective` verifies, challenges, audits, and prevents drift.

- If a source applies to both, document the difference in how each head uses it.

- Include cross-head handoff templates:

- strategy asks detective for audit

- detective escalates strategic ambiguity

- both produce a joint decision memo

Required output folders:

- `managed/agent_kb/meta_strategy/`

- `managed/agent_kb/meta_detective/`

```

## Individual Prompt Part 3: Special Ops Heads

```markdown

Build KB bases for:

- `special_ops__knowledge_bank`

- `special_ops__prompts_workflows`

- `special_ops__ai_handling_routing`

- `special_ops__hygiene_clean`

- `special_ops__informatics_design`

Source index:

- `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`

Shared Special Ops goal:

Create operational specialist KBs that can support other agents with bounded, high-signal expertise. These KBs should be practical, reusable, and strongly anti-drift.

Per-agent focus:

1. `special_ops__knowledge_bank`

- knowledge capture

- source-to-KB extraction

- durable memory structures

- learning queues

- source manifests and coverage audits

2. `special_ops__prompts_workflows`

- prompt design

- workflow construction

- iterative prompt flows

- handoff prompts

- bounded execution instructions

3. `special_ops__ai_handling_routing`

- model/tool/agent selection

- routing criteria

- escalation rules

- when to use single-agent vs multi-agent flow

- handling constraints and source authority

4. `special_ops__hygiene_clean`

- drift prevention

- cleanup rules

- repository/file hygiene

- duplicate handling

- validation before and after moves/copies

5. `special_ops__informatics_design`

- information design

- file purpose and structure

- taxonomy

- naming, templates, and artifact conventions

- turning raw material into navigable systems

Required extra care:

- Do not collapse these five specialists into one generic operations KB.

- Keep each role narrow and sharp.

- Use evidence-only sources for failures and anti-patterns, not as doctrine.

- Include reusable checklists for each specialist.

- Include a cross-specialist routing map showing when one specialist should call another.

Required output folders:

- `managed/agent_kb/special_ops__knowledge_bank/`

- `managed/agent_kb/special_ops__prompts_workflows/`

- `managed/agent_kb/special_ops__ai_handling_routing/`

- `managed/agent_kb/special_ops__hygiene_clean/`

- `managed/agent_kb/special_ops__informatics_design/`

```

## Validation Plan

The browser chat must finish with these checks:

- Changed-file list contains only Apex AI repo paths.

- No Master Of Arts files were modified.

- Every head/agent has all required KB files.

- Every `SOURCE_MANIFEST.md` lists read/skipped/blocked sources.

- Every `COVERAGE_AUDIT.md` lists gaps, contradictions, and confidence.

- `KB_BUILD_MANIFEST.md` summarizes all generated folders.

- All source links to Master Of Arts are treated as references only.

- The output is not a shallow summary; it is a usable KB base.

## Assumptions

- The Apex AI repo has or should accept a `managed/agent_kb/<agent>/` structure.

- Master Of Arts remains the source repository.

- The browser chat can access the three index files through the GitHub connector.

- Local/manual attachment files from the indexes should be used if attached in that browser chat; otherwise they must be marked as unavailable in `SOURCE_MANIFEST.md`

Build KB bases for:

- `meta_strategy`

- `meta_detective`

Source index:

- `agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md`

`meta_strategy` synthesis focus:

- information architecture strategy

- file taxonomy and artifact choice

- strategic routing and system design decisions

- decision quality, prioritization, and tradeoff framing

- source authority for planning and durable structure

- how to turn messy material into coherent operating systems

- when to recommend architecture changes vs preserve current conventions

`meta_detective` synthesis focus:

- source authority verification

- audit procedure

- drift detection

- contradiction detection

- evidence handling

- failure pattern identification

- red-team posture

- validation gates

- when to escalate uncertainty or block a change

Shared meta-head care:

- Keep strategy and detective roles distinct.

- `meta_strategy` decides structure and direction.

- `meta_detective` verifies, challenges, audits, and prevents drift.

- If a source applies to both, document the difference in how each head uses it.

- Include cross-head handoff templates:

- strategy asks detective for audit

- detective escalates strategic ambiguity

- both produce a joint decision memo

Required output folders:

- `managed/agent_kb/meta_strategy/`

- `managed/agent_kb/meta_detective/`