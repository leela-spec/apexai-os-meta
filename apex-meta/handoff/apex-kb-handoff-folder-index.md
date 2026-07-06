# Apex KB Handoff Folder Index

## 1. Executive Navigation

This folder currently contains two distinct handoff families:

1. **Apex KB process handoffs**: durable process learning and v2 planning for future Apex KB work.
2. **NARM-support project handoffs**: H6 continuation files for a therapy-support knowledgebase project.

Future Apex KB planning runs should treat `apex-kb-chat-drift-learning.okf.md` and `apex-kb-v2-planning-handover.md` as the primary process files. The NARM files are operational domain handoffs; they are useful when the next task concerns `narm-support-knowledgebase`, but they should not be mistaken for generic Apex KB architecture authority.

Use this folder as a routing layer, not as the full evidence corpus. When a future run needs implementation truth, it must reload live repo files such as `.claude/skills/apex-kb/` and `apex-meta/scripts/apex_kb.py` before patching.

## 2. Read-First Files

| Rank | File | Authority | Why read first | Main topics | Currentness | Risk if ignored |
|---:|---|---|---|---|---|---|
| 1 | `apex-kb-chat-drift-learning.okf.md` | P0_binding | Defines the process failures and corrected response protocol for Apex KB work. | process drift, executor routing, lifecycle order, Codex handoffs | Current process memory | Repeats partial prompts, option sprawl, phase rewinds, and wrong executor routing. |
| 2 | `apex-kb-v2-planning-handover.md` | P0_binding | Captures the latest V2 planning agenda after V1 execution and repair. | V2 priorities, quality/eval, tier policy, source-set planning, skill compaction | Current planning handover; live repo verification required | Reopens solved V1 issues or misses high-impact V2 improvements. |
| 3 | `narm-index-prep-handover.md` | P1_operational | Best routing file for the NARM-support KB continuation. | definitions of done, artifact plan, source map, prompts | Current for NARM pre-indexing | Builds final NARM indexes too early or writes to wrong destination. |
| 4 | `next-session.md` | P1_operational | Short NARM next-session pointer. | NARM next actions, open items, risks | Partly superseded by `narm-index-prep-handover.md` | Misses open destination/privacy/source-inspection questions. |
| 5 | `task_plan.md` | P1_operational | Compact NARM project phase plan. | NARM phases, therapy-support scope, risks | Current as H6 plan | Confuses therapy-support infrastructure with therapist replacement. |
| 6 | `findings.md` | P1_operational | Durable NARM source and decision notes. | durable findings, source notes, operator validation | Current for NARM source notes | Loses named source files and operator validation basis. |
| 7 | `progress.md` | P1_operational | Historical session log for H6 artifact creation. | session log, state deltas, next apex-sync route | Historical | Repeats already-created H6 artifacts or mutates wrong state. |

## 3. Topic Index

### 3.1 Current State Locks

| Lock | Evidence files | Status | Future-use rule |
|---|---|---|---|
| Apex KB lifecycle order must be preserved. | `apex-kb-chat-drift-learning.okf.md` | Binding | Do not rewind to earlier phases unless a hard missing artifact is proven. |
| Python/deterministic tools own structure, hashing, source manifests, Phase 0 maps, indexes, retrieval builds, lint/audit mechanics. | `apex-kb-chat-drift-learning.okf.md`, `apex-kb-v2-planning-handover.md` | Binding | Keep semantic synthesis out of deterministic scripts. |
| LLM owns source relevance judgment, concept/entity extraction, contradiction interpretation, Phase 1 analysis, Phase 2 wiki drafting, and query synthesis. | `apex-kb-chat-drift-learning.okf.md`, `apex-kb-v2-planning-handover.md` | Binding | Do not ask Codex/Python to synthesize meaning. |
| Codex execution prompts must be complete, main-policy aware, and not split into partial packets. | `apex-kb-chat-drift-learning.okf.md` | Binding | Emit one executable artifact per execution boundary. |
| V2 planning should optimize value-to-overhead, not add files because the architecture can support them. | `apex-kb-v2-planning-handover.md` | Binding planning direction | Prefer compaction, quality checks, and coverage over package sprawl. |
| NARM project is therapy-support infrastructure, not therapist replacement. | `task_plan.md`, `findings.md`, `narm-index-prep-handover.md` | Binding for NARM | Preserve redaction, clinical-use limits, and direct evidence labeling. |

### 3.2 Deterministic Script Inefficiencies

| Inefficiency | Evidence files | Layer | Current status | Recommended next check |
|---|---|---|---|---|
| Need better non-semantic quality/eval checks beyond basic lint. | `apex-kb-v2-planning-handover.md` | script/lint | Proposed V2 priority | Verify live `apex_kb.py` command surface and add `quality` only if absent. |
| Need source-set planning before ingestion. | `apex-kb-v2-planning-handover.md` | ingest planning | Proposed | Decide whether LLM artifact or deterministic candidate-source report owns it. |
| Need page-class budgets to avoid wiki sprawl. | `apex-kb-v2-planning-handover.md` | wiki compile/lint | Proposed | Add threshold rules to templates/contract before generating more pages. |
| Need claim-density and redundancy checks. | `apex-kb-v2-planning-handover.md` | lint/quality | Proposed | Implement only countable structure checks in Python; leave semantic rating to LLM quality notes. |
| Need query-performance smoke tests. | `apex-kb-v2-planning-handover.md` | retrieval/eval | Proposed | Add canned query eval packs per KB after retrieval path is stable. |
| Need coverage dashboard from manifest-derived facts. | `apex-kb-v2-planning-handover.md` | status/coverage | Proposed | Build from manifest/page frontmatter; do not infer semantic coverage automatically. |

### 3.3 Lifecycle Prompt-Flow Inefficiencies

| Failure pattern | Evidence files | Why it matters | Corrected rule |
|---|---|---|---|
| Partial Codex packets. | `apex-kb-chat-drift-learning.okf.md` | Forces repeated user orchestration and cross-referencing. | A Codex handoff must include repo, branch, commands, validation, report path, commit/push, and final schema. |
| Options when execution was required. | `apex-kb-chat-drift-learning.okf.md` | Creates divergent paths inside a linear lifecycle. | Produce the single next artifact unless options are explicitly requested. |
| Deterministic loop overextension. | `apex-kb-chat-drift-learning.okf.md` | Treats validation gates as the product. | After PASS/PASS_WITH_WARNINGS, route to next lifecycle phase. |
| Phase rewind. | `apex-kb-chat-drift-learning.okf.md` | Invalidates accepted state and restarts old debates. | Preserve prior state unless hard blocker proves it invalid. |
| Wrong executor routing. | `apex-kb-chat-drift-learning.okf.md` | Sends semantic work to Codex or deterministic work to chat. | Select exactly one executor: CODEX, DETERMINISTIC_TOOL, LLM, or HUMAN_OPERATOR. |
| Over-fragmented NARM preparation. | `narm-index-prep-handover.md`, `next-session.md` | Final indexes could be built before preparation artifacts are ready. | Prepare definitions/prompts/artifact plan first; final index build is a later pass. |

### 3.4 Missing or Wrongly Excluded High-Impact Tools

The live handoff folder does not contain full technical evidence for every tool below. Entries marked `not evidenced in handoff folder` should be routed to the broader project-resource index or live repo verification before implementation.

| Tool / Pattern | Desired layer | Current status | Why it matters | Evidence files | Recommendation |
|---|---|---|---|---|---|
| source-payload-manifest / BagIt-style hashing | Source custody | Not evidenced in this live handoff folder | Proves exact raw payload at root/group/file level. | None in folder; route to broader Apex KB source-custody files. | Add to future handoff folder if it is now a binding target; verify live script before patching. |
| SQLite FTS5/BM25 | Retrieval | Mentioned only indirectly through query/retrieval priorities | Enables local deterministic full-text retrieval over compiled KB pages. | `apex-kb-v2-planning-handover.md` | Verify retrieval script and derived-artifact policy outside this folder. |
| JSON retrieval fallback | Retrieval | Not evidenced in handoff folder | Keeps retrieval usable if FTS5 is unavailable. | None in folder | Route to retrieval contract/project resources. |
| `apex_kb_retrieval.py` | Retrieval script | Not evidenced in handoff folder | Runtime retrieval implementation surface. | None in folder | Live-verify before any retrieval-related Codex task. |
| `markdown-it-py` | Phase 0 parser V1.5 | Not evidenced in handoff folder | Optional parser-boundary validator when simple parser warnings justify it. | None in folder | Do not discuss unless parser failure is the current task. |
| PyYAML / `python-frontmatter` | Frontmatter parsing | Not evidenced in handoff folder | Useful for robust YAML/frontmatter handling if package dependency policy allows. | None in folder | Keep out of current handoff-driven patches unless exact frontmatter issue is active. |
| graph/process-flow extraction | Phase 0/V1.5 navigation | Indirectly relevant through lifecycle and executor routing | Helps map process and contract edges for LLM navigation. | `apex-kb-chat-drift-learning.okf.md` | Treat as later V1.5/navigation patch, not current source-custody patch. |
| GitHub connector | Repo inspection/publishing | Implied by repo handoff context, not explicitly specified | Enables live repo reads/writes when local checkout is unavailable. | None in folder | Future handoffs should specify connector vs local Codex surface explicitly. |
| LLM Phase 1/Phase 2 semantic synthesis | Semantic KB lifecycle | Explicitly present | Core LLM-owned stages after deterministic preparation and gate. | `apex-kb-chat-drift-learning.okf.md`, `apex-kb-v2-planning-handover.md` | Preserve ownership split and gate semantics. |
| lint/audit/status/health | Deterministic validation | Present as solved/tested V1 surfaces and future quality direction | Prevents structural drift and exposes stale/broken artifacts. | `apex-kb-v2-planning-handover.md` | Add quality/coverage only after live command-surface check. |
| command-contract docs | Skill/package contract | Present as repaired branch file set to reload | Keeps documented commands aligned with scripts. | `apex-kb-v2-planning-handover.md` | Always read contract plus live script before patching. |
| Codex main-only execution standard | Execution process | Explicit process rule | Prevents branch/PR drift against operator preference. | `apex-kb-chat-drift-learning.okf.md` | Use in Codex prompts unless operator explicitly asks otherwise. |

### 3.5 Source Custody and Manifest Integrity

The handoff folder contains **process-level custody concerns**, not the full source-custody implementation contract. For NARM, source custody is still at the named-source and source-folder level: `findings.md`, `task_plan.md`, and `narm-index-prep-handover.md` preserve exact source paths and file names. For Apex KB generically, the handoff folder says source manifest shape, source storage mode recording, and file hashing belong to deterministic ownership, but does not include enough detail to implement payload manifests directly.

Recommended routing:

| Need | Read first | Then verify |
|---|---|---|
| NARM source custody | `findings.md`, `narm-index-prep-handover.md` | Exact operator source files are accessible and redaction rules are resolved. |
| Apex KB manifest patch | `apex-kb-chat-drift-learning.okf.md`, `apex-kb-v2-planning-handover.md` | Live `.claude/skills/apex-kb/` and `apex-meta/scripts/apex_kb.py`; broader source-payload manifest handover if present. |
| Source drift checks | `apex-kb-v2-planning-handover.md` | Whether current lint/status already exposes changed hashes and stale wiki pages. |

### 3.6 Retrieval and Query Layer

The live handoff folder treats retrieval mostly as a lifecycle stage and V2 evaluation topic. It does not contain the retrieval-engine technical contract. Retrieval work should therefore **not** be patched from this folder alone.

| Topic | Handoff status | Recommendation |
|---|---|---|
| Query entry point | `wiki/index.md` appears as a stable architectural decision in V2 handover. | Preserve index-first query flow. |
| Query-performance smoke tests | Proposed high-impact V2 change. | Add only after compiled pages and retrieval path exist for a target KB. |
| SQLite FTS5/BM25 | Not technically evidenced here. | Route to retrieval contract or live script. |
| JSON fallback | Not evidenced here. | Do not infer; verify retrieval script. |
| Derived artifact hygiene | Not fully evidenced here. | Verify `.gitignore`, `derived/search/`, and query packet outputs live. |

### 3.7 Graph and Phase 0 Navigation

This folder preserves the lifecycle boundary around deterministic corpus intelligence but does not include a graph extraction spec. `apex-kb-chat-drift-learning.okf.md` identifies deterministic ownership for corpus profiles, heading/link/frontmatter maps, keyword hits, index sections, and audit file listing. Graph/process-flow extraction should be considered a future V1.5 navigation enhancement, not a current handoff-folder-backed patch.

### 3.8 Codex and GitHub Execution Process

The binding process rules are in `apex-kb-chat-drift-learning.okf.md`:

- Work directly on `main` for Codex prompts unless the operator explicitly requests branches/PRs.
- Avoid partial Codex handoffs.
- Avoid optional branches inside execution prompts.
- Do not stop on unrelated dirty files unless they conflict with the exact target scope.
- Commit and push when the user requests a repo change.
- Name the executor explicitly and do not mix execution surfaces.

For GitHub connector runs, add one extra rule not yet explicit in the folder: **state whether writes were made through connector contents API or local git/Codex**, because commit granularity and validation differ.

### 3.9 Failure Patterns and Process Learning

| Pattern | Cost | Prevention |
|---|---|---|
| Losing lifecycle state | Reopens settled decisions and frustrates operator | Start from latest handoff and live repo state. |
| Treating deterministic validation as destination | Creates unnecessary Codex cycles | Advance to semantic or post-semantic phase after validation passes. |
| Over-reading broad repo context | Token waste and drift | Read handoff folder first; expand only for exact references. |
| Confusing NARM domain handoffs with Apex KB process handoffs | Wrong patch priorities | Route NARM tasks to `narm-index-prep-handover.md`; route Apex KB process tasks to the two Apex KB handoffs. |
| Implementing missing tools from memory | Risk of wrong layer and wrong current status | Mark absent evidence and live-verify tool/script state. |

### 3.10 Future Development Backlog

| Rank | Idea | Layer | Impact 1-100 | Evidence 1-100 | Risk 1-100 | Cost 1-100 | Source files | Recommendation |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | Add/verify Apex KB output tier policy | Lifecycle UX | 94 | 85 | 25 | 35 | `apex-kb-v2-planning-handover.md` | Implement after live contract check. |
| 2 | Add deterministic `quality` or `eval` command | Validation | 92 | 82 | 40 | 55 | `apex-kb-v2-planning-handover.md` | Start with countable non-semantic checks plus LLM notes. |
| 3 | Compact `SKILL.md` into routing kernel | Skill package | 88 | 75 | 45 | 45 | `apex-kb-v2-planning-handover.md` | Do only after current skill package is stable on main. |
| 4 | Add source-set planning before ingestion | Ingest planning | 87 | 78 | 35 | 40 | `apex-kb-v2-planning-handover.md` | LLM-owned plan, deterministic artifact placement. |
| 5 | Add page-class budgets | Phase 2/wiki | 84 | 78 | 30 | 35 | `apex-kb-v2-planning-handover.md` | Prevent wiki sprawl before large KB compiles. |
| 6 | Add query-performance smoke tests | Retrieval/eval | 78 | 68 | 35 | 45 | `apex-kb-v2-planning-handover.md` | Pair with compiled page sets and retrieval script. |
| 7 | Add manifest-derived coverage dashboard | Status/coverage | 70 | 62 | 35 | 45 | `apex-kb-v2-planning-handover.md` | Useful after source manifest/page frontmatter are reliable. |
| 8 | Create NARM preparation artifacts | NARM project | 80 | 95 | 30 | 45 | `narm-index-prep-handover.md` | Execute before any final NARM index build. |
| 9 | Resolve NARM destination/redaction decisions | NARM governance | 76 | 85 | 60 | 25 | `task_plan.md`, `findings.md`, `next-session.md` | Ask operator only when next NARM write target is active. |
| 10 | Add GitHub connector/local-Codex execution surface note to future handoffs | Process docs | 65 | 45 | 20 | 20 | inferred gap from folder | Low-cost addition to prevent local filesystem assumptions. |

## 4. File-by-File Ledger Summary

| File | Authority | Topics | Key claims | Patch relevance | Stale risk | Read priority |
|---|---|---|---|---|---|---:|
| `apex-kb-chat-drift-learning.okf.md` | P0_binding | process drift; lifecycle; executor routing | Preserve lifecycle state; emit complete artifacts; avoid option sprawl. | High for any Apex KB planning/Codex task. | Low | 1 |
| `apex-kb-v2-planning-handover.md` | P0_binding | V2 planning; quality; compaction; query eval | V1 works but needs value-to-overhead optimization. | High for Apex KB V2 planning. | Medium | 2 |
| `narm-index-prep-handover.md` | P1_operational | NARM preparation artifacts; prompts; source map | Prepare artifacts, do not final-build indexes. | High for NARM continuation. | Low/medium | 3 |
| `next-session.md` | P1_operational | NARM next actions and open items | Read NARM prep handover next; preserve risks. | Medium for NARM only. | Medium-high | 4 |
| `task_plan.md` | P1_operational | NARM phases and risks | Therapy-support KB, not therapist replacement. | Medium for NARM scope. | Medium | 5 |
| `findings.md` | P1_operational | NARM durable findings and sources | Lists source files and operator validation. | Medium for NARM source custody. | Medium | 6 |
| `progress.md` | P1_operational | H6 session log | H6 artifacts created; next route to apex-sync. | Low/medium. | Medium | 7 |

## 5. Future Run Routing

- **If the next task is source custody**, read `apex-kb-chat-drift-learning.okf.md` and `apex-kb-v2-planning-handover.md`; then live-verify `.claude/skills/apex-kb/`, `apex-meta/scripts/apex_kb.py`, and the relevant KB manifests. For NARM source custody, also read `findings.md` and `narm-index-prep-handover.md`.
- **If the next task is retrieval**, read `apex-kb-v2-planning-handover.md`; then live-verify retrieval contracts and `apex_kb_retrieval.py`. Do not patch retrieval from this handoff folder alone.
- **If the next task is prompt-flow repair**, read `apex-kb-chat-drift-learning.okf.md` first. It is the strongest process-learning file.
- **If the next task is script patching**, read `apex-kb-chat-drift-learning.okf.md`, `apex-kb-v2-planning-handover.md`, then live-read the actual script and command-contract docs. Do not rely on handoff claims alone.
- **If the next task is full Apex KB planning**, read both Apex KB handoffs first, then route to broader project resources and live repo files.
- **If the next task is NARM-support indexing**, read `narm-index-prep-handover.md`, then `task_plan.md`, `findings.md`, `progress.md`, and `next-session.md`. Do not build final indexes until the preparation artifacts are complete.

## 6. Non-Reopen Rules

- Do not relitigate the deterministic-vs-LLM ownership split.
- Do not route semantic synthesis to Python/Codex.
- Do not route hashing/manifests/index/lint/audit mechanics to LLM prose.
- Do not rewind Apex KB lifecycle phases without a proven missing artifact.
- Do not produce partial Codex prompts when a complete execution packet is needed.
- Do not introduce branches or PRs in Codex prompts unless the operator explicitly asks.
- Do not treat NARM handoff files as generic Apex KB package authority.
- Do not build final NARM indexes before the preparation artifacts specified in `narm-index-prep-handover.md` exist.
- Do not implement missing tools from this folder alone when the folder marks them absent or only indirectly evidenced.
