# APEX Orchestration User Stories

## 1. Purpose

These seven user stories show how Alex uses the finished APEX orchestration system to complete real projects. They are workflow blueprints for Fable, not an exhaustive runtime specification.

The portfolio demonstrates one coherent model:

- four durable accountabilities—Alfred, Meta Strategy, Meta Ops, and Meta Detective;
- bounded specialists, domain workers, skills, and deterministic tools activated only when useful;
- independent validity review separated from strategic-alignment review;
- explicit repair routes to the owner of a defect;
- operator control over consequential choices;
- macro direction before meso workflow and micro execution;
- durable artifacts and state deltas instead of dependence on conversation memory.

Repository grounding was read from `leela-spec/apexai-os-meta@f4c81bf7fe5ad00b9bab6b83026071a7bb96d884`. No repository content was changed.

## 2. Reading Model

### Evidence labels

- **[V] Verified project fact:** directly supported by the repository or fixed project description.
- **[D] Accepted orchestration decision:** fixed by the operator request or a current locked Fable decision.
- **[I] Inferred workflow design:** a proposed use of the accepted architecture to make the project executable.
- **[E] External best-practice improvement:** a current primary-source practice translated into the story without adding a new APEX layer.

### Three levels

- **Macro** states the project target, constraints, smallest useful agent set, final deliverable, and observable completion condition.
- **Meso** shows the actual sequence, parallel branches, integrations, reviews, repair loops, and operator gates.
- **Micro** appears only where a difficult handoff, acceptance condition, deterministic check, or repair path must be unambiguous.

### Milestone rule

The full milestone loop is used when an output changes direction, authorizes substantial work, becomes public, changes durable knowledge, affects safety or compliance, or enables a major next phase:

```okf
milestone_loop:
  candidate: "Created by the accountable agent or bounded worker."
  integration: "Meta Ops reconciles dependencies and packages the candidate."
  validity: "Meta Detective issues pass, revise, hold, needs_input, or escalate."
  correction: "A failed criterion returns to the owner of that specific defect."
  revalidation: "Meta Detective reviews the corrected candidate, not the correction claim."
  alignment: "Meta Strategy checks the validated result against the macro objective."
  authority: "Alex approves consequential direction, release, mutation, spending, or external action."
  continuation: "Meta Ops opens only the next approved batch and records the state delta."
```

Low-impact work does not receive this whole ceremony. For example, a raw idea is not routed through Meta Strategy unless it could alter priorities, create a project, or change accepted doctrine.

## 3. Shared Agent and Skill Context

```okf
shared_context:
  core_agents:
    Alfred:
      accountability: "Operator interface, intake, constraints, decision presentation, and explicit operator response capture."
      must_not: "Execute project work, choose strategy, integrate the workflow, or validate outputs."
    Meta_Strategy:
      accountability: "Macro direction, options, leverage, timing, positioning, audience, and upward alignment review."
      must_not: "Implement artifacts, run project operations, or validate its own recommendation."
    Meta_Ops:
      accountability: "Meso workflow, bounded work packets, routing, dependencies, integration, durable state, and continuation."
      must_not: "Set final strategy, self-validate important work, or silently authorize durable mutation."
    Meta_Detective:
      accountability: "Independent evidence, contradiction, plausibility, safety, scope, drift, and authority-boundary review."
      must_not: "Implement the fix, become the orchestrator, or replace qualified external professionals."

  specialist_lanes:
    Knowledge_Bank: "Source custody, placement, candidate-versus-accepted status, provenance, and retrieval."
    Informatics_Design: "Terminology, taxonomy, artifact structure, scanability, and cross-asset consistency."
    Prompts_and_Workflows: "Reusable method, script, workflow, prompt, and handoff templates."
    activation_rule: "A specialist receives one bounded objective and returns an artifact to Meta Ops; it does not inherit orchestration."

  domain_workers:
    definition: "Temporary, context-isolated workers or human professionals assigned to a specific deliverable."
    rule: "They receive only the source slice, acceptance criteria, allowed tools, and stop condition needed for that deliverable."

  skill_harmony:
    rule: "A skill supports the accountable agent that invokes it; the skill never erases ownership."
    examples:
      - "Meta Ops may invoke project routing, handoff, source-map, script, workshop, requirements, or evidence-register skills."
      - "Meta Detective may invoke no-drift, contradiction, safety-boundary, and acceptance-criteria review skills."
      - "Meta Strategy may invoke option, leverage, positioning, or alignment-review skills."

  meta_ops_support_capabilities:
    apex_plan: "Produces a candidate execution skeleton, dependencies, and proposed next batches; it does not authorize them."
    apex_sync: "Computes deterministic status, dependency, evidence, stale-source, or asset-consistency reports; it does not make semantic choices."
    apex_session: "Records operator-approved state deltas, evidence links, verdicts, and next-session context; it does not invent work."

  durable_artifacts:
    minimum_set:
      - "macro target and accepted decisions"
      - "source and authority map"
      - "meso execution skeleton"
      - "bounded work packets and returned artifacts"
      - "Detective verdicts and named repair routes"
      - "Strategy alignment decisions"
      - "operator approvals"
      - "state delta and next-session packet"
    learning_rule: "After-action observations remain candidates until independently reviewed and accepted; no agent silently rewrites its own doctrine."
```

## 4. Portfolio Overview

| Story | Distinct orchestration challenge | Smallest useful durable set | Bounded specialist or worker use | Main operator gate | Final deliverable |
|---|---|---|---|---|---|
| **US-SEQ-01** | Strategic ambiguity → method → pilot → learning | Alfred, Strategy, Ops, Detective | Prompts & Workflows; coaching-method and pilot-design workers | Select method thesis; authorize pilot; accept/pivot after evidence | Pilot-ready coaching method and offer pack |
| **US-MEDIA-01** | One source concept → parallel, consistent public assets | Alfred, Strategy, Ops, Detective | Prompts & Workflows; Informatics Design; script/production/release workers | Approve series bible and pilot script; authorize release | Three-part pilot series and release pack |
| **US-LEELA-01** | Human-led value → bounded software behavior and backlog | Alfred, Strategy, Ops, Detective | Human-practice analyst; Informatics Design; requirements worker; Codex only after approval | Approve use case; approve implementation batch | Validated use-case specification and implementation-ready backlog |
| **US-WORKSHOP-01** | Embodied pedagogy, facilitator usability, and physical/child safety | Alfred, Strategy, Ops, Detective | Prompts & Workflows; exercise/pedagogy workers; qualified safety reviewer | Approve pilot scope and safety conditions | Pilot-ready Peaceful Warrior / Superhero Training package |
| **US-IDEA-01** | Messy input → preserved knowledge without premature project creation | Alfred, Ops, Detective | Knowledge Bank; Strategy only on consequential routing | Accept durable record; choose whether any project action follows | Source-preserving idea record and bounded action choice |
| **US-OFFER-01** | Demand validation before one-to-many commercial output | Alfred, Strategy, Ops, Detective | Demand, offer-copy, workshop, media, and informatics workers | Authorize demand test; proceed/pivot/stop; authorize launch | Validated fusion offer and coherent launch assets |
| **US-COMP-01** | High-risk external obligations, evidence, professionals, and recurring state | Alfred, Strategy, Ops, Detective | Knowledge Bank; Informatics Design; tax/legal/insurance/product professionals | Choose launch scope; approve submissions/spend/release | Controlled compliance operations system and evidence register |

## 5. Seven User Stories

### 5.1 US-SEQ-01 — Sequencing Coaching Format

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] The Master of Arts workflow records identify sequencing_coaching_format_definition as a macro workflow candidate."
    - "[V] The same corpus links Sequencing, routines, Flow/Session/Spark concepts, coaching, and possible Leela translation."
    - "[V] Sequencing-to-Leela is recorded as inferred and medium confidence; it must remain a downstream possibility, not an assumed product requirement."
  accepted_decisions:
    - "[D] The project first defines a pilot-ready coaching method and offer; it does not begin with detailed Leela implementation."
    - "[D] Important method and pilot milestones receive independent validity review, strategic alignment review, and operator approval."
  inferred_workflow_design:
    - "[I] A one-session pilot is the first micro batch; the full coaching format is expanded only after that unit survives review."
    - "[I] Leela implications are captured in a separate candidate note after pilot evidence exists."
  external_improvements:
    - "[E] Use an evaluator-optimizer loop only where explicit method criteria and pilot evidence make revision measurable."
    - "[E] Keep source material behind compact references and load only the material needed for the current method component."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: L32 and W08"
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/ProcessRanking_GPT&MasterOA.md: creation, divergence, systems, and verification stacks"
```

#### Macro

```okf
macro:
  story_id: "US-SEQ-01"
  project: "Sequencing Coaching Format"
  orchestration_type: "strategy-to-method-to-pilot learning loop"
  operator_goal: "Turn the existing Sequencing concept into a defined, pilot-ready coaching method and offer."
  starting_point: "Existing Sequencing, routine, coaching, Master of Arts, and possible Leela source material; the method is promising but not yet a locked offer."
  active_agents:
    core: [Alfred, Meta Strategy, Meta Ops, Meta Detective]
    specialists: [Prompts and Workflows]
    domain_workers: [coaching-method worker, pilot-design worker]
  final_deliverable: "A validated method brief, one-session pilot protocol, facilitator materials, offer brief, feedback instrument, and candidate Leela implications note."
  completion_condition: "Alex approves a method and offer whose audience, promise, principles, session structure, boundaries, pilot evidence plan, and revision criteria have passed independent validity and macro-alignment review."
```

#### Why this set is minimal

Strategy is required because the starting ambiguity is directional, not merely editorial. Ops is required because the method must become a staged pilot and durable offer pack. Detective is required because efficacy claims, source drift, and method contradictions cannot be accepted by their creators. Prompts & Workflows is activated only for the reusable method and session grammar; no separate knowledge or product agent is needed in the first phase.

#### Meso orchestration

```okf
meso:
  - stage: "1. Intake and target lock"
    owner: "Alfred"
    action: "Capture intended audience, coaching context, desired transformation, pilot constraints, non-goals, and whether Leela is in or out of the current scope."
    handoff: "Send an operator-intent packet to Meta Strategy."
    output: "Accepted intake packet."
    review_or_gate: "Alex confirms the target wording; no method design begins before this lock."

  - stage: "2. Macro option frame"
    owner: "Meta Strategy"
    action: "Develop two or three distinct method theses, each with audience, value, leverage, risks, and what must be learned in a pilot."
    handoff: "Return options through Alfred, not directly into execution."
    output: "Strategy option memo."
    review_or_gate: "Meta Detective checks unsupported assumptions; Alex selects one thesis or requests a bounded revision."

  - stage: "3. Candidate execution skeleton"
    owner: "Meta Ops"
    action: "Use Plan support to convert the selected thesis into method architecture, pilot design, evidence capture, offer definition, and explicit dependencies."
    handoff: "Open only the source-analysis and pilot-design batches."
    output: "Meso execution skeleton and source map."
    review_or_gate: "No full curriculum, website, or app backlog is authorized."

  - stage: "4. Parallel bounded development"
    owner: "Meta Ops"
    action: "Run a coaching-method worker on principles and sequence while a pilot-design worker defines one-session scope, feedback, and observable outcomes."
    handoff: "Each worker returns a self-contained artifact with source refs, uncertainties, and stop condition."
    output: "Method component map plus pilot hypothesis."
    review_or_gate: "Workers may not validate each other or expand into product architecture."

  - stage: "5. First method integration"
    owner: "Meta Ops"
    action: "Integrate the two returns into a concise method blueprint and one-session pilot, resolving only operational conflicts."
    handoff: "Package candidate with sources and acceptance criteria for Detective."
    output: "Candidate method-and-pilot pack v0.1."
    review_or_gate: "Meta Ops does not mark it valid."

  - stage: "6. Independent validity milestone"
    owner: "Meta Detective"
    action: "Check source fidelity, internal contradiction, plausible mechanism, boundaries, participant safety, unsupported transformation claims, and scope drift."
    handoff: "Issue a criterion-level verdict and name the owner of every defect."
    output: "Validity verdict."
    review_or_gate: "Revise routes to Strategy for a defective promise, the method worker for a defective method component, or Meta Ops for a dependency/integration defect."

  - stage: "7. Revalidation and upward alignment"
    owner: "Meta Strategy"
    action: "After Detective passes the corrected pack, check whether it still serves the selected audience, leverage, timing, positioning, and intended outcome."
    handoff: "Return aligned, redirect, or stop recommendation through Alfred."
    output: "Macro-alignment verdict."
    review_or_gate: "Alex approves the pilot promise, boundaries, and resource commitment."

  - stage: "8. Pilot micro build"
    owner: "Prompts and Workflows specialist"
    action: "Create only the approved one-session facilitator flow, participant prompts, timing sheet, and feedback instrument."
    handoff: "Return the pack to Meta Ops for integration."
    output: "Pilot kit v1."
    review_or_gate: "Detective checks the public/participant-facing kit; Strategy checks no drift from the selected thesis."

  - stage: "9. Human-led pilot and evidence capture"
    owner: "Alex or an approved facilitator"
    action: "Run the pilot; record observed friction, participant responses, deviations, safety issues, and outcome evidence without rewriting the method during delivery."
    handoff: "Provide raw evidence to Meta Ops."
    output: "Pilot evidence packet."
    review_or_gate: "No positive lesson is promoted from facilitator impression alone."

  - stage: "10. Evidence integration and learning loop"
    owner: "Meta Ops"
    action: "Use Sync support to compare intended versus actual sequence, outcomes, deviations, and missing evidence; draft candidate revisions."
    handoff: "Send evidence and candidate revisions to Detective."
    output: "Pilot review and candidate change set."
    review_or_gate: "Detective checks evidence quality; Strategy recommends keep, pivot, narrow, or stop; Alex decides."

  - stage: "11. Offer finalization and continuity"
    owner: "Meta Ops"
    action: "Finalize only the accepted method, pilot protocol, offer brief, and next experiment; isolate possible Leela implications as unaccepted candidates."
    handoff: "Use Session support to record approved state and next-session context."
    output: "Pilot-ready coaching offer pack and state delta."
    review_or_gate: "Completion requires fetch-back of all artifacts and an explicit operator acceptance record."
```

#### Critical handoff

```okf
handoff:
  from: "Meta Strategy"
  to: "Meta Ops"
  objective: "Operationalize the selected Sequencing thesis without changing its audience, promise, or non-goals."
  inputs: [operator-approved thesis, source refs, pilot questions, boundaries, excluded Leela work]
  return: "Method blueprint and one-session pilot with uncertainties and acceptance criteria."
  validator: "Meta Detective"
  next: "Strategy alignment and operator pilot gate after a pass."
  stop: "Stop if the method requires unsupported efficacy claims, concealed therapeutic scope, or an undefined target participant."
```

#### Micro controls and repair behavior

```okf
micro:
  first_batch_acceptance:
    - "One named audience and one pilot context."
    - "A short causal method hypothesis, explicitly marked as a hypothesis."
    - "A session sequence in which every step supports the transformation arc."
    - "Observable feedback signals and a stop condition."
    - "No Leela requirement, certification claim, therapeutic claim, or full-course expansion."
  repair_examples:
    - trigger: "Detective finds that the offer promise exceeds the available evidence."
      owner: "Meta Strategy"
      correction: "Narrow or reframe the promise; the facilitator-copy worker does not solve a strategy defect."
    - trigger: "The pilot activities do not operationalize the stated principle."
      owner: "coaching-method worker"
      correction: "Repair the method-to-activity mapping; Meta Ops then reintegrates."
    - trigger: "Pilot feedback contradicts the intended sequence."
      owner: "Meta Ops"
      correction: "Create a candidate sequence change, preserve raw evidence, and re-run Detective and Strategy review."
  continuity_artifacts: [method-decision-log, source-map, pilot-kit, evidence-packet, Detective-verdicts, accepted-change-set, next-session-packet]
```

---

### 5.2 US-MEDIA-01 — Morning Routine Media Series

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] Morning Routine appears in the Master of Arts project portfolio as a concrete project and media-output candidate."
    - "[V] The project-to-execution workflow includes a card to produce a Morning Routine video set with an expected three-video plan."
    - "[V] The corpus defines theory-to-content and media-output planning as reusable workflows."
  accepted_decisions:
    - "[D] The target is a coherent public series with scripts, production sequence, release assets, and efficient reuse of one source concept."
    - "[D] Public output requires independent validity review, strategic-alignment review, and an operator release gate."
  inferred_workflow_design:
    - "[I] A three-part pilot series is used because it is the concrete repository example; Alex may change the number at the macro gate."
    - "[I] One pilot episode and the series bible are validated before the remaining scripts fan out."
  external_improvements:
    - "[E] Parallelize only independent script and asset work after the shared source model and acceptance criteria are stable."
    - "[E] Use a compact series bible and just-in-time source packets to prevent each worker from re-reading the entire project corpus."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: L20, L30, W03"
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/ProcessRanking_GPT&MasterOA.md: master creation and durable orchestration relationships"
```

#### Macro

```okf
macro:
  story_id: "US-MEDIA-01"
  project: "Morning Routine Media Series"
  orchestration_type: "single-source multi-asset production fan-out"
  operator_goal: "Turn the mature Morning Routine practice into a coherent media series with scripts, production sequence, and release assets."
  starting_point: "An existing Morning Routine practice and project context, plus a repository-backed three-video planning candidate; detailed episode content must come from the actual source material."
  active_agents:
    core: [Alfred, Meta Strategy, Meta Ops, Meta Detective]
    specialists: [Prompts and Workflows, Informatics Design]
    domain_workers: [pilot-script worker, episode-script workers, production-plan worker, release-asset worker]
  final_deliverable: "An approved series bible, three scripts, shot and production sequence, asset register, release copy, and publication checklist."
  completion_condition: "Every public asset traces to the approved source concept, uses consistent terminology and promise, passes independent public-facing review, and is ready for an operator-approved production and release sequence."
```

#### Why this set is minimal

Strategy is needed once to lock audience, series promise, and release purpose. Ops then owns the reusable production spine. Informatics Design prevents terminology and asset inconsistency; Prompts & Workflows supports script grammar. Detective independently reviews source fidelity, public claims, and cross-asset contradictions. No separate standing media department is created; temporary workers handle bounded episodes and asset types.

#### Meso orchestration

```okf
meso:
  - stage: "1. Series intake"
    owner: "Alfred"
    action: "Capture target audience, channels, preferred format, source corpus, tone constraints, production capacity, release horizon, and excluded claims."
    handoff: "Send a media-intent packet to Meta Strategy."
    output: "Accepted series objective."
    review_or_gate: "Alex confirms whether the initial target is the repository-backed three-part pilot."

  - stage: "2. Macro series direction"
    owner: "Meta Strategy"
    action: "Define the audience problem, series promise, episode progression, positioning, and success signal."
    handoff: "Send only the selected direction to Meta Ops."
    output: "Series strategy brief."
    review_or_gate: "Detective checks that the promise is supported by source material; Alex selects the direction."

  - stage: "3. Source-to-asset model"
    owner: "Meta Ops"
    action: "Create a source concept map and Plan-supported production skeleton covering bible, pilot script, remaining episodes, production, release, and review dependencies."
    handoff: "Assign Informatics Design only the terminology and asset taxonomy task."
    output: "Source map, asset graph, and work packets."
    review_or_gate: "No script worker receives the whole corpus or an unbounded 'make content' instruction."

  - stage: "4. Series bible and pilot episode"
    owner: "Prompts and Workflows specialist"
    action: "Create the reusable episode grammar and one complete pilot script from the approved source slice."
    handoff: "Return source refs, reused elements, new claims, and production assumptions to Meta Ops."
    output: "Series bible v0.1 and pilot script."
    review_or_gate: "This stage is sequential; fan-out waits for validation."

  - stage: "5. Pilot milestone review"
    owner: "Meta Detective"
    action: "Check source fidelity, public plausibility, unsupported health or performance claims, contradiction, tone, scope, and audience fit."
    handoff: "Return criterion-level defects to the script specialist or Strategy, depending on ownership."
    output: "Pilot validity verdict."
    review_or_gate: "After a pass, Meta Strategy checks the pilot against the series objective and Alex approves the bible."

  - stage: "6. Controlled parallel fan-out"
    owner: "Meta Ops"
    action: "Open separate packets for episodes two and three, production sequencing, and release assets using the approved bible and shared source map."
    handoff: "Run independent packets in parallel; each return includes changed terms, claims, dependencies, and missing inputs."
    output: "Candidate scripts, shot plan, production schedule, metadata, thumbnails brief, and release copy."
    review_or_gate: "Workers do not rewrite the bible or each other's assets."

  - stage: "7. Fan-in and deterministic consistency report"
    owner: "Meta Ops"
    action: "Integrate returned assets and use Sync support to compute asset completeness, terminology consistency, source coverage, dependencies, and reuse."
    handoff: "Provide the integrated release candidate and consistency report to Detective."
    output: "Series release candidate."
    review_or_gate: "Meta Ops reports conflicts but does not self-certify them resolved."

  - stage: "8. Independent cross-asset review"
    owner: "Meta Detective"
    action: "Review each asset and the set as a whole for evidence, contradiction, repeated or missing content, public risk, scope, and drift."
    handoff: "Route local defects to the responsible asset worker; route repeated defects to the bible owner; route positioning defects to Strategy."
    output: "Cross-asset validity verdict and repair map."
    review_or_gate: "Only failed assets reopen; passed independent assets are not regenerated."

  - stage: "9. Strategic release alignment"
    owner: "Meta Strategy"
    action: "Check whether the validated series still has the intended sequence, audience, positioning, leverage, and release timing."
    handoff: "Present release, reorder, narrow, or hold options through Alfred."
    output: "Release recommendation."
    review_or_gate: "Alex approves production and publication sequence."

  - stage: "10. Production and release control"
    owner: "Meta Ops"
    action: "Track recording, editing, approvals, filenames, versions, and release dependencies in the durable asset register."
    handoff: "Send only changed public assets for final Detective delta review."
    output: "Production-ready and then release-ready asset set."
    review_or_gate: "Alex performs the final external publication action."

  - stage: "11. Release learning and continuity"
    owner: "Meta Ops"
    action: "Record actual release evidence and candidate lessons without changing the series doctrine."
    handoff: "Detective checks evidence quality; Strategy decides whether the next series changes direction."
    output: "Release evidence and next-series candidate note."
    review_or_gate: "Session support records only operator-accepted changes and the next-session packet."
```

#### Critical handoff

```okf
handoff:
  from: "Meta Ops"
  to: "episode-script worker"
  objective: "Write one assigned episode that advances the approved series progression."
  inputs: [approved series bible, episode objective, bounded source slice, prior-episode summary, claims boundary, output template]
  return: "Script, source trace, reused assets, new-claim list, and unresolved production questions."
  validator: "Meta Detective"
  next: "Meta Ops integration after a pass."
  stop: "Stop rather than invent practice details, credentials, health effects, or visual assets absent from the source packet."
```

#### Micro controls and repair behavior

```okf
micro:
  series_bible_acceptance:
    - "One audience, promise, tone, canonical term set, episode progression, and call-to-action rule."
    - "A source concept inventory that distinguishes direct practice content from inferred explanatory framing."
    - "A reuse map for opening, closing, visual language, and release metadata."
  repair_examples:
    - trigger: "Episode two repeats episode one and fails to advance the progression."
      owner: "episode-two script worker"
      correction: "Rewrite only the duplicated sections against the episode objective; preserve passed content."
    - trigger: "Several assets use conflicting names for the same Morning Routine component."
      owner: "Informatics Design specialist"
      correction: "Repair the canonical term map; Meta Ops propagates a deterministic change list to affected assets."
    - trigger: "The series promise no longer matches the approved audience."
      owner: "Meta Strategy"
      correction: "Revise positioning or recommend hold; copy workers do not decide the strategic promise."
  continuity_artifacts: [series-strategy-brief, source-map, series-bible, asset-register, script-versions, review-verdicts, release-record, next-series-candidates]
```

---

### 5.3 US-LEELA-01 — Master of Arts to Leela Use-Case Translation

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] The workflow database defines a Sequencing Coaching Format to Leela Use Case process with scenario, Spark/Session/Flow mapping, agent interaction, product backlog, and canonical-term review."
    - "[V] Its explicit failure condition is turning an inspirational or coaching principle directly into an implementation specification."
    - "[V] The source leaves implementation granularity open: conceptual use case, screen flow, data model, or agent workflow."
  accepted_decisions:
    - "[D] This story translates a mature human-led Master of Arts practice into a bounded Leela use case and requirements before any Codex execution."
    - "[D] Human-only value and software-supportable behavior must be separated explicitly."
  inferred_workflow_design:
    - "[I] A human-value boundary map is the gate between practice analysis and requirements."
    - "[I] Codex receives only an operator-approved vertical slice after requirement and backlog validation."
  external_improvements:
    - "[E] Use structured outputs between analysis, requirements, and implementation to constrain drift and unsafe downstream interpretation."
    - "[E] Treat data/resources, reusable prompts, and executable tools as distinct surfaces; approval is required before write-side action."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: W08"
    - "apex-meta/kb/apex-plan-sync-session-workflow-v2/wiki/concepts/proposal-computation-mutation-split.md"
    - "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/project-execution-state-safety-model.md"
```

#### Macro

```okf
macro:
  story_id: "US-LEELA-01"
  project: "Master of Arts to Leela Use-Case Translation"
  orchestration_type: "human-practice decomposition to product requirements and gated implementation"
  operator_goal: "Translate a mature human-led Master of Arts practice into a bounded Leela use case, requirements, and implementation-ready backlog."
  starting_point: "A real human-led practice, existing Master of Arts and Sequencing material, and a repository-defined Leela translation workflow; product granularity is not assumed."
  active_agents:
    core: [Alfred, Meta Strategy, Meta Ops, Meta Detective]
    specialists: [Prompts and Workflows, Informatics Design]
    domain_workers: [human-practice analyst, product-requirements worker, Codex implementation worker after approval]
  final_deliverable: "A validated use-case specification, human/software boundary map, canonical flow, requirements, acceptance criteria, dependency-aware backlog, and optional approved vertical-slice implementation packet."
  completion_condition: "Alex approves a use case that preserves human-only value, defines software-supportable behavior and limits, passes terminology, evidence, privacy, safety, and scope review, and is ready for a bounded implementation decision."
```

#### Why this set is minimal

This project needs Strategy to decide whether digitization creates real user value, Ops to translate practice into requirements, Informatics Design to keep canonical terms and data boundaries coherent, and Detective to catch unsupported product architecture and human-value loss. A human-practice analyst and requirements worker are temporary. Codex is not active until the operator approves an implementation packet.

#### Meso orchestration

```okf
meso:
  - stage: "1. Practice and product intake"
    owner: "Alfred"
    action: "Capture the exact human-led practice, target user, trigger, desired outcome, current pain, Leela context, and requested implementation granularity."
    handoff: "Send a locked problem packet to Meta Strategy."
    output: "Accepted problem statement."
    review_or_gate: "Alex confirms that the selected practice is mature enough to analyze and that no code is yet authorized."

  - stage: "2. Product-value frame"
    owner: "Meta Strategy"
    action: "Define the user value, strategic fit, leverage, timing, and the questions that would make digitization inappropriate."
    handoff: "Send the approved product question and exclusions to Meta Ops."
    output: "Use-case thesis and non-goals."
    review_or_gate: "Detective checks for assumed benefits or hidden implementation commitments; Alex selects proceed, narrow, or stop."

  - stage: "3. Human-practice decomposition"
    owner: "human-practice analyst"
    action: "Map the real practice step by step, including human judgment, relationship, embodiment, consent, ambiguity, exceptions, and evidence used by the practitioner."
    handoff: "Return a source-traced practice map to Meta Ops."
    output: "As-is human practice map."
    review_or_gate: "Stop if the source material does not support a stable practice description."

  - stage: "4. Human/software boundary"
    owner: "Meta Ops"
    action: "Classify each practice function as human-only, software-supportable, software-automatable with approval, or out of scope."
    handoff: "Ask Informatics Design to normalize terms and object relationships without inventing product behavior."
    output: "Boundary map and canonical vocabulary."
    review_or_gate: "Alex reviews any function whose automation could weaken human agency or alter the practice."

  - stage: "5. Candidate use-case flow"
    owner: "Prompts and Workflows specialist"
    action: "Convert only the approved software-supportable functions into a user scenario and canonical Leela flow."
    handoff: "Return trigger, actor, state, interaction, outputs, exceptions, and human checkpoints."
    output: "Candidate use-case flow."
    review_or_gate: "No screen, data model, or agent architecture is invented unless that granularity was approved."

  - stage: "6. Requirements and acceptance batch"
    owner: "product-requirements worker"
    action: "Write the smallest requirement set and observable acceptance criteria for one coherent use-case slice."
    handoff: "Return requirement-to-source and requirement-to-user-value traceability."
    output: "Candidate requirements and test scenarios."
    review_or_gate: "Meta Ops integrates dependencies but cannot approve requirements."

  - stage: "7. Independent validity milestone"
    owner: "Meta Detective"
    action: "Check source fidelity, canonical terminology, human/software boundary, privacy, consent, safety, scope, contradictions, testability, and unsupported architecture."
    handoff: "Route practice defects to the analyst, terminology defects to Informatics Design, requirement defects to the requirements worker, and integration defects to Meta Ops."
    output: "Validity verdict and repair map."
    review_or_gate: "The corrected package receives a new Detective verdict."

  - stage: "8. Upward product alignment"
    owner: "Meta Strategy"
    action: "Assess whether the validated use case still preserves the intended human value, serves the target user, has sufficient leverage, and is timely relative to other Leela work."
    handoff: "Present proceed, defer, narrow, or reject through Alfred."
    output: "Product-alignment decision."
    review_or_gate: "Alex approves the use-case definition before backlog creation."

  - stage: "9. Backlog and implementation packet"
    owner: "Meta Ops"
    action: "Use Plan support to decompose the approved use case into dependency-aware backlog items, each with acceptance criteria, source refs, allowed files/surfaces, and stop conditions."
    handoff: "Use Sync support to check dependency completeness and requirement coverage."
    output: "Implementation-ready backlog and candidate first vertical slice."
    review_or_gate: "Detective validates scope and testability; Strategy checks no product drift; Alex authorizes or declines implementation."

  - stage: "10. Optional Codex vertical slice"
    owner: "Codex implementation worker"
    action: "Implement only the approved first slice in an isolated, reviewable batch using the supplied requirements and repository constraints."
    handoff: "Return code diff, tests, implementation notes, and deviations to Meta Ops."
    output: "Candidate implementation."
    review_or_gate: "Deterministic tests run first; Meta Detective then reviews requirement fidelity and authority boundaries."

  - stage: "11. Implementation repair and acceptance"
    owner: "Meta Ops"
    action: "Route failed tests to Codex, requirement ambiguity to the requirements worker, and product mismatch to Strategy; reintegrate only passed corrections."
    handoff: "Provide the revalidated delta to Alfred."
    output: "Accepted vertical slice or held implementation."
    review_or_gate: "Alex decides merge/release; no model self-authorizes mutation."

  - stage: "12. Durable continuation"
    owner: "Meta Ops"
    action: "Use Session support to record accepted requirements, verdicts, backlog state, implementation evidence, unresolved boundaries, and the next approved batch."
    handoff: "Next session loads the compact state packet and retrieves deeper sources only as needed."
    output: "Use-case state packet."
    review_or_gate: "Completion is claimed only after artifact fetch-back and state-delta verification."
```

#### Critical handoff

```okf
handoff:
  from: "Meta Ops"
  to: "product-requirements worker"
  objective: "Specify one approved Leela use-case slice without digitizing excluded human-only functions."
  inputs: [approved use-case thesis, as-is practice map, human-software boundary, canonical vocabulary, source refs, non-goals]
  return: "Requirements, exceptions, acceptance criteria, traceability matrix, and unresolved decisions."
  validator: "Meta Detective"
  next: "Meta Strategy product-alignment review after validity pass."
  stop: "Stop if a requirement depends on an undefined human judgment, an unapproved data category, or unsupported product architecture."
```

#### Micro controls and repair behavior

```okf
micro:
  boundary_categories:
    human_only: "Requires relationship, embodied observation, ethical judgment, consent negotiation, or practitioner accountability that software should not replace."
    software_supportable: "Organizes, prompts, retrieves, visualizes, or records while leaving the decision with the person."
    approval_automation: "May perform a reversible action only after explicit user confirmation."
    excluded: "Creates unacceptable safety, privacy, autonomy, or product-scope risk."
  first_slice_acceptance:
    - "One concrete actor, trigger, goal, and successful end state."
    - "Every requirement traces to an approved user need and source."
    - "Human checkpoints and failure recovery are visible."
    - "Acceptance can be observed or tested without relying on the author's confidence."
  repair_examples:
    - trigger: "A requirement automates a human-only coaching judgment."
      owner: "Meta Ops boundary-map owner"
      correction: "Reclassify the function and repair downstream requirements; do not ask Codex to encode the ambiguity."
    - trigger: "The use case uses noncanonical Leela terminology."
      owner: "Informatics Design specialist"
      correction: "Repair the vocabulary and issue a deterministic affected-artifact list."
    - trigger: "Code passes tests but violates the accepted user journey."
      owner: "Codex implementation worker"
      correction: "Repair implementation against requirements; Detective revalidates the behavior, not merely the tests."
  continuity_artifacts: [practice-map, boundary-map, canonical-vocabulary, use-case-spec, traceability-matrix, validated-backlog, implementation-evidence, next-session-packet]
```

---

### 5.4 US-WORKSHOP-01 — Peaceful Warrior / Superhero Training

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] Peaceful Warrior / Superhero Training is identified as a high-value source for workshop creation, facilitation logic, child safety, embodied progression, and iterative refinement."
    - "[V] The workshop workflow requires audience, transformation arc, phase sequence, exercises, facilitation, safety, transfer, and revision."
    - "[V] The corpus separately records embodied-technique-to-drill and scan-optimized workshop architecture processes."
  accepted_decisions:
    - "[D] The output is a pilot-ready embodied training or workshop package, not merely an inspirational concept document."
    - "[D] Physical or child-safety concerns require independent review and qualified human expertise where applicable."
  inferred_workflow_design:
    - "[I] The first implementation batch is one pilot format and one facilitator dry run, not all audience variants."
    - "[I] A one-screen scan map is produced only after the full workshop logic is stable."
  external_improvements:
    - "[E] Use explicit human intervention for high-risk activity and set stop conditions for unclear participant, contact, venue, or supervision constraints."
    - "[E] Design recovery and correction for when the system or facilitator plan is wrong, not only the ideal execution path."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: S06, W05, W06, W07"
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/ProcessRanking_GPT&MasterOA.md: workshop-production stack"
```

#### Macro

```okf
macro:
  story_id: "US-WORKSHOP-01"
  project: "Peaceful Warrior / Superhero Training"
  orchestration_type: "embodied pedagogy and safety-gated pilot design"
  operator_goal: "Turn the existing concept and source material into a pilot-ready embodied training or workshop package."
  starting_point: "Existing concept, workshop, embodied-practice, and safety material; the target audience, duration, venue, contact level, and pilot boundaries still require an operator decision."
  active_agents:
    core: [Alfred, Meta Strategy, Meta Ops, Meta Detective]
    specialists: [Prompts and Workflows, Informatics Design]
    domain_workers: [pedagogy worker, exercise-design worker, facilitator-usability tester, qualified safety reviewer]
  final_deliverable: "A pilot workshop pack containing transformation arc, phase plan, exercise cards, facilitator guide, safety and inclusion controls, scan map, materials list, and feedback instrument."
  completion_condition: "A facilitator can run the bounded pilot from the pack; independent and qualified reviews have cleared or explicitly held safety-sensitive elements; Alex approves the pilot conditions and the evidence-based revision path."
```

#### Why this set is minimal

Strategy is needed to define the transformation arc and audience rather than prematurely assembling exercises. Ops is needed to sequence embodied, pedagogical, logistical, and review work. Prompts & Workflows supports facilitator and exercise grammar; Informatics Design is used only for facilitator usability and the final scan map. Detective reviews evidence, drift, and safety boundaries but does not substitute for a qualified physical or child-safety professional.

#### Meso orchestration

```okf
meso:
  - stage: "1. Pilot intake and risk context"
    owner: "Alfred"
    action: "Capture audience and age, group size, duration, venue, supervision, contact level, accessibility, desired transformation, source materials, and explicit exclusions."
    handoff: "Send a locked workshop-intent packet to Meta Strategy."
    output: "Accepted pilot context."
    review_or_gate: "Alex resolves the audience and safety context before exercise design."

  - stage: "2. Transformation and pedagogical direction"
    owner: "Meta Strategy"
    action: "Define the transformation arc, core principle, participant promise, positioning, and what the pilot must demonstrate."
    handoff: "Return one selected direction and rejected alternatives to Meta Ops."
    output: "Workshop strategy brief."
    review_or_gate: "Detective checks unsupported outcome claims; Alex approves the direction."

  - stage: "3. Phase skeleton before exercises"
    owner: "Meta Ops"
    action: "Use Plan support to build the phase sequence from arrival and safety through embodied learning, integration, and transfer."
    handoff: "Open separate pedagogy and exercise packets only after the skeleton is stable."
    output: "Meso workshop architecture."
    review_or_gate: "No facilitator script or visual compression is produced yet."

  - stage: "4. Parallel bounded design"
    owner: "Meta Ops"
    action: "Run a pedagogy worker on learning progression and an exercise-design worker on solo/partner drills, cues, regressions, progressions, and observable feedback."
    handoff: "Workers return source links, risks, prerequisites, and alternatives for each component."
    output: "Pedagogy map and exercise set."
    review_or_gate: "Exercise workers cannot assert real-world self-defense efficacy or approve safety."

  - stage: "5. Workshop integration"
    owner: "Meta Ops"
    action: "Integrate only compatible exercises into the phase skeleton; add timing, transitions, materials, facilitator decisions, and contingency branches."
    handoff: "Package the candidate with a risk register for Detective and the qualified reviewer."
    output: "Candidate workshop pack v0.1."
    review_or_gate: "Ops marks uncertainties and does not self-clear them."

  - stage: "6. Independent validity and safety review"
    owner: "Meta Detective"
    action: "Check source fidelity, age fit, contact risk, scope, overclaim, contradiction, consent visibility, and facilitator assumptions."
    handoff: "In parallel, send physical/child-safety questions and activity descriptions to the qualified safety reviewer."
    output: "Detective verdict plus professional safety response."
    review_or_gate: "A Detective pass cannot override a professional hold; absent qualified review, sensitive activities remain held."

  - stage: "7. Named repair loop"
    owner: "Meta Ops"
    action: "Route learning-sequence defects to the pedagogy worker, exercise mechanics to the exercise worker, facilitator ambiguity to Prompts & Workflows, and safety controls to the qualified reviewer for confirmation."
    handoff: "Reintegrate the corrected components with a change log."
    output: "Corrected workshop pack."
    review_or_gate: "Detective issues a new verdict; it does not implement the fixes."

  - stage: "8. Upward alignment and pilot gate"
    owner: "Meta Strategy"
    action: "Check whether the validated pack still creates the intended transformation for the chosen audience and fits the available time, venue, and positioning."
    handoff: "Present pilot, narrow, redesign, or stop options through Alfred."
    output: "Pilot recommendation."
    review_or_gate: "Alex approves exact pilot scope, facilitator, safety conditions, and stop rules."

  - stage: "9. Facilitator usability batch"
    owner: "Prompts and Workflows specialist"
    action: "Create the facilitator guide, exercise cards, exact safety prompts, transition cues, and contingency wording."
    handoff: "Send the pack to a facilitator-usability tester who did not author it."
    output: "Facilitator-ready pilot kit."
    review_or_gate: "Tester records where hidden reasoning or missing context prevents execution."

  - stage: "10. Scan map and final pre-pilot review"
    owner: "Informatics Design specialist"
    action: "Compress the stable workshop into a one-screen architecture map without replacing the facilitator guide."
    handoff: "Return map and trace to the full pack."
    output: "Workshop scan map."
    review_or_gate: "Detective checks that compression has not removed safety, progression, or transfer logic."

  - stage: "11. Human-led pilot and evidence"
    owner: "Alex or approved facilitator"
    action: "Run the pilot within the approved conditions and record participation, deviations, incidents, exercise usability, timing, and outcome evidence."
    handoff: "Provide raw feedback and incident data to Meta Ops."
    output: "Pilot evidence packet."
    review_or_gate: "Any incident triggers hold and review before another run."

  - stage: "12. Revision and durable continuation"
    owner: "Meta Ops"
    action: "Use Sync support to compare planned and actual delivery; create bounded candidate changes and preserve raw evidence."
    handoff: "Detective checks evidence and risk; Strategy checks transformation alignment; Alex accepts the next version."
    output: "Pilot-ready v2 or explicit hold record."
    review_or_gate: "Session support records accepted changes, unresolved risks, and next-session context."
```

#### Critical handoff

```okf
handoff:
  from: "Meta Ops"
  to: "qualified safety reviewer"
  objective: "Review only the physical, child-safety, consent, contact, supervision, and emergency-control aspects of the proposed pilot."
  inputs: [audience profile, venue, group size, facilitator qualifications, exercise descriptions, intensity, contact rules, contingency plan]
  return: "Clear, conditionally clear, revise, or hold verdict with named conditions and unresolved questions."
  validator: "Meta Detective checks that the professional conditions are accurately represented and not diluted."
  next: "Meta Ops routes required changes to their owners."
  stop: "Stop the pilot if the reviewer cannot assess the risk from the supplied information or identifies an unresolved high-severity concern."
```

#### Micro controls and repair behavior

```okf
micro:
  exercise_card_acceptance:
    - "Purpose, setup, participant level, duration, cues, success signal, regression, progression, contact rule, and stop signal."
    - "No exercise relies on facilitator intuition that is absent from the guide."
    - "No speculative combat effect is presented as established safety or efficacy."
  repair_examples:
    - trigger: "An exercise is engaging but breaks the transformation progression."
      owner: "pedagogy worker"
      correction: "Reposition, replace, or remove it; the safety reviewer is not asked to solve pedagogy."
    - trigger: "A partner drill has unclear consent or contact boundaries."
      owner: "exercise-design worker with qualified reviewer confirmation"
      correction: "Add explicit setup, opt-out, intensity, stop, and supervision controls; revalidate."
    - trigger: "The scan map is readable but omits a critical safety phase."
      owner: "Informatics Design specialist"
      correction: "Repair the compressed representation; do not rewrite the underlying passed workshop."
  continuity_artifacts: [workshop-strategy-brief, phase-skeleton, exercise-cards, risk-register, professional-verdict, facilitator-guide, scan-map, pilot-evidence, accepted-revisions]
```

---

### 5.5 US-IDEA-01 — Raw Voice Idea to Knowledge and Project Action

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] The Audio-to-Idea workflow accepts spoken or rough notes that may be multilingual, nonlinear, emotional, repetitive, or incomplete."
    - "[V] Its output includes a structured Markdown entry, metadata, tags, project mapping, rules, next actions, and clustering links."
    - "[V] Its pass condition is semantic fidelity; its failure example is turning a raw insight into generic self-help language."
  accepted_decisions:
    - "[D] Candidate classification and project links remain separate from accepted durable knowledge."
    - "[D] A raw idea does not automatically create a project, task, rule, or skill."
  inferred_workflow_design:
    - "[I] The default path uses Alfred, Meta Ops, Knowledge Bank, and Meta Detective only; Strategy is conditional."
    - "[I] One idea record is the entire micro batch, allowing a fast operator acceptance gate."
  external_improvements:
    - "[E] Use structured fields to constrain downstream interpretation while retaining the raw source as the semantic anchor."
    - "[E] Keep the operator able to correct the AI when it is wrong and record accepted correction over time."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: S05 and W04"
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/ProcessRanking_GPT&MasterOA.md: knowledge-bank stack"
```

#### Macro

```okf
macro:
  story_id: "US-IDEA-01"
  project: "Raw Voice Idea to Knowledge and Project Action"
  orchestration_type: "semantic-preservation intake and candidate routing"
  operator_goal: "Convert a rough voice idea into preserved knowledge, correct classification, project connections, and bounded next actions."
  starting_point: "One raw voice note or transcript whose meaning may be incomplete, mixed-language, nonlinear, emotional, repetitive, or cross-project."
  active_agents:
    core: [Alfred, Meta Ops, Meta Detective]
    specialists: [Knowledge Bank]
    domain_workers: [Meta Strategy only when the idea changes priorities or proposes a new project]
  final_deliverable: "A source-preserving idea record with confidence-marked classification, candidate project links, explicit uncertainties, and zero or a few bounded next-action options."
  completion_condition: "The raw source is retained; the structured entry passes independent fidelity and placement review; Alex accepts, edits, or rejects durable mutation and separately chooses whether any project action follows."
```

#### Why this set is minimal

This is a compact knowledge operation, not a portfolio-planning project. Alfred captures the note and operator intent. Meta Ops structures it. Knowledge Bank handles placement and candidate status. Detective protects meaning and source custody. Strategy is activated only if the idea could redirect accepted priorities, create a project, or alter a cross-project principle.

#### Meso orchestration

```okf
meso:
  - stage: "1. Preserve before interpreting"
    owner: "Alfred"
    action: "Capture the raw audio or transcript, language, date, operator label, immediate context, and any explicit instruction about privacy or intended project."
    handoff: "Send the untouched source plus intake metadata to Meta Ops."
    output: "Immutable source record and intake note."
    review_or_gate: "No summary replaces the raw source."

  - stage: "2. Candidate structured entry"
    owner: "Meta Ops"
    action: "Invoke the idea-entry skill to distill the core, preserve unresolved roughness, and propose tags, claims, principles, project links, and small next actions."
    handoff: "Send source and candidate entry to Knowledge Bank."
    output: "Candidate idea record."
    review_or_gate: "All uncertain interpretations and mappings are marked tentative."

  - stage: "3. Placement and lifecycle check"
    owner: "Knowledge Bank specialist"
    action: "Check source identity, duplicate or related records, correct knowledge lane, candidate status, and whether the idea belongs in an existing project rather than a new one."
    handoff: "Return placement recommendation, related links, and unresolved classification questions."
    output: "Placement packet."
    review_or_gate: "The specialist does not promote the entry or create a project."

  - stage: "4. Independent fidelity review"
    owner: "Meta Detective"
    action: "Compare the candidate entry to the raw source for omission, over-cleaning, invented certainty, generic reframing, contradiction, privacy, and authority drift."
    handoff: "Return semantic defects to Meta Ops and placement defects to Knowledge Bank."
    output: "Fidelity and placement verdict."
    review_or_gate: "A failed entry is corrected and revalidated before Alex sees an acceptance choice."

  - stage: "5. Durable-knowledge gate"
    owner: "Alfred"
    action: "Present the raw source link, concise candidate entry, uncertain mappings, and Detective verdict."
    handoff: "Capture Alex's accept, edit, reject, or hold decision."
    output: "Operator decision."
    review_or_gate: "This gate authorizes knowledge mutation only, not a new project or task."

  - stage: "6. Accepted state mutation"
    owner: "Meta Ops"
    action: "Use Session support to write the accepted idea record and a narrow state delta; preserve rejected alternatives and source provenance where useful."
    handoff: "Use Sync support only if existing project links or duplicate indexes require deterministic updates."
    output: "Accepted knowledge entry and verified index delta."
    review_or_gate: "Fetch back the stored entry and confirm exact status and links."

  - stage: "7. Conditional strategic routing"
    owner: "Meta Strategy"
    action: "Only when triggered, assess whether the accepted idea changes project priority, creates a new opportunity, or is merely a note inside existing work."
    handoff: "Return a small set of route options to Alfred; do not create the project."
    output: "Optional leverage and routing note."
    review_or_gate: "Detective checks unsupported strategic claims; Alex chooses no action, attach to project, create candidate project, or schedule a bounded experiment."

  - stage: "8. Bounded action creation"
    owner: "Meta Ops"
    action: "Create only the operator-selected next action or candidate project packet with owner, output, source link, and stop condition."
    handoff: "Record the link from action back to the idea source."
    output: "Optional bounded action."
    review_or_gate: "No automatic cascade into multiple tasks, content assets, or skills."
```

#### Critical handoff

```okf
handoff:
  from: "Alfred"
  to: "Meta Ops"
  objective: "Structure the idea without losing source meaning or deciding its strategic importance."
  inputs: [raw audio or transcript, intake metadata, explicit operator wording, privacy constraints]
  return: "Candidate record with core meaning, preserved nuance, tentative tags, candidate links, uncertainties, and bounded action options."
  validator: "Meta Detective"
  next: "Operator durable-knowledge gate."
  stop: "Stop and request operator clarification if mutually incompatible interpretations would materially change the record."
```

#### Micro controls and repair behavior

```okf
micro:
  candidate_record_fields:
    - "source_id, source_path, date, language, and source-status"
    - "near-source summary and distilled core"
    - "explicit claims, metaphors, rules, questions, and unresolved fragments"
    - "candidate tags and project links with confidence"
    - "candidate next actions with effort and stop condition"
    - "status: candidate, accepted, rejected, or held"
  repair_examples:
    - trigger: "Detective finds that the entry converts a distinctive insight into generic self-help language."
      owner: "Meta Ops"
      correction: "Redistill directly against the source, restore the distinctive wording or uncertainty, and revalidate."
    - trigger: "The entry is correctly summarized but placed in the wrong project."
      owner: "Knowledge Bank specialist"
      correction: "Repair placement and related links; preserve the accepted semantic body."
    - trigger: "The idea appears important but strategic value is uncertain."
      owner: "Meta Strategy"
      correction: "Propose a bounded evidence-gathering action rather than asserting a new priority."
  continuity_artifacts: [immutable-source-record, candidate-entry, placement-packet, Detective-verdict, operator-decision, accepted-state-delta, optional-action-link]
```

---

### 5.6 US-OFFER-01 — Dance and Martial Arts Fusion Offer Launch

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] Dance Fusion appears in the Master of Arts project-to-execution portfolio alongside coaching, media, workshops, and products."
    - "[V] The workflow corpus identifies demand-prioritized offer development and media-output planning as macro workflows."
    - "[V] The corpus supports one concept becoming website, content, community, video, workshop, and other output forms."
  accepted_decisions:
    - "[D] Demand is validated before full offer and asset production."
    - "[D] Website, media, and workshop outputs must share one approved audience, promise, scope, and safety posture."
  inferred_workflow_design:
    - "[I] The story uses a small evidence test and explicit proceed/pivot/stop threshold before launch production."
    - "[I] Exact audience, price, venue, and commercial terms remain operator decisions because the repository does not verify them."
  external_improvements:
    - "[E] Start with the simplest adequate workflow and expand to parallel workers only after the demand and offer hypotheses are stable."
    - "[E] Risk-rate public and action tools; require approval for spending, publication, booking, payments, or irreversible launch actions."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: L20, L29, L30, W03"
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/ProcessRanking_GPT&MasterOA.md: project matrix, demand-first, creation, risk, and verification relationships"
```

#### Macro

```okf
macro:
  story_id: "US-OFFER-01"
  project: "Dance and Martial Arts Fusion Offer Launch"
  orchestration_type: "demand-first commercial validation with controlled asset fan-out"
  operator_goal: "Validate demand for a fusion concept and produce a coherent offer with related website, media, and workshop outputs."
  starting_point: "A real Dance Fusion concept in the Master of Arts portfolio and reusable demand, workshop, media, and offer workflows; audience and commercial details are not yet treated as verified."
  active_agents:
    core: [Alfred, Meta Strategy, Meta Ops, Meta Detective]
    specialists: [Prompts and Workflows, Informatics Design]
    domain_workers: [demand-research worker, offer-copy worker, workshop-outline worker, media worker, launch-operations worker]
  final_deliverable: "A demand evidence packet, approved offer architecture, master offer brief, website copy, media assets, workshop outline, launch checklist, and post-launch learning plan."
  completion_condition: "Alex authorizes launch based on explicit demand evidence; every public artifact derives from one validated offer brief; claims, workshop scope, asset dependencies, and launch controls pass independent review."
```

#### Why this set is minimal

Strategy owns demand hypothesis, audience, positioning, and proceed/pivot/stop interpretation. Ops owns the evidence plan and later fan-out. Prompts & Workflows and Informatics Design are needed only after the offer survives the demand gate. Detective prevents cherry-picked evidence, inconsistent public claims, and unsafe workshop promises. Temporary workers produce evidence and assets; they do not control launch.

#### Meso orchestration

```okf
meso:
  - stage: "1. Commercial intent and constraints"
    owner: "Alfred"
    action: "Capture concept, operator motivation, candidate audiences, location or online mode, available time and budget, existing proof, safety boundaries, desired launch horizon, and explicit non-goals."
    handoff: "Send a locked commercial-intent packet to Meta Strategy."
    output: "Accepted launch question."
    review_or_gate: "Alex confirms the maximum validation spend and actions requiring approval."

  - stage: "2. Demand hypothesis"
    owner: "Meta Strategy"
    action: "Define candidate audience, problem, promise, differentiation, demand assumptions, evidence threshold, and proceed/pivot/stop rules."
    handoff: "Return one bounded validation thesis to Meta Ops."
    output: "Demand hypothesis and decision rule."
    review_or_gate: "Detective checks circular or unfalsifiable criteria; Alex authorizes the demand test."

  - stage: "3. Minimum evidence plan"
    owner: "Meta Ops"
    action: "Use Plan support to sequence the smallest useful interviews, outreach, landing-page or waitlist test, comparable-offer scan, and evidence capture."
    handoff: "Issue separate packets only where evidence streams are independent."
    output: "Validation plan, instruments, evidence schema, and stop conditions."
    review_or_gate: "No full website, media campaign, or workshop package is produced."

  - stage: "4. Bounded demand research"
    owner: "demand-research worker"
    action: "Collect the approved evidence without changing the audience, promise, or threshold after seeing results."
    handoff: "Return raw data, provenance, limitations, and a non-interpretive summary to Meta Ops."
    output: "Demand evidence packet."
    review_or_gate: "Personal enthusiasm is recorded separately from market evidence."

  - stage: "5. Evidence integration and validity"
    owner: "Meta Ops"
    action: "Use Sync support to calculate response counts, source coverage, threshold status, contradictions, missing evidence, and test costs."
    handoff: "Send raw evidence, deterministic report, and assumptions to Detective."
    output: "Integrated demand candidate."
    review_or_gate: "Detective checks methodology, provenance, cherry-picking, plausibility, and whether the threshold was moved."

  - stage: "6. Demand decision milestone"
    owner: "Meta Strategy"
    action: "Interpret only the Detective-passed evidence and recommend proceed, narrow, pivot, run one additional test, or stop."
    handoff: "Present options, tradeoffs, and confidence through Alfred."
    output: "Demand decision memo."
    review_or_gate: "Alex chooses; a stop or pivot closes the original launch branch without sunk-cost asset production."

  - stage: "7. Master offer architecture"
    owner: "Meta Strategy"
    action: "For an approved direction, lock audience, promise, scope, differentiation, format, exclusions, success measure, and commercial assumptions requiring later confirmation."
    handoff: "Send the operator-approved offer decision to Meta Ops."
    output: "Master offer brief."
    review_or_gate: "Detective checks claim support and hidden safety or compliance assumptions."

  - stage: "8. Controlled one-to-many fan-out"
    owner: "Meta Ops"
    action: "Open independent packets for website copy, media, pilot workshop outline, and launch operations using the same master offer brief and canonical terms."
    handoff: "Workers return assets plus claim, dependency, source, and unresolved-decision lists."
    output: "Candidate launch asset set."
    review_or_gate: "Workers cannot change audience, offer scope, price logic, or safety boundaries."

  - stage: "9. Fan-in and consistency control"
    owner: "Informatics Design specialist"
    action: "Build the cross-asset term, promise, call-to-action, date, contact, and dependency matrix; flag mismatches for Meta Ops."
    handoff: "Meta Ops integrates and sends the release candidate to Detective."
    output: "Coherent launch candidate and consistency report."
    review_or_gate: "A consistency report is evidence, not approval."

  - stage: "10. Independent public and workshop review"
    owner: "Meta Detective"
    action: "Check demand traceability, public claims, contradiction, workshop safety boundary, pricing/status uncertainty, reputation risk, scope, and completion evidence."
    handoff: "Return local defects to asset owners, repeated defects to the master-brief owner, and compliance questions to the compliance workflow."
    output: "Launch validity verdict and repair map."
    review_or_gate: "Corrected assets receive delta review; Detective does not write the copy or workshop."

  - stage: "11. Strategic launch alignment"
    owner: "Meta Strategy"
    action: "Check whether the validated package still fits the demand signal, timing, audience, leverage, capacity, and intended outcome."
    handoff: "Present launch, staged launch, hold, or narrow options through Alfred."
    output: "Launch recommendation."
    review_or_gate: "Alex approves publication, spend, venue commitments, and any payment or booking action."

  - stage: "12. Staged launch and evidence loop"
    owner: "Meta Ops"
    action: "Execute only approved release tasks, track versions and dependencies, and capture inquiries, conversions, objections, delivery feedback, costs, and incidents."
    handoff: "Detective checks evidence integrity; Strategy recommends the next commercial decision."
    output: "Launch evidence and candidate revision set."
    review_or_gate: "Session support records accepted state, not every speculative lesson."
```

#### Critical handoff

```okf
handoff:
  from: "Meta Strategy"
  to: "Meta Ops"
  objective: "Validate one explicit Dance and Martial Arts Fusion demand hypothesis before producing the offer ecosystem."
  inputs: [candidate audience, problem, promise, differentiation, evidence threshold, budget cap, approved test modes, stop rule]
  return: "Raw evidence packet, deterministic threshold report, limitations, and unresolved decisions."
  validator: "Meta Detective"
  next: "Meta Strategy proceed/pivot/stop interpretation and operator decision."
  stop: "Stop if the test changes the hypothesis after results arrive, uses unapproved spend, or cannot distinguish interest from commitment."
```

#### Micro controls and repair behavior

```okf
micro:
  demand_gate_acceptance:
    - "The audience and promise were fixed before evidence collection."
    - "The evidence threshold and maximum test budget were operator-approved."
    - "Raw responses and provenance are retained; summaries do not replace them."
    - "Contrary and null evidence is represented."
    - "The decision memo distinguishes demand evidence from strategic judgment."
  master_offer_fields:
    - "audience, problem, promise, mechanism, format, scope, exclusions, evidence, safety posture, call to action, dependencies, unresolved commercial decisions"
  repair_examples:
    - trigger: "Detective finds that weak expressions of interest were counted as purchase intent."
      owner: "demand-research worker"
      correction: "Reclassify evidence using the pre-approved schema; Meta Ops recomputes the report."
    - trigger: "Website and workshop assets promise different outcomes."
      owner: "Meta Strategy if the master promise is ambiguous; otherwise the nonconforming asset worker"
      correction: "Repair the owning layer, then update only affected assets."
    - trigger: "A workshop activity introduces physical risk absent from the offer brief."
      owner: "workshop-outline worker with qualified safety review"
      correction: "Remove, bound, or professionally review the activity before launch revalidation."
  continuity_artifacts: [commercial-intent, demand-hypothesis, raw-evidence, threshold-report, demand-decision, master-offer-brief, asset-matrix, launch-verdicts, launch-evidence]
```

---

### 5.7 US-COMP-01 — Self-Employment and Product Compliance Operations

#### Source-grounded basis

```okf
basis:
  verified_project_facts:
    - "[V] The repository records a Legal / Organizational Self-Employment Setup Board covering formalities, tax, bookkeeping, insurance, product compliance, documentation, and external actions."
    - "[V] The intended business scope may include coaching, workshops, trainings, physical products, content, and Leela-related questions."
    - "[V] The workflow explicitly requires professional-advice gates, monthly finance review, quarterly compliance review, and separation of execution checklists from legal or tax certainty."
  accepted_decisions:
    - "[D] AI has no final legal, tax, insurance, accounting, or product-compliance authority."
    - "[D] Consequential submissions, purchases, declarations, product release, and financial actions remain operator-controlled and may require professional sign-off."
  inferred_workflow_design:
    - "[I] An obligation register with authority, evidence, owner, dependency, status, and next review is the durable control artifact."
    - "[I] Work branches by obligation lane but converges before any external action."
  external_improvements:
    - "[E] Use lifecycle risk management across design, use, evaluation, and recurring review rather than a one-time checklist."
    - "[E] Keep tool approvals on and require clear consent for read and write actions; use progress, cancellation, error, and logging support for long-running external workflows."
  repository_refs:
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md: S04, L33-L36, W09"
    - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/AgnetFlows_Projects_Targets/ProcessRanking_GPT&MasterOA.md: risk, durable orchestration, and operating-cycle stacks"
```

#### Macro

```okf
macro:
  story_id: "US-COMP-01"
  project: "Self-Employment and Product Compliance Operations"
  orchestration_type: "evidence-controlled high-risk operations with external professional gates and recurring state"
  operator_goal: "Turn business, tax, bookkeeping, insurance, and product obligations into a controlled execution workflow with evidence and professional-review gates."
  starting_point: "Existing legal and organizational source guidance, a mixed business-activity scope, external authorities and deadlines, and unresolved questions whose answers may vary by jurisdiction, activity, timing, and product."
  active_agents:
    core: [Alfred, Meta Strategy, Meta Ops, Meta Detective]
    specialists: [Knowledge Bank, Informatics Design]
    domain_workers: [official-source research workers, tax adviser, legal adviser, accounting or bookkeeping professional, insurance adviser, product-compliance professional]
  final_deliverable: "A validated obligation register, sequenced operations board, authority and evidence repository, professional-review packets, submission and decision log, recurring review schedule, and current status report."
  completion_condition: "Every in-scope obligation has an accountable owner, authority source, evidence, dependency, due or review date, status, professional gate where required, and verified closure; Alex controls every consequential external action."
```

#### Why this set is minimal

Strategy is used to decide which business activities launch first and how risk affects sequencing, not to give legal advice. Ops owns the operational register and evidence flow. Knowledge Bank is necessary for source authority and document custody; Informatics Design provides a stable obligation/evidence schema. Detective independently checks authority, uncertainty, contradictions, and AI limits. External professionals remain the authoritative reviewers in their domains.

#### Meso orchestration

```okf
meso:
  - stage: "1. Business-scope intake"
    owner: "Alfred"
    action: "Capture jurisdiction, residence and operating locations, intended activities, launch order, revenue assumptions, products, venues, partners, existing registrations, software, accounts, insurance, deadlines, and open questions."
    handoff: "Send a complete intake packet to Meta Strategy and Meta Ops."
    output: "Business-scope baseline."
    review_or_gate: "Alex marks unknowns and confirms which activities are actually planned first."

  - stage: "2. Strategic activity sequencing"
    owner: "Meta Strategy"
    action: "Assess activity combinations, timing, operational load, dependencies, downside exposure, and which launch sequence minimizes avoidable complexity."
    handoff: "Present launch-scope options through Alfred."
    output: "Activity sequencing decision."
    review_or_gate: "Detective checks that no legal or tax classification is asserted as strategy; Alex selects the in-scope launch set."

  - stage: "3. Authority and obligation model"
    owner: "Meta Ops"
    action: "Create the obligation-register schema and Plan-supported lanes for setup, tax, bookkeeping, insurance, product compliance, contracts, privacy, documentation, and recurring review."
    handoff: "Assign Knowledge Bank the source-authority and evidence-custody task; assign Informatics Design the schema-normalization task."
    output: "Candidate obligation register and source map."
    review_or_gate: "Unverified guidance is never treated as authority."

  - stage: "4. Parallel official-source research"
    owner: "Meta Ops"
    action: "Open bounded read-only packets by obligation lane, each constrained to the relevant jurisdiction, activity, date, and official or professional source hierarchy."
    handoff: "Workers return requirements, authority refs, effective dates, uncertainty, evidence needed, and questions for professionals."
    output: "Lane evidence packets."
    review_or_gate: "Research workers do not make filings, provide final legal conclusions, or reuse requirements across jurisdictions without proof."

  - stage: "5. Deterministic dependency and status integration"
    owner: "Meta Ops"
    action: "Use Sync support to calculate missing evidence, blocked tasks, dependency order, deadlines, stale sources, duplicate obligations, and professional-review requirements."
    handoff: "Send the integrated register and reports to Detective."
    output: "Integrated compliance candidate."
    review_or_gate: "The deterministic report does not authorize external action."

  - stage: "6. Independent authority and risk review"
    owner: "Meta Detective"
    action: "Check source authority, jurisdiction and date fit, contradictions, completeness, uncertainty, scope, evidence, AI authority limits, and hidden product or insurance risks."
    handoff: "Return source defects to the research lane, schema defects to Informatics Design, integration defects to Meta Ops, and unresolved professional questions to the correct adviser packet."
    output: "Validity verdict and professional-gate map."
    review_or_gate: "A pass means the packet is ready for professional review or operator action, not that AI has supplied professional advice."

  - stage: "7. Professional-review packets"
    owner: "Meta Ops"
    action: "Create concise packets for tax, legal, accounting, insurance, or product-compliance professionals with business facts, exact questions, candidate interpretation, source refs, dependencies, and requested return format."
    handoff: "Send each packet only to the relevant qualified reviewer."
    output: "Professional responses, conditions, and requested changes."
    review_or_gate: "Conflicting professional advice is recorded and escalated; it is not silently reconciled by AI."

  - stage: "8. Correction and revalidation"
    owner: "Meta Ops"
    action: "Apply professional answers and operator decisions as traceable changes to the obligation register and task sequence."
    handoff: "Send changed authority, status, dependency, and evidence fields to Detective for delta review."
    output: "Revalidated operations board."
    review_or_gate: "The real owner repairs each defect: source researcher, schema specialist, professional, or Ops integrator."

  - stage: "9. Strategic alignment and execution gate"
    owner: "Meta Strategy"
    action: "Check whether the validated sequence still fits the chosen launch scope, timing, cost, business model, and risk tolerance."
    handoff: "Present proceed, reorder, defer, narrow, or stop options through Alfred."
    output: "Execution recommendation."
    review_or_gate: "Alex approves each consequential submission, purchase, policy selection, contract, declaration, or product-release action."

  - stage: "10. Human external execution"
    owner: "Alex or authorized professional"
    action: "Perform the approved filing, payment, consultation, account setup, policy purchase, contract execution, or product-control action."
    handoff: "Return receipts, confirmations, documents, conditions, dates, and unresolved issues to Meta Ops."
    output: "External evidence packet."
    review_or_gate: "AI does not impersonate Alex, sign, declare, pay, or submit without explicit authorized tooling and approval."

  - stage: "11. Evidence closure and state mutation"
    owner: "Meta Ops"
    action: "Use Session support to record the verified evidence, status delta, next review, dependent task release, and concise next-session context."
    handoff: "Use Sync support to confirm that the changed status is supported by fetched evidence."
    output: "Current compliance status and audit trail."
    review_or_gate: "Detective reviews high-risk closures and any discrepancy between claimed and retrieved state."

  - stage: "12. Recurring operations and recovery"
    owner: "Meta Ops"
    action: "Run monthly finance and bookkeeping review and quarterly compliance and source-freshness review; reopen obligations when activities, laws, products, locations, or professional advice change."
    handoff: "Escalate stale, contradictory, missed, or incident-triggered items to Detective and the appropriate professional."
    output: "Recurring review reports and repaired state."
    review_or_gate: "Alex approves consequential corrective actions; Strategy rechecks alignment when the business scope changes."
```

#### Critical handoff

```okf
handoff:
  from: "Meta Ops"
  to: "tax adviser"
  objective: "Resolve a specific tax or activity-classification uncertainty that blocks dependent setup and bookkeeping tasks."
  inputs: [verified business facts, jurisdiction, activities, timing, revenue assumptions, candidate interpretations, official source refs, exact blocked decisions]
  return: "Professional answer, conditions, missing facts, effective date, confidence or caveat, and recommended next action."
  validator: "Meta Detective checks that the response is represented accurately and that dependencies are updated consistently."
  next: "Meta Ops updates the register; Alex approves any filing or declaration."
  stop: "Hold dependent tasks if facts are incomplete, advice conflicts, or the adviser requires a different professional domain."
```

#### Micro controls and repair behavior

```okf
micro:
  obligation_record_fields:
    - "obligation_id, activity, jurisdiction, authority, authority_date, requirement, applicability status, owner"
    - "dependencies, due date, next review, evidence required, evidence location, status, confidence"
    - "professional gate, operator approval, external action record, closure proof, reopen trigger"
  status_values: [candidate, researching, needs_professional_review, operator_decision, ready_for_action, externally_in_progress, evidence_pending, verified_closed, held, reopened]
  repair_examples:
    - trigger: "Research finds contradictory guidance on activity classification."
      owner: "official-source research worker and tax adviser"
      correction: "Preserve both authorities, formulate the precise professional question, and hold dependent tasks."
    - trigger: "A task is marked complete but no retrievable receipt or confirmation exists."
      owner: "Meta Ops"
      correction: "Return status to evidence_pending; do not infer closure from memory."
    - trigger: "A new physical product changes insurance or product obligations."
      owner: "Meta Strategy for scope decision; product-compliance and insurance professionals for domain review"
      correction: "Reopen affected lanes and block release until revalidated."
  continuity_artifacts: [business-scope-baseline, activity-sequencing-decision, authority-map, obligation-register, professional-review-packets, external-evidence, approval-log, recurring-review-reports, incident-and-reopen-log]
```

## 6. Cross-Story Orchestration Coverage

### Coverage matrix

| Required behavior | SEQ | MEDIA | LEELA | WORKSHOP | IDEA | OFFER | COMP |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Macro target locked before detailed work | ✓ | ✓ | ✓ | ✓ | lightweight | ✓ | ✓ |
| Meso dependency skeleton before micro generation | ✓ | ✓ | ✓ | ✓ | not needed | ✓ | ✓ |
| Safe parallel branches | method/pilot | scripts/assets | analysis/requirements where independent | pedagogy/exercises | no default fan-out | demand streams; later assets | obligation lanes |
| Independent Meta Detective validity review | ✓ | ✓ | ✓ | ✓ | ✓ for durable entry | ✓ | ✓ |
| Meta Strategy upward alignment review | ✓ | ✓ | ✓ | ✓ | conditional | ✓ | ✓ |
| Named defect-owner repair | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Consequential operator gate | thesis/pilot/learning | bible/release | use case/implementation | pilot/safety | durable entry/project action | demand/launch | scope/external action |
| Durable multi-session state | ✓ | ✓ | ✓ | ✓ | compact state delta | ✓ | essential |
| Plan support under Meta Ops | ✓ | ✓ | ✓ | ✓ | no default | ✓ | ✓ |
| Sync deterministic support | pilot comparison | asset consistency | backlog coverage | pilot comparison | optional index update | demand/asset reports | dependencies/stale evidence |
| Session mutation support | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Specialist activation only when material | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Qualified external professional boundary | as needed | no default | as needed | safety | no | as needed | core requirement |
| Candidate-only learning | pilot lessons | release lessons | implementation lessons | pilot lessons | classifications | launch lessons | recurring risk observations |

### Portfolio reconciliation

```okf
cross_story_validation:
  materially_different_workflows:
    US_SEQ_01: "Ambiguous concept becomes method, pilot, and evidence-based offer."
    US_MEDIA_01: "Stable source becomes a parallel, reusable public asset system."
    US_LEELA_01: "Human practice becomes bounded product behavior and gated implementation."
    US_WORKSHOP_01: "Embodied pedagogy becomes facilitator-usable and safety-gated delivery."
    US_IDEA_01: "One messy source becomes candidate knowledge without automatic project creation."
    US_OFFER_01: "Commercial evidence precedes offer architecture and asset fan-out."
    US_COMP_01: "External obligations become evidence-controlled recurring operations."

  role_boundary_checks:
    Meta_Strategy_does_not_execute: true
    Meta_Ops_does_not_self_validate_important_work: true
    Meta_Detective_does_not_implement: true
    Alfred_remains_operator_interface: true
    specialists_do_not_take_over_orchestration: true
    skills_do_not_erase_accountability: true

  repair_checks:
    every_failed_review_has_named_owner: true
    corrected_work_is_revalidated: true
    generic_improve_it_step_absent: true
    passed_independent_work_is_not_regenerated_without_reason: true

  state_and_context_checks:
    durable_artifacts_replace_chat_memory: true
    handoffs_do_not_require_hidden_reasoning: true
    raw_sources_and_evidence_are_preserved: true
    just_in_time_source_loading_is_supported: true
    candidate_and_accepted_state_are_separate: true

  governance_checks:
    full_milestone_loop_is_risk_weighted: true
    operator_gates_are_consequential_not_constant: true
    public_safety_compliance_and_mutation_receive_stronger_control: true
    historical_runtime_mechanisms_are_translated_not_restored: true
```

### System-wide repair law

```okf
repair_law:
  defective_strategy_or_promise: "Return to Meta Strategy."
  defective_source_interpretation_or_artifact_content: "Return to the creating worker or specialist."
  defective_dependency_handoff_or_integration: "Return to Meta Ops."
  defective_validation_criterion_or unsupported verdict: "Escalate for independent review; Detective does not silently rewrite the work."
  defective_implementation: "Return to the implementation worker with failed tests and requirement deltas."
  unresolved_professional_domain_question: "Hold and route to the qualified human professional."
  operator_choice_required: "Stop the execution branch and present bounded options through Alfred."
```

## 7. Implications for Fable

The stories demonstrate the following concrete system capabilities. They do not prescribe Fable’s internal file layout, runtime framework, model roster, or implementation language.

1. **Operator-intent lock:** capture a concise objective, constraints, non-goals, and explicit decisions before work is decomposed.
2. **Macro–meso–micro representation:** maintain a visible macro target, meso dependency and handoff structure, and bounded micro work packets, with upward synthesis after important batches.
3. **Accountable routing:** route work to Alfred, Meta Strategy, Meta Ops, Meta Detective, a specialist lane, a temporary worker, a deterministic tool, or a qualified external professional without creating unnecessary durable agents.
4. **Artifact contracts:** issue self-contained work packets and require returns with sources, assumptions, uncertainties, changed claims, evidence, and stop conditions.
5. **Parallel-safe orchestration:** run independent branches concurrently, prevent workers from rewriting shared strategy, and fan results back into one Meta Ops integration point.
6. **Two-stage milestone review:** represent Meta Detective validity and Meta Strategy alignment as separate verdicts, both occurring after integration and before consequential continuation.
7. **Criterion-level repair routing:** attach each failed criterion to the real defect owner, reopen only affected work, and require revalidation of corrected output.
8. **Operator-gated consequence:** pause for Alex before direction changes, public release, durable knowledge promotion, implementation, spending, external submission, physical-safety exposure, or compliance action.
9. **Meta Ops support integration:** allow Plan to propose execution structure, Sync to compute deterministic read-side reports, and Session to record approved state deltas and continuation context under Meta Ops accountability.
10. **Durable continuity:** preserve targets, sources, dependencies, versions, verdicts, approvals, evidence, candidate learning, and next-session packets outside chat history.
11. **Progressive disclosure:** load compact indexes and task-specific source slices first; retrieve detailed knowledge, skills, and evidence only when the active batch needs them.
12. **Deterministic/model boundary:** use model judgment for ambiguity, synthesis, and options; use deterministic mechanisms for status, dependencies, matching, completeness, diffs, tests, and evidence retrieval.
13. **Risk-weighted control:** apply the full milestone loop only where failure would change direction, publish output, alter durable state, authorize substantial work, or create safety/compliance exposure.
14. **External-authority handoff:** hold AI work where legal, tax, accounting, insurance, product, or physical/child-safety authority belongs to a qualified person, and preserve that person’s response as evidence.
15. **Candidate-only learning:** capture lessons from pilots, releases, incidents, and corrections without allowing any creator to promote its own lesson directly into accepted agent or skill behavior.
