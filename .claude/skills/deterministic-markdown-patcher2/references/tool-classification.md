# Tool Classification

## Core

| Tool | Role |
|---|---|
| Python executor | Owns schema validation, live target resolution, bounded mutation, reporting, rollback orchestration. |
| JSON Schema | Owns planner intent and policy contracts before any mutation. |
| git | Provides worktree isolation, generated diff proof, status checks, and rollback primitives. |
| yq | Handles guarded YAML frontmatter updates when available. |
| rg | Performs fast discovery and match counting; it is not a mutator. |
| fixture runner | Builds repeatable fixtures and converts validations into pass/fail reports. |

## Trial Only

| Tool | Trial boundary |
|---|---|
| mdpatch | Test only after fixture coverage for duplicate headings, nested headings, CRLF, code fences, and frontmatter. |
| remark/mdast | Test range extraction only; do not adopt full-file serialization without formatting fixtures. |
| comby | Limit to code-like patterns inside Markdown or config-like blocks with explicit uniqueness checks. |
| fuzzy matching | Use only for candidate ranking; never as a silent writer without strict confidence and margin reporting. |
| Markdown table row editing | Treat as a specialized fixture-backed mode with header and row-key uniqueness checks. |
| blocking hooks | Add after audit-mode logging proves the policy will not block valid executor flows. |

## Rejected As Core

| Tool or pattern | Reason |
|---|---|
| AI-authored unified diffs | Fragile context, hunk, and line-offset dependence. |
| Line-number mutation | File drift makes line positions non-authoritative. |
| Direct sed/awk/perl from planner output | Deterministic execution does not prove semantic target safety. |
| Patch fuzz | Applies near-matches without proving intended target semantics. |
| Full AST reserialization | Risks unrelated formatting churn across Markdown files. |
