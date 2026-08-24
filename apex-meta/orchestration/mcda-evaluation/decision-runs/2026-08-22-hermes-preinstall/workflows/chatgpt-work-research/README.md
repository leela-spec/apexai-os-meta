# ChatGPT Work Research Program — Hermes Pre-Install Research

Status: **READY TO CONFIGURE / NO RESEARCH EXECUTED YET**  
Date: 2026-08-23  
Product target: **ChatGPT Work on web/browser subscription**  
Repository: `leela-spec/MasterOfArts`  
Branch: `main`

## 1. Purpose

Use the new **ChatGPT Work** experience to execute the seven Hermes pre-install research specifications at decision-grade, high level before the interactive realization run continues.

This is **not** a new orchestration architecture. It is a way to use an existing OpenAI workflow product to run the already-defined research work consistently.

The seven authoritative research specifications remain:

1. `research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md`
2. `research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md`
3. `research/R03-HERMES-QMD-REPO-INTEGRATION.md`
4. `research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md`
5. `research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md`
6. `research/R06-HERMES-CONTINUOUS-LEARNING.md`
7. `research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md`

## 2. Verified ChatGPT Work product model

Current official OpenAI documentation distinguishes the relevant pieces clearly:

| OpenAI feature | Role in this research program | Required? |
|---|---|---:|
| **ChatGPT Project** | Persistent container for related Work chats, project instructions, files and context | YES |
| **ChatGPT Work** | Long-running multi-step agent that researches/analyzes and produces finished deliverables | YES |
| **Plan mode** | Work gathers context and proposes a step-by-step approach for review before execution | YES where exposed |
| **GitHub plugin/app** | Reads the current private repository and writes approved result files; avoids stale uploaded copies | YES for this design |
| **Web/browser research** | Retrieves current official upstream documentation and repositories | YES |
| **Skills** | Reusable tested workflow instructions that Work can invoke automatically or explicitly | AFTER workflow proof |
| **Scheduled Tasks** | Recurring/triggered Work execution | NO for this one-time pre-install research program |
| **Codex** | Software-development environment | NO for the semantic research itself |

Official sources:

- ChatGPT Work overview: https://openai.com/chatgpt-work/
- ChatGPT Work and Codex: https://help.openai.com/en/articles/20001275
- Projects in ChatGPT: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- Skills in ChatGPT: https://help.openai.com/en/articles/20001066
- Using Skills: https://openai.com/academy/skills/
- Work workflow design guide: https://academy.openai.com/public/clubs/champions-ecqup/resources/chatgpt-work-reimagine-guide-for-team-activators-2026-07-08
- Work webinar resource guide: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/get-started-with-chatgpt-work-webinar-resource-guide-2026-08-03
- Plugins in ChatGPT and Codex: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex

## 3. Recommended research organization

Use **one ChatGPT Project** as the shared research workspace and **one separate Work thread per research track**.

```text
CHATGPT PROJECT: MoA — Hermes Pre-Install Research
|
+-- Project instructions
|   +-- evidence/source rules
|   +-- no-install / no-custom-system rules
|   +-- result/persistence rules
|
+-- Work thread R01 — Safety
+-- Work thread R02 — Macro/Meso/Micro project + knowledge
+-- Work thread R03 — Hermes/QMD/repo
+-- Work thread R04 — Project knowledge lifecycle
+-- Work thread R05 — Specialist agents + priming
+-- Work thread R06 — Continuous learning
+-- Work thread R07 — MarketingSkills integration
|
+-- Work review thread(s)
|   +-- check each result against its authoritative prompt and official sources
|
+-- Final Work synthesis thread
    +-- consumes only accepted R01-R07 results + current ADR/state
    +-- feeds the existing QA-VALIDATION-RUNBOOK-v2.md
```

### Why this structure

OpenAI Projects are explicitly intended to keep related chats, files and instructions together for repeated/evolving research. Work can start inside a Project and use that Project context. Separate Work threads keep each research question bounded while preserving the common operating rules.

The research task files remain in GitHub and are fetched live through the GitHub plugin. Do **not** upload duplicate copies unless plugin access fails; duplicated uploads can go stale.

## 4. Workflow per research track

Each R01-R07 run follows the same complete process:

```text
1. Open new Work thread inside the Project
2. Use Plan mode
3. Give Work the exact research-spec path
4. Work reads current ADR-002 + state.yaml + that research spec
5. Work identifies only repo files needed for the specific question
6. Work proposes research plan + authoritative source plan
7. Human reviews/approves the plan
8. Work researches current official web/repository sources
9. Work inspects the current MasterOfArts repo where the spec requires it
10. Work produces the full decision-grade result
11. Run evidence/coverage review
12. Human resolves consequential uncertainties
13. GitHub plugin writes the accepted result into the designated result path
14. Update track status; do not change architecture/installation state unless the operator approves it
```

Nothing in this program installs Hermes, QMD, BMAD or MarketingSkills.

## 5. Inputs and outputs

### Shared inputs

Read live from GitHub:

- `ADR-002-full-functional-hermes-target.md`
- `state.yaml`
- `Orchestration/03-SCOPE-LOCK.md`
- `Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md`
- `Orchestration/02-PILOT-PROTOCOL.md`

Then read only the current Rxx task file and repo areas it explicitly needs.

### External inputs

Use current public web sources, with priority:

1. official product documentation;
2. official repositories/source code/releases;
3. official package/catalog documentation;
4. first-party examples;
5. secondary sources only for unresolved operational experience, never as sole proof of a load-bearing capability.

### Result outputs

Write accepted results under:

`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/`

One result per research track. Do not overwrite the research prompt itself.

## 6. Research quality standard

Every load-bearing claim must be labelled mentally/explicitly as one of:

- `VERIFIED_OFFICIAL` — exact current official evidence;
- `SUPPORTED_INFERENCE` — evidence exists but mapping to MoA requires inference;
- `OPEN` — not yet established;
- `CONTRADICTED` — official evidence conflicts with an existing assumption.

For every system connection, identify:

`from | to | exact mechanism | local/remote | API/network | deterministic/AI | persistent state | data egress | existing/custom | source`

Do not write phrases such as “the agent will know,” “the systems talk,” or “the context is shared” without naming the actual mechanism.

## 7. Skill strategy — test first, then save the tested workflow

Do **not** invent a large research Skill before running the workflow.

OpenAI's current Work/Skills guidance recommends first performing and refining the workflow, then saving the version that actually works as a Skill. Skills are designed to preserve repeatable instructions, resources, evidence checks and output rules, not the one-off dataset/findings from a specific run.

After the first accepted research run, create these two reusable Skills through ChatGPT Work's built-in Skill creation flow:

### Skill A — `moa-official-source-research`

Preserve:

- official-source priority;
- repository-grounding procedure;
- claim status labels;
- connection/mechanism matrix;
- contradiction and staleness checks;
- exact output/evidence requirements.

Do **not** preserve the current Hermes conclusion or R01-specific findings.

### Skill B — `moa-research-evidence-review`

Create only after the review procedure has successfully caught/confirmed issues on at least one real result.

Preserve:

- coverage check against authoritative Rxx specification;
- source freshness and authority check;
- native/official/config/custom classification check;
- invented-connection check;
- contradiction/uncertainty check;
- PASS / REVISE / BLOCK verdict.

These Skills can then be used by later Work threads. OpenAI documents that installed Skills may be invoked automatically or explicitly and follow the Agent Skills open standard.

## 8. Capabilities that must be available in the Work Project

Before running R01, confirm:

- Work is available on the user's plan/surface;
- the Work thread is inside the correct ChatGPT Project;
- GitHub plugin access can read `leela-spec/MasterOfArts`;
- GitHub write actions require review/approval before persisting research outputs;
- web browsing/search is available;
- Work can enter Plan mode or, if that UI is not exposed on the current surface, can be instructed to propose a plan and wait before execution;
- no research Skill is treated as trusted until its actual instructions/resources are reviewed.

## 9. What this workflow deliberately does not add

- no new database;
- no QMD for ChatGPT Work research;
- no MCP server;
- no custom research agent framework;
- no custom scheduler;
- no duplicated copy of the MasterOfArts repository inside ChatGPT;
- no separate Work Project for every research question;
- no automated installation/change to the Hermes target stack.

The only new operating structure is an OpenAI-native **Project + Work threads + Plugins + later tested Skills** arrangement.

## 10. Next action

1. Create/open the ChatGPT Project `MoA — Hermes Pre-Install Research`.
2. Put the contents of `PROJECT-INSTRUCTIONS.md` into Project settings.
3. Confirm the GitHub plugin is available inside Work.
4. Start with R01 using `WORK-RESEARCH-LAUNCHERS.md`.
5. Do not create the reusable research Skill until the first real run has been accepted.
