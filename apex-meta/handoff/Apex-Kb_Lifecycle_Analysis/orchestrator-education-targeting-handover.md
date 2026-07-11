---
doc_type: claude-code-handover
task_id: claude-code-orchestration-design-orchestrator-targeting
version: 2
created: 2026-07-11
updated: 2026-07-11
authority: SINGLE_SOURCE_OF_TRUTH
supersedes: v1 of this same file — v1's structure let an executing agent spend an entire session on decisions/maintenance and return zero new content, which was not the ask
mode: read-write (KB content only, under existing apex-kb constraints)
writes_allowed_to: [apex-meta/kb/claude-code-orchestration-design/**]
writes_forbidden: [repo root, .claude/, apex-plan/sync/session/PreCap/FlowRecap/APSU state, source-knowledge/**]
---

# Handover — Author High-Value Wiki Pages So an AI Can Become a Master Orchestrator

## 0. THE DELIVERABLE (read this paragraph twice — it is the whole point)

**Your job this session is to write new, high-value wiki pages** (`wiki/summaries/`, `wiki/concepts/`, `wiki/entities/`) in `apex-meta/kb/claude-code-orchestration-design/`, covering the seven areas in §3, each one real, source-grounded, and useful enough that another AI reading only the wiki tier becomes meaningfully better at designing Claude Code agents/subagents/skills/workflows. **A session that ends with only frontmatter fixes, index rebuilds, or a round of operator questions — and zero new authored pages — has failed this handover, even if every deterministic check passes.** Say so explicitly if that happens; do not report it as progress.

A prior run of a v1 version of this handover did exactly that failure: it spent ~20 minutes asking the operator five separate maintenance/decision questions, patched frontmatter on 25 existing pages, rebuilt an index, and returned **zero new pages**. Do not repeat this. The fix: resolve decisions fast (§1, one batch, defaults where safe), then spend the great majority of the session on §3/§4 authoring.

## 1. Fast preamble — batch this, don't multi-turn it

Ask the operator these in **one message**, proceed on defaults if no answer arrives quickly, and move on to authoring regardless:

- Reconciling `wiki/*/max-run-20260709/` duplicate topics against the root pages (defer if operator says so — do not let this block new-page authoring either way).
- Anything else procedural you notice. If it's genuinely low-stakes (a script patch, a naming choice, a maintenance item), **default and proceed** — do not spend a turn asking permission for something reversible and cheap. Only stop for things this repo's constraints actually require confirmation for (batch-writing many files at once, deleting/moving content, mutating state/ files).

Do not treat this section as a place to camp. One batch, then §3.

## 2. Ground truth (context, not a to-do list)

Read `log/lifecycle-completion-report-20260710.md` once for background. As of that report: 74 pages under flat `wiki/{concepts,entities,summaries}/` are real, source-grounded, and clean (`quality --strict` passes on all of them). A separate `wiki/*/max-run-20260709/` (25 pages) duplicates many of the same topics and had a lint-blocking frontmatter defect — a later maintenance pass may already have patched this; re-run `quality --json` / `lint --json` yourself rather than trusting any prior number, including this handover's.

None of this is your deliverable. It's background so you don't re-author what already exists or misdiagnose stale state as broken. Spend five minutes here, not fifty.

## 3. The seven areas to author — this is the actual task

For each area below, author at least one strong `wiki/summaries/*.md` page (plus supporting `concepts/`/`entities/` pages where a single summary can't carry the material). "Strong" means: real Macro/Meso/Micro synthesis, multiple specific Key Claims with real source pointers (not file-level-only), Routes Here, and honest Uncertainty triggers — not a heading-complete shell. Ground every claim in the actual raw corpus below; if a claim can't be grounded, mark it `working_hypothesis` and say why, don't invent detail to sound complete.

1. **agent-subagent-design** — when to use a subagent vs. inline work, context isolation, tool-scoping, ephemeral vs. persistent identity.
2. **skill-package-design** — `SKILL.md` structure, frontmatter requirements, progressive disclosure, granularity/splitting rules.
3. **workflow-design** — fixed pipelines vs. open agent loops, the named workflow patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer).
4. **commands-hooks-rules-memory** — how slash commands, hooks, CLAUDE.md rules, and persistent memory interact with skills/subagents.
5. **prompt-pack-and-artifact-contracts** — structured handoff/output contract design (cross-reference the operator's own Apex artifact-contract work rather than duplicating it).
6. **external-repo-patterns** — patterns mined from the downloaded practitioner repos (BMAD-METHOD, personal-os, claude-agents, awesome-claude-code, Aider, SWE-agent) — translate as evidence, never revive as a runtime spec verbatim.
7. **apex-application-patterns** — how the above patterns map onto this specific Apex system (cross-reference, don't rebuild it here).

Source priority when citing (from `manifests/migration/source-root-map.json`):
- **P0** — `raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23/` (official Anthropic Agent Skills docs/spec/repos). Cite first.
- **P0-P1** — `raw/source-groups/claude-skill-design/`, `raw/source-groups/skill-design-best-practices/`.
- **P1-P3** — `raw/source-groups/claude-orchestration-agents/` (practitioner repos — translate, don't copy runtime specifics).
- **P2** — `raw/source-groups/prompt-engineer-research-base/` (supporting only, for area 5).

Use the `apex-kb` skill's Phase 2 per-page loop (draft → validate → retry ≤2 → escalate to `audit/` if still failing) — don't hand-roll a different process. Work in small batches (2-3 related pages), but **keep batching through all seven areas in this same session** rather than stopping after the first batch to ask what's next.

## 4. After authoring (not before, and not instead of)

Once the seven areas each have a real page:
- Author target queries into `query-eval-pack.json` from the seven areas above (this is easy once the pages exist — the queries are literally "what would someone ask each page").
- Run the deterministic postflight (`index`, `retrieval build-index`, `lint --strict`, `quality --strict`, `audit`, `status`) and report actual pass/fail — don't claim `query_ready` unless it actually is.

## 5. What NOT to do

- Do not spend the session on decisions, frontmatter, or index rebuilds and call it done. If maintenance work is genuinely needed, do it in minutes, then author pages.
- Do not re-author the 74 already-good root pages from scratch.
- Do not silently delete or move `max-run-20260709/` or any other existing content.
- Do not invent claims or Adaptive Ranked Source Set entries — ground in real files, mark gaps as `working_hypothesis`.
- Do not implement the semantic-acceptance tooling redesign from `Apex-KB-Semantic-Quality-Realization-Handover.md` as a prerequisite — it was validated but never built, and manual grounding discipline (real claim IDs, honest confidence downgrades) already works. Don't block authoring on building it.

## 6. Definition of done — check this first, before anything else

- [ ] Seven areas in §3 each have at least one new, strong, source-grounded summary page. **This is the primary criterion. If this box isn't checked, the session failed regardless of what else got done.**
- [ ] Target queries authored and tried against the new pages.
- [ ] Deterministic checks run and reported honestly (pass or named failure, not silence).
