This is a broad set of domains — let me structure it in two layers: a master capability matrix across all three surfaces, then deeper breakdowns for the domains that need real explaining (multi-agent orchestration, PPT-from-mixed-sources, M365, websites).

## Master Capability Matrix (1–100)

|Domain|Claude Chat|Claude Code|Cowork|Best tool|
|---|---|---|---|---|
|App development planning (architecture, specs)|75|90|65|Code|
|Actual app development (writing/running code)|40|95|55|Code|
|Project planning (roadmaps, milestones)|80|60|85|Chat/Cowork|
|Project management (tracking, updating tasks over time)|45|55|80|Cowork|
|Task management (day-to-day to-dos)|50|40|85|Cowork|
|Personal assistant (calendar, email, cross-tool)|35|20|90|Cowork|
|Multi-agent orchestration (you design the system)|20|90|45|Code|
|Multi-agent project management (agents run a project)|15|75|55|Code|
|Business plan writing|85|55|75|Chat|
|PowerPoint from many local + git sources|30|70*|85|Cowork (see below)|
|Business slide design/layout quality|70|40|85|Cowork|
|Microsoft 365 file understanding (SharePoint/OneDrive/Outlook)|75|10|75|Chat/Cowork (connector-based)|
|Writing emails (drafting)|90|20|85|Chat|
|Sending/managing emails directly|10|5|70**|Cowork (via M365/Gmail connector)|
|Building a website (static/simple)|70|95|75|Code|
|Website animations|55|90|60|Code|

*Code can produce a deck's content/structure but has no native pptx-rendering skill the way Chat/Cowork do — it would generate the file via the same underlying pptx skill mechanism, just without Cowork's file-orchestration layer. **Depends entirely on admin-enabled write tools; off by default in many orgs.

## Deep dive: Multi-agent orchestration & multi-agent project management

|Capability|Claude Chat|Claude Code|Cowork|
|---|---|---|---|
|Spawn specialist sub-agents you define|0|90|30|
|Agents communicate peer-to-peer|0|75 (agent teams)|10|
|Parallel task execution with dependency graphs|0|85|40|
|Persistent role definitions (reusable across sessions)|0|90|25|
|Runs unattended over days|0|40|85|
|Scheduling/recurrence|0|30 (DIY via SDK)|90|
|Setup effort required|—|High (CLAUDE.md, agent files, flags)|Low|

**Verdict:** if "multi-agent project management" means _you architecting a system of specialized agents that coordinate_, that's Claude Code territory — nothing else here has the primitives. If it means _"delegate this whole project and check in periodically,"_ Cowork's opacity becomes a feature, not a limitation.

## Deep dive: PowerPoint from files saved both locally and in git

|Step|Tool|Notes|
|---|---|---|
|1. Gather git-sourced content (docs, data, code comments, READMEs)|Claude Code (local)|Direct filesystem + git access, no connector needed|
|2. Gather locally-saved files not in git|Cowork (web/mobile, upload) or Cowork Desktop (if Pro)|Web Cowork needs manual upload; Desktop would read the folder directly|
|3. Synthesize/summarize combined material into slide content|Either|Chat is fine here too if you paste/upload everything manually|
|4. Generate the actual .pptx file|Cowork or Chat|Both use the same underlying pptx-generation skill; Cowork also offers post-generation editing via "Claude for PowerPoint"|
|5. Refine layout/design|Cowork or Chat|Neither is Claude Code's strength — this is a document/design skill, not a coding one|

**Practical path for your setup:** pull git content via Claude Code locally → hand the synthesized text/outline to Cowork (web) along with manually uploaded local files → have Cowork build and refine the deck. Don't expect one single surface to reach into both git and your local folder in one motion — that bridge doesn't exist yet.

## Deep dive: Microsoft 365 (SharePoint/OneDrive/Outlook/Teams)

|Capability|Available?|Conditions|
|---|---|---|
|Search/read SharePoint, OneDrive, Outlook, Teams|Yes — 85|Claude can search any SharePoint sites and shared drives you have permission to access, including team sites and document libraries. Requires a work Microsoft 365 account (Entra tenant) — personal Outlook/Hotmail accounts don't qualify.|
|Draft/send email, manage calendar, create/update OneDrive & SharePoint files|Conditional — 40|Only if your admin has enabled write tools; when they're not enabled, the integration is read-only.|
|Attach files to drafted/sent emails|No — 0|Attachments aren't currently supported in write tools — Claude can't send, forward, or draft emails with attachments.|
|Post to or manage Teams|No — 0|Claude cannot attach files to the drafts it creates and cannot send Teams messages.|
|Works the same across Chat/Code/Cowork|Chat & Cowork: yes. Code: no|This is a connector, not a filesystem — Claude Code has no access to it at all unless you build a custom MCP bridge yourself.|

Note: this connector is available on all plans including Free, but write actions specifically need an Entra admin to switch on — worth checking if that's realistic for your account type (personal/business).

## Deep dive: Website + animations

|Task|Best tool|Score|Why|
|---|---|---|---|
|Static site structure/HTML/CSS|Claude Code|90|Full file system, can scaffold a whole project, run a dev server, iterate|
|CSS/JS animations|Claude Code|90|Same reason — animations are just code, benefits from iteration loop|
|Quick single-page visual mockup|Chat (via artifacts)|80|Fast, no setup, good for prototyping a look before building it properly|
|Deploying/hosting|Claude Code|70|Can run build tools, git push to a host, but actual hosting still needs an external service|
|Ongoing content updates to a live site|Cowork (if connected to the right repo/CMS)|50|Weaker fit generally — better handled by Code unless the site's CMS has its own connector|

## One structural point worth internalizing across all of this

Notice the pattern: **Chat** is best when the output lives in the conversation or as a single generated file and doesn't need external systems. **Code** is best whenever the task is fundamentally about files-on-disk-plus-logic — repos, apps, orchestration you design. **Cowork** is best whenever the task spans multiple _external services_ (connectors) over _time_ (scheduling, persistence) without you needing to architect the internals.

Given your specific situation — repo-based work, Windows Home, wanting a "personal assistant + project manager + business deck generator" — a realistic three-way split would be: **Claude Code** for anything code/repo/orchestration-heavy, **Cowork (web)** for scheduling, M365, task/personal management, and slide generation, and **Chat** for drafting (emails, business plans, quick mockups) before handing the result to one of the other two for execution.