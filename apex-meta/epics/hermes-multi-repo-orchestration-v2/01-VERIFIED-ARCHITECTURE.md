# Verified Architecture — Hermes Multi-Repo Orchestration v2

Status: **RESEARCH COMPLETE ENOUGH FOR OPERATOR DECISIONS / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

## 1. Verified conclusions

### V1 — One Hermes installation can serve multiple repositories

Hermes' reusable primitives are machine/profile level, while project context and project skills are discovered from the active workspace/repository. Therefore one installation does not need to be cloned per repo.

Use one WSL2 runtime containing the managed repo checkouts, one Hermes installation, one Docker policy, and one QMD installation.

### V2 — Profiles are agent/identity boundaries, not repository boundaries

Hermes profiles have independent configuration, sessions, memory, credentials, and profile-local skills. A profile therefore models a durable agent such as `research-strategist`, not `research-strategist-for-acim`.

Do not simultaneously run multiple independent Hermes processes against the same profile state. Use separate profiles when true concurrent independent identity/state is required.

### V3 — Project context stays project-local

Hermes context discovery reads repository/workdir context such as `AGENTS.md`. Project-local skills are also discovered from supported project skill directories after trust.

Therefore project-specific facts/rules should remain with the repo rather than being copied into profile memory.

### V4 — One shared Kanban board + tenants is the strongest native portfolio candidate

Hermes boards are strong isolation boundaries. Hermes documents that links cannot point across boards.

Tenant is a soft namespace inside a board and can be filtered.

Consequently:

```text
one board
  tenant=apex
  tenant=masterofarts
  tenant=acim
  tenant=investment
```

preserves a native cross-repository dependency graph better than:

```text
apex board
masterofarts board
acim board
investment board
```

plus a second aggregate board, which would require duplicated tasks or a synchronization mechanism.

This is still a candidate until live acceptance testing.

### V5 — Apex should be control plane, not project-content warehouse

Apex may version:

- portfolio registry;
- agent/profile specifications;
- shared skill source;
- orchestration ADRs;
- portfolio decision records;
- cross-project summaries and operating views;
- policy and onboarding contracts.

Apex should not automatically copy:

- the entire contents of MasterOfArts, ACIM, Investment or other repos;
- QMD SQLite indexes;
- Hermes Kanban SQLite DB;
- raw Hermes `MEMORY.md`/`USER.md` profile data;
- sessions;
- credentials.

Those already have native owners.

## 2. User stories — reusable profiles

### US-P1 — Researcher moves between repos

```text
TASK A
repo = Investment
profile = research-strategist
workspace = ~/workspaces/Investment
QMD = investment-* collections

research-strategist
  -> reads Investment AGENTS/context
  -> uses its stable research identity/procedures
  -> retrieves Investment evidence
  -> produces Investment artifact
  -> may learn a generic research procedure locally

TASK B
repo = acim-secular
same profile = research-strategist
workspace = ~/workspaces/acim-secular
QMD = acim-site-* collections

same identity/procedural memory
+ different repo context/evidence
= cross-repo capability without factual contamination
```

**Spillover:** generic research methods can persist with the role.  
**No spillover:** Investment holdings/facts should not become ACIM project truth.

### US-P2 — Marketing agent uses shared method but local product truth

```text
marketing-executive
  |
  +-- shared MarketingSkills procedures
  |
  +-- task: MasterOfArts offer
  |     -> MasterOfArts local product-marketing context
  |
  +-- task: ACIM website
        -> acim-secular local product-marketing context
```

The agent is reused. The product facts are not.

### US-P3 — Reviewer audits another agent across repos

```text
research-strategist -> Investment result
                       |
                       v
independent-reviewer --+

marketing-executive -> ACIM result
                       |
                       v
same independent-reviewer
```

Reviewer identity remains stable while repo context changes.

### US-P4 — Concurrent work

Do:

```text
research-strategist -> Investment
marketing-executive -> ACIM
independent-reviewer -> MasterOfArts
```

Avoid:

```text
research-strategist process A -> Investment
research-strategist process B -> Apex
```

at the same time if both mutate the same profile state.

If parallel research becomes necessary, explicitly create another worker identity/profile.

## 3. User stories — shared flows and skills

### Skill class S1 — globally reusable procedure

Examples:

- source-verification checklist;
- exact-match patch generation;
- workshop-curriculum method;
- research synthesis method.

Candidate ownership:

```text
apexai-os-meta
  -> reviewed shared skill source
  -> installed/synced to Hermes-readable shared external skill directory
  -> selected profiles discover metadata
```

Rule: procedure only; no repo-specific facts.

### Skill class S2 — role-specific reusable procedure

Example:

```text
research-strategist
  -> systematic-evidence-review
  -> contradiction-review
  -> source-ranking
```

These can remain profile-local until proven valuable across more than one role.

### Skill class S3 — repository-specific procedure

Example: Apex KB.

```text
apexai-os-meta/.agents/skills/apex-kb/
```

or another currently supported project-local Hermes skill path.

Only Apex tasks should discover the Apex-specific behavior through project precedence.

### Promotion process

```text
repo task exposes useful method
  -> role-local learned procedure
  -> repeated successfully in >1 repo/task class
  -> reviewer removes repo facts and checks overlap
  -> accepted shared skill committed in Apex
  -> distributed through documented Hermes external/project skill mechanism
  -> all intended roles discover metadata
```

Do not automatically promote every learned behavior.

## 4. BMAD and MarketingSkills placement

### MarketingSkills

Verified upstream:

- universal Agent Skills install uses `.agents/skills/`;
- `product-marketing` creates/uses project-local `.agents/product-marketing.md`;
- project-specific product context therefore belongs in each repo that uses the skill.

Target pattern:

```text
shared/installed MarketingSkills procedure library

MasterOfArts/.agents/product-marketing.md
acim-secular/.agents/product-marketing.md
Investment/.agents/product-marketing.md   # only if marketing is relevant
```

Do not centralize each repo's product facts in Apex.

### BMAD

BMAD currently supports Hermes as a platform target, but its official installer model remains project-oriented. An upstream proposal exists for global shared installations via symlinked project discovery; that proposal is not evidence that global shared BMAD is already production-supported.

Therefore v2 must distinguish:

1. **BMAD method as reusable conceptual capability** — may be available to agents;
2. **BMAD project state/assets** — remain in the project repos that actually use BMAD;
3. **future deduplication/global-link behavior** — verify live before adopting.

Do not invent a global BMAD storage scheme before the live installer/runtime proves one.

## 5. Apex information interchange model

The operator idea "repos report upward to Apex and useful learning spills back down" is achievable, but not by copying all data.

Use four channels:

### Channel A — portfolio/task state

Candidate:

```text
ONE Hermes Kanban board
  tenants per repo
```

Apex-level tasks can depend on tasks in project tenants because they remain on one board.

Example:

```text
Apex task: Weekly CEO review
  depends on:
    ACIM launch readiness
    Investment evidence refresh
    MasterOfArts workshop delivery
```

### Channel B — durable cross-project summaries

Apex owns concise durable rollups such as:

```text
portfolio/projects.yaml
portfolio/current-priorities.md
portfolio/cross-project-decisions/
portfolio/weekly-reviews/
```

These contain pointers/status/decisions, not copies of full project KBs.

### Channel C — procedural learning

```text
role-local learned skill
   -> reviewed generalization
   -> Apex shared skill source
   -> distributed to applicable agents
```

This is the first recommended cross-agent learning mechanism.

### Channel D — retrieval

QMD can index curated collections from multiple independent repos.

Apex/orchestrator can retrieve across explicitly selected collections when a portfolio question genuinely requires cross-project evidence.

Example:

```text
CEO asks: What are my three biggest execution blockers?

orchestrator
  -> Kanban tenant filters
  -> QMD query over selected control/status collections
  -> concise synthesis
```

Do not index everything into one unscoped collection.

## 6. QMD deeper explanation

QMD is one local retrieval engine with many named collections.

Example registry:

```text
qmd
  +-- apex-control
  +-- apex-current-epics
  +-- moa-orchestration
  +-- moa-lika
  +-- acim-site-docs
  +-- acim-site-code
  +-- investment-control
  +-- investment-research
```

A collection is a scoped corpus, not another database-of-truth.

Process:

```text
repo files change
  -> qmd update
  -> qmd embed where required
  -> derived index refreshes

Hermes task
  -> decides information is needed
  -> QMD query(collections=[relevant scopes])
  -> local retrieval/reranking
  -> bounded passages returned
  -> only selected passages reach remote reasoning model
```

Portfolio query:

```text
collections=[apex-control, moa-orchestration, investment-control]
```

Project query:

```text
collections=[acim-site-docs]
```

This allows cross-repo knowledge access without physically merging repos.

## 7. Filesystem and CLI clients

### Canonical managed workspace

Current Microsoft/Docker guidance supports keeping Linux-heavy repos in the WSL filesystem for Linux tooling and bind-mounted Docker workloads.

Candidate:

```text
~/workspaces/
  apexai-os-meta/
  MasterOfArts/
  acim-secular/
  Investment/
```

Windows Explorer accesses the same files through `\\wsl.localhost\...`.

### Codex

OpenAI's current Codex Windows documentation states the Windows sandbox is experimental and recommends WSL for the best Windows experience, especially when dependencies/tools live there.

Therefore installing/running Codex CLI in the same WSL workspace is the preferred multi-tool path.

### Claude Code

Claude Code supports Windows directly and also supports WSL. It does not require WSL in the same way. For this architecture, however, running Claude Code inside the same WSL environment removes cross-filesystem path translation and lets Claude, Codex, Hermes, Git, QMD and Docker operate on the same canonical files.

This is an architectural convenience/performance choice, not a claim that native Windows Claude Code is unsupported.

### Antigravity

Antigravity CLI can also run in Linux/WSL, but it is not a permanent architectural dependency. The orchestration must remain usable when Antigravity quota/subscription is unavailable.

## 8. Proposed portable operating experience

The operator should be able to switch executor clients without changing project truth:

```text
Windows Terminal / WSL
  |
  +-- hermes
  +-- codex
  +-- claude
  +-- agy (when available)
       |
       +-- same ~/workspaces repositories
       +-- same Git state
       +-- same repository AGENTS.md
       +-- compatible project Agent Skills where supported
```

Hermes-only state remains Hermes-only:

- Kanban DB;
- profile memories;
- Hermes sessions;
- QMD local MCP/runtime.

Portable state remains Git/repository based:

- AGENTS.md;
- shared/project skill source where the client supports it;
- project truth;
- decisions;
- outputs;
- Apex portfolio registry/summaries.

## 9. What is not yet proven

- A fully automatic repo -> Apex portfolio status synchronization using only upstream Hermes primitives.
- Automatic promotion of learned Hermes skills into a reviewed Git-based Apex shared library.
- A single globally installed BMAD tree reused natively by every repo without project-local installation/linking.
- Cross-profile shared raw Hermes memory without an external provider.
- The exact final QMD collection design for Apex's very large historical corpus.

These remain implementation/research gates; do not fake them with custom scripts until their value is demonstrated.
