# R03 — Hermes + QMD + MasterOfArts Repository Integration Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — QMD is a locked target component**  
Depends on: R02 project/context mapping  
Decision owner: Human CEO

## Decision question

How does the **official Hermes QMD integration** operate against the real MasterOfArts repository so that project knowledge is searchable, project scopes remain distinguishable, context/token waste is controlled, and no custom retrieval service has to be built?

QMD is not being evaluated as a replacement knowledge base. The canonical files remain the project files. QMD is the retrieval/index layer over them.

## Hard rules

- use current official Hermes QMD documentation and current `tobi/qmd` repository;
- no custom RAG server;
- no custom MCP server;
- no custom vector database;
- no new canonical copy of project knowledge inside QMD;
- no hand-waved Windows/WSL support;
- prove exact inputs/outputs and update behavior;
- classify local deterministic work, local model computation and cloud model reasoning separately.

## Primary official sources

- Hermes QMD skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- Hermes MCP/client configuration docs as linked by the QMD skill
- Hermes platform support: https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
- QMD repository/README: https://github.com/tobi/qmd

## Current upstream facts to verify/reconfirm

QMD currently documents:

- local installation through npm/Bun;
- collections that point to existing directories;
- BM25 keyword search;
- vector semantic search;
- hybrid query expansion/fusion/reranking;
- local GGUF/model execution;
- CLI JSON/file outputs for agents;
- MCP `query`, `get`, `multi_get`, `status` tools;
- stdio local MCP and localhost HTTP modes;
- collection scoping;
- file update/re-index and embedding operations.

Hermes currently documents an official QMD skill/integration.

## Research tasks

### 1. Installation chain

Document the exact upstream installation/configuration chain:

```text
operator
 -> install Hermes official QMD skill
 -> install QMD runtime/dependencies
 -> configure Hermes MCP/QMD connection
 -> define QMD collections
 -> build/update index
 -> Hermes calls QMD query/get tools
```

For each step record:

| Step | Command/config | Official source | Local/remote | Requires auth/API? | Writes where? | Expected result |
|---|---|---|---|---|---|---|

Do not execute commands during this research run.

### 2. Windows/WSL path

The target operator uses Windows. Determine exactly:

- whether Hermes itself runs native Windows or WSL2 for the intended stack;
- what the Hermes QMD skill officially supports;
- whether QMD itself supports the target environment;
- whether Node/Bun/local model dependencies work in that supported environment;
- how paths from the MasterOfArts repo are addressed;
- whether stdio MCP works across the chosen environment boundary;
- whether Docker is required/recommended for safety and how that affects QMD access;
- whether any step becomes an unsupported hack.

Result must be `SUPPORTED`, `SUPPORTED_WITH_OFFICIAL_WSL_PATH`, or `BLOCKED/UNVERIFIED`.

### 3. Repository collection design from actual project boundaries

Use R02's validated project-family/micro-project model.

Determine which QMD collection strategy is supported and operationally useful:

- one collection for entire repo;
- collection per project family;
- selected project/family collections plus shared organization context;
- another upstream-supported collection arrangement.

Do not choose based on aesthetic folder preferences. Test retrieval behavior and update burden.

For each candidate show:

| Collection strategy | Query scoping | Cross-project leakage risk | Index duplication | Update burden | Agent usability | Fits R02 hierarchy? |
|---|---|---|---|---|---|---|

### 4. QMD context metadata

QMD supports context metadata for collections/paths. Determine whether and how that can represent existing project meaning without creating a second manual knowledge hierarchy.

For each proposed context entry answer:

- who maintains it;
- whether it duplicates an `AGENTS.md` or project file;
- whether QMD requires it for retrieval quality;
- whether it can be generated/read from existing durable metadata through an upstream-supported mechanism;
- whether manual synchronization would be required.

Reject a design that requires maintaining the same project description independently in many systems.

### 5. Exact call path

For a semantic request such as:

> Find the most relevant prior material for group grounding exercises in the current workshop family.

Trace:

```text
Hermes reasoning
 -> chooses QMD skill/tool
 -> Hermes MCP client sends structured call
 -> local QMD query
 -> QMD local query expansion/search/reranking
 -> ranked results
 -> Hermes receives selected snippets/paths
 -> Hermes optionally calls get/multi_get
 -> only retrieved text enters model context
 -> Hermes reasons/writes output
```

For every edge classify:

`deterministic | local-model computation | cloud-model inference | no model`.

### 6. Input/output contract

Record the exact useful I/O for:

- `query`;
- `get`;
- `multi_get`;
- `status`;
- index/update;
- embeddings.

Show what Hermes sees and what stays only in QMD's local index.

### 7. Token/cost analysis

Separate:

- QMD local computation;
- QMD local models;
- data returned into Hermes context;
- subsequent cloud model tokens;
- index storage/disk;
- network calls.

The research must state whether QMD itself causes cloud token/API charges in the documented local setup.

### 8. Privacy/security analysis

Verify:

- where the QMD index lives;
- whether stdio stays local;
- localhost HTTP behavior;
- authentication or lack thereof;
- QMD host/origin protections;
- risk of binding HTTP beyond localhost;
- what environment variables/credentials Hermes passes to MCP subprocesses;
- how the R01 safety profile should treat QMD.

### 9. Freshness/update behavior

Simulate:

```text
project file changes
 -> QMD update/reindex
 -> embeddings refreshed where required
 -> old/deleted file behavior
 -> next query returns current material
```

Determine the supported automation options for keeping the index current without building a custom watcher if an upstream mechanism already exists.

### 10. Failure/recovery

Simulate:

- QMD not installed;
- index missing;
- stale embeddings;
- QMD process dead;
- one collection path moved;
- MCP tool unavailable;
- query returns low relevance;
- QMD local model cannot load.

For each record whether Hermes can detect/report the failure and what official recovery step exists.

## Required retrieval simulations

Use real repo content where possible:

1. exact query for a known file/concept;
2. semantic query where terminology differs;
3. project-family-scoped query;
4. cross-document query inside one family;
5. intentionally ambiguous query that could retrieve unrelated project material;
6. changed-file + index refresh;
7. query that returns only enough lines/passages for the task rather than full documents.

For each record:

| Query | Collections | QMD tool | Returned paths/passages | Context size | Relevant? | Wrong-project leakage? | Follow-up get needed? |
|---|---|---|---|---|---|---|---|

## Required output

1. verified installation/configuration chain;
2. Windows/WSL support verdict;
3. collection strategy recommendation grounded in real project structure;
4. exact Hermes-QMD call flow;
5. deterministic/AI classification;
6. token/cost/privacy matrix;
7. update/freshness process using existing mechanisms;
8. failure/recovery matrix;
9. retrieval simulations;
10. exact commands/config examples from official sources, marked `DO NOT EXECUTE` during research;
11. verdict:
   - `QMD_INTEGRATION_CONFIRMED`
   - `QMD_PLATFORM_BLOCKER`
   - `QMD_CONTEXT_MODEL_CONFLICT`
   - `CUSTOM_CONNECTION_REQUIRED`.

## Failure condition

If the target requires us to write a custom QMD wrapper, custom MCP service, custom RAG router, or manual synchronization layer between the repo and QMD, stop and report the blocker instead of designing it.
