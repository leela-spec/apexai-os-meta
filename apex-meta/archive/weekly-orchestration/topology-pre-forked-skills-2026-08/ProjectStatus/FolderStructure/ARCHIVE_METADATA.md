```yaml
archive_metadata:
  original_path: .claude/skills/ProjectStatus/FolderStructure/
  archived_date: 2026-08-18
  reason: abandoned_generator_artifact_never_promoted_never_referenced_by_live_SKILL_md
  replacement: .claude/skills/ProjectStatus/SKILL.md
  architecture_decision_ref: apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md#D007
```

This folder contains a partially built `references/` + `templates/` + `examples/` layout matching what `ProjectStatus/SKILL.md` declares -- but it was never promoted up one level, and `SKILL.md` never referenced it. Initially misread as evidence that the subdirectory layout was intended (it is not: the live package's actual consumers use flat paths, and this folder is simply another artifact of the same generator that left AIRouting's file-creation scaffolding behind, tracked separately in the repair pass).

Preserved as-is for Module 08 alongside `FirstIteration/`, since it duplicates the same divergent content set. Kept for history per D007 -- not deleted.
