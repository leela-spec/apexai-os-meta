# Apex KB Final Design Deep Research — Start Here

## Mission

This package prepares one evidence-grounded Deep Research run to define the final Apex KB lifecycle. It does not implement or patch Apex KB.

The locked product is:

> Deterministically map the complete in-scope corpus, then use LLM judgment to compile durable concept knowledge that explains the concept at Macro, Meso, and Micro levels and tells future AIs exactly which source files cover it, what each file contributes, how current or stale it is, and where the evidence lives.

The compiled layer must save future AIs more work than reading the source set again. A wiki that merely rewrites a few files, lists reopen triggers, or satisfies headings has failed.

## Package map

| File | Purpose |
|---|---|
| `01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md` | Current implementation versus intended value, including the latest remote semantic changes. |
| `02-LIFECYCLE-COMPONENT-VALUE-MAP.md` | Every material lifecycle component, tool, script, LLM instruction, handoff, cost, value, and decision question. |
| `03-ARTIFACT-HANDOFF-TEMPLATES.md` | Rough schemas and examples for the files each stage should create. |
| `04-Apex-KB-Current-Research-Index.md` | Human reading order with current repository-relative paths and source roles. |
| `05-Apex_KB_Current_Research_Index.machine-readable.yaml.md` | Machine-readable equivalent used for routing and validation. |
| `06-LLM-WIKI-REPOSITORY-GUIDE.md` | What each of the three LLM-Wiki sources actually contributes, including scripts and missing capabilities. |
| `07-DEEP-RESEARCH-PROMPT-PACKET.md` | Provider-targeted prompt packet and clean copy-paste ChatGPT Deep Research prompt. |

## Evidence boundary

This package separates four classes of truth:

1. **Operator target** — the product definition above and the requirement for whole-corpus concept/source intelligence.
2. **Current implementation** — repository `origin/main` at commit `d72f07f7b598` (`Enforce semantic value in Apex KB compilation`).
3. **Research intent** — the moved research files under `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/`.
4. **Blueprint evidence** — the three local LLM-Wiki repositories under `source-knowledge/ProjectRepos/`.

The old project indexes are historical evidence. For this run, files `04` and `05` are the routing authority because they use the current folder layout and exclude failed prompt material.

## Explicit exclusions

Do not use either directory as design authority or ordinary Deep Research input:

- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Failed_Prompts/`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/FailedKBCreation/`

They remain available only for a separately requested failure-history investigation. They are absent from both new indexes.

Leela is evidence that the lifecycle failed in practice, not the subject of this research. Use the prior execution audit only to test whether a proposed Apex design would have prevented shallow compilation.

## Required reading flow

1. Read this package in numeric order.
2. Deep-read the two P0 decision documents named in file `04`.
3. Inspect the current Apex KB skill and runtime on the current main branch.
4. Read the deterministic/parser/graph and LLM-Wiki source spine.
5. Read retrieval research only when deciding the downstream retrieval contract.
6. Use targeted reads for alternatives; do not reread every historical research output equally.
7. Validate unstable external tool claims against primary sources only.

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
- Optional graph, UI, vector, and heavy parser systems enter only when measured need justifies their setup and maintenance cost.

## Required Deep Research outcome

The run must return a decision-complete design and implementation plan, not another general research summary. It must state exactly what to keep, change, add, simplify, defer, or remove in the current Apex KB package and runtime, with artifact contracts and tests sufficient for implementation.
