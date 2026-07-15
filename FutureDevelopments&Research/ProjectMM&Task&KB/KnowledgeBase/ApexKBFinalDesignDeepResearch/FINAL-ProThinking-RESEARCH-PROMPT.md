# Pro Thinking Apex KB Final Architecture

You are a senior knowledge-system architect conducting **one coherent Deep Research run** to define the final Apex KB architecture and its implementation guidance.

Your job is to research and design the complete, multifunctional Apex KB system. You are not implementing it in this run. Do not write repository patches, finished scripts, complete replacement files, or falsely finalized contracts. Produce detailed, implementation-ready design guidance that later implementation agents can execute without rediscovering the architecture.

---

## 1. Non-negotiable product target

Design **one final Apex KB architecture** that:

1. deterministically inventories every in-scope source or explicitly excludes it with a reason;

2. creates durable concept-to-source intelligence showing where every concept is discussed and why each file was surfaced;

3. preserves a reusable map of the documentary landscape for each concept, including current, historical, prototype, implementation, contextual, duplicate, superseded, incidental, blocked, and irrelevant-after-review sources;

4. uses deterministic scripts for observable, repeatable work and LLM judgment only for meaning, authority, contradiction, synthesis, and other semantic decisions;

5. compiles durable Macro, Meso, and Micro knowledge that is more valuable than rereading the raw corpus;

6. creates a durable concept dossier and a durable source atlas or equivalent lossless source-map surface for every configured concept;

7. makes future AI queries faster, cheaper, more complete, and easier to verify;

8. supports incremental maintenance without rereading unchanged evidence unnecessarily;

9. supports configurable execution profiles within the same final architecture;

10. supports a future low-token Codex orchestration loop that delegates semantic work to ChatGPT web in the strongest suitable reasoning mode;

11. minimizes redundant instructions, duplicate metadata, performative checks, and guardrails that do not prevent a demonstrated failure or eliminate repeat work;

12. remains honest when evidence or tooling is unavailable.

The source map and source atlas are **part of the durable product**, not disposable preprocessing. Future AIs must be able to discover quickly which files contain which information, what each source contributes, how sources relate, and where evidence lives.

---

## 2. Known failure mode — incomplete version drift

Treat this as a binding prohibition:

> Do not reinterpret “efficient,” “bounded,” “prioritized,” “iterative,” “configurable,” or “token-saving” as permission to design a lightweight, minimal, preliminary, V1, V1.5, later-completed, deferred, or partially functional Apex KB product.

The target is one final multifunctional architecture.

- **Prioritization controls research order.**

- **Configuration controls execution scope.**

- Neither reduces, postpones, or fragments the final system design.

Do not use maturity labels such as `V1`, `V1.5`, `minimal version`, `light version`, `smallest lifecycle`, `minimum critical path`, or `defer to later` as design dispositions.

Allowed dispositions are:

- `keep`

- `change`

- `add`

- `merge`

- `remove`

- `configurable`

- `reject`

- `requires_evidence_probe`

`reject` is valid only when a capability creates insufficient product value relative to its cost and complexity. Difficulty or setup cost alone is not sufficient. A valuable capability must be designed into the final architecture even when an execution profile can switch it off.

Technical schema versions may exist only as compatibility identifiers. They must never imply an incomplete product stage.

---

## 3. Repository identity and path contract

Use this identity wherever repository evidence is available:

```yaml

repository_owner: leela-spec

repository_name: apexai-os-meta

repository_full_name: leela-spec/apexai-os-meta

branch: main

research_package_root: FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch

path_style: repository_relative

```

Rules:

1. Use repository-relative paths after this identity block.

2. Do not use local drive paths, local-checkout assumptions, or environment-specific prefixes.

3. Resolve and record the current `main` commit at research start when repository access works.

4. Do not treat a commit written inside an older research file as the current implementation authority.

5. If a file exists in multiple representations, preserve the repository-relative identity and record which representation was actually read.

---

## 4. Source-access probe and fallback modes

Perform one small access probe before substantive research. This probe prevents wasting the run on an unusable source route; it must not become a large validation bureaucracy.

Attempt to open completely:

1. `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/00-START-HERE.md`

2. `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/02-LIFECYCLE-COMPONENT-VALUE-MAP.md`

3. `.claude/skills/apex-kb/SKILL.md`

Try source routes in this order:

1. enabled GitHub app or GitHub connector;

2. public GitHub pages for `leela-spec/apexai-os-meta` on `main`;

3. raw GitHub file URLs for the same repository and branch;

4. uploaded Project Sources containing the complete research package and selected repository files.

Do not attempt local paths.

Select one evidence mode:

### Mode A — `full_repository_evidence`

Use when the package, current Apex KB implementation, indexes, and blueprint sources are accessible reliably. Perform the complete current-state mismatch analysis.

### Mode B — `project_source_repository_snapshot`

Use when GitHub routes fail but Project Sources contain the package and important repository files. Treat those files as a snapshot. Record what implementation evidence is present, what may be stale, and which conclusions cannot be verified against current `main`.

### Mode C — `architecture_research_without_apex_implementation`

Use when neither GitHub nor uploaded Project Sources provide reliable current Apex implementation evidence.

Do **not** abort the Deep Research run. Continue with:

- the available research-instruction package;

- uploaded self-created research files;

- available LLM-Wiki sources;

- available Claude/skill/orchestration design sources;

- current official primary-source web documentation;

- high-quality primary implementation sources for tools and libraries.

In Mode C:

- design the final architecture and implementation guidance;

- do not claim to have verified the current Apex KB implementation;

- mark current mismatch scores as `unverified` where evidence is absent;

- produce a precise list of implementation facts that must later be checked;

- keep the research run useful by focusing on the value, design, mechanisms, tools, interfaces, and creation guidance.

Do not lower the product target because repository access failed.

---

## 5. Evidence classes and authority

Separate every major conclusion into one of these evidence classes:

1. **Operator target** — binding intent defined by this prompt and the package target lock.

2. **Current implementation fact** — verified directly from current `main`, or explicitly identified snapshot evidence in Mode B.

3. **Existing Apex research intent** — decisions and hypotheses from the research package and indexed research files.

4. **LLM-Wiki blueprint evidence** — mechanisms and implementation patterns from the available LLM-Wiki sources.

5. **Claude/skill/orchestration design evidence** — best practices for skill structure, progressive disclosure, workflow ownership, scripts, files, recovery, and micro file-creation patterns.

6. **External primary evidence** — current official documentation, specifications, code repositories, or library documentation.

7. **Inference** — reasoned conclusion derived from cited evidence.

8. **Recommendation** — the proposed final design decision.

Do not let older research claims override current code. Do not let paths, dates, filenames, scores, or deterministic matches establish semantic authority by themselves.

---

## 6. Mandatory source families

### 6.1 Prepared Apex research package

Read the available package files in numeric order:

- `00-START-HERE.md`

- `01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md`

- `02-LIFECYCLE-COMPONENT-VALUE-MAP.md`

- `03-ARTIFACT-HANDOFF-TEMPLATES.md`

- `04-Apex-KB-Current-Research-Index.md`

- `05-Apex_KB_Current_Research_Index.machine-readable.yaml.md`

- `06-LLM-WIKI-REPOSITORY-GUIDE.md`

Treat `02-LIFECYCLE-COMPONENT-VALUE-MAP.md` as a **seed hypothesis that this research run must verify and update**, not as a locked final design.

### 6.2 Current Apex KB implementation

When available, inspect current `main`, including at least:

- `.claude/skills/apex-kb/SKILL.md`

- relevant `.claude/skills/apex-kb/references/`

- relevant `.claude/skills/apex-kb/templates/`

- `apex-meta/scripts/apex_kb.py`

- `apex-meta/scripts/apex_kb_retrieval.py`

- current tests, fixtures, manifests, runbooks, and generated contracts that materially affect behavior.

Inspect code behavior, not only contract prose.

### 6.3 LLM-Wiki sources — mandatory for every module

For each researched lifecycle module, consult the relevant LLM-Wiki source material. Do not isolate LLM-Wiki analysis into one early comparison and then forget it.

For every module, state:

- which LLM-Wiki mechanism creates relevant value;

- whether Apex should copy, adapt, combine, configure, or reject it;

- what the mechanism lacks relative to the final Apex target;

- which file, workflow, script, or data-layout pattern provides implementation evidence.

Use the available original LLM-Wiki concept source and both operational LLM-Wiki packages identified in the research indexes.

### 6.4 Claude skill and orchestration design — mandatory for micro design

For every recommendation about an Apex skill file, reference file, template, workflow, script, hook, agent, browser handoff, or orchestration boundary, consult the relevant Claude/skill/orchestration design evidence.

Start with available compiled sources such as:

- `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md`

- `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/agent-skill-orchestration-resilient-workflows.md`

- `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/agent-subagent-design-patterns.md`

- `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/agent-vs-subagent-vs-skill.md`

- `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/commands-hooks-rules-memory-model.md`

- `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/apex-application-orchestration-patterns.md`

If a named path is unavailable, use the corresponding compiled index or uploaded Project Source and record the substitution.

Use raw research notes only when the compiled page does not answer the decision or when provenance is disputed.

### 6.5 External web research

Use current web research when it materially improves the design, especially for:

- current ChatGPT Deep Research and connected-app behavior;

- current GitHub access behavior;

- current Claude Code, Agent Skills, and orchestration capabilities;

- parser, extraction, indexing, retrieval, and database behavior;

- tool installation, maintenance, platform compatibility, and licensing;

- browser automation or API feasibility.

Prefer official primary documentation and primary repositories. Separate product facts from recommendations.

---

## 7. One coherent run — no operator approval pauses

This is one Deep Research prompt and one coherent research run.

- Do not split lifecycle groups into separate Deep Research runs.

- Do not pause for operator validation between groups.

- Do not ask the operator to approve the target lock, map, grouping, or module results during the run.

- Consultation about execution profiles happens after the final report and before implementation.

- Grouping exists to prevent context mixing and to focus source reading inside the same run.

---

## 8. Required research sequence

### Step 1 — Create the Target Lock

This must be the first substantive output section.

Define:

- the final Apex KB purpose;

- the exact future-AI jobs it must perform;

- the durable concept dossier target;

- the durable source map/source atlas target;

- deterministic versus semantic ownership;

- token-saving and value requirements;

- configurable-mode principles;

- current-state and maintenance requirements;

- measurable success conditions;

- explicit non-success proxies;

- known failure modes, including incomplete-version drift and guardrail bureaucracy.

Do not inherit the target uncritically from the existing package. Verify that it captures the operator intent and the highest-value behavior.

### Step 2 — Verify and update the Lifecycle Component and Value Map

Use the existing map as a seed.

For every existing component:

1. verify whether it belongs in the final lifecycle;

2. correct its definition;

3. add missing components and subcomponents;

4. merge duplicates;

5. identify dependencies and consumers;

6. distinguish deterministic, semantic, orchestrator, evaluator, and operator ownership;

7. compare it with the current Apex implementation when evidence permits;

8. score it using the 1–100 model below;

9. assign a justified disposition;

10. identify which research module should resolve it.

Do not pre-accept current map groupings, scores, priorities, or recommendations.

### Step 3 — Group the lifecycle for focused research

Create coherent research groups based on dependencies, source overlap, and decision boundaries.

Likely domains include, but are not binding:

- target, scope, and source custody;

- deterministic corpus intelligence;

- concept-to-source maps and durable source atlases;

- semantic source analysis and knowledge compilation;

- semantic acceptance and truthful completion;

- retrieval and query behavior;

- incremental maintenance and impact analysis;

- configurable execution profiles;

- Codex/browser/deterministic-runtime orchestration;

- Apex skill package, workflows, templates, scripts, and micro file design.

Regroup where evidence supports a better architecture.

### Step 4 — Rank groups by current value opportunity

Research the highest-value mismatches first.

Prioritize primarily by:

```text

current Apex mismatch

× achievable product-value gain

× downstream lifecycle leverage

```

When current implementation evidence is unavailable, use target contribution, failure severity, and downstream leverage, and mark mismatch as unverified.

### Step 5 — Research each group iteratively inside the same run

For each group:

1. state its target contribution;

2. identify the current mismatch or unverified implementation questions;

3. derive only the research questions needed for that group;

4. identify a focused source bundle;

5. read only the shared authority sources and sources relevant to the group;

6. compare current Apex, LLM-Wiki, Claude/skill/orchestration design, and external best practice;

7. design the module and possible submodules;

8. define implementation guidance and interconnections;

9. define file/script-level creation guidance;

10. update remaining priorities before moving to the next group.

Do not maintain one large flat list of global research questions.

---

## 9. Module output contract

For every grouped module, provide:

### A. Module purpose and value

- target contribution;

- future-AI jobs supported;

- failure prevented;

- repeat work or tokens eliminated.

### B. Current-state mismatch

- verified current behavior;

- intended behavior from existing research;

- mismatch and severity;

- unavailable facts that require later verification.

### C. Focused research and evidence

- module-specific questions;

- sources read;

- repository facts;

- blueprint evidence;

- external evidence;

- inferences and disagreements.

### D. Final module strategy

- keep/change/add/merge/remove/configurable/reject decisions;

- module boundary;

- submodules;

- owners;

- inputs;

- operations;

- outputs;

- consumers;

- failure behavior;

- recovery behavior only where it prevents a demonstrated failure.

### E. Implementation map

- implementation order;

- dependencies;

- migration from current behavior;

- compatibility implications;

- deterministic and semantic interfaces;

- tests and fixtures;

- measurable acceptance.

### F. Creation guidance

- required logic and flow;

- best-practice patterns;

- what must be derived versus authored;

- what must not be duplicated;

- progressive-disclosure strategy;

- context and token implications.

### G. Interconnectedness

- upstream producers;

- downstream consumers;

- cross-module dependencies;

- affected artifacts;

- incremental invalidation and maintenance impact.

### H. File and script impact

Identify every affected existing or proposed file/script and provide the file/script design record defined below.

---

## 10. File and script design record

For every affected file, template, script, workflow, reference, manifest, or generated artifact, provide:

- repository-relative target path or proposed path;

- artifact type;

- purpose;

- owner;

- canonical, generated, derived, or temporary status;

- current behavior and current mismatch;

- final responsibilities;

- explicit non-responsibilities;

- inputs;

- outputs;

- consumers;

- required sections, chapters, interfaces, commands, or data fields;

- control flow;

- deterministic versus semantic boundary;

- relationships to other files;

- progressive-disclosure/loading behavior;

- best-practice source used for the micro design;

- migration behavior;

- tests and fixtures;

- failure behavior;

- token and maintenance cost;

- risks;

- disposition and rationale.

Do not write the complete file, complete contract, or code. Give enough detail that implementation does not need to rediscover the design.

---

## 11. Scoring model — 1 to 100

Score every material component, module, tool, script, artifact, and LLM instruction on these separate dimensions:

- target contribution;

- current mismatch;

- achievable knowledge-value gain;

- token-saving potential;

- deterministic leverage;

- downstream leverage;

- failure severity if absent or wrong;

- resilience contribution;

- implementation cost;

- recurring token/compute/maintenance cost;

- evidence confidence.

Use `unverified` instead of inventing a current-mismatch score when current implementation evidence is unavailable.

You may calculate a transparent priority score for sequencing, but:

- show the formula;

- do not hide dimensional tradeoffs;

- do not treat the score as semantic authority;

- do not use false precision unsupported by evidence.

---

## 12. Configurable execution-profile strategy

Design configurable modes inside the one final architecture. The report must propose sensible defaults and named profiles for later operator consultation.

At minimum, evaluate independent configuration axes for:

- source-format coverage, including non-Markdown files;

- corpus-priority coverage;

- topic coverage;

- semantic depth;

- full versus targeted source reading;

- source-atlas depth;

- duplicate and version-family handling;

- graph extraction;

- external verification;

- acceptance depth;

- new build, complete rebuild, incremental update, and targeted repair;

- terminal, connector, and browser semantic-execution surfaces.

A profile may switch a capability off for a run, but the final architecture must still define that capability, its dependencies, activation criteria, and consequences.

The final report must distinguish:

- `rejected`: insufficient value for the final product;

- `configurable`: valuable and designed, but selectable per execution;

- `requires_evidence_probe`: value may exist, but a named technical fact must be tested before final implementation choice.

Do not create V1/V2 maturity tracks.

---

## 13. Future Codex and ChatGPT web orchestration design

Research and design this as part of the final Apex KB architecture. It is not the execution method of this Deep Research run.

Target ownership split:

| Owner | Responsibilities | Must not do |

|---|---|---|

| Codex/orchestrator | necessary scope/profile Q&A; deterministic command execution; bounded task packets; changed-path verification; Git operations; execution coordination | deep-read the corpus; duplicate semantic synthesis; author knowledge from shallow context |

| ChatGPT web in the strongest suitable reasoning mode | read sources; judge authority, contradiction, freshness, and meaning; write Phase 1/2 knowledge; perform semantic evaluation | run local lifecycle scripts; perform Git commits or pushes |

| Deterministic runtime | inventory; hashes; extraction status; Phase 0 maps; structural validation; retrieval/index rebuild; observable postflight facts | judge semantic truth or authority |

Do not hard-code a model marketing label. Require the strongest suitable available reasoning mode and record the actual model/mode used at execution.

Define a **save batch** as a coherent, context-aware, completed Apex KB unit—for example one concept plus its source atlas, or one tightly related source group—not an arbitrary partial draft.

Evaluate this operating loop:

```text

Operator answers scope/profile questions once

→ Codex runs deterministic source mapping

→ Codex submits one bounded semantic batch to ChatGPT web

→ ChatGPT reads and writes the requested semantic artifacts

→ Codex verifies changed scope and runs deterministic checks

→ an independent semantic context performs only the acceptance work whose value is demonstrated

→ Codex rebuilds retrieval and performs Git operations

→ next saved batch

```

Do not add generic guardrails, ledgers, evaluator layers, or restart protocols merely because they sound safe. Retain only mechanisms that directly prevent a demonstrated failure, preserve valuable work, or eliminate repeat work.

---

## 14. Durable source-map and index design

The final design must preserve the concept-to-source work that is already performed during discovery and semantic classification.

Research and specify:

- exhaustive machine-readable concept candidate maps;

- compact LLM navigation projections that never replace the exhaustive set;

- durable per-concept source atlases or equivalent lossless structures;

- per-file content snapshot and individual value;

- freshness, authority, lifecycle, contradiction, duplicate, and supersession relationships;

- exact evidence pointers;

- blocked/unreadable visibility;

- how maps remain useful for audits and failure diagnosis;

- how retrieval indexes these maps without confusing them with semantic authority;

- how changed files invalidate affected maps, capsules, dossiers, and retrieval artifacts;

- how future AIs use the map to form a complete picture quickly.

Do not treat this as an optional reporting feature. It is one of the core product values.

---

## 15. Required final report structure

Return the report in this order.

# 1. Target Lock

The complete, measurable final product target and failure-mode prohibitions.

# 2. Evidence Mode and Source Truth

- selected evidence mode;

- source-access results;

- current `main` commit when available;

- sources available and unavailable;

- snapshot limitations;

- evidence-class rules used.

# 3. Verified and Updated Lifecycle Component and Value Map

- corrected complete component map;

- added, merged, removed, configurable, rejected, and probe-required components;

- 1–100 scores;

- ownership and dependencies;

- current mismatch or `unverified` status.

# 4. Research Grouping and Priority Order

- groups;

- why each group is coherent;

- focused source bundle for each group;

- priority calculations and sequencing.

# 5 onward. Priority-Ordered Module Research

One complete module report per group, using the Module Output Contract.

# Configurable Apex KB Execution Profiles

- independent configuration axes;

- named profiles;

- defaults;

- tradeoffs;

- decisions requiring later operator consultation.

# Codex / ChatGPT Web / Deterministic Runtime Orchestration

- responsibilities;

- batch design;

- task-packet structure;

- file handoffs;

- failure behavior;

- demonstrated validation needs;

- token implications.

# Final File and Script Implementation Plan

- exact proposed final tree;

- every affected current and proposed file/script;

- file/script design records;

- dependency order;

- migration strategy;

- tests and fixtures;

- no code and no full replacement-file contents.

# Cost, Token, and Complexity Audit

- one-time and recurring costs;

- token drivers;

- deterministic savings;

- unnecessary files, fields, gates, and instructions to remove or merge;

- high-cost capabilities and the value required to justify them.

# Implementation Acceptance Model

- measurable product acceptance;

- deterministic checks;

- semantic checks whose value is demonstrated;

- durable source-map completeness;

- fixtures and real-corpus canaries;

- truthful partial and blocked states.

# Research Confidence and Future Investigation

This is the final export only. Include:

1. trusted findings;

2. current implementation facts verified directly;

3. findings with limited evidence;

4. research hypotheses not yet validated;

5. remaining knowledge gaps;

6. possible future research;

7. capabilities requiring technical probes;

8. what worked well in the research process;

9. weak sources or approaches;

10. what implementation agents must verify before relying on the design.

Do not interrupt the run with these questions earlier.

---

## 16. Validation before returning

Before finalizing, verify that:

- the first substantive section is the Target Lock;

- the Lifecycle Component and Value Map was verified, corrected, expanded, rescored, and regrouped by the research run;

- every material component has a disposition and rationale;

- no valuable capability was omitted merely because it was difficult or expensive;

- no V1/V1.5/minimal/deferred architecture remains;

- configuration is not confused with product incompleteness;

- every module was researched with focused sources inside the same run;

- LLM-Wiki evidence was consulted for every module;

- Claude/skill/orchestration design evidence was used for every micro file or workflow recommendation;

- current code behavior is distinguished from research intent when current code is accessible;

- fallback evidence modes are honest and still produce useful research;

- the durable source map/source atlas is a core product output;

- all paths are repository-relative after the single repository identity block;

- the report does not contain patches, finished scripts, complete replacement files, or unsupported claims;

- the final design is sufficiently detailed for implementation without architecture rediscovery;

- the final section records confidence, gaps, probes, and future research.

Return a decision-complete research report with citations and explicit source attribution.