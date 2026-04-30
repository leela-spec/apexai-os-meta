# Handover: Redo Special Ops KB Source Lists In Master Of Arts Repo

## Situation

The current generated Special Ops KB source index was created from `[REPO_ROOT]`, but the actual files are now understood to be inside the Master of Arts repo. The next agent must redo the list from inside the Master of Arts repo where it has real file access.

Do not trust the earlier classification that files are external just because they are outside `apexai-os-meta`. In the redo run, treat the Master of Arts repo as the accessible source root and resolve all paths relative to that repo.

## Goal

Create an agent-mode index for building the KB base of each Special Ops agent.

The index must:

- list all files relevant for each Special Ops agent
- group files by Special Ops agent
- rank files per agent by importance for that agent's KB
- use only files actually accessible through the Master of Arts repo as repo-accessible entries
- place any files still outside the Master of Arts repo in a separate manual-attachment list
- use embedded clickable Markdown links for every file

## Special Ops Agents To Cover

- `special_ops__knowledge_bank`
- `special_ops__prompts_workflows`
- `special_ops__ai_handling_routing`
- `special_ops__hygiene_clean`
- `special_ops__informatics_design`

## Required Output

Create one master index file in the Master of Arts repo, preferably:

`agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`

If that folder does not exist, create a similarly named folder such as:

`kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`

The file must have this structure:

```md
# Special Ops KB Base Build Index

## Repo-Accessible Files

### special_ops__knowledge_bank

1. [filename.md](</absolute/path/inside/Master of Arts repo/filename.md>)
   - role: `primary|supporting|evidence|duplicate`
   - read: `read full|skim|use as evidence only`
   - reason: one short reason

### special_ops__prompts_workflows

...

### special_ops__ai_handling_routing

...

### special_ops__hygiene_clean

...

### special_ops__informatics_design

...

## Files Outside Master Of Arts Repo To Attach Manually

### special_ops__knowledge_bank

1. [filename.md](</absolute/path/outside/repo/filename.md>)

...
```

## Important Formatting Requirement

All file references must be clickable blue links in the Codex desktop app.

Use this exact Markdown form:

```md
[filename.md](</C:/absolute/path/with spaces/filename.md>)
```

Do not output plain `C:\...` paths when the user needs to click them.

## Control Sources From Previous Run

Use the previous run as orientation only, not as final truth:

- [SPECIAL_OPS_KB_BASE_BUILD_INDEX.md](</[REPO_ROOT]/agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md>)
- [special_ops__knowledge_bank.md](</[REPO_ROOT]/agent_kb_source_indexes/special_ops__knowledge_bank.md>)
- [special_ops__prompts_workflows.md](</[REPO_ROOT]/agent_kb_source_indexes/special_ops__prompts_workflows.md>)
- [special_ops__ai_handling_routing.md](</[REPO_ROOT]/agent_kb_source_indexes/special_ops__ai_handling_routing.md>)
- [special_ops__hygiene_clean.md](</[REPO_ROOT]/agent_kb_source_indexes/special_ops__hygiene_clean.md>)
- [special_ops__informatics_design.md](</[REPO_ROOT]/agent_kb_source_indexes/special_ops__informatics_design.md>)

If these paths are not available in the Master of Arts repo session, proceed from the local ledgers and repository search instead.

## Preferred Evidence Sources In Master Of Arts Repo

Search for and use these first if present:

- `ROLE_AND_KB_TARGET_MAP.md`
- `KB_RANKINGS_BY_AGENT.md`
- `SOURCE_INVENTORY_LEDGER.md`
- `MASTER_IDEA_LEDGER.md`
- `FAILURE_AND_ANTI_DRIFT_LEDGER.md`
- `ESSENCE_CANDIDATES.md`
- `ResourceScreeningLedgers`
- `AllAIBestPractice`
- `AIHowTo`
- `04_final-system-setup`

Expected search roots from the earlier task:

- `OpenClaw/OpenClaw/07_finalopenclawsystem/NewFinals/ResourceScreeningLedgers`
- `OpenClaw/OpenClaw/04_final-system-setup`
- `OpenClaw/AIHowTo`
- `Ressources/AllAIBestPractice`

In the Master of Arts repo, discover the actual equivalent locations with `rg --files`.

## Selection Rules

- Start from `KB_RANKINGS_BY_AGENT.md` if it exists.
- Pull all `strong_candidate` items for each Special Ops agent.
- Add missing high-value files from `AIHowTo`, `AllAIBestPractice`, and `04_final-system-setup` when not already represented.
- Prefer distilled, final, canon, essence, guide, checklist, index, and ledger files over raw chats.
- Use raw chats, patches, diffs, and postmortems mainly as evidence unless they contain a unique process rule.
- Do not promote archived or failure material into live authority.
- If a file fits multiple agents, place it under the most specific owner and cross-reference or duplicate it as supporting only where useful.
- If no owner is obvious but the file is high impact, put it in a short residual/manual-placement section.

## Ranking Guidance By Agent

### special_ops__knowledge_bank

Highest value:

- KB architecture
- source indexing
- evidence ledgers
- file taxonomy
- capture rules
- canonical storage and retrieval practices
- duplicate handling

### special_ops__prompts_workflows

Highest value:

- prompt flow
- workflow design
- handover discipline
- prompt design best practices
- execution handoff
- no-drift interaction patterns
- chat-to-artifact conversion practices

### special_ops__ai_handling_routing

Highest value:

- model routing
- API cost/performance
- agent selection
- research agent handling
- routing rules
- task decomposition
- multi-agent interaction patterns

### special_ops__hygiene_clean

Highest value:

- cleanup rules
- repo/file hygiene
- drift prevention
- validation
- audit checklists
- failure postmortems
- SSOT realignment
- patch evidence for cleanup failures

### special_ops__informatics_design

Highest value:

- information design canon
- terminology
- file taxonomy
- audit checklists
- prompt flow as information architecture
- execution handover
- open questions for information design
- orchestration architecture

## Validation Checklist

Before finalizing:

- Verify every repo-accessible path exists inside the Master of Arts repo.
- Verify each Special Ops agent has a ranked section.
- Verify every link is clickable Markdown using absolute path angle-bracket syntax.
- Verify files outside the Master of Arts repo are separated into the manual-attachment section.
- Verify no raw transcript is ranked as primary when a distilled/final/canon source exists.
- Verify duplicate representatives are not promoted twice as separate primary sources.
- Verify each ranked repo-accessible entry has role, read mode, and reason.

## Final Response To User

When done, keep the response short and provide only the link to the new index file, for example:

```md
[SPECIAL_OPS_KB_BASE_BUILD_INDEX.md](</absolute/path/inside/Master of Arts repo/agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md>)
```

If the user asks for files outside the repo, answer with only clickable links, one per line, grouped by agent if needed. No prose.
