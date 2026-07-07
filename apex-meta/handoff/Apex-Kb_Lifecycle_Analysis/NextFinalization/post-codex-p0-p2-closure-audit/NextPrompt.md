You are GPT-5.5 Agent Mode acting as the Apex KB v3 P0-P2 Closure Repair Patch-Pack Builder.

Repository:
leela-spec/apexai-os-meta

Branch:
main

Local repo:
C:\GitDev\apexai-os-meta

Mission:
Create a validated Git-native repair patch pack only.

Do not directly apply final implementation changes.
Do not leave target files modified.
Do not manually implement equivalent changes and call that success.
Do not use old failed patch files as source.
Do not create abbreviated hunk patches.
Do not touch apex-kb2.
Do not touch unrelated untracked files.

Patch-pack root:
apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/

Read first:
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/post-codex-p0-p2-closure-audit/connector-detective-audit-and-repair-plan.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/post-codex-p0-p2-closure-audit/local-behavioral-check-report.md

Live target files to read before editing:
apex-meta/scripts/apex_kb.py
apex-meta/scripts/apex_kb_retrieval.py
.claude/skills/apex-kb/references/script-command-contract.md

Allowed target files:
apex-meta/scripts/apex_kb.py
apex-meta/scripts/apex_kb_retrieval.py
.claude/skills/apex-kb/references/script-command-contract.md
.claude/skills/apex-kb/references/acceptance-tests.md
.claude/skills/apex-kb/examples/powershell-commands.md

Preserve current working behavior:
- CLI global flag normalization.
- --output-json support.
- status freshness split:
  - wiki_index_status
  - retrieval_index_status
  - source_payload_manifest_status

Repair required behavior:
1. pointer_only Phase 0:
   - Resolve safe kb-local and repo-local pointer_only text files.
   - Include resolved pointer-only files in Phase 0 scanning OR explicitly report unresolved pointers.
   - Populate pointer_only_scanned_count, pointer_only_warning_count, pointer_only_unresolved truthfully.

2. quality / coverage:
   - Populate source_to_page_map and page_to_source_map from wiki page frontmatter source_refs.
   - Include manifest sources even if no pages reference them.
   - Detect shell_page_candidates using missing Phase 2 value-contract headings, low body density, and empty source_refs.
   - Detect phase2_repair_candidates for pages missing Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, or Uncertainty / Raw Source Reopen Triggers.

3. query-eval:
   - --init must create a deterministic starter pack at outputs/queries/evals/query-eval-pack.json when --allow-write is present.
   - Without --allow-write it must report the planned write.
   - Existing packs must be read and validated.
   - Validate entries for expected_routes, expected_minimal_pages, and raw_source_needed fields.
   - Return issue_count and status.

4. graph / process-graph:
   - Extract deterministic markdown links, wikilinks, repo/path references, YAML/path references, and simple process-sequence edges from KB text files.
   - Return non-empty edge structures when source files contain such references.
   - If --allow-write is present, write graph artifacts under manifests/phase0/.

5. script-command-contract:
   - Update only after code behavior matches.
   - Remove or soften any claims that remain unsupported.

Patch files:
001-apex-kb-pointer-only-phase0-real-scan.patch
002-apex-kb-quality-coverage-real-maps.patch
003-apex-kb-query-eval-pack.patch
004-apex-kb-graph-process-flow-extraction.patch
005-script-command-contract-align-behavior.patch
006-acceptance-tests-p0-p2-closure-repair.patch
007-powershell-commands-p0-p2-closure-repair.patch

Patch method:
For each patch:
1. Start from clean main.
2. Modify only the intended target file.
3. Generate the patch with:
   git diff --no-ext-diff -- <target-file> > <patch-file>
4. Verify patch is non-empty.
5. Verify it has a real diff --git header and normal hunk headers.
6. Revert target file.
7. Run:
   git apply --check <patch-file>
8. Temporarily apply the patch.
9. Verify changed-file scope is exactly the intended file.
10. Run relevant sanity checks.
11. Revert target file.

Cumulative validation:
- git apply --check all patches in order.
- git apply all patches in order.
- Verify changed files are only allowed target files.
- Run:
  python -m py_compile apex-meta/scripts/apex_kb.py
  python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
- Run behavioral smoke checks on a safe KB root.
- Revert target files.
- Verify final builder state has target files clean and patch artifacts only.

Metadata required:
apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/000-patch-manifest.md
apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/999-codex-apply-handoff.md
apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/validation-report.md

Final repo state:
Only patch-pack artifacts should be committed and pushed.
Runtime target files must be clean and unmodified.

Final report:
FINAL_REPORT:
  verdict: PASS|FAIL
  patch_pack_root: "apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/"
  patches_created:
    - ...
  git_apply_check_each: PASS|FAIL
  git_apply_check_cumulative: PASS|FAIL
  py_compile: PASS|FAIL
  behavior_smoke: PASS|FAIL
  target_files_clean_final: true|false
  patch_artifacts_committed: true|false
  commit_sha: "<sha or null>"
  blockers: []