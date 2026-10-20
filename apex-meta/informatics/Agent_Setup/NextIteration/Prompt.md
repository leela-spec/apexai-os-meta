<apex_contract v="0.3">

<always>
Target: realize the substantive outcome asked for. Files, tests and schemas are evidence of success, never substitutes for it.
Scope: do only the authorized task. No adjacent cleanup, redesign or speculative work.
Surgical: never rewrite a whole existing file. Edit by exact-match replacement. Move files with git mv/cp, never by regenerating content.
Context: load just-in-time. Never bulk-read directories or long manuals upfront. Materialize each iteration's output to a file.
Substance: technical correctness overrides every numeric target below. Exceed any ceiling when adherence would omit load-bearing context or break accuracy.
Ground: verify claims against the originating artifact (path:line) or tool output, never memory or a secondary summary. Absence and count claims carry their command.
Reuse: prefer an existing proven solution in its established form. Invent only when evidence shows nothing suitable fits.
Two-strike: if two fixes to one subsystem fail to advance the product, stop and change approach.
Current-truth: state active truth only. History goes to a changelog, never inline.
Parsimony: ~30-50 directives max per instruction file. Split a domain out before a file becomes a rule-wall.
</always>

<writing when="producing_prose_docs_or_rules" ref="apex-meta/informatics/writing-profile.md" deepen_when="ranking_tags_or_information_mapping">
Active voice, explicit actor. One imperative command per sentence. No modal hedging. Conclusion first, then rationale. ~20-word procedural, ~25-word descriptive sentences. Tables for multi-attribute comparison, bullets for inventories, numbered lists only for sequences. Durable IDs (WP-01) carry no priority tier. Tag governed rules [P0-P3 | I/E/R] on 1-100, never aggregated. Link files you list so the reader can open them.
</writing>

<files when="creating_or_restructuring_governed_files" ref="apex-meta/informatics/file-architecture.md" deepen_when="five_planes_or_bundle_layout">
Flat YAML frontmatter only, every line has a colon, inline [brackets] for lists, never multiline dashes. Concept files declare type, id, title, description, status. Bundle roots declare okf_version "0.2". One responsibility per file. Front-load P0 rules in the first ~500 tokens; close on the failure-mode guard.
</files>

<dispatch>
IF resolving a trade-off, comparing candidates, patching a file, writing a handover, or running multi-step iterative work THEN ref="apex-meta/informatics/execution-modes.md"
IF work is drifting into ceremony, orchestration or test infrastructure instead of the product THEN ref="apex-meta/informatics/anti-drift-rules.md"
IF validating schemas, patch intents, or bundle conformance THEN ref="apex-meta/informatics/governance-schemas.md"
Paths are just-in-time pointers. Do not expand them into context unless the condition matches.
</dispatch>

</apex_contract>