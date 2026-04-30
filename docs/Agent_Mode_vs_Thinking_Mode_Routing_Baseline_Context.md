# Agent Mode vs Extended Thinking vs Deep Research - Routing Baseline Context

## 1. Purpose

This companion context records the reasoning behind `docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md`.

It exists to preserve the lesson that Agent Mode is not bad; it is wrong when routed to work whose bottleneck is precise reasoning, doctrine, prompt design, KB writing, markdown, or unified diff production.

## 2. Core correction

The corrected doctrine is:

> Agent Mode is for complex tool action. Extended thinking is for complex reasoning. Deep Research is for complex source synthesis. Codex/repo tools are for complex patch execution and validation.

The earlier failure pattern was not merely weak prompting or insufficient diligence. The deeper issue was **mode-mismatch substitution**: a task was routed into a mode whose strengths did not match the bottleneck, causing the run to produce the wrong class of output.

## 3. Classification verdict

| Work type | Best mode | Why |
|---|---|---|
| Browser, website, or UI task | Agent Mode | The bottleneck is external action through a browser or app. |
| Multi-app operational workflow | Agent Mode | The hard part is operating across tools, not composing doctrine. |
| In-depth external research report | Deep Research | The bottleneck is broad source discovery, synthesis, and citations. |
| KB architecture, prompt design, workflow doctrine | Extended thinking | The hard part is judgment, synthesis, exact wording, and controllable iteration. |
| Repo file reading and markdown/diff production | Extended thinking with repo/file tools, or Codex for application/testing | The target is a precise text artifact, not a browser action. |
| Patch application and tests | Codex or repo-aware execution | The bottleneck is mechanical repo mutation and validation. |
| Audit after produced artifacts exist | Extended thinking | The work requires close inspection of concrete outputs, not autonomous process expansion. |

## 4. Failure analysis

### 4.1 The value model was wrong for the task

The failed task pattern was mostly:

```text
read known files -> reason about source fit -> produce exact KB artifacts or diffs
```

That is controlled writing, architecture, and patch synthesis work. It is not primarily browser or computer-use work.

### 4.2 Agent Mode executed the prompt shape too literally

When a prompt over-specifies gates, phases, reports, ledgers, validation plans, or audit machinery, Agent Mode may faithfully execute those surrounding structures instead of forcing closure on the requested target artifact.

That is useful when the user needs an autonomous operator. It is risky when the user needs a precise file, exact markdown body, or validated diff.

### 4.3 Production-first Agent Mode prompts can still drift

Even improved prompts can slip back into process-first behavior if they preserve too much phase machinery. A three-phase Agent Mode run can still spend disproportionate effort on source reports and patch-planning tables instead of producing the artifact.

## 5. Mode-mismatch substitution

**Definition:** the task is routed to a mode whose strengths do not match the bottleneck, causing the system to produce the wrong kind of output.

| Misroute | Typical failure |
|---|---|
| KB writing -> Agent Mode | Produces reports, plans, ledgers, or control artifacts instead of exact files. |
| Research synthesis -> Agent Mode | Over-executes and drifts through tools instead of synthesizing evidence. |
| Browser task -> extended thinking | Gives advice instead of acting. |
| Patch/test task -> normal chat only | Produces unverified diffs or unchecked instructions. |
| Architecture task -> autonomous agent run | Loses user steering and over-plans. |

**Severity:** P1 when the user asked for a concrete artifact and the run returns only meta-work.

## 6. Practical routing rule

For current OpenClaw KB and prompt-flow work:

1. Do not use Agent Mode for prompt design, workflow design, KB synthesis, doctrine repair, exact markdown, or unified diff production by default.
2. Use extended thinking for source digestion and artifact creation.
3. Use Agent Mode only when a browser, app, website, spreadsheet, or external UI action is actually required.
4. Use Deep Research when the target is broad cited research, not repo mutation.
5. Use Codex/repo tooling when patches must be applied, tested, or mechanically checked.

## 7. Integration consequence

This context supports three integration surfaces:

- `managed/agent_kb/special_ops__ai_handling_routing/MISTAKES.md` for the durable AI-routing mistake pattern.
- `managed/rules/QA_HYGIENE_PROTOCOL.md` for the hygiene consequence when mode mismatch replaces requested artifacts with control theater.
- later cross-reference and playbook reconciliation surfaces, so Agent Mode playbooks do not imply that Agent Mode is the default for exact KB/diff production.
