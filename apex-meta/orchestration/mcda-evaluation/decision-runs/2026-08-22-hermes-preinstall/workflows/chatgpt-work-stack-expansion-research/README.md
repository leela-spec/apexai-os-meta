# ChatGPT Work — Hermes Stack Expansion Research

Status: **READY FOR AUTONOMOUS RESEARCH / NO INSTALLATION**  
Date: 2026-08-23  
Repository: `leela-spec/MasterOfArts`  
Branch: `main`

## 1. Purpose

This workflow asks a different question from the completed Hermes pre-install research:

> **Given the now-researched Hermes-centered pipeline, do CrewAI, Agency Agents, Superpowers, Semantic Router, or AnythingLLM provide verified additional value, replace a module more effectively, or add unnecessary duplication?**

The workflow must not invent a new combined architecture. It evaluates only capabilities and integrations that can be verified in current upstream products, official repositories, first-party documentation, current releases, tests, and operational evidence.

The current Hermes research is the baseline, not a sacred conclusion. The completed R01-R07 results must be read and then re-checked against current upstream sources wherever a claim becomes load-bearing in this comparison.

## 2. Baseline being compared

The existing researched target is:

```text
Human CEO
   |
Hermes Agent
   |
   +-- Hermes Kanban: durable work/review/dependencies
   +-- existing MasterOfArts repo: factual source/artifact estate
   +-- hierarchical project context: root/family/micro context
   +-- shared Hermes profiles: reusable specialist identities
   +-- BMAD: workflow/persona/method skills
   +-- MarketingSkills: marketing specialist procedures
   +-- QMD: local retrieval index over repo truth
   +-- Hermes memory + Curator: runtime/procedural learning
   +-- model/provider path
   +-- official local safety controls
```

The completed ChatGPT Work research currently marks all seven original tracks `PASS`, while preserving important configuration/pilot gates such as project-context creation, MarketingSkills multi-family path validation, QMD runtime validation, and learning governance.

Baseline evidence lives under:

`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/`

## 3. Candidate identities — locked

Do not silently substitute similarly named products.

| Candidate | Authoritative identity | Initial role to test, not assume |
|---|---|---|
| CrewAI | `crewAIInc/crewAI` + `docs.crewai.com` | alternative/supplemental multi-agent workflow runtime |
| Agency Agents | `msitarzewski/agency-agents` | specialist-agent roster/router for Hermes and other harnesses |
| Superpowers | `obra/superpowers` | workflow/skill methodology, especially planning/review/software work |
| Semantic Router | `aurelio-labs/semantic-router` | semantic decision/routing component |
| AnythingLLM | `Mintplex-Labs/anything-llm` + official docs | knowledge/RAG/agent/workspace application and possible module substitute |

## 4. Research program

```text
R00 VERIFIED CURRENT PIPELINE BASELINE
  What is actually established already, and what remains only configured/pilot-level?
       |
       v
R01 GENERAL ALTERNATIVE LANDSCAPE
  Baseline vs CrewAI vs Agency Agents vs Superpowers vs Semantic Router vs AnythingLLM
       |
       +--> R02 CrewAI detailed integration/fit
       +--> R03 Agency Agents detailed integration/fit
       +--> R04 Superpowers detailed integration/fit
       +--> R05 Semantic Router detailed integration/fit
       +--> R06 AnythingLLM detailed integration/fit
       |
       v
R07 EVIDENCE MATRIX V1
  Module substitution/supplement matrix + MCDA + preliminary recommendation
       |
       v
R08 ADVERSARIAL EVIDENCE AUDIT
  Re-open every decision-changing source; attack every matrix cell and integration edge
       |
       v
R09 SOPHISTICATED V2 SYNTHESIS
  Final evidence-adjusted recommendation, exact keep/add/replace/defer/reject decisions
```

R02-R06 may run in parallel after R01 if Work supports it natively. Otherwise Work chooses the sequence. There are no routine operator approval gates.

## 5. Evidence standard

A feature existing in a README is not automatically established value.

Use this proof ladder:

1. **Current official product documentation / source code** — proves the capability exists and its exact mechanism.
2. **Official releases, tests, CI, examples** — proves maintained implementation and supported path.
3. **Direct operational evidence** — current issue reports, maintainer discussions, first-party production/customer case studies, reproducible integration reports.
4. **Objective adoption/maintenance evidence** — release cadence, repository activity, package/repo adoption metrics where available. Stars alone do not prove reliability.
5. **Secondary independent evidence** — useful for operational experience, never sole proof of a load-bearing capability.
6. **Model reasoning** — may interpret evidence but never counts as evidence.

Every decision-changing claim must be classified as one of:

- `VERIFIED_CAPABILITY`
- `VERIFIED_INTEGRATION`
- `VERIFIED_LIMITATION`
- `REPORTED_OPERATIONAL_EVIDENCE`
- `VENDOR_CLAIM_ONLY`
- `SUPPORTED_INFERENCE`
- `OPEN`
- `CONTRADICTED`

## 6. Matrix rule — no unsupported cells

Every substantive matrix cell must carry one or more evidence IDs/links. A cell without current evidence is `UNVERIFIED/OPEN`, not a model-generated score.

For each module/candidate cell record:

```text
CAPABILITY:
ROLE: KEEP | REPLACE | SUPPLEMENT | DUPLICATE | ORTHOGONAL | NO_FIT | OPEN
EVIDENCE_STATUS:
SOURCES:
EXACT_MECHANISM:
INTEGRATION_CLASS: native | official_plugin | official_protocol | established_package | documented_config | custom_required | none
LOCAL/REMOTE:
MODEL/API REQUIREMENT:
PERSISTENT_STATE:
DATA_EGRESS:
TOKEN/CONTEXT_EFFECT:
MATURITY/OPERATIONAL_EVIDENCE:
LIMITATIONS:
```

No recommendation may be derived from an unsupported cell.

## 7. Decision method

The final comparison follows current decision-analysis guidance rather than simple arbitrary weighted scoring:

- apply hard filters first;
- define operational criteria;
- complete the evidence matrix;
- use MCDA swing weighting only after the performance range between viable options is understood;
- test sensitivity/switching conditions;
- reduce uncertainty only when it could plausibly alter the recommendation.

Primary methodology sources:

- UK Green Book 2026: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
- NASA Decision Analysis: https://www.nasa.gov/reference/6-8-decision-analysis/

The Green Book explicitly distinguishes MCDA from simplistic MCA weighting/scoring and recommends swing weighting for complex technical trade-offs. NASA requires evaluation of every alternative against criteria, assumptions, uncertainty and recommendation robustness.

## 8. Full-function and reuse-first rules

- Do not lower a requirement to make a candidate look viable.
- Do not design an adapter merely because two systems could theoretically communicate.
- An integration is real only if current upstream documentation/source demonstrates it or an established protocol path exists on both sides.
- If integration requires bespoke glue, mark `CUSTOM_REQUIRED` and evaluate that as a material downside/blocker.
- Do not create parallel sources of truth for tasks, project facts, memory, retrieval indexes, or specialist definitions unless the candidate's verified value clearly outweighs the duplication.
- Do not assume adding more agents improves quality.
- Do not assume local means free, secure, or tokenless; trace the actual model/embedding/API path.

## 9. Real Master of Arts user stories

Every detailed candidate research must test at least these real operating patterns:

1. CEO intent -> correct project/workflow/specialist routing.
2. Research -> evidence -> project knowledge -> workshop/artifact.
3. One shared Marketing specialist -> two materially different project families.
4. Project-local knowledge retrieval without cross-family contamination.
5. Maker -> independent reviewer -> request-changes -> recovery.
6. Interrupted execution resumes from durable state.
7. Useful procedure learned in Project A is reusable in Project B without copying Project A facts.
8. Local/private project work preserves defined security boundaries.
9. Web/subscription AI can still read durable repo artifacts even when local runtime-only tools are unavailable.

## 10. Research outputs

Research specifications live in this workflow's `research/` directory.

Accepted results must be written under:

`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/`

Do not modify the completed R01-R07 baseline results.
Do not change ADR-002 or authorize installation from this workflow.

## 11. ChatGPT Work operating model

Use one Work session to execute the complete dependency graph autonomously. ChatGPT Work is explicitly intended for longer multi-step work across connected apps/files, and can use GitHub plus current web sources. Plan internally, but do not stop for routine plan approval.

OpenAI sources:

- https://openai.com/chatgpt-work/
- https://help.openai.com/en/articles/20001275/
- https://help.openai.com/en/articles/20001066

The operator should only be asked when a genuine decision gate in `AUTONOMOUS-PROGRAM-LAUNCHER.md` is reached.
