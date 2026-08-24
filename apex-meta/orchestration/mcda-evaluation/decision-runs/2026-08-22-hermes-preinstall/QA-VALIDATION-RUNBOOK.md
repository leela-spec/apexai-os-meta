# Hermes Pre-Install Realization & Decision Runbook

Status: **READY FOR INTERACTIVE Q&A / NO INSTALLATION**  
Date: 2026-08-22  
Primary candidate: Hermes Agent  
Direct challenger: OpenClaw  
Decision owner: Human CEO

## 0. Purpose

This runbook is for a separate chat whose job is to **prove or falsify the Hermes-first architecture before anything is installed or reorganized**.

The chat is not allowed to invent a better architecture. It must:

1. read the current Master of Arts scope and decision state;
2. verify all load-bearing claims from current official upstream sources;
3. walk the operator through the actual component interactions in plain language;
4. simulate real Master of Arts user stories step by step;
5. classify every step as deterministic, AI-semantic, or hybrid;
6. identify exact prompt/context/tool inputs and exact outputs;
7. expose token/context costs and data egress;
8. prove how project knowledge and project management would work using native Hermes mechanisms;
9. prove how BMAD/Agent Skills enter the same runtime without custom middleware;
10. prove what a web subscription AI can and cannot do with the same repository files;
11. compare OpenClaw only where Hermes has a demonstrated gap;
12. end with an explicit install/no-install decision packet.

No implementation changes are allowed during this run.

---

## 1. Operating law for the validating AI

### DO

- use current official documentation/repositories for load-bearing claims;
- distinguish verified fact from inference from unresolved question;
- show the actual call path between components;
- use the real MasterOfArts repository/project folders as examples;
- prefer native features and official integrations;
- quantify manual steps, token/context burden and duplicated state;
- stop at operator decisions instead of silently selecting consequential architecture;
- maintain the machine-readable `state.yaml` after each phase if repository writing is authorized.

### DO NOT

- install Hermes, OpenClaw, QMD, BMAD or any other component;
- reorganize project folders;
- create a custom knowledge schema;
- create a custom RAG layer;
- write custom orchestration code;
- add a second task database because it seems convenient;
- synchronize Hermes/OpenClaw/Claude/ChatGPT memories;
- assume that an online AI can execute a repo skill merely because it can read the file;
- describe any step as "the agent knows" without identifying the input path;
- recommend a component without explaining maker, install method, local/remote behavior, cost/license, data egress, input and output.

### FAILURE DEFAULT

If a requirement can only be satisfied by inventing a subsystem, mark that requirement `FAIL_CUSTOM_REQUIRED` and test the challenger instead.

---

## 2. Read order

Read these repository sources first, in order:

1. `Orchestration/03-SCOPE-LOCK.md`
2. `Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md`
3. `Orchestration/09-PRIMARY-ORCHESTRATION-SELECTION-HANDOVER.md`
4. `Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-001-provisional-hermes-stack.md`
5. `Orchestration/02-PILOT-PROTOCOL.md`
6. `Orchestration/mcda-state.yaml`
7. current project folders needed for the user stories only

Do not read historical OpenClaw custom architecture as authority. Use it only as failure/history evidence if needed.

Then verify current upstream facts from official sources. Minimum source set:

- Hermes context files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Hermes Curator: https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
- Hermes providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Hermes QMD skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- Hermes platform support: https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
- BMAD platform targets: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml

For OpenClaw challenger claims, use only current official OpenClaw docs/repository.

---

## 3. Interaction style — this is an operator walkthrough

Do not deliver one giant report before interacting.

For each phase:

1. explain what is being tested in plain language;
2. show the current verified facts in one compact matrix;
3. identify remaining unknowns;
4. ask the operator only the decisions that genuinely affect the next phase;
5. record the decision;
6. proceed.

Use `CONFIRMED`, `REJECTED`, `OPEN`, `FAIL_NATIVE`, `FAIL_CUSTOM_REQUIRED` consistently.

Do not ask the operator to decide technical questions that official evidence can answer.

---

# PHASE A — Freeze the actual candidate architecture

## A1. Reconstruct the current Hermes proposal

Show this exact ownership model and verify each connection:

```text
CEO
 -> Hermes
    -> Kanban (durable work state)
    -> specialist profile + skill
       -> BMAD / other installed Agent Skills
    -> selected AI provider/model
    -> project workdir
       -> project context files
       -> project source/artifact files
       -> optional QMD retrieval only if needed
    -> review/request-changes
    -> durable output/task state
    -> bounded Hermes learning
```

For each edge, fill:

| From | To | Mechanism | Native/official/config/custom | Network/API | Persistent state | Verified source |
|---|---|---|---|---|---|---|

If any edge is `custom`, pause and test whether the architecture should be rejected before continuing.

## A2. Explain every component in plain operational terms

Mandatory card:

```text
NAME:
MAKER:
WHAT IT IS:
WHY IT EXISTS IN THIS STACK:
MANDATORY OR OPTIONAL:
HOW INSTALLED:
WHAT IT READS:
WHAT IT WRITES:
LOCAL OR REMOTE:
NETWORK/API REQUIRED:
DATA SENT OUTSIDE MACHINE:
PRICE/BILLING PATH:
LICENSE:
WHAT BREAKS IF REMOVED:
OFFICIAL SOURCE:
```

Required cards:

- Hermes Agent
- Hermes Kanban
- Hermes project context / `AGENTS.md`
- Hermes memory
- Hermes Curator
- Agent Skills
- BMAD
- QMD
- MCP **only as Hermes <-> QMD in this stack**
- selected model/provider paths
- OpenClaw challenger

Do not mention Docling unless a specific source file format creates a real blocker.

### Operator gate A

Ask:

> Does this component map now describe the system you think we are evaluating, or is there still a component whose role is unclear?

Do not proceed until answered.

---

# PHASE B — Native Master of Arts project and knowledge model

This phase answers the central unresolved question:

> **How do existing MoA projects become understandable, isolated working contexts for Hermes without creating our own KB platform?**

## B1. Inspect the real repository, not an imagined clean structure

Sample at least three materially different domains, for example:

- one workshop/method domain;
- one business/operations domain;
- one research/content or IPOS/Lika domain.

For each record:

```text
PROJECT_PATH:
CURRENT_CONTENT_TYPES:
CURRENT_ORIENTATION_FILES:
CURRENT_STATUS/PM_FILES:
CURRENT_DUPLICATION_OR_NOISE:
WHAT_HERMES_CAN_READ_NATIVELY:
WHAT_HERMES_CANNOT_USE_NATIVELY:
```

Do **not** reorganize anything.

## B2. Test the native context hierarchy on paper

Hermes officially supports root-to-working-directory `AGENTS.md` context plus progressive nested discovery.

Use a concrete simulation such as:

```text
MasterOfArts/AGENTS.md
        ↓
Workshops/AGENTS.md
        ↓
Workshops/Awakenings/AGENTS.md
        ↓
Workshops/Awakenings/2026-Munich/AGENTS.md   (only if needed)
```

The validating AI must answer:

1. Which levels are automatically loaded when Hermes starts in the micro-project directory?
2. Which nested context appears only when the agent navigates there?
3. What is the token cost of automatic context?
4. Which raw files are not automatically loaded?
5. How does Hermes find them using native file/search tools?
6. At what measured corpus size/complexity does this become inefficient enough to justify QMD?

## B3. Determine the minimum project-local knowledge package

Do not design an ontology. Identify the **minimum information Hermes requires** for one project to be operable.

Test whether this can be satisfied by existing upstream-native concepts only:

- one concise project context file (`AGENTS.md` or Hermes-native equivalent);
- current project brief/status/decision artifact if one already exists;
- existing project sources/files;
- links/paths to authoritative outputs;
- optional nested context only where scope genuinely changes.

For each proposed file, require:

```text
CONSUMER: which upstream runtime/tool reads it?
VALUE: what failure occurs without it?
NATIVE_DISCOVERY: yes/no
DUPLICATES_EXISTING_TRUTH: yes/no
ALWAYS_LOADED_OR_ON_DEMAND:
TOKEN_COST:
```

If a proposed field/file has no named consumer or no measurable value, remove it.

## B4. Project-management mapping

Simulate native Hermes structures against:

- Macro = Master of Arts organization/portfolio;
- Meso = project/program/family;
- Micro = concrete delivery project/task flow.

For each level show whether it maps to:

- board;
- parent/child task/dependency;
- project workdir;
- profile/assignee;
- comments/attachments;
- review state;
- something not natively represented.

Do not add GitHub Projects unless Hermes fails a required management behavior.

### Operator gate B

Present exactly three outcomes:

1. `HERMES_NATIVE_SUFFICIENT`
2. `HERMES_NATIVE_PLUS_OFFICIAL_QMD_SUFFICIENT`
3. `HERMES_REQUIRES_CUSTOM_KB_OR_SECOND_PM_SYSTEM` -> **candidate failure condition**

Ask the operator to confirm the interpretation before moving on.

---

# PHASE C — Shared specialist + BMAD simulation

## C1. Verify BMAD installation path without installing

Confirm from current BMAD upstream configuration that Hermes is an explicit target and that project installation writes BMAD skills under `.agents/skills/`.

Then verify Hermes project-skill discovery for that same directory.

Result must be one of:

- `UPSTREAM_TO_UPSTREAM_CONFIRMED`
- `PATH_COMPATIBLE_BUT_EXECUTION_UNPROVEN`
- `CUSTOM_ADAPTER_REQUIRED` -> fail

## C2. Simulate one shared Marketing Executive across projects

Use the same specialist definition/skills in two different project workdirs.

### Scenario 1

`Marketing Executive -> launch one Awakenings workshop`

### Scenario 2

`Marketing Executive -> market a different MoA offer/project`

For each step use:

| Step | Exact input | What gets automatically loaded | On-demand retrieval | Skill loaded | AI or deterministic | Token driver | Output | Persistent state | Native? |
|---|---|---|---|---|---|---|---|---|---|

Pass only if:

- specialist definition is not duplicated per project;
- project context differs correctly;
- shared skills remain the same;
- no unrelated project knowledge is automatically injected;
- task/review state remains durable;
- the operator does not manually paste context between roles.

## C3. BMAD user stories

At minimum simulate:

- BMAD deep research/recon style workflow for a MoA research question;
- BMAD review for a non-code artifact;
- one creative/strategy workflow if verified upstream.

For each, distinguish:

- BMAD procedure text loaded into context;
- Hermes runtime/tool calls;
- model reasoning;
- resulting files;
- state stored in Hermes vs project repo;
- whether another Agent-Skills client could consume the same skill files.

### Operator gate C

Ask:

> Does the shared-specialist model now behave as intended, or does it still require one agent copy per project / manual context handoff?

---

# PHASE D — User-story simulations before install

Run the same simulations for Hermes first. Use OpenClaw only after Hermes results are recorded.

## US-1 — Research -> knowledge -> workshop

### Operator prompt

> Research one bounded Master of Arts topic using existing project knowledge plus fresh sources, produce a decision-ready synthesis, have a separate reviewer challenge it, and convert the accepted result into a workshop skeleton without losing provenance.

### Required flow

```text
prompt
 -> find current project/board
 -> retrieve existing project context
 -> activate research workflow/skill
 -> perform fresh research where required
 -> persist research artifact
 -> reviewer receives artifact/evidence
 -> review/change loop
 -> CEO gate
 -> workshop workflow receives accepted synthesis
 -> final workshop skeleton
 -> proposed reusable learning
```

The simulation must expose every input/output and whether it is D/AI/H.

## US-2 — Workshop -> marketing launch

### Operator prompt

> Take one approved workshop and create a launch package: landing-page copy, channel plan, short-form posts and launch tasks, while respecting the workshop's local knowledge and Master of Arts public/private rules.

Pass only if one shared marketing capability can act on the workshop without the operator re-explaining the project.

## US-3 — Weekly CEO operating cycle

### Operator prompt

> Review current work across at least three heterogeneous MoA areas, identify blocked/stale/dependent work, continue routine work where authorized, and surface only consequential decisions to the CEO.

Pass only if the system can answer from durable state:

- what matters now;
- what is blocked;
- what changed;
- who acts next;
- what needs CEO decision;
- how to resume after interruption.

## US-4 — Failure and recovery

Paper-simulate and later pilot:

- worker session dies;
- model quota/auth fails;
- reviewer rejects draft;
- project file changes during work;
- parent task has unfinished children.

For every case show deterministic recovery state and any AI reasoning required.

## US-5 — Learning after successful work

Example:

> The workshop launch reveals a repeatable marketing pattern that should help the next workshop.

Trace four possible destinations separately:

1. temporary session context;
2. Hermes profile memory;
3. reusable skill/procedure;
4. project factual knowledge.

The system fails if those categories are silently merged.

---

# PHASE E — QMD decision, not QMD assumption

QMD is not installed by default.

## E1. Native-search control

Simulate one retrieval task using only:

- project context files;
- `read_file`/file listing/search tools;
- direct known paths.

Record expected file reads and approximate prompt/context volume.

## E2. QMD-assisted version

Use Hermes' official documented integration on paper:

```text
Hermes
 -> native MCP client
 -> local QMD process/server
 -> local search index
 -> ranked matching passages/files
 -> Hermes receives only selected results
```

Classify:

- index build/update = deterministic/local tooling;
- keyword/vector retrieval = deterministic/local search/model computation;
- semantic synthesis after retrieval = AI reasoning;
- cloud token spend for QMD itself = none in documented local mode;
- context tokens = only returned passages loaded into the reasoning model.

## E3. Platform gate

Official Hermes QMD skill declares macOS/Linux. Because the target operator uses Windows, verify **before installation** whether the intended Hermes environment is native Windows or WSL2 and whether QMD is supported there without unsupported hacks.

Possible outcomes:

- `QMD_NOT_NEEDED`
- `QMD_OFFICIAL_PATH_SUPPORTED`
- `QMD_VALUE_HIGH_BUT_PLATFORM_BLOCKED`
- `QMD_REQUIRES_CUSTOM_WORK` -> do not adopt

---

# PHASE F — Web/subscription AI interoperability

This phase must separate four different questions that are often conflated.

## F1. Can the web AI read repository files?

Test per actual client/connector. Record `yes/no`, permission model and whether private repo access is supported.

## F2. Can the web AI read a `SKILL.md` file and follow it as ordinary instructions?

This is different from native skill installation. Test with one harmless upstream skill and record manual prompting required.

## F3. Does the web AI natively discover/activate repo-local Agent Skills?

Do not assume. Require official client evidence or an observed test.

## F4. Can the web AI operate Hermes/QMD/local tools?

A web AI with GitHub access normally cannot be assumed to control software running on the operator's machine. Only count this if an official connector/remote execution path exists and is explicitly accepted.

### Web-AI output matrix

| Client | Read repo | Write repo | Read project context | Follow SKILL as file | Native skill activation | Call Hermes | Call QMD | Extra API/billing | Verdict |
|---|---|---|---|---|---|---|---|---|---|

The goal is **shared durable files where possible**, not pretending every runtime has identical execution capabilities.

---

# PHASE G — Token, cost, privacy and determinism audit

For every component and every user story calculate qualitatively first, quantitatively where evidence permits:

| Item | Always in prompt? | Model tokens? | Local computation? | External data egress? | Persistent? | Deterministic? |
|---|---|---|---|---|---|---|
| Root context | | | | | | |
| Project context | | | | | | |
| Nested context | | | | | | |
| Skill index | | | | | | |
| Full skill | | | | | | |
| QMD query | | | | | | |
| Retrieved passages | | | | | | |
| Kanban state operation | | | | | | |
| Model synthesis | | | | | | |
| Reviewer pass | | | | | | |
| Memory injection | | | | | | |

Explicitly distinguish **local compute cost** from **cloud inference token/quota cost**.

For each provider record:

- authentication method;
- billing/quota path;
- what data leaves the machine;
- whether private MoA content is transmitted;
- whether use can be routed to local models;
- unresolved plan semantics.

---

# PHASE H — OpenClaw challenger only on decision-changing gaps

Do not rerun broad landscape research.

Take each Hermes result marked:

- `FAIL_NATIVE`;
- `FAIL_CUSTOM_REQUIRED`;
- `HIGH_FRICTION`;
- `HIGH_TOKEN_WASTE`;
- `POOR_KNOWLEDGE_RETRIEVAL`;
- `POOR_MACRO_MESO_MICRO_CONTROL`.

For only those requirements, test OpenClaw's current native implementation using the same input/output table and the same user stories.

OpenClaw wins only if it materially closes a decision-changing Hermes gap **without** requiring a second canonical PM system, unsafe/untrusted marketplace dependency, or custom synchronization.

---

# PHASE I — Final Q&A decision game

Present one question at a time.

## Q1 — Primary control plane

Which candidate passed the actual macro/meso/micro and recovery simulations with less custom glue?

Options:
- Hermes
- OpenClaw
- neither

## Q2 — Knowledge handling

Which verified arrangement is sufficient?

Options:
- native project context + file tools
- native project context + official QMD
- neither -> candidate fails unless challenger solves natively

## Q3 — Skills

Did BMAD/approved Agent Skills work through an upstream-supported installation path with no custom middleware?

Options:
- yes
- partially
- no

## Q4 — Shared specialists

Can one specialist operate across multiple projects with correct scoped context and no duplicated role definition?

Options:
- yes
- partial/high-friction
- no

## Q5 — Web AI

Is repo-file access sufficient for useful bounded subscription-AI work even when local Hermes/QMD execution is unavailable?

Options:
- yes
- useful but limited
- no

## Q6 — Learning

Is Hermes' native memory/skills/Curator split sufficient without custom cross-runtime synchronization?

Options:
- yes
- needs bounded governance/config only
- no/custom system required

## Q7 — Complexity

Does the selected stack remain at least ~90% upstream/existing?

Options:
- yes
- no

## Q8 — Installation authorization

Only after all previous decisions:

- `APPROVE_INSTALL_HERMES`
- `APPROVE_INSTALL_OPENCLAW`
- `RESEARCH_ONE_BLOCKER`
- `REJECT_CURRENT_FINALISTS`

Do not infer approval from conversational agreement on individual components.

---

# PHASE J — Required final deliverable before any installation

The validating chat must produce exactly these sections:

1. **Decision summary** — winner/challenger/why.
2. **Verified end-to-end flowchart** — no hypothetical edges.
3. **Component interaction matrix** — protocol/API/local/network/data egress/custom work.
4. **Knowledge/project-management model** — actual native mapping of macro/meso/micro.
5. **User-story simulation results** — pass/fail with artifacts/state.
6. **Deterministic vs AI execution matrix**.
7. **Token/context/cost/privacy matrix**.
8. **Shared specialist/BMAD portability result**.
9. **Web subscription AI capability result**.
10. **Unresolved blockers** — only decision-changing unknowns.
11. **Installation blueprint** — official commands/config only, but DO NOT EXECUTE.
12. **Rollback/uninstall path** — official mechanisms only.
13. **Exact repo changes proposed after approval** — minimal list.
14. **CEO decision** — one explicit option from Q8.

---

## Acceptance criteria for this run itself

The run is successful only if the operator can answer all of the following in plain language:

- What is the one primary system?
- Where does project/task state live?
- Where do my existing project files live?
- How does Hermes know which project it is in?
- What gets automatically loaded and what is searched on demand?
- What exactly would QMD do, and is it required?
- What exactly does MCP connect in our chosen setup?
- Where do BMAD skills live and how does Hermes see them?
- Can the same specialist work on two projects without duplication?
- What does Hermes learn automatically and where does that learning live?
- What remains available to a web subscription AI through the repo?
- Which steps are deterministic and which call an AI model?
- Which steps consume cloud inference quota/tokens?
- What information leaves the machine?
- What breaks after a restart or interrupted task?
- Which parts are existing upstream features and which parts would be ours?

If any answer still depends on "we would build a mechanism for that," the architecture has not passed.
