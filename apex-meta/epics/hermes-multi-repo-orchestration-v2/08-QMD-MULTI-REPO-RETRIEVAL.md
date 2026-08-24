# 08 — QMD Multi-Repo Retrieval

Status: **D08 VERIFIED / LIVE MULTI-PROFILE ACCEPTANCE TEST REQUIRED**  
Date: 2026-08-24

## Direct answer

**Yes.** An agent working only inside one repo can have QMD available without moving to Apex or merging repositories.

But distinguish two layers:

```text
QMD ENGINE / INDEX REGISTRY
  machine-level local service/config

QMD MCP CONNECTION
  must be configured for each Hermes profile that should use it
```

Once the QMD MCP server is configured in a Hermes profile, Hermes' official QMD integration says the agent receives the QMD tools automatically without loading the QMD skill on every task.

QMD collection scoping is independent of current directory: current QMD syntax explicitly states `-c` / MCP `collections` matches collection names and **works from any directory**.

Therefore:

```text
research-strategist working in Investment
  -> same local QMD installation
  -> MCP connection in research-strategist profile
  -> collections=[investment-control, investment-evidence]

same research-strategist later in acim-secular
  -> same QMD installation
  -> same MCP connection
  -> collections=[acim-control, acim-site-docs]
```

No duplicate QMD installation is needed.

## Native architecture

```text
                    ONE QMD LOCAL ENGINE
                           |
           +---------------+---------------+
           |               |               |
     QMD collection   QMD collection   QMD collection
       Investment          ACIM          MasterOfArts
           |               |               |
           +---------------+---------------+
                           |
                         MCP
                           |
       +-------------------+-------------------+
       |                   |                   |
research-strategist   independent-reviewer  other approved
Hermes profile        Hermes profile         Hermes profile
       |
       v
active repo/workspace determines project context;
explicit QMD collections determine retrieval corpus
```

## Important condition — profile MCP configuration

Hermes profiles isolate config and MCP connections. Therefore "one QMD engine" does **not** mean a brand-new independent profile automatically knows about QMD.

Each reusable profile that requires retrieval must receive the approved QMD MCP declaration.

Possible proven mechanisms:

1. configure QMD once in each live profile;
2. package the MCP declaration in an Apex-controlled Hermes profile distribution and install/update the role profile through the native distribution mechanism.

Profile distributions deliberately preserve local memory/session/auth while distributing MCP/config/skills, making option 2 attractive after acceptance testing.

## Collection registry candidate

```text
QMD global registry
|
+-- apex-control
+-- apex-current-epics
|
+-- moa-control
+-- moa-lika
+-- moa-ipos
|
+-- acim-control
+-- acim-site-docs
+-- acim-site-code
|
+-- investment-control
+-- investment-evidence
+-- investment-code
```

Names are candidates; exact corpus masks must be designed from each repo's current authority structure.

## Collection behavior verified upstream

QMD supports:

```bash
qmd collection add ~/work/docs --name docs
qmd collection add /absolute/path --name name --mask "..."
qmd collection include <name>
qmd collection exclude <name>
qmd search "..." -c <name>
qmd query "..." -c <name>
```

MCP uses plural collection scope:

```json
{
  "searches": [
    {"type": "lex", "query": "current project blocker"},
    {"type": "vec", "query": "what prevents release"}
  ],
  "collections": ["investment-control"],
  "limit": 10
}
```

Current QMD explicitly warns that a singular MCP field `collection` is silently ignored. Use `collections`.

## Default-search policy

Unscoped QMD queries search every collection marked `includeByDefault: true`.

That is convenient for personal notes but dangerous for a multi-repo orchestration estate because it can:

- retrieve irrelevant projects;
- mix stale/history corpora into current work;
- increase local retrieval/reranking latency;
- return passages the task did not need;
- increase downstream provider context.

### Recommended v2 policy

```text
Project-heavy collections: exclude from default search
Apex tiny control collection: optionally default-included
Every project task: explicit collections
Every portfolio task: explicit selected control collections
```

Example:

```text
Investment task
collections=[investment-control, investment-evidence]

ACIM code task
collections=[acim-control, acim-site-code]

CEO portfolio question
collections=[apex-control, moa-control, acim-control, investment-control]
```

Do not use a default "search all repos" behavior for ordinary work.

## How an agent knows its repo's collections

Do not hard-code project collections into the reusable role profile.

Put routing metadata with the project context, for example a concise repo `AGENTS.md` pointer:

```yaml
Hermes/QMD retrieval:
  control: investment-control
  evidence: investment-evidence
  code: investment-code
  rule: use explicit collections; do not query other repos unless task requires it
```

This means the same role profile can move repos without carrying a permanent Investment QMD assumption.

## QMD context descriptions

QMD supports hierarchical collection/path context descriptions. Upstream documentation emphasizes that descriptive context improves retrieval decisions.

Use descriptions to say **what authority a corpus represents**, not repeat the corpus itself.

Example:

```text
investment-control
  "/" = "Current Investment operating docs, runbooks and accepted control-plane decisions. Excludes old chat dumps and raw external research."
```

## QMD is derived state, not project truth

```text
Git repo files   = canonical truth
QMD index        = rebuildable retrieval structure
QMD context      = retrieval metadata
```

If QMD is deleted, project truth must still exist in Git/filesystem.

## Refresh flow

```text
accepted repo change
   |
   v
qmd update
   |
   +-- BM25/index refresh
   |
   v
qmd embed    # where semantic embeddings are required/pending
   |
   v
qmd status / retrieval test
```

Do not automatically run expensive full re-embedding for every tiny change without measuring need.

## Local compute vs provider cost

| Operation | Network/model provider tokens | Local cost |
|---|---:|---|
| QMD BM25 search | 0 | SQLite/CPU |
| vector search | 0 provider tokens | local embedding model |
| hybrid/rerank | 0 provider tokens | local GGUF models/CPU/RAM |
| update/index | 0 provider tokens | disk/CPU |
| embed | 0 provider tokens | CPU/GPU/RAM/time |
| Hermes reasoning over returned passage | provider dependent | returned passage enters model context |

## Project-local `.qmd` configuration caution

QMD supports project-local configuration, but August 2026 security reports showed checked-in `.qmd/index.yml` could influence update hooks, collection paths and models. Fixes/trust gates have been landing rapidly.

For v2 multi-repo orchestration:

- prefer a machine-owned QMD registry for the cross-repo collection map;
- do not blindly trust repo-provided `update:` commands;
- inspect exact installed QMD version/current trust behavior before enabling project-local automation;
- avoid using project-local QMD config as a way for one repo to point at unrelated repos.

This reduces supply-chain/path-scope ambiguity.

## Code retrieval

Current QMD supports AST-aware chunking for TypeScript, JavaScript, Python, Go and Rust via the documented automatic chunk strategy.

Use only after a code collection has a demonstrated retrieval need.

Do not index the entire large Apex estate by default. Curate current control/code domains and exclude historical/recovery/vendor/bulk corpora.

## User stories

### US-Q1 — Investment-only session

```text
cd ~/workspaces/Investment
research-strategist
  -> loads Investment AGENTS.md
  -> QMD MCP tools already present from profile config
  -> queries collections=[investment-control, investment-evidence]
  -> never needs to enter Apex checkout
```

### US-Q2 — same profile, ACIM later

```text
cd ~/workspaces/acim-secular
research-strategist
  -> loads ACIM project context
  -> same QMD MCP connection
  -> collections=[acim-control, acim-site-docs]
```

The QMD engine is shared; the retrieval scope changes.

### US-Q3 — Apex portfolio question

```text
portfolio-orchestrator
  -> reads latest deterministic board rollup
  -> only if deeper evidence needed:
     QMD collections=[apex-control, moa-control, acim-control, investment-control]
  -> synthesizes decision view
```

Do not search project code/evidence collections unless required.

## Acceptance tests

For **every profile intended to use QMD**:

- [ ] MCP QMD server appears in profile config/runtime;
- [ ] QMD tools available in a fresh session without loading QMD skill manually;
- [ ] from `~/workspaces/Investment`, query `investment-control` succeeds;
- [ ] from the same cwd, query `acim-control` also technically succeeds when explicitly requested (proves cwd independence);
- [ ] ordinary Investment instruction selects only Investment collections;
- [ ] unscoped query does not search excluded large project collections;
- [ ] plural `collections` is used in MCP calls;
- [ ] known control question returns current authoritative source;
- [ ] deliberately stale/historical result is not promoted as current authority;
- [ ] after a known source edit, update/embed/freshness test succeeds;
- [ ] QMD removal/rebuild would not destroy canonical project data.

## Runtime-source precedence

QMD and Hermes are changing quickly. At implementation time use:

1. installed `qmd --version` / current MCP schema;
2. installed Hermes MCP tool discovery;
3. current QMD primary docs/source;
4. current Hermes QMD integration docs;
5. this architecture file.

The MasterOfArts pilot already observed that published Hermes QMD skill tool names can lag the actual QMD MCP schema. Do not code against stale names.

## Primary sources

- QMD README: https://github.com/tobi/qmd/blob/main/README.md
- QMD query syntax/scoping: https://github.com/tobi/qmd/blob/main/docs/SYNTAX.md
- QMD example global registry: https://github.com/tobi/qmd/blob/main/example-index.yml
- QMD project-local trust issue #886: https://github.com/tobi/qmd/issues/886
- QMD path/model trust issue #889: https://github.com/tobi/qmd/issues/889
- Hermes QMD integration: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- Hermes QMD skill source: https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/research/qmd/SKILL.md
- Hermes Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes Profile Distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
