# Production-First Agent Mode KB Update Prompt Flow

## Purpose

Create a continuation-based prompt flow that converts the core learning from the failed Agent Mode runs into concrete updates for:

1. the GPT Agent Mode browser subscription playbook;
2. the Prompt Design agent KB;
3. the Workflow / Process agent KB;
4. shared OpenClaw / Special Ops KB doctrine;
5. a final verification pass after real artifacts exist.

The central learning is:

> For subscription-browser Agent Mode runs, heavy pre-analysis, source gates, ledgers, and governance artifacts can crowd out the actual deliverable. The safer high-impact pattern is **production-first iteration**: produce the target files or unified diff first, then validate, audit, and research against the produced artifact.

---

## Binding operating principle

### Production-first rule

For file-creation, KB-update, prompt-design, and workflow-design tasks, the first production run must create the requested output artifact directly unless a truly blocking source or permission failure prevents it.

Do not replace production with:

- batch-scope contracts;
- source-claim caches;
- broad ledgers;
- group-level control artifacts;
- all-system audits;
- acceptance-test definitions without execution;
- “recommended next action” instead of the requested file/diff.

### Correct iteration model

Use this sequence:

1. **Produce:** create the requested target file or unified diff.
2. **Validate:** check the concrete artifact against scope, patchability, source fit, and plausibility.
3. **Improve:** create a second-pass diff if validation reveals defects.
4. **Document learning:** only after a concrete artifact exists.

Do not use this sequence:

1. Pre-analysis.
2. Ledger.
3. Source gate.
4. Meta-audit.
5. Plan.
6. No target output.

---

## How to use this flow

Run one step per chat turn. Do not combine steps.

Use these continuation commands:

| Command | Output artifact |
|---|---|
| `CONTINUE 1` | Learning decision record for the production-first doctrine |
| `CONTINUE 2` | Unified diff for `GPT_Agent_Mode_Business_Playbook.md` |
| `CONTINUE 3` | Unified diff for Prompt Design agent KB files |
| `CONTINUE 4` | Unified diff for Workflow / Process agent KB files |
| `CONTINUE 5` | Unified diff for shared KB / operating doctrine files |
| `CONTINUE 6` | Post-production validation report over the produced diffs |
| `CONTINUE 7` | Final integration pack and next-run Agent Mode prompt template |

Each continuation step must return a downloadable Markdown artifact and a compact status note. No step may create unrelated control files.

---

# CONTINUE 1 — Create the learning decision record

## Role

You are a master AI workflow and prompt-design learning architect.

## Task

Create one concise but high-evidence learning decision record capturing the production-first doctrine learned from the failed Agent Mode runs.

## Inputs

Use only the attached/current files:

- `PromptDesignFB.md`
- `2ndAgentModeAudit.md`
- `Agent_Mode_KB_Factory_Audit.md`
- `chat thinking.md`
- `chat thinking 2.md`
- `GPT_Agent_Mode_Business_Playbook.md`
- this conversation’s user feedback

## Output artifact

Create:

```text
Production_First_Iteration_Learning_Record.md
```

## Required structure

```markdown
# Production-First Iteration Learning Record

## 1. Core learning

## 2. Evidence from failed runs
| Evidence | What happened | Why it matters | Impact |
|---|---|---|---|

## 3. New doctrine

## 4. Anti-pattern to reject

## 5. Positive operating pattern

## 6. Risk / evidence / impact classification
| Claim | Evidence strength | Impact | Risk if adopted | Risk if ignored | Verdict |
|---|---:|---:|---:|---:|---|

## 7. Integration targets
| Target KB/playbook file | Exact doctrine to add | Priority |
|---|---|---|

## 8. Promotion rule
```

## Execution rules

- Produce the artifact directly.
- Do not create a broad audit.
- Do not create a plan for future work instead of the learning record.
- Keep it under 1,800 words.
- Make the learning actionable enough to patch KB files in later steps.

---

# CONTINUE 2 — Patch the GPT Agent Mode Business Playbook

## Role

You are a master prompt designer for GPT Agent Mode in the subscription browser window.

## Task

Create a unified diff updating `GPT_Agent_Mode_Business_Playbook.md` so it explicitly teaches production-first Agent Mode prompting and warns against overbuilt pre-analysis flows.

## Inputs

Use only:

- `GPT_Agent_Mode_Business_Playbook.md`
- `Production_First_Iteration_Learning_Record.md` if already created
- `PromptDesignFB.md`
- `2ndAgentModeAudit.md`
- this user feedback

## Output artifact

Create:

```text
GPT_Agent_Mode_Business_Playbook.production_first.patch.md
```

## Required output structure

```markdown
# GPT Agent Mode Business Playbook — Production-First Patch

## Patch summary
| Target section | Change | Reason | Risk/evidence/impact |
|---|---|---|---|

## Unified diff
```diff
...
```

## Validation
| Check | Result | Notes |
|---|---|---|
```

## Patch goals

Add doctrine for:

1. **Production-first file/diff runs:** when the deliverable is a file or patch, produce the file/patch before broad validation.
2. **No control-artifact substitution:** forbid replacing requested files/diffs with ledgers, manifests, or meta-audits unless explicitly requested.
3. **Iteration that actually stops:** require explicit stop points such as “stop after this file/diff and wait for CONTINUE.”
4. **Validation after artifact:** move source checks, plausibility, risk, and secondary research after the first concrete output exists.
5. **One unit of work:** one agent, one folder, one file group, or one diff per Agent Mode run.
6. **Completion standard:** an Agent Mode run is not complete until the target artifact exists and is validated, not when it recommends a next action.

## Forbidden behavior

- Do not rewrite the whole playbook.
- Do not create a new playbook.
- Do not create a separate audit report.
- Do not include general OpenAI marketing guidance.
- Do not add long theoretical sections.

## Validation rules

- The diff must be minimal and section-targeted.
- The patch must preserve the existing playbook structure.
- The new doctrine must be findable in the playbook by a future prompt designer.

---

# CONTINUE 3 — Patch the Prompt Design agent KB

## Role

You are a master KB architect for the Prompt Design agent.

## Task

Create a unified diff updating the Prompt Design agent KB so it encodes the production-first doctrine as a core prompt-design rule.

## Target files

Patch only the Prompt Design agent’s existing KB files. Expected folder:

```text
docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/agents/prompt_design/
```

Files, in order:

1. `BEST_PRACTICES.md`
2. `MISTAKES_FAILURES.md`
3. `LEARNING.md`
4. `AGENT_CARD.md`
5. `ESSENCE.md`

## Output artifact

Create:

```text
Prompt_Design_Agent.production_first.patch.md
```

## Required output structure

```markdown
# Prompt Design Agent — Production-First Patch

## Patch summary
| File | Edit zones | Change | Reason |
|---|---|---|---|

## Unified diff
```diff
...
```

## Validation
| Check | Result | Notes |
|---|---|---|
```

## Required doctrine updates

Add or reinforce:

- Prompt design must make the **target artifact impossible to miss**.
- The first objective must be concrete production, not pre-analysis.
- Guardrails must be subordinate to output delivery.
- “Do not” rules must not outnumber or overpower “produce this” rules.
- Iteration must be enforced with actual stop conditions.
- For file/diff tasks, validation happens after the first artifact exists.
- Risk/evidence/impact belongs in the artifact’s review layer, not as a substitute for the artifact.

## Anti-patterns to add

- Governance-first prompt.
- Ledger-as-output drift.
- Validation theater.
- Source-gate paralysis.
- Meta-analysis loop.
- Recommended-next-action instead of delivered artifact.

## Forbidden behavior

- Do not patch non-Prompt-Design agent files.
- Do not create new control files.
- Do not re-audit the whole KB.
- Do not expand into workflow agent doctrine except where necessary for boundaries.

---

# CONTINUE 4 — Patch the Workflow / Process agent KB

## Role

You are a master workflow-process KB architect.

## Task

Create a unified diff updating the Workflow / Process agent KB so it encodes production-first iteration as the default workflow for file/diff creation tasks.

## Target files

Patch only the Workflow / Process agent’s existing KB files. Expected folder:

```text
docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/agents/workflow_process/
```

Files, in order:

1. `BEST_PRACTICES.md`
2. `MISTAKES_FAILURES.md`
3. `LEARNING.md`
4. `AGENT_CARD.md`
5. `ESSENCE.md`

## Output artifact

Create:

```text
Workflow_Process_Agent.production_first.patch.md
```

## Required doctrine updates

Add or reinforce:

- Default production loop: **produce → validate → improve → document learning**.
- Pre-analysis cap: maximum 10–20% of run unless explicitly requested.
- Artifact-first workflow: first checkpoint must be a usable draft/diff/file, not a planning artifact.
- Iterative stopping: one unit per turn/run; stop after the concrete artifact.
- Validation must inspect an existing artifact, not hypothetical requirements.
- Broad control runs are allowed only when the user explicitly asks for control/audit/governance work.

## Required output structure

```markdown
# Workflow / Process Agent — Production-First Patch

## Patch summary
| File | Edit zones | Change | Reason |
|---|---|---|---|

## Unified diff
```diff
...
```

## Validation
| Check | Result | Notes |
|---|---|---|
```

## Forbidden behavior

- Do not patch non-Workflow agent files.
- Do not create a workflow manifesto.
- Do not create a standalone audit.
- Do not recommend another pre-analysis pass.

---

# CONTINUE 5 — Patch shared KB / operating doctrine

## Role

You are a master OpenClaw KB integration architect.

## Task

Create a unified diff integrating the production-first learning into shared operating doctrine files, only where it belongs.

## Candidate target files

Use the attached/current files and patch only those where the doctrine clearly fits:

- `LEARNING_SYSTEM.md`
- `PROCESS_BLUEPRINT_SYSTEM.md`
- `QA_HYGIENE_PROTOCOL.md`
- `PROJECT_ROUTING.md`
- `AGENT_SWARM_INTERACTION_CANON.md`
- `OPERATING_SPINE_CANON.md`

## Output artifact

Create:

```text
Shared_KB.production_first.patch.md
```

## Selection rule

Patch at most three shared files. Choose the files with the highest direct fit. Do not patch everything.

## Required doctrine updates

Capture:

- Production-first iteration as a promoted learning.
- Validation-after-artifact as QA doctrine.
- Avoiding meta-control sprawl as hygiene doctrine.
- Routing rule: if user asks for a file/diff, route to production mode, not audit mode.

## Required output structure

```markdown
# Shared KB — Production-First Patch

## Target selection
| File | Selected? | Reason |
|---|---|---|

## Unified diff
```diff
...
```

## Validation
| Check | Result | Notes |
|---|---|---|
```

## Forbidden behavior

- Do not patch more than three shared files.
- Do not create a new operating system layer.
- Do not alter runtime config.
- Do not rewrite existing doctrine wholesale.

---

# CONTINUE 6 — Validate produced artifacts after they exist

## Role

You are a strict but production-friendly QA auditor.

## Task

Validate the already produced production-first diffs. Do not create new doctrine unless the validation finds a concrete defect.

## Inputs

Use the artifacts from CONTINUE 2–5.

## Output artifact

Create:

```text
Production_First_Update_Validation_Report.md
```

## Required structure

```markdown
# Production-First Update Validation Report

## Executive verdict
pass | revise | fail

## Artifact inventory
| Artifact | Exists? | Scope correct? | Patch usable? | Verdict |
|---|---|---|---|---|

## Risk / evidence / impact review
| Finding | Evidence | Risk | Impact | Action |
|---|---|---:|---:|---|

## Doctrine consistency check
| Doctrine | Playbook | Prompt Design Agent | Workflow Agent | Shared KB | Consistent? |
|---|---|---|---|---|---|

## Required fixes
| Fix | Target artifact | Priority |
|---|---|---|

## Promotion recommendation
```

## Rules

- Validate only existing artifacts.
- Do not recommend a new pre-analysis run.
- If fixes are needed, specify exact patch target and edit zone.

---

# CONTINUE 7 — Create final integration pack and next-run prompt template

## Role

You are a master prompt designer for GPT Agent Mode production runs.

## Task

Create the final integration pack that summarizes all updates and provides a corrected reusable Agent Mode prompt template for future one-agent/five-file KB diff runs.

## Output artifact

Create:

```text
Final_Production_First_Agent_Mode_Integration_Pack.md
```

## Required structure

```markdown
# Final Production-First Agent Mode Integration Pack

## 1. What changed

## 2. Files patched
| File | Purpose of patch | Status |
|---|---|---|

## 3. Core doctrine now added

## 4. Future Agent Mode prompt template
```text
/agent
...
```

## 5. Operator checklist

## 6. Anti-pattern checklist

## 7. Promotion recommendation
```

## Future Agent Mode template requirements

The template must enforce:

- one selected agent;
- exactly five target files;
- no control artifacts;
- no all-system audit;
- one unified diff;
- validation after diff creation;
- explicit stop after the artifact;
- no recommendation-only completion.

---

## Meta-rules for every continuation step

1. **Produce the artifact first.** A compact patch summary is allowed, but no broad pre-analysis.
2. **No substitute outputs.** Do not replace requested diffs/files with plans, ledgers, or audits.
3. **One output unit only.** Each continuation step creates exactly one artifact.
4. **Risk/evidence/impact belongs after production.** Use it for validation, not for avoiding output.
5. **No uncontrolled expansion.** Do not patch extra files unless the step explicitly allows them.
6. **No “next action” as completion.** The step is complete only when the artifact exists.
7. **Be honest about blockers.** If a target file is unavailable, create a blocker section and stop that step.
