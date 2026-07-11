# Apex Alfred Orchestration Research Reference

The uploaded brief established the baseline design choices and known gaps that this document validates, deepens, and corrects where the current public record disagrees. fileciteturn0file0

Two findings materially affect the implementation plan. First, your **four permanent profiles** are directionally aligned with current Claude Code practice, but the research strongly suggests keeping those roles as the **stable control plane** and using **ephemeral subagents or dynamic workflows** for burst specialization rather than adding more permanent profiles. Anthropic’s current guidance repeatedly favors small teams, clear boundaries, and isolated context over large fixed agent rosters. citeturn2view1turn43view0turn46view0turn42view1

Second, one item in the known state needs a precise correction. **GitHub Actions remains a valid event bus**, but the **official Anthropic Claude Code GitHub Action is not subscription-only**: Anthropic’s own setup documentation is built around `ANTHROPIC_API_KEY` or cloud-provider credentials, while remote Claude Code **Routines** remain in research preview as of June 2026. In parallel, Claude Code now also has **Desktop local scheduled tasks**, but they only run while the app is open and the machine is awake, so they do not replace a production-grade scheduler. In practice, this means your subscription-only architecture should treat **Hermes cron or another self-hosted scheduler as the primary executor**, and use GitHub Actions for repository events, gating, and dispatch into self-hosted runtime—not as a drop-in way to run Claude Max in GitHub-hosted CI via Anthropic’s official action. citeturn51view0turn50view4turn50view5turn50view0turn50view2

## Validated Source List

The table below prioritizes official Anthropic documentation as ground truth for Claude Code behavior, then the official Agent Skills standard, GitHub’s official workflow documentation, and finally practitioner and research sources for operational patterns and failure modes. Where Anthropic pages are live docs without a visible publish stamp, they are marked as **undated live docs** and treated as current as of June 13, 2026. citeturn52view5turn14view0turn39view1

| Title | URL | Publish date | Why it is authoritative | Key claim relevant to Apex Alfred |
|---|---|---:|---|---|
| Claude Code Docs — How Claude remembers your project | `https://code.claude.com/docs/en/memory` | Undated live doc | Official Anthropic documentation for persistent project instructions and rule-loading behavior. | Claude Code reads `CLAUDE.md`, **not** `AGENTS.md`; it recommends keeping `CLAUDE.md` under 200 lines, using path-scoped rules when it grows, and importing `AGENTS.md` when you want cross-tool reuse. citeturn4view0turn49view1turn49view0turn49view2 |
| Claude Code Docs — Agent Teams | `https://code.claude.com/docs/en/agent-teams` | Undated live doc; feature introduced Feb 5, 2026 in changelog | Official Anthropic documentation for multi-session coordination. | Agent teams use a shared task list with self-coordination, work best when teammates can operate independently, are experimental, and currently have limits such as no nested teams, lagging task status, and fixed lead ownership. citeturn43view0turn43view1turn43view2turn13view0 |
| Claude Code Docs — Extend Claude with skills | `https://code.claude.com/docs/en/skills` | Undated live doc | Official Anthropic documentation for skills. | Claude Code skills follow the Agent Skills open standard; `SKILL.md` should stay concise, ideally under 500 lines, and can run inline or in isolated subagent context. citeturn2view4turn7view0turn7view2turn7view7 |
| Claude Code Docs — Extend Claude Code | `https://code.claude.com/docs/en/features-overview` | Undated live doc | Official Anthropic decision guide for choosing between CLAUDE.md, skills, subagents, agent teams, hooks, and plugins. | Anthropic explicitly says to start with `CLAUDE.md`, then add other extensions only as concrete triggers appear; it also distinguishes subagents from agent teams and frames teams as higher-cost coordination with shared tasks. citeturn8view0turn43view3 |
| Claude Code Docs — Explore the `.claude` directory | `https://code.claude.com/docs/en/claude-directory` | Undated live doc | Official Anthropic file-layout reference. | `.claude/skills/`, `.claude/agents/`, `.claude/workflows/`, and `settings.json` are the canonical project artifact locations; most users only need `CLAUDE.md` and `settings.json` first, then add the rest as needed. citeturn44view0turn44view1turn44view2turn44view4turn44view5 |
| Claude Code Docs — Dynamic Workflows | `https://code.claude.com/docs/en/workflows` | Undated live doc; requires v2.1.154+ | Official Anthropic documentation for script-based orchestration. | Dynamic workflows are now a first-class native Claude Code orchestration mechanism on paid plans; they move orchestration logic into code, can scale to dozens or hundreds of agents, and live in `.claude/workflows/`. citeturn46view0 |
| Claude Code Docs — Routines | `https://code.claude.com/docs/en/routines` | Undated live doc | Official Anthropic documentation for cloud scheduling. | Routines are still in **research preview** and can run on schedules, API calls, or GitHub events; GitHub triggers are configured from the web UI only. citeturn2view6turn50view3turn50view4turn50view5 |
| Claude Code Docs — Desktop scheduled tasks | `https://code.claude.com/docs/en/desktop-scheduled-tasks` | Undated live doc | Official Anthropic documentation for local scheduling. | Claude Code Desktop now supports local scheduled tasks, but they only run while the Desktop app is open and the computer is awake, making them unsuitable as the primary production scheduler for always-on orchestration. citeturn50view0turn50view1turn50view2 |
| Claude Code Docs — GitHub Actions | `https://code.claude.com/docs/en/github-actions` | Undated live doc | Official Anthropic documentation for CI/CD integration. | Anthropic’s official GitHub Action is configured around `ANTHROPIC_API_KEY` or cloud-provider backends, which means it is **not** a strict subscription-only path by itself. citeturn51view0 |
| Claude Code changelog | `https://code.claude.com/docs/en/changelog` | Feb–Apr 2026 entries used | Official Anthropic release record. | On Feb 5, 2026, Anthropic added research-preview agent teams; on Feb 6, 2026, it added `TaskCompleted` and `TeammateIdle` hooks plus agent memory frontmatter, which matter directly for orchestration and quality gating. citeturn13view0 |
| Agent Skills — Overview | `https://agentskills.io/home` | Undated live doc | Official documentation for the Agent Skills open standard. | Agent Skills are a lightweight portable folder format centered on `SKILL.md`, designed for cross-product reuse and progressive disclosure. citeturn14view0 |
| Agent Skills — Best practices for skill creators | `https://agentskills.io/skill-creation/best-practices` | Undated live doc | Official best-practice guidance for the open standard Anthropic uses. | Useful skills come from real project artifacts and real execution traces, not generic prompting; they should be moderately detailed, structured with progressive disclosure, and include gotchas, checklists, templates, and validation loops where needed. citeturn15view0 |
| Agent Skills — Optimizing descriptions | `https://agentskills.io/skill-creation/optimizing-descriptions` | Undated live doc | Official guide to improving skill activation quality. | Skill descriptions should be empirically tuned against should-trigger and should-not-trigger queries to reduce false activations and missed activations. citeturn16view3 |
| Agent Skills — Evaluating skill output quality | `https://agentskills.io/skill-creation/evaluating-skills` | Undated live doc | Official eval methodology for skills. | Skills should be iterated through prompt/output test cases, assertions, transcript review, and human review; the standard explicitly recommends eval-driven iteration. citeturn16view6 |
| Shipyard — Claude Code Subagents Quickstart | `https://shipyard.build/blog/claude-code-subagents-guide/` | Mar 6, 2026 | Practitioner guide from a company shipping agent-friendly developer infrastructure. | Practical subagent advice aligns with Anthropic’s context-isolation story: start subagents one by one, keep the roster small, and rely on specialization only where it improves outcomes. citeturn25view0turn42view0turn42view1 |
| EffiFlow — Multi-Agent Orchestration: Routing Design | `https://jangwook.net/en/blog/en/multi-agent-orchestration-routing/` | Feb 9, 2026 | Useful practitioner source focused on orchestration strategy rather than product marketing. | Routing is the hard part; role boundaries, escalation paths, and feedback loops matter more than simply adding more agents. citeturn25view1turn42view3turn42view6 |
| Configuring Agentic AI Coding Tools: An Exploratory Study | `https://arxiv.org/abs/2602.14690` | Feb 16, 2026 | Primary research on real-world repository configuration patterns across tools. | Context files dominate, AGENTS.md is emerging as the cross-tool standard, and Claude Code repos use the broadest range of mechanisms—but advanced skills/subagents remain shallowly adopted in practice. citeturn47view0turn47view1turn47view2turn47view3 |
| Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code's Auto Mode | `https://arxiv.org/abs/2604.04978` | Apr 4, 2026 | Primary research on Claude Code permission behavior under ambiguous state-changing tasks. | Auto mode is useful but should not be treated as a complete safety boundary for ambiguous or stateful operations; in adversarial ambiguity tests, many dangerous in-project edits fell outside the classifier’s scope. citeturn48view3turn48view4 |
| Towards Secure Agent Skills | `https://arxiv.org/abs/2604.02837` | Apr 2026 | Primary security analysis of the Agent Skills ecosystem. | Skill trust can be over-broad because instructions and executable resources coexist in a single package, with a persistent trust model after installation. citeturn48view5turn48view6 |
| Channel Fracture | `https://arxiv.org/abs/2606.04896` | Jun 3, 2026 | Primary research focused directly on Hermes Agent cron/memory behavior. | Hermes-style scheduled contexts can silently fail to write cross-agent memory because cron execution may be isolated from the memory layer; receiver-side delivery verification is essential. citeturn48view0turn48view1turn48view2 |

## Step-by-Step Build Order

The order below is the one most strongly supported by the evidence and by Claude Code’s own extension hierarchy. The central principle is: **define the narrowest durable contracts first, then let Claude generate the executable artifacts from those contracts**. Anthropic’s own guidance says to start with `CLAUDE.md`, add other extensions only as specific triggers arise, and separate research/planning from execution; the open Agent Skills guidance says skills work best when grounded in real artifacts and tested iteratively. Your required `AGENTS.md → CLAUDE.md → settings → schemas → skills → board → workflows → first runnable skill → CI skeleton` sequence is therefore correct **if** `AGENTS.md` is treated as the shared cross-tool contract and `CLAUDE.md` is the Claude adapter that imports it. citeturn8view0turn5view2turn15view0turn16view6

**Step 1: `AGENTS.md`**

**What it is.** Your cross-tool, human-readable operating contract. This belongs first because current research finds `AGENTS.md` emerging as the most interoperable context-file standard across tools, even when tools also use their own native file names. citeturn47view0turn47view1

**Why it must come before later steps.** If you define profiles, responsibilities, artifact names, and escalation rules here first, every later Claude-native file can be an adapter rather than an independent source of truth. That sharply reduces instruction drift. citeturn47view1turn49view5

**Exact format/content it must contain.** It should contain only the permanent contract: mission, the four permanent profiles, role boundaries, allowed artifact locations, naming conventions, packet lifecycle, escalation policy, and done criteria. Do **not** put long procedures here; the Agent Skills standard and Anthropic docs both push task procedures into skills or scoped rules instead. citeturn49view2turn15view0

**Minimum viable template**
```md
# Apex Alfred Core Contract

## Mission
Operate a subscription-only agent orchestration system using Claude-first artifacts and a Hermes-compatible runtime.

## Permanent Profiles
- Alfred: intake, routing, packet creation, task assignment
- meta_operations: workflow execution, packaging, artifact assembly
- meta_strategist: prioritization, decomposition, sequencing
- meta_detective_controller: validation, drift detection, contradiction checks

## Boundaries
- Alfred does not perform deep implementation work.
- meta_strategist does not package final deliverables.
- meta_operations does not change priorities without escalation.
- meta_detective_controller can veto completion but does not own delivery packaging.

## Canonical Artifact Names
- handoff packet: `handoff_packet`
- task board: `tasks.json`
- workflow spec: `workflow_def`
- validation report: `verification_report`

## Finish Conditions
A task is done only when:
1. deliverables exist at declared paths
2. verification criteria pass
3. downstream handoff packet is written or task is marked terminal
```

**Step 2: `CLAUDE.md`**

**What it is.** Claude Code’s native persistent project instruction file. Official Anthropic docs are explicit: Claude Code reads `CLAUDE.md`, not `AGENTS.md`. citeturn49view2

**Why it must come before later steps.** It is the file Claude loads every session, so it must exist before asking Claude to generate any skills, subagents, or workflows. Anthropic’s own extension guide says to start here. citeturn8view0turn49view2

**Exact format/content it must contain.** Keep it thin. Import `AGENTS.md`, then add only Claude-specific rules such as when to use plan mode, which artifacts live in `.claude/`, what paths are writable, and what verification signal must exist before task completion. Anthropic recommends targeting under 200 lines and moving conditional detail into rules or skills. citeturn49view1turn49view0

**Minimum viable template**
```md
@AGENTS.md

## Claude Code Adapter
- Always read and write orchestration artifacts under the canonical paths in this repo.
- Use plan mode before changing schemas, workflows, or settings.
- Prefer skills for repeatable procedures and workflows for large fan-out orchestration.
- Never treat runtime files under ~/.claude/teams or ~/.claude/tasks as canonical state.
- A task is not complete until a verification report exists.
```

That import pattern is the exact Anthropic-supported bridge between `AGENTS.md` and `CLAUDE.md`. citeturn49view2

**Step 3: `.claude/settings.json`**

**What it is.** The project-level configuration layer for permissions, hooks, environment values, and model defaults. Anthropic identifies `settings.json` as one of the two files most users should establish first. citeturn44view0turn44view4

**Why it must come before later steps.** Without the permission and hook policy, Claude may scaffold skills or workflows that can touch the wrong files, leak secrets, or bypass validation gates. Also, some settings—such as repository-level `auto` mode—have product constraints you need to understand before relying on them. citeturn2view7turn2view8turn5view8

**Exact format/content it must contain.** At minimum: `permissions.deny` for secrets and protected state, `env` entries used by workflows, and hook stubs for validation checkpoints. Anthropic explicitly recommends `permissions.deny` for sensitive files, and `PreToolUse` hooks when a rule must actually be enforced rather than merely requested. citeturn2view8turn5view8turn49view2

**Minimum viable template**
```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Write(./state/runtime/**)"
    ]
  },
  "env": {
    "APEX_STATE_DIR": "./state",
    "APEX_SCHEMA_DIR": "./schemas"
  },
  "hooks": {
    "TaskCompleted": [
      {
        "type": "command",
        "command": "scripts/check-task-completion.sh"
      }
    ]
  }
}
```

One Anthropic-specific nuance belongs in your implementation notes: **project-level** `.claude/settings.json` cannot grant repository-wide `auto` mode, because Anthropic ignores that setting there to prevent untrusted repos from self-elevating. citeturn2view7

**Step 4: `schemas/`**

**What it is.** The canonical machine contracts for the control plane. This is where you should lock the packet, task, workflow-input, workflow-output, and verification-report structures **before** generating skills or workflows. That exact “schemas before code” sequence is a synthesis from Anthropic’s “explore first, then plan, then code” guidance and the Agent Skills guidance to ground reusable artifacts in concrete project materials, not generic prose. citeturn5view2turn15view0turn16view6

**Why it must come before later steps.** Skills and workflows are easier for Claude to generate once the shape of valid inputs and outputs is already concrete and example-backed. It also fixes your current naming drift problem early. citeturn5view3turn15view0turn49view5

**Exact format/content it must contain.** At minimum:
- `handoff_packet.schema.json`
- `task.schema.json`
- `workflow_def.schema.json`
- `verification_report.schema.json`
- `naming.md` with the canonical field names

**Minimum viable example**
```json
{
  "$id": "handoff_packet.schema.json",
  "type": "object",
  "required": [
    "packet_id", "from_profile", "to_profile", "objective",
    "constraints", "inputs", "deliverables", "verification"
  ],
  "properties": {
    "packet_id": { "type": "string" },
    "from_profile": { "type": "string" },
    "to_profile": { "type": "string" },
    "objective": { "type": "string" },
    "constraints": { "type": "array", "items": { "type": "string" } },
    "inputs": { "type": "array" },
    "deliverables": { "type": "array" },
    "verification": { "type": "array", "items": { "type": "string" } }
  }
}
```

**Step 5: skill definitions**

**What it is.** Reusable procedural units in `.claude/skills/<name>/SKILL.md`. Anthropic and the Agent Skills standard agree that skills are the right place for reusable knowledge and workflows, while project-global standing instructions stay in `CLAUDE.md`. citeturn8view0turn7view2turn14view0

**Why it must come before the task board and workflow code.** Skills are where you encode the stable procedures each profile will invoke repeatedly: packet validation, task triage, verification, packaging, prioritization. If you skip this and jump straight to workflows, you end up hard-coding procedures into orchestration instead of composing them from reusable units. citeturn8view0turn15view0turn16view6

**Exact format/content it must contain.** Each skill should have:
- a narrow `description`
- only the core instructions in `SKILL.md`
- references/examples/scripts in supporting files
- eval cases in `evals/` if the skill is critical
- `disable-model-invocation: true` for high-side-effect actions such as deploy, state mutation, or scheduler writes. citeturn7view3turn15view0turn16view6

**Minimum viable example**
```md
---
description: Validate a handoff packet against the canonical schema and report missing fields, contradictory constraints, and unverifiable completion criteria.
disable-model-invocation: false
allowed-tools: Read Grep Glob Bash
---

## Procedure
1. Read `schemas/handoff_packet.schema.json`.
2. Read the target packet.
3. Check required fields.
4. Check naming against `schemas/naming.md`.
5. Emit a `verification_report` with pass/fail and concrete fixes.
```

**Step 6: task board**

**What it is.** Your project-native durable coordination state, for example `state/tasks.json` plus a human-readable `state/tasks.md`. This must be **your** canonical coordination plane, not an attempt to author Anthropic’s internal team runtime files. Anthropic’s runtime state under `~/.claude/teams/{team-name}/config.json` and `~/.claude/tasks/{team-name}/` is generated automatically and is explicitly not meant to be hand-edited or pre-authored. citeturn2view2turn43view0

**Why it must come before workflow definitions.** Once the board exists, workflows can target a known durable state format rather than inventing ad hoc status files. This also solves your “canonical state path” gap. citeturn43view0turn44view0

**Exact format/content it must contain.** Each task should include at least:
`task_id`, `title`, `owner_profile`, `status`, `dependencies`, `packet_path`, `deliverable_paths`, `verification_path`, `updated_at`.

**Minimum viable example**
```json
[
  {
    "task_id": "TASK-0001",
    "title": "Validate intake packet naming",
    "owner_profile": "meta_detective_controller",
    "status": "pending",
    "dependencies": [],
    "packet_path": "state/packets/TASK-0001.yaml",
    "deliverable_paths": [],
    "verification_path": null,
    "updated_at": "2026-06-13T10:00:00Z"
  }
]
```

**Step 7: workflow definitions**

**What it is.** The repeatable orchestration logic. In 2026, the strongest native Claude format is now `.claude/workflows/*.js`, because Anthropic’s dynamic workflows move orchestration into executable scripts, can be saved and rerun, and scale far beyond what a single conversational turn can coordinate. citeturn46view0turn44view1

**Why it must come before the first runnable skill.** You want the invocation topology fixed before you decide which skill becomes the first runnable slice. Otherwise you risk building a skill no orchestration path actually uses. citeturn46view0

**Exact format/content it must contain.** Start with only two workflow families:
- `intake_to_strategy.js`
- `strategy_to_operations_with_validation.js`

Both should consume canonical task-board entries and handoff packets, and both should write explicit verification artifacts. Because dynamic workflows are native Claude runtime code, this is the right place to encode fan-out and cross-check patterns—but only after schemas and skills exist. citeturn46view0turn15view0

**Minimum viable example**
```js
// .claude/workflows/intake_to_strategy.js
// Pseudocode shape, not production code.
const task = args.task;
const packet = readJson(task.packet_path);

// fan out research in isolated workers
// synthesize into a prioritization draft
// write updated task status and next handoff packet
```

**Step 8: first runnable skill**

**What it is.** The smallest end-to-end executable slice proving the control plane works. The best first slice is not “build a whole feature”; it is a **packet validation and task transition** path. Anthropic’s guidance for new multi-agent usage favors research/review tasks with clear boundaries before broad implementation, and the Agent Skills standard recommends eval-driven iteration from a tiny test set. citeturn2view1turn16view6

**Why it must come here.** At this point all contracts already exist, so the first runnable slice tests the whole artifact chain instead of locking you into premature implementation details. citeturn5view2turn16view6

**Exact format/content it must contain.** Build one command that:
1. loads a packet,
2. validates schema + naming,
3. writes a verification report,
4. updates the task board,
5. emits a next-hop packet or terminal result.

**Minimum viable example**
```md
/validate-and-advance TASK-0001
```

This should resolve to a skill that reads `state/tasks.json`, validates the linked packet, and either moves the task to `ready` or returns a concrete failure report.

**Step 9: CI/CD skeleton**

**What it is.** The automation perimeter. Under a strict subscription-only constraint, this should initially be a **dispatch and validation skeleton**, not a full “run Claude in hosted CI” integration, because Anthropic’s official GitHub Action path expects API/provider auth. citeturn51view0

**Why it comes last.** CI should automate a design that already exists; it should not become the place where the design is first invented. citeturn8view0turn5view2

**Exact format/content it must contain.** The minimum CI/CD artifact set should include:
- `.github/workflows/task-ingest.yml`
- `.github/workflows/schema-check.yml`
- `ops/dispatch/` scripts that hand off work to your self-hosted runtime
- no Anthropic-hosted-action dependency unless you relax the subscription-only rule

**Minimum viable example**
```yaml
name: task-ingest
on:
  issues:
    types: [opened, edited]
  workflow_dispatch:

jobs:
  ingest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate schemas
        run: ./scripts/validate-control-plane.sh
      - name: Dispatch to self-hosted runtime
        run: ./ops/dispatch/send-task.sh
```

## Pre-Definition Packages

The fastest way to get good autonomous output from Claude Code is to hand it **coherent packages** rather than isolated files. This follows Anthropic’s emphasis on specific context and the Agent Skills guidance to ground reusable behavior in project-specific artifacts rather than broad generic instructions. citeturn5view3turn15view0

| Package name | Files it contains | What Claude can autonomously generate once this package exists | What Claude cannot generate reliably without it |
|---|---|---|---|
| Core operating contract | `AGENTS.md`, `CLAUDE.md`, `.claude/rules/*.md` | Accurate role prompts, profile-specific handoff language, project-native task phrasing, and non-conflicting standing instructions. citeturn49view2turn49view3 | Stable role boundaries, shared nomenclature, and cross-tool consistency. Without this package, Claude tends to regenerate its own terms and duplicate policy in multiple places. citeturn49view5turn47view1 |
| Safety and execution policy | `.claude/settings.json`, hook stubs, secret deny rules | Safer skills and workflows that respect protected paths, verification gates, and environment boundaries. citeturn2view8turn5view8 | Reliable enforcement of “never touch X” constraints. Anthropic docs are explicit that prompt instructions are guidance, while hooks enforce. citeturn8view0turn5view8 |
| Control-plane schema package | `schemas/*.schema.json`, `schemas/naming.md`, `examples/*.yaml` | Correct packet templates, task board writers, validators, and workflow I/O glue with low naming drift. citeturn5view3turn15view0 | Durable task transitions or predictable artifact generation. Without schemas first, Claude often invents fields, aliases, and partial structures. This is a synthesis from Anthropic’s structured-context guidance and your current drift gap. citeturn5view3turn49view5 |
| Role procedure package | `.claude/skills/*`, `.claude/agents/*`, `evals/*` | Reusable packet triage, prioritization, packaging, and validation procedures, plus role-specific subagent definitions. citeturn7view2turn44view2turn16view6 | High-quality repeated actions. Without skill and agent definitions, Claude falls back to long ad hoc prompting and weak repeatability. citeturn8view0turn47view2 |
| Native orchestration package | `.claude/workflows/*.js`, `state/tasks.json`, `state/packets/*` | Repeatable multi-agent fan-out and cross-check workflows that can be rerun, paused, inspected, and later adapted into Hermes runtime semantics. citeturn46view0turn44view1 | Scaled orchestration. Without this package, you are limited to conversational delegation or ephemeral team state that is not durable enough to be your canonical control plane. citeturn43view0turn46view0 |
| Delivery automation package | `.github/workflows/*.yml`, `ops/dispatch/*`, runtime adapter docs | Event ingestion, schema checks, promotion gates, and dispatch into self-hosted execution. citeturn40view0turn40view1turn40view2turn40view3 | A production-grade automation perimeter. Without it, orchestration remains manually launched and will not survive team use. citeturn39view0turn40view0 |

## Architecture Validation

The short version is: the **four-profile topology is good**, the **Claude-first artifact layer is good**, the **task board plus handoff packets model is good**, but the **scheduler row needs correction**, and your **workflow-definition layer should now explicitly adopt native `.claude/workflows/`** instead of remaining purely abstract. The strongest pattern in the 2026 Anthropic stack is a small permanent control plane plus isolated, temporary workers. citeturn43view0turn46view0turn8view0

| Component | Our current design | Best practice from research | Gap / change recommended | Source |
|---|---|---|---|---|
| Permanent topology size | Fixed four permanent profiles | Anthropic’s working guidance favors **small team counts** and clear specialization; agent teams are usually strongest around 3–5 teammates, and dynamic workflows can supply larger temporary fan-out without making every specialty permanent. | **Keep the four permanent profiles.** Do **not** add more permanent profiles yet. Instead, let workflows or subagents create temporary specialists when needed. | citeturn2view1turn43view0turn46view0turn42view1 |
| Alfred | Intake/router | Current best practice is a thin orchestrator that routes, delegates, and keeps its own context clean by pushing research into separate contexts. | **Optimal if kept thin.** Add an explicit rule that Alfred never performs deep execution work; it only packetizes, routes, and escalates. | citeturn5view5turn43view4 |
| `meta_operations` | Workflow / packaging | Workflows are now a native Claude artifact in `.claude/workflows/`; reusable procedures belong in skills, while orchestration logic belongs in workflow scripts. | **Strengthen this role by making it the owner of `.claude/workflows/` and artifact packaging.** Do not let it own priority decisions. | citeturn46view0turn8view0turn44view1 |
| `meta_strategist` | Prioritization | Anthropic’s planning guidance separates exploration, planning, and implementation; routing research also emphasizes role boundaries and escalation rules. | **Good role.** Make it the sole author of decomposition order and dependency edges; keep final implementation ownership elsewhere. | citeturn5view2turn42view6 |
| `meta_detective_controller` | Validation / drift | Anthropic recommends fresh-context verification via subagent review; agent teams now also support `TaskCompleted` and `TeammateIdle` hooks for quality gates. | **Excellent role, and it should have veto power.** Bind task completion to explicit verification artifacts and fresh-context review. | citeturn5view0turn43view2 |
| Claude-first authoring + Hermes runtime | Claude-native artifacts with Hermes-compatible execution | Anthropic’s extension model is layered: `CLAUDE.md` for standing context, skills for reusable procedures, subagents for isolated workers, workflows for repeatable orchestration. Agent Skills are portable across tools. | **Validated.** Make Claude-native artifacts the canonical authoring layer and generate Hermes adapters from them, not vice versa. | citeturn8view0turn2view4turn14view0 |
| Shared task board + YAML handoff packets | Durable project coordination | Anthropic’s internal team state is ephemeral and auto-generated; it should not be pre-authored. The durable control plane therefore belongs in your repo, not in `~/.claude/teams/...` or runtime task files. | **Validated, with one correction:** explicitly separate **repo canonical state** from Anthropic runtime state. Keep packet and board schemas in-repo; never try to hand-author Anthropic’s runtime config. | citeturn2view2turn43view0 |
| Workflow definitions | Abstract workflow layer | Claude Code now has native dynamic workflows living in `.claude/workflows/`, and they materially improve reproducibility and scale. | **Change recommended:** use `.claude/workflows/` as the canonical workflow-definition format for Claude-native execution, then adapt outward to Hermes as needed. | citeturn46view0turn44view1 |
| Scheduling | GitHub Actions for repo events + Hermes cron for recurring jobs; not Routines | Remote Routines are still research preview; Desktop local scheduled tasks are workstation-dependent; the official Anthropic GitHub Action uses API/provider auth. | **Partially contradicted.** Keep **Hermes cron** as the primary recurring scheduler. Keep **GitHub Actions** only as an event bus, schema gate, and self-hosted dispatcher unless you accept API/provider auth. Do **not** assume Anthropic’s official GitHub Action satisfies strict subscription-only. | citeturn50view4turn50view5turn50view0turn50view2turn51view0 |
| Deployment path | Single VM + Docker Compose first, Kubernetes later | The strongest pattern in the current docs is incremental adoption and adding complexity only when a trigger appears. Nothing in the 2026 Claude documentation argues for front-loading Kubernetes for a first slice. | **Keep as-is.** Promote to Kubernetes only when you need stronger isolation, runner scale, or multi-tenant scheduling—not before. This recommendation is an inference from the research’s repeated “build over time” pattern rather than a direct deployment prescription. | citeturn8view0turn15view0 |

**Flagged correction from the known state.** The major corrective finding is not that “GitHub Actions” itself is wrong, but that **the official Anthropic Claude Code GitHub Action is not compatible with your strict “Claude Max subscription + Claude Code, no raw API” constraint** unless you reinterpret GitHub Actions as a general trigger/dispatch perimeter instead of the Anthropic-hosted CI execution path. That is the single biggest architectural nuance surfaced by this research. citeturn51view0

## Known Failure Modes

Most failures in Claude Code orchestration are not “model intelligence” failures. They are artifact design failures, context-loading failures, permission-boundary failures, or runtime-state assumptions. The table below focuses on the ones most relevant to a subscription-only multi-agent control plane. citeturn49view5turn48view9turn48view3

| Name | How it manifests in subscription-only Claude Code setups | Prevention pattern | Detection signal |
|---|---|---|---|
| CLAUDE.md bloat and contradiction | Claude starts ignoring standing instructions, follows some rules but not others, or behaves inconsistently across sessions because global instructions are too large or conflict with one another. | Keep each `CLAUDE.md` under ~200 lines, move conditional instructions into path-scoped rules, and periodically prune contradictory files. | Repeated need to restate rules, `/memory` showing too many loaded instruction files, or drift between neighboring directories. citeturn49view1turn49view0turn49view5 |
| AGENTS.md without a Claude adapter | You maintain a beautiful `AGENTS.md`, but Claude Code simply does not see it, because Claude loads `CLAUDE.md` natively. | Always pair `AGENTS.md` with a thin `CLAUDE.md` that imports it. | Claude ignores contract details that exist only in `AGENTS.md`. citeturn49view2 |
| Wrong built-in subagent for policy-sensitive work | Explore or Plan produces outputs that ignore project-specific policy or repo state because those built-in agents skip `CLAUDE.md` and parent git status to stay lean. | Use custom subagents or general-purpose agents for policy-sensitive steps; preload the needed skill or prompt instead of relying on Explore/Plan defaults. | Research output is technically correct but violates your repo’s standing conventions. citeturn6view4 |
| Same-file parallel overwrite | Two workers touch the same file and one silently stomps the other, especially in teams or parallel sessions. | Partition file ownership per task, or isolate parallel work with worktrees. | Unexpected diffs, lost edits, or teammates revisiting the same file set. citeturn2view1turn2view11 |
| Lead takeover and premature completion | The lead begins implementing work instead of waiting for workers, or declares the team done while tasks are still open. | Instruct the lead to wait, keep work units small and independent, and add `TaskCompleted` / `TeammateIdle` gates where possible. | Pending tasks after “done,” or missing outputs from workers the lead bypassed. citeturn2view1turn43view2 |
| Runtime task-state lag and resume gaps | Team progress appears stuck because completed tasks remain unmarked, or `/resume` tries to message teammates that no longer exist. | Keep your own repo-native task board, treat Anthropic runtime state as ephemeral, and respawn teammates after resume when necessary. | Blocked dependent tasks, ghost teammates, or resumed sessions with broken references. citeturn43view1turn2view2 |
| Permission overtrust in `auto` mode | A dangerous state change slips through because it is performed by in-project file edits rather than the exact command classes the permission gate evaluates. | Use `permissions.deny` for protected files, put fragile infra work in plan mode, and enforce truly critical boundaries in hooks rather than trusting classifier coverage alone. | Unexpected edits to stateful config, Terraform, or infra files that were never explicitly reviewed. citeturn48view3turn48view4turn2view8turn5view8 |
| Skill trust escalation | A skill package carries more authority than intended because instructions and scripts live together and trust is effectively granted at install/use level. | Pin to trusted local skills, review bundled scripts, and set `disable-model-invocation: true` on side-effect-heavy skills. | Unreviewed script execution, unexplained network calls, or skills activating where they should only be user-invoked. citeturn48view5turn48view6turn7view3 |
| Scheduler memory fracture | A scheduled worker appears to “succeed,” but the target memory or target agent never actually receives the intended knowledge update. | Verify delivery at the **receiver** side, not just the writer side, and keep critical coordination state in your repo-native task board rather than memory alone. | Cron reports success while the intended target lacks the fact, packet, or state transition. citeturn48view0turn48view1turn48view2 |
| CI auth mismatch | You design around GitHub-hosted CI running Claude Max directly, then discover the official Anthropic action requires API/provider auth. | Treat GitHub Actions as dispatch and gating unless you intentionally relax the subscription-only rule. | Workflow setup requires `ANTHROPIC_API_KEY`, cloud-provider creds, or SDK-driven auth. citeturn51view0 |
| Too many permanent roles | Productivity drops because coordination overhead, token cost, and role overlap exceed the benefit from more fixed agents. | Keep permanent roles small; express temporary specialties as skills, custom subagents, or workflow fan-out instead. | Idle agents, repeated routing indecision, and more “team management” than useful work. citeturn2view1turn42view1 |

## Comparison Between Apex Alfred and Comparable Approaches

This comparison separates what is **possible** from what is **appropriate under your exact constraint**. Claude-native options are most relevant; non-Claude rows are included because they expose converging 2026 patterns around context files, local CLI agents, and repository automation. citeturn47view1turn35view0turn35view4

| Approach | Tooling | Coordination method | Key strength | Key weakness | Applicable to our constraint |
|---|---|---|---|---|---|
| **Apex Alfred** | Claude Max + Claude Code artifacts + Hermes-compatible runtime | Durable repo-native task board + handoff packets + workflow scripts + self-hosted scheduling | Best fit for portability, auditability, and subscription-era artifact authoring | Requires discipline around schemas, naming, and scheduler boundaries | **Yes** |
| Claude subagents + skills only | `CLAUDE.md`, `.claude/skills/`, `.claude/agents/` | Main session delegates isolated workers and gets summaries back | Lowest orchestration overhead; strong context hygiene | Weak for durable team state and cross-session control plane | **Yes, but limited**. Best for early slices, not the whole program. citeturn8view0turn6view4 |
| Claude Agent Teams | Native Anthropic team runtime | Shared task list + direct teammate messaging | Good for parallel work where peers must challenge and inform one another | Experimental; no nested teams; lagging task state; higher token cost; ephemeral runtime state | **Yes, but only as a runtime layer**. Keep your repo-native board as canonical. citeturn43view0turn43view1 |
| Claude Dynamic Workflows | `.claude/workflows/*.js` | Scripted orchestration with background run management | Best native Claude option for repeatability and large fan-out; orchestration becomes code | More product-specific than simple skill orchestration; still needs strong schemas and skill boundaries | **Yes**. This is the strongest native addition to your current design. citeturn46view0 |
| Official Anthropic Claude Code GitHub Action | `anthropics/claude-code-action` | GitHub workflow triggers drive Claude execution in CI | Strong GitHub integration and convenient event wiring | Official setup is API/provider oriented, not strict subscription-only | **No, not under a strict subscription-only rule**. citeturn51view0 |
| Codex CLI | OpenAI Codex CLI + `AGENTS.md`-style repo conventions | Local terminal agent; can use ChatGPT-plan sign-in | Strong evidence that cross-tool context-file conventions are converging; proves AGENTS-style workflows are not Claude-specific | Not Claude-only and not Hermes-compatible by default | **No** for your current constraint, but useful as a portability benchmark. citeturn35view0turn35view1 |
| Gemini CLI | Gemini CLI + `GEMINI.md` + GitHub Action | Local CLI agent with repo context + automation hooks | Confirms the same 2026 pattern: local agent, context file, workflow automation, GitHub integration | Different context-file name and ecosystem; not Claude-only | **No** for your current constraint, but useful as a design comparison. citeturn35view4 |

The important architectural conclusion from this comparison is that **your direction is stronger than a pure native-Agent-Teams design**, because Anthropic’s own team runtime is still experimental and intentionally ephemeral, while your task board and packet model provide the durable state Anthropic does not currently expose as a project-authored primitive. The strongest improvement is therefore **not** “switch to Agent Teams,” but “keep your durable control plane and adopt native Claude workflows for repeatable runtime fan-out.” citeturn2view2turn43view1turn46view0

## Recommended Immediate Actions

**Action 1: Freeze the shared contract first.**  
Create `AGENTS.md` and a thin importing `CLAUDE.md` immediately. This gives you the shared cross-tool core plus the Claude-native adapter Anthropic requires, and it eliminates the largest early source of drift before any skills or workflows are generated. The artifact produced is `AGENTS.md` + `CLAUDE.md`. citeturn47view1turn49view2turn8view0

**Action 2: Lock the schemas and names before you let Claude author procedures.**  
Create `schemas/handoff_packet.schema.json`, `schemas/task.schema.json`, `schemas/workflow_def.schema.json`, `schemas/verification_report.schema.json`, and `schemas/naming.md`. This is the fastest way to solve your current “canonical state paths” and `prompt_packets`-style variable drift gap. The artifact produced is the entire `schemas/` package plus `examples/` fixtures. This sequencing is a research-backed inference from Anthropic’s plan-first guidance and the Agent Skills emphasis on artifact-grounded procedures. citeturn5view2turn15view0turn49view5

**Action 3: Establish the execution safety perimeter before building workflows.**  
Create `.claude/settings.json` with deny rules for secrets and runtime state, plus hook stubs for completion checks. Add one shell script stub such as `scripts/check-task-completion.sh`. The artifacts produced are `.claude/settings.json` and hook/check scripts. This matters because prompt instructions are guidance, while hooks and permissions are the actual enforcement layer. citeturn2view8turn5view8turn44view4

**Action 4: Build one end-to-end validator slice before building “smart” orchestration.**  
Implement exactly one task-flow skill and one detective subagent:
- `.claude/skills/validate-and-advance/SKILL.md`
- `.claude/agents/meta_detective_controller.md`
- `evals/validate-and-advance/evals.json`

This should validate a packet, write a `verification_report`, and move a task to the next state. The artifact produced is your first reproducible control-plane slice. Anthropic’s current guidance favors starting with research/review/validation tasks with clear boundaries, and fresh-context review is the right design for your detective role. citeturn2view1turn5view0turn16view6

**Action 5: Rewrite the scheduler specification to reflect the actual 2026 product boundary.**  
Produce an explicit scheduler matrix document, for example `ops/scheduler-matrix.md`, plus a dispatch-only GitHub workflow like `.github/workflows/event-ingest.yml`. The document should designate:
- **Hermes cron** as the primary recurring executor
- **GitHub Actions** as repo-event intake / schema gate / dispatch
- **Claude Desktop scheduled tasks** as optional personal-local automation only
- **Anthropic Routines** as not production-canonical while still in research preview
- **Anthropic GitHub Action** as out-of-scope unless you relax the subscription-only rule

This is the most important architectural correction surfaced by the research. citeturn50view4turn50view5turn50view2turn51view0

### Open questions and limitations

One design choice remains conditional on your exact execution plan: whether **GitHub Actions** is intended merely to **dispatch into your self-hosted runtime** or to **run Claude itself inside hosted CI**. The first stays compatible with your stated constraint; the second does not match Anthropic’s official subscription-free CI path as currently documented. citeturn51view0

Hermes-specific public evidence was materially thinner than Anthropic’s official corpus. The most concrete public 2026 evidence I found for Hermes scheduling behavior was the June 2026 **Channel Fracture** analysis, which is strong enough to justify adding receiver-side delivery verification, but it is still a narrower evidence base than the Anthropic documentation used above. citeturn48view0turn48view2