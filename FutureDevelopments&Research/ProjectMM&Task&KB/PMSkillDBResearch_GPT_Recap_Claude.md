# APEX PM ARCHITECTURE SESSION — Result

## Step 1 — Skill/community search result

### Bottom line

|Finding|Result|
|---|---|
|Hermes PM skill ecosystem|**Not found.** Searched: `NousResearch Hermes agent skills project management GitHub`, `Hermes AI agent skills SKILL.md project management GitHub`, `Hermes Agent skill repository project management Python`, `site:github.com Hermes Agent skills SKILL.md`. I found Hermes/model/tool-use references, but no verified Hermes PM skill database with portable Python PM skills.|
|Better-than-prior PM spine|**No exact community PM system found.** No discovered system is a ready clone of Apex’s multi-domain project-kb-manager.|
|Better architecture pattern found|**Yes.** OpenClaw TaskFlow + CrewAI task design + LangGraph-style stateful execution are stronger for the Python/AI split than the earlier pure-Markdown PM tools.|
|Import strategy|**Layered import, not one spine.** Use existing battle-tested patterns by layer.|

### Candidate ranking

|Rank|Candidate|What it is|Fit for Apex|Verdict|
|--:|---|---|---|---|
|**1**|**OpenClaw TaskFlow / Skills**|Local AI assistant with Markdown skills, skill registry, TaskFlow runtime, Python scripts, and local-first patterns. The repo exposes a `skills/` directory with many skills, including `taskflow`, `model-usage`, `gh-issues`, `trello`, and others. ([GitHub](https://github.com/openclaw/openclaw "GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way.  · GitHub"))|Best discovered **skill-style pattern** for durable task state + deterministic tooling + AI decisions.|Import TaskFlow lifecycle and Python-script pattern. Do **not** import OpenClaw wholesale.|
|**2**|**CrewAI + CrewAI Skills**|Python multi-agent framework with official Agent Skills-format skill repo. It defines Crews, Flows, YAML task/agent configs, Python code integration, structured outputs, guardrails, dependencies, human review, and output files. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub"))|Best discovered **Python + AI task design pattern**.|Import task design grammar: task dependencies, expected output, guardrails, structured output, output files.|
|**3**|**LangGraph**|Python framework for long-running, stateful agent workflows with durable execution, human-in-the-loop, memory, debugging, and deployment. ([GitHub](https://github.com/langchain-ai/langgraph "GitHub - langchain-ai/langgraph: Build resilient agents. · GitHub"))|Best future **state-machine layer** if Apex outgrows simple scripts.|Reference for later; not needed for v1 unless the Python layer becomes a graph engine.|
|**4**|**Agent Skills ecosystem / ClawHub / skill libraries**|Large and growing skill ecosystem. Research finds tens of thousands of public skills, mostly software/info/content oriented, with security risks. ([arXiv](https://arxiv.org/abs/2602.08004?utm_source=chatgpt.com "Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality"))|Useful for skill packaging norms and security lessons, not PM logic.|Reference only. Never blindly clone marketplace skills.|
|**5**|**AutoGen**|Microsoft agent framework, but repo states it is in maintenance mode and new users should use Microsoft Agent Framework. ([GitHub](https://github.com/microsoft/autogen "GitHub - microsoft/autogen: A programming framework for agentic AI · GitHub"))|Not primary for Apex.|Reference only.|
|**6**|Prior PM tools: CCPM, Backlog.md, Task Master, GSD, planning-with-files|Partial-fit PM/task/context tools from prior research.|Still useful as pattern libraries.|Keep narrow imports only.|

## Step 2 — Actual files read

## Candidate 1: OpenClaw TaskFlow / Skills

### Files read

|File|Evidence|
|---|---|
|`skills/taskflow/SKILL.md`|Defines TaskFlow as durable detached task coordination with owner context, persisted state, waits, child tasks, lifecycle, revision tracking. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|
|`skills/taskflow-inbox-triage/SKILL.md`|Shows TaskFlow used for inbox triage: create flow, run detached classification, persist state, wait, resume, finish. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow-inbox-triage/SKILL.md "raw.githubusercontent.com"))|
|`skills/model-usage/SKILL.md`|Uses a Python script to summarize local model cost logs; explicitly routes deterministic summarization to script. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/model-usage/SKILL.md "raw.githubusercontent.com"))|
|`skills/model-usage/scripts/model_usage.py`|Python parses args, reads JSON or subprocess output, filters dates, aggregates cost by model, renders text/JSON. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/model-usage/scripts/model_usage.py "raw.githubusercontent.com"))|
|`skills/taskflow/examples/inbox-triage.lobster`|Deterministic fetch + LLM JSON classification + deterministic branching/action. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/examples/inbox-triage.lobster "raw.githubusercontent.com"))|
|`skills/taskflow/examples/pr-intake.lobster`|Deterministic GitHub PR fetch + LLM JSON classification + deterministic branching/action. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/examples/pr-intake.lobster "raw.githubusercontent.com"))|

### Extracted pattern

|Area|What OpenClaw does|Apex import|
|---|---|---|
|Python/deterministic operations|Reads structured data, runs subprocesses, parses JSON, filters, aggregates, renders output. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/model-usage/scripts/model_usage.py "raw.githubusercontent.com"))|Python reads `.claude/kb/projects/*.md`, computes scores, generates registry, appends logs.|
|AI reasoning|Uses LLM for classification/recommendation into constrained JSON, then deterministic runtime branches on that JSON. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/examples/inbox-triage.lobster "raw.githubusercontent.com"))|Claude synthesizes next action, implicit blockers, and focus recommendation into structured packet.|
|State model|TaskFlow owns `flowId`, owner, `currentStep`, `stateJson`, `waitJson`, linked children, lifecycle, revision tracking. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Apex should use compact YAML frontmatter + Markdown body, plus append-only progress log and revision/stale checks.|
|Operator output|TaskFlow emphasizes resumable state, waits, summaries, and lifecycle transitions. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Apex output should show current focus, why, blockers, next Precap signal, validation flags.|
|Boundary rule|TaskFlow explicitly says runtime owns state/linkage, not business logic; decisions live above runtime. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Core Apex rule: Python owns deterministic state; Claude owns reasoning.|

**Import verdict:** OpenClaw TaskFlow is the best discovered pattern for Apex’s **durable operation wrapper**, not for Apex’s PM schema.

---

## Candidate 2: CrewAI + CrewAI Skills

### Files read

|File|Evidence|
|---|---|
|`crewAIInc/crewAI` README|CrewAI has Crews and Flows; Flows provide event-driven workflows, fine-grained execution paths, secure state management, Python code integration, and conditionals. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub"))|
|`crewAIInc/skills` README|Official CrewAI skills follow Agent Skills format; includes `getting-started`, `design-agent`, `design-task`, `ask-docs`. ([GitHub](https://github.com/crewAIInc/skills "GitHub - crewAIInc/skills · GitHub"))|
|`skills/design-task/SKILL.md`|Defines task design: description, expected output, dependencies via `context`, structured output, guardrails, human review, async execution, output files. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|
|`skills/getting-started/SKILL.md`|Defines when to use LLM call, Agent, Crew, or Flow; says use Flow for production apps requiring deterministic steps, state, and conditional logic. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/getting-started/SKILL.md "raw.githubusercontent.com"))|

### Extracted pattern

|Area|What CrewAI does|Apex import|
|---|---|---|
|Python/deterministic operations|Uses Python project structure, `crew.py`, `main.py`, YAML configs, tool files, task objects, output files. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub"))|Apex Python script should be a deterministic local tool package, not hidden prompt logic.|
|AI reasoning|Agents/tasks produce outputs from descriptions and expected outputs; structured outputs can use Pydantic or JSON. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Claude output from project-kb-manager should be schema-bounded: ranked signal, next action, confidence, assumptions, blockers.|
|State files|Uses `agents.yaml`, `tasks.yaml`, `output_file`, structured task configs. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub"))|Apex uses one file per entity with YAML frontmatter and Markdown body, not CrewAI YAML wholesale.|
|Operator output|Task output can be Markdown file, structured output, human-review gated result. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Apex should show one 30-second operator screen plus write `next-precap-context.md` after validation.|
|Boundary rule|`design-task` separates task anatomy, dependencies, structured outputs, guardrails, human review. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Import task object grammar: `description`, `expected_output`, `context`, `guardrail`, `human_review`, `output_file`.|

**Import verdict:** CrewAI is the best discovered pattern for Apex’s **task/operation contract design**, not the PM database itself.

---

# Import spec

## What Apex should import

|Source|Import|Apex adaptation|
|---|---|---|
|**OpenClaw TaskFlow**|Durable flow lifecycle: state bag, wait/resume, child task links, revision checks, decisions above runtime.|`project-kb-manager` operations become resumable local operations with append-only logs and stale/revision flags.|
|**OpenClaw deterministic script pattern**|Python scripts parse inputs, compute deterministic summaries, output text/JSON.|`project_kb_query.py`, `project_kb_update.py`, `project_kb_registry.py` later. No file generation now.|
|**OpenClaw LLM-classify-then-branch pattern**|LLM produces constrained JSON; deterministic runtime acts on fields.|Claude proposes structured deltas; Python writes only explicit validated fields.|
|**CrewAI task design**|Task has description, expected_output, context dependencies, structured output, guardrails, human input, output file.|Apex tasks/chunks/workflows should have compact expected-output and validation fields.|
|**CrewAI Flow abstraction**|Deterministic steps + conditional logic + Python integration.|Future project-kb-manager can become a small local Flow if simple Python scripts become insufficient.|
|**LangGraph**|Durable stateful workflow architecture.|Later escalation path for multi-repo/team scale, not v1.|
|**Backlog.md**|Markdown task frontmatter fields.|Borrow task file grammar only.|
|**Task Master AI**|Dependency/next-task scoring concept.|Borrow scoring idea only.|
|**GSD Core**|`STATE.md` / `CONTEXT.md`.|Add session-continuity artifacts for long Claude Code sessions.|
|**planning-with-files**|2-action write rule, error persistence.|Apply to long KB updates and research tasks.|
|**llms.txt conventions**|LLM-readable Markdown standard.|File format layer for all Apex PM entity files.|

## What Apex should not import

|Source|Do not import|Reason|
|---|---|---|
|OpenClaw wholesale|Full runtime, marketplace, security surface.|Too broad. Security risk from community skills.|
|CrewAI wholesale|Full multi-agent framework.|Apex is Claude Code-native and local-file-first.|
|LangGraph now|Full state graph.|V1 can use plain Python scripts.|
|AutoGen|Primary architecture.|Repo is in maintenance mode. ([GitHub](https://github.com/microsoft/autogen "GitHub - microsoft/autogen: A programming framework for agentic AI · GitHub"))|
|CCPM wholesale|GitHub Issues/worktrees.|Too coupled to software-team execution.|
|Backlog.md wholesale|TypeScript CLI/task board.|Useful task grammar, not planning brain.|
|Task Master wholesale|JSON/MCP/Node stack.|Useful scoring concept, not storage layer.|

# Step 3 — Apex Python/Claude split

## Architecture rule

```yaml
apex_project_kb_manager:
  format_layer: llms_txt_style_markdown
  deterministic_layer: local_python_scripts
  reasoning_layer: Claude_Code_skill
  persistence_layer: git_repo_files
  v1_scope: one_project_apex_os_meta
```

## Operation split

|Operation|Layer|Source pattern|Why this layer|
|---|---|---|---|
|Read project files|Python|OpenClaw `model_usage.py` deterministic file/JSON reading pattern. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/model-usage/scripts/model_usage.py "raw.githubusercontent.com"))|Deterministic. No reasoning needed.|
|Parse YAML frontmatter|Python|CrewAI YAML config pattern. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub"))|Deterministic schema extraction.|
|Validate required fields/enums|Python|CrewAI function guardrail concept. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Deterministic pass/fail.|
|Generate `registry.md` index|Python|OpenClaw script renders summaries from structured input. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/model-usage/scripts/model_usage.py "raw.githubusercontent.com"))|Deterministic aggregation.|
|Append progress log entry|Python|TaskFlow persisted state / revision discipline. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Must be append-only and consistent.|
|Update explicit status/priority fields|Python|Deterministic write after validated input.|Values are explicit. No reasoning needed.|
|Compute `priority_score`|Python|Deterministic scoring + Task Master-inspired dependency scoring.|Formula-based. Token waste if Claude does it.|
|Compute `unlock_depth`|Python|Graph/dependency computation; LangGraph as future model. ([GitHub](https://github.com/langchain-ai/langgraph "GitHub - langchain-ai/langgraph: Build resilient agents. · GitHub"))|Deterministic dependency traversal.|
|Detect blocked dependencies|Python|TaskFlow lifecycle state/check pattern. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Deterministic.|
|Detect stall condition|Python|TaskFlow currentStep/state persistence pattern. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Same `next_action` for 3+ sessions is countable.|
|Produce structured packet for Claude|Python|OpenClaw examples: deterministic data first, LLM receives structured context. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/examples/inbox-triage.lobster "raw.githubusercontent.com"))|Keeps Claude context small.|
|Synthesize `next_action`|Claude|OpenClaw LLM JSON classification/recommendation pattern. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/examples/inbox-triage.lobster "raw.githubusercontent.com"))|Requires interpreting progress, blockers, and intent.|
|Rank focus using operator context|Claude|CrewAI task expected-output reasoning pattern. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Requires judgment beyond numeric score.|
|Merge FlowRecap narrative into state deltas|Claude → Python write|OpenClaw “LLM decides, runtime persists” boundary. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))|Narrative interpretation requires reasoning; persistence must be deterministic.|
|Detect implicit blockers|Claude|LLM classification pattern from OpenClaw examples. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/examples/inbox-triage.lobster "raw.githubusercontent.com"))|Blockers may be unstated.|
|Generate focus recommendation|Claude|CrewAI task output / expected_output model. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Operator-facing synthesis.|
|Write `next-precap-context.md`|Python after Claude packet|Deterministic output-file pattern from CrewAI. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|Final write should be stable and repeatable.|
|Operator validation prompt|Claude|Human review pattern from CrewAI task design. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))|User-facing approval needs explanation.|

# Step 4 — First test run design

## Known input

Accessible Apex project example data confirms:

```yaml
project:
  id: apex-os-meta
  name: Apex OS Meta
  domain_type: dev
  repo_url: https://github.com/leela-spec/apexai-os-meta
  project_status: active
  priority: 90
  urgency: 85
  date: NA
confirmed_milestones:
  M1: project-kb-manager skill
  M2: FlowRecap integration
  M3: PrecapNextDay KB upgrade
```

The uploaded prompt-flow source confirms only M1–M3 names. M4–M8 names were not found in the available project-source snippets, so the mock output must not pretend to know them. The user’s current prompt overrides state to: **M1 complete, M2 in progress, M3–M8 pending**.

## Test sequence

|Step|Action|Layer|Output|
|--:|---|---|---|
|1|Read `apex-os-meta` project record.|Python|Parsed project packet.|
|2|Compute M2 dependency state.|Python|`M2_unblocked: true` because M1 complete.|
|3|Compute known unlock depth.|Python|`known_unlock_depth: 1`, because M2 unlocks M3.|
|4|Detect missing milestone metadata.|Python|`M4_M8_names_missing: true`.|
|5|Send compact packet to Claude.|Python → Claude|Scores, blockers, dependencies, progress log excerpts.|
|6|Synthesize recommendation.|Claude|Focus recommendation + next action + Precap signal.|
|7|Show 30-second operator output.|Claude|Human-readable summary.|
|8|Operator validates.|Marco|Approve / correct / ask to rerank.|

## Python packet mock

```yaml
project_kb_python_packet:
  project_id: apex-os-meta
  project_name: Apex OS Meta
  project_status: active
  priority: 90
  urgency: 85
  date: NA

  current_focus_candidate:
    milestone_id: M2
    milestone_name: FlowRecap integration
    status: in_progress
    dependency_status: unblocked
    depends_on:
      - M1
    completed_dependencies:
      - M1

  known_unlocks:
    - milestone_id: M3
      milestone_name: PrecapNextDay KB upgrade
      blocked_by:
        - M2

  computed:
    priority_score: 90
    urgency_score: 85
    known_unlock_depth: 1
    blocked: false
    stalled: unknown_not_enough_history
    missing_milestone_names:
      - M4
      - M5
      - M6
      - M7
      - M8

  python_recommendation_basis:
    - M2 is active/in_progress
    - M2 is unblocked because M1 is complete
    - M2 unlocks M3
    - M4-M8 cannot be ranked confidently until names/dependencies exist
```

## Operator-facing mock output

````md
# Project KB — Apex OS Meta

## Focus now

**M2 — FlowRecap integration**

**Why:** M1 is complete. M2 is unblocked. Completing M2 unlocks M3 — PrecapNextDay KB upgrade. This makes M2 the current bottleneck for closing the execution-memory loop.

## Ranked signals

| Rank | Item | Status | Signal | Next action |
|---:|---|---|---|---|
| 1 | M2 — FlowRecap integration | in_progress | focus_now | Define the FlowRecap → project-kb delta contract and the first Python-read/Claude-merge packet. |
| 2 | M3 — PrecapNextDay KB upgrade | pending | blocked_by_M2 | Wait until M2 produces stable KB deltas. |
| 3 | M4-M8 | pending | metadata_missing | Add names/dependencies before ranking. |

## Python checks

```yaml
registry_read: true
m1_complete: true
m2_unblocked: true
known_unlock_depth_m2: 1
stall_condition: unknown_not_enough_history
missing_milestone_metadata: [M4, M5, M6, M7, M8]
operator_review_needed: true
````

## PrecapNextDay signal

```yaml
recommended_flow_project: Apex
recommended_focus: FlowRecap integration
recommended_sprint_goal: define FlowRecap-to-project-kb state delta contract
reason: M2 is the unblocked bridge between completed project-kb-manager foundation and future PrecapNextDay KB upgrade.
```

## Validation prompt

Approve this as the next Apex focus, or correct one of:

- M2 next_action
    
- M3 dependency
    
- M4-M8 milestone names
    
- priority/urgency assumptions
    

```

# Import decision table

| Operation | Layer | Source pattern | Why this layer |
|---|---|---|---|
| Read project files | Python | OpenClaw deterministic script pattern. :contentReference[oaicite:42]{index=42} | File reads are deterministic. |
| Parse frontmatter | Python | CrewAI YAML config pattern. :contentReference[oaicite:43]{index=43} | Structured parsing should not spend AI tokens. |
| Validate schema | Python | CrewAI guardrail pattern. :contentReference[oaicite:44]{index=44} | Closed enums and required fields are deterministic. |
| Generate registry | Python | OpenClaw summary-render script pattern. :contentReference[oaicite:45]{index=45} | Aggregation is deterministic. |
| Append progress log | Python | OpenClaw TaskFlow persisted state discipline. :contentReference[oaicite:46]{index=46} | Append-only state must be consistent. |
| Compute priority score | Python | Deterministic formula + prior Task Master scoring concept. | Formula-based. |
| Compute unlock depth | Python | Graph traversal; LangGraph is later escalation model. :contentReference[oaicite:47]{index=47} | Dependency traversal is deterministic. |
| Detect stall | Python | TaskFlow currentStep/state persistence pattern. :contentReference[oaicite:48]{index=48} | Repeated `next_action` count is deterministic. |
| Produce Claude packet | Python | OpenClaw deterministic-context-before-LLM pattern. :contentReference[oaicite:49]{index=49} | Keeps context small and stable. |
| Synthesize next_action | Claude | LLM JSON classification/recommendation pattern. :contentReference[oaicite:50]{index=50} | Requires reasoning over intent and context. |
| Rank focus | Claude | CrewAI expected-output task reasoning. :contentReference[oaicite:51]{index=51} | Requires operator-context judgment. |
| Merge FlowRecap narrative | Claude → Python | OpenClaw separation: runtime owns state, authoring layer owns decisions. :contentReference[oaicite:52]{index=52} | Narrative needs reasoning; writes need determinism. |
| Detect implicit blockers | Claude | LLM classification pattern. :contentReference[oaicite:53]{index=53} | Blockers may be implicit. |
| Write next-precap-context | Python | CrewAI output-file pattern. :contentReference[oaicite:54]{index=54} | Final write should be stable. |
| Ask operator validation | Claude | CrewAI human-review pattern. :contentReference[oaicite:55]{index=55} | Human gate needs concise explanation. |

The first test run will show Marco: a 30-second Apex focus screen naming M2 FlowRecap integration as the unblocked next bottleneck, showing why it unlocks M3, flagging missing M4–M8 metadata, and asking for validation before any files are changed.
```