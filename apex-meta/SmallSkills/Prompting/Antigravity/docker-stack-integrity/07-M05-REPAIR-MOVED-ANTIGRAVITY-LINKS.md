# M05 — Repair Moved Antigravity Authority Links

## Goal

Repair the broken relative links created when the Docker-stack implementation plans were moved from the Antigravity prompting folder to `apex-meta/Alpine/ImplementationPlans/`.

## Depends on

Baseline only; execute after M04 for program order.

## Required active context

Read only:

- correction control files;
- this module;
- `apex-meta/Alpine/ImplementationPlans/00-START-HERE.md`;
- `apex-meta/Alpine/ImplementationPlans/01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md`;
- directory listing for `apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/`.

Do not load the contents of every implementation plan.

## Current defect

Moved plan files still reference paths such as:

```text
../antigravity-instruction-orchestrator/SKILL.md
```

That path is no longer valid from `apex-meta/Alpine/ImplementationPlans/`.

## Scope

Patch only broken authority/resource links in the moved implementation-plan control files and any other plan file where the same stale relative path is actually present.

Use the real current repository location:

`apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/`

Prefer repository-relative links that remain understandable from GitHub and local checkout. Do not duplicate the orchestrator files into the Alpine folder.

## Verification

Positive:

- resolve every patched link against the repository tree;
- all referenced `SKILL.md`, `lessons-learned.md`, and `prompt-patterns.md` paths exist;
- no required authority link points outside the repo incorrectly.

Negative/adversarial:

- search `apex-meta/Alpine/ImplementationPlans/` for the old invalid `../antigravity-instruction-orchestrator` form;
- result must be zero unless a literal historical example is explicitly marked non-executable.

## Acceptance

PASS when Antigravity can start from the moved START-HERE file and resolve every authority/resource link without guessing.

Persist M05 result, update state, commit only link/path corrections, context-reset, continue M06.