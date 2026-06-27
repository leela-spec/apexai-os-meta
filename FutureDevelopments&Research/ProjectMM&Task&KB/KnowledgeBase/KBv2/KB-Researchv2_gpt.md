# Research report — best KB / memory / retrieval architecture for Apex + Claude Code

## Executive verdict

**Best architecture for Apex is a layered repo-native system, not a single memory product.**

```yaml
recommended_architecture:
  canonical_source_of_truth:
    - repo_committed_markdown_yaml_json
    - raw_source_snapshots_or_pointers_with_hashes
    - compiled_apex_kb_wiki_pages
    - deterministic_python_indexes_and_lint_reports

  always_loaded_memory:
    - tiny_CLAUDE_md_control_plane
    - path_scoped_rules_only_when_needed

  operational_procedures:
    - Claude_native_skills
    - apex-kb
    - apex-plan
    - apex-sync
    - apex-session
    - PromptEngineer / prompt-engineer

  retrieval_stack:
    v1_best:
      - file_manifest
      - markdown_index
      - SQLite_FTS5_BM25_or_plain_Python_index
      - deterministic_query_outputs
    v2_optional:
      - local_vector_index
      - hybrid_BM25_plus_vector
    escalation_only:
      - MCP_servers
      - hosted_vector_DBs
      - cloud_file_search
      - SaaS_project_memory
```

**Core decision:** Apex should use **`CLAUDE.md` + Claude Skills + `apex-kb` / llm-wiki-style compiled KB + deterministic Python + local lexical retrieval** as the canonical stack. Add **local vector search only after the file-first/BM25 system is stable**. Use **MCP and hosted/cloud memory only as adapters or escalation layers**, not as the canonical memory.

This fits Apex’s actual repo state: `.claude/Claude.md` defines Apex as a Claude-native orchestration system that creates structured plans, lets Marco execute, and converts evidence into durable project state; it also defines the core loop as `PreCapWeek → PreCapNextDay → OperatorExecutesPlannedFlow → FlowRecap → APSU → next_PreCapNextDay`. The current repo also already separates planning/support skills from missing durable-memory loop pieces like FlowRecap, StatusMerge, RawFlowDumpNormalize, and ModelUsageLog.

---

## 1. The best answer to the primary question

### Should Apex be built primarily from `CLAUDE.md`, Auto Memory, llm-wiki, MCP memory servers, vector/BM25 retrieval, repo-native Markdown, hosted memory, or a combination?

**Answer:** a **layered combination**, with **repo-native Markdown/YAML/JSON + deterministic Python + compiled KB** as the center.

|Layer|Best role in Apex|Verdict|
|---|---|---|
|`CLAUDE.md`|Tiny always-loaded operating constitution|**Use, but keep small.**|
|Claude Auto Memory|Personal preference / repeated correction memory|**Do not use as canonical Apex state.**|
|Claude Skills|Procedures, gates, artifact contracts, progressive disclosure|**Core control plane.**|
|`apex-kb` / llm-wiki|Source custody, raw source preservation, compiled wiki, query/audit/lint|**Core KB engine.**|
|Markdown task/KG systems|Project/task/status substrate|**Use selectively; adapt patterns, not full systems.**|
|SQLite FTS5 / BM25|Cheap, local, deterministic first retrieval layer|**Best v1 retrieval engine.**|
|Local vector DB|Optional semantic recall layer|**Add v2, not v1 dependency.**|
|MCP memory servers|Tool bridge / optional graph memory|**Adapter, not source of truth.**|
|Hosted/cloud retrieval|Expensive or privacy-sensitive escalation|**Use only for high-value external research or team scale.**|

---

## 2. Why `CLAUDE.md` cannot be the whole memory system

Claude Code’s official memory docs say each session starts with a fresh context window and that durable knowledge is carried through two mechanisms: human-written `CLAUDE.md` files and Claude-written Auto Memory. ([Claude API Docs](https://docs.anthropic.com/en/docs/claude-code/memory "How Claude remembers your project - Claude Code Docs")) They also explicitly say both are loaded as context, **not enforced configuration**, and Auto Memory is loaded into every session only up to “first 200 lines or 25KB.” ([Claude API Docs](https://docs.anthropic.com/en/docs/claude-code/memory "How Claude remembers your project - Claude Code Docs"))

For Apex, that means:

```yaml
CLAUDE_md_should_hold:
  - system_identity
  - core_loop
  - trigger_phrases
  - forbidden_actions
  - artifact_paths
  - startup_protocol

CLAUDE_md_should_not_hold:
  - raw_research_corpus
  - full_project_state
  - all_recaps
  - all_prompt_packets
  - all_KB_pages
  - complete_process_definitions
```

Claude’s docs also recommend keeping `CLAUDE.md` under about 200 lines and moving multi-step procedures into skills or path-scoped rules when it grows. ([Claude API Docs](https://docs.anthropic.com/en/docs/claude-code/memory "How Claude remembers your project - Claude Code Docs")) This exactly matches Apex’s direction: `.claude/Claude.md` should stay a **routing constitution**, while `.claude/skills/*` and `apex-meta/kb/*` carry the heavy operational memory.

---

## 3. Why Claude Skills are the correct procedure layer

Claude Code skills are designed for reusable procedures: official docs say skills extend Claude by adding a `SKILL.md`, load when relevant or by `/skill-name`, and are preferable when a repeated checklist or procedure would otherwise bloat `CLAUDE.md`. ([Claude API Docs](https://docs.anthropic.com/en/docs/claude-code/skills "Extend Claude with skills - Claude Code Docs")) The Agent Skills standard also frames a skill as a folder with `SKILL.md`, optional scripts, references, assets, and progressive disclosure, where only name/description are loaded at startup and full instructions load on demand. ([agentskills.io](https://agentskills.io/ "Agent Skills Overview - Agent Skills"))

This is almost perfectly aligned with Apex:

```yaml
Apex_skill_layer:
  apex-kb:
    owns: source custody, raw/compiled KB, query, lint, audit
  apex-plan:
    owns: project decomposition and planning
  apex-sync:
    owns: deterministic read-side task/index/drift reports
  apex-session:
    owns: session state, handoff files, gated mutation records
  prompt-engineer:
    owns: prompt packet creation, validation, reuse, learning loop
```

Anthropic’s skill guidance also says code is appropriate when deterministic reliability is needed; their example notes that sorting by token generation is more expensive than running a sorting algorithm and that deterministic code makes workflows repeatable. ([Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills "Equipping agents for the real world with Agent Skills \ Anthropic")) This supports Apex’s current Python-only script direction.

---

## 4. Apex-specific evidence from the repo

### 4.1 `apex-kb` is already the right KB spine

The current `apex-kb` skill declares itself as the tool for scaffolding, ingesting, compiling, querying, linting, and auditing durable Apex KBs under `apex-meta/kb/<kb-slug>/`, producing source-preserving KB artifacts, ingest analysis, wiki pages, saved queries, deterministic health reports, and audit flags.

Its data layout already has the right shape:

```txt
apex-meta/kb/<kb-slug>/
  README.md
  kb-schema.md
  raw/articles/
  raw/papers/
  raw/notes/
  raw/refs/
  ingest-analysis/
  wiki/index.md
  wiki/concepts/
  wiki/entities/
  wiki/summaries/
  manifests/source-manifest.json
  audit/
  outputs/queries/
  log/
```

That layout is explicitly defined in the skill contract.

Most importantly, `apex-kb` already encodes the architectural principle Apex needs: raw sources are immutable, exact source filename/path must be preserved, missing sources must never be treated as verified, and generated pages require source pointers.

### 4.2 `apex-sync` is the right deterministic retrieval/status layer

`apex-sync` is already defined as a deterministic read-side synchronization package: next actions, blockers, stale tasks, registry previews, drift checks, dependency validation, priority, urgency, unlock depth, and focus candidates are delegated to `scripts/apex_sync.py`.

The package manifest locks it to seven files, including `scripts/apex_sync.py`, and makes Python standard-library-only, dry-run default, and no task mutation part of the invariant set.

This is exactly what Apex needs for token efficiency: Claude should not read every task file and “reason over the registry” when a script can compute the task graph, blockers, stale state, and drift.

### 4.3 `apex-session` is the right continuity layer

`apex-session` is already scoped to session state, gated mutation records, state deltas, entity update records, handoff files, and next-session context. It explicitly does **not** rank tasks, scan blockers, rebuild registries, compute scores, run scripts, or decompose work.

It also preserves the H6 handoff artifact set:

```txt
task_plan.md
findings.md
progress.md
next-session.md
```

and validates `next-session.md` sections as `Current Step`, `Open Items`, `Risks`, `Decisions Made`, and `Next Actions`.

That makes `apex-session` the right answer to “memory between sessions,” not Claude Auto Memory.

---

## 5. Retrieval architecture recommendation

### Recommended v1: local lexical retrieval first

Use **SQLite FTS5 / BM25** or a standard-library Python fallback as the first retrieval layer.

Why:

|Criterion|SQLite FTS5 / BM25|Local vector DB|
|---|--:|--:|
|Local/cost-free|Excellent|Good, but embeddings add setup/cost/compute|
|Deterministic|Excellent|Medium; embedding models change behavior|
|Easy to rebuild|Excellent|Medium|
|Token efficient|Excellent|Excellent after setup|
|Citation/source pointer fidelity|Excellent|Requires careful metadata|
|Semantic recall|Medium|Excellent|
|Apex v1 fit|**Best**|Optional v2|

SQLite FTS5 includes built-in `bm25()` ranking, `highlight()`, `snippet()`, and rank support. Its docs specify that better BM25 matches are assigned numerically lower values and can be ordered directly with `ORDER BY bm25(ft)` or `ORDER BY rank`. ([sqlite.org](https://www.sqlite.org/fts5.html "SQLite FTS5 Extension"))

**Canonical v1 retrieval flow:**

```yaml
apex_retrieval_v1:
  1_query_parse:
    - classify query as project_state, source_research, prompt_packet, recap, task_sync, or session_context

  2_manifest_filter:
    - search source-manifest.json
    - filter by kb_slug, page_type, project, source_authority, freshness, tags

  3_lexical_search:
    - SQLite FTS5 over wiki pages + summaries + source pointers
    - use bm25/rank
    - return top 5-12 candidate pages

  4_context_pack:
    - include title
    - page_path
    - source_pointer
    - short snippet
    - confidence/freshness flags
    - contradictions/open_questions

  5_llm_synthesis:
    - read only selected pages
    - cite source pointers
    - output answer + evidence table + gaps

  6_save_if_useful:
    - optionally save to outputs/queries/
    - optionally promote to synthesis page after operator approval
```

### Recommended v2: local hybrid retrieval

Add local vector search only after the KB has enough compiled pages to justify semantic retrieval. Qdrant can run locally via Docker and stores data under a local `qdrant_storage` directory by default, but its own quickstart warns the default local instance has no encryption or authentication unless secured. ([qdrant.tech](https://qdrant.tech/documentation/quickstart/ "Local Quickstart - Qdrant")) FAISS is a strong local similarity-search library, but it is a vector-search toolkit rather than a full source-custody or memory system. ([arXiv](https://arxiv.org/abs/2401.08281?utm_source=chatgpt.com "The Faiss library"))

**Best v2 pattern:**

```yaml
hybrid_retrieval_v2:
  lexical:
    engine: SQLite_FTS5_BM25
    owns:
      - exact_terms
      - IDs
      - artifact names
      - dates
      - paths
      - source citations

  semantic:
    engine_options:
      - Qdrant_local
      - FAISS
      - LanceDB
      - Chroma
    owns:
      - fuzzy_recall
      - concept_similarity
      - long_research_theme_matching

  merge:
    method: reciprocal_rank_fusion_or_weighted_score
    final_gate: source_pointer_required
```

**Apex rule:** vector hits must never be accepted without a raw source pointer or compiled wiki page path.

---

## 6. Evaluation of major options

|Option|Fit|Why|
|---|--:|---|
|`CLAUDE.md` only|25/100|Too token-expensive if expanded; context, not database; not enforceable.|
|Claude Auto Memory|30/100|Useful for preferences and repeated corrections, not auditable Apex state.|
|Claude Skills only|70/100|Excellent procedure layer, but not enough for source custody/retrieval.|
|`apex-kb` / llm-wiki|**92/100**|Best source-grounded KB spine; preserves raw sources, compiles wiki, supports query/lint/audit.|
|SQLite FTS5 / BM25|**90/100**|Best v1 retrieval engine: local, cheap, deterministic, source-citable.|
|Local vector DB|75/100 now, 90/100 later|Strong semantic recall, but adds embedding/index maintenance.|
|Backlog.md-style task files|78/100|Strong Markdown task substrate; useful fields include dependencies, raw content, acceptance criteria, DoD, parent/subtasks, priority.|
|Task Master-style next-task logic|75/100|Strong dependency-satisfied next-task logic, but JSON/tooling should be adapted into Apex Python rather than copied wholesale.|
|GSD Core-style session artifacts|80/100|Strong context-engineering pattern; it uses fresh-context subagents and persistent artifacts like `STATE.md` / `CONTEXT.md` to fight context rot.|
|MCP memory server|55/100|Good adapter/interop layer; not enough custody, schema, gates, or repo-native determinism.|
|Hosted vector/cloud file search|45/100 for default; 85/100 for escalation|Powerful, but not local/cost-free and can weaken repo custody unless mirrored back.|

---

## 7. MCP recommendation

MCP should be treated as an **access layer**, not Apex’s canonical memory.

The official MCP overview defines MCP as an open standard for connecting AI applications to external systems like local files, databases, tools, and workflows. ([modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro "What is the Model Context Protocol (MCP)? - Model Context Protocol")) The modelcontextprotocol servers repo includes reference servers for filesystem, git, memory, time, and other tools, but its README warns that the reference servers are educational examples rather than production-ready solutions. ([GitHub](https://github.com/modelcontextprotocol/servers "GitHub - modelcontextprotocol/servers: Model Context Protocol Servers · GitHub"))

**Use MCP for:**

```yaml
good_MCP_uses:
  - read_only_filesystem_access_to_apex_meta
  - git_status_and_diff_query
  - optional_memory_graph_experiment
  - bridge_to_calendar_or_docs_when_operator_approves
  - external_tool_interop
```

**Do not use MCP for:**

```yaml
bad_MCP_uses:
  - canonical_project_state
  - sole_source_of_truth
  - uncontrolled_memory_mutation
  - replacing_apex-kb_manifest_hash_custody
  - replacing_apex-session_handoff
```

The MCP memory server is interesting because the repo describes it as a “knowledge graph-based persistent memory system,” but for Apex it should be a **derived mirror** of repo state, not the state owner. ([GitHub](https://github.com/modelcontextprotocol/servers "GitHub - modelcontextprotocol/servers: Model Context Protocol Servers · GitHub"))

---

## 8. Hosted/cloud options and why they are not default

OpenAI’s current API docs include file search/retrieval, vector stores, hosted tools, and Codex-related docs; those are serious options for hosted retrieval or agent workflows. ([OpenAI Platform](https://platform.openai.com/docs/guides/tools-file-search "File search | OpenAI API")) But Apex’s stated priority is **local, cost-free, token-efficient, deterministic, long-term maintainable**. Hosted file search and vector stores violate at least two of those priorities by default: cost and external dependency.

**Escalation criteria for hosted/cloud retrieval:**

```yaml
use_hosted_only_when:
  - source_corpus_is_too_large_for_local_laptop
  - team_needs_shared_query_service
  - cloud_docs_are_already_source_of_truth
  - advanced_embedding_quality_is_worth_cost
  - external_search_requires current web/API retrieval
  - operator_explicitly_approves sync_or_upload
```

**Never allow hosted systems to be canonical unless:**

```yaml
hosted_canonical_exception:
  required:
    - local_snapshot
    - source_manifest_entry
    - hash_or_version_marker
    - export_path_back_to_repo
    - operator_review_gate
```

---

## 9. Final recommended architecture

```txt
repo root
├── .claude/
│   ├── Claude.md                         # tiny control plane
│   ├── rules/                            # path-scoped instructions
│   └── skills/
│       ├── apex-kb/                      # KB custody/query/lint/audit
│       ├── apex-plan/                    # decomposition/planning
│       ├── apex-sync/                    # deterministic task/index reports
│       ├── apex-session/                 # handoff/session/state deltas
│       └── prompt-engineer/              # prompt packet creation/reuse
│
├── apex-meta/
│   ├── kb/
│   │   ├── <kb-slug>/
│   │   │   ├── raw/
│   │   │   ├── ingest-analysis/
│   │   │   ├── wiki/
│   │   │   ├── manifests/source-manifest.json
│   │   │   ├── outputs/queries/
│   │   │   ├── audit/
│   │   │   └── log/
│   │   └── _source-acquisitions/
│   │
│   ├── registry/
│   │   ├── index.md
│   │   ├── search.sqlite                 # v1 generated, not hand-edited
│   │   └── vector/                       # v2 optional
│   │
│   ├── epics/
│   │   └── <epic>/
│   │       ├── epic.md
│   │       └── 001.md
│   │
│   └── sessions/
│       └── YYYY-MM-DD/
│           ├── task_plan.md
│           ├── findings.md
│           ├── progress.md
│           └── next-session.md
│
├── state/
│   ├── apex-project-status.md
│   └── consumed-recap-registry.md
│
├── artifacts/
│   ├── weekly-plans/
│   ├── next-day-plans/
│   ├── flow-packets/
│   └── flow-recap-packets/
│
└── scripts/
    ├── apex_kb.py
    ├── apex_sync.py
    └── apex_search.py
```

---

## 10. Concrete implementation path

### Phase 1 — stabilize the canonical repo state

```yaml
phase_1:
  create_or_confirm:
    - apex-meta/kb/
    - apex-meta/registry/
    - apex-meta/sessions/
    - scripts/apex_kb.py
    - scripts/apex_sync.py
    - scripts/apex_search.py

  enforce:
    - CLAUDE.md under 200 lines
    - no raw corpus in CLAUDE.md
    - no silent state mutation
    - all KB claims need source pointers
```

### Phase 2 — build local lexical retrieval

```yaml
phase_2:
  script: scripts/apex_search.py
  storage: apex-meta/registry/search.sqlite
  commands:
    - rebuild
    - query
    - explain
    - stale
    - validate
  indexed_fields:
    - page_path
    - kb_slug
    - title
    - page_type
    - summary
    - body
    - source_paths
    - tags
    - updated_at
    - hash
```

### Phase 3 — integrate with `apex-kb`

```yaml
phase_3:
  apex_kb_query:
    - uses wiki/index.md first
    - uses search.sqlite for candidate retrieval
    - reads top selected pages only
    - returns evidence table
    - saves high-value answers to outputs/queries/
```

### Phase 4 — connect loop memory

```yaml
phase_4:
  after_FlowRecap:
    - raw_flow_dump retained
    - flow_recap_packet created
    - model_usage_delta captured
    - relevant learnings routed to apex-session
    - stable knowledge routed to apex-kb ingest queue
    - status changes routed to APSU/status merge
```

### Phase 5 — add optional hybrid vector

```yaml
phase_5_optional:
  add_when:
    - lexical_search_returns_too_many_false_negatives
    - compiled_wiki_pages_exceed_manual_scan_scale
    - concept_similarity_becomes_needed
  candidates:
    - Qdrant_local_if_Docker_ok
    - FAISS_if_library_only_preferred
    - LanceDB_or_Chroma_if_simpler_python_API_preferred
```

---

## 11. Final ranking

```yaml
final_decision:
  best_default_architecture:
    name: Apex_FileFirst_KB_BM25_Skills_Architecture
    score: 94
    summary: >
      Keep Apex memory in repo-owned files, compile raw sources into apex-kb
      wiki pages, retrieve through deterministic indexes, use Claude Skills for
      procedures, and use Claude Code memory only as a small routing/control
      layer.

  second_best:
    name: Apex_FileFirst_plus_Local_Vector_Hybrid
    score: 88_now_95_later
    summary: >
      Same as default, but with local embeddings/vector search once enough
      compiled KB exists and retrieval misses become costly.

  not_recommended_as_primary:
    - CLAUDE_md_only
    - Auto_Memory_only
    - MCP_memory_server_as_canonical
    - hosted_vector_DB_as_default
    - SaaS_project_memory_as_default
```

**Bottom line:** Apex should become a **repo-native, source-custodial, compiled-wiki + deterministic-index system**. The shortest path is not “choose the best memory server.” It is:

```txt
CLAUDE.md for routing
+ Skills for procedures
+ apex-kb for source custody and compiled knowledge
+ apex-session for continuity
+ apex-sync for deterministic state/index reports
+ SQLite FTS5/BM25 for cheap local retrieval
+ optional local vector only after v1 works
```

That gives Apex the thing generic memory tools usually do not: **auditable memory with operator gates, source custody, deterministic rebuilds, and low-token retrieval.**