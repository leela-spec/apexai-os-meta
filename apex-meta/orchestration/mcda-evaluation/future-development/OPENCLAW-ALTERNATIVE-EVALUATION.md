# Future 2Do — Deferred Alternatives and Optional Components

Status: **DEFERRED / NOT PART OF CURRENT HERMES RUN**  
Originally deferred: 2026-08-22  
Expanded by operator decision: 2026-08-23  
Owner: Human CEO  
Priority: future only

The historical filename is retained so existing references do not break. This file now owns the future-development backlog for the explicitly deferred alternatives and optional components below.

## Current decision

The Hermes-centered architecture is accepted for the current pre-install realization path.

Do not add or pilot the following during the current run:

- **OpenClaw** — alternative orchestration/runtime candidate;
- **Agency Agents** — optional lazy specialist-roster supplement;
- **AnythingLLM** — optional human-facing knowledge/RAG application;
- **Semantic Router** — optional semantic-routing component.

The previously recommended bounded Agency Agents pre-install pilot is explicitly **skipped for now**. Baseline Hermes profiles + BMAD + MarketingSkills remain specialist owners.

## Why retained

These candidates have real upstream capabilities or prior research value, but none currently earns a new runtime, state store, knowledge store, routing service, or specialist layer before the accepted Hermes baseline has been installed and tested.

Keeping them here preserves the research without allowing optional architecture expansion to block the first working Hermes system.

## Candidate-specific reopen triggers

### OpenClaw

Reopen when:

- the validated Hermes system has a demonstrated orchestration/recovery limitation;
- a later full-system comparison is explicitly requested; or
- OpenClaw gains a materially decision-changing upstream capability.

### Agency Agents

Reopen when:

- recurring specialist gaps remain after actual use of Hermes profiles + BMAD + MarketingSkills;
- maintaining equivalent specialist profiles creates measurable context/maintenance cost; or
- the operator explicitly requests the previously researched lazy-router pilot.

If reopened, reuse the completed Agency research and test search/inspect/load first; do not silently make Agency the identity, project-context, review, or learning owner.

### AnythingLLM

Reopen only when there is a named human-facing knowledge/UI requirement that Hermes + QMD + repository artifacts do not satisfy.

Any future test must preserve the repository as canonical truth and avoid creating an unnecessary second document/vector truth store. Prefer consuming QMD through supported MCP behavior over duplicating native ingestion where possible.

### Semantic Router

Reopen only after **measured routing failures** demonstrate that Hermes task/profile/skill selection is insufficient and a maintained supported integration exists.

Do not create a custom wrapper/service merely to insert Semantic Router.

## Preserved evidence

Use existing research rather than restarting discovery:

- `Orchestration/research-runs/`
- `Orchestration/09-PRIMARY-ORCHESTRATION-SELECTION-HANDOVER.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-001-provisional-hermes-stack.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R03-AGENCY-AGENTS-INTEGRATION-AND-FIT-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R05-SEMANTIC-ROUTER-INTEGRATION-AND-FIT-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R06-ANYTHINGLLM-INTEGRATION-AND-FIT-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R08-ADVERSARIAL-EVIDENCE-AUDIT-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R09-SOPHISTICATED-V2-SYNTHESIS-RESULT.md`
- prior OpenClaw official-source findings referenced in those documents

Historical custom OpenClaw/Apex orchestration designs remain non-authoritative unless independently supported by current upstream OpenClaw behavior.

## Future evaluation law

A future evaluation must start from the **Hermes system that was actually installed and used**, identify a measured unmet requirement, and compare only existing current upstream solutions against the same real Master of Arts user story.

Do not add a component because it has broad capabilities. Promote it only when its measured value exceeds its additional runtime/state/context/security/maintenance cost.
