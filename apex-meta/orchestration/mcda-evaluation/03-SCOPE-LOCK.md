# 03 — Scope Lock: Master of Arts Orchestration

Status: **AUTHORITATIVE MCDA SCOPE INPUT**  
Decision profile: **A — Balanced MCDA weights accepted by operator**  
Date: **2026-08-21**

## 1. Source authority

The MCDA is now grounded primarily in the operator-supplied `master_of_arts_project_description.md` (2026-08-21). The supplied `Developing MoA Meta Workign file.docx` is supporting working material.

The previous assumption that a `Website/` directory was needed to define scope is superseded. Website work is one workflow/output family inside the larger Master of Arts operating model, not the scope authority for orchestration.

## 2. What the orchestration system is actually orchestrating

Master of Arts is simultaneously:

- an operating business;
- a knowledge-production system;
- a live experimentation/commercialization layer;
- a method-development system;
- a content/public-positioning system;
- a future source layer for Leela digital productization.

It is explicitly **not** reducible to one project type such as software, coaching, content, research, or website development.

## 3. Required workflow classes

A production orchestration framework must support all six classes without creating a separate project-management subsystem for each.

### W1 — Administrative workflows

Examples:

- invoices and payment tracking;
- customer records;
- session logs;
- email/customer communication;
- scheduling/booking support;
- bookkeeping preparation;
- SOP/template management;
- project/status records.

### W2 — Customer-delivery workflows

Examples:

- intake and first client talk;
- first-three-meetings design;
- session preparation;
- session execution/logging;
- client-specific adaptation;
- next-action and follow-up generation;
- Sequencing/coaching process application.

### W3 — Research and synthesis workflows

Examples:

- source ingestion;
- extraction and cross-reference;
- comparison of theories/methods;
- taxonomy/concept management;
- synthesis papers;
- research-to-practice translation;
- practitioner summaries;
- concept-to-offer translation.

### W4 — Content/public communication workflows

Examples:

- website/platform content;
- social media/video/short/blog production;
- long-form to micro-content reuse;
- public/private visibility checks;
- booking/offer linkage;
- recurring content cycles.

### W5 — Product/offer/workshop workflows

Examples:

- workshop/class/training/retreat design;
- concept evaluation by effort/value/risk/dependency;
- pricing hypotheses;
- pilot/test offer creation;
- launch readiness;
- physical/digital product work;
- community/event work.

### W6 — Leela translation workflows

Examples:

- method -> use case;
- session/process -> digital flow;
- entity/state/trigger/routine derivation;
- human-only vs software-supportable separation;
- product-spec precursor generation;
- provenance from real-world practice to software concept.

## 4. Required information model

The orchestration system must be able to coordinate work around linked entities rather than only flat tickets.

Core entities:

- concept;
- offer;
- project;
- workflow;
- client;
- session;
- research source;
- research synthesis;
- content asset;
- product;
- operational document;
- visibility class;
- Leela use case;
- SOP/template.

Important relations include:

- concept -> generates -> output;
- concept -> belongs to -> family;
- concept -> feeds -> Leela use case;
- research source -> supports -> concept;
- synthesis -> distills -> sources;
- content asset -> markets -> offer;
- session -> belongs to -> client/project;
- invoice -> belongs to -> client/service/project.

The selected framework does not need to implement a graph database. It **must** allow durable machine-readable links/relationships without requiring a custom orchestration database.

## 5. Mandatory metadata / decision dimensions

Work must be able to carry or reference:

- status/readiness;
- priority/critical path;
- public/private visibility;
- cost/effort;
- revenue/value potential;
- room/partner/social dependencies;
- research maturity;
- operational maturity;
- legal/reputational sensitivity;
- relation to Leela;
- provenance/evidence;
- owner/agent/reviewer;
- acceptance criteria;
- CEO decision state where applicable.

## 6. Governing business logic that orchestration must preserve

1. **Low effort / high leverage first.**
2. **Demand prioritization:** offers can be developed/perfected when need is demonstrated.
3. **Content before infrastructure overbuilding.**
4. **One concept can generate many outputs.**
5. **Operational simplicity matters.**
6. **Public/private layers must be deliberately separated.**
7. **Breadth must remain coherent rather than flatten into one generic category.**
8. **Master of Arts must work independently of Leela while remaining exportable into it.**
9. **Real-world work should generate reusable methods, evidence, learnings, and future product logic.**

## 7. Priority horizons

### Horizon A — immediate operations

Highest near-term reliability requirement:

- invoices/admin;
- communication;
- records/session logs;
- project overview;
- templates/SOPs;
- coaching preparation;
- booking/offer clarity.

### Horizon B — method formalization

- Sequencing;
- first-three-meetings;
- process documentation;
- research-backed coaching structures;
- converting tacit practice into explicit reusable methods.

### Horizon C — content and offer multiplication

- website/platform;
- content cycles;
- offer pages;
- workshops/classes/products;
- visibility policy;
- launches.

### Horizon D — Leela productization

- use cases;
- entities/states/triggers;
- machine-usable routines/flows;
- provenance into software/product architecture.

The orchestration framework should therefore work immediately for A/B while allowing C/D without replacement of the core project state model.

## 8. Consequences for candidate screening

The source definition strengthens or clarifies the existing hard gates:

### G9 — non-software extensibility becomes decisive

A coding-centric system cannot pass merely because arbitrary text can technically be stuffed into an issue. It must demonstrate usable workflows for at least administration, research, content/offer work, and live-service/workshop work.

### G3/C6 — durable linked state matters more

The framework must preserve relationships among concepts, outputs, sources, projects, offers, clients, and future Leela use cases without requiring chat reconstruction.

### G5/C4 — CEO governance must be explicit

The operator must be able to:

- set priorities;
- approve/reject consequential decisions;
- see conflicts;
- stop/re-scope work;
- choose among alternatives;
- allow agents to continue routine approved execution without repeated micromanagement.

### G6/C7 — deterministic mechanics should be first-class

Scheduling, status transitions, dependency checks, schema validation, file checks, recurring reviews, and mechanical routing should use deterministic automation where the chosen framework supports it.

### C5 — skills/process library must span heterogeneous output types

Reusable workflows are required for examples such as:

- workshop creation;
- research synthesis;
- content repurposing;
- client/session preparation;
- offer evaluation;
- recurring operating reviews;
- Leela use-case translation.

### C10 — token/context efficiency must include knowledge selection

Agents should not reread the entire business corpus for every task. The framework/composition must make it natural to load:

- relevant project/task state;
- linked source/evidence;
- applicable SOP/skill;
- current decision/acceptance criteria;
- compact prior handoff/history.

## 9. Representative portfolio lanes for MCDA pilots

Finalists must demonstrate that the **same core orchestration system** can manage at least these lanes:

| Lane | Example pilot output |
|---|---|
| Operations | invoice/customer follow-up workflow with approval boundary |
| Coaching/method | first-three-meetings / Sequencing method artifact |
| Research | source set -> grounded synthesis -> applied method candidate |
| Workshop | concept -> rough skeleton -> expert/reviewer iteration -> CEO approval |
| Content | source concept -> long-form/public asset -> derivative content queue |
| Portfolio | weekly prioritization across all active work |
| Leela bridge | approved Master of Arts method -> structured future software use-case candidate |

## 10. Explicit exclusions

This MCDA is **not** selecting:

- the final website architecture;
- the final coaching method;
- a custom ontology database;
- a custom RAG/knowledge platform;
- an AI model provider;
- a replacement for Git;
- a new homemade agent protocol.

Those may become downstream users/components of the selected orchestration system, but they are not the decision being made here.

## 11. Scope-lock test

A candidate is on-target only if the answer to all of these is yes:

1. Can the system coordinate work that ends in **documents, decisions, sessions, content, workshops, business actions, and software precursors**, not only code?
2. Can multiple AI clients understand the durable state without relying on one vendor's private conversation memory?
3. Can work be decomposed, claimed, reviewed, resumed, and accepted?
4. Can the operator remain the CEO while routine execution continues with low friction?
5. Can repeatable workflows become reusable skills/templates without inventing a parallel framework?
6. Can relevant context be retrieved progressively rather than loading the whole business into every prompt?
7. Can links/provenance from concept -> work -> output -> learning -> future Leela use case survive across sessions?

If not, the candidate cannot be the Master of Arts production orchestration core.
