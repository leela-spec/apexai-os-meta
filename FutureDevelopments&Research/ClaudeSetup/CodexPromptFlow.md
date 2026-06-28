```
# Codex Task — Apex KB2 Installation and Testing Run## 0. MissionYou are working in the repository:```textleela-spec/apexai-os-meta
```

Your task is to run a **repo-local installation, consistency, and smoke-test validation pass** for the Apex KB2 package.

This is not an architecture rediscovery run.  
This is not a file-generation run.  
This is not a broad cleanup run.  
This is a mechanical repo validation run with minimal targeted repairs only if tests prove a defect.

The active package is:

```
.claude/skills/apex-kb2/
```

The repo also contains the older package:

```
.claude/skills/apex-kb/
```

Do not delete, overwrite, rename, or merge the older `apex-kb` package unless explicitly instructed.

The current working branch to validate is expected to be:

```
apex-kb2-finalize-agent
```

If this branch exists, start from it.  
If it does not exist, report that clearly and stop before modifying files.

---

## 1. Source-grounding requirement

Before editing or testing, inspect the live repo files. Do not rely on memory.

Read at minimum:

```
.claude/skills/apex-kb2/SKILL.md.claude/skills/apex-kb2/package-manifest.md.claude/skills/apex-kb2/references/kb-contract.md.claude/skills/apex-kb2/references/script-command-contract.md.claude/skills/apex-kb2/references/retrieval-contract.md.claude/skills/apex-kb2/references/lifecycle-state-machine.md.claude/skills/apex-kb2/references/acceptance-tests.md.claude/skills/apex-kb2/examples/powershell-commands.mdapex-meta/scripts/apex_kb.pyapex-meta/scripts/apex_kb_retrieval.py
```

If project-resource handovers are mounted, also read the latest saved handover/audit before proceeding. If they are not mounted, state that and continue from repo files only.

Known recent intended changes:

```
.claude/skills/apex-kb2/SKILL.md.claude/skills/apex-kb2/package-manifest.md.claude/skills/apex-kb2/references/kb-contract.md
```

These changes should only correct KB2 package identity and contract references. They must not change lifecycle behavior, retrieval behavior, or runtime KB layout.

---

## 2. Hard boundaries

Preserve these invariants:

```
hard_boundaries:  runtime_kb_root: apex-meta/kb/<kb-slug>/  no_hardcoded_test_kb: claude-skill-design  scripts:    no_network: true    no_shell_out: true    dry_run_default: true    writes_require: --allow-write    writes_outside_kb_root: forbidden  phase0:    deterministic_only: true    forbidden:      - semantic ingest      - wiki page generation      - embeddings      - vector stores      - LLM semantic claims  phase1:    creates_analysis_shell_or_analysis_only: true    must_halt_before_wiki_generation: true  phase2:    required_phrase: approve ingest  retrieval:    index_is_derived: true    index_is_rebuildable: true    canonical_source_of_truth: false  forbidden_mutation_targets:    - Apex Plan    - Apex Sync    - Apex Session    - PreCap    - FlowRecap    - APSU/status-merge    - personal orchestration state
```

Do not add broad architecture changes.  
Do not create a zip.  
Do not merge.  
Do not open a PR unless explicitly instructed.

---

## 3. Branch and preflight

Run:

```
git status --shortgit branch --show-currentgit fetch origin
```

Then locate the target branch:

```
git branch --all | grep "apex-kb2-finalize-agent" || true
```

If branch exists remotely or locally:

```
git checkout apex-kb2-finalize-agent || git checkout -b apex-kb2-finalize-agent origin/apex-kb2-finalize-agentgit pull --ff-only || true
```

Create a test branch from it:

```
git checkout -b codex/apex-kb2-install-test
```

If the checkout is dirty before your work, stop and report:

```
PRECHECK_FAILED:  reason: dirty_working_tree_before_codex_changes  dirty_files:    - <files>
```

Do not proceed until the dirty tree is resolved.

---

## 4. Static inventory check

Run:

```
required_files=(  ".claude/skills/apex-kb2/SKILL.md"  ".claude/skills/apex-kb2/package-manifest.md"  ".claude/skills/apex-kb2/references/kb-contract.md"  ".claude/skills/apex-kb2/references/script-command-contract.md"  ".claude/skills/apex-kb2/references/ingest-query-lint-audit-rules.md"  ".claude/skills/apex-kb2/references/retrieval-contract.md"  ".claude/skills/apex-kb2/references/lifecycle-state-machine.md"  ".claude/skills/apex-kb2/references/acceptance-tests.md"  ".claude/skills/apex-kb2/templates/ingest-analysis-template.md"  ".claude/skills/apex-kb2/templates/wiki-page-templates.md"  ".claude/skills/apex-kb2/templates/query-output-template.md"  ".claude/skills/apex-kb2/templates/kb-schema-template.md"  ".claude/skills/apex-kb2/templates/source-manifest-template.json"  ".claude/skills/apex-kb2/examples/powershell-commands.md"  ".claude/skills/apex-kb2/examples/lifecycle-runbook.md"  "apex-meta/scripts/apex_kb.py"  "apex-meta/scripts/apex_kb_retrieval.py")missing=()for f in "${required_files[@]}"; do  if [ ! -f "$f" ]; then    missing+=("$f")  fidoneprintf '%s\n' "${missing[@]}"
```

Expected result:

```
<no output>
```

If files are missing, do not invent replacements immediately. First report:

```
MISSING_FILE_AUDIT:  missing_files:    - <path>  likely_impact:  proposed_minimal_repair:
```

Only repair missing files if the expected content is clearly present elsewhere in the repo or project resources.

---

## 5. Identity and collision audit

Run:

```
grep -RIn --include='*.md' \  -e '^name: apex-kb$' \  -e 'package_name: apex-kb$' \  -e 'package_path: .claude/skills/apex-kb/$' \  .claude/skills/apex-kb2 || true
```

Expected result:

```
<no output>
```

Then run:

```
grep -RIn --include='*.md' ".claude/skills/apex-kb/" .claude/skills/apex-kb2 || true
```

Expected result:

```
<no output>
```

Important:

- It is acceptable for `.claude/skills/apex-kb/` itself to still refer to `apex-kb`.
- It is acceptable for backups, verification folders, and historical source snapshots to contain old references.
- It is **not** acceptable for `.claude/skills/apex-kb2/` to identify itself as `apex-kb`.

If drift is found inside `apex-kb2`, repair only the package identity references. Do not change lifecycle logic unless a test failure requires it.

---

## 6. Command contract audit

Extract implemented commands from help output.

Run:

```
python --versionpython apex-meta/scripts/apex_kb.py --helppython apex-meta/scripts/apex_kb_retrieval.py --help
```

Verify that `apex_kb.py` exposes:

```
scaffoldsource-intakehashpreflightphase0ingest-phase1ingest-phase2indexquerylintauditstatushealth
```

Verify that `apex_kb_retrieval.py` exposes:

```
healthbuild-indexstalequeryexportclear-index
```

If a command is documented but missing, stop and report. Do not silently rewrite the parser.

---

## 7. Python and JSON static validation

Run:

```
python -m py_compile apex-meta/scripts/apex_kb.pypython -m py_compile apex-meta/scripts/apex_kb_retrieval.pypython - <<'PY'import jsonfrom pathlib import Pathpath = Path(".claude/skills/apex-kb2/templates/source-manifest-template.json")json.loads(path.read_text(encoding="utf-8"))print("json ok")PY
```

Expected:

```
json ok
```

If compile fails, repair only syntax/runtime compatibility issues. Do not redesign.

---

## 8. Clean lifecycle smoke test

Use a temporary KB root and temporary source.

```
KB="apex-meta/kb/apex-kb2-smoke"TMP="tmp/apex-kb2-smoke"rm -rf "$KB" "$TMP"mkdir -p "$TMP"cat > "$TMP/smoke-source.md" <<'EOF'# Smoke SourceThis source mentions Apex KB2, source manifest, Phase 1, approve ingest, SQLite FTS5, and BM25.EOF
```

### 8.1 Scaffold

```
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json scaffoldtest ! -e "$KB" || echo "ERROR: dry-run scaffold unexpectedly created KB root"python apex-meta/scripts/apex_kb.py --kb-root "$KB" --allow-write --json scaffold --title "Apex KB2 Smoke"test -f "$KB/README.md"test -f "$KB/kb-schema.md"test -f "$KB/wiki/index.md"test -f "$KB/manifests/source-manifest.json"
```

### 8.2 Source custody and Phase 0

```
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json hash --path "$TMP/smoke-source.md"python apex-meta/scripts/apex_kb.py \  --kb-root "$KB" \  --allow-write \  --json source-intake \  --source-path "$TMP/smoke-source.md" \  --source-type note \  --storage-mode copy_into_kb \  --source-id smoke-sourcepython apex-meta/scripts/apex_kb.py --kb-root "$KB" --json preflight --source-path "$TMP/smoke-source.md"python apex-meta/scripts/apex_kb.py --kb-root "$KB" --allow-write --json phase0
```

Verify Phase 0 artifacts:

```
phase0_files=(  "corpus-profile.md"  "heading-map.json"  "markdown-link-map.json"  "frontmatter-map.json"  "keyword-hits.ndjson"  "topic-file-map.json"  "source-priority-candidates.md"  "phase0-navigation-report.md")for f in "${phase0_files[@]}"; do  test -f "$KB/manifests/phase0/$f" || echo "MISSING_PHASE0: $f"done
```

Also verify Phase 0 did not create semantic wiki pages:

```
find "$KB/wiki/concepts" "$KB/wiki/entities" "$KB/wiki/summaries" -type f | sort
```

Expected result:

```
<no semantic pages from phase0>
```

### 8.3 Phase 1 and Phase 2 gate

```
python apex-meta/scripts/apex_kb.py \  --kb-root "$KB" \  --allow-write \  --json ingest-phase1 \  --source-path "$TMP/smoke-source.md" \  --source-slug smoke-sourcetest -f "$KB/ingest-analysis/smoke-source.analysis.md"
```

Wrong phrase must fail or report blocked:

```
set +epython apex-meta/scripts/apex_kb.py \  --kb-root "$KB" \  --json ingest-phase2 \  --analysis smoke-source.analysis.md \  --approval-phrase "not approved"wrong_phrase_exit=$?set -eecho "wrong_phrase_exit=$wrong_phrase_exit"
```

Correct phrase must validate the gate:

```
python apex-meta/scripts/apex_kb.py \  --kb-root "$KB" \  --json ingest-phase2 \  --analysis smoke-source.analysis.md \  --approval-phrase "approve ingest"
```

The script may validate the gate. It must not invent semantic wiki prose by itself.

### 8.4 Manual compiled page for retrieval

Create one minimal compiled page:

```
mkdir -p "$KB/wiki/concepts"cat > "$KB/wiki/concepts/retrieval.md" <<'EOF'---title: "Retrieval"page_type: conceptkb_slug: "apex-kb2-smoke"source_refs:  - source_id: "smoke-source"created_at: "2026-06-27T00:00:00Z"updated_at: "2026-06-27T00:00:00Z"confidence: "high"claim_label: "source_backed_summary"status: "active"---# RetrievalSQLite FTS5 and BM25 provide local lexical retrieval over compiled KB pages. Search indexes are derived artifacts.EOF
```

### 8.5 Index and retrieval

```
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --allow-write --json indexpython apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --json healthpython apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --allow-write --json build-indexpython apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --json stalepython apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --allow-write --json query --query "sqlite bm25" --limit 3 --save
```

Verify:

```
test -f "$KB/derived/search/search-index.json"test -f "$KB/derived/search/index-meta.json"find "$KB/outputs/queries" -type f | sort
```

Expected:

- query returns the `Retrieval` page
- saved query packet exists
- stale status is fresh after build-index

### 8.6 Maintenance

```
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json lint --strictpython apex-meta/scripts/apex_kb.py --kb-root "$KB" --json auditpython apex-meta/scripts/apex_kb.py --kb-root "$KB" --json statuspython apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --json stale
```

---

## 9. Outside-KB write protection test

Run one negative test to verify write safety.

```
set +epython apex-meta/scripts/apex_kb_retrieval.py \  --kb-root "$KB" \  --allow-write \  --json export \  --output "../outside-kb-export.json"outside_write_exit=$?set -eecho "outside_write_exit=$outside_write_exit"
```

Expected:

- command fails or refuses path outside KB root
- no file is written outside `$KB`

If the script allows the write, that is a FAIL and must be repaired before merge.

---

## 10. Cleanup

Only after recording test results:

```
rm -rf "$KB" "$TMP"
```

Confirm cleanup does not remove anything else:

```
git status --short
```

Generated smoke artifacts under `apex-meta/kb/apex-kb2-smoke` and `tmp/apex-kb2-smoke` must not remain in the final diff.

---

## 11. Commit rules

If and only if tests required small repairs:

```
git diff --statgit status --short
```

Commit only targeted fixes:

```
git add <changed-files>git commit -m "Validate Apex KB2 install and smoke tests"
```

Do not commit generated smoke KB files.  
Do not commit temporary outputs.  
Do not merge.  
Do not open a PR unless explicitly asked.

If no repairs are needed, do not create an empty commit.

---

## 12. Final report format

Return exactly this structure:

```
FINAL_REPORT:  verdict: PASS | FAIL | PARTIAL  branch:  base_branch:  started_from_branch:  dirty_tree_at_start:  dirty_tree_at_end:  files_created:  files_modified:  files_deleted:  package_inventory:    missing_files:    unexpected_files:  identity_collision_audit:    apex_kb2_old_identity_refs:    legacy_apex_kb_touched: yes | no  command_contract:    apex_kb_py_commands:    apex_kb_retrieval_py_commands:    missing_documented_commands:    undocumented_commands:  static_validation:    python_version:    py_compile_apex_kb_py:    py_compile_apex_kb_retrieval_py:    source_manifest_template_json:  smoke_tests:    scaffold:    source_intake:    preflight:    phase0_artifacts:    phase0_boundary:    ingest_phase1:    phase2_wrong_phrase:    phase2_approve_ingest:    index:    retrieval_health:    retrieval_build_index:    retrieval_query:    saved_query_packet:    lint:    audit:    status:    stale:  safety_tests:    outside_kb_write_protection:    no_plan_sync_session_mutation:    no_generated_smoke_artifacts_left_in_git:  git_diff_summary:  commits_created:  remaining_risks:  ready_for_pr: yes | no  ready_to_merge: yes | no
```

If any test fails, include:

```
FAILURE_DETAIL:  failed_command:  exit_code:  relevant_stdout:  relevant_stderr:  likely_file_responsible:  minimal_repair_recommendation:
```

Do not claim PASS unless every required check above passes.

```
---## Why this is the right Codex flowThe saved audit says the remaining work is not feature design but validation: run static inventory, identity checks, Python compile, JSON validation, clean lifecycle smoke tests, retrieval tests, and final PR handover. The earlier repo-agent recommendation also says the task should be converted from a chat-style “one file per prompt” flow into a repo-local agent task that inspects current repo state, detects collisions, repairs exact files, compiles Python, runs smoke tests, and produces an audit/diff summary. :contentReference[oaicite:2]{index=2}The target is stable: `.claude/skills/apex-kb2/`, generic `--kb-root apex-meta/kb/<kb-slug>/`, deterministic Phase 0 only, Phase 2 gated by `approve ingest`, derived retrieval indexes, and no mutation of Plan/Sync/Session/PreCap/FlowRecap/APSU. 
```