---
title: "User Stories — Decision and Definition Log"
purpose: >
  Lock the scope, agent model, workflow semantics, story portfolio, and output
  structure for the creation of user-stories.md.
status: "operator-validated baseline"
created: "2026-07-11"
target_artifact: "apex-meta/fable-orchestrator/user-stories.md"
---

# User Stories — Decision and Definition Log

```okf
decision_definition_log:

  mission:
    definition: >
      user-stories.md describes how Alex uses the finished Apex orchestration
      system to complete real projects.
    primary_question: >
      Given a concrete operator objective, how do the Apex agents, specialist
      agents, skills, deterministic tools, and operator gates cooperate until
      a usable real-world result exists?
    audience:
      - "Fable, while designing the final orchestration system"
      - "Future agents implementing or validating that system"
      - "The operator reviewing whether the design matches intended use"

  source_authority:

    architecture_authority:
      use_for:
        - "current Claude-native system boundaries"
        - "agent-versus-skill decisions"
        - "final orchestration design"
      primary:
        - "apex-meta/fable-orchestrator/"
        - "apex-meta/kb/operator-research-orchestration-20260711/"
        - "apex-meta/kb/claude-code-orchestration-design/"
        - "apex-meta/kb/apex-plan-sync-session-workflow-v2/"

    agent_and_handoff_evidence:
      use_for:
        - "agent responsibilities"
        - "specialist lanes"
        - "handoff patterns"
        - "validation loops"
        - "failure lessons"
      primary:
        - "apex-meta/kb/old-apex-full-orchestration-agent-kb/"
        - "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/"
      rule: >
        Translate useful role and workflow patterns into the final Claude-native
        system. Do not automatically revive every historical runtime mechanism.

    user_story_content_authority:
      use_for:
        - "real projects"
        - "real goals"
        - "real tasks"
        - "real constraints"
        - "real intended outputs"
      primary:
        - "the Master of Arts project and workflow records"
        - "OperatorResearch/AgnetFlows_Projects_Targets or spelling variants"
        - "Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md"
        - "ProcessRanking_GPT&MasterOA.md"
        - "underlying project files referenced by those records"
      rule: >
        A story must be grounded in a concrete project record. Architecture logs
        alone cannot supply a user-story scenario.

    navigation_only:
      examples:
        - "indexes"
        - "process rankings"
        - "source maps"
      rule: >
        Use these to locate evidence. Do not treat them as sufficient evidence
        when the underlying project or workflow record is available.

  locked_decisions:

    D01_story_purpose:
      decision: >
        The stories demonstrate real operator use of the finished orchestration
        system.
      excluded_interpretation: >
        They are not primarily stories about Fable designing, researching, or
        rebuilding the orchestration system itself.

    D02_no_self_referential_core_stories:
      decision: >
        Architecture reconciliation, design-lock resolution, Fable build logs,
        and generic worker-routing tests are excluded from the core portfolio.
      allowed_use: >
        They may later become implementation tests, simulations, or internal
        process examples.

    D03_concrete_project_anchor:
      decision: >
        Every core story names one concrete project, its actual starting
        material, and an observable final result.
      invalid_example: "Create a workshop."
      valid_example: >
        Turn the existing Peaceful Warrior / Superhero Training material into
        a pilot-ready 90-minute workshop package.

    D04_portfolio_size:
      decision: >
        Create approximately seven core user stories.
      reason: >
        Seven allows broad coverage without repeating the same orchestration
        pattern under different project names.
      constraint: >
        Each story must expose a materially different project shape,
        specialist configuration, risk profile, or execution pattern.

    D05_agents_must_be_visible:
      decision: >
        Stories explicitly name the responsible Apex agents and specialist
        agents.
      rule: >
        Do not replace Meta Strategy, Meta Ops, Meta Detective, Alfred, and
        specialist lanes with generic terms such as worker, system, or AI when
        responsibility matters.

    D06_not_every_agent_in_every_story:
      decision: >
        Activate only the smallest useful agent set.
      rule: >
        A story must not force all agents into every workflow merely to display
        the architecture.
      requirement: >
        Every activation must correspond to a real responsibility in that
        project.

    D07_agent_and_skill_harmonization:
      decision: >
        Multi-agent orchestration and Apex skill orchestration appear together
        where the project requires both.
      rule: >
        Agents own judgment, accountability, routing, integration, and
        validation. Skills perform reusable bounded capabilities.
      implication: >
        A skill invocation does not erase the responsible agent.

    D08_apex_plan_sync_session:
      decision: >
        apex-plan, apex-sync, and apex-session may appear inside stories when
        their boundaries clarify the workflow.
      not_required: >
        They do not need to be named in every story.
      prohibited: >
        They must not become standalone story subjects unless the real project
        outcome itself depends on explaining that boundary.

    D09_macro_meso_micro:
      decision: >
        Every story uses macro, meso, and micro layers in token-efficient OKF.
      purpose:
        macro: "Understand the whole project and agent configuration quickly."
        meso: "Understand stages, handoffs, review gates, and execution flow."
        micro: "Inspect exact task mechanics only when needed."

    D10_concise_representation:
      decision: >
        Use short declarative sentences and a small stable field set.
      avoid:
        - "large generic input schemas"
        - "duplicated explanations"
        - "long prose hidden inside fields"
        - "variables that do not change agent behavior"
        - "repeating every global rule inside every story"

    D11_review_loop:
      decision: >
        Important work passes through both adversarial validation and strategic
        alignment before execution continues.
      distinction:
        meta_detective: >
          Issues the independent validity verdict. Checks evidence,
          contradictions, plausibility, drift, safety, and boundary compliance.
        meta_strategy: >
          Confirms that a valid output still serves the intended goal,
          leverage, timing, and strategic direction.
      rule: >
        Strategic alignment is not a substitute for independent validation.

    D12_revision_loop:
      decision: >
        A failed review returns to the agent that owns the defect.
      routing:
        strategy_problem: "Return to Meta Strategy."
        execution_path_problem: "Return to Meta Ops."
        workflow_shape_problem: "Return to Prompts/Workflows."
        structure_problem: "Return to Informatics Design."
        evidence_or_drift_problem: "Return through Meta Ops with the Detective verdict."
        hygiene_problem: "Route to Hygiene Clean."
        knowledge_placement_problem: "Route to Knowledge Bank."
      stop_rule: >
        No story may hide the revision loop behind a generic statement such as
        improve the result.

    D13_milestone_review:
      decision: >
        Meta Detective and Meta Strategy review every important milestone.
      important_milestone_definition: >
        An output is important when it changes project direction, commits
        substantial work, creates a public or customer-facing artifact, affects
        safety or compliance, changes durable knowledge, or enables the next
        major execution phase.
      low_impact_rule: >
        Minor mechanical steps do not require a ceremonial dual review.

    D14_operator_position:
      decision: >
        The operator receives decision-ready outputs and retains approval over
        consequential choices.
      operator_gates_include:
        - "selecting a strategic direction"
        - "approving a public, commercial, or safety-sensitive artifact"
        - "accepting durable project or knowledge changes"
        - "authorizing consequential repository execution"
        - "resolving value tradeoffs that agents cannot decide"

    D15_final_presentation:
      decision: >
        Meta Ops integrates the completed work. Alfred presents the concise
        result, decisions, unresolved issues, and next action to the operator.
      rule: >
        Alfred is the operator interface, not the execution controller or final
        validator.

  definitions:

    user_story:
      definition: >
        A source-grounded record of how Alex and the finished orchestration
        system move one concrete project from trigger to completed outcome.

    orchestration_story:
      definition: >
        A user story that shows responsibility transfer across agents, skills,
        tools, review gates, and the operator.

    concrete_project:
      definition: >
        A named body of work with existing source material and a real
        deliverable. It is not a generic capability category.

    agent:
      definition: >
        A durable responsibility and accountability lane.
      warning: >
        An agent name does not grant unlimited permission or make that agent
        responsible for every task in its domain.

    specialist_sub_agent:
      definition: >
        A bounded specialist lane activated by Meta Ops for a specific part of
        a project.
      rule: >
        It returns a defined artifact and does not take over orchestration.

    domain_worker:
      definition: >
        A temporary project-specific expert for coaching, workshop design,
        media, Leela, content, business, legal research, or another bounded
        domain.
      rule: >
        Domain workers are not automatically permanent Apex agents.

    skill:
      definition: >
        A reusable capability invoked by an accountable agent.
      examples:
        - "planning"
        - "deterministic state analysis"
        - "session handoff"
        - "research"
        - "prompt or workflow creation"
        - "knowledge-base management"

    handoff:
      definition: >
        A bounded transfer that tells the receiving agent what to do, what
        evidence to use, what to return, and when to stop.

    validation:
      definition: >
        Independent checking of evidence, consistency, safety, authority,
        completeness, and drift.

    strategic_alignment:
      definition: >
        Confirmation that a valid artifact still supports the project's goal,
        leverage, timing, audience, and intended result.

    operator_gate:
      definition: >
        A point where the system presents a bounded decision and waits for Alex
        before consequential execution or durable acceptance.

    completion:
      definition: >
        Observable evidence that the real project deliverable exists, passed
        its required reviews, and has a clear next state.

  agent_model:

    core_heads:

      alfred:
        canonical_id: "alfred"
        purpose: "Operator intake, constraint capture, clarification, and presentation."
        receives:
          - "operator request"
          - "changed priorities"
          - "operator feedback"
        returns:
          - "bounded route brief"
          - "decision-ready final presentation"
        must_not:
          - "control execution"
          - "replace Meta Strategy"
          - "replace Meta Ops"
          - "perform adversarial validation"

      meta_strategy:
        canonical_id: "meta_strategy"
        purpose: "Vision, options, leverage, timing, and strategic recommendation."
        typical_steps:
          - "frame the desired transformation"
          - "compare viable paths"
          - "choose or recommend strategic direction"
          - "confirm alignment after validation"
        returns:
          - "strategy packet"
          - "option comparison"
          - "strategic-alignment verdict"
        must_not:
          - "execute its own recommendation"
          - "replace Meta Detective"
          - "override operator constraints"

      meta_ops:
        canonical_id: "meta_ops"
        purpose: "Orchestration, decomposition, activation, sequencing, and integration."
        typical_steps:
          - "translate strategy into an execution path"
          - "select the smallest specialist set"
          - "create bounded handoffs"
          - "sequence dependencies"
          - "integrate returned artifacts"
          - "route review and revisions"
        returns:
          - "execution path"
          - "specialist activation plan"
          - "integrated milestone artifact"
          - "final result packet"
        must_not:
          - "own final strategy"
          - "self-validate high-impact work"
          - "silently approve durable truth"

      meta_detective:
        canonical_id: "meta_detective"
        purpose: "Independent adversarial validation."
        typical_steps:
          - "check evidence"
          - "surface contradictions"
          - "test plausibility"
          - "detect drift"
          - "issue pass, revise, hold, or escalate verdict"
        returns:
          - "validation verdict"
          - "defect list"
          - "correction route"
          - "stop or escalation condition"
        must_not:
          - "implement its own findings"
          - "silently rewrite the artifact"
          - "become the orchestrator"

    specialist_sub_agents:

      knowledge_bank:
        canonical_id: "special_ops__knowledge_bank"
        use_when:
          - "new knowledge needs durable placement"
          - "source and candidate material must remain separate"
          - "project learning may become reusable knowledge"
        returns:
          - "placement recommendation"
          - "source map"
          - "candidate/canon boundary note"

      informatics_design:
        canonical_id: "special_ops__informatics_design"
        use_when:
          - "taxonomy or terminology matters"
          - "large content needs retrieval-efficient structure"
          - "information must be decomposed or indexed"
        returns:
          - "information architecture"
          - "taxonomy"
          - "naming and decomposition recommendation"

      prompts_workflows:
        canonical_id: "special_ops__prompts_workflows"
        use_when:
          - "a repeated process needs a reusable shape"
          - "a prompt or handoff sequence must be designed"
          - "execution risks process drift"
        returns:
          - "workflow pattern"
          - "prompt pattern"
          - "bounded sequence"
          - "acceptance checklist"

      ai_handling_routing:
        canonical_id: "special_ops__ai_handling_routing"
        use_when:
          - "model or tool choice materially affects quality"
          - "external research or execution capability is required"
          - "cost, context, or fallback posture matters"
        returns:
          - "advisory model or tool recommendation"
          - "capability-fit rationale"
          - "fallback path"
        must_not:
          - "control orchestration"
          - "change runtime configuration"

      hygiene_clean:
        canonical_id: "special_ops__hygiene_clean"
        use_when:
          - "pointer integrity or stale state matters"
          - "structural correctness is uncertain"
          - "cleanup may accidentally alter accepted meaning"
        returns:
          - "structural QA finding"
          - "pointer check"
          - "stale-state warning"
          - "closure or escalation recommendation"

  canonical_project_flow:

    macro:
      sequence:
        - "Alex states a real project objective."
        - "Alfred captures intent and constraints."
        - "Meta Strategy defines the vision or compares paths."
        - "Meta Ops translates the selected direction into an execution path."
        - "Meta Ops activates only the specialists needed."
        - "Specialists complete bounded steps and return artifacts."
        - "Meta Detective validates the milestone."
        - "Meta Strategy confirms strategic alignment."
        - "Failed review returns to the responsible owner."
        - "Passed work proceeds to execution or the next milestone."
        - "Meta Ops integrates the final product."
        - "Alfred presents it to Alex."
        - "Alex accepts, revises, or authorizes the next phase."

    meso:
      default_stages:

        - stage: "intake"
          owner: "alfred"
          output: "route brief"

        - stage: "strategy"
          owner: "meta_strategy"
          output: "strategy or option packet"

        - stage: "execution_design"
          owner: "meta_ops"
          output: "sequenced execution path"

        - stage: "specialist_work"
          owner: "activated specialist agents"
          output: "bounded specialist artifacts"

        - stage: "integration"
          owner: "meta_ops"
          output: "integrated milestone candidate"

        - stage: "adversarial_review"
          owner: "meta_detective"
          output: "pass, revise, hold, or escalate verdict"

        - stage: "strategic_alignment"
          owner: "meta_strategy"
          output: "aligned or redirect verdict"

        - stage: "operator_gate"
          owner: "operator"
          output: "approved direction or requested revision"

        - stage: "execution_or_delivery"
          owner: "meta_ops and selected execution capability"
          output: "real project deliverable"

        - stage: "closure_and_continuity"
          owner: "meta_ops with relevant Apex skills"
          output: "confirmed progress and next-session state"

    review_loop:
      detective_fail:
        action: "Return the finding to Meta Ops."
        routing: "Meta Ops sends the defect to its actual owner."
        resume_when: "The corrected artifact receives a new Detective verdict."

      strategy_misalignment:
        action: "Return to Meta Strategy."
        routing: "Meta Strategy revises direction; Meta Ops revises execution."
        resume_when: "The revised path passes Detective and Strategy review."

      operator_revision:
        action: "Alfred captures the changed constraint or preference."
        routing: "Meta Ops reopens only the affected stages."
        resume_when: "A revised decision-ready artifact is presented."

  apex_skill_integration:

    apex_plan:
      use_when:
        - "the project needs a formal task or dependency proposal"
        - "multiple workstreams require operator review"
      accountable_agent: "meta_ops"
      strategic_input: "meta_strategy"
      rule: "Planning output remains a proposal until accepted."

    apex_sync:
      use_when:
        - "dependencies, blockers, stale work, or exact state require computation"
        - "the project needs deterministic read-side verification"
      accountable_agent: "meta_ops"
      rule: "Computed results inform decisions; they do not make strategic choices."

    apex_session:
      use_when:
        - "work spans sessions"
        - "progress, findings, evidence, or next actions must persist"
        - "an operator-confirmed state change must be recorded"
      accountable_agent: "meta_ops"
      rule: "Session continuity is embedded in long-running stories, not a separate generic story."

  story_representation:

    format: "OKF"
    design_goal: "Fast macro comprehension with optional meso and micro retrieval."

    macro_fields:
      - "story_id"
      - "project"
      - "operator_goal"
      - "starting_point"
      - "core_agent_set"
      - "final_deliverable"
      - "completion_condition"

    meso_fields:
      - "stage"
      - "owner"
      - "action"
      - "handoff"
      - "output"
      - "review_or_gate"

    micro_fields:
      include_only_when_needed:
        - "source paths"
        - "acceptance checks"
        - "specialist instructions"
        - "failure and correction details"
        - "Apex skill or deterministic tool use"
        - "operator decision wording"

    compact_handoff:
      required:
        from: "responsible agent"
        to: "receiving agent"
        objective: "one bounded objective"
        inputs: "only authoritative inputs needed"
        output: "one explicit return artifact"
        validator: "named when review is required"
        next: "next action after return"
        stop: "condition that blocks continuation"
      optional:
        evidence_impact_risk: >
          Use low, material, or high bands only when they affect routing or
          validation. Do not add fine-grained scores to every story step.

  core_story_portfolio:

    selection_rule: >
      Each story must differ in project type, specialist pattern, review need,
      or final-output class.

    stories:

      - story_id: "US-SEQ-01"
        project: "Sequencing Coaching Format"
        orchestration_type: "Service and method design"
        target: >
          Turn the existing Sequencing concept into a defined, pilot-ready
          coaching method and offer.
        distinctive_features:
          - "high strategic ambiguity"
          - "coaching-method architecture"
          - "pilot and learning loop"
          - "possible Leela implications"
        likely_agents:
          core:
            - "alfred"
            - "meta_strategy"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__prompts_workflows"
            - "special_ops__informatics_design"
            - "special_ops__knowledge_bank"
        status: "mandatory benchmark story"

      - story_id: "US-MEDIA-01"
        project: "Morning Routine Media Series"
        orchestration_type: "Creative media production"
        target: >
          Turn the mature Morning Routine practice into a coherent video or
          media series with scripts, production sequence, and release assets.
        distinctive_features:
          - "content architecture"
          - "parallel production steps"
          - "public-facing quality gate"
          - "asset consistency"
        likely_agents:
          core:
            - "alfred"
            - "meta_strategy"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__prompts_workflows"
            - "special_ops__informatics_design"
            - "special_ops__ai_handling_routing"

      - story_id: "US-LEELA-01"
        project: "Master of Arts to Leela Use-Case Translation"
        orchestration_type: "Human-practice to software-product translation"
        target: >
          Convert a mature Master of Arts practice into a bounded Leela use
          case, product requirements, and implementation-ready backlog.
        distinctive_features:
          - "human-versus-software capability separation"
          - "product definition"
          - "requirements and backlog"
          - "possible Codex execution after approval"
        likely_agents:
          core:
            - "meta_strategy"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__informatics_design"
            - "special_ops__prompts_workflows"
            - "special_ops__ai_handling_routing"

      - story_id: "US-WORKSHOP-01"
        project: "Peaceful Warrior / Superhero Training"
        orchestration_type: "Embodied workshop creation"
        target: >
          Produce a pilot-ready workshop with transformation arc, exercises,
          facilitation, materials, and safety controls.
        distinctive_features:
          - "creative and pedagogical design"
          - "physical and child-safety concerns"
          - "multiple milestone reviews"
          - "pilot feedback loop"
        likely_agents:
          core:
            - "alfred"
            - "meta_strategy"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__prompts_workflows"
            - "special_ops__informatics_design"
            - "special_ops__knowledge_bank"

      - story_id: "US-IDEA-01"
        project: "Raw Voice Idea to Knowledge and Project Action"
        orchestration_type: "Knowledge ingestion and routing"
        target: >
          Preserve a rough voice idea, classify it, connect it to relevant
          projects, and propose bounded next actions without semantic drift.
        distinctive_features:
          - "messy input"
          - "semantic preservation"
          - "knowledge placement"
          - "candidate-versus-accepted separation"
        likely_agents:
          core:
            - "alfred"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__knowledge_bank"
            - "special_ops__informatics_design"

      - story_id: "US-OFFER-01"
        project: "Dance and Martial Arts Fusion Offer Launch"
        orchestration_type: "Demand-tested commercial offer and asset fan-out"
        target: >
          Validate demand with a small offer, then produce congruent website,
          social, and workshop assets from one approved core proposition.
        distinctive_features:
          - "demand-prioritized launch gate"
          - "commercial strategy"
          - "one-to-many content fan-out"
          - "cross-output consistency"
        likely_agents:
          core:
            - "alfred"
            - "meta_strategy"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__prompts_workflows"
            - "special_ops__informatics_design"
            - "special_ops__ai_handling_routing"

      - story_id: "US-COMP-01"
        project: "Self-Employment and Product Compliance Operations"
        orchestration_type: "External dependency and compliance workflow"
        target: >
          Turn the business, tax, bookkeeping, insurance, and product
          obligations into a controlled execution plan with professional-advice
          gates and durable evidence.
        distinctive_features:
          - "high-risk external dependencies"
          - "legal and tax uncertainty"
          - "recurring administration"
          - "strong operator and professional gates"
        likely_agents:
          core:
            - "alfred"
            - "meta_strategy"
            - "meta_ops"
            - "meta_detective"
          specialists:
            - "special_ops__knowledge_bank"
            - "special_ops__hygiene_clean"
            - "special_ops__informatics_design"

    reserve_stories:

      - project: "Neijia Theory to Short Video or Training Asset"
        use_if: >
          The media story lacks a clear theory-to-practical-output conversion
          pattern.

      - project: "Master of Arts Portfolio Prioritization"
        use_if: >
          Fable needs a dedicated cross-project selection and resource-allocation
          story.

      - project: "Cocoa Product Launch Compliance"
        use_if: >
          A concrete product-import example is better evidenced than the broader
          self-employment operations story.

  explicit_exclusions:

    not_core_user_stories:
      - "Reconcile the final Apex orchestration architecture."
      - "Resolve design-lock questions."
      - "Decide how Fable should delegate research."
      - "Test generic worker fan-out."
      - "Build the orchestration system itself."
      - "Explain apex-plan, apex-sync, and apex-session in isolation."
      - "Create a handoff merely to demonstrate handoffs."
      - "Resume a session merely to demonstrate session persistence."

    embedding_rule: >
      Delegation, planning, synchronization, validation, handoff, and session
      continuity must appear inside real project stories where they naturally
      matter.

  unresolved_implementation_boundaries:

    U01_runtime_mapping:
      unresolved: >
        The user stories define responsibilities and interactions. They do not
        pre-decide which responsibility becomes a persistent Claude agent,
        ephemeral subagent, skill step, external model call, or inline Fable
        action.
      required_future_decision: >
        Fable resolves this from the final architecture evidence.

    U02_state_machine:
      unresolved: >
        The stories preserve candidate, review, approval, and execution
        separation without requiring the historical BUILD/VERIFY/LOCK model to
        be implemented literally.
      required_future_decision: >
        Fable determines whether the final package boundaries already provide
        sufficient permission control.

    U03_exact_skill_activation:
      unresolved: >
        The exact use of apex-plan, apex-sync, apex-session, and other skills
        differs by story.
      required_future_decision: >
        Use the real current skill contracts when writing each detailed record.

    U04_domain_specialists:
      unresolved: >
        Coaching, media, workshop, Leela, content, and compliance expertise may
        be temporary domain workers rather than permanent named agents.
      required_future_decision: >
        Do not create permanent domain agents without repeated bounded need and
        supporting architecture evidence.

  acceptance_criteria_for_user_stories_md:

    required:
      - "Approximately seven materially different concrete project stories."
      - "Sequencing Coaching Format is the first benchmark story."
      - "Every story names its active core agents and specialist agents."
      - "Every story uses macro, meso, and optional micro layers."
      - "Every story contains explicit handoffs between responsible agents."
      - "Meta Detective performs independent validation."
      - "Meta Strategy performs strategic alignment confirmation."
      - "Meta Ops owns sequencing, activation, integration, and revision routing."
      - "Alfred owns operator intake and final presentation."
      - "Important milestones contain the dual Detective and Strategy review."
      - "Failed reviews create a visible correction loop."
      - "Consequential decisions return to the operator."
      - "Apex skills appear only where they support the real project flow."
      - "Every story ends in a real deliverable and an observable completion condition."
      - "Project claims and inputs point to real source files."
      - "No architecture-build or self-referential story enters the core portfolio."

    failure_conditions:
      - "Stories are generic capability descriptions."
      - "Agents are replaced by unnamed workers."
      - "All agents are activated in every story without reason."
      - "Meta Strategy becomes executor."
      - "Meta Detective implements its own findings."
      - "Meta Ops self-validates important work."
      - "Alfred becomes the entire system."
      - "Specialist agents take over orchestration."
      - "The same workflow is repeated under different project names."
      - "The story explains system construction instead of operator use."
      - "The output invents project facts not present in sources."
```