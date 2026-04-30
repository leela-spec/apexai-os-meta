I agree with the core hypothesis, with one important correction:

**Agent Mode is not “bad.” It is misrouted for your current KB/prompt/workflow work.**  
Your failed runs show that Agent Mode is behaving like an autonomous operator: it executes the task definition literally, tends to continue through phases, and can overproduce surrounding process artifacts when the prompt contains many gates. That is useful for **browser/app/tool execution**, but risky for **doctrine, prompt design, repo KB architecture, and exact diff writing**.

I created the baseline artifact here:

[Download `Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md`](sandbox:/mnt/data/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md)

---

## 1. Classification verdict

|Work type|Best mode|Why|
|---|---|---|
|**Browser / website / UI tasks**|**Agent Mode**|Agent Mode is explicitly built to navigate websites, use a visual browser, connect apps, fill forms, edit spreadsheets, run code, and take actions on your behalf. ([OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent "ChatGPT agent \| OpenAI Help Center"))|
|**Multi-app operational workflows**|**Agent Mode**|Best when the hard part is executing across tools/apps, not reasoning about doctrine.|
|**In-depth external research report**|**Deep Research**|Deep Research is explicitly designed to plan, research, synthesize, and return a documented report with citations. ([OpenAI Help Center](https://help.openai.com/articles/10500283 "Deep research in ChatGPT \| OpenAI Help Center"))|
|**KB architecture / prompt design / workflow doctrine**|**Extended thinking / Pro reasoning**|The hard part is reasoning, synthesis, and exact wording. Agent Mode adds autonomous execution risk without adding much value.|
|**Repo file reading + markdown/diff production**|**Extended thinking with repo/file tools, or Codex for application/testing**|The target is a precise text artifact, not a browser action.|
|**Patch application + tests**|**Codex / repo execution tool**|Needs mechanical validation, not browser orchestration.|
|**Audit after produced artifacts exist**|**Extended thinking**|Needs close inspection and judgment; Agent Mode often turns validation into another “run.”|

---

## 2. Why your Agent Mode runs keep failing

### A. The value model is wrong for this task

OpenAI describes ChatGPT agent as useful for “complex online tasks” that involve reasoning, researching, and **taking actions**: navigating websites, working with files, connecting to apps, filling forms, editing spreadsheets, and running code. ([OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent "ChatGPT agent | OpenAI Help Center"))

Your task was mostly:

> read known files → reason about source fit → produce exact KB artifacts / diffs.

That is not primarily a browser/computer-use task. It is a **controlled writing + architecture + patch synthesis task**.

### B. Agent Mode executes the prompt shape literally

Your own diagnosis file says the failure was not laziness: the prompt told Agent Mode to optimize for governance/control artifacts instead of target production, so it created ledgers, manifests, scope contracts, and status reports instead of the five KB files.

The second audit scored the run **46/100** and found that although artifacts existed, patch integrity was **0/10**, validation rigor was **2/10**, and operational usefulness was only **5/10**.

### C. Even the improved prompt still kept Agent Mode in an over-controlled phase structure

The later `AgentPrompt_v3.md` was much better because it narrowed the work to one agent folder and five files, but it still used a three-phase Agent Mode run with source report, patch plan, and then diff. The execution output shows it spent substantial space on a source-and-target read report and a patch-planning table before final diff output.

That confirms the new learning: **even “production-first” Agent Mode prompts can slip back into process-first behavior if the run structure gives it too much phase machinery.**

---

## 3. Correct routing doctrine

### Use Agent Mode when the bottleneck is **external action**

Agent Mode should be used when the task requires:

- **Visual browser work:** websites, forms, UI navigation, dashboards.
    
- **Authenticated interaction:** logging into services, taking supervised actions.
    
- **Cross-app orchestration:** calendar + email + documents + web.
    
- **Spreadsheet or file operations through apps:** especially when UI state matters.
    
- **Scheduled or recurring operational tasks:** when the action itself is repeatable.
    
- **Tool-chain execution:** where the output depends on operating tools, not just thinking.
    

OpenAI also warns that Agent Mode can access sensitive data and perform actions, so it needs supervision and careful app enablement. ([OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent "ChatGPT agent | OpenAI Help Center"))

### Use Deep Research when the bottleneck is **source breadth and synthesis**

Deep Research fits when you need:

- multi-source research;
    
- citations and traceability;
    
- external/public web comparison;
    
- a structured report;
    
- source controls before research begins.
    

OpenAI says Deep Research is for multi-step, in-depth questions requiring aggregation and synthesis across sources, especially when you want explicit control over sources. ([OpenAI Help Center](https://help.openai.com/articles/10500283 "Deep research in ChatGPT | OpenAI Help Center"))

### Use extended thinking when the bottleneck is **judgment and artifact quality**

For your OpenClaw work, this should be the default for:

- prompt design;
    
- workflow design;
    
- KB architecture;
    
- doctrine updates;
    
- source digestion;
    
- repo-file reading and exact markdown writing;
    
- unified diff drafting;
    
- audit of existing artifacts;
    
- learning extraction.
    

This matches OpenAI’s own agentic prompting guidance: for agentic systems, you must control eagerness, define how much context to gather, and avoid unnecessary expansion; the guide explicitly advises “prefer acting over more searching” and says peak performance comes when separable tasks are broken across multiple turns. ([cookbook.openai.com](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide?_bhlid=27320832b2c4d44c80a3ec7a903a45cb3d6329e8 "GPT-5 prompting guide"))

---

## 4. Baseline rule for the KB

Add this as the core doctrine:

> **Route by bottleneck.**  
> Use Agent Mode when the bottleneck is external tool/browser/app action. Use Deep Research when the bottleneck is multi-source research synthesis. Use extended thinking when the bottleneck is reasoning, doctrine, prompt design, KB writing, exact markdown, or unified diffs. Use Codex/repo execution when the bottleneck is patch application and tests.

### OpenClaw-specific routing table

|Request|Route|
|---|---|
|“Create/update these KB files”|Extended thinking + repo/file access|
|“Design a prompt flow”|Extended thinking|
|“Audit these outputs and create doctrine”|Extended thinking|
|“Research official/current best practices online”|Deep Research or web-backed extended thinking|
|“Use a website/app to perform task X”|Agent Mode|
|“Fill forms / operate UI / collect data across browser tabs”|Agent Mode|
|“Apply this patch and run checks”|Codex / repo execution|
|“Do research, design, patch, validate, and apply”|Split across modes|

---

## 5. Updated anti-pattern name

The earlier anti-pattern “governance-first substitution” is still valid, but we need a broader one:

## **Mode-mismatch substitution**

**Definition:** The task is routed to a mode whose strengths do not match the bottleneck, causing the system to produce the wrong kind of output.

|Misroute|Failure|
|---|---|
|KB writing → Agent Mode|Produces reports/plans/control artifacts instead of exact files|
|Research synthesis → Agent Mode|Over-executes and drifts through tools|
|Browser task → extended thinking|Gives advice instead of acting|
|Patch/test task → normal chat only|Produces unverified diffs|
|Architecture task → autonomous agent run|Loses user steering and over-plans|

**Severity:** P1 when the user asked for a concrete artifact and the run returns only meta-work.

---

## 6. Practical rule going forward

For your current OpenClaw/KBOps work:

1. **Do not use Agent Mode for prompt design, workflow design, or KB synthesis by default.**
    
2. **Use extended thinking for source digestion and artifact creation.**
    
3. **Use Agent Mode only when a browser/app/website/spreadsheet action is actually required.**
    
4. **Use Deep Research only when the target is a research report, not repo mutation.**
    
5. **Use Codex/repo tooling when patches must be applied and checked.**
    

The next update to your playbook should replace “Agent Mode for complex tasks” with:

> **Agent Mode for complex tool actions. Extended thinking for complex reasoning. Deep Research for complex source synthesis. Codex/repo tools for complex patch execution.**