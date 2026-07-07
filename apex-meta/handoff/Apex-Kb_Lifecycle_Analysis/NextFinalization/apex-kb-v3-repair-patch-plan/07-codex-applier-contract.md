# Codex Applier Contract

## 1. Role

```yaml
codex_role:
  role: "deterministic patch applier/verifier"
  branch: main
  patch_pack_root: "apex-meta/patches/apex-kb-v3-repair/"
````

## 2. Must

```yaml
must:
  - "work directly on main"
  - "apply the validated patch pack only"
  - "reject patch files that fail git apply --check"
  - "run py_compile on both scripts"
  - "run command help checks"
  - "run targeted smoke behavior checks for repaired features"
  - "verify changed-file scope"
  - "commit and push only after all validation passes"
```

## 3. Must not

```yaml
must_not:
  - "perform manual equivalent edits after failed patch apply"
  - "accept marker checks as behavior proof"
  - "push PASS_WITH_WORKAROUNDS"
  - "edit target files outside patch application"
  - "repair invalid patches in place and still claim validated-pack apply"
  - "open a PR unless explicitly requested"
```

## 4. Required command shape

```bash
git checkout main
git pull --ff-only origin main
git apply --check apex-meta/patches/apex-kb-v3-repair/*.patch
git apply apex-meta/patches/apex-kb-v3-repair/*.patch
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design --help
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-skill-design --help
```

## 5. Final report requirements

```yaml
final_report_required_fields:
  - verdict
  - patch_pack_root
  - git_apply_check_all
  - py_compile_apex_kb
  - py_compile_retrieval
  - behavior_checks
  - changed_file_scope
  - commit_sha
  - pushed_to_origin_main
  - workarounds_used
```

`workarounds_used` must be `false` for PASS.
