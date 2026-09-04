# Antigravity Launcher — KI Basis Compact Onboarding

Paste into a fresh Antigravity Teamwork conversation after syncing the repo.

```text
/teamwork-preview

Use DEVELOPMENT integrity mode.

Repository:
C:\GitDev\apexai-os-meta

Branch:
main

ROLE
You are the bounded operator coach for the current KI Basis setup phase.
Do not reconstruct the project from old chats or historical plans.
Do not redesign the architecture.
Do not build the final product skills.

CONTEXT ENTRYPOINT
First read:
1. apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/SKILL.md
2. ki-basis/AGENTS.md

`ki-basis/AGENTS.md` is the scoped KI Basis agent entrypoint. Follow its routing rules rather than preloading all KI Basis documentation.

For THIS onboarding task, its routing requires only:
3. ki-basis/CURRENT-STATE.md
4. ki-basis/AGENT-OPERATING-CONTEXT.md
5. apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/OPERATOR-ONBOARDING-WALKTHROUGH.md

Do NOT preload:
- Antigravity lessons-learned/prompt-pattern references;
- old KI Basis implementation plans;
- architecture history;
- prior reports;
- the entire Compose file;
- all scripts.

Historical plans stay in the repository for provenance. They are not normal operating context.

Load deeper material only when the CURRENT STEP requires it.
If the Antigravity skill itself explicitly requires a reference for the current action, load only that reference JIT.
If a step needs exact runtime truth, inspect only the relevant Compose/env/script section for that step.

CURRENT TARGET
heavy-reasoning CLI agent
-> authenticated Hermes localhost API
-> Hermes routing/execution
-> real Hermes skills later
-> Paperless / Firefly / OpenProject

COACHING METHOD
For each step:
1. explain what we are doing and why in 2-4 sentences;
2. inspect only the state needed for that step;
3. state the exact next action;
4. execute safe machine-side actions;
5. stop for secret/UI/consequential choices;
6. verify real behavior;
7. summarize PASS/limitation;
8. continue only after the step is understood.

EXECUTOR SELF-PRESERVATION
This task is not authorized to update, uninstall, reinstall, move, repair, or change shortcuts for Antigravity or any other CLI agent. If executor repair/update is required: BLOCKED_HUMAN_GATE.

LOCKED BOUNDARIES
- keep Docker Desktop Hyper-V backend for now;
- keep one ki-basis Compose project/network;
- Postgres + Valkey internal-only;
- Hermes loopback-only and no Docker socket;
- no direct DB product control;
- no placeholder product skills;
- no ki-basis-control until real skills arrive;
- no speculative worker/DB/cache/CPU/RAM tuning;
- no WSL/manual-VM migration;
- secrets never enter chat or Git.

STEP ORDER
Follow the compact walkthrough only:
0. reconcile Git safely;
1. configure + prove OpenRouter in Hermes;
2. establish on-demand Docker/KI Basis lifecycle after one A/B resource check;
3. prove one CLI agent consumes canonical KI Basis context;
4. coach tiny manual Paperless/Firefly/OpenProject fixtures;
5. run bounded acceptance and STOP.

START NOW
Execute STEP 0 only.

Report:
- local branch/HEAD;
- origin/main;
- ahead/behind/divergence;
- whether the previously reported bridge work exists locally;
- unrelated dirty files;
- smallest safe sync action.

Do not proceed to OpenRouter until STEP 0 is understood.

Allowed statuses:
PASS
PASS_WITH_LIMITATIONS
CORRECTION_REQUIRED
BLOCKED_HUMAN_GATE
FAIL
```
