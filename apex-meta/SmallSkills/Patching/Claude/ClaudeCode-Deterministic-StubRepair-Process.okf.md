---
okf_schema: "apex.claude_code.deterministic_stub_repair_process.v1"
guide_id: "claude_code_deterministic_stub_repair"
status: "recommended"
supersedes_for_scope: "none — companion to AgentMode-GitNative-PatchPack-Process.okf.md, not a replacement"
created_for: "repairing stub/partial functions in a live repo with minimum LLM token spend"
companion_script: "apex-meta/SmallSkills/Patching/stub_repair_toolkit.py"
derived_from: "apex-meta/SmallSkills/Patching/FirstClaudePatchReport.okf.md"
purpose: >
  Force a hard split between the one step that genuinely requires an LLM
  (recognizing a stub and writing correct replacement code) and every other
  step (git plumbing, fixture construction, validation, scope checks, apply,
  commit, push), which must run as deterministic script calls, not
  LLM-orchestrated tool calls. The prior run spent ~90 tool calls; the
  mechanical phases (fixture build/check, per-file patch loop) accounted for
  most of them and are the direct target of this guide.

division_of_labor:
  llm_does:
    - "read the target file once to find candidate stub/partial functions"
    - "decide the correct replacement behavior and write it as real code"
    - "author ONE fixture spec (JSON) declaring: files to create, CLI commands to run, JSON-path assertions to check"
    - "author ONE commit message"
    - "read tool output and decide pass/fail/next-step"
  script_does:
    - "worktree create/remove"
    - "diff generation from an already-edited file (git diff, never hand-authored)"
    - "individual + cumulative git apply --check"
    - "py_compile without touching tracked __pycache__"
    - "revert-after-patch-generation cycle"
    - "fixture directory construction from the JSON spec"
    - "CLI execution + JSON-path assertion evaluation, reported as one PASS/FAIL block"
    - "changed-file scope verification"
    - "pull --ff-only / apply / commit / push to the real branch"
  must_not_do_by_hand:
    - "one-off Bash calls to cat/inspect a single JSON field — use run-fixture assertions instead"
    - "manually typed checkout/diff/revert per file — use gen-patch"
    - "manually typed cumulative apply/compile/revert — use validate"
    - "hand-built fixture KBs via heredocs, one file at a time — use run-fixture's files: {} block"

known_failure_modes_from_first_run:
  - id: "design_agent_overhead"
    symptom: "spawned subagents to re-derive a design the main thread had already read enough to write directly"
    rule: "if you already read every relevant source line yourself, do not delegate re-derivation; delegate only a short confirm/refute verdict if a second opinion is wanted"
  - id: "fixture_construction_by_hand"
    symptom: "~24 separate Bash calls to build 4 fixture KBs and inspect JSON fields one at a time"
    rule: "always go through `run-fixture --spec <json>`; write the spec once, run once"
  - id: "pycache_drift"
    symptom: "python -m py_compile writes into tracked apex-meta/scripts/__pycache__/*.pyc even with PYTHONDONTWRITEBYTECODE=1 (that env var only suppresses import-time caching, not explicit py_compile writes)"
    rule: "never call `python -m py_compile` directly against a tracked file; use the toolkit's py_compile_no_cache (redirects cfile to a temp dir outside the repo)"
  - id: "prose_manifest"
    symptom: "wrote a 108-line narrative README instead of a dense manifest"
    rule: "patch-pack documentation defaults to OKF/YAML, not prose Markdown"
  - id: "fixture_placement_mistake"
    symptom: "first fixture put a pointer_only source file inside raw/, a normally-scanned dir, silently defeating the test"
    rule: "before writing a fixture spec, restate in one line what the fixture must prove false (e.g. 'file must NOT be reachable via normal scanning') and check the files: {} paths against that line"

process:
  - phase: "0_identify"
    llm_action: "read target file(s) once; list candidate stub functions with 1-line evidence each (e.g. 'returns hardcoded {} — never touches manifest')"
    script_action: "none yet"
    output: "short list: function name -> 1-line bug -> 1-line required behavior"

  - phase: "1_worktree"
    script_action: "python stub_repair_toolkit.py worktree-add --repo <repo> --at <scratch-path> --ref <branch>"
    llm_action: "none"
    rule: "never edit the primary checkout, even transiently"

  - phase: "2_write_replacement"
    llm_action: "edit the stub function(s) in place inside the scratch worktree using normal file-edit tools — this is the one step that must be LLM-authored"
    script_action: "none"

  - phase: "3_gen_patch"
    script_action: "python stub_repair_toolkit.py gen-patch --repo <scratch-path> --out <patch-dir>/NNN-name.patch <target-file> [<target-file> ...]"
    what_it_does: "diffs the already-edited file(s), verifies non-empty + expected file count, reverts the target(s) to clean, re-validates the patch with git apply --check against the now-clean tree"
    llm_action: "none — read the PATCH_OK line, move on"

  - phase: "4_fixture_spec"
    llm_action: >
      author one JSON file: {"kb_root": "...", "files": {"<rel path>": "<content>", ...},
      "commands": [{"id": "...", "argv": [...], "assert": [{"path": "a.b.c", "equals": X}, ...]}]}.
      One spec should cover every behavior claim from phase 0's list.
    script_action: "python stub_repair_toolkit.py run-fixture --spec <spec.json>"
    output: "single PASS/FAIL block per command, nonzero exit on any failure"
    rule: "if a FAIL appears, fix the replacement code (phase 2) and re-run this phase — do not hand-inspect JSON with ad hoc one-liners"

  - phase: "5_validate_pack"
    script_action: "python stub_repair_toolkit.py validate --repo <scratch-path> --patches <patch-dir> --py-compile <changed .py files>"
    what_it_does: "individual git apply --check per patch, cumulative check, real cumulative apply, py_compile (no cache drift), scope check, revert to clean"
    llm_action: "none"

  - phase: "6_docs_pass"
    llm_action: "diff each doc file mentally against the NEW behavior; only edit ones with a real, stated inaccuracy or gap — do not touch docs that are already accurate just because they were in scope"
    script_action: "gen-patch + validate, same as code files, one patch per doc file"
    rule: "record in the manifest which doc files were checked and needed nothing — that is a valid, reportable outcome, not a skipped step"

  - phase: "7_assemble"
    llm_action: "write one dense OKF/YAML manifest: patch list, target map, what each patch fixes in <=2 lines, validation results, apply instructions"
    script_action: "none (no assemble subcommand yet — see open_items)"
    rule: "no prose README; match apex-meta/patches/*/000-patch-manifest.md convention"

  - phase: "8_cleanup_builder"
    script_action: "python stub_repair_toolkit.py worktree-remove --repo <repo> --at <scratch-path>"
    llm_action: "copy the finished patch-pack directory into the real repo's apex-meta/patches/<name>/ (new dir, no overwrite risk)"

  - phase: "9_apply_to_main"
    trigger: "only on a separate, explicit user instruction — never automatically follow from phase 8"
    script_action: >
      python stub_repair_toolkit.py finalize --repo <repo> --patches <patch-dir> --branch main
      --commit-message "<msg>" [--push]
    what_it_does: "checkout branch, pull --ff-only, dirty-overlap guard, apply --check, apply, scope check, py_compile, optional add+commit+push"
    llm_action: "write the commit message; read the FINAL_REPORT block; decide whether to pass --push"

token_budget_expectation:
  llm_authored_artifacts_per_run: "1 stub list, N replacement-code edits, 1 fixture spec, 1 manifest, 1 commit message"
  script_calls_per_run: "1 worktree-add, N gen-patch, 1 run-fixture, 1 validate, 1 worktree-remove, 1 finalize"
  contrast_with_first_run: "~90 tool calls total, most of them ad hoc Bash; this shape targets roughly (5-8) + (2N) calls for an equivalent N-file repair"

open_items_for_further_research:
  - id: "no_assemble_subcommand"
    gap: "phase 7 manifest writing is still manual/LLM-authored; a fields-in-JSON -> manifest.md templating subcommand would remove the last prose-risk step"
    next_step: "add `assemble` subcommand to stub_repair_toolkit.py once 2-3 more real runs show a stable manifest field set"
  - id: "ast_stub_detection_unimplemented"
    gap: "phase 0 is still fully manual reading; an AST-based scanner (flag functions whose body is a single Return of an empty literal, or a single Pass) could pre-filter candidates before the LLM reads the file"
    next_step: "prototype as a `find-stubs` subcommand; validate false-positive rate on 2-3 real files before trusting it unattended"
  - id: "fixture_spec_reuse_across_runs"
    gap: "each run currently authors a fresh fixture spec from scratch; common KB-shaped fixtures (manifest + pointer source + wiki page) recur across apex-kb repair runs"
    next_step: "extract a small library of reusable fixture-spec fragments once 3+ runs exist to compare against"
  - id: "toolkit_tested_only_on_apex_kb_shape"
    gap: "gen-patch/validate/run-fixture were smoke-tested against apex_kb.py in a disposable worktree; not yet exercised on a multi-directory or non-Python target"
    next_step: "next real usage should be treated as the first production test, not assumed pre-validated for arbitrary repo shapes"
---
