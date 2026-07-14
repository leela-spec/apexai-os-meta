# Apex KB Final Design Deep Research — Start Here

## Mission

This package prepares one evidence-grounded Deep Research prompt and one coherent research run to define the final Apex KB architecture and detailed implementation guidance. It does not implement, patch, commit, or execute Apex KB.

The locked product is one final multifunctional Apex KB architecture that:

> Deterministically maps the complete configured corpus, preserves durable concept-to-source intelligence, and uses LLM judgment to compile Macro, Meso, and Micro knowledge that tells future AIs which files cover each concept, what every relevant file contributes, how the sources relate over time, and where the evidence lives.

The source map and source atlas are durable parts of the product, not disposable preprocessing. The compiled layer must save future AIs more work than reading the source set again. A wiki that merely rewrites a few files, lists reopen triggers, satisfies headings, or loses the documentary map has failed.

Configuration may alter execution scope—such as file formats, source priorities, topic coverage, or semantic depth—but it may not fragment the architecture into incomplete maturity versions.

## Package map

| File | Purpose |
|---|---|
| `01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md` | Evidence-backed implementation snapshot, known failures, and unresolved target mismatches. |
| `02-LIFECYCLE-COMPONENT-VALUE-MAP.md` | Seed component inventory that Deep Research must verify, correct, expand, rescore on 1–100 dimensions, and regroup. |
| `03-ARTIFACT-HANDOFF-TEMPLATES.md` | Illustrative research interfaces and value tests, not finalized schemas or contracts. |
| `04-Apex-KB-Current-Research-Index.md` | Human source-routing authority with repository identity, access fallbacks, shared sources, and module bundles. |
| `05-Apex_KB_Current_Research_Index.machine-readable.yaml.md` | Machine-readable equivalent of file `04`; both indexes must express the same routing logic. |
| `06-LLM-WIKI-REPOSITORY-GUIDE.md` | Recurring module-level LLM-Wiki evidence and its relationship to Claude skill/orchestration micro-design guidance. |
| `07-DEEP-RESEARCH-PROMPT-PACKET.md` | Canonical executable Deep Research prompt. Files `00`–`06` support it and may not contradict it. |

## Repository identity, source access, and evidence boundary

```yaml
repository_owner: leela-spec
repository_name: apexai-os-meta
repository_full_name: leela-spec/apexai-os-meta
branch: main
package_root: FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch
path_style: repository_relative
```

After this identity block, use repository-relative paths only. Do not introduce local-drive paths or local-checkout assumptions.

Resolve the current `main` commit at research start when repository access works. A commit recorded inside this package is an implementation snapshot, not permanent current truth.

Use the first reliable source route:

1. enabled GitHub app or connector;
2. public GitHub pages on `main`;
3. raw GitHub files on `main`;
4. uploaded Project Sources containing the package and selected repository evidence.

If all repository routes fail, continue in architecture-research mode with the uploaded package, self-created research, LLM-Wiki evidence, Claude skill/orchestration evidence, and current primary web sources. Mark current Apex implementation claims and mismatch scores as `unverified`; never fabricate them or lower the product target.

This package separates these classes of truth:

1. **Operator target** — binding product intent.
2. **Current implementation fact** — verified from current `main`, or explicitly labeled Project Source snapshot evidence.
3. **Existing Apex research intent** — decisions and hypotheses from indexed research files.
4. **LLM-Wiki blueprint evidence** — product, workflow, script, and data-layout mechanisms.
5. **Claude skill/orchestration design evidence** — package, workflow, agent, script, hook, loading, and micro file-creation patterns.
6. **External primary evidence** — current official documentation and primary repositories.
7. **Inference and recommendation** — explicitly labeled synthesis.

Repository-relative paths are stable provenance identities, not required physical wrapper directories in Google Drive or Project Sources. A source may be supplied as:

- the `KnowledgeBase` Drive folder, including `ApexKBFinalDesignDeepResearch`;
- the standalone `apex-kb` Drive folder;
- the standalone `claude-code-orchestration-design` Drive folder;
- the three standalone LLM-Wiki Drive folders (`llm-wiki`, `llm-wiki-main`, `llm-wiki-skill-main`);
- uploaded Project Sources containing Git snapshots or missing implementation files;
- an explicitly authorized GitHub read for a specific unresolved implementation fact.

Do not require a physical `apexai-os-meta` folder or a physical `source-knowledge` folder in the source-access surface. Preserve the inferred repository-relative identity when reliable, while recording the representation actually read.

The old project indexes are historical evidence. Files `04` and `05` are the current routing authority and must remain synchronized.

## Explicit exclusions

Do not use either directory as design authority or ordinary Deep Research input:

- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Failed_Prompts/`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/FailedKBCreation/`

They remain available only for a separately requested failure-history investigation. They are absent from both new indexes.

Leela is evidence that the lifecycle failed in practice, not the subject of this research. Use the prior execution audit only to test whether a proposed Apex design would have prevented shallow compilation.

## Required one-run research flow

1. Perform the small source-access probe defined in file `07` and select an evidence mode.
2. Read this package in numeric order.
3. Produce the Target Lock as the first substantive research output.
4. Verify, correct, expand, rescore, and regroup file `02`; do not treat its existing map as final.
5. Rank research groups by current mismatch × achievable value × downstream leverage.
6. Research each group inside the same run using only shared authority sources and the focused module bundle from files `04` and `05`.
7. Consult relevant LLM-Wiki evidence for every module.
8. Consult relevant Claude skill/orchestration design evidence for every micro file, script, workflow, template, hook, agent, or browser-handoff recommendation.
9. Use current primary web sources when unstable external facts materially affect a decision.
10. Complete the run without operator approval pauses; operator consultation about execution profiles happens after the report and before implementation.

## Non-negotiable design tests

The final design must make all of these true:

- Every in-scope file is inventoried or explicitly excluded with a reason.
- Topic matching exposes inspectable filename, path, title, heading, body, link, duplicate, and date/version signals rather than one opaque hit count.
- No top-N truncation hides the authoritative candidate set.
- Deterministic signals guide reading but never declare semantic authority.
- The LLM dispositions every candidate for a concept: core evidence, contextual, historical, prototype, duplicate, superseded, incidental, unreadable, or irrelevant.
- Every core/current source is read completely; targeted reading has exact section coverage and a reason.
- The concept dossier answers important questions at Macro, Meso, and Micro levels.
- A source atlas gives every candidate file an individual snapshot, value assessment, freshness/authority assessment, relationships, and evidence pointers.
- One source analysis can be reused by content hash across topics.
- Fresh-context page-only and claim-entailment evaluation is required before semantic completion.
- Retrieval is built from accepted compiled knowledge and cannot make shallow pages valuable.
- The ordinary LLM route is short enough that instructions do not consume the context needed for source reading and file creation.
- Graph, UI, vector, parser, extraction, and publishing capabilities receive evidence-based `configurable`, `reject`, or `requires_evidence_probe` dispositions. Complexity alone is not grounds for architectural omission.

## Required Deep Research outcome

The run must return a decision-complete design and implementation plan, not another general research summary. It must state exactly what to keep, change, add, merge, remove, make configurable, reject for insufficient value, or subject to a named evidence probe. It must provide detailed module and file/script creation guidance without writing patches, finished scripts, complete replacement files, or falsely finalized contracts.
