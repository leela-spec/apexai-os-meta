# Apex KB Lifecycle Analysis Folder Index

## 0. Machine-Readable Routing Summary

```yaml
index_metadata:
  repo: leela-spec/apexai-os-meta
  branch: main
  folder: apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/
  generated_at: "2026-07-06T00:00:00+02:00"
  artifact_type: lifecycle_analysis_folder_index
  source_access: pass
  discovery_method:
    - GitHub connector repository metadata
    - GitHub connector file search scoped to target folder
    - GitHub connector fetch_file reads for every discovered file

routing:
  read_first_core:
    - file: apex-kb-target-drift-failure-learning.okf.md
      reason: Directly defines the failure gates for this index class and blocks folder-membership-as-authority drift.
    - file: apex-kb-chat-drift-learning.okf.md
      reason: Binding process learning for lifecycle state, executor routing, deterministic/LLM split, and no-option-sprawl behavior.
    - file: apex-kb-v2-source-payload-manifest-handover.md
      reason: Direct source-custody and BagIt-style payload-manifest authority for the next Apex KB lifecycle patch family.
    - file: Apex-KB_UpdatePlan.md
      reason: Consolidated implementation-ready source-custody plan with command, schema, lifecycle insertion point, validation, and drift guards.
    - file: Apex KB Lifecycle Execution Audit.md
      reason: Direct lifecycle execution audit exposing CLI, phase-gate, pointer-only, scaffold, and ordered-command process defects.
    - file: codex-old-agent-kb-execution-process-audit.md
      reason: Direct Codex/process audit for main-only execution, dirty-tree policy, PowerShell, retrieval/index sequencing, and patch backlog.
    - file: apex-kb-next-runbook-v2.md
      reason: Compact lifecycle runbook mapping deterministic preparation, Phase 1, approval, Phase 2, and postflight.
    - file: apex-kb-full-lifecycle-test-handover.md
      reason: Direct full-lifecycle test handover with canonical package/scripts, command sequence, and boundaries.
    - file: apex-kb-v2-planning-handover.md
      reason: V2 planning authority for quality/eval, output tiering, compaction, source-set planning, page budgets, and query-eval direction.

  supporting_evidence:
    - file: codex-run-apex-kb-contract-repair.md
      reason: Concrete repair-script handoff; useful for package-contract repair scope and validation expectations.
    - file: FailureAnalysis_ChatHistory.md
      reason: Concrete corrected Codex closure prompt showing deterministic closure standards.
    - file: Apex-KB_FixesClaude.md
      reason: Remediation sequence evidence: truth chain, derived-artifact hygiene, validation, S10 maintenance, retrieval eval, lifecycle simplification.
    - file: process-validation-and-extension-review_20260630.md
      reason: Lika KB validation report with transferable repo-truth, chat-output-vs-repo-state, and postflight lessons.
    - file: next-actions-ranked_20260630.md
      reason: Lika ranked action plan; useful as transferable evidence for repo-state verification, source-specific Phase 1, and post-Phase-2 retrieval/query tests.

  generated_artifacts_under_review:
    - file: apex-kb-handoff-folder-index.md
      reason: Prior generated folder index; useful as failure evidence but not source truth.
    - file: apex-kb-handoff-topic-map.okf.md
      reason: Prior machine topic map; repeats wrong NARM read-first promotion.
    - file: apex-kb-handoff-file-ledger.json
      reason: Prior machine ledger; repeats wrong read-first routing and references old folder scope.

  domain_or_appendix:
    - file: findings.md
      reason: NARM-support domain handoff; valid project context but not generic Apex KB lifecycle authority.

  stale_or_contaminating:
    - file: Apex-KB_FixesClaude2.md
      warning: Early BagIt/source-manifest draft with unverified source-intake status and hardcoded batch groups; only use as contamination trace.
    - file: apex-kb-handoff-folder-index.md
      warning: Says NARM files are not generic authority while ranking them read-first.
    - file: apex-kb-handoff-topic-map.okf.md
      warning: Machine-readable repetition of the same ranking error.
    - file: apex-kb-handoff-file-ledger.json
      warning: Machine-readable repetition of the same ranking error plus old folder path.
```

## 1. Executive Verdict

This folder is useful as a **lifecycle-improvement evidence bundle** for Apex KB. Its highest-value files explain process drift, source-custody repair, deterministic/semantic ownership, Codex execution failures, Phase 0/1/2 boundaries, retrieval/index sequencing, and future quality/eval improvements.

It is **not** a generic folder inventory and not a domain KB source set. Folder membership does not imply lifecycle authority. The new target-drift learning file explicitly states that reading a file proves access only, not authority, and that a task-specific lifecycle index must rank only files that serve the declared lifecycle target.

True read-first lifecycle core files are the target-drift learning file, chat-drift learning file, source-payload manifest handover, update plan, lifecycle execution audits, old-agent Codex audit, lifecycle runbook/test handovers, and V2 planning handover. Supporting evidence includes contract repair, failure-history closure prompts, remediation plans, and Lika KB validation reports. Domain-only context is currently limited to `findings.md`, which is about a NARM-support therapy KB.

Most important lifecycle improvement ideas found:

- Do not let source access become source authority.
- Keep Apex KB lifecycle state locked across chats.
- Preserve Python/deterministic ownership for hashing, manifests, Phase 0 maps, indexing, retrieval rebuilds, lint, audit, and status.
- Preserve LLM ownership for semantic source analysis, concept/entity synthesis, contradiction interpretation, wiki drafting, and query answer synthesis.
- Add or preserve source-payload custody as a deterministic companion to `source-manifest.json`.
- Run payload manifest generation after source intake and before Phase 0.
- Avoid branches/PRs unless explicitly requested; work on `main` for Codex prompts.
- Do not stop on unrelated dirty files; block only overlapping dirt.
- Run wiki index rebuild before retrieval build-index when post-LLM content changes.
- Treat generated index artifacts under this folder as evidence under review, not as authority.

## 2. Source Access Ledger

| File | Read status | Lines read | Size/shape if available | Scope class | Confidence | Notes |
|---|---:|---:|---|---|---:|---|
| `apex-kb-target-drift-failure-learning.okf.md` | full | 247/247 | OKF learning file | apex_kb_lifecycle_core | high | Mandatory gate file. |
| `apex-kb-chat-drift-learning.okf.md` | full-near | 352/355 | OKF learning file | apex_kb_lifecycle_core | high | Connector output truncated only at final few lines. |
| `apex-kb-v2-source-payload-manifest-handover.md` | partial | 371/1064 plus key sections | long handover/planner | apex_kb_lifecycle_core | high | Enough read for accepted decisions, command, schema, lifecycle insertion, tool exclusions. |
| `Apex-KB_UpdatePlan.md` | partial-but-substantive | 338/406 via two fetches | update plan | apex_kb_lifecycle_core | high | Core source-custody implementation plan and final Codex prompt read. |
| `Apex KB Lifecycle Execution Audit.md` | full | 965/965 via two fetch ranges | audit report | apex_kb_lifecycle_core | high | Full lifecycle audit read. |
| `codex-old-agent-kb-execution-process-audit.md` | near-full | 648/648 with final tool truncation | process audit | apex_kb_lifecycle_core | high | Process audit and backlog read. |
| `apex-kb-next-runbook-v2.md` | full | 105/105 | compact runbook | apex_kb_lifecycle_core | high | Full lifecycle runbook read. |
| `apex-kb-full-lifecycle-test-handover.md` | full | 67/67 | test handover | apex_kb_lifecycle_core | high | Canonical test handover read. |
| `apex-kb-v2-planning-handover.md` | partial | 263/324 | V2 planning handover | apex_kb_lifecycle_core | high | Core ranking and compaction sections read. |
| `codex-run-apex-kb-contract-repair.md` | full | 133/133 | Codex handoff | apex_kb_supporting_evidence | high | Repair script instructions read. |
| `FailureAnalysis_ChatHistory.md` | partial | 201+ | corrected Codex prompt / chat history | apex_kb_supporting_evidence | medium | Enough for closure-flow lessons. |
| `Apex-KB_FixesClaude.md` | full | 57/57 | remediation program | apex_kb_supporting_evidence | high | Fix-first/simplify-second program read. |
| `process-validation-and-extension-review_20260630.md` | partial | 173/227 | Lika validation report | transferable_domain_process_evidence | high | Strong transferable lifecycle validation content. |
| `next-actions-ranked_20260630.md` | full | 51/51 | Lika ranked action plan | transferable_domain_process_evidence | high | Domain-specific but process-transferable action ranking. |
| `apex-kb-handoff-folder-index.md` | partial | 138/179 | prior generated Markdown index | generated_index_artifact_under_review | high | Contains the exact prior ranking contradiction. |
| `apex-kb-handoff-topic-map.okf.md` | full | 222/222 | prior generated OKF map | generated_index_artifact_under_review | high | Machine-readable duplicate of prior bad ranking. |
| `apex-kb-handoff-file-ledger.json` | full | 158/158 | prior generated JSON ledger | generated_index_artifact_under_review | high | Machine-readable duplicate of prior bad ranking. |
| `findings.md` | full | 32/32 | NARM findings | domain_only_context | high | Valid NARM source/context, not lifecycle authority. |
| `Apex-KB_FixesClaude2.md` | partial | 99 lines attempted, key lines read | early BagIt draft | stale_or_contaminating | high | Contains unverified source-intake claim and hardcoded batches. |

## 3. Read-First Lifecycle Core

### `apex-kb-target-drift-failure-learning.okf.md`

- Why read first: It is the required anti-drift gate for this exact index class.
- What it gives the LLM: Binary relevance gates, read-first purity rules, contradiction blocking, artifact minimality, and classification policy.
- Macro idea: The previous failure was a scope-priority inversion: folder membership was treated as relevance.
- Meso idea clusters: source-access vs source-authority; folder inventory vs task index; domain handoff vs process handoff; machine output strictness; redundancy control.
- Micro extraction targets: mandatory prewrite gates, corrected scope classes, demotion rules, failure-prevention algorithm.
- Use for: Every future Apex KB lifecycle index or folder handoff classification.
- Do not use for: Broad architecture redesign or domain KB content.
- Key citations: lines 23-39 define the failure event and correct output class; lines 73-89 define source-access and machine-output distinctions; lines 91-123 define gates; lines 125-148 define scope classes; lines 173-193 define concrete demotions and true read-first core.

### `apex-kb-chat-drift-learning.okf.md`

- Why read first: It is the central process-memory file for Apex KB chat drift.
- What it gives the LLM: Lifecycle order, deterministic/LLM ownership, executor routing, no partial Codex handoffs, and no phase rewinds.
- Macro idea: Apex KB assistance must preserve global lifecycle state, not optimize only local response correctness.
- Meso idea clusters: lifecycle state lock; Codex packet completeness; options vs execution; phase rewind; deterministic loop overextension; executor routing.
- Micro extraction targets: lifecycle order, deterministic ownership list, LLM ownership list, hard rules, executor matrix.
- Use for: Process standard and prompt-flow discipline.
- Do not use for: Specific source-payload manifest schema; use source-payload files for that.
- Key citations: lines 28-43 define the failure; lines 45-83 define lifecycle and ownership; lines 85-168 define failure modes and corrected rules; lines 169-229 define mandatory response protocol.

### `apex-kb-v2-source-payload-manifest-handover.md`

- Why read first: It carries the accepted source-custody patch target and non-reopen decisions.
- What it gives the LLM: Binding decision lock for BagIt-style payload manifest, command target, output path, raw-folder grouping, and forbidden drifts.
- Macro idea: Source custody and lifecycle-control drift are the current root problems.
- Meso idea clusters: accepted decisions; source manifest vs source-payload manifest split; deterministic/LLM ownership; lifecycle insertion after source-intake and before Phase 0; no parser/retrieval drift.
- Micro extraction targets: `generate-source-payload-manifest`, `manifests/source-payload-manifest.json`, group `root`, first-level raw folders, no hardcoded batches, main-only.
- Use for: Source-custody patch and source-payload manifest implementation planning.
- Do not use for: Retrieval rebuild, parser debate, semantic wiki generation.
- Key citations: lines 20-48 lock accepted decisions and current next patch; lines 80-114 define problem stack; lines 120-161 define ownership; lines 167-174 define the new artifact.

### `Apex-KB_UpdatePlan.md`

- Why read first: It is a compact implementation-ready plan for the payload-manifest patch.
- What it gives the LLM: Command behavior, JSON shape, hashing rules, grouping algorithm, exclusion/idempotency rules, validation, acceptance criteria, and a final Codex prompt.
- Macro idea: Add a deterministic payload-custody ledger; do not redesign lifecycle or retrieval.
- Meso idea clusters: manifest split; generic grouping; simplified flow; patch scope; tool inclusion/exclusion matrix; Codex execution policy.
- Micro extraction targets: command shape, flags, manifest schema, SHA-256 aggregation rules, no generated_at by default, test KB validation.
- Use for: Micro implementation of the source-payload manifest generator.
- Do not use for: Lika/NARM domain content or broad V2 planning.
- Key citations: lines 5-20 define the verdict; lines 38-60 define artifact and grouping; lines 64-90 define four-stage flow; lines 100-175 define command, schema, hashing, and JSON behavior; continuation lines 3-24 define execution policy and validation.

### `Apex KB Lifecycle Execution Audit.md`

- Why read first: It audits a real lifecycle run and exposes concrete script/process mismatches.
- What it gives the LLM: Evidence of safe scoped staging, Phase 2 gate preservation, deterministic checks, CLI flag-order mismatch, source-intake/hash alias gaps, scaffold-directory ambiguity, pointer-only Phase 0 behavior, ordered-command risk.
- Macro idea: The lifecycle can pass, but friction comes from command contract and process mismatches.
- Meso idea clusters: pass summaries; positive findings; CLI defects; scaffold/Phase 2 boundary; pointer-only Phase 0 gap; sequential execution; PowerShell commit checks; patch backlog.
- Micro extraction targets: global flag placement, `--source-path`, `--path`, scaffold reserved dirs, pointer-only warnings, no parallel execution when order is specified.
- Use for: CLI/process patch prioritization and execution audit design.
- Do not use for: Semantic correctness of batch content.
- Key citations: lines 20-67 summarize lifecycle pass; lines 96-187 show safe behavior and gate preservation; lines 191-258 show flag-order defect; lines 260-343 show source/hash flag mismatches; lines 344-483 show scaffold and pointer-only issues; continuation lines 3-42 show ordered-command risk; lines 201-288 show efficiency/safety assessment; lines 288-399 show concrete script patches.

### `codex-old-agent-kb-execution-process-audit.md`

- Why read first: It audits old-agent KB deterministic runs and codifies main-only, dirty-tree, shell, and index/retrieval lessons.
- What it gives the LLM: Timeline of lifecycle success and wasted motion, branch chaos, dirty-file false stops, global flag mismatch, PowerShell JSON redirection, pointer-only Phase 0, remote artifact lookup, retrieval vs wiki index separation, and remaining patch backlog.
- Macro idea: The process succeeded but was inefficient due to execution-surface and command-contract drift.
- Meso idea clusters: old-agent lifecycle timeline; branch/main policy; dirty worktree policy; CLI compatibility; shell portability; pointer-only scan; index/retrieval model; patch backlog.
- Micro extraction targets: no branches, ignore unrelated dirt, accept subcommand-level flags, PowerShell-safe JSON capture, check origin/main before missing-file failure, run `apex_kb.py index` before retrieval build-index.
- Use for: Codex execution standards and patch backlog.
- Do not use for: Semantic content quality of the old-agent KB.
- Key citations: lines 28-39 summarize success and inefficiency; lines 130-205 define main-only and dirty policy; lines 207-265 define flag compatibility; continuation lines 3-31 define pointer-only patch; lines 82-112 define retrieval/index distinction; lines 250-316 define patch backlog.

### `apex-kb-next-runbook-v2.md`

- Why read first: It is the clean operator-facing lifecycle sequence.
- What it gives the LLM: Deterministic prep, Phase 1, approval, Phase 2, postflight, and compact operator prompt template.
- Macro idea: The lifecycle has a stable practical run order.
- Meso idea clusters: inputs; deterministic preparation; Phase 1 semantic ingest; approval gate; Phase 2 compile order; postflight; final reporting.
- Micro extraction targets: exact approval phrase, query simulations, source refs/hash/pointers, repo-local boundaries.
- Use for: Next-run orchestration and lifecycle phase map.
- Do not use for: Detailed source-payload manifest schema.
- Key citations: lines 14-29 define deterministic prep; lines 30-44 define Phase 1; lines 45-62 define gate and Phase 2; lines 75-83 define postflight.

### `apex-kb-full-lifecycle-test-handover.md`

- Why read first: It names canonical package/scripts and a concrete lifecycle smoke-test flow.
- What it gives the LLM: Main-only branch policy, `.claude/skills/apex-kb/`, `apex_kb.py`, `apex_kb_retrieval.py`, recent Phase 0 fixes, and test boundaries.
- Macro idea: Full lifecycle test should reload live package files and run the end-to-end command surface.
- Meso idea clusters: current state; recent completed work; suggested mission; boundaries; caveats.
- Micro extraction targets: `utf-8-sig` inventory read, sources/raw scan, full command sequence, Phase 0/2 boundaries, no adjacent Apex mutation.
- Use for: Full lifecycle smoke testing and canonical path resolution.
- Do not use for: Current implementation status without live repo check.
- Key citations: lines 5-13 define current state; lines 14-21 define recent script fixes; lines 30-61 define command sequence and boundaries.

### `apex-kb-v2-planning-handover.md`

- Why read first: It frames Apex KB V2 after real execution and repair.
- What it gives the LLM: Evidence base to load, solved/unsolved state, priority metric, ranked V2 improvements, compaction recommendations, extensions.
- Macro idea: V2 should optimize value-to-overhead, not add package files by architectural possibility.
- Meso idea clusters: current state; solved V1 package proof; remaining efficiency/quality problem; ranking model; high-impact realizations; compaction; extensions.
- Micro extraction targets: output tier policy, quality command, source-set plan, page budgets, query eval pack, coverage report, skill compaction.
- Use for: V2 roadmap and quality/eval planning.
- Do not use for: Current script truth without live verification.
- Key citations: lines 21-37 define current state; lines 72-95 define solved state; lines 97-110 define V2 problem; lines 143-161 rank V2 actions; lines 163-213 define compaction.

## 4. File-by-File Macro/Meso/Micro Index

### `apex-kb-target-drift-failure-learning.okf.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: low
```

#### Macro
Records the critical failure that produced the prior bad folder index and defines this corrected output class as an Apex KB lifecycle failure/upgrade index.

#### Meso
- Failure event and root cause.
- Source-access/source-authority distinction.
- Mandatory prewrite gates.
- Corrected classes and output design.
- Concrete demotion of NARM files from read-first.

#### Micro
- `wrong_output_class: folder_inventory_router_disguised_as_lifecycle_index`.
- `source_access_is_not_source_authority` gate.
- `read_first_purity_gate` requires 100% direct relevance.
- True read-first core explicitly includes chat drift, V2 planning, source-payload handover, update plan, lifecycle execution audit, and Codex audit.

#### What this file offers for Apex KB lifecycle development
A hard classifier and contradiction blocker for future lifecycle indexes.

#### What this file must not be allowed to do
It must not add broad guardrail prose without actually enforcing demotion and read-first purity.

#### Best future query routes
Target drift prevention; source-access vs authority; generated index failure repair; read-first purity.

#### Line evidence
Lines 23-39, 40-71, 73-123, 125-148, 173-193, 198-247.

### `apex-kb-chat-drift-learning.okf.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: low
```

#### Macro
Durable process memory for Apex KB chat/process drift.

#### Meso
- Lifecycle order.
- Deterministic vs LLM ownership.
- Failure modes and corrected rules.
- Mandatory response protocol.
- Executor routing matrix.

#### Micro
- Deterministic ownership includes scaffold, hashing, manifest shape, Phase 0 maps, index/retrieval/lint/audit.
- LLM ownership includes relevance judgment, concept/entity synthesis, Phase 1/2, query synthesis.
- Codex handoffs must be complete one-block execution packets.

#### What this file offers for Apex KB lifecycle development
Prevents phase rewinds, deterministic loop overextension, option sprawl, and wrong executor routing.

#### What this file must not be allowed to do
It should not be treated as a source-payload schema or retrieval technical contract.

#### Best future query routes
Codex prompt repair; lifecycle phase preservation; executor selection; no-option-sprawl.

#### Line evidence
Lines 28-43, 45-83, 85-168, 169-229, 230-355.

### `apex-kb-v2-source-payload-manifest-handover.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: low
```

#### Macro
Locks source custody as the current next patch and defines the payload-manifest companion artifact.

#### Meso
- Accepted decisions and must-not-reopen list.
- Problem stack: context drift, source custody weakness, lifecycle fragmentation, tool omission.
- Target architecture and manifest split.
- BagIt insertion point after source intake and before Phase 0.
- Tool exclusions.

#### Micro
- Add `generate-source-payload-manifest` to `apex-meta/scripts/apex_kb.py`.
- Output `apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json`.
- Use first-level `raw/` folders and `root` group for direct raw files.
- No hardcoded four semantic batches; no semantic filename inference.

#### What this file offers for Apex KB lifecycle development
The clearest source-custody patch contract.

#### What this file must not be allowed to do
Do not use it to reopen parser libraries, retrieval architecture, or operator-gate debates.

#### Best future query routes
Source payload manifest; BagIt-style custody; manifest split; patch scope.

#### Line evidence
Lines 20-48, 80-114, 120-174, 202-272, 292-371.

### `Apex-KB_UpdatePlan.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: low
```

#### Macro
Implementation-ready source-custody update plan.

#### Meso
- Executive verdict: focused source-custody patch.
- Manifest split and generic grouping.
- Four-stage lifecycle model.
- CLI command and flags.
- Hashing/idempotency/validation.
- Tool inclusion matrix and final Codex prompt.

#### Micro
- `hashlib`, `pathlib`, `json`, `argparse` included.
- `markdown-it-py`, PyYAML/frontmatter, SQLite, Node/remark, external BagIt package excluded from this patch.
- Validation includes temp KB with `raw/refs/a.md`, `raw/notes/b.md`, `raw/root-file.md`, idempotency diff.

#### What this file offers for Apex KB lifecycle development
A directly executable micro plan for the source-payload manifest command.

#### What this file must not be allowed to do
Do not let its optional docs become a broad package rewrite.

#### Best future query routes
Exact manifest JSON shape; hashing; command validation; tool inclusion/exclusion.

#### Line evidence
Lines 5-20, 38-60, 64-90, 100-175, continuation lines 3-24 and 50-61.

### `Apex KB Lifecycle Execution Audit.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: low
```

#### Macro
Audits a real Apex KB lifecycle run for `apex-plan-sync-session-workflow-v2`.

#### Meso
- Pass 1 lifecycle through Phase 1.
- Pass 2 deterministic checks after Phase 1.
- Positive findings: branch safety, scoped staging, Phase 2 not run, lint/audit/status/health pass, operator gate preserved.
- Problems: CLI flag ordering, flag aliases, scaffold directories, pointer-only Phase 0, parallel ordered commands, commit check quoting.

#### Micro
- Global flags before subcommands worked while post-subcommand flags failed.
- `source-intake` uses `--source-path`, not `--source`.
- `hash` uses `--path`, not `--source`.
- Empty scaffold directories are not Phase 2 execution.
- Pointer-only sources may produce zero Phase 0 file count unless scanned or warned.

#### What this file offers for Apex KB lifecycle development
Concrete friction-to-patch evidence from a successful but noisy run.

#### What this file must not be allowed to do
Do not treat this KB-specific audit as semantic authority over Apex Plan/Sync/Session content.

#### Best future query routes
CLI compatibility; Phase 2 gate; pointer-only Phase 0; ordered execution; safety audit.

#### Line evidence
Lines 20-95, 96-187, 191-258, 260-343, 344-483, continuation lines 3-42, 201-288, 288-399, 465-480.

### `codex-old-agent-kb-execution-process-audit.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: low
```

#### Macro
Audits deterministic Codex runs for the old-agent KB.

#### Meso
- Lifecycle succeeded but inefficiently.
- Timeline covers lifecycle start, publishing, Phase 2 reconciliation, retrieval/index validation, lint command implementation, final postflight, post-LLM validation.
- Problems: branch chaos, unrelated dirty-file false stops, flag placement, PowerShell JSON, pointer-only Phase 0, remote/local divergence, wiki index vs retrieval index.

#### Micro
- Work directly on main when operator preference says main-only.
- Stop only on overlapping dirty files.
- Accept `--allow-write` after subcommands or correct examples.
- Use UTF-8-safe PowerShell JSON capture.
- Run `apex_kb.py index` before retrieval build-index.

#### What this file offers for Apex KB lifecycle development
A patch backlog and execution-process standard derived from real Codex failures.

#### What this file must not be allowed to do
Do not use it to judge old-agent semantic page correctness.

#### Best future query routes
Dirty-tree policy; branch policy; PowerShell behavior; retrieval/index sequencing; patch backlog.

#### Line evidence
Lines 28-39, 41-126, 130-205, 207-265, continuation lines 3-31, 50-80, 82-112, 171-316.

### `apex-kb-next-runbook-v2.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: medium
  contamination_risk: low
```

#### Macro
Compact lifecycle runbook.

#### Meso
- Inputs.
- Deterministic preparation.
- Phase 1 semantic ingest.
- Approval gate.
- Phase 2 compile.
- Postflight and final report.

#### Micro
- Phase 1 high-risk claims require source-specific analysis.
- Gate phrase is exactly `approve ingest`.
- Phase 2 generates summaries, concepts, entities, semantic index, audit/risk items, and query packets.
- Postflight includes query simulations.

#### What this file offers for Apex KB lifecycle development
A clean phase map and operator prompt template.

#### What this file must not be allowed to do
Do not use it to replace the deeper script contracts.

#### Best future query routes
Lifecycle order; approval gate; Phase 2 compile order; postflight checklist.

#### Line evidence
Lines 14-29, 30-44, 45-62, 64-83, 85-105.

### `apex-kb-full-lifecycle-test-handover.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P0
  lifecycle_relevance: direct
  confidence: high
  token_value: medium
  contamination_risk: low
```

#### Macro
Handover for end-to-end Apex KB lifecycle testing.

#### Meso
- Current state and canonical package/script paths.
- Recent completed Phase 0 script fixes.
- Suggested test mission and live files to read.
- Boundaries and caveats.

#### Micro
- Canonical package is `.claude/skills/apex-kb/`.
- Main scripts are `apex_kb.py` and `apex_kb_retrieval.py`.
- Phase 0 scans `sources/` and `raw/` and reads inventories with `utf-8-sig`.
- Full test includes scaffold through retrieval query/export/lint/audit/status.

#### What this file offers for Apex KB lifecycle development
Canonical path and command-flow alignment for lifecycle smoke tests.

#### What this file must not be allowed to do
Do not hardcode `claude-skill-design` as a default KB; it is explicitly a test/reference KB.

#### Best future query routes
Canonical package; end-to-end test flow; Phase 0 boundaries.

#### Line evidence
Lines 5-21, 23-61, 63-67.

### `apex-kb-v2-planning-handover.md`

```yaml
file_profile:
  scope_class: apex_kb_lifecycle_core
  read_priority: P1
  lifecycle_relevance: direct
  confidence: high
  token_value: high
  contamination_risk: medium
```

#### Macro
V2 planning handover after V1 execution proof and repair.

#### Meso
- Evidence base to load.
- Solved V1 state.
- V2 efficiency/quality problem.
- Priority metric.
- Ranked high-impact realizations.
- Compaction recommendations and extensions.

#### Micro
- Output tiers: `source_only`, `analysis_only`, `compiled_minimal`, `compiled_full`, `query_only`.
- Add deterministic quality/eval command.
- Compact SKILL.md into routing kernel.
- Add source-set planning, page-class budgets, claim-density, query-performance smoke tests, coverage dashboard.

#### What this file offers for Apex KB lifecycle development
High-level V2 roadmap and prioritization model.

#### What this file must not be allowed to do
Do not treat its branch/test context as current live repo truth without verification.

#### Best future query routes
V2 roadmap; quality/eval; compaction; source-set planning; page budgets.

#### Line evidence
Lines 21-37, 39-70, 72-110, 112-161, 163-213, 215-248.

### `codex-run-apex-kb-contract-repair.md`

```yaml
file_profile:
  scope_class: apex_kb_supporting_evidence
  read_priority: P1
  lifecycle_relevance: supporting
  confidence: high
  token_value: medium
  contamination_risk: low
```

#### Macro
Concrete Codex handoff to run package contract repair.

#### Meso
- Target repo/path.
- Repair script path.
- Allowed file scope.
- Execution steps.
- Expected repairs.
- Validation and report format.

#### Micro
- Repair script: `scripts/fix_apex_kb_package_contracts.py`.
- Allowed files include SKILL.md, wiki template, script command contract, ingest/query/lint/audit rules, and `apex_kb.py`.
- Expected repairs include source storage modes, gate policy, claim labels, frontmatter uncollapse, JSON compatibility.

#### What this file offers for Apex KB lifecycle development
A bounded repair example and allowed-scope pattern.

#### What this file must not be allowed to do
Do not use it as a current execution command unless the repair script and branch state are live-verified.

#### Best future query routes
Package contract repair; allowed patch scope; validation report schema.

#### Line evidence
Lines 3-21, 23-42, 43-66, 68-100, 102-133.

### `FailureAnalysis_ChatHistory.md`

```yaml
file_profile:
  scope_class: apex_kb_supporting_evidence
  read_priority: P1
  lifecycle_relevance: supporting
  confidence: medium
  token_value: medium
  contamination_risk: medium
```

#### Macro
Corrected deterministic closure prompt after a partial-packet failure.

#### Meso
- Recognizes prior structural failure.
- Defines one full Codex execution flow.
- Uses main branch, no PR, no redesign.
- Validates two lint commands and writes a final report.

#### Micro
- Prior PASS commit: `d2b418...`.
- Commands: `lint-repo-execution-router`, `lint-historical-path-authority`.
- Output report path under old-agent KB synthesis.
- Full script includes repo resolution, checkout, pull, py_compile, fixtures, JSON validation, status/lint/audit/health.

#### What this file offers for Apex KB lifecycle development
Example of the full deterministic execution closure pattern.

#### What this file must not be allowed to do
Do not copy its strict dirty-tree stop uncritically; later audits prefer overlap-aware dirty policy.

#### Best future query routes
Full Codex closure flow; lint command validation; deterministic fixture design.

#### Line evidence
Lines 5-20, 22-49, 52-101, 152-201.

### `Apex-KB_FixesClaude.md`

```yaml
file_profile:
  scope_class: apex_kb_supporting_evidence
  read_priority: P1
  lifecycle_relevance: supporting
  confidence: high
  token_value: medium
  contamination_risk: medium
```

#### Macro
Fix-first, simplify-second remediation program.

#### Meso
- Truth/auditability before simplification.
- Eight-step remediation program.
- Work order from source custody to artifact hygiene, deterministic stability, S10 maintenance, retrieval eval, semantic cleanup, lifecycle simplification, clutter reduction.

#### Micro
- Step 1: restore source custody baseline.
- Step 2: separate canonical from derived artifacts.
- Step 3: stabilize deterministic validation.
- Step 4: create real S10 maintenance loop.
- Step 5: harden retrieval evaluation.

#### What this file offers for Apex KB lifecycle development
A strategic remediation sequence useful after source-custody patching.

#### What this file must not be allowed to do
Do not treat its questions as blockers when the user asks for deterministic execution.

#### Best future query routes
Remediation ordering; S10 maintenance; derived artifact hygiene; retrieval eval.

#### Line evidence
Lines 3-13, 17-30, 34-44, 47-57.

### `process-validation-and-extension-review_20260630.md`

```yaml
file_profile:
  scope_class: transferable_domain_process_evidence
  read_priority: appendix
  lifecycle_relevance: transferable
  confidence: high
  token_value: medium
  contamination_risk: medium
```

#### Macro
Lika/tax KB process validation report with strong transferable lifecycle lessons.

#### Meso
- Source availability ledger.
- Process reconstruction.
- Artifact inventory.
- Impact/evidence/risk matrix.
- Token and retrieval simulation.
- Source-grounding audit.

#### Micro
- Distinguishes repo truth from chat-output artifacts.
- Verifies deterministic Phase 0 and manifest status.
- Flags Phase 2 summaries/concepts as not installed in verified repo.
- Requires source refs, hashes/no-hash reasons, confidence, claim labels, open questions, review flags.

#### What this file offers for Apex KB lifecycle development
Transferable process lessons on repo-state verification, chat-output vs installed artifacts, and high-risk source grounding.

#### What this file must not be allowed to do
Do not steer generic Apex KB architecture with Lika tax content.

#### Best future query routes
Repo-state vs chat-output; Phase 2 installed-state verification; source-grounding checks.

#### Line evidence
Lines 15-29, 30-52, 53-83, 123-147.

### `next-actions-ranked_20260630.md`

```yaml
file_profile:
  scope_class: transferable_domain_process_evidence
  read_priority: appendix
  lifecycle_relevance: transferable
  confidence: high
  token_value: medium
  contamination_risk: medium
```

#### Macro
Lika/tax ranked action plan.

#### Meso
- Ranked next actions.
- Deferred gap matrix.
- Mandatory sequence.

#### Micro
- First action is verifying repo vs chat-output state.
- Backfill source-specific high-risk Phase 1 analyses.
- Install/regenerate summaries and concepts.
- Rebuild index/retrieval and run query simulations.

#### What this file offers for Apex KB lifecycle development
A transferable post-Phase-0/Phase-2 sequencing example.

#### What this file must not be allowed to do
Do not use Lika-specific legal/tax priorities as generic Apex KB priorities.

#### Best future query routes
Ranked domain lifecycle continuation; query simulation; high-risk source-specific backfill.

#### Line evidence
Lines 11-24, 26-41, 43-51.

### `apex-kb-handoff-folder-index.md`

```yaml
file_profile:
  scope_class: generated_index_artifact_under_review
  read_priority: exclude_from_core
  lifecycle_relevance: stale
  confidence: high
  token_value: low
  contamination_risk: high
```

#### Macro
Prior generated folder index that caused the target-drift failure.

#### Meso
- It correctly noticed Apex KB process and NARM-support families.
- It then contradicted itself by ranking NARM files read-first.
- It contains useful failure evidence and some true process topic rows.

#### Micro
- Lines 7-14 say NARM files are not generic Apex KB authority.
- Lines 20-26 rank NARM files 3-7 in read-first.
- Lines 63-80 list tools and execution standards but also state some evidence is absent from folder.

#### What this file offers for Apex KB lifecycle development
A concrete example of the prior bad classification and some salvageable topic categories.

#### What this file must not be allowed to do
Do not trust its read-first ranking.

#### Best future query routes
Failure evidence; redundancy audit; target drift example.

#### Line evidence
Lines 7-14, 16-26, 63-80, 123-132.

### `apex-kb-handoff-topic-map.okf.md`

```yaml
file_profile:
  scope_class: generated_index_artifact_under_review
  read_priority: exclude_from_core
  lifecycle_relevance: stale
  confidence: high
  token_value: low
  contamination_risk: high
```

#### Macro
Prior machine-readable topic map duplicating the bad folder index.

#### Meso
- Source folder recorded as `apex-meta/handoff/`, not the current analysis subfolder.
- Lists NARM files as read-priority 3-7.
- Has useful topic structures but contaminated priorities.

#### Micro
- `files_read` includes NARM and Apex files together.
- NARM entries get read_priority 3-7.
- `topic_routes` includes domain project indexing separately but still mixed in read-first data.

#### What this file offers for Apex KB lifecycle development
Evidence that machine-readable outputs can harden bad routing if not stricter than prose.

#### What this file must not be allowed to do
Do not use as routing authority.

#### Best future query routes
Machine-readable redundancy; prior ranking error; domain-context exclusion.

#### Line evidence
Lines 4-20, 21-85, 86-156, 205-222.

### `apex-kb-handoff-file-ledger.json`

```yaml
file_profile:
  scope_class: generated_index_artifact_under_review
  read_priority: exclude_from_core
  lifecycle_relevance: stale
  confidence: high
  token_value: low
  contamination_risk: high
```

#### Macro
Prior JSON file ledger duplicating the bad ranking.

#### Meso
- Lists only seven files from old `apex-meta/handoff/` scope.
- Promotes NARM entries to read_priority 3-7.
- Includes a non-reopen rule not to treat domain handoffs as generic authority, creating a contradiction with read-first.

#### Micro
- `read_first` includes NARM prep file.
- `topic_routes.domain_project_indexing` properly isolates NARM but not enough to prevent read-first pollution.

#### What this file offers for Apex KB lifecycle development
Redundancy and contradiction evidence for machine-readable artifact audit.

#### What this file must not be allowed to do
Do not use its read_priority values.

#### Best future query routes
Prior machine ledger failure; redundancy/token waste audit.

#### Line evidence
Lines 3-26, 33-62, 63-131, 133-157.

### `findings.md`

```yaml
file_profile:
  scope_class: domain_only_context
  read_priority: appendix
  lifecycle_relevance: domain_only
  confidence: high
  token_value: low_for_lifecycle_high_for_narm
  contamination_risk: medium
```

#### Macro
NARM-support therapy KB durable findings.

#### Meso
- NARM-support project intent.
- Decisions made.
- Source notes and named sources.
- Open questions around destination, redaction, relationship notes, adjacent practice context.
- Operator validation.

#### Micro
- Four functions: NARM theory indexing, personal psychological material indexing, guided self-exploration flows, therapist session prep.
- Therapy-support infrastructure, not therapist replacement.

#### What this file offers for Apex KB lifecycle development
Only a transferable example that source notes and operator validation matter.

#### What this file must not be allowed to do
It must not steer generic Apex KB lifecycle architecture or be read-first for lifecycle work.

#### Best future query routes
NARM-specific continuation; domain source custody; redaction questions.

#### Line evidence
Lines 3-32.

### `Apex-KB_FixesClaude2.md`

```yaml
file_profile:
  scope_class: stale_or_contaminating
  read_priority: exclude_from_core
  lifecycle_relevance: stale
  confidence: high
  token_value: low
  contamination_risk: high
```

#### Macro
Early BagIt/source-manifest design draft with unverified assumptions.

#### Meso
- Claims repo context but says it cannot directly read live repo files.
- States no confirmed source-intake command.
- Proposes hardcoded four batch groups.
- Later accepted decisions supersede this with generic `--kb-root`, raw-folder-derived grouping, and no hardcoded semantic batches.

#### Micro
- Lines 21-23 say no confirmed source-intake command.
- Lines 24-39 propose fixed `BAGIT_BATCH_GROUPS` and `generate-source-manifest`, which conflicts with the later generic `generate-source-payload-manifest` plan.

#### What this file offers for Apex KB lifecycle development
Contamination trace showing why hardcoded semantic batches and unverified repo assumptions must be blocked.

#### What this file must not be allowed to do
Do not use it as implementation authority.

#### Best future query routes
Stale assumptions; hardcoded batch contamination; source-payload manifest evolution history.

#### Line evidence
Lines 3-18 and continuation lines 4-39.

## 5. Idea-to-File Map

| Idea / Decision / Failure Pattern | Primary file(s) | Supporting file(s) | Lifecycle phase | Importance | Notes |
|---|---|---|---|---:|---|
| Target drift prevention | `apex-kb-target-drift-failure-learning.okf.md` | prior generated index/map/ledger | process_learning_and_failure_prevention | 100 | Mandatory gate for this artifact class. |
| Source-access vs source-authority | `apex-kb-target-drift-failure-learning.okf.md` | `apex-kb-handoff-folder-index.md` | process_learning_and_failure_prevention | 100 | Prevents folder membership from becoming read-first authority. |
| Source custody and payload manifest | `apex-kb-v2-source-payload-manifest-handover.md`, `Apex-KB_UpdatePlan.md` | `Apex-KB_FixesClaude.md`, `Apex-KB_FixesClaude2.md` | source_payload_manifest | 100 | Later files supersede hardcoded batch design. |
| BagIt-style raw payload proof | `apex-kb-v2-source-payload-manifest-handover.md`, `Apex-KB_UpdatePlan.md` | `Apex-KB_FixesClaude2.md` as warning | source_payload_manifest | 98 | Generic folder-derived, not semantic batch-derived. |
| Phase 0 deterministic corpus intelligence | `apex-kb-next-runbook-v2.md`, `apex-kb-full-lifecycle-test-handover.md` | `apex-kb-chat-drift-learning.okf.md` | phase0_deterministic_corpus_intelligence | 94 | Phase 0 is deterministic, not semantic. |
| Phase 1 semantic ingest analysis | `apex-kb-next-runbook-v2.md`, `apex-kb-chat-drift-learning.okf.md` | `process-validation-and-extension-review_20260630.md` | phase1_ingest_analysis | 92 | LLM-owned; source-specific for high-risk domains. |
| Phase 2 wiki compile | `apex-kb-next-runbook-v2.md`, `apex-kb-full-lifecycle-test-handover.md` | `process-validation-and-extension-review_20260630.md` | phase2_wiki_compile | 90 | Requires approval phrase where gate policy applies. |
| Operator gate policy | `apex-kb-next-runbook-v2.md`, `Apex KB Lifecycle Execution Audit.md` | `process-validation-and-extension-review_20260630.md` | operator_gate | 88 | There is tension with one-prompt flow in source-payload plan; future tasks must respect current operator mode. |
| Retrieval / FTS5 / BM25 / query packets | `codex-old-agent-kb-execution-process-audit.md`, `apex-kb-next-runbook-v2.md` | `process-validation-and-extension-review_20260630.md`, `next-actions-ranked_20260630.md` | retrieval_build_and_query | 86 | Folder has process evidence, not full technical contract. |
| Lint / audit / status / health | `Apex KB Lifecycle Execution Audit.md`, `codex-old-agent-kb-execution-process-audit.md` | `apex-kb-v2-planning-handover.md` | lint_audit_status_health | 94 | Strong evidence of command friction and patch backlog. |
| Codex main-only execution | `codex-old-agent-kb-execution-process-audit.md`, `apex-kb-chat-drift-learning.okf.md` | `FailureAnalysis_ChatHistory.md`, `apex-kb-full-lifecycle-test-handover.md` | codex_execution_and_postflight | 96 | Branches/PRs are contamination unless explicitly requested. |
| Branch and dirty-tree handling | `codex-old-agent-kb-execution-process-audit.md` | `Apex KB Lifecycle Execution Audit.md` | codex_execution_and_postflight | 94 | Use overlap-aware dirty policy. |
| Prompt design failures | `apex-kb-chat-drift-learning.okf.md`, `FailureAnalysis_ChatHistory.md` | `codex-old-agent-kb-execution-process-audit.md` | process_learning_and_failure_prevention | 95 | Full execution packets, no options, no phase rewind. |
| Machine-readable artifact strictness | `apex-kb-target-drift-failure-learning.okf.md` | prior generated OKF/JSON | process_learning_and_failure_prevention | 96 | Machine files must be smaller and stricter than prose. |
| Redundancy and token-waste control | `apex-kb-target-drift-failure-learning.okf.md`, `apex-kb-v2-planning-handover.md` | prior generated artifacts | process_learning_and_failure_prevention | 90 | Avoid Markdown+OKF+JSON duplication. |
| Domain-context exclusion | `apex-kb-target-drift-failure-learning.okf.md` | `findings.md`, prior generated artifacts | process_learning_and_failure_prevention | 100 | Domain files can be valid and still excluded from core. |
| Process drift and phase rewind | `apex-kb-chat-drift-learning.okf.md` | `FailureAnalysis_ChatHistory.md` | process_learning_and_failure_prevention | 98 | Preserve state unless hard evidence invalidates it. |

## 6. Lifecycle Phase Map

| Lifecycle phase | Files that help | What they add | Missing / weak evidence |
|---|---|---|---|
| scaffold | `apex-kb-full-lifecycle-test-handover.md`, `Apex KB Lifecycle Execution Audit.md` | Canonical scripts, command sequence, scaffold caveats. | Current live script behavior must be checked before patching. |
| source_intake | `Apex KB Lifecycle Execution Audit.md`, `codex-old-agent-kb-execution-process-audit.md` | `--source-path` alias issue, pointer-only source behavior. | Need current script verification. |
| source_payload_manifest | `apex-kb-v2-source-payload-manifest-handover.md`, `Apex-KB_UpdatePlan.md` | Command/schema/hash/grouping contract. | Need live implementation status. |
| phase0_deterministic_corpus_intelligence | `apex-kb-next-runbook-v2.md`, `apex-kb-full-lifecycle-test-handover.md`, audits | Phase 0 artifact expectations and pointer/raw/sources behavior. | Graph/process-flow details not in folder. |
| phase1_ingest_analysis | `apex-kb-next-runbook-v2.md`, `process-validation-and-extension-review_20260630.md`, `next-actions-ranked_20260630.md` | Source-specific vs grouped analysis policy. | Domain examples are Lika-specific. |
| operator_gate | `apex-kb-next-runbook-v2.md`, `Apex KB Lifecycle Execution Audit.md`, process validation | Approval phrase and gate preservation. | One-prompt flow/gate policy needs current task context. |
| phase2_wiki_compile | `apex-kb-next-runbook-v2.md`, process validation, next actions | Compile order and repo-output vs chat-output warning. | Current compiled repo pages must be live-verified. |
| deterministic_index_validation | audits, full lifecycle handover | Wiki index rebuild behavior and stale warnings. | Need current `apex_kb.py status/lint` behavior. |
| retrieval_build_and_query | old-agent audit, runbook, Lika validation | Retrieval after index; query simulations; derived index distinction. | Full FTS5/BM25 contract not in this folder. |
| query_packet_generation | runbook, process validation, next actions | Query packets after Phase 2 and retrieval. | Needs target KB-specific query suite. |
| lint_audit_status_health | lifecycle audit, old-agent audit | Command contracts, JSON flags, status distinctions, health checks. | Need implementation verification. |
| codex_execution_and_postflight | chat drift, old-agent audit, failure history | Main-only, complete execution packet, dirty-tree policy, commit/push. | Connector vs local git execution should be declared per run. |
| process_learning_and_failure_prevention | target drift, chat drift, prior generated artifacts | Anti-drift gates and redundancy controls. | Must be enforced, not repeated as prose only. |

## 7. Tool / Script / Process Inclusion Map

| Tool/process | Files mentioning it | Current status | Why it matters | Risk | Next action |
|---|---|---|---|---|---|
| `apex_kb.py` | source-payload handover, UpdatePlan, lifecycle audits, contract repair, full lifecycle handover | Canonical deterministic lifecycle script | Owns source custody, Phase 0, index, lint/audit/status, lifecycle helpers. | Command-surface drift if not live-verified. | Fetch live script before any patch. |
| `apex_kb_retrieval.py` | full lifecycle handover, old-agent audit, runbook | Retrieval script/process surface | Builds/queries derived retrieval index. | Retrieval freshness can be confused with wiki index freshness. | Verify script and run after `apex_kb.py index`. |
| `source-manifest.json` | source-payload handover, UpdatePlan, V2 planning, process validation | Canonical source-reference ledger | Tracks source identity/storage/ingest status. | Empty/weak manifest breaks custody. | Preserve role; add companion payload manifest. |
| `source-payload-manifest.json` | source-payload handover, UpdatePlan, FixesClaude2 | Accepted companion artifact | Proves raw payload state with file/group/root hashes. | Hardcoded batch contamination from FixesClaude2. | Implement generic folder-derived command if absent. |
| SQLite FTS5 / BM25 | UpdatePlan as deferred, runbook, audits | Retrieval layer, not custody layer | Local deterministic retrieval over compiled pages. | Premature retrieval patch can distract from source custody. | Use after compiled pages and index rebuild. |
| Markdown parser / heading-link-frontmatter maps | chat drift, runbook, full lifecycle handover | Phase 0 navigation layer | Helps LLM route sources without semantic synthesis. | Parser-library drift if discussed outside parser task. | Keep V1 simple; verify only when parser warnings require. |
| Graph/process-flow extraction | prior folder index, chat drift indirectly | Future V1.5 navigation | Maps process edges and file relationships. | Not enough technical spec in folder. | Route to graph audit/project resources when active. |
| GitHub connector | generated artifacts, this run | Repo access/write surface | Useful when local terminal unavailable. | Connector writes do not run local validation. | Declare connector vs local execution in final reports. |
| Codex execution prompt standards | chat drift, old-agent audit, failure analysis | Binding process standard | Prevents branch drift and partial handoffs. | Over-strict dirty policy can waste turns. | Main-only, overlap-aware dirty, complete command flow. |
| lint / audit / status / health | audits, runbook, V2 planning | Deterministic validation | Exposes structural/stale defects. | False pass/fail if index types confused. | Separate wiki and retrieval freshness. |
| query eval pack | V2 planning, next actions, runbook | Proposed V2 quality layer | Proves retrieval/token value. | Requires compiled pages first. | Add after Phase 2 and retrieval rebuild. |
| quality/eval command | V2 planning, prior index | Proposed V2 command | Measures non-semantic structure and coverage beyond lint. | Risk of LLM semantics creeping into Python. | Python counts structure; LLM writes quality notes. |
| source-set planning | V2 planning | Proposed ingest-planning layer | Reduces blind ingestion and token waste. | Could become another gate if overdone. | Use as compact LLM planning artifact. |

## 8. Failure Pattern and Guardrail Map

| Failure pattern | Where documented | How it manifested | Guardrail / repair | Future trigger |
|---|---|---|---|---|
| Folder membership treated as lifecycle relevance | target-drift file; prior generated index | NARM/domain files ranked read-first | Read-first only core lifecycle files | Any folder index task. |
| Machine-readable duplication of bad routing | target-drift file; old OKF/JSON | Bad ranking repeated in Markdown, OKF, JSON | One index file or strict compact routing map only | Generating multiple artifacts. |
| Partial Codex handoffs | chat drift; FailureAnalysis | User had to assemble execution flow | One complete executable artifact per Codex task | User asks for Codex/execution prompt. |
| Option sprawl when execution is defined | chat drift | Alternatives offered despite known next step | Single next action unless options requested | User asks to continue process. |
| Phase rewind | chat drift | Returned to earlier decisions/gates | Preserve latest state unless hard blocker | Follow-up lifecycle tasks. |
| Deterministic loop overextension | chat drift | More validation after PASS instead of semantic continuation | Advance lifecycle after deterministic PASS | Postflight closure. |
| Branch chaos | old-agent audit | Work invisible across follow-up because branch/main split | Work on main unless explicit branch request | Codex repo changes. |
| Dirty unrelated files caused false stop | old-agent audit | Validation stopped on unrelated dirt | Stop only on overlapping dirty paths | Any repo task with dirty tree. |
| CLI global flag mismatch | lifecycle audit; old-agent audit | `--json`/`--allow-write` placement failed | Accept both placements or document exact syntax | Running script commands. |
| PowerShell JSON encoding | old-agent audit | UTF-16 redirection broke JSON validation | Use UTF-8 `Set-Content` or native output path | PowerShell command captures. |
| Pointer-only source not scanned by Phase 0 | lifecycle audit; old-agent audit | Source manifest had pointer entries but Phase 0 saw zero files | Scan repo-internal pointer paths or emit warning | Pointer-only source-intake. |
| Wiki index vs retrieval index confusion | old-agent audit | Retrieval fresh but wiki index stale | Separate `wiki_index_status` and `retrieval_index_status` | Post-LLM validation. |
| Chat-output mistaken for repo truth | process validation; next actions | Phase 2 pages existed as chat output, not installed repo pages | Verify repo state before claiming compiled KB | Phase 2 compilation/evaluation. |
| Hardcoded batch groups | FixesClaude2 | Proposed four fixed groups before folder verification | Derive groups from actual raw folders | Source-payload manifest patch. |

## 9. Redundancy and Token-Waste Audit

| Redundant cluster | Files | Repeated content | Keep | Compress | Delete/deprecate | Reason |
|---|---|---|---|---|---|---|
| Prior handoff index trio | `apex-kb-handoff-folder-index.md`, `apex-kb-handoff-topic-map.okf.md`, `apex-kb-handoff-file-ledger.json` | File list, rankings, topic map, source access | Keep only as under-review failure evidence | Do not read except for target-drift audit | Deprecate as routing authority | All three preserve or repeat the read-first/domain contradiction. |
| Source-payload planning cluster | `apex-kb-v2-source-payload-manifest-handover.md`, `Apex-KB_UpdatePlan.md`, `Apex-KB_FixesClaude2.md` | BagIt/source-payload ideas | Keep first two as authority | Treat FixesClaude2 as contamination history | Deprecate FixesClaude2 for implementation | Later files supersede hardcoded batch draft. |
| Process drift cluster | `apex-kb-chat-drift-learning.okf.md`, `FailureAnalysis_ChatHistory.md`, old-agent audit | Codex prompt failures, no options, main-only | Keep chat drift as general rule; old-agent audit as evidence | Use FailureAnalysis only for example prompt shape | Do not repeat all three in every prompt | Chat drift captures the abstract rule; audits provide evidence. |
| Lika domain/process cluster | `process-validation-and-extension-review_20260630.md`, `next-actions-ranked_20260630.md` | Repo-vs-chat output, high-risk source backfill, query sims | Keep as transferable appendix | Summarize only when process question matches | Do not use as generic lifecycle authority | Domain-specific tax content should not steer Apex KB core. |
| V2 planning cluster | `apex-kb-v2-planning-handover.md`, `Apex-KB_FixesClaude.md` | V2 improvements and remediation sequence | Keep both; they answer different levels | Compress into roadmap if used later | No delete | V2 planning ranks features; FixesClaude sequences remediation. |

## 10. Stale / Contamination / Domain-Only Appendix

### `findings.md`

- Why it is not core: It is about a NARM-support therapy knowledgebase, not generic Apex KB lifecycle mechanics.
- Whether it has transferable process value: Low to medium. It shows source notes and operator validation but not lifecycle architecture.
- Safe use: NARM-specific continuation, source custody for NARM, redaction/open-question handling.
- Unsafe use: Ranking it read-first for Apex KB lifecycle improvement.

### `process-validation-and-extension-review_20260630.md`

- Why it is not core: It is a Lika/tax-accounting KB validation report.
- Whether it has transferable process value: High. It distinguishes repo truth from chat-output artifacts, validates Phase 0/Phase 1/Phase 2 state, and defines source-grounding checks.
- Safe use: Process examples for repo-state verification and post-Phase-2 validation.
- Unsafe use: Importing Lika tax priorities into generic Apex KB architecture.

### `next-actions-ranked_20260630.md`

- Why it is not core: It ranks Lika/tax accounting next actions.
- Whether it has transferable process value: Medium. It gives a useful sequence: verify repo state, backfill high-risk source-specific analysis, compile pages, rebuild index/retrieval, run query sims.
- Safe use: Pattern for domain KB continuation after Phase 0/Phase 2 uncertainty.
- Unsafe use: Treating legal/tax risk priorities as generic Apex KB priorities.

### `apex-kb-handoff-folder-index.md`

- Why it is not core: Prior generated index under review; contains the bad read-first ranking.
- Whether it has transferable process value: High as failure evidence.
- Safe use: Redundancy and target-drift audit.
- Unsafe use: Any read-first routing.

### `apex-kb-handoff-topic-map.okf.md`

- Why it is not core: Prior machine map under review; repeats old folder scope and bad NARM priorities.
- Whether it has transferable process value: High as a lesson that machine outputs must be stricter than prose.
- Safe use: Machine-readable failure evidence.
- Unsafe use: Routing authority.

### `apex-kb-handoff-file-ledger.json`

- Why it is not core: Prior machine ledger under review; repeats bad read-first routing.
- Whether it has transferable process value: High as evidence of redundant machine artifact failure.
- Safe use: Redundancy audit.
- Unsafe use: File priority routing.

### `Apex-KB_FixesClaude2.md`

- Why it is not core: Contains unverified assumptions and hardcoded batch-group design superseded by later generic source-payload manifest policy.
- Whether it has transferable process value: Medium as contamination trace.
- Safe use: Explain why hardcoded semantic groups and unverified repo assumptions must be rejected.
- Unsafe use: Implementing its `BAGIT_BATCH_GROUPS` or treating its source-intake claim as current.

## 11. Recommended Future Use

If the next task is **target drift prevention**, read `apex-kb-target-drift-failure-learning.okf.md`, then the prior generated artifacts only as failure evidence.

If the next task is **source custody**, read `apex-kb-v2-source-payload-manifest-handover.md` and `Apex-KB_UpdatePlan.md`; use `Apex-KB_FixesClaude2.md` only as a contamination warning.

If the next task is **lifecycle simplification**, read `apex-kb-next-runbook-v2.md`, `apex-kb-v2-planning-handover.md`, and `Apex-KB_FixesClaude.md`.

If the next task is **Codex prompt repair**, read `apex-kb-chat-drift-learning.okf.md`, `codex-old-agent-kb-execution-process-audit.md`, `Apex KB Lifecycle Execution Audit.md`, and `FailureAnalysis_ChatHistory.md`.

If the next task is **retrieval**, read `codex-old-agent-kb-execution-process-audit.md`, `apex-kb-next-runbook-v2.md`, and then live `apex_kb_retrieval.py` / retrieval contracts. This folder alone is not enough for FTS5/BM25 implementation.

If the next task is **LLM phase behavior**, read `apex-kb-chat-drift-learning.okf.md`, `apex-kb-next-runbook-v2.md`, `process-validation-and-extension-review_20260630.md`, and `next-actions-ranked_20260630.md` if a domain KB example is useful.

If the next task is **failure prevention**, read `apex-kb-target-drift-failure-learning.okf.md`, `apex-kb-chat-drift-learning.okf.md`, and both execution audits.

If the next task is **domain-specific NARM work**, read `findings.md` and search outside this analysis folder for the missing NARM handoffs (`narm-index-prep-handover.md`, `task_plan.md`, `next-session.md`, `progress.md`) if they exist elsewhere. Do not use NARM files for generic Apex KB lifecycle authority.

## 12. Non-Reopen Rules

```yaml
non_reopen:
  - do not treat folder membership as lifecycle authority
  - do not rank domain-only files as read-first lifecycle core
  - do not regenerate three redundant index artifacts with the same file ledger and priorities
  - do not reintroduce broad architecture discovery if the task is indexing
  - do not collapse deterministic inventory/source access into semantic authority
  - do not use stale generated index files as truth without checking underlying files
  - do not implement source-payload manifest from hardcoded semantic batch groups
  - do not reopen parser-library discussion for source custody patches
  - do not patch retrieval while executing a source-custody patch
  - do not create branches or PRs for Apex KB Codex work unless explicitly requested
  - do not stop on unrelated dirty files; use overlap-aware dirt policy
  - do not confuse chat-output artifacts with repo-written KB pages
```

## 13. Final Validation Checklist

```yaml
validation:
  every_discovered_file_listed: true
  every_file_has_scope_class: true
  every_file_has_macro_meso_micro: true
  no_domain_only_file_in_read_first: true
  read_first_reasons_are_direct_lifecycle_reasons: true
  generated_index_does_not_duplicate_old_bad_classification: true
  contradictions_checked: true
  line_citations_included_where_available: true
  redundancy_audit_included: true
  source_access_method_recorded: true
  generated_artifacts_classed_under_review_not_authority: true
  domain_or_project_specific_files_demoted_to_appendix: true
```
