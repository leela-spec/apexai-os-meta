# Recommendation

Use a **two-stage run**, not one free-form Deep Research mega-run.

**Best path:**

1. **Decision-lock Q&A:** lock the operator decisions in the prompt itself so the model does not rediscover settled architecture.
    
2. **Deep Research / generation run:** validate only the risky implementation details, inspect repo truth, then output **final full-file replacements / new files**, not vague recommendations.
    

This matters because Apex already has a layered architecture direction: repo-native Markdown/YAML/JSON as source of truth, tiny `CLAUDE.md`, path rules, Claude skills, deterministic Python, compiled KB pages, and SQLite/FTS5/BM25 as v1 retrieval. The prior research explicitly recommends that layered repo-native stack and keeps MCP/cloud/vector systems as escalation layers rather than canonical memory. The personal orchestration layer also must be first-class beside repo/project memory, not collapsed into project KB.

Repo access is available: `leela-spec/apexai-os-meta` exists, is private, and its code search index is active. I also confirmed the repo currently surfaces `.claude/skills/apex-kb/` files, including `SKILL.md`, manifest, templates, and command contract references. A direct repo search for `search.sqlite FTS5 BM25` returned no matches, so the prompt should require a truth pass before assuming the SQLite retrieval layer already exists.

---

# A. Fast Q&A Decision Lock

Use this as the prefilled decision sheet. Only change the answers you disagree with.

|ID|Question|Recommended answer|Why|
|--:|---|---|---|
|**Q1**|Should the run research the whole architecture again?|**No. Validate and integrate.**|The architecture has already converged on repo-native KB + deterministic Python + SQLite/BM25 v1.|
|**Q2**|Should it generate final files or just a report?|**Generate final full-file contents plus a validation report.**|The goal is integration-ready output, not another abstract audit.|
|**Q3**|Should it write to the repo directly?|**No by default. Output full-file replacements and creation paths.**|Prior repo-write workflows showed full-file replacement is safer than fake “patch hunk” wording; fetch → generate full replacement → validate is the right model.|
|**Q4**|Should the KB retrieval skill be merged into `apex-kb`?|**No. Keep `apex-kb` for custody/compilation; create `apex-query` for retrieval.**|Separation prevents `apex-kb` from becoming overbuilt.|
|**Q5**|Name of retrieval skill?|**`.claude/skills/apex-query/`**|“Query” matches your language better than “search”; prompt should allow renaming only if repo conventions already use `apex-search`.|
|**Q6**|What does `apex-kb` own?|**Source custody, manifests, compiled wiki pages, lint/audit, source-read verification.**|Prior Apex KB hardening already centers source custody/read verification.|
|**Q7**|What does `apex-query` own?|**Index building, stale checks, FTS5/BM25 query, snippets, saved query outputs.**|Keeps deterministic retrieval as a tool layer.|
|**Q8**|Should personal orchestration be indexed in the same system?|**Yes, but as a separate domain/folder, not mixed into project KB.**|Personal orchestration stores routines, flow history, AI routing, and capacity beside project memory.|
|**Q9**|Should compiled wiki pages be the retrieval surface?|**Yes.**|Prior specs define compiled pages as the LLM-readable surface instead of raw-source rereads.|
|**Q10**|Should raw sources be directly indexed?|**No by default. Only compiled pages, with raw-source fallback for conflict checks.**|Reduces token noise and prevents raw-source sprawl from dominating results.|
|**Q11**|Should the run use SQLite FTS5/BM25 as v1?|**Yes, with runtime FTS5 availability check.**|Prior audit found architecture sound but unsafe without FTS5 preflight and BM25 vector tests.|
|**Q12**|Should vector search be included now?|**No. Design optional v2 hook only.**|Local vector adds complexity; prior verdict says add only after BM25/file-first is stable.|
|**Q13**|YAML parser policy?|**Do not force stdlib-only. Prefer robust parser if allowed; otherwise define strict subset.**|“Stdlib only / no PyYAML” appears to have been AI-injected, not operator-decided.|
|**Q14**|DB location?|**`apex-meta/registry/search.sqlite` as derived artifact.**|Keep one shared registry; never treat DB as source.|
|**Q15**|Should `search.sqlite` be committed?|**No. `.gitignore` before first build.**|Previous audit marks this as a critical ordering gate.|
|**Q16**|Rebuild strategy?|**Full rebuild for v1.**|Simpler, safer, and enough for small corpora.|
|**Q17**|Staleness method?|**mtime/ns for fast check + optional hash strict mode.**|mtime alone is useful but not perfect.|
|**Q18**|Query output format?|**Human Markdown + optional JSON mode.**|Claude needs readable snippets; scripts need deterministic output.|
|**Q19**|Should `CLAUDE.md` receive full retrieval instructions?|**No. Add only a tiny routing block.**|Claude guidance favors compact `CLAUDE.md`; procedures belong in skills.|
|**Q20**|Skill package format?|**Folder with `SKILL.md`, `references/`, optional `scripts/`, optional `evals/`.**|Your skill guide defines this as canonical.|
|**Q21**|How to avoid over-engineering?|**Only build v1 files required to answer: “what should Claude read now?”**|Anything beyond custody, index, query, stale check, and validation is v2.|
|**Q22**|Definition of done?|**Final file tree, full file contents, validation commands, rollback notes, and risk report.**|Prevents another abstract research result.|

---

# B. Locked Target Architecture

```yaml
apex_kb_query_architecture_v1:
  principle: simple_resilient_repo_native_local_first

  domains:
    project_repo_memory:
      path_candidates:
        - apex-meta/kb/
        - apex-meta/projects/
        - apex-meta/state/
        - artifacts/
      purpose:
        - project knowledge
        - task state summaries
        - source-backed compiled wiki pages
        - project status inputs

    personal_orchestration_memory:
      path_candidates:
        - apex-meta/orchestration/
        - apex-meta/personal-os/
      purpose:
        - weekly and daily routines
        - flow recaps
        - AI routing history
        - model usage notes
        - personal capacity constraints
        - cross-project priorities

  skills:
    apex-kb:
      owns:
        - source custody
        - source manifests
        - compiled wiki page contracts
        - source-read verification
        - KB lint/audit
      does_not_own:
        - FTS query interface
        - BM25 ranking policy
        - project task execution
        - daily or weekly planning

    apex-query:
      owns:
        - SQLite registry/index creation
        - FTS5 availability preflight
        - BM25 query
        - snippet output
        - stale check
        - saved query output
      does_not_own:
        - raw-source rewriting
        - project planning
        - personal orchestration decisions

  retrieval_surface:
    primary: compiled_wiki_pages
    fallback: raw_sources_only_for_conflict_resolution

  generated_artifacts:
    derived_do_not_commit:
      - apex-meta/registry/search.sqlite
    source_controlled:
      - compiled wiki markdown
      - source manifests
      - query logs if intentionally saved
      - skill package files
      - scripts
      - validation fixtures
```

---

# C. Copy-Paste Deep Research Prompt

````markdown
# Deep Research Prompt — Apex KB + apex-query SQLite FTS5/BM25 Final Integration

You are GPT-5.5 Deep Research working as a senior local-first systems architect and implementation auditor for the Apex2Claude2 project.

Your task is to produce the final integration design and complete file contents for the Apex knowledge-base + local retrieval layer.

This is not broad research.
This is not architecture rediscovery.
This is not a vague recommendation report.
This is not an implementation run that writes directly to the repo.

You must inspect the provided project files and the connected repo, validate unresolved technical risks, and output final repo-ready file contents or full-file replacement blocks.

---

## 0. Mission

Create the final, coherent, minimal, resilient integration between:

1. `apex-kb`
   - source custody
   - source manifests
   - compiled wiki pages
   - source-read verification
   - lint/audit contracts

2. `apex-query`
   - SQLite FTS5/BM25 index
   - local query interface
   - stale checks
   - snippets
   - saved query outputs
   - validation fixtures

3. Apex orchestration
   - project/repo memory
   - personal orchestration memory
   - PreCap / FlowRecap / APSU loop
   - project status overview / downstream planning inputs

The final system must be simple, local-first, deterministic, cheap, token-efficient, and not over-engineered.

---

## 1. Binding decision capsule

Treat these decisions as already decided unless direct repo evidence proves a conflict.

```yaml
binding_decisions:
  execution_model:
    repo_write_now: false
    output_full_file_contents: true
    output_patch_plan: true
    output_validation_commands: true
    output_rollback_notes: true

  architecture:
    canonical_stack:
      - repo_committed_markdown_yaml_json
      - raw_source_snapshots_or_pointers_with_hashes
      - compiled_apex_kb_wiki_pages
      - deterministic_python_scripts
      - SQLite_FTS5_BM25_v1
    vector_search:
      status: optional_v2_only
    cloud_memory:
      status: escalation_only_not_canonical
    MCP:
      status: adapter_only_not_canonical

  skill_split:
    apex_kb:
      role: source_custody_compilation_lint_audit
      owns:
        - raw source custody
        - source manifests
        - compiled wiki page contracts
        - source-read verification
        - KB lint and audit
      does_not_own:
        - BM25 query ranking
        - SQLite search CLI
        - daily planning
        - project execution

    apex_query:
      role: local_retrieval_engine
      package_path: .claude/skills/apex-query/
      owns:
        - SQLite FTS5 availability preflight
        - full rebuild index creation
        - BM25 query and snippets
        - stale check
        - saved query outputs
        - query validation fixtures
      does_not_own:
        - source rewriting
        - project planning
        - operator decision-making

  naming:
    preferred_retrieval_skill_name: apex-query
    acceptable_if_repo_already_uses: apex-search
    rule: >
      Choose one name and apply it consistently. Prefer apex-query unless repo
      already has stronger evidence for apex-search.

  data_domains:
    project_repo_memory:
      role: project state, source docs, compiled KB, repo artifacts
      candidate_paths:
        - apex-meta/kb/
        - apex-meta/projects/
        - apex-meta/state/
        - artifacts/
    personal_orchestration_memory:
      role: weekly/daily routines, flow history, model routing, capacity, cross-project priorities
      candidate_paths:
        - apex-meta/orchestration/
        - apex-meta/personal-os/
      rule: separate_domain_not_collapsed_into_project_kb

  retrieval_surface:
    primary: compiled_wiki_pages
    fallback: raw_sources_only_for_conflict_or_source_verification

  SQLite:
    db_path: apex-meta/registry/search.sqlite
    db_is_derived_artifact: true
    commit_db_to_git: false
    gitignore_before_first_build: true
    rebuild_strategy_v1: full_drop_create_insert
    fts5_preflight_required: true
    tokenizer_default: unicode61_remove_diacritics_2_but_fixture_test_required
    bm25_weights:
      title: 5
      tags: 3
      summary: 2
      body: 1
    schema_weight_rule: >
      Weight vector must match FTS5 table column order exactly.
      Add tests that fail if order changes.

  parser_policy:
    no_false_stdlib_only_constraint: true
    preferred: robust_frontmatter_parser_if_dependency_policy_allows
    fallback: strict_manual_frontmatter_subset
    forbidden: broad_regex_that_claims_to_parse_all_yaml

  output_policy:
    no_overengineering: true
    v1_goal: answer_what_should_claude_read_now
    v1_must_include:
      - skill package entrypoint
      - script contracts
      - minimal Python scripts or script specs
      - validation fixtures
      - tiny CLAUDE.md routing block
      - gitignore rule
      - registry docs
    v1_must_not_include:
      - vector search implementation
      - hosted services
      - Docker
      - heavy component registry
      - new profile systems
      - autonomous execution loop
````

---

## 2. Required source files to inspect

Read project resources and repo files before producing outputs.

### 2.1 Uploaded / project-resource sources

Find and read these exact or nearest-matching files:

```txt
Apex KB+SQLite FTS5BM25 Implementation Plan.md
Claude_Apex KB_SQLiteFTS5BM25_CCv2.md
Claude_Apex KB_SQLiteFTS5BM25_CCv3.md
Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md
Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md
Claude_Apex KB_SQLiteFTS5BM25_CC.md
Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md
Apex Knowledge Base Architecture.txt
Apex-KB Skill Analysis.txt
Apex Hermes Claude Build Pack.md
Apex_Alfred_Skill_Definition_Guide.md
PreCap Week v0.2.md
WeeklyRoutine_Overview_Marco&Meso.md
current-project-status-overview-template.md
project-status-overview-contract_v2_fixed.md
project-status-overview_SKILL_v3.md
ranking-and-validation-rules.md
ProThinkingGPT_Harmonization_v1.md
APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md
Phase 7 Package Readiness.txt
```

### 2.2 Repo truth pass

Inspect the connected repo:

```txt
repo: leela-spec/apexai-os-meta
branch: main
```

Required repo searches:

```txt
apex-kb
apex-query
apex-search
search.sqlite
FTS5
BM25
source-manifest
wiki-page
compiled wiki
source custody
script-command-contract
apex-meta/registry
.claude/skills
.claude/Claude.md
CLAUDE.md
```

Required repo truth outputs:

```yaml
repo_truth_required:
  repository_found: true_or_false
  code_search_index_available: true_or_false
  current_apex_kb_files:
    - path
    - role
    - status
  current_retrieval_files:
    - path
    - exists_or_missing
  current_registry_files:
    - path
    - exists_or_missing
  current_scripts:
    - path
    - role
    - status
  current_claude_control_plane:
    - .claude/Claude.md_or_CLAUDE.md
    - relevant routing blocks
  conflict_or_drift:
    - path
    - description
    - severity
```

Do not assume files exist. Verify.

---

## 3. External verification rules

Use web research only for current or official technical facts that matter to implementation correctness.

Required official sources:

```txt
SQLite FTS5 official documentation
Python sqlite3 official documentation
Claude Code / Agent Skills official documentation
```

Optional blueprint sources:

```txt
nvk/llm-wiki
llm-wiki-compiler
Kenso
OntoShip / gitmark
Backlog.md
CCPM
Task Master AI
planning-with-files
```

Do not treat AI blogspam as evidence. Prefer official docs, real repos, and implementation files.

---

## 4. Required analysis phases

### Phase 1 — Architecture reconciliation

Produce a concise reconciliation of:

1. `apex-kb`
    
2. `apex-query`
    
3. project/repo memory
    
4. personal orchestration memory
    
5. Apex planning loop inputs and outputs
    
6. `CLAUDE.md` / `.claude/skills` / path rules
    

Output:

```yaml
architecture_reconciliation:
  final_layer_model:
  file_ownership_map:
  skill_ownership_map:
  path_ownership_map:
  unresolved_conflicts:
```

### Phase 2 — Repo truth and drift audit

Compare the intended architecture against actual repo state.

Classify each target as:

```txt
EXISTS_KEEP
EXISTS_PATCH
EXISTS_REPLACE
MISSING_CREATE
MISSING_DEFER
CONFLICT_REVIEW
```

### Phase 3 — Technical risk validation

Validate at minimum:

1. FTS5 availability preflight requirement
    
2. BM25 vector and schema column order
    
3. snippet column index
    
4. tokenizer behavior for slugs, camelCase, snake_case, hyphens, IDs
    
5. frontmatter parser policy
    
6. mtime vs hash staleness
    
7. `.gitignore` order
    
8. malformed query handling
    
9. deterministic tie-break ordering
    
10. index exclusion policy
    

Output a risk table:

```yaml
risk:
  id:
  description:
  severity:
  source_evidence:
  required_fix:
  target_file:
```

### Phase 4 — Minimal v1 file tree

Propose the smallest final v1 tree.

At minimum consider:

```txt
.claude/skills/apex-kb/SKILL.md
.claude/skills/apex-kb/package-manifest.md
.claude/skills/apex-kb/references/kb-contract.md
.claude/skills/apex-kb/references/script-command-contract.md
.claude/skills/apex-query/SKILL.md
.claude/skills/apex-query/package-manifest.md
.claude/skills/apex-query/references/query-contract.md
.claude/skills/apex-query/references/sqlite-fts5-bm25-contract.md
.claude/skills/apex-query/references/validation-fixtures.md
scripts/apex-index.py
scripts/apex-query.py
apex-meta/registry/index.md
.gitignore
.claude/Claude.md or CLAUDE.md routing block
.claude/rules/apex-meta.md if applicable
```

If a file already exists, decide whether to patch, replace, or leave it.

### Phase 5 — File content generation

Generate complete final file contents for every `MISSING_CREATE`, `EXISTS_PATCH`, or `EXISTS_REPLACE` file.

Rules:

```yaml
file_generation_rules:
  full_file_contents_only: true
  no_unified_diff_hunks: true
  each_file_has:
    - target_path
    - action
    - reason
    - complete_content
    - validation_notes
  preserve_existing_content_policy:
    if_existing_file:
      - summarize what must be preserved
      - mark where integration additions go
      - if exact preservation cannot be guaranteed, output REVIEW_REQUIRED
```

For Python scripts:

```yaml
python_script_rules:
  may_generate_code: true
  stdlib_only_not_required_unless_repo_policy_says_so: true
  if_external_dependency_used:
    - justify it
    - provide stdlib fallback
  required_behaviors:
    - explicit utf-8 reads
    - FTS5 preflight
    - full rebuild
    - skip/exclude navigation index files
    - malformed frontmatter handling
    - stale check
    - deterministic ordering
    - safe error messages for malformed MATCH queries
    - no DB commit assumption
```

### Phase 6 — Validation plan

Create validation commands for Windows PowerShell and POSIX shell.

Required tests:

```txt
FTS5 preflight
fixture index build
fixture query exact title match
fixture query tag match
fixture query body match
fixture malformed query
fixture stale detection
gitignore check for search.sqlite
no wiki/index.md in results
BM25 schema/vector alignment
UTF-8 read check
```

### Phase 7 — Final integration verdict

Output:

```yaml
final_verdict:
  ready_to_apply_files: true_or_false
  must_review_before_apply:
    - item
  highest_risk:
  first_safe_application_order:
    - file
  rollback_plan:
  next_operator_action:
```

---

## 5. Non-negotiable constraints

1. Do not over-engineer.
    
2. Do not add vector search in v1.
    
3. Do not add Docker, hosted services, SaaS, or MCP as canonical memory.
    
4. Do not collapse personal orchestration into project KB.
    
5. Do not put long retrieval instructions into `CLAUDE.md`.
    
6. Do not pretend a broad regex parses all YAML.
    
7. Do not assume Python sqlite3 has FTS5; test it.
    
8. Do not commit `search.sqlite`.
    
9. Do not generate fake patch hunks if the write mechanism uses full-file replacement.
    
10. Do not invent repo state. Verify.
    
11. Do not use “research says” without pointing to a file or source.
    
12. Do not produce only a report. Produce final file contents where safe.
    

---

## 6. Required final output format

Use this exact structure:

# 0. Executive Decision

- Overall verdict
    
- Apply now / apply with review / stop
    
- Top 5 changes
    
- Top 5 do-not-change decisions
    

# 1. Repo Truth Pass

Table with discovered files, missing files, and drift.

# 2. Final Architecture

Short layer model plus ownership map.

# 3. Decision Lock Confirmation

List all binding decisions and whether confirmed, changed, or review-needed.

# 4. Technical Risk Register

Risk table with fixes and target files.

# 5. Final File Tree

Tree with action labels.

# 6. Complete File Contents

For each file:

## FILE: path/to/file

ACTION: CREATE | REPLACE | PATCH-BY-FULL-FILE | REVIEW_REQUIRED

REASON:  
...

```filetype
complete content here
```

# 7. Validation Commands

PowerShell and POSIX commands.

# 8. Application Order + Rollback

Exact order and rollback plan.

# 9. Open Questions

Only questions that block safe file generation. Do not ask questions that can be answered from repo or project resources.

Begin now.

```

---

# D. One Important Adjustment Before Running It

I would **not** make the Deep Research run decide everything from scratch. Use this framing:

> “Validate these locked decisions, override only if repo truth or official technical docs prove a conflict, then generate final full-file contents.”

That is the right balance: it prevents blind execution, but also avoids the repeated failure pattern of reopening the whole Apex architecture every time.
```