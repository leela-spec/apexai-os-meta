# Intro

The current live-span/validator-first design is directionally correct; no single off‑the‑shelf skill or package today gives you the full “plan → deterministic validate → deterministic apply → rollback → hook‑enforced” pipeline for Markdown/frontmatter, so the final architecture should combine a small set of focused CLI tools (yq, a span replacer, a section replacer, git apply) behind Claude Code hooks and a “no agent writes Markdown directly” policy.
## source_ledger

## Source 1

- source_name: Claude Code Hooks Reference / Hooks Guide
    
- url_or_repo: [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)[[code.claude](https://code.claude.com/docs/en/hooks-guide)]
    
- type: official docs
    
- freshness: 2026-06 (current hooks docs, referenced by multiple guides)[[youtube](https://www.youtube.com/watch?v=8bbJ4-nAZew&vl=sr)][[hidekazu-konishi](https://hidekazu-konishi.com/entry/claude_code_hooks_complete_guide.html)]
    
- evidence_summary: Defines PreToolUse/PostToolUse, lifecycle events, exit‑code semantics, and matcher/filters for tool names and arguments; shows that hooks can block or modify tool calls deterministically before and after execution.[[code.claude](https://code.claude.com/docs/en/hooks-guide)]
    
- relevance: core for enforcing “no Write/Edit/Bash outside patch CLI”, “no apply before validate”, and for gating edits on presence of a validated plan JSON.
    
- copyable_parts: example PreToolUse scripts for Write/Bash, settings.json hook registration patterns, permissionDecision schema, hook event list and blocking semantics.[[llmversus](https://llmversus.com/claude-code/pre-tool-use)]
    
- risks: hooks are shell scripts (security depends on your implementation), some bugs/limitations reported around blocking behavior and permissions integration.[[github](https://github.com/anthropics/claude-code/issues/4362)]
    

## Source 2

- source_name: disler/claude-code-hooks-mastery
    
- url_or_repo: [https://github.com/disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery)[[github](https://github.com/disler/claude-code-hooks-mastery)]
    
- type: GitHub repo + tutorials
    
- freshness: 2024-01 initial, still referenced in 2026 guides as a hooks pattern collection.[[context7](https://context7.com/disler/claude-code-hooks-mastery)]
    
- evidence_summary: Provides worked examples of using hooks to validate prompts, enforce tool policies, and add logging/TTS; demonstrates structuring hooks as a “deterministic shell layer” around Claude Code.[[context7](https://context7.com/disler/claude-code-hooks-mastery)]
    
- relevance: Good reference for structuring your own PreToolUse/PostToolUse scripts and for understanding practical pitfalls (exit codes, environment variables, JSON parsing).
    
- copyable_parts: hook skeleton scripts, JSON parsing patterns, suggestions for separating audit hooks from blocking hooks.
    
- risks: not an official repo; must review scripts for security, correctness, and compatibility with current Claude Code versions.
    

## Source 3

- source_name: @tylerburleigh/claude-sdd-toolkit / sdd-modify
    
- url_or_repo:
    
    - [https://github.com/tylerburleigh/claude-sdd-toolkit](https://github.com/tylerburleigh/claude-sdd-toolkit)[[github](https://github.com/tylerburleigh/claude-sdd-toolkit)]
        
    - [https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify](https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify)[[claude-plugins](https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify)]
        
- type: Python CLI + Claude skill bundle
    
- freshness: active through early 2026 with recent changelog entries and docs updates.[[github](https://github.com/tylerburleigh/claude-sdd-toolkit/blob/main/docs/getting-started.md)]
    
- evidence_summary: Implements spec‑driven development: plan‑first JSON specs, CLI that applies modifications with dry‑run, validation, backups, and rollback support; sdd‑modify is specifically marketed as “apply modifications systematically with safety checks and rollback.”[[github](https://github.com/tylerburleigh/claude-sdd-toolkit/blob/main/docs/architecture.md)]
    
- relevance: Closest existing “complete package” for plan/validate/apply/rollback integration, but its domain is code and SDD specs rather than Markdown patching.
    
- copyable_parts: architecture patterns (separate plan JSON, immutable spec, apply‑modifications command, backup/rollback strategy, test hooks), config file layout under .claude/.sdd_config.[[github](https://github.com/tylerburleigh/claude-sdd-toolkit/blob/main/docs/architecture.md)]
    
- risks: complexity overhead if adopted wholesale; SDD spec model might be overkill for relatively small Markdown patch tasks; needs security review before integrating its skills/scripts.
    

## Source 4

- source_name: coddingtonbear/markdown-patch
    
- url_or_repo: [https://github.com/coddingtonbear/markdown-patch](https://github.com/coddingtonbear/markdown-patch)[[github](https://github.com/coddingtonbear/markdown-patch)]
    
- type: library (Python) used inside Obsidian REST APIs
    
- freshness: maintained indirectly via Obsidian ecosystem, but repo itself shows limited recent activity (risk of slow bug fixes).
    
- evidence_summary: Implements a patch format that is aware of Markdown structure (frontmatter, headings, lists, blocks); used by obsidian-local-rest-api’s PATCH endpoint to modify frontmatter and headings.[[github](https://github.com/coddingtonbear/obsidian-local-rest-api/wiki/Changes-to-PATCH-requests-between-versions-2.0-and-3.0)]
    
- relevance: Strong candidate to replace bespoke “markdown-section-replacer”, at least for frontmatter and simple heading/section edits.
    
- copyable_parts: patch schema (operation, target_type, target, content), semantics for heading/frontmatter targeting, error behavior (invalid target).
    
- risks: known issue where heading‑based patches fail for nested headings if given only a leaf name, causing invalid‑target errors and pushing users toward full‑file rewrites.[[forum.obsidian](https://forum.obsidian.md/t/patch-content-with-target-type-heading-fails-on-all-h2-headings/114680)]
    

## Source 5

- source_name: Obsidian Local REST API + “REST API” successor plugin
    
- url_or_repo:
    
    - [https://github.com/coddingtonbear/obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api)[[github](https://github.com/coddingtonbear/obsidian-local-rest-api)]
        
    - [https://community.obsidian.md/plugins/rest-api](https://community.obsidian.md/plugins/rest-api)[[community.obsidian](https://community.obsidian.md/plugins/rest-api)]
        
- type: Obsidian plugin / local REST + MCP server
    
- freshness: local‑rest‑api is mature; REST API successor is more recent (2025–2026).[[github](https://github.com/coddingtonbear/obsidian-local-rest-api/releases)]
    
- evidence_summary: Exposes PATCH endpoints that use markdown-patch or a similar engine to target headings, blocks, and frontmatter; REST API plugin adds a “PATCH engine” with heading parsing, block/frontmatter targeting, and search‑replace operations.[[community.obsidian](https://community.obsidian.md/plugins/obsidian-local-rest-api)]
    
- relevance: Shows a production usage pattern for patching Markdown deterministically via HTTP; demonstrates how a structured patch format plus AST‑aware engine can avoid full‑file rewrites.
    
- copyable_parts: PATCH JSON schema (operation, targetType, target, content, createTargetIfMissing), search‑replace operation semantics, content negotiation and document‑map responses.[[community.obsidian](https://community.obsidian.md/plugins/rest-api)]
    
- risks: Obsidian‑specific; not directly usable for arbitrary repos; patch implementation still inherits markdown-patch limitations for nested headings unless mitigated by wrapper logic.[[github](https://github.com/coddingtonbear/obsidian-local-rest-api/wiki/Changes-to-PATCH-requests-between-versions-2.0-and-3.0)]
    

## Source 6

- source_name: yq frontmatter processing
    
- url_or_repo:
    
    - blog examples: [yq frontmatter edit posts](https://blog.omuomugin.com/posts/2025-05-07/)[[blog.omuomugin](https://blog.omuomugin.com/posts/2025-05-07/)]
        
    - Obsidian forum frontmatter CLI examples[[forum.obsidian](https://forum.obsidian.md/t/cli-ability-to-manipulate-frontmatter-for-a-document/112457)]
        
    - bulk frontmatter tag updates[[recfab](https://recfab.net/blog/2024/06/08/update-note-tags/)]
        
- type: CLI tool (yq), usage guides
    
- freshness: yq v4.x guides up to 2025; still widely used.
    
- evidence_summary: yq’s `--front-matter=process` flag allows reading and rewriting YAML frontmatter in Markdown files in‑place, supporting mass updates, field renames, and tag changes, with standard YAML syntax and the `-i` in‑place flag.[[haseebmajid](https://haseebmajid.dev/posts/2022-11-17-til-you-can-use-yq-to-mass-edit-markdown-files/)]
    
- relevance: Excellent match for “frontmatter patcher using yq”; clearly sufficient for most frontmatter tasks without custom parsing.
    
- copyable_parts: CLI patterns combining `find` + `yq --front-matter=process -i` for bulk edits, examples of adding/removing tags and fields, warnings about extract vs process modes.[[blog.omuomugin](https://blog.omuomugin.com/posts/2025-05-07/)]
    
- risks: assumes well‑formed YAML frontmatter; misuse of `extract` can accidentally overwrite content if not careful; requires yq dependency and some user familiarity.
    

## Source 7

- source_name: remark / unified / mdast ecosystem
    
- url_or_repo:
    
    - remarkjs/remark repo[https://github.com/remarkjs/remark](https://github.com/remarkjs/remark)[[github](https://github.com/remarkjs/remark)]
        
    - remark-cli[https://unifiedjs.com/explore/package/remark-cli/](https://unifiedjs.com/explore/package/remark-cli/)[[unifiedjs](https://unifiedjs.com/explore/package/remark-cli/)]
        
    - mdast-util-heading-range[https://www.npmjs.com/package/mdast-util-heading-range](https://www.npmjs.com/package/mdast-util-heading-range)[[npmjs](https://www.npmjs.com/package/mdast-util-heading-range)]
        
    - markdown-tree-parser CLI[https://github.com/ksylvan/markdown-tree-parser](https://github.com/ksylvan/markdown-tree-parser)[[github](https://github.com/ksylvan/markdown-tree-parser)]
        
- type: JS libraries + CLI
    
- freshness: actively maintained; mdast and remark CLI have recent releases and broad ecosystem usage.[[github](https://github.com/syntax-tree/mdast)]
    
- evidence_summary: remark-cli can “inspect and change markdown files” via AST plugins; mdast-util-heading-range allows programmatically replacing the content of a section between a heading and the next heading; markdown-tree-parser wraps remark into a CLI for tree manipulation.[[npmjs](https://www.npmjs.com/package/mdast-util-heading-range)]
    
- relevance: Ideal for section‑level deterministic replacements (heading‑scoped ranges, AST‑based transformations) and for validating Markdown structure before/after changes.
    
- copyable_parts: headingRange API pattern (find heading, handler replaces its section), CLI usage examples (`remark --output --use plugin file.md`), AST inspection for testing uniqueness of spans.
    
- risks: Node.js dependency; requires writing small JS scripts or plugins; remark-cli by itself does not provide rollback logic or validation beyond what your plugins implement.
    

## Source 8

- source_name: comby – structural search/replace
    
- url_or_repo: [https://comby.dev](https://comby.dev/) and [https://github.com/comby-tools/comby](https://github.com/comby-tools/comby)[[github](http://github.com/comby-tools/comby)]
    
- type: CLI + library
    
- freshness: actively maintained; widely referenced in structural refactoring discussions.[[comby](https://comby.dev/redirect)]
    
- evidence_summary: Comby performs structural search/replace using lightweight templates across “~every language,” understanding block/quote/string syntax for many formats; examples show code, HTML, JSON rewrites with in‑place modification or match‑only mode.[[hexmos](https://hexmos.com/freedevtools/tldr/common/comby/)]
    
- relevance: Good candidate for repetitive, content‑blind text restructurings (e.g., patternised list changes) but not Markdown‑semantics aware like mdast; best used for limited patterns where context is obvious.
    
- copyable_parts: CLI template syntax, in‑place (`-in-place`) mode, match‑only mode for validation.
    
- risks: for Markdown, comby treats files as text, not AST; high risk of multi‑match or mis‑match if patterns are not carefully constrained.
    

## Source 9

- source_name: Obsidian frontmatter tools / bulk-edit utilities
    
- url_or_repo:
    
    - obsidian-metadata[https://github.com/natelandau/obsidian-metadata](https://github.com/natelandau/obsidian-metadata)[[github](https://github.com/natelandau/obsidian-metadata)]
        
    - obsidian-bulk-edit[https://github.com/FrtZgwL/obsidian-bulk-edit](https://github.com/FrtZgwL/obsidian-bulk-edit)[[github](https://github.com/FrtZgwL/obsidian-bulk-edit)]
        
    - YAML Toolkit plugin[https://forum.obsidian.md/t/new-plugin-yaml-toolkit-for-obsidian-batch-manipulate-front-matter-with-conditional-rules/109674](https://forum.obsidian.md/t/new-plugin-yaml-toolkit-for-obsidian-batch-manipulate-front-matter-with-conditional-rules/109674)[[forum.obsidian](https://forum.obsidian.md/t/new-plugin-yaml-toolkit-for-obsidian-batch-manipulate-front-matter-with-conditional-rules/109674)]
        
    - Obsidian Frontmatter Tool GUI[https://forum.obsidian.md/t/obsidian-frontmatter-tool-desktop-gui-for-batch-editing-validation/101709](https://forum.obsidian.md/t/obsidian-frontmatter-tool-desktop-gui-for-batch-editing-validation/101709)[[forum.obsidian](https://forum.obsidian.md/t/obsidian-frontmatter-tool-desktop-gui-for-batch-editing-validation/101709)]
        
- type: scripts/plugins/GUI
    
- freshness: active through 2025–2026.[[github](https://github.com/FrtZgwL/obsidian-bulk-edit)]
    
- evidence_summary: All provide ways to batch manipulate YAML frontmatter across Markdown vaults, using Python scripts or plugin UIs, with preview/dry‑run and conditional rules.[[github](https://github.com/FrtZgwL/obsidian-bulk-edit)]
    
- relevance: Confirm that “frontmatter+CLI” is a common pattern; their approaches can be replicated with yq or a custom Python frontmatter script for non‑Obsidian repos.
    
- copyable_parts: function signature patterns (frontmatter dict + content list → modified tuple), conditional logic concepts, dry‑run/preview workflows.
    
- risks: Obsidian‑specific, some repos unmaintained; not ideal to depend on them directly outside Obsidian.
    

## Source 10

- source_name: General frontmatter libraries & scripts
    
- url_or_repo:
    
    - Ruby/JS/Python frontmatter parsing examples[https://stackoverflow.com/questions/36948807/edit-yaml-frontmatter-in-markdown-file](https://stackoverflow.com/questions/36948807/edit-yaml-frontmatter-in-markdown-file)[[stackoverflow](https://stackoverflow.com/questions/36948807/edit-yaml-frontmatter-in-markdown-file)]
        
    - PowerShell Set-MarkdownFrontMatter.ps1[https://www.powershellgallery.com/packages/PSBlogger/0.2.0/Content/public%5CSet-MarkdownFrontMatter.ps1](https://www.powershellgallery.com/packages/PSBlogger/0.2.0/Content/public%5CSet-MarkdownFrontMatter.ps1)[[powershellgallery](https://www.powershellgallery.com/packages/PSBlogger/0.2.0/Content/public%5CSet-MarkdownFrontMatter.ps1)]
        
- type: utilities/snippets
    
- freshness: mixed; many are older but still functional.
    
- evidence_summary: Show simple patterns: parse frontmatter (YAML), modify fields, write back file; emphasise that full‑file rewrite is typical for frontmatter changes unless you use tools like yq’s `--front-matter=process` to avoid corruption.[[powershellgallery](https://www.powershellgallery.com/packages/PSBlogger/0.2.0/Content/public%5CSet-MarkdownFrontMatter.ps1)]
    
- relevance: Confirms that a tiny custom frontmatter script is viable if yq cannot cover certain edge cases (e.g., non‑YAML metadata).
    
- copyable_parts: regex to isolate frontmatter, YAML.parse + content concat patterns, parameterization of update/replace operations.
    
- risks: many snippets do naive parsing; high silent corruption risk if adopted uncritically.
    

## Source 11

- source_name: markdown-replace-section CLI
    
- url_or_repo: [https://github.com/renke/markdown-replace-section](https://github.com/renke/markdown-replace-section)[[github](https://github.com/renke/markdown-replace-section)]
    
- type: Node CLI (UNMAINTAINED)
    
- freshness: marked unmaintained; last update years ago.[[github](https://github.com/renke/markdown-replace-section)]
    
- evidence_summary: CLI that “replaces everything between the first heading named <heading_name> and the next heading of the same level with content from stdin”; supports a `--not-hungry` option to stop at first heading.[[github](https://github.com/renke/markdown-replace-section)]
    
- relevance: Exactly matches “markdown-section-replacer” concept for simple cases.
    
- copyable_parts: CLI interface design (input_file, heading_name, output_file, content via stdin), notion of level‑scoped section replacement.
    
- risks: unmaintained; no validation or rollback; heading match is name‑only (no uniqueness checks), so ambiguous headings can cause scope creep.
    

## Source 12

- source_name: Git apply docs / CI patterns
    
- url_or_repo:
    
    - git-apply manual[https://git-scm.com/docs/git-apply](https://git-scm.com/docs/git-apply)[[git-scm](https://git-scm.com/docs/git-apply)]
        
    - “git apply command reference” article[https://latchkey.dev/learn/command-reference/git-apply-command-reference](https://latchkey.dev/learn/command-reference/git-apply-command-reference)[[latchkey](https://latchkey.dev/learn/command-reference/git-apply-command-reference)]
        
- type: official docs + reference article
    
- freshness: current Git docs; article updated 2026-06.[[latchkey](https://latchkey.dev/learn/command-reference/git-apply-command-reference)]
    
- evidence_summary: Explain `git apply --check` for validation without changes, `--index` to stage, `--3way` for drifted bases; recommended pattern: run `--check` before applying patches in CI.[[git-scm](https://git-scm.com/docs/git-apply)]
    
- relevance: Strong backing for “git scope validator” and “patch-pack validator/finalizer”; validates using Git’s native diff machinery instead of AI or custom logic.
    
- copyable_parts: `git apply --check patch`, `git apply --index patch` sequences, best practices for fail‑fast CI.
    
- risks: still requires accurate base; if unified diffs are stale, `--check` fails but does not fix them.
    

## Source 13

- source_name: OpenHands path-triggered rules / agent skills authoring
    
- url_or_repo:
    
    - OpenHands Path Rules[https://docs.openhands.dev/overview/skills/path](https://docs.openhands.dev/overview/skills/path)[[docs.openhands](https://docs.openhands.dev/overview/skills/path)]
        
    - Automattic agent skills authoring guide[https://github.com/Automattic/agent-skills/blob/trunk/docs/authoring-guide.md](https://github.com/Automattic/agent-skills/blob/trunk/docs/authoring-guide.md)[[github](https://github.com/Automattic/agent-skills/blob/trunk/docs/authoring-guide.md)]
        
- type: agent frameworks docs
    
- freshness: 2025–2026; active projects.[[github](https://github.com/Automattic/agent-skills/blob/trunk/docs/authoring-guide.md)]
    
- evidence_summary: Show how skills/rules can be auto‑injected based on file paths, ensuring deterministic guidance when specific files are touched; authoring guide emphasises deterministic scripts for detection and validation rather than letting the model improvise.[[github](https://github.com/Automattic/agent-skills/blob/trunk/docs/authoring-guide.md)]
    
- relevance: Reinforces design where Markdown patching is handled by a dedicated skill/CLI per path, not by generic Write/Edit.
    
- copyable_parts: path‑based frontmatter in SKILL.md, “scripts/” helpers for deterministic checks.
    
- risks: frameworks are external; copying patterns is fine, but copying skills wholesale without review can add opaque complexity.
    

## Source 14

- source_name: alirezarezvani/claude-skills collection
    
- url_or_repo: [https://github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)[[github](https://github.com/alirezarezvani/claude-skills)]
    
- type: large skill library
    
- freshness: updated through 2025–2026 with many skills and scripts.[[github](https://github.com/alirezarezvani/claude-skills/wiki)]
    
- evidence_summary: Provides ~180–300+ skills and scripts for Claude Code, emphasizing deterministic scripts for detection/validation and keeping SKILL.md short and procedural; authoring conventions recommend scripts for anything that would otherwise be “guessed.”[[github](https://github.com/alirezarezvani/claude-skills)]
    
- relevance: Good pattern source for structuring your own md‑patcher SKILL, but no single skill appears to implement the full plan/validate/apply/rollback Markdown pipeline.
    
- copyable_parts: skill frontmatter conventions, separation of SKILL.md vs scripts vs references, evaluation scaffolding.
    
- risks: very large repo; copying skills or scripts without review risks bringing in assumptions and security exposures that don’t match your environment.
    

## Source 15

- source_name: MDAST MCP server (mcp-mdast)
    
- url_or_repo: [https://lobehub.com/mcp/mako10k-mcp-mdast](https://lobehub.com/mcp/mako10k-mcp-mdast)[[lobehub](https://lobehub.com/mcp/mako10k-mcp-mdast)]
    
- type: MCP server for Markdown AST
    
- freshness: released late 2025 / early 2026.[[lobehub](https://lobehub.com/mcp/mako10k-mcp-mdast)]
    
- evidence_summary: Provides operations over a Markdown AST via MCP, using selector syntax like `heading[depth="2"]` to select nodes and perform insert/replace; acts as a remote AST store/manipulator rather than plain text edits.[[lobehub](https://lobehub.com/mcp/mako10k-mcp-mdast)]
    
- relevance: Strong candidate for “outside box” design where the agent edits an AST store and a deterministic generator writes Markdown output, decoupling LLM from byte‑level patching.
    
- copyable_parts: selector syntax, “select / insert content” operations, concept of AST‑based modifications over MCP.
    
- risks: new ecosystem; needs evaluation for stability and security; adds network and MCP complexity if adopted.
    

---

## candidate_tools_ranked

Numbers below (evd/imp/rsk/cost) are analytic scores, not from sources (inference).

|rank|name|category|evd|imp|rsk|cost|best_use_case|not_for|copy_or_build_decision|
|---|---|---|---|---|---|---|---|---|---|
|1|yq `--front-matter=process`|deterministic CLI|90|85|20|25|All YAML frontmatter edits (single or batch) in Markdown files.[[blog.omuomugin](https://blog.omuomugin.com/posts/2025-05-07/)]|Non‑YAML frontmatter, binary files|Copy (adopt yq as your frontmatter engine; no custom parser needed).|
|2|remark-cli + mdast-util-heading-range|AST CLI + library|85|90|25|40|Deterministic section replacement under specific headings, with AST validation.[[npmjs](https://www.npmjs.com/package/mdast-util-heading-range)]|Arbitrary regex‑style span replacements, binary content|Build small JS wrappers using these libraries rather than invent a new section replacer.|
|3|git apply `--check` / patch-pack workflow|Git CLI|95|80|15|20|Validating and applying patch packs, ensuring scope and base correctness.[[git-scm](https://git-scm.com/docs/git-apply)][[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]|Direct AI-authored diffs without prior validation|Copy patterns directly; keep git as sole patch validator.|
|4|markdown-patch (library)|Markdown‑aware patch engine|75|70|35|35|Frontmatter and simple heading/block patches when targets are unambiguous.[[github](https://github.com/coddingtonbear/markdown-patch)]|deeply nested headings with ambiguous names|Use selectively or copy ideas; do not depend on it as sole section engine due to known heading bugs.|
|5|markdown-replace-section CLI|section replacer|60|65|50|30|Simple “replace section under heading” operations in scripts.[[github](https://github.com/renke/markdown-replace-section)]|mission‑critical patching; ambiguous headings|Copy interface design; re‑implement in a maintained language or via mdast, not adopt directly.|
|6|comby|structural search/replace CLI|80|60|40|35|Repetitive, pattern‑based rewrites across many Markdown files (e.g., list bullet normalization).[[comby](https://comby.dev/)]|semantics‑sensitive section/frontmatter edits|Use as a helper for content‑blind bulk changes; not core span replacer.|
|7|Claude Code hooks (PreToolUse/PostToolUse)|hook system|90|95|30|30|Enforcing “no Write/Edit/Bash without plan+validator”, blocking unsafe calls, logging tool usage.[[code.claude](https://code.claude.com/docs/en/hooks-guide)]|Deep semantic validation (it only sees tool inputs/outputs)|Copy hook patterns but write your own scripts; do not rely solely on hooks for security.|
|8|SDD Toolkit (sdd-modify)|spec-driven CLI + skills|80|70|35|55|Large, spec‑driven codebase modifications with safety, backups, rollback.[[github](https://github.com/tylerburleigh/claude-sdd-toolkit)]|small, localized Markdown patch tasks|Copy architectural ideas (plan JSON, backup/rollback), not the full toolkit, unless you want SDD.|
|9|MDAST MCP server (mcp-mdast)|AST store/server|70|75|40|60|AST‑based selection/insertion where you want LLM to operate on structure, not text.[[lobehub](https://lobehub.com/mcp/mako10k-mcp-mdast)]|low‑complexity local repos|Consider for a future “AST store” architecture; not required for current patch skill.|
|10|Obsidian REST API PATCH engine|application‑specific REST|75|55|45|50|Learning how structured PATCH formats and document maps are designed.[[community.obsidian](https://community.obsidian.md/plugins/rest-api)]|general repo patching outside Obsidian|Copy schema ideas; do not depend on plugin.|
|11|obsidian-metadata / bulk-edit scripts|batch frontmatter tools|65|55|35|35|Batch frontmatter migrations/cleanup in Obsidian‑like vaults.[[github](https://github.com/natelandau/obsidian-metadata)]|core executor for arbitrary repos|Use patterns (function signature, preview modes); not adopt raw tools.|
|12|alirezarezvani/claude-skills conventions|skill authoring patterns|85|80|30|45|SKILL.md structure, script separation, eval scaffolding for skills.[[github](https://github.com/Automattic/agent-skills/blob/trunk/docs/authoring-guide.md)]|direct Markdown patch implementation (no single skill does it)|Copy conventions to structure your md-patcher SKILL.|
|13|OpenHands path-triggered rules|path-based injection|75|70|35|40|Auto‑injecting patch guidance when certain files are touched.[[docs.openhands](https://docs.openhands.dev/overview/skills/path)]|enforcement of actual writes (needs tool hooks)|Copy concept for path‑scoped skills; actual enforcement lives in hooks/CLI.|

---

## existing_skill_gap_verdict

- complete_package_found: false
    
- closest_existing_package: SDD Toolkit’s `sdd-modify` + its plan/validate/apply/rollback workflow, supplemented by Claude Code hooks for enforcement.[[code.claude](https://code.claude.com/docs/en/hooks-guide)]
    
- missing_capabilities:
    
    - Markdown/frontmatter‑specialized span/section selection (SDD is spec/code‑centric, not Markdown‑centric).[[github](https://github.com/tylerburleigh/claude-sdd-toolkit/blob/main/docs/architecture.md)]
        
    - Tight integration with Claude Code hooks to _force_ use of the SDD CLI for all edits in Markdown files (today SDD is a skill, not a global guard).[[code.claude](https://code.claude.com/docs/en/hooks-guide)]
        
    - Fine‑grained uniqueness semantics for spans (local exact match once, with explicit failure on multi‑match) baked into a CLI rather than delegated to LLM text search.
        
    - Repo‑agnostic support for frontmatter + Markdown sections without assuming Obsidian or a specific vault layout.[[github](https://github.com/coddingtonbear/markdown-patch)]
        
- confidence: high (broad search across Claude Code docs, skills marketplaces, SDD repos, Obsidian/Docusaurus tooling, and AST/patch tools produced many building blocks but no unified “Markdown patching + hooks” package).[[code.claude](https://code.claude.com/docs/en/hooks-guide)]
    

---

## architecture_options

## A: current live-span replacer architecture

- description:  
    AI produces intent description and candidate location; deterministic executor reads live files, selects exact span, validates uniqueness (0/1/>1 matches), applies a once‑only replacement, then produces git diff and runs validators before any commit/push.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/0f7025a3-26fc-4ce4-a80d-045854ab9dfb/AgentModePatchingPromptTemplate.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=jGfysm9XU%2F8nnC6OdhOxNWVwroo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]
    
- files_needed (inference):
    
    - span‑replacer CLI (e.g., Python or shell)
        
    - markdown-section-replacer tool or script
        
    - frontmatter patcher (yq or small script)
        
    - git scope validator script (wrapping `git diff` / `git apply --check`)
        
    - fixtures/assertions runner and patch‑pack finalizer metadata (manifest).
        
- runtime_dependencies: git, yq, language runtime for span/section tooling (likely Python or Node), Claude Code hooks for enforcement.
    
- how_it_blocks AI mistakes:
    
    - LLM never writes bytes directly; it only specifies spans/headings/frontmatter keys, plus desired replacement text.
        
    - CLI ensures exactly one match or fails; multi‑match becomes a blocked state instead of silent corruption.
        
    - git diff + `git apply --check` enforce base correctness and scope; validators (markdownlint, link check) run before commit.[[git-scm](https://git-scm.com/docs/git-apply)]
        
- evd: 80 (backed by your internal process docs and Git practices).[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/7d9395f7-57fd-46cd-9951-be3d18fe92cd/AgentPrompt_v4.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=em2KkOtwMNRqhDGVlG2p3m6nN5o%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]
    
- imp: 90 (removes LLM from byte‑level editing, centralizes validation).
    
- rsk: 30 (custom scripts must be written & maintained; mis‑implementation can introduce silent corruption).
    
- cost: 45 (more pieces than minimal; needs careful design and tests).
    
- finalization_readiness: medium–high; concept is solid, but implementations (local-span-replacer, markdown-section-replacer) should be trimmed and backed by existing libraries where possible to reduce custom logic.
    

## B: markdown-patch/mdpatch-based architecture

- description:  
    Use markdown-patch (or an equivalent) as the primary patch engine: AI or spec produces “patch operations” (frontmatter updates, heading/section inserts/overwrites); executor sends patches to the engine, which applies them structurally to Markdown; git apply and validators guard correctness.[[github](https://github.com/coddingtonbear/obsidian-local-rest-api)]
    
- files_needed:
    
    - CLI wrapper around markdown-patch
        
    - patch spec schema (JSON/YAML)
        
    - integration script with git apply/validators
        
    - thin SKILL.md describing how AI emits patch specs.
        
- runtime_dependencies: Python (markdown-patch), possibly Obsidian‑style wrappers if you reuse their implementation, git, validators.
    
- how_it_blocks AI mistakes:
    
    - patch engine rejects invalid targets (e.g., heading not found) instead of partially rewriting files; frontmatter operations are schema‑aware.[[github](https://github.com/coddingtonbear/markdown-patch)]
        
    - AI is constrained to patch schema; direct Write/Edit is blocked by hooks.
        
- evd: 75 (real‑world usage in Obsidian Local REST API and similar tools).[[community.obsidian](https://community.obsidian.md/plugins/obsidian-local-rest-api)]
    
- imp: 75 (for frontmatter/headings it can replace custom section replacers).
    
- rsk: 40 (known heading bugs for nested sections, plus reliance on a single library’s correctness).[[forum.obsidian](https://forum.obsidian.md/t/patch-content-with-target-type-heading-fails-on-all-h2-headings/114680)]
    
- cost: 50 (setup and possible upstream limitations; patch schemas must be learned).
    
- finalization_readiness: medium; good for frontmatter and simple headings, but you would still need additional mechanisms for nested sections and unique spans, or wrapper code that resolves hierarchical headings.
    

## C: SDD-toolkit + Claude hooks architecture

- description:  
    Treat Markdown modifications as SDD “spec tasks”: AI produces SDD JSON specs; SDD Toolkit runs `sdd-modify` to apply changes via its safe pipeline (backup, dry run, validation, rollback); Claude Code hooks enforce that Markdown files may not be edited except via sdd-modify and related CLI tools.[[github](https://github.com/tylerburleigh/claude-sdd-toolkit)]
    
- files_needed:
    
    - SDD Toolkit configs (.claude/settings.local.json, .claude/sdd_config.json)[[github](https://github.com/tylerburleigh/claude-sdd-toolkit/blob/main/docs/getting-started.md)]
        
    - spec definitions for Markdown tasks
        
    - hook scripts that block Write/Edit/Bash touching Markdown outside sdd-modify.
        
- runtime_dependencies: SDD Python CLI, Claude Code, git, test/validation commands configured per project.
    
- how_it_blocks AI mistakes:
    
    - spec‑first: AI must produce machine‑readable plan; actual modifications are CLI‑driven.
        
    - SDD handles backups/dry‑runs/rollback; hooks ensure only SDD tools perform edits on scoped paths.
        
- evd: 80 (well‑documented architecture; changelog shows active development).[[github](https://github.com/tylerburleigh/claude-sdd-toolkit/blob/main/docs/changelog.md)]
    
- imp: 70 (aligns strongly with your plan/validate/apply/rollback ideal).
    
- rsk: 35 (overkill for pure Markdown docs; misconfiguration may cause complexity rather than safety).
    
- cost: 60 (setup overhead; learning curve; spec discipline required).
    
- finalization_readiness: low–medium for _this_ patching skill specifically; best used as inspiration rather than full adoption unless you want SDD across your whole project.
    

## D: yq/frontmatter-first architecture

- description:  
    Make frontmatter the primary state; treat most Markdown prose as derived. Use yq for all frontmatter mutations (fields, tags, schemas), and generate Markdown sections from frontmatter/state rather than patching prose often; for remaining prose, use minimal span/section replacers.[[recfab](https://recfab.net/blog/2024/06/08/update-note-tags/)]
    
- files_needed:
    
    - frontmatter CLI scripts (yq invocations)
        
    - generator scripts that render Markdown from frontmatter/state (e.g., templates).
        
- runtime_dependencies: yq, language runtime for generators, git.
    
- how_it_blocks AI mistakes:
    
    - drastically reduces direct prose patching; AI changes structured frontmatter, generators produce Markdown.
        
    - frontmatter operations are atomic and audited; templates are static.
        
- evd: 75 (multiple examples of bulk frontmatter edits in real docs/blog/Obsidian workflows).[[forum.obsidian](https://forum.obsidian.md/t/cli-ability-to-manipulate-frontmatter-for-a-document/112457)]
    
- imp: 80 (big potential reduction in patch complexity if your docs content fits the model).
    
- rsk: 30 (requires discipline to keep docs templated; free‑form sections still need safe patching).
    
- cost: 40 (initial migration to frontmatter‑first patterns; template maintenance).
    
- finalization_readiness: medium; promising for some doc types, but not a full replacement for your current patch architecture.
    

## E: no-agent-write architecture (only executor script mutates files)

- description:  
    Disable Write/Edit/MultiEdit for Markdown/config files via Claude Code hooks; allow only a small set of custom tools (span replacer, section replacer, frontmatter patcher, git diff/apply validators) to perform mutations; AI interacts by producing structured “patch plans” consumed by those tools.[[llmversus](https://llmversus.com/claude-code/pre-tool-use)][[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/7d9395f7-57fd-46cd-9951-be3d18fe92cd/AgentPrompt_v4.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=em2KkOtwMNRqhDGVlG2p3m6nN5o%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[code.claude](https://code.claude.com/docs/en/hooks-guide)]
    
- files_needed:
    
    - hook scripts for PreToolUse/PostToolUse to block direct writes and dangerous bash.
        
    - CLI executors: `md-span-replace`, `md-section-replace`, `frontmatter-patch` (yq), `patch-pack-validate`.
        
    - SKILL.md describing plan JSON format and allowed tools.
        
- runtime_dependencies: git, yq, language runtimes for executors, Claude Code hooks.
    
- how_it_blocks AI mistakes:
    
    - direct Write/Edit/MultiEdit on Markdown/config paths is simply impossible; tools enforce path and operation constraints.
        
    - executors implement exact‑match semantics, uniqueness tests, scope filters, and validation, independent of AI reasoning.
        
- evd: 85 (hooks docs and your own agent-mode prompt/process docs already assume executor vs builder separation).[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[code.claude](https://code.claude.com/docs/en/hooks-guide)]
    
- imp: 95 (maximally removes LLM from byte‑level editing; centralizes all mutations in audited scripts).
    
- rsk: 25 (failure modes localised in a small set of scripts; hook bugs are visible via log).
    
- cost: 50 (requires writing and maintaining executors and hooks; but fewer moving parts than patch‑pack + SDD hybrid).
    
- finalization_readiness: high; this is essentially what your current synthesis is converging to, and external evidence supports it strongly.
    

## F: outside-box alternative (AST/DB store)

- description (example):  
    Use an AST‑backed or block‑store (MDAST MCP server, SQLite index, or OKF schema store) as the authoritative representation; AI edits structured entities (nodes, blocks, records) via deterministic operations; a generator writes Markdown views from the store; git diff operates on generated files only.[[github](https://github.com/syntax-tree/mdast)]
    
- files_needed:
    
    - MCP server or service for AST/block storage.
        
    - generator scripts for Markdown.
        
    - minimal patching logic (mostly generation).
        
- runtime_dependencies: AST server, DB, generator runtime, git.
    
- how_it_blocks AI mistakes:
    
    - no direct text patching; AI can only call operations like “update frontmatter field X” or “replace section node Y”; underlying engine ensures structural correctness.
        
    - rollback handled at DB/AST layer.
        
- evd: 60 (MDAST MCP and similar projects are emerging but not yet mainstream for docs‑as‑code pipelines).[[lobehub](https://lobehub.com/mcp/mako10k-mcp-mdast)]
    
- imp: 80 (in principle, it removes nearly all text‑level corruption risk).
    
- rsk: 45 (system complexity, new failure modes in server/DB; may be overkill).
    
- cost: 70 (substantial new infrastructure).
    
- finalization_readiness: low for immediate skill finalization; good long‑term direction if you later decide to re‑platform docs.
    

---

## recommended_final_architecture

## thesis

Use your current live-span deterministic replacement architecture as the core, but simplify and harden it by:

- Making frontmatter patching entirely yq‑based.
    
- Implementing a small, CLI‑level span replacer and section replacer (possibly backed by remark/mdast rather than ad‑hoc regex).
    
- Enforcing a strict “no-agent-write” policy via Claude Code hooks so all Markdown/config mutations go through these tools.
    
- Keeping git diff + `git apply --check` as the only patch-pack validator and source of “proof of change.”[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[git-scm](https://git-scm.com/docs/git-apply)]
    

## minimum_files_to_build (inference)

1. `md-span-replacer` CLI (e.g., Python) – exact once-only replacement of a literal span in a file, with uniqueness checks (0/1/>1 matches).
    
2. `md-section-replacer` CLI – heading‑bounded replacement using remark/mdast or a similar AST tool, with heading name + depth and uniqueness validation.
    
3. `frontmatter-patcher` script – thin wrapper around yq `--front-matter=process` to apply specific JSON/YAML operations per file.
    
4. `patch-pack-validator` script – wraps `git diff`, `git apply --check`, and scope checks, producing a manifest and optionally a report (very similar to your existing patch-pack metadata schema).[[latchkey](https://latchkey.dev/learn/command-reference/git-apply-command-reference)][[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[git-scm](https://git-scm.com/docs/git-apply)]
    
5. `claude-code-hooks` directory – PreToolUse/PostToolUse scripts that:
    
    - Block Write/Edit/MultiEdit/Bash on Markdown/config paths unless the tool is one of the allowed CLIs.
        
    - Optionally require a `plan.json` path argument or environment variable indicating a validated plan ID.
        

## existing_code_to_copy

- From internal docs:
    
    - AgentMode-GitNative-PatchPack-Process.okf.md for patch-pack phases, manifest structure, and validation sequence.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]
        
    - AgentPrompt_v4.md for the executor vs thinker role clarity, and the idea that “executor must not think; must run script.”[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/7d9395f7-57fd-46cd-9951-be3d18fe92cd/AgentPrompt_v4.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=em2KkOtwMNRqhDGVlG2p3m6nN5o%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]
        
    - AgentModePatchingPromptTemplate.md for templated fields like environment mode selection, executor gate, patch-pack vs direct edit, validation ledger, and final report schema.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/0f7025a3-26fc-4ce4-a80d-045854ab9dfb/AgentModePatchingPromptTemplate.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=jGfysm9XU%2F8nnC6OdhOxNWVwroo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]
        
- From external tools:
    
    - yq frontmatter patterns for in‑place updates and bulk operations.[[haseebmajid](https://haseebmajid.dev/posts/2022-11-17-til-you-can-use-yq-to-mass-edit-markdown-files/)]
        
    - remark/mdast heading-range patterns for section replacement.[[npmjs](https://www.npmjs.com/package/mdast-util-heading-range)]
        
    - git apply `--check` usage and CI patterns.[[git-scm](https://git-scm.com/docs/git-apply)]
        
    - Claude Code PreToolUse hook skeletons for Write/Bash, including parsing `CLAUDE_TOOL_INPUT` JSON.[[prg](https://prg.sh/notes/Claude-Code-Hooks)]
        

## custom_code_needed

- A small “local-span-replacer” script:
    
    - Input: file path, exact search string, replacement string, optional match index or uniqueness mode.
        
    - Behavior:
        
        - Count occurrences.
            
        - If 0 → fail clearly (no corruption).
            
        - If >1 → fail or require explicit index; no multi‑match replacement by default.
            
        - If 1 → replace once, write file, and optionally output diff to stdout.
            
- A section replacer using AST:
    
    - Use remark/mdast; take heading text + level; validate uniqueness; replace the section’s content with new Markdown.
        
    - Guarantee no edits outside the section, and no multi‑section matches.
        
- A thin patch-pack validator/finalizer:
    
    - Parse patch files; run `git apply --check` individually and cumulatively; check `git diff --name-only` equals target files; run linting; produce manifest & report similar to your current OKF schemas.[[latchkey](https://latchkey.dev/learn/command-reference/git-apply-command-reference)][[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[git-scm](https://git-scm.com/docs/git-apply)]
        

## hook_policy

- PreToolUse:
    
    - Block all Write/Edit/MultiEdit tool calls whose paths match Markdown/config globs unless the tool is your patch CLI or an approved generator.[[llmversus](https://llmversus.com/claude-code/pre-tool-use)]
        
    - Block Bash commands containing direct editors for Markdown files (e.g., `sed -i` on `.md`, `rm` on doc folders) and any git commands that apply patches outside the patch-pack validator script.
        
    - Optionally require a “validated plan” marker (e.g., presence of plan.json path in tool input) before allowing patch CLIs.
        
- PostToolUse:
    
    - Inspect outputs from patch CLIs; run quick checks on changed files (e.g., frontmatter still parseable, Markdown still valid via remark lint).[[code.claude](https://code.claude.com/docs/en/best-practices)]
        
    - Log each mutation to an audit ledger for traceability.
        

## script_policy

- All scripts must:
    
    - Be idempotent at the level of “re‑running with same inputs yields same outputs.”
        
    - Fail loud on ambiguity (multi‑match spans, multiple headings matching the same name).
        
    - Avoid full‑file rewrites except where absolutely necessary (e.g., generator outputs).
        
    - Be small enough to audit easily; no multi‑thousand‑line helpers.
        

## validation_policy

- Pre‑commit:
    
    - `git apply --check` for patch packs prior to application.[[git-scm](https://git-scm.com/docs/git-apply)]
        
    - Markdown lint (remark-lint or markdownlint-cli) on changed files.[[unifiedjs](https://unifiedjs.com/explore/package/remark-cli/)]
        
    - Markdown link check / frontmatter schema validators where relevant.[[blog.omuomugin](https://blog.omuomugin.com/posts/2025-05-07/)]
        
- Scope:
    
    - After applying patch packs in a staging area: `git diff --name-only` must equal allowed targets only.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[latchkey](https://latchkey.dev/learn/command-reference/git-apply-command-reference)]
        
    - Span/section scripts must report exact lines/regions changed for human review.
        

## rollback_policy

- For span/section/frontmatter CLIs:
    
    - Always create a backup copy (e.g., file.md.bak) or rely on git (commit before patch, revert via `git checkout` on failure).[[git-scm](https://git-scm.com/docs/git-apply)]
        
- For patch packs:
    
    - Keep patch files and manifest separate from commits; rollback by `git checkout` to pre‑patch commit or by `git apply -R patch`.
        
- Hooks:
    
    - Never attempt automatic rollback of arbitrary tool operations; restrict potential damage by whitelisting only patch CLIs and safe tools in hooks.
        

---

## kill_list

(What to remove or de‑emphasize from the current plan.)

1. **Over-reliance on custom “markdown-section-replacer” if it’s purely regex-based.**
    
    - Replace with remark/mdast-based section replacer or a small AST script; regex section replacement is hard to make safe for nested headings.[[npmjs](https://www.npmjs.com/package/mdast-util-heading-range)]
        
2. **Any design that treats AI-authored unified diffs as a primary path.**
    
    - Keep AI-authored diffs strictly as a “rank 5 fallback” as you specified; the core must be live-span selection + deterministic diff via git.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)][[git-scm](https://git-scm.com/docs/git-apply)]
        
3. **Content-blind generated scripts that try to capture many repetitive edits without AST or uniqueness checks.**
    
    - Use comby or yq for clearly patternised or frontmatter-centric edits; do not maintain a large custom library of regex span scripts.[[comby](https://comby.dev/)]
        
4. **Large numbers of patch-pack variants and multiple overlapping validators.**
    
    - Your internal docs already converge on a minimal patch-pack flow (one patch per file, git apply --check, manifest).[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEQLHNM7MV&Signature=RwQm3hWoAPYaOONt3BgGgAV4RyU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFsxmohNjgVCWplmhb%2FvDfvPnZBVuRXNmHoczHTKYg0EAiA27ZnfYjw8vTs22gAlPjqozk3BmKKV0ISsLE1%2B8P1nTSr8BAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMhppIapwPUWL2VefoKtAEt3PTTnT0wdbqhalheUF%2F0dZjPsUT9aQo3K%2FBXSIm0aq1bOlr%2BFQEmiBVQyTbHHd7dLtnr84AtgFIHuJ6lUqSrjn06PH6h%2FPCUQxZQGvEd5PIbdhLh%2BH%2B27DuE3cpGtmqYhh6XdjoP%2Bn7cDfA39RvFu5Q932NLSaeU61rtEeKz%2Flzjq%2F3YyZDEqhoFj2uwkatFkbqZZdITNeLviJGBAo4udIx9C6dNm0I6GI08olBHP0fXvq3GduGtwbcot3Gjf75vtBFoAWSjYKVe20eAIZKt6x8xnCYrlbiAhGcFbI1tjlclnsyn8%2Fp1o4BKsrNPSP%2Fm%2Fn9yL2jLlo%2BrMAj%2B7kpzw9Q38Co5S%2Fknrp6izv4TYaRexxA7N7CKtVcqv1XciRkzZ9tvdmHXYh%2BnZQHu5K2%2F%2B0Dejpugl12%2BT1BMirB2t5lm%2F5JuBe56flWtAIFeBoZ1oq%2B5wcTOmizjIh%2BZYjlcBjn3Ta4J0vqz7hN%2B9TuE%2FKXwy%2B23ro93q5kDcNetkm6zV%2F2kzWzFw6R4BemsUgrXIBvOU3rNrjpOe%2BH70quSGo3dCh1S4h5WkG4siCz5CDloIrU1g7Jo7C8jXJzFaungrW5qW%2FxJHP9TmaS4daNTanOesNT4MJDOWaXXh1xbVgO7w9fqhOxoIeN1ScSmx6grwcamni%2FtktW9GsG%2FM7moxM4aBXwVY0wWLAibexda6Ksd0TyUg6r7R0TMEQGZwm%2F2nU8JlyrQ43JVI47lK74sCm5aFh5WanSS8ATxef4fhcqwH9ohXL%2BC7yGCeXX73T0%2BTCc9r7SBjqZAR51RmYLPh96SFiv2qhrZYtOWszYlvFzNqZqmj7fmMqYBVOyCsWvRXvO1ZhrMSmuzRy%2F0vlW9rY3N5ZHW8F3zRAN9wyNyBEkfXJX95WQLM79q0hvER4NL8OkCRNQ5ZZ2xDILnt4OI64iZbDc9YLFT%2F%2BrRnI%2F%2F7AQEDxjIHujdzPc8C9WSZgchIaqLIpmf8i3XnMDANm9vqg0sA%3D%3D&Expires=1783613679)]
        
    - Avoid adding extra phases beyond what git + linting + marker checks provide.
        
5. **Any hooks design that tries to introspect diffs and semantics in shell in a brittle way.**
    
    - Hooks should focus on gating tool usage and path patterns, not reimplement diff logic; keep semantics in your CLIs and tests.[[blakecrosley](https://blakecrosley.com/fr/blog/claude-code-hooks-explained)]
        
6. **Attempting to fold SDD Toolkit wholesale into the Markdown patching skill.**
    
    - Copy the plan/validate/apply/rollback concepts, but do not import the full SDD spec machinery unless you’re ready to reorient your whole repo around it.[[github](https://github.com/tylerburleigh/claude-sdd-toolkit)]
        

---

## open_research

1. **Span-replacer implementation strategy.**
    
    - Whether to back `md-span-replacer` with simple literal search or a micro‑AST representing inline tokens, to detect and avoid matches inside code blocks or links (not yet fully resolved).
        
2. **Section uniqueness semantics.**
    
    - Best way to express “candidate location” for heading ranges: heading text + depth, or a hierarchical path (like markdown-patch’s qualified paths).
        
3. **Path-scoped skills vs global hooks.**
    
    - Whether to introduce SKILL-level path rules (similar to OpenHands) inside Claude Code for additional guidance, beyond hooks and CLIs.[][]
        
4. **AST/DB store viability.**
    
    - Long-term cost/benefit of moving to MDAST MCP or a local AST store for docs; this could eventually make span/section replaces far simpler but adds infrastructure.[]
        
5. **Formal frontmatter schema.**
    
    - For your docs, defining JSON Schema/YAML schema for frontmatter and integrating schema validation into the patch pipeline (research needed on best tooling and performance).
        

---

## finalization_prompt

Use this deterministic prompt (or equivalent spec) for the next AI that will build the actual skill/process:

> TITLE Markdown Patch Skill – Deterministic Live-Span Replacement Only
> 
> ROLE You are designing and implementing a small set of CLI tools and Claude Code hooks. Your goal is to make Markdown and frontmatter edits deterministic, safe, and cheap.
> 
> REQUIRED OUTPUT
> 
> 1. `md-span-replacer` CLI:
>     
>     - Inputs: file path, exact search string, replacement string, optional match index or uniqueness mode.
>         
>     - Behavior: count matches; if 0 or >1 (without explicit index) fail loudly; if 1, replace once and exit 0.
>         
>     - No regex by default; treat search string literally.
>         
>     
> 2. `md-section-replacer` CLI backed by remark/mdast:
>     
>     - Inputs: file path, heading text, heading depth, replacement Markdown.
>         
>     - Behavior: find exactly one section; replace its content only; fail on 0 or >1 matches.
>         
>     
> 3. `frontmatter-patcher` CLI using yq `--front-matter=process`:
>     
>     - Inputs: file path, yq expression (read-only from config), optional dry-run flag.
>         
>     - Behavior: apply expression in place; ensure YAML still parses.
>         
>     
> 4. `patch-pack-validator` script:
>     
>     - Inputs: list of patch files and expected target files.
>         
>     - Behavior: run `git apply --check` per patch and cumulatively; check `git diff --name-only` equals target files; run markdownlint and link checks on changed files; output manifest + report.
>         
>     
> 5. Claude Code hooks configuration:
>     
>     - PreToolUse: block Write/Edit/MultiEdit/Bash for Markdown/config paths unless tool is one of the CLIs above; optionally require plan.json or plan ID; log all tool calls.
>         
>     - PostToolUse: run quick checks on changed files (frontmatter parse, markdownlint) and log outcomes.
>         
>     
> 
> USE ONLY THESE DEPENDENCIES git, yq, remark/mdast, Python or Node, and standard shell. Do not introduce additional heavy frameworks.
> 
> GUARANTEES TO ENFORCE
> 
> - No full-file rewrites unless explicitly documented and gated.
>     
> - No multi-match replacements without explicit index.
>     
> - No edits outside declared target scope.
>     
> - No patch application before validation (`git apply --check` must succeed first).
>     
> - LLM never calls Write/Edit/MultiEdit directly for Markdown/config paths.
>     

This keeps the next step tightly focused on implementing the minimal, deterministic tooling implied by the research above, without reopening broad architecture questions.