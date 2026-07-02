# Claude Skill Design Source Gap Analysis

## Do we have enough official Claude/Agent Skills sources?

ProjectRepos adds examples, not canonical authority. The official-baseline Phase 1 should rely on existing curated official docs/repos. If those official sources are complete, yes; from ProjectRepos alone, no.

## Do we have enough real-world SKILL.md examples?

Yes. The generated candidate report contains 2,000 ranked candidates, dominated by real SKILL.md packages. The allowlist includes 45 first-pass examples and 34 maybe-later examples after deduping repeated antigravity plugin copies.

## Do we have skill evaluation/rubric sources?

Partially. Strong candidates include `skillcheck`, CrewAI valid/minimal/invalid fixtures, `testing-qa`, `verification-before-completion`, `test-master`, `code-reviewer`, `security-reviewer`, and security testing packages. A dedicated official rubric or evaluator spec is still a gap.

## Do we have prompt/instruction-design sources?

Partially. Good candidates include prompt optimization, writing plans, spec mining, Claude code guide, AGENTS.md, recursive context pruning/token budgeting, and feature-forge. These are useful examples but should be subordinated to official skill description/frontmatter rules.

## Do we have evidence for subskills/package modularity?

Yes, but mostly example-level rather than canonical. Evidence comes from nested paths such as `app-builder/templates/SKILL.md`, template/reference packages, manifest setup, bundle-style workflow packages, memory/MCP packages, and many duplicate plugin bundle copies. Treat this as design evidence, not official proof.

## Which repo families are useful but not core?

- `antigravity-awesome-skills-main`: very useful for examples, but noisy and highly duplicated across top-level, plugin, and bundle paths.
- `claude-skills-main`: useful as a compact second corpus of real Claude skill examples.
- `skillcheck`: core for quality/evaluation despite being small.
- `crewAI-main`: useful only for skill fixture examples and comparative agent framework context.
- `claude-task-master-main`, `backlog-main`, `ccpm-main`, `planning-with-files-master`: useful only if studying transferable process/task orchestration patterns, not core skill package design.

## Which repo families should not enter the Claude Skill Design KB?

- Binary/media-heavy folders and screenshots.
- Generated catalogs and dependency lockfiles.
- Duplicate antigravity plugin/bundle copies when a top-level skill copy exists.
- Generic app source code that does not explain skill package structure.
- Project-management-only frameworks unless a later task explicitly studies comparative workflow design.

## Practical Gap Closure

Before final synthesis, import the include-first allowlist, rerun deterministic `apex_kb.py phase0`, and then run Phase 1 batches in the order specified by the task: official guidance, official repo core, high-impact repo examples, operator notes, and academic/security sources.
