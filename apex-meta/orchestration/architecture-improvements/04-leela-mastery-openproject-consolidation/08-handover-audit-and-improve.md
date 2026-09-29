---
type: Handover
title: Audit & improve the OpenProject agent setup — efficiency, best-practice, multi-repo access
description: Brief for an auditor/improver agent to (1) quantify the WSL/Ubuntu computational drag, (2) web-research whether the current setup is best practice or has high-impact betterments, and (3) prove whether agents in OTHER repos (e.g. MasterOfArts) can access OpenProject efficiently — tested with a real agent.
tags: [handover, audit, openproject, wsl2, best-practice, multi-repo, mcp]
status: ready
generated: { by: "claude/opus-4.8", at: "2026-09-27" }
implementation_authority: research-and-recommend (no infra/data changes without operator OK)
---

# Handover: audit & improve the OpenProject agent setup

> **✅ PARTLY ADDRESSED (2026-09-28).** The "is the skill setup best practice?" question was researched and
> acted on: the skill is now a single canonical source at `C:\GitDev\agent-skills\skills\openproject\`
> (was `Leela-Cloud-2026\.agents\skills\openproject\` — path references below are historical), linked into
> each agent's user-global dir; token at `~/.config/openproject/op.env`; client hardened (atomic config +
> host guard). Reasoning/research: `agent-skills/README.md`, `agent-skills/research/FINDINGS.md` +
> `LEARNINGS.md`, and `ki-basis/docs/openproject/DECISION-2026-09-28-canonical-skill-architecture.md`.
> Still open from this brief: WSL drag quantification and multi-repo access proof (the 5-account test, T07).

## 0. Your role
You are an **auditor and improver**, not just an implementer. Verify claims against evidence and official
sources (do not approve by fluency). Produce a **verdict** for each question: *best practice as-is* /
*inefficient — fix* / *high-impact betterment available* — each with evidence and a concrete recommendation.
The apex-meta skill `source-authority-and-verdict-packet` is the intended output discipline. **Do not change
infrastructure or live data without explicit operator approval** — this is research + measurement + a
recommendation, plus a **read-only** or **clearly-labeled-test-scope** simulation for Q3.

## 1. Current state — VERIFIED this session (do not re-derive; verify only if you doubt it)

### What exists and where
- **OpenProject** `leela-op178-openproject` = image `openproject/openproject:17.8.0`, running in **Docker
  inside WSL2** (Ubuntu distro "Apex", native `dockerd`, **not** Docker Desktop — retired, see the WSL2
  migration bundle). DB = `priv_openproject` on the shared `ki-basis-shared-postgres` cluster.
- **Port**: `compose.shared-db.yaml` publishes **`0.0.0.0:8083:80`** (changed this session from
  `127.0.0.1:8083`). Reachable from **both** inside WSL and the **Windows host** at
  `http://127.0.0.1:8083` (verified 401/200 warm). `OPENPROJECT_HOST__NAME=127.0.0.1:8083` (host-check →
  use exactly that URL, not `localhost`/IPv6, not the WSL IP).
- **The skill** (portable Node CLI, no framework): `C:\GitDev\Leela-Cloud-2026\.agents\skills\openproject\`
  — `SKILL.md`, `client/opCall.js`, `client/opClient.js`, `references/operations.md`, `references/write-policy.md`.
  Claude Code sees it via the `.claude/skills/openproject` junction. **Repo-local to Leela-Cloud-2026.**
- **Config/token**: `C:\GitDev\leela-op178\op.env` (base `http://127.0.0.1:8083`, admin API token,
  `OPENPROJECT_EXPECT_VERSION_PREFIX=17.`, `OPENPROJECT_EXPECT_HOST=127.0.0.1:8083`). Never in a repo.
- **Node runtimes**: WSL user-space **`/home/gehma/nodejs/bin/node`** (v24.21.0, installed this session,
  no sudo); Windows **`C:\Users\gehma\AppData\Local\Programs\ApexNode\node-v24.18.0-win-x64\node.exe`**.
- **Root access without password**: `wsl -d Ubuntu -u root -- <cmd>` (WSL default; used for docker/rails).
  Permission allow-rules for the classifier live in `C:\.claude\settings.local.json`.
- **How the skill is invoked today** (this session's pattern): from Windows,
  `wsl -d Ubuntu -- /home/gehma/nodejs/bin/node <repo>/.agents/skills/openproject/client/opCall.js <op> … [--confirmed]`
  with `op.env` env loaded; bulk work via a Python orchestrator in WSL that shells to the CLI per object.
  **Note:** because the port is now on `0.0.0.0`, the skill could ALSO run natively on Windows Node — this
  is one of the efficiency questions (Q1).
- **Skill ops now include**: reads (`root/whoami/project.*/wp.*/type.list [--project]/relation.*`), a
  read-only **`doctor`** self-check, and gated writes (`wp.create` with type name→id resolution,
  `wp.update`, `wp.comment`, `wp.attach`, `relation.create/delete`, `project.create/update/delete`).
- **What's already in OpenProject**: root **Leela & Mastery** (id 4) → **Leela** (id 3, 83 WPs = the full
  Leela plan) + **PM Infrastructure** (id 5, 14 WPs = the initiative's open tasks, incl. this audit).
  A separate **community** OpenProject runs on `:9082` — **never touch it**.

### Known operational facts (measured this session)
- WSL VM **idle-sleeps**: after inactivity the whole VM shuts down; next access cold-boots ~**80s**
  (`000 → 503 → 401/200`). This is the single biggest UX drag; a keepalive fix is handover 05.
- `.wslconfig` = `[wsl2] memory=16GB, swap=4GB` (no `networkingMode`, so NAT; `localhostForwarding` default on).
- Running Node against `/mnt/c/**` uses the WSL **9p** bridge (slow file I/O); each `wsl.exe` invocation has
  process-startup overhead.

## 2. Mandatory reading (files + links)
Repo bundle (this initiative): `apex-meta/orchestration/architecture-improvements/04-leela-mastery-openproject-consolidation/`
- `00-handover.md` (mission), `01-leela-plan-breakdown-design.md`, **`02-preflight-and-transport-diagnosis.md`**
  (the transport/idle-sleep/type-enablement evidence — read this closely), `03-visual-explainer.html`,
  `05/06/07-handover-*.md` (the three open tasks), `index.md`.
WSL2 infra bundle: `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/`
— `log.md` + `02-decisions-log.md` (D-01…D-18; the live instance this all runs on, incl. the D-17 dual
incident about wrong-target OpenProject — read before touching infra).
Prior PM/OpenProject research (IMPORTANT for Q2 — they already discussed the **official MCP server** as the
AI-agent path): `Leela-Cloud-2026/docs/orchestration/wave-orchestration/project-management-consolidation/infrastructure-improvement-portfolio-2026-09-18/`
— `06-phase0-…`, `07-…`, `08-…-v2` (v2 supersedes 07).
Memory notes (agent auto-memory): `leela-openproject-instance-access.md`, `leela-mastery-openproject-consolidation.md`.
Skill source: read `SKILL.md`, `client/opCall.js`, `client/opClient.js`, `references/*` in full.
Official docs to research against:
- OpenProject **MCP server**: https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/
- OpenProject API v3: https://www.openproject.org/docs/api/  · endpoints https://www.openproject.org/docs/api/endpoints/
- Install/ops + system requirements: https://www.openproject.org/docs/installation-and-operations/
- WSL networking (127.0.0.1 vs 0.0.0.0, mirrored mode): https://learn.microsoft.com/en-us/windows/wsl/networking
  · the container-port issue: https://github.com/microsoft/WSL/issues/9515
- WSL `.wslconfig` (memory, vmIdleTimeout, networkingMode): https://learn.microsoft.com/en-us/windows/wsl/wsl-config

## 3. Question 1 — WSL/Ubuntu computational drag
**Determine:** Do we actually need to route through Ubuntu, and how much does it cost?
- Clarify the two distinct needs: (a) **running the skill** (API client) and (b) **operating the instance**
  (docker/rails). Since the port is now on `0.0.0.0`, (a) can run on **Windows Node directly** — (b) still
  needs WSL/docker. Establish which parts truly require WSL.

**Measure (concrete):**
- Per-call latency, warm instance, same op (e.g. `whoami` ×20): **Windows Node** (`node opCall.js whoami`)
  vs **WSL Node via wsl.exe** (`wsl -d Ubuntu -- …/node opCall.js whoami`) vs skill files on `/mnt/c` vs
  copied into the WSL ext4 home. Report median + spread; attribute cost to wsl.exe startup vs 9p I/O vs HTTP.
- WSL VM footprint: `wsl -d Ubuntu -- free -m`, `wsl -d Ubuntu -- nproc`, and the Windows **`Vmmem`/`vmmemWSL`**
  process RAM/CPU (Task Manager or `Get-Process vmmem*`); OpenProject container idle CPU/RAM
  (`docker stats --no-stream`). Compare against the 16 GB cap and the 32 GB shared-memory machine.
- Quantify the **idle-sleep cold-boot** cost (time-to-first-200) and the keepalive's steady-state overhead.

**Deliver:** a drag table (latency, RAM, CPU, cold-boot), a verdict (negligible / meaningful / severe), and
a recommendation (e.g. "run the skill on Windows Node natively; keep only docker in WSL" — or keep WSL and
add a keepalive). Note the tradeoff vs Q2's "should this even run in WSL" question.

## 4. Question 2 — best practice vs. our setup (web research)
**Determine:** Is the current setup best practice, inefficient, or does a high-impact betterment exist?
Research and compare against official/primary sources; date every time-sensitive claim.

Cover at least:
1. **Custom Node CLI skill vs. OpenProject's official MCP server** (BIGGEST question — prior research
   06/07/08 already flagged the MCP server as the intended AI-agent interface). Is a hand-rolled Node CLI
   the right call, or should agents talk to OpenProject via its **MCP server** (native tool discovery, auth,
   per-tool enable/disable, token-efficient responses)? Evaluate: multi-agent fit, maintenance, the existing
   write-gate/fingerprint safety we'd lose or have to re-implement, Community-vs-Enterprise availability of
   MCP, and whether a hybrid (MCP for reads/discovery + the gated CLI for confirmed writes) is better.
2. **Hosting**: OpenProject running in **WSL2** on a workstation vs a persistent server/VPS vs SaaS —
   is a laptop WSL VM (that idle-sleeps) an appropriate host for a system multiple agents/repos depend on?
   What do OpenProject's install/ops + system-requirements docs recommend?
3. **Networking**: `0.0.0.0` publish + host firewall vs **mirrored** WSL networking vs a reverse proxy /
   HTTPS. Security posture of exposing `0.0.0.0` inside the WSL NAT VM (LAN reachability, Hyper-V firewall).
4. **Ops hygiene**: backups/restore for `priv_openproject`, upgrades, secrets handling (token in `op.env`),
   the shared-Postgres coupled failure domain (see WSL2 bundle D-07).
5. **Idle-sleep / keepalive** approaches vs. simply hosting on an always-on target.

**Deliver:** a best-practice matrix (our choice | best practice | gap | impact | recommendation) with
sources, and a ranked list of high-impact betterments (the MCP-server question is expected to top it).

## 5. Question 3 — multi-repo access (the MasterOfArts test)
**Determine:** Can an agent working in ANOTHER repo (e.g. the local **MasterOfArts** clone,
`C:\GitDev\MasterOfArts`) access this OpenProject efficiently — and prove it with a real agent, not theory.

Facts to start from:
- The skill is currently **repo-local to Leela-Cloud-2026** (`.agents/skills/openproject` + the
  `.claude/skills/openproject` junction). An agent in MasterOfArts does **not** see it by default.
- The skill is **portable**: it only needs Node + the skill files + `op.env` env vars. So access options
  include: (a) copy/junction the skill into each repo's `.agents/skills` / `.claude/skills`; (b) a **shared
  global** skill location (e.g. `~/.claude/skills/openproject`) all repos inherit; (c) the **official MCP
  server** (repo-independent — the agent connects to the instance regardless of cwd); (d) a global `op`
  launcher on PATH. Evaluate each for efficiency, drift risk, and "5 accounts use the identical skill".

**Simulate & test (the operator explicitly wants this run with the real agent):**
1. Stand up (or point) a CLI agent **primed in `C:\GitDev\MasterOfArts`** (Claude Code with its own
   `CLAUDE_CONFIG_DIR`, or Codex — see the fleet research paths in `07-handover-5account-…md`).
2. Have that agent discover + run the skill against OpenProject: `doctor --project 3`, one read, and one
   **authorized, clearly-labeled TEST-scope** write (a comment on a throwaway test WP, or a WP in a
   `zz-skill-test` project) — through the preview→`--confirmed`→reread gate. **Do not test-write on the 83
   real Leela WPs or the 14 PM-Infra WPs.**
3. Record: did it discover the skill, reach the instance, produce identical identity/output, and gate the
   write — and how much friction (setup steps, latency) vs. running from Leela-Cloud-2026.
4. Compare the access options above head-to-head; recommend one convention for all repos/accounts.

**Deliver:** a working demonstration (transcript/log) that an agent in MasterOfArts can operate OpenProject,
plus a recommended standard for cross-repo access (skill copy vs shared vs MCP), with the tradeoffs.

## 6. Safety
- Live data: Leela (id 3, 83 WPs) and PM Infrastructure (id 5, 14 WPs) are real — read-only unless doing a
  clearly-labeled test-scope write in a throwaway target; clean up afterward.
- Never target the community instance (`:9082` / `comm_openproject`) or revive the retired v14 duplicate;
  keep `OPENPROJECT_EXPECT_*` set so the fingerprint guard holds (D-17 lesson).
- No infra change (networking, hosting, MCP enablement) or skill rewrite without operator approval — this is
  audit + recommend. Any docker/rails action runs as `wsl -u root` with reread-after-write discipline.

## 7. Definition of done
Three verdicts with evidence and a ranked recommendation set:
1. **WSL drag** quantified (table) + a keep-WSL-or-move recommendation, incl. "run skill on Windows Node?".
2. **Best-practice audit** (matrix + sources), explicitly answering: inefficient? high-impact betterments?
   or best practice? — with the custom-skill-vs-official-MCP question resolved.
3. **Multi-repo access proven** by a real agent operating OpenProject from the MasterOfArts repo, plus a
   recommended cross-repo standard. All claims sourced or measured; nothing approved by fluency.
