# Agent Mode vs Extended Thinking vs Deep Research — Routing Baseline

## 1. Core ruling

Agent Mode should **not** be the default for OpenClaw KB architecture, prompt design, doctrine synthesis, or one-agent/five-file markdown patch work.

Agent Mode is best treated as an **action-execution and tool-orchestration mode**: use it when the value comes from navigating websites, using a visual browser, crossing apps, filling forms, manipulating remote UI state, editing spreadsheets, or performing supervised multi-step online actions.

For OpenClaw-style reasoning, realignment, KB synthesis, prompt-flow design, and markdown/diff production, prefer **extended thinking in normal ChatGPT / Pro reasoning mode with direct repo/file access**. That mode is more inspectable, more steerable turn-by-turn, and less likely to turn the task into an autonomous “process run” that substitutes plans, ledgers, or validation theater for the requested artifact.

## 2. Decision table

| Work type | Use | Avoid | Reason |
|---|---|---|---|
| Browser/UI action | Agent Mode | Extended thinking only | Agent Mode’s value is using a browser/computer-like environment and apps. |
| Authenticated website operation | Agent Mode with supervision | Deep research | Needs stateful interaction, clicks, forms, and possible user confirmation. |
| Spreadsheet manipulation through UI or app | Agent Mode | Deep research | Agent Mode can act on spreadsheets, not only report on them. |
| Multi-app operational task | Agent Mode | Pure chat | Example: calendar + email + website + downloadable output. |
| Long source synthesis | Deep Research or extended thinking | Agent Mode | Research/digestion is not mainly a browser-action problem. |
| OpenClaw KB doctrine design | Extended thinking | Agent Mode | Needs controllable reasoning, source comparison, and exact wording. |
| Prompt design | Extended thinking | Agent Mode | Prompt design should be iterative and inspectable, not autonomous browser execution. |
| One-agent/five-file KB patch | Extended thinking / repo-aware chat / Codex | Agent Mode | The target is exact text/diff production; a browser agent adds risk. |
| Mechanical code edit + tests | Codex or repo-aware coding tool | Agent Mode browser | Needs patch/test loop, not visual navigation. |
| Final validation after artifact exists | Extended thinking or code tool | Agent Mode as default | Validation should inspect concrete outputs; Agent Mode is overkill unless external UI checks are required. |
| External benchmark/research report | Deep Research | Agent Mode | Deep Research is designed for planned, cited, multi-source synthesis. |
| Scheduled external monitoring | Agent Mode / scheduled task if supported | Extended thinking | The value is repeated tool use or online checking. |

## 3. Primary doctrine

### Rule 1 — Tool-orchestration threshold

Use Agent Mode only when at least one of these is true:

- **Browser state:** the task requires navigating websites or visual UI.
- **External action:** the task requires filling forms, downloading/uploading through UI, changing settings, or interacting with accounts.
- **Multi-app operation:** the task needs several apps/connectors in one supervised workflow.
- **Spreadsheet/UI manipulation:** the task requires acting on spreadsheet-like objects through tools or UI.
- **Recurring operational task:** the task should later be scheduled or repeated as an online action.
- **Action trail matters more than reasoning trace:** the hard part is doing steps, not designing the concept.

If none are true, do not default to Agent Mode.

### Rule 2 — Reasoning and KB work defaults to extended thinking

Use extended thinking when the task requires:

- architectural judgment;
- prompt design;
- doctrine synthesis;
- reading and comparing files;
- producing markdown;
- writing unified diffs;
- reviewing existing output;
- designing process flows;
- generating KB updates;
- validating produced artifacts.

### Rule 3 — Deep Research is for synthesis, not repo mutation

Use Deep Research when the task is:

- multi-source;
- external/public-web or connector-backed;
- requires citation-heavy synthesis;
- needs a report;
- does not require applying repo changes or performing UI actions.

### Rule 4 — Codex/repo tools for repo mutation

Use Codex or direct repo/file tools when the task is:

- apply a patch;
- run tests;
- validate `git apply`;
- create or edit files inside a repository;
- inspect code or markdown paths precisely.

## 4. Risk classification

| Pattern | Evidence strength | Impact | Risk if adopted | Risk if ignored | Verdict |
|---|---:|---:|---:|---:|---|
| Agent Mode for browser/app action | High | High | Medium: needs supervision | High: manual work remains | Use |
| Agent Mode for KB/prompt reasoning | High | High | High: autonomous run drifts or over-produces meta-work | High: repeated failures | Avoid by default |
| Extended thinking for KB synthesis | High | High | Low: slower but inspectable | High: Agent Mode repeats control drift | Use |
| Deep Research for external synthesis | High | Medium-high | Low-medium: slower, report-like | Medium: shallow research | Use when source breadth matters |
| Codex/repo tools for patch/test | High | High | Medium: requires patch hygiene | High: invalid diffs | Use |
| Governance-first Agent Mode prompts | Very high | High | High: ledgers replace artifacts | Very high | Reject |
| Produce → validate → improve loop | High | High | Low-medium: first draft may need repair | High: endless pre-analysis | Adopt |

## 5. OpenClaw routing law

### Default mode map

| Task request | Route |
|---|---|
| “Create / patch / update these KB files” | Extended thinking + repo/file tools |
| “Design a prompt flow” | Extended thinking |
| “Audit previous outputs and derive doctrine” | Extended thinking, optionally with web or Deep Research if public best practice is needed |
| “Research current external best practices” | Deep Research or web-backed extended thinking |
| “Use the browser to do X online” | Agent Mode |
| “Fill in / submit / operate external UI” | Agent Mode |
| “Run patch + tests in repo” | Codex or repo-aware execution environment |
| “Do all of the above” | Split: research/design first in thinking mode, then tool/action in Agent Mode or Codex |

### Red-line rule

Do not use Agent Mode for a task whose success condition is mostly a **precise text artifact** unless a browser/app action is necessary to obtain or deliver that artifact.

## 6. Prompt-design update text

Add this to prompt-design best practices:

> Agent Mode is not the default for prompt design, KB synthesis, doctrine repair, or exact markdown/diff production. Use Agent Mode when the task’s value comes from acting through tools, websites, apps, forms, spreadsheets, or other external UI. For reasoning-heavy artifact work, use extended thinking with direct repo/file access and a produce → validate → improve loop.

Add this to workflow/process best practices:

> Route work by bottleneck. If the bottleneck is reasoning, synthesis, or exact artifact wording, use extended thinking. If the bottleneck is external action across web/apps/tools, use Agent Mode. If the bottleneck is code/repo mutation and validation, use Codex or repo-aware execution. Do not send KB or prompt-design work into Agent Mode merely because it is “complex.”

Add this to QA/Hygiene:

> **Governance-first substitution** includes misrouting a reasoning/artifact task into Agent Mode, where the run produces planning, logs, ledgers, or reports instead of the requested artifact. Closure requires the actual target artifact, not a better next-step plan.

## 7. Agent Mode prompt gate

Before using Agent Mode, answer these five questions:

1. Does this task require a visual browser, website UI, app connector, form submission, or remote spreadsheet operation?
2. Is the expected output an action result, not mainly a doctrine/report/diff?
3. Can the task be safely completed in one autonomous supervised run?
4. Are the external-action permissions and confirmation boundaries clear?
5. Would extended thinking with repo/file access be worse because the bottleneck is tool operation rather than reasoning?

Use Agent Mode only if the answer to question 1 is yes and at least three of questions 2–5 are yes.

## 8. Updated operating mantra

> Agent Mode is an operator.  
> Deep Research is a researcher.  
> Extended thinking is an architect/writer.  
> Codex/repo execution is a patch/test worker.  
> Do not ask the operator to become the architect unless the task actually requires operating external tools.
