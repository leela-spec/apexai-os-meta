# Apex KB Current Research Reading Index

## Path convention and authority

All paths below are repository-relative to `apexai-os-meta`. This makes the same route usable from:

- local checkout: prefix `C:/GitDev/apexai-os-meta/`;
- Git connector: open the repository path on `main`;
- GitHub/online: append the path to the repository branch URL.

The two primary design sources are research decisions, not proof of current implementation. Current implementation truth comes from the live skill and scripts on the branch being evaluated.

This index replaces the old reading route for the final-design Deep Research run. It excludes `Failed_Prompts/`, `FailedKBCreation/`, prompt-only predecessors, and prior failed plan outputs.

## Priority model

| Priority | Read mode | Meaning |
|---|---|---|
| P0 | complete, first | Binding operator vision/decision or current implementation truth. |
| P1 | complete | Strong executed research or direct blueprint implementation evidence. |
| P2 | targeted | Needed for one design decision; read relevant named sections. |
| P3 | reference only | Older/superseded research useful for provenance or alternatives. |
| Excluded | do not read | Failed prompts, failed creation transcripts, prompt-only predecessors, and superseded draft plans. |

## P0 — read completely first

| Order | Path | What value it contains | What not to assume |
|---:|---|---|---|
| 1 | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex Phase 0 Corpus Intelligence Implementation Decision.md` | Intended Phase 0 product, V1/V1.5 artifacts, parser boundary, navigation report, acceptance criteria. | Some target paths and exact artifacts predate current runtime; reconcile rather than copy. |
| 2 | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex KB × Apex Orchestration Integration Map.md` | Macro/Meso/Micro ownership, end-to-end handoffs, tool options, token-efficiency rationale. | It explicitly lacked live-repo access; all implementation claims need current verification. |
| 3 | `.claude/skills/apex-kb/SKILL.md` | Current operational entrypoint, routes, states, target-query and semantic acceptance rules. | Use current `main`, not the local checkout if it is behind. |
| 4 | `apex-meta/scripts/apex_kb.py` | Current deterministic lifecycle, Phase 0 ranking, validation, status, and postflight behavior. | Contract prose does not override actual code behavior. |
| 5 | `.claude/skills/apex-kb/references/semantic-value-contract.md` | Latest semantic value and completion rules added at `d72f07f7b598`. | It closes shallow stopping but not exhaustive corpus mapping by itself. |
| 6 | `.claude/skills/apex-kb/templates/ingest-analysis-template.md` and `.claude/skills/apex-kb/templates/wiki-page-templates.md` | Current authored artifacts and instruction burden. | Required sections are not proof that resulting pages are valuable. |

## P1 — executed research and direct blueprint evidence

| Order | Path | Contribution to final design | Required extraction |
|---:|---|---|---|
| 7 | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/APEX KB — LLM-Wiki Blueprint Capability Map.md` | File-by-file comparison of two operational LLM-Wiki packages and copy/adapt/omit decisions. | Blueprint operations, scripts, data layout, semantic capabilities, and missing files. |
| 8 | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/markdown-parser-spike-report.md` | Executed parser comparison and output fields. | Python state-machine strategy, section pointers, parser warnings, MDX/PDF failure cases. |
| 9 | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Pre-LLMToolStack.md` | Small deterministic tool stack and token-saving rationale. | Tool value table plus the caveat that its runtime was not the operator's Windows machine. |
| 10 | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Apex Link Graph and Process-Flow Representability Audit.md` | Evidence that Apex graph signals are path/YAML/process edges, not mainly Markdown links. | Edge types, hub files, deterministic/semantic boundary, V1.5 cost/value. |
| 11 | `source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md` | Original product vision: persistent compounding wiki, one source updating many pages, index-first query, lint, saved synthesis. | The actual value proposition, not implementation detail. |
| 12 | `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/SKILL.md` | Operational skill routing, proactive index-first use, scripts, two-phase ingest, hash/idempotency. | Control flow and progressive disclosure. |
| 13 | `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/workflows/ingest.md` | Detailed Phase 1/Phase 2 source-to-many-pages process and interruption handling. | Source hashing, context read, extraction, contradiction, crosslink, index/manifest/sentinel updates. |
| 14 | `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/workflows/query.md` | Concrete index-first retrieval and save-synthesis loop. | How 3–5 pages are selected and how gaps/contradictions are reported. |
| 15 | `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md` | Typed concept/entity/summary tree, compile/ingest/query/lint/audit operations, human feedback surface. | Hierarchical page topology, source summaries, incremental operations, audit loop. |
| 16 | `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/article-guide.md` | Concrete concept/entity/summary structures and crosslink/contradiction guidance. | Keep dense-page and split heuristics; do not turn word counts into semantic gates. |
| 17 | `apex-meta/scripts/apex_kb_retrieval.py` and `.claude/skills/apex-kb/references/retrieval-contract.md` | Current chunking, FTS5 probe, lexical fallback, stale detection, query packets. | Downstream contract and why retrieval cannot compensate for shallow compilation. |

## P2 — targeted design decisions

| Path | Read when | Relevant sections/value | Caveat |
|---|---|---|---|
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Pre-LLM Tool Stack Installability and Value Audit.md` | Comparing parser/search/tool dependencies. | Ranked tools, install/runtime cost, keep/test/reject. | Contains task/prompt material mixed with results. Use results only. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/Pre-LLMCorbusMechanisms_GPT.md` | Checking broader real-world preprocessing options. | Static-site, AST, graph, link checker, search mechanisms. | Broad option catalog; later decisions supersede its defaults. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/process-flow-graph-audit.md` | Defining graph output schema. | Compact edge policy and process-flow examples. | Largely overlaps the full graph audit. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/link-graph.sample.json` | Designing graph fixtures/interfaces. | Concrete node/edge record examples. | Sample, not exhaustive corpus evidence. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/graph-summary.md` | Quick graph orientation. | Hubs, weak spots, output set. | Summary only. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_GPTv2.md` | Validating retrieval mechanics and token layering. | FTS5 probe, BM25 vector, snippets, frontmatter, stale policy, token cost by layer. | Several external claims are dated; revalidate only if material. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_Specia_CC.md` | Choosing YAML/frontmatter parser. | AI-injected stdlib-only restriction and parser options. | Treat library popularity claims as time-sensitive. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/DR_Apex KB  QueryRetrieval Integration_Final Patch Pack.md` | Comparing current retrieval implementation with the prior patch design. | Retrieval schema, command contract, query packet, validation risks. | Patch pack predated current implementation; never apply directly. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/FB_DR_RetrievalINtegration_Claude.md` | Auditing patch-pack collision/assumption risks. | Anchor and interface criticism. | Feedback snapshot, not current authority. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Updates_apex-kb.md` | Understanding the earlier Apex KB baseline and drift history. | Scaffold, two-phase ingest, query/lint/audit, deterministic/semantic split. | Snapshot contains stale implementation claims and conversational contamination. |
| `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/workflows/lint.md` | Designing cheap versus semantic health checks. | Quick deterministic lint and full semantic review split. | Full semantic lint over an entire large wiki may be too expensive. |
| `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/WIKI_SCHEMA.md` | Comparing page/index/frontmatter contracts. | Page types, index fields, contradictions, health categories. | Flat namespace and bilingual requirements are blueprint-specific. |
| `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/schema-guide.md` | Designing short startup/schema guidance. | Scope, naming, current articles, open questions, research gaps. | An always-loaded `CLAUDE.md` is not automatically appropriate for Apex KB. |
| `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/scripts/lint_wiki.py` | Reusing deterministic checks. | Dead links, orphans, index omissions, audit shape/targets. | Adapt interfaces; do not copy parser assumptions blindly. |
| `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/scripts/scaffold.py` | Comparing scaffold simplicity. | Small stdlib tree/bootstrap script. | Current Apex scaffold already exists. |

## P3 — provenance and alternative history only

These files are useful only when a specific decision needs history. They should not consume the initial Deep Research context.

| Path | Preserved value | Why lower priority |
|---|---|---|
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex_KB_Project_Resource_Index.machine-readable.yaml.md` | Old 38-file routing model, risks, and supersession concepts. | Paths and priorities predate the folder cleanup; replaced by this index. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex_KB_Project_Resource_Machine_Readable_Knowledge_Index.md` | Detailed schema for per-file authority, role, freshness, risks, and relationships. | Representation of the old index; use its schema ideas, not its paths as current truth. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/FBClaude4GPT_KBSkillthroughLLMWIKI.md` | Early requirement that the skill be executable and separated from always-loaded guidance. | Pre-implementation feedback. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM-Wiki_Details&projects.md` | Broader LLM-Wiki repository comparison. | Several external repository claims may be stale; local blueprint repos are stronger evidence. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Apex KB+SQLite FTS5BM25  Implementation Plan.md` | Older sequencing and validation ideas. | Superseded by verifier and implemented retrieval. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CC.md` | Original Macro/Meso/Micro retrieval specification. | Superseded and contains corrected assumptions. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CCv2.md` | Implementation sequencing. | Superseded details; use only for a disputed order decision. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CCv3.md` | Technical verifier and gap analysis. | Large and partly superseded by GPTv2/special/add-on/current code. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/Claude_Apex KB_SQLiteFTS5BM25_CCv4AddOn.md` | External feasibility correction and blueprint-gap reduction. | Time-sensitive external claims; architecture is already implemented locally. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/KB-Researchv2_gpt.md` | Early KB/memory/retrieval architecture. | Broad and superseded. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/KB-Researchv3_gpt.md` | Personal orchestration and retrieval vocabulary. | Can restart settled architecture debates. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/KB-Researchv3_gpt_FB_claude.md` | Score corrections to v3. | Feedback only. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/LLM&RetrievalPhaseResearch/research2_gem.md` | Provider/memory option vocabulary. | Provider scores are unstable and need new web verification. |

## Exclusion policy

Do not read or cite files beneath the two failed-output directories. Do not use standalone prompt drafts, chat histories, or prior draft plans as design evidence. If a substantive executed report exists, read that report instead of its generating prompt.

## Source questions by design decision

| Decision | Start with | Then inspect |
|---|---|---|
| What must deterministic Phase 0 create? | Phase 0 Decision | current `apex_kb.py`, parser report, component map |
| How should stages hand off? | Integration Map | artifact templates, current contracts |
| How should the LLM-Wiki create compounding value? | original `llm-wiki.md` | both operational packages and repository guide |
| How should all concept files be mapped? | Phase 0 Decision + old machine-index schema ideas | current ranking code, proposed topic-map/atlas templates |
| How should semantic completeness be proven? | current semantic-value contract | prior execution audit, acceptance schema, atlas acceptance proposal |
| How should retrieval work? | current retrieval code/contract | GPTv2 verifier only for unresolved mechanics |
| How should context/tokens be minimized? | Integration Map token layering + LLM-Wiki index-first flow | current skill/template instruction load and proposed short route |
| What should be optional? | tool-stack report | graph, AST, UI, vector, static-site alternatives |
