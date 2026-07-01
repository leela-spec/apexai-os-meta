Title: Claude Skills Rules | SKILL.md Naming Conventions and the 500-Line Limit

URL Source: https://clauder-navi.com/en/claude-skills-rules

Published Time: 2026-05-16T15:00:10+09:00

Markdown Content:
## What Are Claude Skills Rules — 4 Types of Rules That Make Skills Work

The core intent behind searching "claude skills rules" is the **set of official rules** that must be followed when creating Claude Agent Skills. Skills are a lightweight extension mechanism that operates entirely through a single SKILL.md file — a YAML frontmatter plus a Markdown body — and Claude automatically discovers them when you place them at `.claude/skills/<name>/SKILL.md`.

However, "working" and "being correctly discovered and executed by Claude" are two different things. Anthropic's [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) defines rules across five areas — frontmatter format validation, naming, description person, body size, and reference hierarchy — and following them makes a significant difference in Skill discoverability and execution accuracy.

This article organizes these rules in order of how easy they are to get wrong. In addition to the four axes introduced above (metadata constraints, description style, physical size, and reference hierarchy), it also covers the discipline of evaluation-driven development — all in one article.

## SKILL.md Frontmatter Validation Rules

The YAML frontmatter at the top of SKILL.md is subject to format validation by Claude's loader. Only two fields are required — `name` and `description` — but each has strict rules.

The constraints on `name` are as follows:

1.   At most 64 characters
2.   Only lowercase letters, digits, and hyphens `-` (no uppercase, underscores, or spaces)
3.   Must not contain XML tags
4.   Must not contain the reserved words `anthropic` or `claude`

The constraints on `description` are three: at most 1024 characters, must not be empty, and must not contain XML tags. Because `description` is **the only summary Claude references when selecting the right Skill from 100 or more options**, it must satisfy the format constraints while also conveying both "what it does" and "when to use it."

These constraints are repeatedly stated in the Skill structure section of the Skills overview and the Naming conventions section of the Best practices guide. Violations result in the Skill failing to load or be discovered — a fatal outcome.

## Naming Conventions — Gerund Form and No Vague Names

Once the `name` field satisfies the format requirements, Anthropic recommends the **gerund form** as the preferred naming style. Verb + -ing concisely communicates "the capability this Skill provides."

Official recommended examples:

1.   `processing-pdfs`
2.   `analyzing-spreadsheets`
3.   `managing-databases`
4.   `testing-code`
5.   `writing-documentation`

Noun phrases (`pdf-processing` / `spreadsheet-analysis`) and verb forms (`process-pdfs` / `analyze-spreadsheets`) are also acceptable alternatives. The following patterns should be avoided:

*   Vague names: `helper` / `utils` / `tools`
*   Overly generic: `documents` / `data` / `files`
*   Reserved word inclusion: `anthropic-helper` / `claude-tools`
*   Inconsistent patterns within a collection

Consistent naming not only helps Claude discover Skills more easily, but also makes it immediately clear — from documentation or conversation references — which Skill is being discussed. When you have 100 Skills, this consistency is what pays off.

## Write Descriptions in Third Person — The Style That Determines Discoverability

The most critical mistake for Skill discoverability is writing `description` in first or second person. Anthropic's official documentation emphasizes **"Always write in third person"** in a Warning block.

The reason is straightforward: descriptions are injected as strings into Claude's system prompt. Mixed perspectives cause Claude to misread "who does what in this Skill," reducing selection accuracy.

*   ✓ Good: "Processes Excel files and generates reports"
*   ✗ Bad: "I can help you process Excel files"
*   ✗ Bad: "You can use this to process Excel files"

In addition, descriptions must include **both "what it does" and "when to use it."** The official PDF Processing Skill description is written as follows:

> Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

The first half states the functionality; the second half states the trigger condition. Vague descriptions like "Helps with documents," "Processes data," or "Does stuff with files" provide no useful signal for Skill selection and will be ignored by Claude.

## The 500-Line Rule and Progressive Disclosure in SKILL.md

While the `name` and `description` metadata are always expanded into the system prompt, the SKILL.md body is only read by Claude when the Skill is triggered. Even so, once loaded, every token consumes context — which is why Anthropic sets **500 lines or fewer as the official upper limit** for the SKILL.md body.

When 500 lines is exceeded, content should be split into separate files and linked from SKILL.md via reference links. This is Progressive Disclosure. By splitting content into domain-specific files like `reference/finance.md` and `reference/sales.md`, when a user asks about sales, Claude only reads sales.md via bash — finance.md is never loaded into context. This is the actual mechanism behind the claim that "even with 100 Skills, context doesn't bloat."

The three key implementation points are:

1.   Keep the SKILL.md body to 500 lines or fewer; split if exceeded
2.   Split files by domain or feature (granular enough that the filename reveals the content)
3.   Place referenced files **only one level deep** from SKILL.md

Point 3 is the topic of the next section.

## Keep References 1 Level Deep — No Deeply Nested References

Anthropic's documentation has a dedicated section titled "Avoid deeply nested references," which explicitly rejects multi-level structures where a reference file chains to another reference file.

The reason is an implementation constraint: Claude may internally read only the beginning of a file, so if nesting is deep, the system can reach a state where it "can only read partway through and never reaches the actual content."

*   ✗ Bad: SKILL.md → advanced.md → details.md (actual content is in details.md)
*   ✓ Good: Link directly from SKILL.md to advanced.md / reference.md / examples.md, with the actual content placed there

Additionally, the official documentation specifies that if a referenced file itself exceeds 100 lines, a **table of contents** must be placed at the top. Even when Claude reads only a portion, having the table of contents section visible lets it determine "this information is located at this position."

## File Path and Terminology Discipline — Forward Slashes and Consistency

Two rules are easy to get wrong during implementation.

First: **always use forward slashes (`/`) for file paths**. Skills run in a Unix-style code execution environment, so Windows-style paths like `scripts\helper.py` will cause errors. Use notation like `scripts/helper.py` and `reference/guide.md`.

Second: **terminology consistency**. Using different words for the same concept within a document causes Claude to become confused.

*   Good (consistent): only "API endpoint," only "field," only "extract"
*   Bad (mixed): mixing "API endpoint," "URL," "API route," and "path"

Additionally, the rules state that time-dependent information (e.g., "use the old API until August 2025, then the new API after that") should not appear in the body. Information that becomes stale over time should be moved into an "Old patterns" section wrapped in `<details>`, leaving only the current correct procedure in the body.

## Reference MCP Tools by Fully Qualified Name

When calling MCP (Model Context Protocol) tools from within a Skill, Anthropic's official documentation **requires the fully qualified format `ServerName:tool_name`**.

*   ✓ Good: `Use the BigQuery:bigquery_schema tool to retrieve table schemas.`
*   ✓ Good: `Use the GitHub:create_issue tool to create issues.`
*   ✗ Bad: `Use bigquery_schema` / `Use create_issue` (no server name)

In environments where multiple MCP servers are active simultaneously, references without a server name will fail with a "tool not found" error. If a Skill is expected to run in multiple environments, writing in fully qualified form from the start is the safe approach.

## Evaluation-Driven Development — Write Evals First

Another important quality rule for Skills is **creating evaluations before writing documentation**. Anthropic's Best practices has a dedicated section titled "Build evaluations first," recommending the following five steps:

1.   Have Claude solve representative tasks without the Skill, and identify where it fails
2.   Create 3 evaluation scenarios and make the gaps into tests
3.   Measure the baseline without the Skill
4.   Write a minimal SKILL.md to close the gaps
5.   Run evaluations and iterate while comparing against the baseline

Putting evals off until later leads to a proliferation of "rules written from imagination" that don't solve actual problems, resulting in a bloated Skill that doesn't work. Writing at least 3 scenarios first and verifying effectiveness across Haiku, Sonnet, and Opus is the final item on the official checklist.

## Summary — Only Rules-Compliant Skills Work Even When You Have 100 of Them

Claude Skills rules span multiple layers: format validation (name up to 64 characters, description up to 1024 characters), naming (gerund form), description style (third person, explicit trigger conditions), physical size (500 lines), reference hierarchy (1 level deep), terminology consistency, MCP fully qualified names, and evaluation-driven development.

Individually, these look like minor conventions — but failing to follow them surfaces in every case as **Claude not discovering, not fully reading, or not selecting the Skill**. The appeal of Skills — that even 100 of them can run without bloating context — is a design that works only because authors follow these rules.

Source: [Skill authoring best practices (Anthropic official)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) / [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
