# V4 Agent-Execution Format — Research Basis (NOT REQUIRED FOR EXECUTION)

This file records why the execution bundle is structured this way.  
The lead executor should **not** load this file during normal execution.

## Primary patterns used

### OpenAI — ExecPlans

OpenAI's published ExecPlan guidance treats complex plans as self-contained, living execution specifications with:
- explicit user-visible outcome;
- exact commands and observable acceptance;
- progress state;
- discoveries;
- decisions;
- outcomes/retrospective;
- autonomous continuation rather than repeatedly asking for next steps.

Source:
https://github.com/openai/openai-cookbook/blob/main/articles/codex_exec_plans.md

### OpenAI — harness engineering

OpenAI reports that a giant AGENTS.md/instruction manual caused agents to miss constraints and optimize for the wrong things. Their preferred pattern is:
- a short stable map;
- repository-local system of record;
- execution plans as first-class artifacts;
- progressive disclosure.

Source:
https://openai.com/index/harness-engineering/

### Anthropic — subagents

Claude Code documentation recommends subagents for self-contained or high-volume work because they use fresh context windows and return only summaries. It recommends focused subagents, detailed descriptions, and restricted tools.

Source:
https://code.claude.com/docs/en/sub-agents

### Anthropic — orchestrator/worker delegation

Anthropic's multi-agent engineering write-up reports that delegated tasks need:
- objective;
- output format;
- tools/sources;
- clear boundaries.

Without those, workers duplicate work or leave gaps.

Source:
https://www.anthropic.com/engineering/multi-agent-research-system

### Anthropic — context engineering

Anthropic recommends specialized subagents with clean context windows for focused technical work, with a lead agent coordinating from a high-level plan and receiving condensed results.

Source:
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Translation into this bundle

- `00-START-HERE.md` is the small map.
- `01-EXECUTION-MAP.yaml` is canonical orchestration/architecture.
- `02-AGENT-CONTRACTS.yaml` makes worker delegation explicit.
- `04-EXECUTION-STATE.yaml` is the living plan state.
- Each file under `modules/` is one progressive-disclosure task packet.
- The lead keeps global state; workers isolate install/debug noise.
- Acceptance is observable mechanical behavior; semantic product quality remains operator-owned.
