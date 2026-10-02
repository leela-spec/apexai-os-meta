# OpenProject for Leela: research findings and adoption blueprint

**Recommendation: advance OpenProject to a bounded pilot as the proposed owner of operational project-management state—not as another tracker beside the existing one. Keep GitHub Projects as the principal fallback.**

OpenProject is a strong fit for the interaction you want: you express goals and make decisions; an AI orchestrator organizes and advances the work; you can inspect and change that work visually; coding agents produce changes in GitHub; verification determines what is actually complete.

However, two conditions materially affect the recommendation:

**First, native AI integration is not a free Community feature.** In OpenProject 17.8.0, the native MCP server requires an Enterprise Professional entitlement. Community remains usable through its REST API, but that is a different integration route and does not automatically provide the same browser-chat experience. ([OpenProject.org](https://www.openproject.org/community-edition/?utm_source=chatgpt.com "OpenProject Community Edition - Free and Open Source"))

**Second, OpenProject must replace selected operational ownership, not duplicate it.** The current repository remains authoritative until a separately approved migration changes that arrangement. The handover explicitly reopens this ownership question; it does not authorize a migration.

**Research basis:** repository snapshot `6e6c496db18048ea640dfa8365e4724856a12d39` on `master`, current official documentation, and selected upstream OpenProject 17.8.0 source. This was a read-only investigation: no installation, configuration, migration, repository changes, live OpenProject permission tests, or test-suite execution.

Below, **facts** describe retrieved evidence; **proposed** mechanisms describe the recommended future operating model.

---

## A. Executive answer

|Your question|Answer|
|---|---|
|**What is OpenProject?**|A persistent project-management application. Its central object, a **work package**, is a work record: a task, story-delivery item, research assignment, decision request, or milestone. It is not the AI itself.|
|**Where would it live?**|Preferably on a managed OpenProject service for the pilot, or on a persistent server under your control. Your browser displays it; its server and database retain the work.|
|**How would I use it?**|Mostly through normal conversation with your AI, plus a few visual views: “Needs my decision,” “Ready,” “In progress,” “Blocked,” and “Milestones.” You can also change priority, pause work, or reopen an item directly.|
|**How would the AI use it?**|Through MCP or the REST API: retrieve relevant work, create proposals, decompose approved work, record dependencies, claim assignments, attach evidence, and update permitted statuses.|
|**What stays in GitHub?**|Code, pull requests, reviews, tests, CI results, accepted repository decisions, semantic contracts, and rule-to-artifact evidence. OpenProject links to these rather than becoming a second product specification.|
|**What decisions remain mine?**|Product intent, consequential scope and priority changes, spending, infrastructure adoption, policy exceptions, and final acceptance at the agreed delivery level.|
|**What survives a closed chat?**|Recorded work, relationships, assignments, decision references, evidence links, and a short checkpoint. An unrecorded conversation or unpublished local code does not become durable merely because an AI saw it.|
|**Why was it rejected earlier?**|The earlier report treated externally persisted PM state as an unacceptable addition to an already authoritative repository-native system. It explicitly considered OpenProject; it did not overlook its existence.|
|**Is it now the strongest option?**|**Conditionally, for your desired operator-facing PM environment.** GitHub Projects becomes the stronger choice when reducing cost, additional administration, and integration boundaries matters more than OpenProject’s workflow model.|

OpenProject’s native GitHub integration displays linked pull requests, their states, and associated GitHub Actions information. Its 17.8.0 release, dated **September 2, 2026**, added MCP creation and modification of work packages, comments, and relations. Those are relevant capabilities—not evidence that Leela already has them configured. ([OpenProject.org](https://www.openproject.org/docs/system-admin-guide/integrations/github-integration/?utm_source=chatgpt.com "GitHub integration - OpenProject"))

### The intended division

> **You decide what matters. OpenProject records what is being organized and delivered. GitHub records implementation and verification evidence. The AI connects these activities without acquiring product authority.**

The important improvement is not “put everything into a nicer board.” It is **making current work retrievable and operable without reconstructing the project from multiple chats and overlapping management documents.**

---

## B. Operator day-in-the-life

The following is the **proposed workflow**, not a description of an existing installation.

### From an idea to approved work

|Journey|What you do|What the orchestrator reads and changes|What you see; approval and recovery|
|---|---|---|---|
|**1. Capture an idea**|“Moving something in Rhythm should not change what I planned to achieve.”|Reads the relevant story and governing references; searches existing work before creating an **Idea** or linking an existing item. No code or semantic changes.|A durable item with your intent and its source. A lost response is recovered by searching that item before creating another.|
|**2. Request a proposal only**|“Explore this; do not implement it.”|Records the proposal-only boundary on a research item. Reads only sources needed for that question.|Findings and options, with implementation still unauthorized.|
|**3. Refine, accept, or reject intent**|You correct the example, accept its meaning, defer it, or reject it.|Records the outcome through the approved repository decision process when product meaning is affected. OpenProject carries the decision reference and planning consequence.|A clear distinction between **accepted intent** and an idea that merely exists. Missing approval keeps dependent work unready.|
|**4. Turn intent into organized work**|“Plan the delivery of this capability.”|Creates a story-delivery work package, coherent child tasks, and a milestone where useful. References accepted intent instead of copying it into competing specifications.|One understandable delivery structure: what it achieves, what is included, and what is not.|
|**5. Let the AI decompose work**|“Work out the implementation steps.”|Reads the selected code, contracts, tests, and evidence gaps. Adds proposed tasks and dependencies within the approved scope.|You review consequential scope choices—not every technical subdivision. Scope expansion returns to you.|
|**6. Select the next work**|“What can we safely advance now?”|Queries approved, unclaimed work; checks actual prerequisites, current priorities, authority references, and overlapping assignments.|A recommended next action with a reason. A missing or ambiguous dependency is shown, not guessed away.|

### From execution to evidence

|Journey|What happens|OpenProject and GitHub changes|Approval and recovery|
|---|---|---|---|
|**7. Coding starts**|The orchestrator claims the bounded task and delegates it to a coding agent.|OpenProject records assignment and execution checkpoint. The coding agent uses a dedicated branch and pull request under the approved repository mandate.|The agent cannot turn an exploratory discussion into coding authority. An unsuccessful claim means no dispatch.|
|**8. Implementation evidence returns**|The coding agent provides its diff, tests, limitations, and PR.|GitHub holds the actual changes and checks. OpenProject links them and records **Implemented**, not automatically **Verified** or **Accepted**.|Failed or missing checks remain visible. A successful old commit is not evidence for a newer commit.|
|**9. A real ambiguity appears**|The agent discovers two materially different product interpretations.|It creates or updates a **Decision request**, links the originating evidence, and blocks only affected work.|You receive the concrete behavior difference and recommendation. Independent work may continue.|
|**10. You intervene directly**|You reprioritize, block, or reopen an item in OpenProject.|That becomes the current operational instruction. The orchestrator rereads it before its next consequential action.|A stale update must not overwrite your intervention. Reopening requires a reason and a new verification target.|

### Across chats, agents, interruptions, and reviews

|Journey|Proposed behavior|Durable result and recovery|
|---|---|---|
|**11. A new chat continues**|It identifies the project, reads current instructions, retrieves selected work and checkpoint, checks linked GitHub evidence, then resumes.|It does not need the whole previous conversation. Missing local work is reported explicitly.|
|**12. Two agents try the same task**|Only a successfully recorded assignment may start. A conflicting update is reread rather than forced through.|One owner for that task. Separate tasks touching the same contracts or files still require coordination.|
|**13. An agent claims “done” too early**|An independent verifier compares the claim against acceptance criteria, the actual diff, test results, and remaining blockers.|The task returns for correction or remains Implemented. A green PR cannot accept product intent.|
|**14. Work is paused, cancelled, superseded, or reopened**|The orchestrator records the reason, unfinished obligations, replacement links, and branch/checkpoint state.|History is retained. Cancellation is not treated as successful fulfillment of a prerequisite.|
|**15. Emergency work arrives**|You explicitly authorize the interruption or invoke a previously approved emergency policy.|A bounded urgent item records what was displaced and which controls still apply. “Urgent” does not silently remove semantic or merge gates.|
|**16. You review a milestone**|You open the milestone view or ask for an explanation.|You see accepted deliveries, unresolved blockers, missing verification, and the consequence for the milestone—not merely a percentage based on closed tasks.|
|**17. Research finishes**|The researcher returns evidence, alternatives, uncertainties, and a recommendation.|The research item can be complete while implementation remains unapproved. Its conclusions do not silently become product truth.|

### What your normal conversation could look like

**You:** “Show me what needs my decision before Rhythm can advance.”

**AI:** “The move operation exists. The unresolved issue is proving that its link to accepted execution remains stable. I recommend accepting the intended behavior, completing a bounded regression task, and keeping the wider identity proof blocked.”

**You:** “Approve that bounded task. Do not redesign the identity model.”

**AI:** Records the exact scope, claims the task, delegates it, and later returns the PR and verification result.

**You, in another chat:** “Continue the Rhythm placement pilot.”

**New AI:** Retrieves the same work item and its evidence instead of reconstructing your instruction from memory.

The current User Story register makes this distinction necessary: it is a **draft for operator verification**, and labels such as `CURRENT` are not blanket acceptance.

---

## C. System architecture and agent operation

### C1. The recommended arrangement

```text
YOU — operator
│
├── Browser → OpenProject
│             priorities · work · blockers · assignments · milestones
│
└── Conversation → PRIMARY AI ORCHESTRATOR
                    │
                    ├── MCP / REST API → OpenProject
                    │                    persistent operational records
                    │
                    ├── GitHub connection → repositories
                    │                       accepted references
                    │                       code · PRs · reviews · CI
                    │
                    ├── bounded research agent
                    ├── bounded coding agent
                    └── independent verification role

GitHub ── signed native webhook ──→ OpenProject
         linked PR/check information

OpenProject server
├── database: work records, relationships, activity
└── persistent files: attachments and configuration
```

**This is a logical workflow, not a command pipeline where OpenProject executes GitHub.** The orchestrator communicates with both systems. OpenProject does not itself become the coding agent or the program supervisor.

A **server** is the continuously available computer running the application. A **database** is where its structured records persist. An **API** is the application’s machine interface. **MCP** exposes selected machine operations in a form compatible AI clients can discover and call. **Credentials** determine whose permissions those calls receive.

**Persistent work is not the same as a continuously running AI.** Closing a chat does not delete the work. It also does not, by itself, leave an agent running. An always-on execution service would be a separate architectural decision; it is not needed to prove this model.

### C2. Native integration versus custom infrastructure

**Proposed:** use the existing AI clients, OpenProject’s official MCP/API, and its native GitHub integration. Do not introduce Hermes, a new orchestration runtime, a custom MCP server, or a bidirectional state-synchronization service as a prerequisite.

For the GitHub link, the native setup uses a dedicated OpenProject account with **View work packages** and **Add notes**, a repository webhook, and a shared webhook secret. OpenProject verifies `X-Hub-Signature-256` when that secret is configured; without it, signature verification is absent. The supported event set is `check_run`, `issue_comment`, `ping`, and `pull_request`. ([OpenProject.org](https://www.openproject.org/docs/system-admin-guide/integrations/github-integration/?utm_source=chatgpt.com "GitHub integration - OpenProject"))

**Linking convention:** always put the full OpenProject work-package URL in the PR description. The detailed documentation also supports `OP#ID`; using the full URL is clearer across instances. Do not depend on a branch name alone to establish the link. ([OpenProject.org](https://www.openproject.org/docs/system-admin-guide/integrations/github-integration/ "GitHub integration - OpenProject"))

### C3. Access by AI client

|Client|Recommended route|What must be proven before use|
|---|---|---|
|**ChatGPT web**|Administrator-published remote MCP connection to OpenProject; OAuth under a restricted automation identity.|The selected workspace supports the required write-capable app flow; authentication, tool discovery, read/write behavior, and confirmation behavior work.|
|**Claude Code**|Native remote HTTP MCP; OAuth or a securely stored token. Community alternative: approved REST calls from the CLI environment.|Only intended tools and project permissions are available; secrets stay outside committed files; updates and resumption work.|
|**Codex CLI**|Its documented MCP configuration, connected to the same official endpoint under a suitable identity.|Client authentication and supported tools are tested separately. Do not assume another client’s configuration is interchangeable.|
|**Other agent clients**|Use the official endpoint only after their specific authentication and transport are checked.|Treat untested compatibility as unverified—not as an installed integration.|
|**Research subagents**|Prefer bounded source packets and read-only access.|They cannot gain implementation authority through task text or tool output.|

OpenAI currently documents full MCP write capabilities in developer mode for Business, Enterprise, and Edu on the web, with workspace administration and permission controls. Client-side confirmations can still apply. Claude Code and Codex document MCP connection mechanisms, but those documents do not prove a working Leela connection. ([OpenAI Help Center](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt "Developer mode and MCP apps in ChatGPT | OpenAI Help Center"))

OpenProject documents `/mcp` as its endpoint. Its shared/web-client OAuth setup uses an application with the `mcp` scope and the client’s redirect URI; its guidance specifies a confidential application. Administrator controls can disable the server or individual tools. ([OpenProject.org](https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/ "MCP Server - OpenProject"))

### C4. A short, restartable startup routine

**Proposed agent runbook:**

```text
1. Identify the project and authenticated role.
2. Read current repository entry instructions and the approved mandate.
3. Query selected work:
   assigned/in-progress → relevant blockers → ready candidates.
4. Fetch only the selected item's references, relations, and latest checkpoint.
5. Reconcile with GitHub:
   branch/PR exists? current commit? checks? conflicting work?
6. Report current state and next action; claim only authorized ready work.
```

The checkpoint belongs inside the existing work package—not in another project-state registry:

```json
{
  "run_id": "<unique execution identifier>",
  "mandate_ref": "<approved scope or decision reference>",
  "repository": "leela-spec/Leela-Cloud-2026",
  "source_commit": "<commit actually inspected>",
  "branch": "<actual branch or null>",
  "pull_request": "<actual PR reference or null>",
  "last_verified_step": "<completed step plus evidence reference>",
  "next_action": "<specific continuation>",
  "pending_decisions": [],
  "unpublished_local_work": "<location and limitation, or none>"
}
```

A fresh chat must **validate** the checkpoint against current records. It is a retrieval aid, not permission to repeat old actions blindly.

### C5. Claiming work and handling collisions

OpenProject’s REST update requires the `lockVersion` obtained when the record was read. A stale update receives a conflict response. The 17.8 MCP write tools also perform version checks. ([OpenProject.org](https://www.openproject.org/docs/api/endpoints/work-packages/ "API: Work Packages"))

**Proposed claim procedure:**

```text
Read current item and version
    ↓
Check: approved scope + eligible dependencies + no current claimant
    ↓
Update together: assignee + In progress + execution run identifier
    ↓
Read back the successful result
    ↓
Dispatch coding work

Conflict → reread → respect the existing claim or operator change
```

This is **not** a native distributed lease or an exactly-once execution guarantee. The application protects a record update; the operating procedure must prevent an agent from starting without a successful claim.

For the pilot, use one primary dispatching orchestrator. Parallel subagents are allowed for independently bounded work. Shared files, shared contracts, or incompatible branches still require serialization.

This fits the current repository better than resurrecting the older global singleton assumption: current `AGENTS.md` permits multiple independent active packets and requires coordination where work overlaps.

For interrupted requests, search for the recorded action/run identifier and reread state before retrying. For an apparently abandoned task, inspect the branch and checkpoint before reassignment. Do not equate “old timestamp” with “safe to run twice.”

---

## D. Ownership matrix

**Proposed post-adoption ownership. None of these changes takes effect through this research.**

|Persistent information|Authoritative home|OpenProject’s role|Repository/GitHub role|
|---|---|---|---|
|**Product goal and intended behavior**|Approved repository product/decision source|Links the goal to planned delivery|Retains the approved meaning|
|**Accepted User Story**|Approved repository story/decision record|Story-delivery item references it|Stores accepted wording and provenance after explicit approval|
|**Product decision**|Existing repository decision mechanism|Requests the decision and displays its operational consequence|Records the ruling and its application|
|**Semantic/specification rule**|Existing repository authority structure|Reference only|Retains rule, decision, and authority relationships|
|**Work breakdown**|OpenProject|Owns delivery decomposition|Holds technical contracts only where they are needed|
|**Operational status and priority**|OpenProject|Owns current planning state|Does not maintain an independently editable copy|
|**Task dependency/blocker**|OpenProject|Owns operational relations|Supplies referenced semantic prerequisites or evidence|
|**Assignment and execution claim**|OpenProject|Owns claimant and checkpoint|Branch/PR supplies execution evidence|
|**Code**|GitHub repository|Links it|Owns it|
|**PR and review**|GitHub|Displays/link references|Owns original review and merge records|
|**Test and CI result**|Originating test/CI evidence|Displays evidence and verification conclusion|Owns original result and tested commit|
|**Materialization assertion**|Existing feature ledger and its governing contract|Links relevant gaps/evidence|Owns rule-to-artifact assertions|
|**Planned milestone/release scope**|OpenProject|Owns intended delivery grouping/date|References resulting releases|
|**Actual release artifact**|GitHub/release system|Links delivered result|Owns actual release/tag/artifact|
|**Operational history**|OpenProject activity|Owns changes to its work records|No duplicate operational journal|
|**Repository change history**|Git and retained repository receipts|Links relevant evidence|Owns the original change history|

**The crucial distinction:** “Task implemented” and “this rule is demonstrably realized by this artifact” are different facts. Moving the first into OpenProject does not justify deleting the second.

The materialization contract explicitly defines rule-to-artifact evidence, including missing, contradicted, implemented, and validated relationships. It is not just a backlog in CSV form.

### An existing authority inconsistency must not be hidden

Current root instructions and some older architecture/PM prose do not express the same precedence and execution model. In particular, root instructions place accepted operator decisions and authored materialization at the top of the working authority chain, while older materialization prose says feature specifications remain semantic truth.

**Recommendation:** follow current entry instructions, surface any consequential conflict, and resolve it through the existing operator process. Do not let OpenProject adoption silently “repair” repository authority.

---

## E. Permissions and autonomy

### E1. Proposed action matrix

“Within mandate” means an explicitly approved scope—not whatever an agent decides would be useful.

|Action|Operator|Primary orchestrator|Research agent|Coding agent|Independent verifier|
|---|---|---|---|---|---|
|Read relevant work/evidence|Yes|Yes|Scoped|Scoped|Scoped|
|Create draft work|Yes|Yes|Propose; orchestrator records|Propose|Propose|
|Decompose approved work|Approves consequential scope|Within mandate|Recommend|Recommend technical steps|Challenge gaps|
|Reprioritize|Decides|Apply explicit decision/delegation|No|No|No|
|Mark work blocked|Yes|Yes, with evidence|Report blocker|Report blocker|Report blocker|
|Claim/assign work|Yes|Dispatch within mandate|Assigned research only|Assigned coding only|Assigned verification only|
|Mark implemented|Yes|On evidence|Research completion only|Own bounded implementation|No self-substitution for coding|
|Mark verified|Accepts/reviews|Records independent result|No|Not own work|Yes|
|Mark operator-accepted|**Yes**|No autonomous transition|No|No|No|
|Reopen|Yes|On failed criteria within policy|Recommend|Recommend|Recommend with evidence|
|Delete work|Exceptional administrative action|No|No|No|No|
|Accept a User Story|**Decides**|Records approved decision only|No|No|No|
|Change a product decision|**Decides**|Applies approved transaction only|No|No|No|
|Link PR/evidence|Yes|Yes|Research evidence|Implementation evidence|Verification evidence|
|Change roles, integrations, secrets|Authorized administrator|No|No|No|No|

**Pilot recommendation:** operational writes pass through the primary orchestrator; research and coding subagents return evidence rather than each receiving broad PM credentials. Separate verifier and operator transitions remain distinguishable.

### E2. What is technically enforced—and what is not

OpenProject supports status-transition workflows by role and work-package type. Additional author/assignee transition settings can grant further transitions, so these must be tested rather than assumed restrictive. ([OpenProject.org](https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-types/workflows/ "https://www.openproject.org/docs/system-admin-guide/manage-work-packages/work-package-types/workflows/"))

Configure server-side restrictions for critical transitions, especially **Operator accepted**, and do not give an automation account the operator’s role.

However:

**“May edit a work package” is not proven equivalent to “may edit every field except priority.”** I did not establish a native field-level permission arrangement that enforces every row of the proposed matrix independently. Some boundaries therefore remain procedural unless the chosen configuration demonstrably enforces them.

Similarly, required custom fields are not a sufficient completion gate: the REST documentation says omitted required custom fields are not automatically validated on every partial update unless full custom-field validation is requested. ([OpenProject.org](https://www.openproject.org/docs/api/endpoints/work-packages/ "API: Work Packages"))

Therefore, **Verified** must depend on inspection of evidence, not merely on a nonempty “Evidence” field.

### E3. GitHub safeguards

At the reviewed snapshot, the branch metadata reported `protected: false`. That is not a complete assessment of all effective repository rulesets, but it is enough to reject an untested assumption that direct writes to `master` are technically prevented.

**Future implementation prerequisite:** verify effective branch protections/rulesets, required reviews/checks, and bypass rights before granting autonomous write credentials. GitHub’s availability of these controls depends on repository visibility and plan. ([GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets?search-overlay-ask-ai=true&search-overlay-input=what+does+setting+ruleset+enforcement+to+evaluate+do "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets?search-overlay-ask-ai=true&search-overlay-input=what+does+setting+ruleset+enforcement+to+evaluate+do"))

Use existing managed GitHub access where suitable. GitHub App installation tokens can be restricted to selected repositories and permissions and expire after one hour; repository write permission still needs branch-level controls to constrain the delivery route. ([GitHub Docs](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app?utm_source=chatgpt.com "Generating an installation access token for a GitHub App - GitHub Docs"))

**Security rule:** work-package text, research findings, and comments are task data. They cannot authorize credential changes, weaken repository rules, or promote themselves into higher-priority instructions.

---

## F. Deployment, editions, and cost

### F1. Deployment comparison

|Dimension|Managed OpenProject cloud|Persistent VPS/server|Laptop-local installation|
|---|---|---|---|
|**Application/database/files**|Provider-hosted|Your server and persistent storage|Your laptop or local VM|
|**Browser access**|Through hosted address|Through secured server address|Local access; remote access needs additional connectivity|
|**Laptop must remain on?**|No|No|Yes, while the service is needed|
|**Agent connectivity**|Suitable for browser and CLI clients|Suitable when securely reachable|Straightforward for local clients; browser/cloud clients need a tested secure route|
|**Maintenance**|Provider handles platform operation|You own updates, monitoring, recovery|You own operation plus laptop availability|
|**Backups**|Provider mechanisms plus your export/recovery checks|You design and test them|You design and test them; same-device copies are insufficient|
|**Security responsibility**|Accounts, roles, integrations, data-sharing policy|Those plus OS, network, database, storage|Those plus local-device exposure and remote-access design|
|**Cost structure**|Subscription; AI-client charges separate|Hosting, storage, administration, and optional Enterprise license|Hardware/resource use, administration, optional license|
|**Reversibility**|Requires usable exports/full backup and a tested exit|Direct control of database/files, still requires restore proof|Same, with greater availability dependence|
|**Recommendation**|**Preferred pilot route, subject to quote and entitlement**|Good when ownership/control justifies operations work|Rehearsal only; not the preferred shared persistent PM home|

OpenProject’s published self-hosting baseline includes a quad-core CPU, 4 GB RAM, and 20 GB disk space. These are starting requirements, not a guarantee for a specific workload or a reason to place another persistent service on an already constrained laptop. ([OpenProject.org](https://www.openproject.org/docs/installation-and-operations/system-requirements/ "https://www.openproject.org/docs/installation-and-operations/system-requirements/"))

### F2. Edition boundaries that affect the decision

|Capability|Finding|Adoption consequence|
|---|---|---|
|Work packages, project tracking, API-based automation|Community provides the underlying application and API without a per-user license charge.|A CLI/API operating model is viable without native MCP.|
|**Native MCP server**|Professional entitlement is indicated by the 17.8.0 upstream configuration test.|Do not budget the browser-agent model as Community-only.|
|MCP writes|Added in 17.8.0.|Require a compatible supported version; older read-only behavior is insufficient.|
|Relations displayed in the work-package table|Moved into Community in 17.8.0.|Older documentation describing that display as paid is outdated for this version.|
|Native GitHub PR/check display|Documented native integration.|Use it for evidence visibility, not as an automatic acceptance mechanism.|
|Portfolio-level functionality|Enterprise functionality.|Not required for one Leela pilot project; avoid making it a dependency.|

Sources: Community/API documentation, pinned MCP entitlement test, versioned release notes, integration documentation, and portfolio documentation. ([OpenProject.org](https://www.openproject.org/community-edition/?utm_source=chatgpt.com "OpenProject Community Edition - Free and Open Source"))

A documentation conflict is worth making explicit: the general MCP administration page still described read-only tools when retrieved; the **versioned 17.8.0 release notes and tagged source** establish the later write capabilities. Use the latter for that version-specific claim. ([OpenProject.org](https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/ "MCP Server - OpenProject"))

### F3. Cost conclusion

The retrieved pricing page’s **on-premises** configuration displays Professional at **€10.95 per user/month with 25 minimum users**. That implies a displayed license floor of **€273.75/month**, before hosting and other applicable charges or billing conditions. It is not a quote for a single operator and must not be reused as a cloud price. ([OpenProject.org](https://www.openproject.org/pricing/ "OpenProject Pricing - from €0. Start your free trial now."))

**Not conclusively established from the retrieved pricing interface:** the complete current Professional cloud total for your intended human and automation accounts, including applicable minimum seats. Obtain that commercial result before purchase; it is a vendor fact to verify, not a question you should have to guess.

Consequently:

> **Do not buy Enterprise Professional simply because native MCP exists. First demonstrate that its operator experience is worth the incremental cost over GitHub Projects or Community plus CLI/API.**

### F4. Recovery requirements

For self-hosting, the backup set must cover the database, persistent attachments, configuration, and necessary secrets; test restoration into an isolated environment. For cloud, the published backup documentation describes retained recovery points, but its self-service attachment export has a 1 GB limit, with larger/full backups requiring the appropriate support route. ([OpenProject.org](https://www.openproject.org/docs/installation-and-operations/operation/backing-up/ "https://www.openproject.org/docs/installation-and-operations/operation/backing-up/"))

**Proposed service targets:** daily recoverable backups, a backup before upgrades, and a demonstrated restore within one working day. These are acceptance targets—not claims about an untested installation or contractual guarantees.

---

## G. What this prevents—and what it does not

The repository’s anti-drift catalog reports false recall, context degradation, dropped instructions, premature completion, wrong-scope work, and redundant verification. OpenProject can provide useful controls around these failures, but it cannot make an AI’s interpretation correct.

|Failure class|Proposed mechanism|What it can prevent|What it cannot prevent|Residual control and pilot test|
|---|---|---|---|---|
|**A new chat loses the state**|Selected-work query plus checkpoint|Reconstructing current assignment from memory|A misleading checkpoint|Fresh GitHub reconciliation; resume in three clean chats|
|**Plans contradict one another**|One operational owner after migration|Independently edited copies of task status|Contradictory product decisions|Repository authority remains; introduce a conflicting source and require escalation|
|**Two agents do the same work**|Version-checked assignment before dispatch|Simultaneous successful claims on one record|Separate tasks touching the same files|Scope/branch coordination; race two claims|
|**An AI overwrites your change**|Fresh read and conflict handling|Blind stale record updates|A deliberate but unauthorized new edit|Permission/policy checks; reprioritize during execution|
|**“Merged” becomes “done”**|Separate Implemented, Verified, Accepted states|Premature administrative closure|Tests that validate the wrong behavior|Independent acceptance review; use the real Rhythm identity gap|
|**Research becomes implementation**|Research-only mandate and approval gate|Unmarked promotion into execution|An agent ignoring its mandate|Restrict credentials and inspect attempted actions|
|**A blocker disappears from view**|Explicit operational relations|Hidden dependencies in prose|Incorrect dependency modeling|Inspect meaning and fulfillment; test cancelled prerequisites|
|**The AI reads the whole repository again**|Task-linked just-in-time retrieval|Unnecessary context loading|A badly scoped retrieval plan|Compare fetched context and result quality against baseline|
|**Old test evidence is reused incorrectly**|Evidence tied to actual commit and inputs|Presenting unrelated results as current|Inadequate tests|Change the branch after a green run and require re-evaluation|
|**Migration loses commitments**|Per-artifact disposition and reconciliation|Untracked deletion of unique obligations|A poor inventory judgment|Reconcile every migrated live item before retirement|
|**A server or credential fails**|Checkpoints, backups, restricted identities|Loss of all resumable state from one failure|Immediate service availability|Revoke a token and perform an isolated restore|

**No supported claim:** OpenProject prevents hallucination, semantic drift, bad requirements, or unauthorized judgment merely by being installed.

---

## H. Repository-artifact disposition

**These are proposed dispositions for a later approved migration wave. Everything stays unchanged during this research and its non-authoritative rehearsal.**

|Artifact family|Proposed disposition|Boundary|
|---|---|---|
|**Generated `STATUS`**|**Retain with narrower role**|Keep repository/materialization health and evidence summaries. Replace operational “what is assigned/next” ownership with an OpenProject reference after cutover.|
|**Live packet contracts**|**Retain with narrower role**|Preserve scope, forbidden changes, acceptance requirements, and technical execution constraints. Remove or derive duplicated operational lifecycle fields only through approved tooling/contract changes.|
|**Embedded task lists and authored backlog/status documents**|**Retire after migration**|Only after every surviving commitment has a destination and inbound references are repaired.|
|**Completed packets**|**Retain unchanged**|Historical delivery records are not stale live state to be rewritten.|
|**`STATE` receipts**|**Retain with narrower role**|Preserve repository delivery/history. Do not duplicate every OpenProject status event there.|
|**Handover documents**|**Replace with link/reference** for live operational continuation|Use work-package checkpoints and source links. Retain unique technical instructions or historical evidence where needed.|
|**Decision queue presentation**|**Retain with narrower role**|OpenProject may present pending decisions affecting work; accepted rulings and their application remain in the existing decision mechanism.|
|**Accepted decisions, governing references, semantic contracts**|**Retain unchanged**|No semantic ownership migration is implied.|
|**Per-feature materialization ledgers**|**Retain unchanged**|Do not convert each artifact edge into a task or replace evidence state with PM status.|
|**Optional offline PM export**|**Derive/generate**|Clearly timestamped, read-only recovery/export material; not another editable authority.|

The existing consolidation packet already requires preserving unique claims before retiring documents and protecting completed/history artifacts. Adoption should reuse that discipline, not bypass it.

**Cutover rule:** define a point after which OpenProject owns the migrated operational fields. Do not run two editable authorities indefinitely.

Changes to packet validation, status generation, or repository entry routing are **part of that future migration**, not incidental setup. A new application cannot override those contracts by existing.

---

## I. Why earlier research rejected OpenProject—and the alternatives

### I1. Forensic answer

The originating report explicitly classified OpenProject as **“Nicht Core”** because its work packages, statuses, roadmaps, and database would create a second operational state. It required priorities, decisions, work in progress, materialization, and status to remain within Leela’s existing system.

|Earlier assumption or finding|Still valid?|What changed?|Consequence|
|---|---|---|---|
|**An additional authoritative tracker creates drift.**|Yes.|The new question permits replacing operational ownership rather than adding a mirror.|Adoption must include retirement/narrowing of duplicate PM surfaces.|
|**Product semantics must not be duplicated in a PM database.**|Yes.|Nothing requires OpenProject to own product semantics.|Keep semantic decisions and evidence in their repository homes.|
|**Exactly one active packet must exist.**|Not as a blanket current rule.|Current root instructions permit independent active packets.|Reassess coordination against current scope-overlap rules.|
|**The core workflow must remain local and Git-only.**|A policy preference, not a universal technical necessity.|A persistent shared PM application is now being considered explicitly.|The operator must consciously accept that availability/storage tradeoff.|
|**The primary agent must remain accountable.**|Yes.|OpenProject need not become another supervisor.|Keep one accountable orchestrator per bounded workstream.|
|**OpenProject’s capabilities at the earlier baseline were sufficient grounds for exclusion.**|Requires updating.|The earlier report referenced 17.6; 17.8 adds MCP writes and relations management.|Current agent interaction is materially more direct.|
|**External persistent state is inherently the wrong solution.**|Too broad for the revised question.|Operational and semantic ownership can be separated.|Evaluate the actual journeys and migration cost instead of excluding by category.|

Current root rules and the later alignment note support the changed framing; the old report supports the original exclusion.

**Conclusion:** the evidence supports a change in the decision premises, plus a relevant capability update. It does **not** support a blanket accusation that all earlier research “missed OpenProject.”

### I2. Bounded alternatives

**GitHub Projects** supports issue/PR-oriented tables, boards, roadmaps, custom fields, and automation. GitHub also now supports nested sub-issues and explicit blocking relationships, so it is a serious alternative for the same journeys. ([GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects?search-overlay-ask-ai=true&search-overlay-input=can+i+edit+the+appearance+of+an+existing+project%3F "https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects?search-overlay-ask-ai=true&search-overlay-input=can+i+edit+the+appearance+of+an+existing+project%3F"))

**Plane** documents a hosted MCP server and official self-hosted connection routes. Its GitHub integration includes issue synchronization and PR-state automation. That integration is marked Pro; its pricing places workflow/approval capabilities in different higher tiers. Its bidirectional synchronization is useful only if field ownership is deliberately controlled. ([Plane Developers](https://developers.plane.so/dev-tools/mcp-server "MCP server | Plane"))

**Linear remains materially relevant** because its managed MCP server supports finding, creating, and updating issues, projects, and comments. It is a credible managed AI-access alternative, rather than something to exclude merely because OpenProject was named first. ([Linear](https://linear.app/docs/mcp "MCP server – Linear Docs"))

### I3. Decision matrix

The following is **my comparative assessment**, not a benchmark measurement. “Higher” is desirable for fit/integration; “lower” is desirable for risks and burdens.

|Option|Impact on your journeys|Evidence confidence|Operator usability hypothesis|Agent integration|Duplicate-state risk if poorly adopted|Maintenance burden|Migration risk|
|---|---|---|---|---|---|---|---|
|**OpenProject, Professional native MCP**|High|High for documented mechanisms; live operation untested|Strong visual work/dependency/approval model|Strong, with a newly expanded MCP surface|High without ownership cutover|Low on managed cloud; higher self-hosted|Medium–high|
|**Current repo-native model**|Limited new improvement|High for inspected repository contracts|Demands more interpretation of files and generated views|Direct for repository agents|Lowest additional risk|Existing custom-document/tooling burden remains|Lowest|
|**GitHub Projects**|High|High for documented mechanisms|Strong for delivery; less separation from developer tooling|Strong proximity to issues, PRs, and existing agent access|Medium until duplicate repo PM fields retire|Low additional infrastructure|Medium|
|**Plane**|High potential|Medium–high; exact chosen-plan behavior needs testing|Promising; unmeasured with you|Official MCP plus GitHub integration|High if bidirectional issue sync is enabled indiscriminately|Low cloud; higher self-hosted|Medium–high|
|**Linear**|High potential|Medium–high for the bounded features examined|Promising managed workflow; unmeasured with you|Strong managed MCP route|Medium until ownership is explicit|Low infrastructure burden|Medium–high|

### I4. Recommendation hierarchy

**Lead candidate: OpenProject**, when the priority is a dedicated operator-facing PM application with explicit workflow and responsibility boundaries.

**Principal fallback: GitHub Projects**, when you prefer fewer services, closer delivery integration, and lower incremental operating cost.

**Challengers: Plane and Linear**, not rejected on principle. Neither has demonstrated a sufficiently decisive advantage in this bounded investigation to justify changing the primary pilot candidate before its price and connection gates are checked.

**Important:** there is no unconditional economic winner yet. OpenProject’s Professional requirement can legitimately reverse the decision for a small operation.

---

## J. The real Leela pilot

### J1. Selected story

**`RHY-08 — Move a placement`**, from:

```text
docs/UserStories/Leela Master User Story Register.md
```

Its stated intent is that moving something in the calendar changes temporal placement only, not Path demand or SequenceInstance structure. The register is still a draft awaiting operator verification.

Use the **repository + source path + story ID + reviewed commit** as the reference. Do not assume `RHY-08` alone is globally unique: the Rhythm specification also contains an older `RHY-xx` decision family.

### J2. What is actually present

|Evidence layer|Retrieved finding|Pilot consequence|
|---|---|---|
|**User intent**|Moving placement must not change demand or accepted structure.|Confirm the intended behavior explicitly.|
|**Governing references**|Rhythm rules include read-only Path consumption and stable accepted-Instance references.|Link those requirements; do not invent new ownership.|
|**Implementation**|`MovePlacementCommand` replaces the interval for the matching placement; undo restores the previous interval.|A bounded characterization/regression task has a real implementation target.|
|**Data shape**|`RhythmPlacement` contains `variantId`; it has no explicit `instanceId` field.|The selected evidence does not establish the complete accepted-Instance guarantee.|
|**Existing tests**|Controller tests cover operations such as scheduling, undo by placement count, and rejected hard-conflict placement.|Useful foundations, not sufficient proof of the full story.|
|**Materialization evidence**|Selected ledger rows record missing/insufficient accepted-identity and read-only-Path proof. Their verification pins are older than the research snapshot.|Recheck evidence rather than promoting historical ledger notes into freshly executed verification.|

Sources: Rhythm specification, command implementation, placement model, controller tests, and the selected ledger slice.

**This is the pilot’s strongest test:** a bounded implementation task may finish while the parent story remains blocked by missing proof. A PM system that marks both complete has failed.

### J3. Proposed OpenProject structure

The labels below are planning labels, **not existing OpenProject IDs**.

```text
Project: Leela PM Pilot
└── Epic: Reliable Rhythm placement
    └── Story delivery: RHY-08 — Move a placement
        ├── R1 Research: establish current move/undo and identity evidence
        ├── D1 Decision: approve story meaning and bounded pilot scope
        ├── T1 Task: characterize and regression-test existing move/undo
        ├── V1 Verification: independently verify T1
        └── T2 Task: prove full accepted-Instance / Path invariants
                     BLOCKED until existing proof is found
                     or a separate repair is approved

Milestone: PM operating model proven
```

Relations:

```text
D1 → blocks T1
T1 → blocks V1
V1 → required evidence for accepting the bounded pilot delivery

T2 remains necessary for full RHY-08 acceptance.
T1/V1 completion does not close the full story.
```

OpenProject distinguishes relation meanings: a **Blocks** relation constrains closure; **Requires** is informational; predecessor/successor scheduling has its own behavior. None should be treated as a universal “safe to start” decision. ([OpenProject.org](https://www.openproject.org/docs/user-guide/work-packages/work-package-relations-hierarchies/ "Work package relations and hierarchies - OpenProject"))

**Pilot policy:** the orchestrator checks that prerequisites were actually fulfilled. A prerequisite closed as cancelled or superseded is not automatically successful.

### J4. Exact repository and GitHub linkage

**Existing inspection targets**

```text
lib/features/rhythm/application/rhythm_commands.dart
lib/features/rhythm/application/rhythm_week_controller.dart
lib/features/rhythm/domain/rhythm_placement.dart
test/features/rhythm/application/rhythm_week_controller_test.dart
docs/ssot/features/rhythm/materialization.csv
```

**Proposed new test target, only after authorization**

```text
test/features/rhythm/application/rhythm_move_placement_test.dart
```

**Proposed branch convention**

```text
pilot/<assigned-work-package-id>-rhy-08-characterization
```

The PR description should carry the actual work-package URL, approved scope reference, source commit, acceptance assertions, test commands/results, and known limitations. No PR number or work-package ID has been invented here.

Potential authorized verification commands include:

```text
flutter test test/features/rhythm/application/rhythm_week_controller_test.dart
flutter test test/features/rhythm/application/rhythm_move_placement_test.dart
python scripts/gates.py --since origin/master
```

Their applicability must follow the repository’s current gate-routing rules. These commands were **not run** during this research.

### J5. Preconditions and scope

The first rehearsal uses an **isolated, non-authoritative pilot project** with real source references and simulated execution transitions.

A real coding pilot requires a separate bounded mandate that reconciles its execution with current repository packet rules. Until that exists, the OpenProject rehearsal does not become a competing live authority.

The pilot does **not** authorize an identity redesign. T2 may be resolved by locating and verifying an existing valid reference-resolution mechanism; otherwise it remains blocked pending separately approved work.

### J6. Scripted acceptance tests

|Test|Script|Required result|
|---|---|---|
|**P01 — Proposal boundary**|Submit RHY-08 with “research only.”|Research item only; no implementation claim or repository write.|
|**P02 — Approval propagation**|Approve only the bounded characterization task.|T1 becomes eligible; full-story acceptance does not occur.|
|**P03 — Claim collision**|Two clients attempt to claim T1 from the same read state.|One valid claim; the other rereads and does not execute.|
|**P04 — Manual intervention**|Change priority or pause the task during a stale agent session.|Your current change survives; the agent reconciles.|
|**P05 — PR feedback**|Link an authorized pilot PR and produce check results.|Correct PR/check information appears against the intended item.|
|**P06 — False completion**|Request full RHY-08 closure using only green move/undo tests.|Closure is rejected or withheld because full invariants lack evidence.|
|**P07 — Independent verification**|Coder marks T1 Implemented and tries to self-accept.|It cannot perform the operator-acceptance transition.|
|**P08 — Fresh-chat resumption**|Resume from three clean conversations.|Each retrieves the same scope, evidence, pending work, and next action without a history dump.|
|**P09 — Lost response/retry**|Interrupt a write response, then retry the workflow.|Existing result is reconciled before another creation or dispatch.|
|**P10 — Cancelled prerequisite**|Cancel a blocker instead of fulfilling it.|Dependent work is not treated as semantically ready merely because the blocker is closed.|
|**P11 — Emergency/pause/reopen**|Introduce urgent work, pause T1, then resume it.|Displaced work, scope, branch, and verification state remain recoverable.|
|**P12 — Credential failure**|Revoke an automation credential.|Access fails safely; no silent switch to an operator/admin identity.|
|**P13 — Recovery**|Restore/export the pilot into an isolated recovery environment.|Items, relations, comments, references, and essential configuration are recoverable.|
|**P14 — Operator review**|Ask you to identify next work, blockers, decisions, and milestone status.|You can explain them without reading repository management documents.|

### J7. Metrics and failure criteria

**Proposed acceptance thresholds—not measured results:**

|Metric|Target|
|---|---|
|Unauthorized semantic acceptance, deletion, or implementation|**Zero**|
|Duplicate execution in 20 controlled claim attempts|**Zero**|
|Lost operator changes in conflict tests|**Zero**|
|Pilot items with source, mandate, owner, and acceptance reference|**100% where applicable**|
|False full-story completion despite the known evidence gap|**Zero**|
|Fresh-chat resumption|Successful in all three scripted attempts|
|Retry reconciliation|No blind duplicate creation/dispatch in the scripted cases|
|Operator comprehension|Find and explain the next action, blocker, and needed decision within two minutes each|
|Efficiency|Compare against the same repo-native exercise; target a meaningful reduction in retrieval/administrative effort without worse answers|
|Recovery|Complete, demonstrated recovery of the pilot evidence and relationships|

A small pilot does not establish a statistical guarantee. It establishes whether the proposed mechanism works in the failures that matter most here.

**Hard stop:** unauthorized authority change, untraceable work, repeated overwrite/duplicate execution, or inability to recover the state.

### J8. Rollback

For the rehearsal: export the evidence, archive the pilot, remove its integration access, revoke pilot credentials, and leave repository authority unchanged.

For an authorized code pilot: preserve the PR and review history; close an unmerged PR or use a separately approved normal revert for merged changes. No force-resetting shared history.

For a later live migration rollback: first preserve **new** operational facts created after cutover and map unfinished work back to the approved repository route. Restoring an old database or old backlog alone is not a complete rollback.

---

## K. Implementation-ready adoption blueprint

**Status: proposed, not executed.**

The default below is **managed OpenProject with Professional MCP entitlement**. Community plus CLI/REST is the explicit alternative, not an invisible substitution.

Each stage defines its prerequisite, action, responsibility, system boundary, evidence, checkpoint, and reversal.

|Stage|Prerequisite / dependency|Exact action, owner, and changed system|Input → output / validation|Checkpoint, edition, security, rollback|
|---|---|---|---|---|
|**1. Select deployment and edition**|Operator chooses the cost/control preference in Section L|**Operator + administrator:** obtain the exact cloud/on-prem quote and verify native-MCP entitlement and intended account licensing. No repository changes.|Requirements and account model → confirmed configuration and total cost. Validate that the selected package includes needed capabilities.|**Checkpoint:** approve pilot expense only. **Edition:** Professional for native MCP; CE for REST alternative. **Security:** no production credentials yet. **Rollback:** decline/cancel trial.|
|**2. Provision and secure the pilot**|Stage 1|**Administrator:** create an isolated private instance/project; configure secure access. For VPS, use the official supported deployment route with persistent storage and database, not a custom application image.|Selected deployment → reachable private service and first recoverable backup. Validate authentication, storage persistence, and recovery access.|**Checkpoint:** no real project data until access is restricted. **Edition:** selected edition. **Security:** HTTPS; nonpublic database; secrets outside Git. **Rollback:** export then remove pilot environment.|
|**3. Establish identities and roles**|Stage 2; autonomy decision|**Administrator:** create operator, restricted orchestrator, verifier, and low-privilege GitHub integration identities. Give subagents direct accounts only where justified.|Permission matrix → configured roles and negative-test results. Attempt prohibited acceptance, deletion, and administration.|**Checkpoint:** approve only the permissions that pass. **Edition:** verify chosen role features. **Security:** no shared operator credential. **Rollback:** revoke tokens/remove memberships.|
|**4. Create project hierarchy**|Stage 3|**Orchestrator under mandate:** create `Leela PM Pilot`, the Rhythm epic, story-delivery item, and pilot milestone. Use the structure in J3.|Qualified source references → scoped hierarchy. Validate no production items or whole-repo imports were created.|**Checkpoint:** confirm scope, not every technical item. **Edition:** no portfolio module dependency. **Security:** private membership. **Rollback:** archive pilot hierarchy.|
|**5. Configure work model**|Stage 4; acceptance policy|**Administrator:** configure types, statuses, transitions, priorities, relations, and reusable item structure described below.|Operating policy → tested work model. Validate forbidden transitions, blocked work, required evidence handling, and view behavior.|**Checkpoint:** accept the lifecycle. **Edition:** selected features verified in instance. **Security:** roles must not regain forbidden transitions through author/assignee grants. **Rollback:** restore pilot configuration snapshot.|
|**6. Configure native GitHub linkage**|Stages 2–5; repository integration authorization|**Repository administrator:** enable the OpenProject GitHub module, set up the restricted integration identity, signed webhook, and supported events. Verify effective repository write/merge protections separately.|Authorized test repository/branch → linked PR/check display. Validate correct mapping and invalid-signature rejection.|**Checkpoint:** approve connection scope. **Edition:** test actual selected instance. **Security:** redact webhook query credentials from logs; no admin token. **Rollback:** remove webhook and revoke integration token.|
|**7. Connect each AI client**|Stage 3 and, for native MCP, entitlement confirmed|**Client/workspace administrator:** connect ChatGPT, Claude Code, or Codex through their documented route; discover enabled tools.|Endpoint, client settings, restricted identity → successful read/create/update tests. Verify each client separately.|**Checkpoint:** enable writes only after negative permission tests. **Edition:** Professional MCP or explicit CE REST route. **Security:** OAuth/secret storage outside repo. **Rollback:** disconnect app and revoke credential.|
|**8. Establish orchestrator routines**|Stages 5–7|**Orchestrator owner:** adopt C4/C5 startup, claim, update, interruption, and checkpoint routines in the approved instruction home. Do not create another task registry.|Current instructions → operational runbook and sample checkpoint. Validate a clean-session rehearsal.|**Checkpoint:** approve the bounded execution policy. **Edition:** either route. **Security:** no privilege escalation through task text. **Rollback:** disable writes and retain read-only procedure.|
|**9. Prepare the real-source pilot**|Stage 8; explicit pilot mandate|**Orchestrator + verifier:** populate R1/D1/T1/V1/T2 with the exact references and limitations from J. Record baseline effort.|Repository evidence → complete pilot items and acceptance scripts. Validate that the draft story is not represented as already accepted.|**Checkpoint:** authorize rehearsal and separately any coding slice. **Edition:** selected route. **Security:** no unrelated repository access. **Rollback:** archive items; leave production untouched.|
|**10. Execute pilot scripts**|Stage 9; authorized scope only|**Operator, orchestrator, coder, verifier:** run P01–P14. A real code task stays on its approved branch and current repository route.|Scripts → observations, PR/evidence references, failures. Validate success and negative cases, not just a happy path.|**Checkpoint:** stop on hard failure. **Edition:** record actual tested version/edition. **Security:** disposable restricted test credentials for failure tests. **Rollback:** J8 procedure.|
|**11. Assess metrics and failures**|Stage 10|**Independent verifier:** compare against the repo-native baseline and check every acceptance criterion.|Evidence → pass/fail report, measured costs, operator feedback, unresolved defects.|**Checkpoint:** no “mostly passed” adoption for a hard failure. **Edition:** assess downgrade implications. **Security:** reports contain no secrets. **Rollback:** remain in rehearsal or reject.|
|**12. Decide adopt versus rollback**|Stage 11 and confirmed commercial terms|**Operator:** accept, extend with a bounded corrective scope, or reject.|Pilot report → explicit decision and permitted next scope.|**Checkpoint:** this is the adoption decision, not permission inferred from successful setup. **Edition:** approved cost/entitlement. **Security:** revoke unused accesses. **Rollback:** export and archive.|
|**13. Migrate and retire PM artifacts**|Separate approved migration mandate after Stage 12|**Repository integration owner + administrator:** inventory only the selected live PM scope; map fields/commitments; freeze old operational writes; migrate; reconcile; change routing/generators/contracts; retire duplicates under H.|Approved mapping → one operational owner and preserved evidence. Validate counts, links, unique commitments, gates, and rollback mapping.|**Checkpoint:** explicit cutover authorization. **Edition:** adopted configuration. **Security:** bounded migration credentials, then revoke. **Rollback:** preserve post-cutover facts before returning ownership.|
|**14. Operationalize backup and upgrades**|Needed before live cutover; fuller review after pilot|**Administrator:** schedule encrypted off-site recovery copies, pre-upgrade backups, restoration exercises, version review, and credential rotation.|Runbook and backup set → demonstrated recovery and maintained service.|**Checkpoint:** accept recovery targets and owner. **Edition:** provider/self-host procedures differ. **Security:** protect backups and key access. **Rollback:** tested restore, not an untested file copy.|
|**15. Publish final operator/agent runbooks**|Stages 12–14|**Orchestrator owner + operator:** record the approved architecture, everyday commands, ownership, escalation, resumption, incident, and exit routines in one approved location with links.|Tested configuration → operator-ready and agent-ready instructions. Validate one final clean-chat continuation.|**Checkpoint:** final acceptance of the operating model. **Edition:** document actual tested dependencies. **Security:** configuration references, never secret values. **Rollback:** return to retained approved runbooks and access policy.|

### K1. Work-model configuration

**Proposed types:** Idea, Research, Story delivery, Task, Decision request, Milestone. Use an Epic parent where it improves understanding.

**Proposed lifecycle:**

```text
Proposed → Needs decision → Approved for planning → Ready
                                                    ↓
                                               In progress
                                                    ↓
                                               Implemented
                                                    ↓
                                                Verified
                                                    ↓
                                            Operator accepted

Side states:
Blocked · Paused · Cancelled · Superseded

Reopening:
returns to the appropriate active state with a reason and new evidence target.
```

Not every type needs every status. A Research item can finish its research lifecycle without passing through “Implemented.” A Decision request is resolved by a linked approved ruling, not by a coding agent’s preference.

**Use built-in fields first:** subject, type, status, priority, assignee, parent, dates, relations, and target version/milestone.

**Additional information only where needed:** qualified intent reference, approved mandate reference, repository/branch/PR reference, evidence reference, and execution checkpoint. Store descriptive detail in the work package; add custom fields only where filtering or validation genuinely needs them.

**Views:** Needs operator decision; Ready; Active by assignee; Blocked with blocker; Awaiting verification; Milestone delivery.

For boards, distinguish a simple board arrangement from a status-changing board: dragging a card on a basic board is not itself proof that the underlying work status changed. Test the selected board behavior. ([OpenProject.org](https://www.openproject.org/docs/user-guide/agile-boards/ "https://www.openproject.org/docs/user-guide/agile-boards/"))

**Version caution:** OpenProject 17.8 changes target-version handling. Existing installations can opt into multiple target versions through a one-way conversion. Do not trigger that conversion merely to run this pilot; inspect the instance’s schema and configuration first.

### K2. Final everyday runbooks

|Role|Routine|
|---|---|
|**Operator**|State goal and boundaries; decide consequential questions; inspect current work visually; accept coherent outcomes rather than every microtask.|
|**Orchestrator**|Retrieve current scope; verify readiness; claim; delegate; reconcile evidence; record checkpoint; continue only within mandate.|
|**Coding agent**|Read bounded instructions and references; modify approved paths; test; return diff, actual results, limitations, and PR reference.|
|**Verifier**|Independently check the current commit against acceptance; distinguish missing implementation, missing proof, and unresolved product meaning.|
|**Administrator**|Maintain access, backups, upgrades, integration health, recovery, and credential revocation.|

---

## L. Remaining operator decisions

Only policy and preference choices remain here. Vendor pricing, actual client compatibility, and effective permissions are **verification tasks**, not matters for you to guess.

For the option labels: **I = impact, E = implementation effort, U = uncertainty, R = risk**, each on a qualitative **01–05** scale. These are decision aids, not measured probabilities.

### Decision 1 — What should the pilot be allowed to prove?

_Question:_ Should OpenProject be evaluated as a replacement operational PM owner, while product meaning and implementation evidence remain in the repository?

_Options:_

**A — Pilot that ownership split, with migration separately gated (I05/E03/U02/R02).**

**B — Keep repository-native operational ownership and evaluate only a read-only visual projection (I02/E02/U01/R01).**

_Recommendation:_ **A.**

_Reasoning:_ B preserves the premise that caused the earlier rejection and is less likely to remove your administrative burden. A tests the actual proposed benefit without granting migration authority prematurely.

_Dependencies:_ Pilot scope, permission tests, artifact-disposition plan.

### Decision 2 — Which deployment/integration tradeoff fits you?

_Question:_ Is the priority managed browser-agent convenience, self-hosted control, or avoiding the native-MCP license cost?

_Options:_

**A — Managed Professional pilot, conditional on an acceptable verified quote (I05/E02/U03/R02).**

**B — Persistent-server Community plus CLI/REST; accept a different browser-chat workflow (I04/E04/U02/R03).**

**C — Persistent-server Professional for control plus native MCP (I05/E04/U02/R03).**

**D — Prefer GitHub Projects if OpenProject’s incremental cost/operation is not justified (I04/E02/U02/R02).**

_Recommendation:_ **A for testing the intended experience; D if its recurring cost is not justified.** Choose B or C because server control is valuable to you—not because self-hosting is assumed to be operationally free.

_Dependencies:_ Exact quote, intended account model, chosen AI-client connection test.

### Decision 3 — How much execution autonomy should be tested?

_Question:_ Once you approve a bounded work item, how far may the agents proceed without returning to you?

_Options:_

**A — Execute within approved scope through implementation and independent verification; retain human merge/acceptance gates during the pilot (I05/E03/U02/R02).**

**B — Require another approval before each implementation task starts (I03/E02/U01/R01).**

**C — Also test policy-based automatic merge after the core pilot passes (I05/E04/U04/R04).**

_Recommendation:_ **A.**

_Reasoning:_ It tests meaningful autonomy without confusing task execution with product or infrastructure authority. B risks preserving the frequent-interruption burden; C should follow evidence from A.

_Dependencies:_ Effective GitHub protections, restricted identities, tested completion boundaries.

### Decision 4 — At what level do you want to accept outcomes?

_Question:_ Should your final acceptance be attached to coherent delivery slices or every internal task?

_Options:_

**A — Accept coherent slices/stories; let independent verification close their internal technical tasks under policy (I05/E02/U02/R02).**

**B — Personally accept every internal task (I02/E02/U01/R01).**

_Recommendation:_ **A**, while keeping full-story acceptance distinct from acceptance of a deliberately partial slice.

_Reasoning:_ In the proposed Rhythm pilot, you can accept the move/undo regression delivery without falsely accepting the unresolved full identity guarantee.

_Dependencies:_ Clear acceptance criteria and the separate Implemented, Verified, and Operator-accepted meanings.

---

## Final recommendation

**OpenProject deserves the pilot under the revised ownership model. It does not yet deserve an unconditional migration or subscription commitment.**

The earlier objection remains correct for an **additional competing tracker**. It is no longer a sufficient reason to reject an application that deliberately replaces operational PM ownership.

The adoption test is therefore concrete:

> **Can you and your agents advance a real Leela workstream, resume across chats, respect your interventions, attach trustworthy evidence, and keep incomplete work honestly incomplete—with less administrative effort than the current model?**

The RHY-08 pilot above tests exactly that. If it passes, its result supports a separately approved ownership cutover. If cost, permissions, recovery, or operator usability fail, GitHub Projects is the strongest bounded fallback—not another round of rebuilding a custom PM system.