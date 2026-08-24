# R06 — AnythingLLM Integration and Fit

Status: **RESEARCH REQUIRED**  
Depends on: R01  
Candidate identity: `Mintplex-Labs/anything-llm`

## Decision question

Does current AnythingLLM provide a verified superior knowledge/RAG/workspace/agent capability that should supplement or replace any part of the Hermes + repo + QMD pipeline, and can it do so without creating a second conflicting knowledge or orchestration system?

## Primary source families

- https://github.com/Mintplex-Labs/anything-llm
- https://docs.anythingllm.com
- current releases/source/tests
- current issues/PRs for workspace isolation, MCP, agents, knowledge and security behavior
- Hermes/QMD docs only where direct comparison/integration is claimed

## Research tasks

### 1. Establish current AnythingLLM product architecture

Verify current behavior of:

- Desktop vs Docker/server variants;
- workspaces;
- document ingestion/chunking/vector stores/RAG;
- workspace/chat memory;
- agents;
- Agent Flows/no-code workflows;
- Agent Skills if current;
- MCP client/server direction and transport support;
- model routing/provider support/local LLMs;
- scheduled/automated jobs;
- permissions/multi-user behavior;
- API/developer interfaces;
- storage locations and backup/export.

Record current release/license/platform support.

### 2. Compare against baseline modules

Directly compare:

- AnythingLLM workspaces vs repo root/family/micro context;
- AnythingLLM RAG/vector DB vs QMD;
- AnythingLLM agents/flows vs Hermes profiles/Kanban;
- AnythingLLM memory vs Hermes memory/Curator;
- AnythingLLM skills vs Agent Skills/BMAD/MarketingSkills;
- model router vs Hermes provider routing;
- scheduling vs Hermes/Kanban scheduling if current.

For each determine whether adoption would `REPLACE`, `SUPPLEMENT`, `DUPLICATE`, or be `ORTHOGONAL`.

### 3. Canonical-truth and synchronization analysis

Trace exactly what happens if MasterOfArts project files are ingested/indexed:

```text
repo file -> ingestion -> parsed/chunked representation -> vector/index storage -> workspace retrieval -> model prompt -> generated output
```

Determine:

- whether source files remain canonical;
- index refresh behavior after edits/deletes;
- whether workspace documents are copies/imports;
- how provenance/path/metadata survives;
- how project-family isolation works;
- whether multiple workspaces share global filesystem/skill resources;
- backup/rebuild behavior.

Search current issues for cross-workspace/global-resource leakage or isolation limitations and verify affected version/status.

### 4. Integration with Hermes/QMD

Investigate only current established paths:

A. AnythingLLM replaces QMD and Hermes calls it through an official interface.
B. AnythingLLM consumes QMD over MCP.
C. AnythingLLM exposes a useful MCP/API endpoint Hermes officially consumes.
D. Both remain separate apps sharing repo artifacts only.
E. Custom bridge would be needed.

For each, verify client/server direction and exact tools/resources. Shared MCP compatibility alone does not prove a usable edge.

### 5. Project hierarchy / shared specialist test

Can one stable specialist work across separate MoA project families without contaminating:

- workspace knowledge;
- memory;
- skills;
- prompts;
- document retrieval;
- output location?

Compare this with the baseline workdir + AGENTS + QMD collection model.

### 6. User-story simulations

Trace with real mechanisms:

1. ingest/retrieve research for a workshop family;
2. update a source file and ensure stale index behavior is controlled;
3. same marketing specialist across two workspaces/projects;
4. maker/reviewer or equivalent workflow;
5. local/private knowledge task;
6. AnythingLLM/Hermes interaction if and only if a proven integration exists;
7. interrupted/restarted service recovery.

### 7. Cost/privacy/security

Verify:

- core license/commercial use;
- desktop/server deployment;
- local vs remote embeddings/models;
- API keys/provider billing;
- ChatGPT/Codex subscription compatibility if any;
- vector DB/default storage;
- network/data egress;
- credential handling;
- community skills/security model;
- Windows support;
- RAM/storage/maintenance implications;
- multi-user/permission boundaries where relevant.

### 8. Established-value evidence

Use releases/tests/issues/first-party operational evidence. Separate broad product adoption from proof that the exact MoA integration is reliable.

### 9. Decision

Choose among:

- `REPLACE_QMD`
- `SUPPLEMENT_HERMES_KNOWLEDGE`
- `USE_AS_SEPARATE_UI_ONLY`
- `PILOT_FOR_SPECIFIC_USE_CASE`
- `DEFER`
- `REJECT_DUPLICATE_OR_SYNC_BURDEN`
- `REJECT_CUSTOM_INTEGRATION_REQUIRED`

State exactly which baseline module disappears if AnythingLLM is added.

## Required output

1. current AnythingLLM architecture;
2. module overlap/replacement matrix;
3. knowledge ingestion/truth/freshness flow;
4. exact Hermes/QMD integration evidence;
5. project isolation/shared-specialist analysis;
6. seven user-story simulations;
7. cost/privacy/security/platform table;
8. operational evidence/current limitations;
9. recommendation and switching conditions;
10. source registry.

## Pass standard

Pass only when the result distinguishes a genuinely superior knowledge/workspace capability from adding a second database/UI/control plane that must be synchronized with the repo/Hermes/QMD system.
