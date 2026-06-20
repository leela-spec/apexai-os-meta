# Apex Session Package Manifest

~~~yaml
package_manifest:
  package_name: apex-session
  package_path: ".claude/skills/apex-session/"
  purpose: "Index the apex-session package files."
  read_when:
    - operator_inspects_package_structure
    - validating_file_inventory
~~~

## File Index

| path | purpose | read_when |
|---|---|---|
| `.claude/skills/apex-session/SKILL.md` | Skill entrypoint and invocation contract. | skill_invocation, entrypoint_review |
| `.claude/skills/apex-session/references/session-cluster-contract.md` | Canonical package boundary and process scope. | boundary_review, process_scope_check |
| `.claude/skills/apex-session/references/mutation-gate-rules.md` | Canonical mutation gate and confirmation rules. | mutation_review, operator_validation |
| `.claude/skills/apex-session/references/state-delta-and-entity-rules.md` | Canonical state delta and entity proposal rules. | state_delta_review, entity_update_review |
| `.claude/skills/apex-session/references/handoff-and-next-session-contract.md` | Canonical handoff and next-session contract. | handoff_review, next_session_review |
| `.claude/skills/apex-session/templates/task_plan.md` | Blank task_plan template. | task_plan_creation |
| `.claude/skills/apex-session/templates/findings.md` | Blank findings template. | findings_creation |
| `.claude/skills/apex-session/templates/progress.md` | Blank progress template. | progress_creation |
| `.claude/skills/apex-session/templates/next-session.md` | Blank next-session template. | next_session_creation |
| `.claude/skills/apex-session/package-manifest.md` | Lightweight package index. | package_review |

## Package Boundaries

- Do not generate scripts.
- Do not write to repositories.
- Do not compute next-task ranking.
- Do not scan blockers.
- Do not rebuild registries.
- Do not compute scores.
- Do not decompose new work.
- Do not mutate without explicit operator confirmation.