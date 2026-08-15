# Deep Research Brief: Subscription-AI Planning to OpenClaw Execution and Feedback

## Instructions to the independent researcher

Research the problem in this document from first principles and against current evidence. Do not assume that a new custom architecture is necessary. Search for native capabilities, existing skills, plugins, hooks, workflows, and maintained open-source projects before proposing new implementation work. Verify all material claims against primary documentation, the current repository, or a reproducible test. Clearly distinguish verified facts, reasonable inferences, unresolved questions, and rejected assumptions.

The required output is a decision-ready narrative report. It must explain what already exists, what can be downloaded or configured, what would have to be built, how each option would operate, which dependencies it introduces, which failures are likely, and which option should be tested first. Cite exact repository paths and public sources close to every supported claim.

## The problem

The Apex Orchestration Reliability Pilot needs a dependable handoff between a subscription AI that creates an orchestration plan and OpenClaw, which executes that already-designed plan. The operator always initiates and uses the subscription AI for planning. The planning AI is responsible for creating the analysis sequence, dependencies, prompts, provider assignments, output contracts, validation criteria, retry rules, and stopping conditions.

OpenClaw is not the planner. It should receive a frozen orchestration flow containing the already-designed prompts, execute those prompts through the assigned subscription AI services, monitor whether each turn actually completes, preserve results and evidence, and return the results to the planning AI. The planning AI must then be able to inspect the returned evidence and decide whether the flow should continue, correct a failed step, issue another execution batch, or finish.

The missing connection is the deterministic trigger and feedback mechanism between these two roles. One hypothesis is that the planning AI writes a flow file into a repository folder dedicated to the OpenClaw harness. A trigger notices the file, validates and claims it, runs the flow, and writes results back where the planning AI can access them. This is only a hypothesis. The research must determine whether OpenClaw, the subscription platforms, an existing downloadable skill, or another established tool already provides a better mechanism.

## Why independent research is required

The broader Apex KB effort has been redesigned approximately twelve times without producing a useful, trustworthy working result. A recurring failure has been AI-generated confidence about capabilities and processes that were never verified. The resulting systems accumulated elaborate calculations, lifecycle machinery, and documentation without delivering proportional user value.

This research must therefore avoid another speculative redesign. It must first discover existing solutions and test their real capabilities. A plausible architecture diagram, a zero-exit command, generated files, or an AI-authored success statement is not proof that a workflow works.

## Correct operating assumptions

The operator initiates the planning conversation and uses a subscription AI to create the plan. The planning AI must not be replaced by OpenClaw or by a deterministic scheduler.

ChatGPT, Gemini, and Perplexity have repository access through the operator's existing accounts. The intended workflow is repository-native: subscription AIs should inspect repository material through their existing repository connections instead of requiring the operator to copy and paste large inputs and outputs. The research must verify the exact current read, write, branch, commit, issue, pull-request, and tool-invocation capabilities of each connection rather than assuming that "repository access" implies every one of those operations.

OpenClaw receives and executes a prepared flow. It may perform bounded operational recovery that is explicitly authorized by the flow, but it must not invent missing analysis steps, redesign prompts, change providers, relax acceptance criteria, or select the final solution.

The repository is the durable source of truth for flow definitions, execution requests, results, receipts, and evidence. Chat history alone is not a sufficient handoff or completion record.

Routine operation should not require the operator. The operator should be involved when initiating planning, correcting the intended process, choosing among consequential alternatives, or authorizing an action that is genuinely outside the prepared flow. A trigger that merely wakes a deterministic controller must not become the orchestration authority.

## Current repository context to inspect

Begin with the current repository rather than relying on this summary. At minimum, inspect the following live paths and determine what they already solve:

- `FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md`
- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `apex-meta/openclaw/openclaw.json`
- `apex-meta/openclaw/skills/subscription-ai-browser/SKILL.md`
- `apex-meta/openclaw/skills/subscription-ai-browser/references/chatgpt.md`
- `apex-meta/openclaw/skills/apex-flow-executor/SKILL.md`
- `scripts/openclaw/validate-execution-request.py`
- `scripts/openclaw/dispatch-execution-request.ps1`
- `scripts/openclaw/verify-execution-evidence.py`
- `scripts/openclaw/tests/`

The repository reportedly already has a versioned `apex.execution-request/v2` envelope, request validation, bounded OpenClaw dispatch, and independent evidence verification. Verify those facts and contracts. Identify the exact missing seams instead of rebuilding capabilities that already exist.

Also search the repository for older orchestration designs, OpenClaw handovers, trigger mechanisms, queue or inbox conventions, scheduler experiments, hooks, browser-session recovery, and subscription-AI integration research. Historical files are evidence and may reveal prior failed approaches, but they must not override current implementation and measured behavior.

## Central research question

What is the simplest currently available, evidence-backed mechanism through which an operator-initiated subscription planning AI can publish a frozen orchestration flow, automatically trigger OpenClaw to execute it exactly once, receive durable execution results and evidence, and continue the planning conversation without routine operator intervention?

The answer must account for both directions of the loop:

1. planning AI to OpenClaw: publish, detect, validate, claim, and execute a frozen flow;
2. OpenClaw to planning AI: persist results, notify or re-enter the correct planning context, provide evidence references, and receive the next frozen batch or a terminal decision.

## Required research streams

### Repository capability audit

Map the current end-to-end path from weekly planning artifacts to OpenClaw execution requests and back to planning evidence. Identify which components are implemented, tested, unproven, contradictory, or missing. Search for existing inboxes, outboxes, state machines, trigger scripts, schedulers, hooks, skills, plugins, or task runners before declaring a gap.

For every claimed existing capability, provide the authoritative path, callable entry point, input contract, output contract, and test evidence. Explain whether it is current production-path code, a fixture, a historical design, or an unimplemented proposal.

### Native OpenClaw capability research

Research the installed OpenClaw version and current official OpenClaw documentation. Determine whether OpenClaw already offers suitable cron jobs, event hooks, webhooks, file triggers, filesystem watchers, gateway APIs, RPC methods, agent-to-agent handoffs, session continuation, skills, plugins, queues, or external automation integrations.

For each relevant native capability, verify how it is configured, how it is invoked, whether it runs on Windows, how it survives restarts, how it prevents duplicate execution, how it reports failure, and whether it can return to an existing subscription-AI planning conversation. Do not infer support from similarly named features.

### Existing skills, plugins, and reusable workflows

Search current official marketplaces, skill registries, plugin catalogs, GitHub repositories, community workflows, and automation tools for an existing solution that can be installed or adapted. Search broadly enough to include OpenClaw-specific skills as well as established deterministic automation systems that could bridge a repository event to a local OpenClaw command.

Candidates may include repository inbox processors, Git-triggered automation, task runners, durable workflow engines, filesystem event tools, GitHub Actions with a self-hosted runner, local schedulers, webhooks, MCP-based dispatch, or provider-native automation. This list is not exhaustive and must not bias the search toward building a new queue.

For every serious candidate, report its current maintenance status, license, supported platforms, installation method, required services, authentication model, repository access requirements, security boundary, operational complexity, and evidence that it can perform the required trigger and feedback loop.

### Subscription-provider capability research

Determine how ChatGPT, Gemini, and Perplexity currently interact with connected repositories. Verify whether each platform can read a named repository revision, write a file, create a commit or branch, open an issue or pull request, invoke a webhook or tool, maintain a planning conversation across external execution, and discover newly written result artifacts.

Where capabilities differ, explain whether one provider should be the planning authority while others execute research prompts. Identify any feature that exists only in a particular product mode, plan, connector, coding agent, browser interface, or API. Do not treat API capabilities as subscription-browser capabilities unless the proposed flow can actually use them.

### Trigger and feedback alternatives

At minimum, investigate native OpenClaw triggers, a repository inbox with scheduled polling, a persistent filesystem watcher, Git push events, GitHub Actions with a self-hosted runner, direct API or webhook invocation, MCP or tool invocation, browser-session monitoring, and any stronger existing solution found during research.

For each alternative, describe the complete process rather than only the wake-up event. Show how a request is uniquely identified, validated, claimed exactly once, executed, retried, timed out, cancelled, and completed. Show how results are bound to the originating request and returned to the correct planning conversation. Explain behavior after process crashes, network failure, duplicate events, partial writes, repository conflicts, provider logout, browser UI changes, or an invalid planning-AI output.

### Empirical test design

Design the smallest test that can disprove each shortlisted option quickly. The test must use a harmless frozen flow with at least two dependent prompts so that it demonstrates sequencing and feedback rather than only process launch.

The test must prove that the planning output reaches the trigger, the request is claimed once, OpenClaw performs the intended provider interactions, results are persisted, the planning AI receives or can retrieve those results, and the second dependent step uses the first result correctly. A negative or malformed request test and a crash/restart or duplicate-event test are also required.

## User stories that the solution must satisfy

As the operator, I initiate a planning session and define the objective once. After the planning AI publishes an approved flow, I do not manually move prompts, copy outputs, watch browser tabs, or restart routine steps.

As the subscription planning AI, I can inspect the repository, design the complete execution flow, publish a machine-valid handoff, receive durable result references, and decide the next batch without depending on undocumented chat context.

As OpenClaw, I receive a frozen flow with explicit prompts and dependencies. I execute it faithfully, monitor real completion, handle only declared operational retries, and return evidence. I do not become the planner.

As the orchestration controller, I can determine the exact state of every request after a crash or restart, and I cannot execute the same external submission twice because two wake-up events arrived.

As the reviewer, I can trace every conclusion to the repository revision, prompt, provider turn, captured result, and verification evidence that produced it.

As the maintainer, I prefer an existing supported skill, plugin, or workflow over another custom subsystem when it meets the same contract with lower operational burden.

## Dependency and failure analysis required for every option

For each candidate, provide a process table containing the step, responsible actor, required inputs, upstream dependencies, produced artifact, downstream consumer, retry behavior, terminal failure, and recovery path.

Explicitly analyze these dependency classes:

- planning-session identity and continuation;
- provider repository access and its actual permissions;
- repository revision, branch, and synchronization behavior;
- request schema and prompt immutability;
- event delivery and duplicate-event handling;
- atomic claim and idempotency;
- local OpenClaw gateway, browser, authentication, and provider sessions;
- evidence capture and independent verification;
- feedback delivery to the correct planning context;
- bounded retries, cancellation, timeout, and terminal markers;
- Windows startup, restart, and unattended execution;
- credentials, tokens, and least-privilege boundaries;
- upgrade compatibility and maintenance ownership.

Do not hide failure modes behind a generic "error handling" row. State what can fail, how the system detects it, whether it retries, and what durable state remains afterward.

## Comparison criteria

Compare options on concrete, separately reported criteria rather than an opaque composite score:

- evidence that the required capability currently exists;
- compatibility with the installed OpenClaw version;
- compatibility with ChatGPT, Gemini, and Perplexity subscription workflows;
- ability to preserve the planning-AI/OpenClaw responsibility boundary;
- unattended operation after the operator initiates planning;
- deterministic validation and exactly-once claim behavior;
- crash recovery and resumability;
- correct feedback to the originating planning session;
- Windows compatibility;
- installation effort and time to first test;
- number of new services and credentials;
- security and repository-write scope;
- observability and audit evidence;
- resistance to browser and provider UI drift;
- ongoing maintenance burden;
- latency and resource usage;
- availability as an existing maintained skill, plugin, or workflow;
- reversibility if the experiment fails.

Use qualitative ratings with cited evidence and a short explanation. Do not manufacture precise numerical scores when no measured data supports them.

## Required deliverables

The research report must include:

1. a concise statement of the verified current architecture and the exact missing seams;
2. an inventory of relevant repository components that already exist;
3. an inventory of native OpenClaw and subscription-provider capabilities;
4. a longlist of existing downloadable skills, plugins, projects, and deterministic workflow options;
5. a shortlist of two or three options that genuinely satisfy the operating model;
6. a dependency and failure-mode map for each shortlisted option;
7. a criterion-by-criterion comparison with evidence and no opaque scoring formula;
8. a recommended first option and a justified fallback;
9. a minimal empirical test plan for the recommendation and fallback;
10. explicit disconfirming evidence and reasons for rejecting attractive but unsuitable options;
11. unresolved questions that require hands-on testing rather than further speculation;
12. direct links to current primary sources and exact repository paths.

The report must say "no verified solution found" if the evidence does not support a candidate. It must not recommend building a new framework merely to ensure that the report ends with a recommendation.

## Definition of done

The research is complete when the operator can decide which trigger-and-feedback option to test without trusting unsupported AI reasoning. At least one recommended option must have a reproducible, bounded proof-of-concept procedure that exercises both directions of the loop. Every material capability claim must be traceable to current documentation, live repository code, or measured test evidence.

Implementation, installation, and production rollout are outside this research brief. They begin only after the research has identified a candidate and the operator has selected the option to test.
