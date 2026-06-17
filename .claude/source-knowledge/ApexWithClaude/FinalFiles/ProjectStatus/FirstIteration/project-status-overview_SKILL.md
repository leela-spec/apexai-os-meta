# FILE: .claude/skills/project-status-overview/SKILL.md

````markdown
---
name: project-status-overview
description: >
  create, normalize, update, rank, or validate a compact cross-project project status overview from manual notes, project-specific status summaries, previous overview text, or unassigned incoming items. produces a project → task → subtask overview with [priority/urgency/date] ratings. does not create weekly plans, daily plans, status merges, project execution, or detailed project databases.
---

# Project Status Overview

## Objective

Use this skill when the operator wants a compact cross-project overview of current project tasks and subtasks. Convert supplied context into a lightweight status aggregator that helps later planning routines see what matters across projects. The output must stay at the project → task → subtask level and must use `[priority/urgency/date]` ratings. Do not create weekly plans, next-day plans, execution plans, status-merge packets, or detailed project-state files.

## Output Shape

Use this compact format:

```text
Project Name
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]
````

Rating fields:

```yaml
rating_format:
  syntax: "[priority/urgency/date]"
  priority: 1-100
  urgency: 1-100
  date: "DD-MM or NA"
```

## Supporting Files

Read these files only when needed:

- `references/project-status-overview-contract.md` — use when the operator asks for contract-level structure or validation.
    
- `templates/current-project-status-overview-template.md` — use when creating a blank or reusable overview template.
    
- `references/ranking-and-validation-rules.md` — use when ranking, validating, or correcting overview entries.
    

## Procedure

**Phase 1 — Load supplied context**

1. Load all context supplied by the operator, including manual notes, project-specific summaries, previous overview text, and unassigned incoming items.
    
2. Identify the active project sections. Default initial projects are `Leela`, `Apex`, `MasterOfArts`, `Investment`, and `Others` unless the operator supplies a different project list.
    

**Phase 2 — Separate assigned and unassigned material**

3. Separate material that clearly belongs to a project from material that is still unassigned.
    
4. Put unresolved incoming infos, tasks, and project candidates into an `Unassigned` section only when they cannot yet be placed under a project.
    
5. Remove an item from `Unassigned` once it has been assigned to a project.
    

**Phase 3 — Normalize into project → task → subtask**

6. Normalize assigned material into project sections.
    
7. Convert main project-level chunks into tasks.
    
8. Convert smaller execution pieces under a task into subtasks.
    
9. Do not create workstreams.
    
10. Do not require project IDs, heavy task IDs, or stable chunk IDs in the human-facing output.
    

**Phase 4 — Preserve or add metrics**

11. Preserve existing `[priority/urgency/date]` ratings when they are supplied and valid.
    
12. Add missing ratings only when the source context supports a reasonable estimate.
    
13. Use `NA` when there is no real deadline.
    
14. Mark uncertain or estimated ratings as needing operator review.
    

**Phase 5 — Rank tasks**

15. Create a ranked task view using this order:
    
    1. Manual override if supplied by the operator.
        
    2. Deadline-first ranking.
        
    3. Priority second.
        
    4. Urgency third.
        
16. Treat `NA` deadlines as no fixed date, not as low importance.
    
17. Apply operator manual override whenever supplied, including pinned, promoted, demoted, or frozen items.
    

**Phase 6 — Surface blockers only when present**

18. Include blockers only when the supplied context names a real blocker.
    
19. Do not invent blockers.
    
20. Do not create a blocker registry.
    

**Phase 7 — Validate compactness**

21. Check that the output uses only project → task → subtask.
    
22. Check that no workstream layer was created.
    
23. Check that no detailed project database was created.
    
24. Check that every task and subtask rating uses `[priority/urgency/date]`.
    
25. Check that every unassigned item is either unresolved or explicitly awaiting assignment.
    

**Phase 8 — Present for operator review**

26. Present the final compact overview.
    
27. Include a short operator review section listing:
    
    - uncertain ratings
        
    - unresolved unassigned items
        
    - possible duplicate tasks
        
    - any ranking conflict caused by deadline versus manual override
        

## Completion Gate

The skill is complete when it produces a compact current project status overview that:

- uses project → task → subtask structure,
    
- uses `[priority/urgency/date]` ratings,
    
- ranks tasks deadline-first unless overridden,
    
- keeps unassigned items separate only while unresolved,
    
- surfaces blockers only when present,
    
- and avoids creating a detailed project database.
    

```

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] File path is `.claude/skills/project-status-overview/SKILL.md`.
- [ ] The skill is compact and Claude-native.
- [ ] The skill uses project → task → subtask.
- [ ] The skill does not use workstreams.
- [ ] The skill does not create detailed project-state files.
- [ ] The skill uses `[priority/urgency/date]`.
- [ ] Ranking is deadline-first with manual override.
```