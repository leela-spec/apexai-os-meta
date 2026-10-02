# Antigravity Launcher — CLI Reasoning -> Hermes Routing Bridge

```text
/teamwork-preview

Use DEVELOPMENT integrity mode.

Repository:
C:\GitDev\apexai-os-meta
Branch:
main

No earlier patch bundle from this chat has been applied.
Use only the current repository plus the newly patched authority files.

Read:

1. apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/SKILL.md
2. apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/references/lessons-learned.md
3. apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/references/prompt-patterns.md
4. apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/00-START-HERE.md
5. apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/04A-DOCKER-BACKGROUND-RUNTIME.md
6. apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/05A-CLI-REASONING-HERMES-ROUTING.md

Verify live Git HEAD/worktree first.

TARGET ARCHITECTURE:

Operator
-> heavy-reasoning CLI agent
-> Hermes OpenAI-compatible API on 127.0.0.1:8642
-> Hermes provider-backed routing/tool execution
-> real Hermes skills later
-> Firefly / Paperless / OpenProject

Do not create a second permanent application-control path.

IMPORTANT CONCEPT:
The CLI agent is upstream planner/reasoner.
It does NOT literally replace Hermes' model.
Hermes still needs a provider to route/load skills/run tools.
OpenRouter is being configured now for that Hermes routing/execution role.
The upstream CLI agent may use its own provider independently.

DOCKER:
Keep Docker Desktop Hyper-V background runtime.
Dashboard closed/not auto-opened.
Do not quit/stop Docker Desktop and claim its Linux engine remains running.
Do not migrate to a manual Linux VM.
Do not apply resource tuning.

PHASE A — background runtime:
- verify "Open Docker Dashboard when Docker Desktop starts" is disabled;
- Dashboard remains closed;
- `docker desktop status`;
- one `docker ps`;
- seven services healthy/running.

PHASE B — Hermes API bridge:
- ensure compose contains the official API server settings already authorized by the patch;
- generate a strong HERMES_API_SERVER_KEY locally if missing;
- store it only in ignored ki-basis/.env;
- never print it;
- recreate only Hermes if necessary;
- prove 127.0.0.1:8642 is loopback-only;
- wrong key must be rejected.

PHASE C — OpenRouter operator gate:
Prepare Hermes.
Then ask the operator for the smallest exact action:
- create/select OpenRouter key outside chat;
- run Hermes interactive provider setup inside ki-basis-hermes;
- enter the key there;
- select a current tool-capable routing/execution model;
- return only "provider configured", never the key.

Do not hard-code a model choice into Git.

PHASE D — machine bridge:
Implement/verify `ki-basis/scripts/invoke-hermes.ps1`.
It must:
- read HERMES_API_SERVER_KEY from ignored .env;
- call Hermes API;
- contain no app-specific business logic;
- fail closed;
- never print the key.

Use it for one non-sensitive test prompt.

PRIVACY:
Do not claim OpenRouter is private because a CLI agent reasons first.
If Hermes receives sensitive product output, Hermes' provider may see it.
Document a future Hermes privacy profile/provider as the extension point.
Do not implement local models now; operator reports prior attempts were not satisfactory.

SKILLS:
Do NOT build placeholder Firefly/Paperless/OpenProject skills.
Do NOT build ki-basis-control yet.
The operator will supply the real skill sets later.
Existing detailed M05 remains future integration reference.

INFRA VERIFICATION:
Re-run the existing stack verifier only as needed to prove no regression.
Do not create a second direct-product CLI-agent control framework.

LIFECYCLE:
With Dashboard closed, restart Docker Desktop through the supported background path.
Prove:
- seven services return;
- Hermes API bridge returns;
- valid bridge invocation works;
- isolation remains intact.

No push unless explicitly authorized by current operator instruction.
Commit only bounded changes from this phase.
STOP after the bridge phase.
```
