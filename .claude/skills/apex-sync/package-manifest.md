# Apex Sync Package Manifest

## package_name

```yaml
package_name: apex-sync
```

## package_path

```yaml
package_path: .claude/skills/apex-sync/
canonical_script_path: scripts/apex_sync.py
```

## package_status

```yaml
package_status: final_canonical_v1
```

## exact_file_index

```yaml
exact_file_index:
  - .claude/skills/apex-sync/SKILL.md
  - .claude/skills/apex-sync/references/sync-cluster-contract.md
  - .claude/skills/apex-sync/references/script-command-contract.md
  - .claude/skills/apex-sync/references/registry-and-drift-rules.md
  - .claude/skills/apex-sync/references/scoring-and-focus-rules.md
  - .claude/skills/apex-sync/package-manifest.md
  - scripts/apex_sync.py
```

Directory tree:

```txt
.claude/skills/apex-sync/
  SKILL.md
  references/
    sync-cluster-contract.md
    script-command-contract.md
    registry-and-drift-rules.md
    scoring-and-focus-rules.md
  package-manifest.md
scripts/
  apex_sync.py
```

## file_purpose_map

| File | Purpose |
|---|---|
| `SKILL.md` | Skill entrypoint, routing description, objective, accepted inputs, required outputs, procedure, validation rules, failure modes, and completion gate. |
| `references/sync-cluster-contract.md` | B_SYNC package boundary, owned/excluded processes, routing, read-side policy, registry write exception, and custom Python caveats. |
| `references/script-command-contract.md` | Canonical command, flags, subcommands, report contracts, exit-code policy, JSON policy, dry-run policy, and no-shell-out policy. |
| `references/registry-and-drift-rules.md` | Task discovery, task frontmatter validation, registry schema, rebuild rules, drift detection rules, malformed-file policy, and write gate. |
| `references/scoring-and-focus-rules.md` | H7 priority and urgency scoring, actionability, blocker semantics, stale semantics, unlock depth, focus sorting, and report schemas. |
| `package-manifest.md` | Package inventory, source basis, read order, invariants, checklist, forbidden claims, and backup/application notes. |
| `scripts/apex_sync.py` | Standard-library Python implementation of deterministic B_SYNC reports. |

## source_basis_map

| Source | Treatment | Used for |
|---|---|---|
| Apex H1–H7 decisions | LOCK | Status enum, path roots, dependency field, Python-only rule, B_SYNC cluster, handoff boundary, priority/urgency scoring. |
| Existing Apex sync scaffold | MIGRATE_AND_REWRITE | Existing parser behavior, subcommand categories, dry-run behavior, registry write restriction, and report vocabulary. |
| CCPM `SKILL.md` and `track.md` | ADAPT | Script-first deterministic reporting principle and tracking command categories. |
| Task Master `find-next-task.js` | ADAPT | Dependency-satisfied candidate filtering, priority weighting, dependency-count tie-break concept, deterministic next-action logic. |
| Backlog `types/index.ts` and `parser.ts` | ADAPT | Frontmatter/body split, task field concepts, raw content preservation, dependencies, priority, parent/subtask ideas. |
| llm-wiki `SKILL.md` | CONCEPT_ONLY | Index discipline, raw/source discipline, audit/drift visibility concept. |
| Apex skill definition guide | FORMAT_GUIDANCE | Frontmatter, objective, procedure, validation, supporting-file structure, completion gate. |
| Unavailable llm-wiki update-index script | OMIT_AS_SOURCE | Not used. No copied behavior claim. |
| Unavailable Kanban blocker script | OMIT_AS_SOURCE | Not used. Blocker behavior is custom Apex Python. |

## read_order

Recommended read order for operators or future maintainers:

1. `SKILL.md`
2. `references/sync-cluster-contract.md`
3. `references/script-command-contract.md`
4. `references/registry-and-drift-rules.md`
5. `references/scoring-and-focus-rules.md`
6. `package-manifest.md`
7. `scripts/apex_sync.py`

## package_invariants

```yaml
package_invariants:
  package_status: final_canonical_v1
  exact_file_count: 7
  canonical_script_path: scripts/apex_sync.py
  no_final_md_variants: true
  no_apex_plan_behavior: true
  no_apex_session_behavior: true
  no_task_status_mutation: true
  no_handoff_authoring: true
  no_operator_validation_claim: true
  default_mode: dry_run
  only_allowed_write_path: apex-meta/registry/index.md
  python_standard_library_only: true
  shell_out_allowed: false
  external_dependencies_allowed: false
  H1_status_enum:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  H3_dependency_field: depends_on
```

## validation_checklist

Before applying this package, validate:

- [ ] Exactly seven target files are present.
- [ ] No `.final.md` variants are created.
- [ ] `SKILL.md` frontmatter is valid YAML.
- [ ] Markdown headings have blank lines around them.
- [ ] Code fences are balanced.
- [ ] The canonical command path is `scripts/apex_sync.py`.
- [ ] `python -m py_compile scripts/apex_sync.py` passes.
- [ ] `python scripts/apex_sync.py next --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py blockers --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py registry --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py stall --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py drift --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py score --root . --json --dry-run true` runs.
- [ ] No task file mutation behavior exists.
- [ ] No handoff authoring behavior exists.
- [ ] Registry write gate exists and is limited to `registry --dry-run false`.
- [ ] `depends_on` is canonical.
- [ ] `dependencies` is not used as canonical.
- [ ] Custom Apex Python caveats are present.
- [ ] Forbidden source-copy claims are absent.

## forbidden_claims

Do not claim:

- `copied_llm_wiki_update_index_py`
- `copied_kanban_blocker_script`
- `copied_OpenClaw_TaskFlow`
- `fully_source_backed_B_SYNC_without_custom_python`
- `copied_bash_script_behavior_as_python_without_adaptation`

## backup_and_application_notes

Before applying final files, back up current files to:

```txt
apex-meta/harmonization/backups/apex-sync-pre-final-YYYY-MM-DD/
```

Back up these files if present:

- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/apex-sync/package-manifest.md`
- `.claude/skills/apex-sync/references/sync-cluster-contract.md`
- `.claude/skills/apex-sync/references/script-command-contract.md`
- `.claude/skills/apex-sync/references/registry-and-drift-rules.md`
- `.claude/skills/apex-sync/references/scoring-and-focus-rules.md`
- `apex-meta/scripts/apex_sync.py`

Then write the final package files to the exact paths in `exact_file_index`.
After validation succeeds, the old backup source script path may be removed by
the operator as a separate cleanup step.