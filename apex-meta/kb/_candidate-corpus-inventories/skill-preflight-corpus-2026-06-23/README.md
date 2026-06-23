# Skill Preflight Corpus Inventory - 2026-06-23

## Status

This folder preserves the accidental broad preflight run originally created under:

- apex-meta/kb/skill-design-best-practices

This is not a semantic Apex KB ingest.

It contains deterministic preflight/hash metadata only:

- source paths
- source hashes
- source storage modes
- proposed analysis paths
- phase gate status
- category grouping added after the fact

No Phase 1 semantic analysis files were generated.
No Phase 2 wiki pages were generated.
No source manifest entries were accepted as curated sources.

## Why this exists

A broad PowerShell run recursively preflighted many local source files. The run took a long time and covered potentially useful future corpora, especially public skill examples and local Apex skills. Instead of discarding the work, this folder preserves it as a reusable candidate-corpus inventory.

## Counts

- Preflight reports preserved: 1890

## Category Counts

- skill-example-corpus: 1536
- legacy-prompt-workflow-research: 174
- local-apex-skills: 118
- therapy-narm-existing-kb: 34
- prompt-engineer-research-base: 16
- apex-meta-internal: 9
- other: 3

## Top Directory Roots

- source-knowledge/ProjectRepos/antigravity-awesome-skills-main/plugins: 1427
- source-knowledge/old_openclaw-KB&Agents/special_ops__prompts_workflows/appendices: 92
- source-knowledge/old_openclaw-KB&Agents/special_ops__prompts_workflows/NewResearchBlueprints: 75
- source-knowledge/ProjectRepos/antigravity-awesome-skills-main/docs_zh-CN: 52
- source-knowledge/ProjectRepos/antigravity-awesome-skills-main/docs: 24
- source-knowledge/ProjectRepos/antigravity-awesome-skills-main/.github: 22
- .claude/skills/apex-plan/references: 18
- apex-meta/kb/prompt-engineer-research-base/raw: 14
- .claude/skills/PrecapNextDay/examples: 14
- source-knowledge/Apex&Claude_old/.claude/skills: 10
- apex-meta/kb/therapy/wiki: 9
- apex-meta/kb/therapy/raw: 9
- .claude/skills/PrecapNextDay/templates: 8
- .claude/skills/PrecapNextDay/references: 7
- source-knowledge/ProjectRepos/antigravity-awesome-skills-main/data: 5
- .claude/skills/project-kb-manager/references: 4
- .claude/skills/ProjectStatus/FirstIteration: 4
- source-knowledge/ProjectRepos/antigravity-awesome-skills-main/apps: 3
- apex-meta/kb/apex-kb-skill-test/wiki: 3
- apex-meta/handoff: 3
- apex-meta/harmonization: 3
- .claude/skills/apex-plan/templates: 3
- source-knowledge/design-docs: 3
- apex-meta/kb/apex-kb-skill-test/ingest-analysis: 3
- apex-meta/kb/prompt-engineer-research-base/log: 2
- .claude/skills/apex-kb/references: 2
- .claude/skills/apex-kb/templates: 2
- .claude/skills/Workflow&Processes/workflow-record-contract.md: 1
- source-knowledge/old_openclaw-KB&Agents/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md: 1
- .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md: 1

## Files

### Derived indexes

- derived/preflight-inventory.csv
- derived/preflight-inventory.json
- derived/category-counts.csv
- derived/top-directory-roots.csv
- derived/duplicate-analysis-paths.csv
- derived/candidate-skill-example-corpus.csv
- derived/candidate-local-apex-skills.csv
- derived/candidate-legacy-prompt-workflow-research.csv

### Raw archive

- archive/raw-preflight-reports.zip
- archive/source-preflight-list.jsonl

### Human summary

- accidental-run-inventory-summary.md

## Future KB split

| KB slug | Intended use | Candidate source class |
|---|---|---|
| skill-design-best-practices | Canonical external best-practice research | Official docs, specs, papers, selected official examples only |
| skill-example-corpus | Empirical analysis of real-world skill/package patterns | skill-example-corpus category |
| apex-skill-review-rubric | Review local Apex skills against best practices | local-apex-skills category |
| prompt-workflow-design | Prompt/workflow/process guardrail research | legacy-prompt-workflow-research category |
| apex-system-meta-kb | Internal Apex architecture/handoff/harmonization memory | apex-meta-internal category |

## Operational warnings

Do not treat this archive as curated ingest.
Do not directly replay the original source list.
Do not ingest all entries into skill-design-best-practices.

Before future ingest:

1. Choose one target KB.
2. Filter one category.
3. Select a small explicit allowlist.
4. Generate stable source slugs from path, not basename.
5. Run preflight only on the allowlist.
6. Create Phase 1 analysis files.
7. Stop before Phase 2 until operator approval.

## Recommended next use

For skill-example-corpus, start with:

1. top-level repo README/docs
2. 10-30 representative skill folders
3. only each skill's SKILL.md first
4. then selected references/templates if needed

Do not start by ingesting all 1,536 files.
