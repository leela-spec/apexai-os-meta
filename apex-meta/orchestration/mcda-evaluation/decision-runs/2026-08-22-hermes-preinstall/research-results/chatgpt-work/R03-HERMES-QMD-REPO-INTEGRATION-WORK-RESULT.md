# R03 — Hermes + QMD + MasterOfArts Repository Integration — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**Track status:** **PASS**  
**Verdict:** `QMD_INTEGRATION_CONFIRMED`

## Executive decision

The official Hermes QMD skill and QMD's native MCP server provide the required connection. No wrapper, custom MCP service, RAG router or synchronization layer is needed. Run Hermes and QMD together in WSL2, use stdio MCP for the baseline, keep the index/config outside the repository, define non-overlapping family collections, exclude sensitive/legacy collections from unscoped queries, and make `qmd update` plus `qmd embed` an explicit native freshness gate after accepted repository changes.

One upstream documentation contradiction is real but bounded: the current Hermes QMD page lists older mode-specific MCP tool names, while QMD 2.8.3 exposes `query`, `get`, `multi_get`, and `status`. The installed MCP server is the runtime authority. Hermes' dynamic MCP names should therefore be validated in QA (normally the server prefix plus current QMD name), and no compatibility wrapper should be written.

## Verified installation/configuration chain — **DO NOT EXECUTE**

Current upstream evidence on 2026-08-23:

- QMD package version: **2.8.3**, MIT, Node `>=22`; local models and SQLite index.
- Hermes official QMD skill: v1.0, MIT; documented for macOS/Linux and installed with Hermes' native skill installer.
- QMD supports stdio MCP (`qmd mcp`) and an optional localhost HTTP MCP endpoint.

```bash
# DO NOT EXECUTE — research evidence only
hermes skills install official/research/qmd
npm install -g @tobilu/qmd

qmd collection add /repo/MasterOfArts/Orchestration --name moa-orchestration
qmd collection add /repo/MasterOfArts/ACIM --name moa-acim
qmd collection add /repo/MasterOfArts/Lika --name moa-lika
qmd collection add /repo/MasterOfArts/IPOS --name moa-ipos
qmd collection add /repo/MasterOfArts/Business --name moa-business

qmd collection exclude moa-business
qmd collection exclude moa-ipos
qmd context add qmd://moa-orchestration "Approved Master of Arts orchestration and decision records"
qmd context add qmd://moa-lika "Lika operating system, evidence, patches, and accepted artifacts"

qmd update
qmd embed
qmd status
```

The path examples are illustrative WSL paths and must be replaced by the real checkout. No collection command was run. `moa-business` is excluded from default search because it contains financial/identity data; it may be queried only by explicit collection name in an authorized task. IPOS is excluded by default because it is an OpenClaw-era design corpus rather than current Hermes authority.

```yaml
# ~/.hermes/config.yaml — DO NOT EXECUTE
mcp_servers:
  qmd:
    command: qmd
    args: ["mcp"]
    timeout: 30
    connect_timeout: 45
```

Use stdio first: it avoids an unauthenticated network listener. If HTTP is later justified for heavy multi-client use, QMD defaults to `localhost:8181/mcp`; do not bind `0.0.0.0`. QMD documents host/origin validation on loopback and warns that broad binding weakens that protection.

## Windows/WSL verdict

Hermes documents Windows 10/11 and WSL2 as Tier 1, but the official Hermes QMD skill declares macOS/Linux. Current QMD contains native-Windows support evidence, including a Windows sqlite-vector package and Windows/CUDA notes, yet that does not override the Hermes skill's declared platform. The supported combined target is therefore **WSL2**, with repository, Hermes, Node/QMD and its local models inside the same WSL environment. Docker is not required for QMD; it is an optional isolation boundary and complicates path/memory access.

## Collection strategy grounded in the live tree

| Collection | Path | Default? | Reason |
|---|---|---:|---|
| `moa-orchestration` | `Orchestration/` | Yes | Current scope, ADRs, runbooks and decision state |
| `moa-acim` | `ACIM/` | No initially | Private/method material; authorize per task |
| `moa-lika` | `Lika/` | Yes for Lika tasks | Strong evidence/governance corpus with patch ambiguity requiring source-aware retrieval |
| `moa-ipos` | `IPOS/` | No | Legacy OpenClaw-oriented design evidence, not current authority |
| `moa-business` | `Business/` | No | Financial/contact/tax/bank sensitivity |
| historical `OpenClaw/` | separate optional collection only | No | Large historical/implementation corpus; high contamination and token risk |

Do not add one whole-repository collection on top of these because that double-indexes files and weakens scope. Do not create a collection for every micro-project until actual volume/use justifies it; QMD can filter within a family and `get` exact paths. Minimal QMD context strings describe corpus identity only. They must not duplicate AGENTS hierarchy or project facts.

## Exact call flow and I/O contract

```text
Operator/Kanban task
 -> Hermes provider model reads task + concise context
 -> Hermes activates official QMD skill
 -> Hermes MCP client calls current QMD server tool
 -> qmd query runs local lexical/vector/HyDE subqueries and local reranking
 -> QMD returns ranked paths/snippets/docids/context/scores
 -> Hermes optionally calls qmd get or multi_get for exact bounded passages
 -> selected passages enter the next provider-model prompt
 -> result is written to declared repository artifact and attached to task
```

Current MCP contract:

| Tool | Key input | Output/use |
|---|---|---|
| `query` | required `searches` array (1–10 typed `lex`/`vec`/`hyde` searches); optional `collections` **array**, intent, limit, score/rerank controls | Ranked results with URI/path, title, context, score and snippet |
| `get` | file/docid plus optional line range | Exact line-numbered document excerpt/full text |
| `multi_get` | list/glob of paths/docids | Multiple exact documents/excerpts |
| `status` | none | Index/collection/model status |

The singular `collection` MCP parameter is silently ignored by current QMD; callers must use `collections: ["moa-lika"]`. CLI `search`, `vsearch`, and `query` still exist, but the current MCP server consolidates retrieval under typed `query`.

## Deterministic/AI, tokens, cost and privacy

| Stage | D/AI/hybrid | Where | Extra cloud call/cost | Privacy/egress |
|---|---|---|---|---|
| Scan/update files | Deterministic | Local WSL/SQLite | None | Local file paths/content indexed locally |
| BM25 lexical search | Deterministic | Local QMD | None | Local |
| Embedding/vector search | Local model inference | Local GGUF | No provider tokens | Local; about 2 GB model download/storage class |
| HyDE/query expansion/rerank | Local model inference | Local QMD | No provider tokens | Local |
| Hermes decides query/tool | AI | Configured provider | Yes | Task/context sent to provider |
| Returned passages synthesized | AI | Configured provider | Yes; proportional to selected snippets | Only selected passages egress, not the whole index |

QMD's HTTP daemon can use roughly 2 GB RAM under the documented heavy-use setup. The retrieval budget should be: scoped collection, small result limit, minimum score, then exact line-ranged `get`. This is native progressive retrieval, not custom compression.

Hermes filters stdio MCP environments to safe system variables plus explicit `env` values and redacts secrets. Do not forward repository/provider credentials to QMD; it does not need them for a local checkout. QMD data and models live in user cache/config locations; filesystem permissions must protect them. The index is derived but sensitive because it contains excerpts from private files.

## Freshness using existing mechanisms

1. Repository file remains the only canonical truth.
2. Accepted task writes/updates the file through normal Git review.
3. Before a retrieval-dependent task or after a material accepted change, run native `qmd update` to rescan additions/updates/removals.
4. Run `qmd embed` for documents reported as needing embeddings; use `-f` only after a model change or diagnosed corruption.
5. Check `qmd status`; record freshness completion in the Kanban task comment/checklist.
6. If a result cites a moved/deleted path, QMD warns and the worker refreshes before continuing.

QMD offers native per-collection update hooks, including commands run before `qmd update`, and project-local `.qmd/index.yml` trust gates. They are not needed here: QMD reads the already-active checkout, and an automatic `git pull` inside it could conflict with local work. Keep operator-owned config in the normal user config and use the explicit refresh gate. This is not manual duplication of facts; it is rebuilding a derived index.

## Failure/recovery matrix

| Failure | Detection | Recovery | No custom layer |
|---|---|---|---|
| `qmd` missing/wrong Node | MCP start/`qmd doctor` fails | Repair supported install/version; rerun doctor | Yes |
| MCP tool-name mismatch | Hermes reports unknown tool | Inspect current MCP `status`/tool schema and update configuration/QA expectation | Yes; no wrapper |
| Stale result/path | Warning, missing file or freshness check | `qmd update`, then `qmd embed`, repeat query | Yes |
| Corrupt/incompatible embeddings | `doctor`/fingerprint/status error | Re-embed (`qmd embed -f`) | Yes |
| Sensitive cross-family result | Collection field absent/wrong | Stop; repeat with explicit `collections` array and inspect task authorization | Yes |
| HTTP endpoint exposure | Listener/firewall check | Stop daemon; return to stdio/loopback | Yes |
| Memory pressure | Process metrics/failure | Use stdio, reduce concurrency/batch size, or resource-limit container | Yes |
| Update hook fails | `qmd update` aborts remaining collections | Fix/clear native hook; rerun update | Yes |

## Retrieval simulations

### Current decision authority

Call `query` with lexical and semantic searches for the approved Hermes architecture and `collections: ["moa-orchestration"]`; retrieve the ADR and scope lines with `get`. Expected: ADR-002/scope/runbook evidence only, not historical OpenClaw designs.

### Lika patch drift

Call `query` for cumulative patch order and editorial drift with `collections: ["moa-lika"]`; retrieve `dry-run-report.md` and the current governance file by exact path. Expected: both the claimed current rule and contradiction/patch warning are visible.

### Business confidentiality

An unscoped query must not include `moa-business` because it is excluded by default. An authorized invoice task explicitly names `collections: ["moa-business"]`, returns only bounded passages, and does not mix ACIM/Lika context.

### Missing Awakenings family

A query scoped to a nonexistent `moa-awakenings` collection should fail/return no such scope. The worker must report the absence, not search all collections and invent a project.

## Evidence review

The first draft inherited the Hermes page's older MCP tool names. Review against QMD 2.8.3 corrected the runtime contract to `query/get/multi_get/status`, documented the contradiction, and retained the official unmodified integration. Review also removed an unnecessary Git-pull update hook and avoided a duplicate whole-repository collection.

**Review result:** **PASS** — official Hermes skill + native QMD MCP meets the locked capability with a supported WSL path and no custom connection.

## Sources

- [Hermes official QMD skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd)
- [QMD repository and current README](https://github.com/tobi/qmd)
- [QMD package metadata](https://github.com/tobi/qmd/blob/main/package.json)
- [Hermes security](https://hermes-agent.nousresearch.com/docs/user-guide/security/)
- [Hermes platform support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
