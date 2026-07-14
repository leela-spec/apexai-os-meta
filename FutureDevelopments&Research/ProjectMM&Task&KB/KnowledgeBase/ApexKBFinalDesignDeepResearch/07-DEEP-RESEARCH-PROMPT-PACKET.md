# Deep Research Prompt Packet

## Packet metadata

```yaml
packet_id: apex-kb-final-design-deep-research-v1
primary_task_type: research
secondary_task_types:
  - long_context_digestion
  - workflow_extraction
  - synthesis
  - planning
expected_output_type: decision_complete_architecture_and_implementation_plan
provider_target: ChatGPT Deep Research
provider_rationale: >-
  The task requires a source-led comparison of a live repository implementation,
  extensive local research, multiple blueprint repositories, and a small amount of
  current official technical verification. It benefits from long-context source
  synthesis and citations, but it does not require code mutation.
iteration_loop: research_synthesize_decide
follow_up_loop: generate_critique_revise
```

## Clean copy-paste prompt

```text
You are a senior knowledge-system architect conducting a repository-grounded Deep Research run.

Your task is to produce the final, decision-complete architecture and implementation plan for Apex KB. Do not write or patch repository files. Do not redesign unrelated Apex orchestration. Do not inspect or require a second repository. Work only from the `apexai-os-meta` repository connected to this chat plus narrowly necessary current primary-source web documentation.

MISSION

Define the smallest resilient lifecycle that combines deterministic whole-corpus indexing with LLM semantic judgment so Apex KB creates durable, high-value knowledge rather than shallow summaries.

The locked product target is:

1. Deterministically inventory every in-scope file or explicitly exclude it with a reason.
2. For every configured concept/topic, expose every deterministic candidate file and the exact reasons it matched: path, filename, title/frontmatter, H1, headings, body, links, co-occurrence, duplicates, and date/version signals where available.
3. Use those maps to let an LLM read core evidence efficiently, classify every candidate, preserve versions and contradictions, and reuse unchanged source understanding.
4. Compile a useful concept dossier that answers important questions at Macro, Meso, and Micro levels.
5. Compile a source atlas that lists every concept candidate with an individual content snapshot, individual value, freshness/authority assessment, duplicate/supersession relationship, review status, and exact relevant pointers.
6. Prove in a fresh context that future AIs can answer routine concept and source-location questions from compiled pages without reopening readable raw sources.
7. Build deterministic index/retrieval/postflight only after semantic acceptance.
8. Keep the normal LLM route short and simple enough that most context and output tokens are spent reading evidence and writing the actual wiki.

The final design must create more value than simply letting an AI read the small set of sources again. File counts, headings, word counts, source counts, commits, and self-reported rereads are never proof of semantic value.

SOURCE BOUNDARY AND READING ORDER

Use repository-relative paths only.

Stage 1 — Read the prepared evidence package completely, in order:

- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/00-START-HERE.md`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/02-LIFECYCLE-COMPONENT-VALUE-MAP.md`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/03-ARTIFACT-HANDOFF-TEMPLATES.md`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/04-Apex-KB-Current-Research-Index.md`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/05-Apex_KB_Current_Research_Index.machine-readable.yaml.md`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/06-LLM-WIKI-REPOSITORY-GUIDE.md`

Stage 2 — Deep-read every P0 source from the new index. Inspect the current Apex KB implementation on current `main`, especially:

- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/references/semantic-value-contract.md`
- `.claude/skills/apex-kb/templates/ingest-analysis-template.md`
- `.claude/skills/apex-kb/templates/wiki-page-templates.md`
- `apex-meta/scripts/apex_kb.py`
- `apex-meta/scripts/apex_kb_retrieval.py`

Do not rely on a local-checkout commit statement when the connected repository shows a newer main branch. Record the exact commit inspected.

Stage 3 — Read the P1 source spine completely. It contains executed deterministic research and the three LLM-Wiki blueprint sources.

Stage 4 — Read P2 sources only for decisions still unresolved after Stages 1–3. Use P3 only to resolve provenance or a specific disagreement. Do not reread every historical report equally.

Do not read, cite, or use as design evidence:

- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Failed_Prompts/`
- `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/FailedKBCreation/`
- standalone failed prompt drafts, chat histories, or superseded draft plans

If current external facts are material—for example SQLite FTS5 behavior, supported parser libraries, or current Claude Code skill loading—verify them using official primary documentation. External web research is validation, not the source of the Apex product target. Clearly separate repository evidence, external evidence, inference, and recommendation.

CORE RESEARCH QUESTIONS

Answer all of these:

1. What value and artifact chain did the Phase 0 and orchestration research actually intend at Macro, Meso, and Micro levels?
2. What does current `apex_kb.py` implement for each intended artifact, and where does it diverge? Inspect code, not only contracts.
3. Does current Phase 0 reliably expose every file that can matter to a concept? Test the ranking design for ambiguous supporting terms, dedicated filenames, headings, long generic files, duplicates, versions, dates, graph links, and candidates beyond rank 30.
4. Which deterministic artifacts make LLM reading materially cheaper, and which artifacts merely add process or duplicate information?
5. What exact handoff should each deterministic artifact provide to the next LLM step?
6. What semantic work should be reusable by source hash, and what must remain topic-specific?
7. What is the leanest reliable way to classify every candidate while reading core/current sources fully and contextual sources only where justified?
8. What exact information must a concept dossier contain? What belongs in a separate source atlas? When may the atlas be embedded?
9. How should freshness, authority, current/prototype/historical/proposal/implementation status, contradiction, duplication, and supersession be assessed without inferring truth from paths or dates alone?
10. Which semantic v2 safeguards added on current main should be preserved, simplified, expanded, or removed?
11. Does the current semantic ledger/template/runbook impose more authored fields and context than their downstream value justifies? Trace every mandatory field to a consumer and demonstrated failure.
12. How should page-only query acceptance, claim entailment, topic-map completeness, and source-atlas completeness combine without creating a new bureaucracy?
13. How should wiki index, chunk retrieval, FTS5/BM25, fallback retrieval, query packets, lint, audit, staleness, and postflight consume accepted compiled pages?
14. How should a changed source deterministically identify affected capsules, topics, dossiers, atlases, and acceptance artifacts so unchanged evidence is not reread?
15. Which mechanisms from each LLM-Wiki repository create the same target value, which are missing, and which would be costly distractions?
16. What exact short instruction flow should a terminal agent and a browser/Git-connector AI follow? How many files and approximate instruction tokens are loaded before topic evidence?
17. Which optional tools—markdown-it-py, YAML libraries, graph extraction, DOCX/PPTX/XLSX/PDF extraction, qmd/vector retrieval, Obsidian/web UI, static-site systems—belong in the core, capability-gated extension, later optimization, or reject list?
18. What fixture and hard canary prove that the lifecycle creates an answer-bearing dossier and a complete source atlas rather than a rewrite of a few sources?

DESIGN DISCIPLINE

- Preserve the deterministic/LLM boundary: scripts report observable file facts; LLMs judge meaning, authority, contradictions, and synthesis.
- Preserve current semantic v2 improvements unless repository evidence shows a simpler mechanism achieves the same protection.
- Treat Phase 0 rankings as navigation only. Do not let any score, path, filename, date, or prior summary establish semantic authority.
- Keep the exhaustive machine candidate set separate from the compact LLM read view. A compact view may be bounded; the authoritative candidate set may not be silently top-N truncated.
- Do not solve missing value with fixed word counts, claim counts, source counts, page counts, or more required headings.
- Do not add an artifact, field, gate, tool, or instruction unless you identify its consumer, the demonstrated failure it prevents or repeat work it removes, and its recurring token/maintenance cost.
- Prefer derived fields over LLM-authored duplicate metadata.
- Prefer one short startup contract and progressive disclosure over loading the whole skill package.
- Keep optional publishing, UI, graph, vector, and heavy-parser systems outside the minimum critical path unless evidence proves they are needed.
- Do not expose hidden chain-of-thought. Provide an evidence ledger, concise decision rationales, alternatives, and tradeoffs.
- Do not use Leela as the design subject. The known failed build is only a negative acceptance case: the final lifecycle must make that shallow outcome impossible to report as complete.

RATING METHOD

For every material component, tool, script, artifact, and LLM instruction, give:

- status: keep | change | add | merge | delete | capability-gate | defer | reject;
- token efficiency: 1–5, where 5 is best;
- value created: 1–5, where 5 is highest;
- resilience: 1–5, where 5 is strongest;
- setup cost: 1–5, where 5 is most expensive;
- recurring management cost: 1–5, where 5 is most expensive;
- evidence and concise rationale;
- exact producer, input, output, consumer, validation, and failure behavior.

Do not average these scores into one authority number. State tradeoffs.

REQUIRED OUTPUT

Return exactly these sections:

# 0. Executive decision

- Final architecture in no more than 15 decisive bullets.
- The minimum critical path.
- Optional/capability-gated path.
- The single biggest current failure and the single most important fix.

# 1. Evidence and implementation truth ledger

- Exact repository commit inspected.
- Every P0/P1 file read and any unavailable file.
- Repository facts versus research intent versus blueprint evidence versus inference.
- Contradictions between the two priority research documents, current contracts, and current code.

# 2. Product target and acceptance lock

- Exact future-AI jobs the KB must perform.
- Macro/Meso/Micro dossier contract.
- Complete source-atlas contract.
- Measurable success and explicit non-success proxies.

# 3. Final lifecycle and handoff map

For every stage from scope to incremental maintenance, provide:

- owner;
- inputs;
- operation;
- exact artifact/output;
- next consumer;
- deterministic validation;
- semantic validation;
- stop/fallback behavior;
- ratings and disposition.

Include one end-to-end flow diagram and one compact table. Do not replace the detailed map with a high-level outline.

# 4. Deterministic corpus-intelligence design

Specify exact final contracts for:

- corpus scope and exclusions;
- inventory/hashes/extraction status;
- heading and section spans;
- field-separated term postings;
- topic vocabulary and ambiguous supporting terms;
- duplicate and possible version families;
- lifecycle/authority hints;
- graph contribution if retained;
- exhaustive topic map;
- compact topic navigation view;
- populated Phase 0 report or its justified deletion;
- deterministic rerun, completeness, and fixture tests.

Show how each intended Phase 0 research artifact maps to keep/change/merge/delete in the final runtime. Resolve the current `keyword-hits.ndjson` / `topic-file-map.json` versus `term-frequency.json` / `topic-source-rankings.json` drift.

# 5. Lean semantic compilation design

Specify:

- source-hash capsule interface and invalidation;
- topic candidate-disposition interface;
- full versus targeted read rules;
- authority/freshness/contradiction/supersession judgment;
- concept dossier structure;
- source-atlas structure and every-candidate reconciliation;
- page topology rules;
- fresh-context evaluation;
- truthful states.

Give a field-level keep/change/delete table for the current Phase 1 template, Phase 2 templates, semantic run ledger, semantic acceptance artifact, and browser runbook. Remove any field with no justified consumer.

# 6. Simple AI instruction flows

Provide two concise, directly usable flows:

1. terminal-backed semantic compiler;
2. browser/Git-connector semantic compiler with no account Skill requirement.

For each, state:

- startup files in exact order;
- approximate startup instruction tokens;
- one-topic work unit;
- interruption recovery state;
- fresh evaluator handoff;
- deterministic handoff;
- what the AI must never do.

The browser flow must be achievable through one repository connector and complete whole-file reads/writes. It must report partial rather than lower quality when constraints block the target.

# 7. Retrieval, query, and maintenance design

- Keep/change assessment of current retrieval runtime.
- Index and source-atlas chunking.
- FTS5 probe and lexical fallback.
- page-first versus raw verification behavior.
- saved synthesis promotion.
- structural lint, semantic audit, staleness, incremental impact, and postflight.
- why retrieval cannot certify page quality.

# 8. File-by-file implementation plan

Give the exact final file tree and, for every current Apex KB file/runtime file affected:

- keep/change/merge/delete/add;
- exact section or interface to change;
- dependency order;
- migration/compatibility behavior;
- tests;
- risk.

Separate minimum-critical-path implementation from optional later work. No code or full file contents.

# 9. Fixtures and hard canary

Define a multi-file fixture containing:

- current specification;
- older conflicting specification;
- prototype;
- implementation evidence;
- exact duplicate;
- possible version;
- contextual cross-feature source;
- incidental high-keyword-noise file;
- relevant candidate beyond rank 30;
- unsupported/unreadable file.

Then define a hard real-corpus concept canary. It passes only when every candidate is visible and dispositioned, core/current sources are read, the dossier answers all priority questions, the atlas explains every candidate, retrieval returns answer-bearing sections, sampled claims are entailed, and measured total future-query work is lower than raw-source rereading.

# 10. Cost, token, and overengineering audit

- Estimated one-time setup cost and recurring cost by phase.
- Estimated LLM input/output token drivers, not false precision.
- Which deterministic artifacts save the most semantic tokens.
- Which current instructions/artifacts should be deleted or merged because they consume context without creating value.
- Maximum recommended ordinary startup package and rationale.
- A “do not build yet” list.

# 11. Decision register and residual uncertainties

- Locked decisions.
- Alternatives considered and rejected.
- Capability probes required before implementation.
- Genuine operator decisions only; do not list questions that repository evidence can resolve.

# 12. Implementation-ready acceptance checklist

Provide a concise checklist that an implementation agent can use to determine whether the design has been implemented without rediscovering the architecture.

VALIDATION BEFORE RETURNING

Before finalizing, verify all of the following:

- Every material component in `02-LIFECYCLE-COMPONENT-VALUE-MAP.md` has a final disposition.
- Every intended artifact in the two P0 research documents maps to a final producer and consumer or an explicit deletion rationale.
- Every major script/process from all three LLM-Wiki sources is copied, adapted, capability-gated, deferred, or rejected with evidence.
- Current code behavior is distinguished from contract claims.
- The final design includes exhaustive candidate visibility and a source atlas, not only target-query answerability.
- The minimum critical path is simpler than the current semantic route in authored fields and startup context unless a measured integrity requirement justifies otherwise.
- No deterministic metric is presented as proof of semantic meaning.
- No optional UI, vector, graph, or publishing system is smuggled into V1 without evidence.
- The output is decision-complete enough for an implementation agent and contains no placeholder sections.

STOP CONDITIONS

If any P0 source or current implementation file is inaccessible, continue with accessible evidence but mark the exact decision that remains unverified. Do not fabricate repository behavior. Do not stop merely because an optional historical/P2/P3 source is unavailable. Do not patch files, commit, push, or execute the Apex lifecycle.
```

## Failure and learning hints

| Likely failure | Correction built into the prompt |
|---|---|
| Repeats the Leela failure analysis instead of redesigning Apex KB | Explicit one-repository scope and Leela-only negative-case boundary. |
| Reads every historical file and burns context | P0/P1 complete spine, P2 conditional, P3 provenance only, failed folders excluded. |
| Returns another high-level architecture outline | Exact output requires producer/input/output/consumer/validation/failure and file-by-file implementation plan. |
| Adds more ledgers/gates/templates | Every field/artifact must name its consumer, prevented failure, savings, and cost; deletion/merge table required. |
| Treats target queries as the entire product | Source-coverage query, exhaustive topic map, and source-atlas acceptance are mandatory. |
| Treats deterministic score as authority | Explicit navigation-only boundary and field-separated evidence. |
| Copies all LLM-Wiki features | Copy/adapt/gate/defer/reject disposition and do-not-build list required. |
| Confuses current code with research intent | Evidence ledger and explicit code inspection required. |
| Produces code instead of a design | No patches or full file contents; implementation-ready interfaces and plan only. |

## Prompt quality review

```yaml
validation_status: ready
provider_fit:
  deep_research_scope_defined: true
  repository_source_priority_defined: true
  external_source_boundary_defined: true
  facts_assumptions_recommendations_separated: true
  citations_required: true
  date_sensitive_claims_flagged: true
output_contract:
  exact_sections: true
  implementation_ready: true
  no_chain_of_thought_request: true
  no_code_mutation: true
context_efficiency:
  progressive_disclosure: true
  failed_sources_excluded: true
  historical_sources_conditional: true
  anti_overengineering_test: true
target_integrity:
  whole_corpus_visibility: true
  macro_meso_micro_dossier: true
  complete_source_atlas: true
  current_code_reconciliation: true
  semantic_and_deterministic_gates_separated: true
```
