# ProjectRepos Corpus Scan Failure Review

## 1. Executive Verdict

**Verdict:** the previous ProjectRepos scan likely failed because it used the wrong execution shape: a broad custom full-corpus scanner over downloaded repositories, before proving cheap inventory speed and before deciding whether this belongs inside `apex_kb.py phase0`.

**Best next architecture:** use a **two-pass preselection design**, with Apex KB remaining canonical.

```yaml
best_practice_verdict:
  recommended_architecture: "Apex KB phase0 remains canonical; add a small ProjectRepos preselector only if external repo selection does not fit cleanly into phase0."
  preferred_shape:
    pass_1: "cheap repo/file inventory only: repo, path, extension, size, likely role, skip/noise flags"
    pass_2: "parse only high-signal text files: README, SKILL.md, docs, examples, package manifests, workflows"
    pass_3: "hash only selected candidate files before source intake"
  what_to_avoid:
    - "full recursive read/hash over all downloaded repos"
    - "semantic ingest or wiki generation"
    - "large JSON dumps before filtering"
    - "one huge uncheckpointed scan"
    - "parallel lifecycle outside Apex KB"
  custom_projectrepos_script: "replace or shrink; do not keep as a full scanner"
```

The existing Apex KB contract already defines the correct lifecycle boundary: Phase 0 is deterministic corpus intelligence; Phase 1/2 are LLM semantic stages; retrieval/indexes are derived and rebuildable. The current skill contract also says one KB root is required and that it must not mutate planning/session/sync/orchestration state.

The uploaded Phase 0 decision already says Phase 0 must produce navigation artifacts, not wiki pages, semantic ingest analyses, embeddings, or vector stores, and that existing `source-inventory.csv/json` should be reused instead of recreated blindly.

---

## 2. Actual Repo State

I cannot verify the live Windows repo state from here. The path:

```text
C:\GitDev\apexai-os-meta
```

is not mounted in this runtime. The mounted project resources contain design reports, contracts, handovers, and generated artifacts, but not the actual local repo tree with `apex-meta/scripts/projectrepos_corpus_intelligence.py`.

```yaml
repo_state_check:
  custom_scanner_exists: "unknown_here; must run Test-Path locally"
  partial_outputs_exist: "unknown_here; must inspect apex-meta/kb/claude-skill-design/manifests/projectrepos-corpus-intelligence locally"
  dirty_files: "unknown_here; must run git status --short locally"
  untracked_files: "unknown_here"
  likely_timeout_cause:
    - "recursive scan across all files under source-knowledge/ProjectRepos"
    - "too much early file reading and/or hashing"
    - "no cheap first-pass inventory"
    - "no max-files / max-bytes / checkpoint / resume"
    - "possibly scanning generated folders such as node_modules, .git, dist, build, package caches, lock-heavy trees"
```

**Lika KB learning reference:** available project artifacts show the Lika run was useful as a routing/navigation proof, but not a complete repo-written lifecycle proof. The Phase 2 output explicitly says it was **chat-output only** and did not write repo files. The concept compile report says the KB value is strongest at routing/indexing, but also notes grouped analysis and noisy/table-heavy source limitations. The saved status handover says a full end-to-end LLM lifecycle test had **not** yet been completed.

---

## 3. Apex KB Script Capability Review

From the available contracts, Apex KB clearly supports the **conceptual** phase split:

```yaml
apex_kb_phase0_fit:
  can_scan_kb_local_sources: "yes, by design"
  can_scan_external_source_root_directly: "unknown; must verify apex_kb.py implementation"
  supports_skip_patterns: "unknown; likely patch needed if not already present"
  supports_max_files_or_incremental: "unknown; likely patch needed"
  supports_repo_summary: "not proven"
  supports_skill_frontmatter_summary: "not proven"
  recommended_patch_needed: true
```

The operation rules define Python ownership over source hashing, scaffold, manifest/frontmatter validation, dead wikilink/orphan/stale checks, machine index generation, and audit listing, while the LLM owns relevance judgment, concept/entity extraction, contradiction interpretation, Phase 1 analysis, wiki drafting, and query synthesis.

**Minimal patch to `apex_kb.py phase0`:**

```yaml
minimal_patch:
  add_options:
    - "--source-root optional external root"
    - "--include-ext .md,.mdx,.txt,.json,.yaml,.yml,.py"
    - "--exclude-dir .git,node_modules,dist,build,.venv,__pycache__,vendor,target,.next,out,coverage"
    - "--max-files"
    - "--max-bytes-per-file"
    - "--mode inventory|structure|full"
    - "--checkpoint-every"
    - "--resume"
  add_outputs:
    - "repo-inventory.json"
    - "candidate-files.md"
    - "scan-summary.json"
  do_not_add:
    - "semantic scoring"
    - "wiki page writes"
    - "bulk source-manifest import"
```

---

## 4. Runtime Failure Diagnosis

The timeout diagnosis is straightforward:

```yaml
runtime_failure_diagnosis:
  root_error: "wrong scan granularity"
  direct_failure: "one broad full-corpus command over ProjectRepos timed out"
  design_failure:
    - "custom scanner was created before checking whether Apex KB phase0 could be extended"
    - "external downloaded repos were treated like already curated KB sources"
    - "full scan happened before cheap filtering"
    - "hash/read_text/json dump likely happened too early"
    - "no checkpoint/resume behavior"
    - "no bounded first-pass inventory"
```

This likely would **not** have failed under a disciplined Apex KB Phase 0 process if Phase 0 had been run only over already-curated `sources/` or over a bounded preselection layer. It failed because ProjectRepos is not the same kind of corpus as `claude-skill-design/sources/`.

---

## 5. Best-Practice Research Summary

For large local repo corpora, current best practice is:

1. **Use tool-native ignore behavior first.** `ripgrep` automatically skips `.gitignore`/`.ignore`/`.rgignore` matches, hidden files/directories, binary files, and symlinks by default; it also supports manual glob and file-type filtering. ([GitHub](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md "ripgrep/GUIDE.md at master · BurntSushi/ripgrep · GitHub"))
    
2. **Use fast file discovery for pass 1.** `fd` recursively lists files, respects `.gitignore` by default, supports extension filters, excludes, hidden/no-ignore toggles, and batched execution. ([GitHub](https://github.com/sharkdp/fd "GitHub - sharkdp/fd: A simple, fast and user-friendly alternative to 'find' · GitHub"))
    
3. **If using Python stdlib, prune during traversal.** `os.walk(topdown=True)` lets the caller mutate `dirnames` in place so unwanted directories are never recursed into; that is the key pattern for skipping `.git`, `node_modules`, `dist`, etc. ([Python documentation](https://docs.python.org/3/library/os.html "os — Miscellaneous operating system interfaces — Python 3.14.6 documentation"))
    
4. **Treat frontmatter extraction as metadata parsing, not semantic interpretation.** Python-Markdown’s metadata extension exposes document metadata as a dict and supports YAML-style delimiters, but it explicitly does not parse the metadata as YAML. ([Python-Markdown](https://python-markdown.github.io/extensions/meta_data/ "Meta-Data — Python-Markdown 3.10.2 documentation"))
    
5. **Use robust frontmatter/YAML only when needed.** For V1, delimiter-based detection is enough for routing; for V1.5, `python-frontmatter` or PyYAML can improve correctness if dependency policy allows it. ([Python Frontmatter](https://python-frontmatter.readthedocs.io/en/latest/ "Python Frontmatter — Python Frontmatter 1.0.0 documentation"))
    

**Pattern comparison:**

|Pattern|Fit|Verdict|
|---|--:|---|
|Existing `apex_kb.py phase0`|High|Best canonical home if patched minimally|
|`ripgrep` / `fd` preselection|High|Best external repo preselector primitive|
|Python `os.walk` scanner|Medium-high|Acceptable if topdown pruning + byte/file limits are enforced|
|Markdown AST parser|Medium|V1.5 only unless parser warnings justify it|
|SQLite FTS/Lunr index|Medium|Derived retrieval layer, not source-selection authority|
|One-shot custom scanner|Low|Delete or replace unless reduced to bounded preselector|

---

## 6. Guardrail Audit

|Instruction|Keep / Remove / Compress|Reason|
|---|---|---|
|Do not run semantic ingest|Keep|Prevents Phase 0/Phase 1 collapse|
|Do not generate wiki pages|Keep|Directly prevents the previous lifecycle confusion|
|Do not mutate `.claude/skills/apex-kb`|Keep|Protects canonical skill package|
|Do not bulk-copy ProjectRepos|Keep|Core source-selection boundary|
|Keep outputs under staging/candidate path|Keep|Prevents source-manifest contamination|
|Report dirty files before writes|Keep|Necessary repo safety|
|Repeating no-wiki/no-phase2 many times|Compress|One hard gate is enough|
|Huge final report key schema before design validation|Remove|Wastes tokens and pushes premature implementation|
|Many output files in first attempt|Remove|Causes timeout and false completeness|
|Full hashing all files before proving speed|Remove|Wrong order; hash only candidates|
|One huge full scan|Remove|Direct failure mode|
|Build custom script before checking `apex_kb.py`|Remove|Architectural drift|

```yaml
instruction_design:
  must_have:
    - "repo status first"
    - "no semantic ingest"
    - "no wiki generation"
    - "no bulk repo copy"
    - "bounded pass 1"
    - "checkpoint/resume or max-files/max-bytes"
    - "report dirty/untracked files"
  nice_to_have:
    - "candidate score explanation"
    - "repo family grouping"
    - "frontmatter summary"
    - "SKILL.md/README/docs priority"
  harmful_overhead:
    - "full final report schema before validating scanner design"
    - "demanding many artifacts before pass 1"
    - "requiring full hashes before selection"
    - "repeating the same prohibition in multiple sections"
```

---

## 7. Recommended Next Implementation

**Decision:** do **not** run another giant scanner. Patch or add a bounded preselector.

```yaml
recommended_next_implementation:
  script_strategy:
    primary: "Patch apex_kb.py phase0 if it already has a clean source iterator and manifest output surface."
    fallback: "Create projectrepos_preselector.py as a tiny auxiliary tool, not a parallel KB lifecycle."
  command_strategy:
    pass_1:
      command: "python apex-meta/scripts/projectrepos_preselector.py --source-root source-knowledge/ProjectRepos --output-root apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates --mode inventory --max-files 20000 --max-bytes-per-file 0 --json"
      behavior: "path/size/ext/repo inventory only; no content reads"
    pass_2:
      command: "python apex-meta/scripts/projectrepos_preselector.py --source-root source-knowledge/ProjectRepos --output-root apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates --mode candidates --include-ext .md,.mdx,.txt,.json,.yaml,.yml,.py --max-bytes-per-file 262144 --json"
      behavior: "read only high-signal candidates"
  outputs_to_create:
    - "repo-inventory.json"
    - "candidate-files.md"
    - "candidate-files.json"
    - "scan-run-summary.json"
  outputs_to_avoid:
    - "full heading map for all repo files"
    - "full hash manifest for all repo files"
    - "source-manifest.json changes"
    - "wiki pages"
    - "ingest-analysis"
```

**Whether current failed script should survive:** only if it can be reduced to the auxiliary preselector above. Otherwise delete it and reimplement the small version.

---

## 8. Revised Codex Prompt

```text
# Codex Task — Bounded ProjectRepos Preselection for Claude Skill Design KB

## Mission

Diagnose and repair the failed ProjectRepos corpus scan.

Do not run Phase 1.
Do not generate wiki pages.
Do not bulk-copy ProjectRepos.
Do not update source-manifest.json.
Do not mutate .claude/skills/apex-kb.

The goal is only to produce a bounded candidate-selection report for files under:

source-knowledge/ProjectRepos/

that may later be curated into:

apex-meta/kb/claude-skill-design/

## Start

cd C:\GitDev\apexai-os-meta

Run and report:

git status --short
Test-Path apex-meta/scripts/projectrepos_corpus_intelligence.py
Test-Path apex-meta/kb/claude-skill-design/manifests/projectrepos-corpus-intelligence

If the output folder exists, list its contents recursively with size and timestamp.

Inspect the failed script if present:
Get-Content apex-meta/scripts/projectrepos_corpus_intelligence.py -TotalCount 160
Select-String -Path apex-meta/scripts/projectrepos_corpus_intelligence.py -Pattern "rglob|os.walk|hash|read_text|open|json.dump" -Context 2,2

Also inspect current phase0 implementation:
Select-String -Path apex-meta/scripts/apex_kb.py -Pattern "def cmd_phase0|def iter_source_files|def parse_markdown_structure|keyword_groups|PHASE0_DIR" -Context 3,8

## Required decision before patching

Report:

- whether the failed script should be deleted, patched, or replaced
- whether apex_kb.py phase0 already supports this with a minimal patch
- exact timeout cause from code inspection
- whether partial outputs can be safely deleted or should be preserved as failed-run evidence

Do not implement until this report is printed.

## If implementation is justified

Implement only one of these:

Option A:
Patch apex_kb.py phase0 minimally to support external --source-root, --exclude-dir, --include-ext, --max-files, --max-bytes-per-file, --mode inventory|structure|full, --checkpoint-every, --resume.

Option B:
Replace projectrepos_corpus_intelligence.py with a small projectrepos_preselector.py that does only two-pass preselection:
1. inventory: repo/path/ext/size/noise flags only, no file content reads
2. candidates: read only high-signal text files under byte limit

Default excludes:
.git
node_modules
dist
build
out
.next
coverage
.venv
__pycache__
target
vendor
site-packages

Candidate priority:
- SKILL.md
- README.md
- docs/**/*.md
- examples/**/*.md
- package manifests
- workflow/process docs
- files mentioning skill, agent, workflow, Claude, MCP, prompt, memory, eval

Outputs only:
apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates/repo-inventory.json
apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates/candidate-files.json
apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates/candidate-files.md
apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates/scan-run-summary.json

No source-manifest writes.
No wiki writes.
No ingest-analysis writes.

## Validation

Run:

python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/projectrepos_preselector.py

Then run a bounded smoke test:

python apex-meta/scripts/projectrepos_preselector.py --source-root source-knowledge/ProjectRepos --output-root apex-meta/kb/claude-skill-design/manifests/projectrepos-candidates --mode inventory --max-files 5000 --json

Report:
- runtime
- files seen
- files skipped by directory
- candidate count
- largest skipped files
- outputs created
- git status --short

Stop after reporting. Do not continue into source intake.
```

**Bottom line:** the hypothesis is mostly correct. The failed run should be treated as a design failure, not merely a timeout. The replacement should be a bounded two-pass preselector or a minimal extension of `apex_kb.py phase0`, with Apex KB remaining the canonical lifecycle.