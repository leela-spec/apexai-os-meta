```yaml
archive_metadata:
  original_path: .claude/skills/ProjectStatus/FirstIteration/
  archived_date: 2026-08-18
  reason: superseded_earlier_iteration_of_the_package_creating_a_competing_entrypoint_claim
  replacement: .claude/skills/ProjectStatus/SKILL.md
  architecture_decision_ref: apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md#D007
```

This folder was a self-labelled earlier iteration of the ProjectStatus package, left in place beside the live `.claude/skills/ProjectStatus/` package. One file inside, `project-status-overview_SKILL.md`, opens with `# FILE: .claude/skills/project-status-overview/SKILL.md` -- a self-declared competing entrypoint claim. Because `ProjectStatus/SKILL.md`'s `supporting_files` declarations could not resolve to their real targets (a separate repair, tracked in `CURRENT-STATE.md`'s "Post-closure repair pass"), a fresh agent searching for the missing files could land here and mistake this folder for current authority.

The divergent template/contract/ranking-rules versions inside this folder are preserved as-is for Module 08 (`08-project-status/README.md`), which decides whether ProjectStatus survives, and if so, which version (if any) is authoritative. Archiving removes the live false-authority hazard without making that content decision.

Kept for history per D007 -- not deleted.
