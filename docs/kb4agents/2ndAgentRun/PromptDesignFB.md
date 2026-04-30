# Diagnosis: why the Agent Mode runs failed

You are right. The failure is not “the agent was lazy.” The core failure is that the prompt design **told Agent Mode to optimize for governance/control artifacts instead of target production**, then treated that as if it were a production run.

The prompt did not behave like: “read one agent’s ranked sources and produce five revised KB files/diffs.”

It behaved like: “run a control/audit/source-gate factory before any agent repair.”

That is why the output drifted into ledgers, scope contracts, manifests, acceptance-test definitions, and status reports.

---

## 1. Official OpenAI findings that matter here

### 1.1 Agent Mode is designed to execute a described task, not infer your hidden intended workflow

OpenAI’s help page says ChatGPT agent begins executing after you describe the task and pauses only when clarification or confirmation is needed; it can use a browser, code interpreter, apps/connectors, and terminal, and tasks commonly take 5–30 minutes depending on complexity. ([OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agen?utm_source=chatgpt.com "ChatGPT agent | OpenAI Help Center"))

**Impact for your runs:**  
If the prompt says “RUN_BATCH: 0_CONTROL” and lists control artifacts as required output, Agent Mode will execute that. It will not infer: “Actually the user wants me to patch one agent’s five files.”

### 1.2 Agent Mode is collaborative, but it does not automatically become iterative unless instructed to stop

OpenAI describes ChatGPT agent as interruptible and steerable during work, and notes it may ask for details when needed, but it still executes the task from start to finish unless the prompt requires staged stopping. ([OpenAI](https://openai.com/index/introducing-chatgpt-agent/?utm_source=chatgpt.com "Introducing ChatGPT agent: bridging research and action | OpenAI"))

**Impact for your runs:**  
Your prompt described batches, but did not enforce: “Stop after Phase 1 and return; wait for user approval before Phase 2.” So it ran through in one go. That is expected behavior.

### 1.3 Official prompting guidance favors clear, specific end goals and constraints

OpenAI’s ChatGPT prompt guidance emphasizes being clear and specific, giving enough context, and iterating based on the output. ([OpenAI Help Center](https://help.openai.com/en/articles/10032626-creating-a-gpt?utm_source=chatgpt.com "Prompt engineering best practices for ChatGPT | OpenAI Help Center")) OpenAI’s API prompt-engineering guidance also says GPT models benefit from precise instructions that explicitly provide the logic and data required to complete the task. ([platform.openai.com](https://platform.openai.com/docs/guides/prompt-engineering/strategies-to-improve-reliability?utm_source=chatgpt.com "Prompt engineering - OpenAI API"))

**Impact for your runs:**  
The prompt was specific, but about the wrong thing. It specified control files, gates, ledgers, and manifests far more strongly than the actual deliverable: “patch these five agent KB files.”

### 1.4 For agentic workflows, OpenAI recommends controlling exploration and stopping conditions

OpenAI’s GPT-5 prompting guide says to define clear criteria for how the model should explore the problem space to reduce tangential tool calling and latency. It also says strong agentic prompts should define stop conditions and when the model should hand back to the user. ([cookbook.openai.com](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide?_bhlid=27320832b2c4d44c80a3ec7a903a45cb3d6329e8&utm_source=chatgpt.com "GPT-5 prompting guide"))

**Impact for your runs:**  
Your prompts had many stop conditions, but they were mostly **risk-stop conditions**, not **production-completion conditions**. The agent learned what to avoid and what to audit, but not the exact production target it had to finish.

### 1.5 OpenAI explicitly notes complex agentic tasks perform better when separable tasks are broken into separate turns

The GPT-5 prompting guide says performance peaks when distinct, separable tasks are broken across multiple agent turns, one turn for each task. ([cookbook.openai.com](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide?_bhlid=27320832b2c4d44c80a3ec7a903a45cb3d6329e8&utm_source=chatgpt.com "GPT-5 prompting guide"))

**Impact for your runs:**  
Your real work unit should have been:

> One agent folder → five files → one unified diff → one validation result.

Instead, the prompt still bundled source recovery, manifests, group artifacts, metadata audits, and final verdict correction into one run.

---

## 2. What went wrong in your two failed runs

## Failure A — The prompt selected the wrong mission

Your uploaded v3 prompt explicitly sets:

```text
RUN_BATCH: 0_CONTROL
RUN_MODE: PATCH_ONLY
```

and defines the mission as repairing the Special Ops KB package through source-gated, batch-limited, patch-only process. It then requires files like `01_BATCH_SCOPE_CONTRACT.md`, `02_SOURCE_ACCESS_LEDGER.md`, `03_SOURCE_CLAIM_CACHE.md`, `04_CHANGE_MANIFEST.md`, and `05_VALIDATION_REPORT.md` before or around the actual patching.

That means the agent was not pointed at:

```text
agents/information_design/
BEST_PRACTICES.md
MISTAKES_FAILURES.md
LEARNING.md
AGENT_CARD.md
ESSENCE.md
```

It was pointed at control-batch infrastructure.

**Root cause:** prompt-objective mismatch.

**Risk:** Very high. It guarantees the agent spends most of its run on pre-analysis.

---

## Failure B — “0_CONTROL” became a bureaucracy generator

The v3 prompt’s `0_CONTROL` batch says the goal is system-level weakness before agent content repair. It includes source-access ledger, source repair map, control manifest corrections, group-level improvement surfaces, acceptance tests, metadata schema audit across all 35 files, and final verdict correction.

That is not wrong as an audit mission. It is wrong as a production mission.

**Your intended task:**  
Read specific agent sources and patch the five KB files.

**Prompted task:**  
Prove, ledger, manifest, test, and audit the whole control layer.

**Impact:** The agent did what the prompt emphasized, not what you actually wanted.

---

## Failure C — The hard source gate blocked production

The prompt says not to produce content patches if a required primary source is missing; instead, mark affected files blocked and create no patch except manifest/audit status corrections.

That makes sense for high-risk governance. But for your intended work, it creates a common failure mode:

1. Agent tries to recover source.
    
2. Source recovery is imperfect.
    
3. Agent marks source missing.
    
4. Agent blocks content work.
    
5. Output becomes a ledger/status package instead of five revised files.
    

**Impact:** The source gate became the product.

---

## Failure D — The prompt made validation outputs mandatory but not executable enough

The prompt required acceptance tests and `git apply --check`. But the produced run reported that acceptance tests were not run and git apply was not checked. That is exactly the kind of failure OpenAI’s agentic prompting guidance warns about indirectly: the model needs explicit completion criteria, tool-use criteria, and stop conditions tied to task completion, not just written checklist definitions. ([cookbook.openai.com](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide?_bhlid=27320832b2c4d44c80a3ec7a903a45cb3d6329e8&utm_source=chatgpt.com "GPT-5 prompting guide"))

**Impact:** The agent created a validation-looking surface instead of doing validation.

---

## Failure E — The prompt over-weighted “do not” instructions

The v3 prompt contains many “do not” constraints: no broad repo exploration, no full rewrite, no source expansion, no final truth, no evidence leakage, no continuation after hard stop, no completeness theater, no opaque citations, and so on. These are individually valid. But the positive production instruction was weaker than the negative safety/control framework.

Official OpenAI guidance says GPT models benefit from precise instructions that explicitly provide the logic and data required to complete the task. ([platform.openai.com](https://platform.openai.com/docs/guides/prompt-engineering/strategies-to-improve-reliability?utm_source=chatgpt.com "Prompt engineering - OpenAI API")) Here, the logic was mostly “how to avoid bad output,” not “how to produce the desired five-file diff.”

**Impact:** The agent avoided risk by producing control artifacts.

---

## Failure F — “Iteration” was described conceptually, not enforced operationally

You wanted iterative production. But Agent Mode will generally keep going until the described task is done; OpenAI says the user can interrupt or steer it during the task, and the agent may ask when needed. ([OpenAI](https://openai.com/index/introducing-chatgpt-agent/?utm_source=chatgpt.com "Introducing ChatGPT agent: bridging research and action | OpenAI"))

To force real iteration, the prompt must say:

```text
After Phase 1, stop and return only the Phase 1 report.
Do not proceed to Phase 2 until the user replies CONTINUE.
```

Without that, “iterative” is just a style word.

---

# 3. The actual design correction

## The next prompt should not be another control prompt

Your next Agent Mode prompt should be a **single-agent patch production prompt**.

It should not say:

- “source-gated improvement factory”
    
- “0_CONTROL”
    
- “group-level improvement surfaces”
    
- “metadata audit across all 35 files”
    
- “create acceptance tests”
    
- “create source claim cache”
    
- “create batch scope contract”
    

Those are hygiene tools. They are not the production target.

---

## 4. Correct target architecture

### The right run unit

|Unit|Value|
|---|---|
|**One run**|One agent folder only|
|**Target**|Exactly five existing KB files|
|**Output**|One unified diff plus compact validation|
|**Allowed sources**|The ranked sources for that agent from the index|
|**Forbidden output**|New governance/control files unless explicitly requested|
|**Stop point**|After one agent’s five-file diff is produced and checked|

### The right production order

1. Read the source index only enough to identify the selected agent’s sources.
    
2. Read the selected agent’s primary/supporting/evidence files.
    
3. Read the five existing target KB files.
    
4. Patch the five files in required order:
    
    - `BEST_PRACTICES.md`
        
    - `MISTAKES_FAILURES.md`
        
    - `LEARNING.md`
        
    - `AGENT_CARD.md`
        
    - `ESSENCE.md`
        
5. Generate one valid unified diff.
    
6. Run `git apply --check`.
    
7. Return the patch and validation result.
    

That is it.

---

# 5. Copy-ready Agent Mode prompt pattern that should replace the failed one

```text
/agent

Use this prompt as the controlling instruction.

Repository: leela-spec/MasterOfArts

MISSION:
Produce a review-ready unified diff for exactly one existing Special Ops agent KB folder.

SELECTED_AGENT:
information_design

TARGET_FOLDER:
docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/agents/information_design/

TARGET_FILES:
1. BEST_PRACTICES.md
2. MISTAKES_FAILURES.md
3. LEARNING.md
4. AGENT_CARD.md
5. ESSENCE.md

SOURCE_INDEX:
SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

PRIMARY OBJECTIVE:
Read the source index, read only the indexed sources assigned to SELECTED_AGENT, read the five existing target files, and produce one valid unified diff that improves those five files.

NON-GOALS:
- Do not create control artifacts.
- Do not create batch scope contracts.
- Do not create source claim caches.
- Do not create acceptance-test files.
- Do not create group-level artifacts.
- Do not audit all 35 files.
- Do not repair other agents.
- Do not browse the web.
- Do not commit, open a PR, or apply changes.

ITERATION RULE:
This run has exactly three phases.
After each phase, stop and return the required phase output.
Do not continue until the user replies CONTINUE.

PHASE 1 — SOURCE AND TARGET READ REPORT
Actions:
1. Read SPECIAL_OPS_KB_BASE_BUILD_INDEX.md.
2. Extract only the selected agent’s source list.
3. Read the selected agent’s indexed sources.
4. Read the five target files.

Return only:
- selected_agent
- sources_read
- target_files_read
- blockers
- proceed_recommendation

Stop after Phase 1.

PHASE 2 — PATCH PLAN
Actions:
1. For each target file, identify only the exact sections that need repair.
2. Do not draft full files.
3. Do not patch unrelated content.

Return only:
| File | Edit zones | Reason | Source basis | Risk |
|---|---|---|---|---|

Stop after Phase 2.

PHASE 3 — UNIFIED DIFF AND VALIDATION
Actions:
1. Generate one unified diff for the five target files.
2. Preserve untouched lines exactly.
3. Use valid hunk ranges.
4. Run git apply --check against the live repo state.
5. If git apply fails, fix the patch once and rerun.
6. Return final patch only if git apply passes.

Return only:
- ALL_CHANGES.patch
- git_apply_status
- files_changed
- files_not_changed
- blockers
- next_agent_recommendation

COMPLETION CRITERIA:
The task is complete only when a valid unified diff exists for the selected agent’s five files and git apply --check passes.

FAILURE RULE:
If a required primary source is missing, do not switch into control-batch mode.
Instead:
1. Patch only source-limit metadata and body caveats in the five target files.
2. Mark affected claims as blocked or provisional inside those five files.
3. Still produce a valid unified diff for the five target files if possible.
```

---

# 6. Why this prompt is materially different

|Old failed pattern|Replacement pattern|
|---|---|
|Batch = `0_CONTROL`|Batch = one concrete agent folder|
|Required output = ledgers/manifests/control files|Required output = five-file diff|
|“Iteration” implied|Explicit stop after each phase|
|Source gap blocks production entirely|Source gap becomes source-limit patch inside target files|
|All-35 metadata audit|Only selected agent’s five files|
|Creates new group artifacts|Explicitly forbidden|
|Validation checklist created|`git apply --check` must actually run|
|Governance-first|Work-product-first|

---

# 7. The hard truth

The previous prompts failed because they were **architecturally elegant but operationally mis-aimed**.

They encoded your fear of bad KB production more strongly than your desired output. So Agent Mode optimized for not being wrong rather than for producing the five files.

The fix is not “more best practices.” The fix is a narrower prompt with a brutally simple production contract:

> **One agent. Five files. One diff. Verified. Stop.**

Then repeat for the next agent.