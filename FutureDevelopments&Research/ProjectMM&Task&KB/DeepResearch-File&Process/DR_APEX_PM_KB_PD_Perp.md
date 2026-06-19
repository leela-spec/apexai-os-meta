**Short answer**

In this pass I was only able to analyze two sources in depth: CCPM (S1) and Hermes-agent’s skills hub/guard (S13).  
That gives strong, _concrete_ implementation patterns for: project decomposition, dependency graph fields, next‑action / blocked computation, and trust / governance around SKILL.md skills, but not full coverage of all 15 sources or all 20 processes. Below I (1) document those proven options and their trade‑offs, (2) map them to the 20 processes where the evidence is solid, and (3) note clearly where implementations are **missing** and require further repository reads.

---

## 0. Scope status (this pass)

- **Sources fully inspected (≥2 non‑README implementation files)**
    
    - **S1 CCPM**: `skill/ccpm/SKILL.md`, `skill/ccpm/references/structure.md`, `skill/ccpm/references/track.md`.
        
    - **S13 Hermes-agent**: `tools/skills_hub.py`, `tools/skills_guard.py`.
        
- **Sources _not yet_ inspected (no evidence in this pass)**
    
    - S2 Backlog.md, S3 Task Master AI, S4 GSD Core, S5 planning-with-files, S6 OpenClaw, S7 CrewAI skills, S8 llm-wiki, S9 kanban-skill, S10 pm-skills, S11 swarmvault, S12 Imprint, S14 LangGraph, S15 pattern SKILLs.
        
    - For each of these, _no file paths were queried yet_, so I cannot claim any execution options from them in this pass.
        
- **Consequence**
    
    - The options tables below list **only implementations actually present in S1 and S13** (or explicitly described there).
        
    - For any process where neither S1 nor S13 clearly implement it, I mark **“No concrete implementation in S1/S13 (other sources not yet read)”** rather than invent a pattern.
        

If you want, we can run a second research round dedicated to S2–S12, S14 and the S15 patterns, then extend/replace these tables accordingly.

---

## 1. Evidence extracts (used for all options)

## 1.1 CCPM: structure & tracking

**Epic → task decomposition and task schema**

- CCPM’s “Structure” phase converts an epic at `.claude/epics/<name>/epic.md` into **numbered task files** `001.md`, `002.md`, etc. in the same directory.
    
- Each task file has YAML frontmatter fields:
    
    text
    
    `--- name: <Task Title> status: open created: <run: date -u +"%Y-%m-%dT%H:%M:%SZ"> updated: <same as created> github: (will be set on sync) depends_on: [] parallel: true conflicts_with: [] ---`
    
    Plus a Markdown body with sections: Description, Acceptance Criteria, Technical Details, Dependencies, Effort Estimate (Size XS–XL, Hours N), Definition of Done checklist.
    
- **Dependency logic** (explicit rules):
    
    - `depends_on`: list of task numbers that must complete before this task can start.
        
    - `parallel: true`: task can run concurrently with others it does not conflict with.
        
    - `conflicts_with`: tasks touching the same files and therefore cannot run in parallel.
        
    - Circular dependencies are treated as an error.
        

**Next‑action / blocked / status scripts**

- CCPM’s SKILL declares a **script‑first rule**: deterministic operations like status, standup, “what’s next”, “what’s blocked” must be executed via bash scripts in `references/scripts/`, not re‑implemented by the LLM.
    
- Track reference maps user intents to specific scripts:
    
    - `status.sh`: project status — active epics, open issues count, recent activity.
        
    - `standup.sh`: standup report — completed yesterday, in progress today, blockers.
        
    - `epic-list.sh`, `epic-show.sh <name>`, `epic-status.sh <name>` — epic registry and per‑epic state.
        
    - `prd-list.sh`, `prd-status.sh` — PRD registry and status.
        
    - `search.sh "<query>"` — searches local task files, PRDs, epics.
        
    - `in-progress.sh` — what’s in progress.
        
    - `next.sh` — “Shows highest‑priority open tasks with no blocking dependencies.”
        
    - `blocked.sh` — what’s blocked.
        
    - `validate.sh` — “frontmatter consistency, orphaned files, missing GitHub links, dependency integrity.”
        
- These scripts are expected to be run from the **project root** (where `.claude/` lives), with paths resolved via `<skill_path>/references/scripts/*.sh` or a project‑local `ccpm/scripts/pm/*.sh` layout.
    

**Plan phase (capture project / PRD / epic)**

- The SKILL defines **Plan** as phase 1: “Capture requirements”. It covers “Writing PRDs through guided brainstorming, converting PRDs to technical epics” with instructions in `references/plan.md` (not yet read in this pass).
    
- The “Plan” phase is invoked whenever the user is defining a new feature or scope (“I want to build X”, “create a PRD for X”).
    
- This suggests a **SKILL‑only, LLM‑reasoning‑first implementation** for PM1/PM2 (capture & high‑level decomposition), with scripts entering later for state querying and validation.
    

## 1.2 Hermes-agent: SKILL metadata, trust, and governance

**Skill metadata & discovery**

- `tools/skills_hub.py` defines a **SkillMeta** dataclass with `name`, `description`, `source`, `identifier`, `trust_level`, `repo`, `path`, `tags`, `extra`.
    
- Skills can be discovered via multiple **source adapters**: GitHubSource (via contents API), SkillsShSource, ClawHubSource, ClaudeMarketplaceSource, LobeHubSource, BrowseShSource, OptionalSkillSource, WellKnownSkillSource, HermesIndexSource.
    
- For GitHub:
    
    - `GitHubSource.inspect` fetches `SKILL.md`, parses YAML frontmatter (via `_parse_frontmatter_quick`), and extracts fields like `name`, `description`, and tags (either from `metadata.hermes.tags` or top-level `tags`).
        
    - `GitHubSource.fetch` downloads all files under a skill directory, requiring `SKILL.md` to exist, returning a `SkillBundle` with `files` (relative path → content) and `trust_level` derived from the hosting repo.
        

**Trust system & skills guard**

- `tools/skills_guard.py` defines `TRUSTED_REPOS` (openai/skills, anthropics/skills, huggingface/skills, NVIDIA/skills) and `INSTALL_POLICY` mapping trust level (`builtin`, `trusted`, `community`, `agent-created`) and scan verdict (`safe`, `caution`, `dangerous`) to allow/block decisions.
    
- `scan_skill` performs:
    
    - Structural checks: file count, total size, large files, binary extensions, symlinks, suspicious executables.
        
    - Regex scanning for categories: exfiltration, injection, destructive, persistence, network, obfuscation, supply chain, privilege escalation, credential exposure, etc.
        
    - Invisible Unicode detection in SKILL content.
        
- `should_allow_install` consults `INSTALL_POLICY` and the verdict to decide allow/ask/block; community skills with dangerous verdicts are blocked even under `--force`.
    

**Hub lock, quarantine, and install**

- `HubLockFile` manages `skills/.hub/lock.json`, tracking for each installed skill: source, identifier, trust_level, scan_verdict, content hash, install_path, files, metadata, timestamps.
    
- `quarantine_bundle` writes downloaded `SkillBundle` files under `.hub/quarantine/<skill_name>`, normalizing paths and forbidding path traversal.
    
- `install_from_quarantine` moves a scanned skill to `~/.hermes/skills/<category>/<skill_name>`, enforcing:
    
    - `install_path` is relative and ends with `<skill_name>` via `_normalize_lock_install_path` and `_resolve_lock_install_path` to prevent `rmtree` escapes.
        
    - No symlinks inside the skill directory (rejects skills containing symlinks before install).
        
    - Lock file update and audit log append with action `INSTALL`, source, trust_level, and content hash.
        

This gives an explicit pattern for **governance processes**: trust‑aware install, structural validation, and audit logging of skills.

---

## 2. Per‑process options (from S1 + S13 only)

For each process, I list options that are **explicitly present** in CCPM or Hermes. If no clear implementation exists in these sources, the table states that explicitly.

## Legend

- **Token cost**:
    
    - Low: ≤ 500 tokens (simple script call or short instructions).
        
    - Medium: 500–2000 tokens.
        
    - High: > 2000 tokens.
        
- **Complexity**:
    
    - Low: trivial call or simple frontmatter.
        
    - Medium: multiple scripts / fields but localized.
        
    - High: multi‑component behaviour.
        

---

## PM1 — Capture project

**What it does:** Capture a project’s name, goal, domain, state, and success criteria as a PRD/epic.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. PRD + epic via Plan phase|CCPM SKILL|Use Plan phase (“Capture requirements”) to guide writing a PRD and converting it into a technical epic file under `.claude/epics/<name>/epic.md`, following conventions in `references/plan.md` (not yet read) and overall CCPM SKILL description.|Medium – LLM‑driven PRD drafting and epic synthesis.|Low – edit SKILL.md and plan reference text; no compiled code.|Medium – multi‑step guided brainstorming and transformation, but all within SKILL instructions.|No – CCPM treats this as reasoning work for the LLM, not a deterministic script.|Yes – all file operations are local Markdown in the repo.|
|2. No direct implementation in Hermes|Hermes skills_hub/guard|Hermes focuses on skill discovery and security; it does not define a project PRD/epic capture workflow.|–|–|–|–|–|

---

## PM2 — Decompose project

**What it does:** Break project/epic into epics/chunks/tasks with explicit splitting rules.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Epic → numbered task files|CCPM structure|Use `Structure — Break Down an Epic`: read `.claude/epics/<name>/epic.md`, analyze for parallelism, and create numbered task files `001.md`, `002.md`, etc. with standard task frontmatter and body sections.|Medium – LLM reads epic, drafts multiple tasks, fills structured sections.|Low – adjust SKILL instructions and template; no external code.|Medium – includes parallelization strategy by epic size and optional subagent orchestration, but all described textually.|No – decomposition is LLM‑reasoning; only optional Task subagents, not external scripts.|Yes – uses local Markdown files and `.claude/` tree.|
|2. No direct decomposition pattern in Hermes|Hermes skills_hub/guard|Hermes metadata is per‑skill, not per project/epic; there is no epic decomposition workflow.|–|–|–|–|–|

---

## PM3 — Assign dependencies

**What it does:** Build a `depends-on` / `unlocks` graph among tasks.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Frontmatter–defined DAG fields|CCPM structure|Use task frontmatter fields: `depends_on` (list of prerequisite task numbers), `parallel` (can run with non‑conflicting tasks), `conflicts_with` (tasks that cannot run in parallel due to file overlap). Dependency rules explicitly forbid cycles.|Low–Medium – LLM writes arrays based on epic analysis; no heavy computation.|Low – if logic changes, update textual rules in `structure.md`; file format is stable.|Medium – encodes DAG semantics in fields but leaves graph processing to later scripts.|No – the graph is represented declaratively via YAML; no separate graph‑building script is mandated.|Yes – pure Markdown/YAML in repo.|
|2. No explicit task dependency graph in Hermes|Hermes skills_hub/guard|Hermes tracks dependencies at _skill_ install level (e.g., scanning, trust) but not intra‑project task graphs.|–|–|–|–|–|

---

## PM4 — Compute next action

**What it does:** From current state and dependency graph, determine what to do next.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Scripted `next.sh` over task DAG|CCPM track|`next.sh` script, run as `bash references/scripts/next.sh`, “Shows highest‑priority open tasks with no blocking dependencies.” It operates on task frontmatter (`status`, `depends_on`, etc.) under `.claude/epics/`.|Low – single shell invocation, tiny LLM wrapper to interpret output.|Medium – task selection logic lives in shell; changing criteria means editing script logic.|Medium – must parse YAML or filenames, evaluate dependency closure, and possibly priority rules; but contained in one script.|**Yes** – explicitly mandated by CCPM: tracking operations should use the script, not be recomputed by the LLM.|Yes – scripts run locally on repo; no SaaS or external DB.|
|2. No generic next‑action engine in Hermes|Hermes skills_hub/guard|Hermes has no concept of per‑task next‑action; it focuses on skill installation and security, not PM task selection.|–|–|–|–|–|

---

## PM5 — Detect blockers

**What it does:** Identify items that cannot proceed.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Scripted `blocked.sh` over task statuses and dependencies|CCPM track|`blocked.sh`, run as `bash references/scripts/blocked.sh`, is mapped to queries like “what’s blocked”, “any blockers” and returns blocked items. It operates over the same task DAG and statuses as `next.sh`.|Low – one script call.|Medium – to adjust what “blocked” means, you edit the script.|Medium – must detect tasks where `status` is open but `depends_on` contain incomplete tasks or conflicts.|**Yes** – again explicitly categorized as a tracking operation that should run via script.|Yes – shell script over local files.|
|2. Standup‑based blocker reporting|CCPM track|`standup.sh` shows “what was completed yesterday, what’s in progress today, any blockers”, so “blocked” items also surface indirectly in the standup script output.|Low|Medium|Medium|Yes – same script rule.|Yes|

---

## PM6 — Update status

**What it does:** Mark items complete after work finishes.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Not explicitly defined in inspected CCPM files|CCPM SKILL/refs|The inspected CCPM files reference _reading_ statuses (e.g., `status: open`, epic “completed” check, and status/standup scripts) but do not specify the concrete mechanism for writing status transitions (`open` → `completed`) in the task/epic frontmatter.|–|–|–|–|–|
|2. Not covered in Hermes|Hermes skills_hub/guard|Hermes governs SKILL installation, not per‑task status updates in a project.|–|–|–|–|–|

---

## PM7 — Detect stall

**What it does:** Find items that have not progressed across multiple sessions.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Not explicitly present|CCPM|Track docs mention “recent activity” and standup, but do not define a specific “stalled item” computation (e.g., based on `updated` timestamps).|–|–|–|–|–|
|2. Not present|Hermes|No stall‑detection logic for project tasks.|–|–|–|–|–|

---

## PM8 — Generate work registry

**What it does:** Produce a compact index of all project state.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Status / list scripts as registry views|CCPM track|`status.sh` (project status), `epic-list.sh`, `epic-status.sh <name>`, `prd-list.sh`, `prd-status.sh`, `in-progress.sh`, `search.sh "<query>"` together act as pre‑defined registry views over the `.claude/` epics, PRDs, and tasks.|Low – each run is a short shell command; LLM mainly passes through output.|Medium – changing registry structure means editing multiple scripts in `references/scripts/`.|Medium–High – distributed across several scripts but each is single‑purpose.|**Yes** – CCPM explicitly treats these as script‑first operations.|Yes – shell over local files.|
|2. No project registry in Hermes|Hermes skills_hub/guard|Hermes lockfile (`skills/.hub/lock.json`) and taps maintain a _skills_ registry (installed skills, their provenance, hashes) but not a PM “work registry” for a specific project.|–|–|–|–|–|

---

## KB1 — Write session progress

**What it does:** Capture what happened during a work session.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Standup / status output as narrative log|CCPM track|`standup.sh` and `status.sh` produce textual summaries of work done (“what was completed yesterday, what’s in progress today, any blockers”), which can be appended to a Markdown session log by the LLM, though CCPM does not prescribe a specific session log file schema.|Low–Medium – scripts plus short narrative wrapping by LLM.|Medium – change script output shape, not SKILL.|Medium – requires out‑of‑band convention for log files.|Yes (for generating the snapshot), No (for where/how to store it – that part is LLM text)|Yes|

No direct, schema‑defined “session progress” entity is present in the inspected files; this is an inferred usage of scripts, so it’s weaker evidence.

---

## KB2 — Extract state deltas

**What it does:** Convert a session narrative into structured field changes.

- **No explicit implementation** in S1 or S13: CCPM shows _semantic meaning_ of fields (e.g., `status`, `depends_on`), and `validate.sh` checks integrity, but there is no script or SKILL description for automatic diffing from narrative text to frontmatter changes.
    

---

## KB3 — Maintain entity files

**What it does:** Apply deltas safely to Markdown files without data loss.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Direct edit of task/epic Markdown|CCPM structure & conventions|CCPM uses Markdown files with structured frontmatter for epics and tasks; the LLM is expected to create and edit these following the documented schemas, but there is no separate merge/patch script to ensure conflict‑free updates.|Medium – LLM has to read and rewrite Markdown blocks.|Low – schemas defined textually; no code to maintain.|Medium – safe edits require careful prompting, but not enforced in code.|No – no deterministic patch tool is mandated.|Yes|

---

## KB4 — Rebuild index

**What it does:** Regenerate registry after state changes.

- In CCPM, registry views are computed on demand by scripts (`status.sh`, `epic-list.sh`, `prd-list.sh`, `search.sh`), not via persistent indices. Rebuilding the “index” is equivalent to **rerunning these scripts**, which is already covered under PM8.
    
- Hermes has a centralized skills index for skills themselves, but that is not per‑project.
    

---

## KB5 — Detect drift

**What it does:** Compare current state vs last session to find divergence.

- Neither CCPM nor Hermes define a project‑level drift detection mechanism (e.g., comparing snapshots of `.claude/` trees over time). CCPM’s `validate.sh` checks consistency (frontmatter, dependency integrity, missing links) at a single point in time, not temporal drift.
    

---

## KB6 — Produce next-session context

**What it does:** Generate a handoff document for the next Claude session.

- CCPM gives the ingredients (status, standup, blocked/next scripts) and task/epic files; the SKILL suggests using ccpm “any time the user is talking about shipping a feature, managing work, or tracking progress”, but it does not define a specific “handoff packet” format between sessions.
    
- Hermes has no per‑project context handoff; it only persists SKILL installations and scans.
    

---

## PD1 — Score priority

**What it does:** Assign a numeric priority value.

- CCPM’s `next.sh` script chooses “highest‑priority open tasks” but the priority logic is not described in the inspected files (no explicit `priority` field, only `Size: XS/S/M/L/XL` and `Hours: N` in the task body). Without the script source, we cannot say whether numeric priority exists or how it is computed.
    
- Hermes does not define numeric priority for tasks or skills beyond trust levels.
    

---

## PD2 — Score urgency

**What it does:** Assess time sensitivity separately from priority.

- No explicit urgency model is present in S1 or S13. Task templates mention “Hours: N” but not deadlines or urgency fields.
    

---

## PD3 — Compute unlock depth

**What it does:** Count how many items become unblocked when this one completes.

- CCPM has the prerequisite structure (`depends_on`) but no script or documented algorithm for _unlock depth_ is described in the inspected files.
    
- Hermes has no notion of unlock depth for tasks.
    

---

## PD4 — Synthesize focus recommendation

**What it does:** Produce a ranked focus list with reasoning.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. LLM reasoning on top of `next.sh` output|CCPM SKILL + track|CCPM suggests using the LLM for synthesis (standups, explanations) while deterministic selection comes from scripts. A natural pattern is: run `next.sh` to get candidate tasks, then have the LLM synthesize a human‑readable, ranked focus list explaining why each is next, using task descriptions and dependencies.|Medium – script output plus reasoning text.|Low–Medium – change reasoning prompts in SKILL; scripts stay stable.|Medium – composition of deterministic and reasoning layers, but both are simple in isolation.|Partially – script for selection, SKILL for explanation.|Yes|

This is not a separate implementation but a composition of documented CCPM behaviours.

---

## PD5 — Validate with operator

**What it does:** Present a human gate before any state mutation is written.

|Option|Source|Mechanism|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|1. Manual operator gating (implied)|CCPM|CCPM explicitly separates deterministic scripts (read‑only status/validation) from reasoning operations (writing PRDs, epics, tasks). Scripts like `validate.sh` check state and present results, but any mutation (editing files, pushing to GitHub) is done by the operator or via explicit LLM actions; there is no automatic write without user prompts.|Low – show script output and ask operator what to do.|Low – gating logic is in conversation, not code.|Low–Medium|No|Yes|
|2. Trust‑aware skill install gate|Hermes skills_guard|Before installing a SKILL, Hermes runs `scan_skill` and passes the result to `should_allow_install`; community skills with dangerous verdicts are blocked, and agent‑created skills may return “NEEDS CONFIRMATION” requiring an explicit user decision.|Low – one scan call, short report.|Medium – maintain regex patterns and install policy table.|Medium–High – many threat patterns and structural rules.|Yes – Python scanner and policy logic.|Yes – local scans over downloaded skill bundles.|

Option 2 is a **governance‑layer** human gate over skills; conceptually similar to PD5 but applied to SKILL install rather than project tasks.

---

## PD6 — Feed planning layer

**What it does:** Hand off ranked context to a daily planning skill.

- CCPM describes “Plan” vs “Track” and provides `next.sh`, `blocked.sh`, `in-progress.sh`, `status.sh`, and standup scripts whose outputs form a natural input to a planning layer, but there is no explicit SKILL that accepts those as a contract.
    
- Hermes’s skills hub can discover and install planning SKILLs from multiple sources, but the handoff contract is per‑SKILL and not defined centrally in `skills_hub.py`.
    

---

## 3. Sub‑skill grouping (based on S1 + S13 only)

## 3.1 Natural clusters

From CCPM and Hermes we can see these clusters:

1. **Decomposition + dependency modelling**
    
    - Processes: PM2, PM3, partially PM1 and KB3.
        
    - Shared context: `.claude/epics/<name>/epic.md` and numbered task files in the same directory; fields `name`, `status`, `created`, `updated`, `github`, `depends_on`, `parallel`, `conflicts_with`, plus body sections.
        
    - Trigger: “turn the X PRD into an epic” / “break down the X epic into tasks”.
        
2. **Tracking + registry views**
    
    - Processes: PM4, PM5, PM8, KB4, partially KB1.
        
    - Shared context: same task/epic/PRD files plus scripts under `references/scripts/*.sh` (`status.sh`, `standup.sh`, `epic-*`, `prd-*`, `search.sh`, `in-progress.sh`, `next.sh`, `blocked.sh`, `validate.sh`).
        
    - Trigger: status queries (“what’s our status”, “standup”, “what’s next”, “what’s blocked”, “validate”).
        
3. **Skill governance and safety**
    
    - Processes: PD5 (as governance analogue), part of process governance outside the 20 PM/KM/PD flows.
        
    - Shared context: Hermes hub directories (`~/.hermes/skills`, `.hub/lock.json`, `.hub/quarantine`, `.hub/audit.log`), scan results, macros like `TRUSTED_REPOS`, `INSTALL_POLICY`, and the install/update flows.
        
    - Trigger: installing/updating/uninstalling a SKILL, checking for updates.
        

## 3.2 Implementation modality per cluster

- **Cluster 1 (Decomposition + dependency) — SKILL‑only**
    
    - CCPM’s decomposition and dependency schema are fully described textually in `SKILL.md` and `references/structure.md`; no external code is required beyond normal file I/O.
        
    - **Implementation type:** Pure SKILL.md instructions running in Claude Code, with local file edits.
        
- **Cluster 2 (Tracking + registry) — Script‑required**
    
    - CCPM explicitly mandates that tracking operations (status, standup, next, blocked, validate, etc.) call the bash scripts in `references/scripts/` instead of recomputing in the LLM.
        
    - **Implementation type:** SKILL.md orchestrating **shell scripts** (bash) for deterministic reads; scripts are the canonical source of truth.
        
- **Cluster 3 (Skill governance and safety) — Python scripts required**
    
    - Hermes’s trust system, scanning, install/update, and unified search are implemented in Python modules `tools/skills_hub.py` and `tools/skills_guard.py` plus associated code; they cannot be re‑implemented reliably as pure SKILLs.
        
    - **Implementation type:** Python scripts and libraries; SKILLs may call these via tools but do not replace them.
        

## 3.3 Reuse of open‑source SKILLs (from S1/S13 only)

- **Cluster 1:** CCPM’s decomposition patterns (`structure.md`) are directly reusable as a base SKILL for Apex, with minimal adaptation to path conventions (still `.claude/epics/...`).
    
- **Cluster 2:** CCPM’s `Track` phase and scripts provide a complete pattern for script‑backed status/registry SKILLs; Apex could adopt the same separation (LLM for explanation, bash for computation).
    
- **Cluster 3:** Hermes’s skills hub and guard provide a base for trust‑aware skill management and process governance around SKILL install/update; Apex could replicate the trust model and scanning approach for its own internal skills.
    

Processes with no concrete pattern yet (e.g., KB2, KB5, PD2, PD3, KB6 as structured packet) would still need designs even after importing these references.

---

## 4. Processes lacking any viable pattern in this pass

Given only S1 and S13 were inspected, the following processes have **no concrete implementation pattern** observed so far:

- **KB2 Extract state deltas** (narrative → structured patches).
    
- **KB5 Detect drift** (temporal divergence).
    
- **KB6 Produce next-session context** (explicit handoff packet format).
    
- **PD1 Score priority** (explicit numeric scoring beyond “highest‑priority open tasks” in `next.sh`).
    
- **PD2 Score urgency** (separate urgency dimension).
    
- **PD3 Compute unlock depth** (quantitative unlock metric over DAG).
    

For these, something would have to be built from scratch or sourced from the yet‑unread repositories (S2–S12, S14, S15).

---

## 5. Interim summary table (S1 + S13 only)

Because I have not yet analyzed S2–S12, S14, S15, this “best source” table is **provisional** and only considers S1 CCPM and S13 Hermes.

|Process ID|Process name|Best source (this pass)|Mechanism (from evidence)|Needs script?|Copy type (relative to source)|Priority rank (given: PM4=1, PM1=27)|
|---|---|---|---|---|---|---|

|Process ID|Process name|Best source (this pass)|Mechanism (from evidence)|Needs script?|Copy type (relative to source)|Priority rank (given: PM4=1, PM1=27)|
|---|---|---|---|---|---|---|
|PM1|Capture project|CCPM|Plan phase: PRD + epic capture in `.claude/epics/<name>/epic.md` guided by SKILL.|No|ADAPT – keep PRD→epic flow, adapt fields/paths|27|
|PM2|Decompose project|CCPM|`structure.md` epic decomposition into numbered tasks with frontmatter and sections.|No|FULL – template and rules can be reused nearly verbatim|(not specified; treat as medium)|
|PM3|Assign dependencies|CCPM|`depends_on`, `parallel`, `conflicts_with` fields and dependency rules.|No|FULL – field schema directly reusable|–|
|PM4|Compute next action|CCPM|`next.sh` over task DAG, “highest‑priority open tasks with no blocking dependencies”.|**Yes** (bash)|ADAPT – copy script pattern, adapt path layout|1|
|PM5|Detect blockers|CCPM|`blocked.sh` + `standup.sh` for blocked items.|Yes|ADAPT|–|
|PM6|Update status|–|No explicit pattern in S1/S13.|–|CONCEPT – must be designed|–|
|PM7|Detect stall|–|No explicit stall detection in S1/S13.|–|CONCEPT|–|
|PM8|Generate work registry|CCPM|Status/list/search scripts over `.claude/` tree as on‑demand registry views.|Yes|ADAPT|–|
|KB1|Write session progress|CCPM|Use `standup.sh`/`status.sh` outputs as session summaries; logging convention not specified.|Yes (for snapshot), No (for where stored)|CONCEPT|–|
|KB2|Extract state deltas|–|Not implemented in S1/S13.|–|CONCEPT|–|
|KB3|Maintain entity files|CCPM|Direct edit of Markdown task/epic files with frontmatter schemas.|No|FULL – schema and sections reusable|–|
|KB4|Rebuild index|CCPM|Recompute via status/list/search scripts; no persistent index.|Yes|ADAPT|–|
|KB5|Detect drift|–|No explicit drift mechanism.|–|CONCEPT|–|
|KB6|Next-session context|–|No structured handoff packet defined; would need to combine existing views.|–|CONCEPT|–|
|PD1|Score priority|–|Priority logic not visible (script internals absent).|–|CONCEPT|–|
|PD2|Score urgency|–|No urgency field.|–|CONCEPT|–|
|PD3|Compute unlock depth|–|DAG present but no unlock metric.|–|CONCEPT|–|
|PD4|Focus recommendation|CCPM|Combine `next.sh` output + LLM reasoning on task bodies/dependencies.|Partially (script + SKILL)|ADAPT|–|
|PD5|Validate with operator|Hermes + CCPM|Hermes scan + `should_allow_install` for skill install gate; CCPM scripts for project validation with human decision.|Yes (Hermes), No (operator gating)|ADAPT (governance pattern)|–|
|PD6|Feed planning layer|CCPM|Use status/next/blocked outputs as planning layer inputs, but no explicit skill contract yet.|Yes (for data), No (for contract)|CONCEPT|–|

---

If you’d like to proceed, the next logical step is a **second research round** focused on S2–S12, S14, and the S15 patterns to (a) add more implementation options per process and (b) replace “CONCEPT” entries with concrete SKILL.md or script patterns from those repositories.