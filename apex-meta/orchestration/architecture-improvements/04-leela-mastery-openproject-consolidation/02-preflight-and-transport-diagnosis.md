---
type: Diagnosis / Preflight
title: OpenProject skill transport + project-type preflight (read-only, reproducible)
description: End-to-end read-only preflight of the real opCall.js skill from the actual Windows agent context, plus per-project type enablement. Establishes, with evidence, why writes fail and what minimal change is needed. No changes applied.
tags: [openproject, wsl2, networking, preflight, diagnosis, read-only]
status: draft
generated: { by: "claude/opus-4.8", at: "2026-09-27" }
authority: verified-evidence
implementation_authority: none
---

# Preflight & transport diagnosis (measure-first)

Prompted by external review: stop assuming, stop raw writes, prove the whole access chain read-only
from the real agent context, then propose a minimal change. **Nothing was changed** (no `.wslconfig`,
no Docker ports, no OpenProject writes, no type activation). Two independent themes.

## Method
Ran read-only checks from four locations while the instance was provably serving, so results are not
confounded by idle-sleep. Scripts: `scratchpad/preflight_wsl.sh`, `preflight_win.ps1`, `preflight_types.py`.

## Evidence

### A. Windows host (the actual agent execution context = Claude Code on win32, Git Bash/PowerShell)
- node: `v24.18.0` at `C:\Users\gehma\AppData\Local\Programs\ApexNode\node-v24.18.0-win-x64\node.exe`
- `Test-NetConnection 127.0.0.1 -Port 8083` → **TcpTestSucceeded: False**
- `curl.exe http://127.0.0.1:8083/api/v3` → **http_code=000, exit 7** (could not connect)
- Proxy env: HTTP_PROXY / HTTPS_PROXY / NO_PROXY all empty (not a proxy issue)
- **Real skill** `opCall.js root|whoami|project.get --id 3|type.list` → all **`ECONNREFUSED 127.0.0.1:8083`**

### B. WSL2 (Ubuntu "Apex", kernel 6.18-microsoft-standard-WSL2) — measured at the same time
- listener: `LISTEN 127.0.0.1:8083` (docker-proxy on the VM loopback)
- `curl 127.0.0.1:8083/api/v3` → **503**; `curl localhost:8083/api/v3` → **503** (i.e. instance up & serving)
- authed root later confirmed `instanceName=OpenProject coreVersion=17.8.0`
- **No node in WSL** → the skill cannot run inside WSL either

### C. Docker
- `docker context ls` → `default … unix:///var/run/docker.sock` (native engine, not Docker Desktop — matches D-09)
- client `29.1.3`; `docker ps` → **permission denied** (gehma not in `docker` group; sudo needs a password)

### D. OpenProject project-type enablement (read-only API)
- `GET /api/v3/projects/3/types` (Leela) → **`Task, Milestone, Summary task`**
- `GET /api/v3/projects/2/types` (Scrum) → `Task, Milestone, Summary task, Epic, User story, Bug`
- `GET /api/v3/projects/1/types` (Demo) → `Task, Milestone, Summary task`
- `GET /api/v3/types` (global) → `1 Task, 2 Milestone, 3 Summary task, 4 Feature, 5 Epic, 6 User story, 7 Bug`

## Conclusions (evidence-backed, not assumed)

**Theme 1 — transport.** The instance is up and serving on the WSL VM loopback (`127.0.0.1:8083`, HTTP 503→200),
yet at the same moment Windows cannot open a TCP socket to it (TcpTestSucceeded False; curl exit 7), with no
proxy in play. Therefore the failure is purely the network path from Windows→WSL: a container port published to
the VM's `127.0.0.1` is not reachable from the Windows host (documented WSL2 NAT behavior — MS networking docs;
microsoft/WSL #9515). The skill's calling side is fine; it simply has no route. And it can't run inside WSL
either (no node there). **Net: no agent can currently reach the instance through the skill.**

**Theme 2 — project types (separate from transport).** The 422 was correct behavior: project 3 (Leela) only
enables `Task, Milestone, Summary task`. The design's taxonomy (Epic, Feature, User story) is defined globally
but not enabled on project 3, so any Epic/Feature create there must 422 — from the skill or from raw calls alike.

## Skill gaps this exposed (must be closed before production writes)
- No read-only **`doctor`/preflight/self-test** op (identity, auth, project read, allowed types, write-gate check).
- No **`type.list --project <id>`** (only global `type.list`) → cannot validate a type is allowed before create.
- Takes numeric **type ids**, not stable names → no project-scoped name→id resolution.
- Write-gate (preview→`--confirmed`→reread) exists in policy; must be verified to actually enforce in `opCall.js`.

## Preflight completeness (corrected — it is PARTIAL, not done)

A full skill-preflight requires all twelve items below proven from the agent's own context. Items 9–12 use the
*real* `opCall.js` and are still OPEN, because the skill can't yet run against the instance (no node in WSL;
ECONNREFUSED from Windows). So this is a reproduced network fault + a raw-API config read — not a completed skill
preflight.

| # | Check | Status |
|---|---|---|
| 1 | Which Windows process runs the skill (agent context) | DONE — Claude Code on win32, Git Bash/PowerShell |
| 2 | Which node.exe | DONE — v24.18.0 at `…\ApexNode\…` |
| 3 | Base URL in skill config | DONE — `http://127.0.0.1:8083` |
| 4 | Docker engine running OpenProject | DONE — native WSL engine (client 29.1.3) |
| 5 | Real Docker port mapping | DONE — `127.0.0.1:8083:80` |
| 6 | WSL listen address | DONE — `127.0.0.1:8083` |
| 7 | Windows localhost:8083 reachable by TCP | DONE — **no** (TcpTestSucceeded False) |
| 8 | Windows localhost:8083 returns HTTP | DONE — **no** (curl exit 7) |
| 9 | Real `opCall.js` read-only API call | **DONE 2026-09-27** — `doctor`/`whoami` via WSL node → 200, verdict pass |
| 10 | Types reported for project 3 *via the skill* | **DONE** — `type.list --project 3` (skill) → Task/Milestone/Summary task |
| 11 | Preview possible without any write | **DONE** — `wp.create` (no `--confirmed`) prints planned body, no write |
| 12 | Write blocked without explicit confirmation | **DONE** — exit 3, nothing created; name "Task"→id 1 resolved correctly |

**Transport resolved via Option C (2026-09-27):** private Node LTS **v24.21.0** installed under `/home/gehma/nodejs`
(user-space, no sudo, checksum-verified, reversible), skill invoked as
`wsl -d Ubuntu -- /home/gehma/nodejs/bin/node …/opCall.js …`. OpenProject stays loopback-only; no port
publishing, no `.wslconfig` change. The existing `/usr/local/bin/node` is a root-owned Hermes symlink,
not usable by `gehma` — hence the private install.

## Proposed change plan (revised per review — boundary first; NOT applied)

**P0 — Evidence: PARTIAL.** Network fault reproduced from the agent context; changed nothing. Items 9–12 pending.

**P1 — Decide the trust boundary (this drives everything else).** Not a pre-ranked A>B>C. Two real architectures:
- **C — skill runs inside WSL (recommended for this privacy/self-hosted setup).** Install node in WSL; every agent
  invokes one identical Windows launcher `wsl -d Ubuntu -- node …/opCall.js …`. Same skill code/guards/config for
  all five agents; OpenProject stays loopback-only (nothing newly exposed); **no networking change**; and it
  **unblocks items 9–12 today** (inside WSL the skill can already reach `127.0.0.1:8083`). Cost: a second node
  runtime + a uniform launcher + WSL idle/boot handling. This is an equal architecture choice, not a deviation.
- **A — skill stays Windows-native.** Publish OpenProject on `0.0.0.0` (all WSL interfaces) + a Windows Hyper-V
  firewall rule limiting 8083 to the host, then verify from Windows/WSL/LAN separately. Cost: wider exposure to
  harden; a one-time docker permission.
- **B — mirrored networking.** Global WSL change; keeps loopback binding; higher variance; own restart. Only if
  broad bidirectional Windows↔WSL is needed later.

**P2 — Skill `doctor` (read-only self-check).** Add an op that verifies: API reachability, authentication, correct
OpenProject instance (fingerprint), expected project access, project-specific allowed types (`type.list --project`),
and that a write is blocked without confirmation. Plus name→id type resolution (accept `--type "Feature"`, resolve
against the project's allowed types, fail if not enabled/ambiguous). Pure local code — no infra needed to author.

**P3 — Enable Leela work-item types.** Enable only the required types (Epic, Feature, User story; Bug if wanted)
**on the Leela project specifically** (not globally); read the effective types back via API. Do this after P1/P2,
before any preview.

**P4 — Dry run.** Read project → resolve types by name → build a preview → **no mutation**.

**P5 — Controlled creation.** Explicit confirmation → exact approved payload → create once → re-read and log.

## Progress — 2026-09-27 (P2 skill hardening, authored)
The skill code was hardened (additive, boundary-independent, existing flows unchanged), in
`.agents/skills/openproject/client/`:
- **`doctor`** op — read-only composite self-check (config, auth/whoami, instance fingerprint, optional
  `--project` access + its enabled types, write-gate active). No mutation; exit 0 pass / 5 fail.
- **`type.list --project <id>`** — lists a project's *enabled* types (not the global set).
- **`wp.create --type "<name>"`** — resolves a type name against the project's enabled types before create;
  fails clearly if not enabled/ambiguous (numeric id still accepted). `opClient.js` gained
  `getProjectTypes` + `resolveTypeName`; docs (`SKILL.md`, `operations.md`) updated to match.
- **Verified now:** `node --check` passes on both files; `opCall.js` usage lists `doctor`.
- **Still untested (checklist 9–12):** the behavioral run needs Node to reach the instance — i.e. the P1
  transport decision. Nothing was run against live data.

## Standing rule (from the review, adopted)
Do not say "preflight completed," and perform no production writes, until the *real* skill runs at least read-only
from the agent context, queries Leela's allowed types itself, can preview without writing, and blocks a write
without confirmation (checklist items 9–12). Raw HTTP/python is a diagnosis tool only, never the production path.

## Why OpenProject writes repeatedly needed a retry (root cause — checked)
Symptom seen throughout the build: a write run (create WPs / attach / re-parent) fails on the first attempt
with `identity gate failed — /api/v3 returned status 503`, and succeeds on a re-run. This is **one root cause,
not flakiness or random failure**:
- **The WSL VM idle-sleeps.** After a short idle gap the whole VM shuts down; the next access cold-boots it and
  OpenProject (`000 → 503 → 200`) over ~65–85s. During that window the API returns `000`/`503`.
- **The skill's identity gate is doing its job.** Before any write, `verifyInstance()` does `GET /api/v3`; a
  `503` (Puma still booting) → the gate **refuses to write**. That refusal is *correct safety behavior*
  (it must not write to an instance it can't verify), but it means a batch started against a cold/half-booted
  instance aborts cleanly and must be re-run once warm.
- **My early scripts under-warmed.** The first boot-wait polled `whoami` and proceeded on the first `200`, but
  the instance then flapped back to `503` mid-batch. Fix applied: warm-up now requires the **root** endpoint
  (the exact one the gate checks) to return `200` **three times consecutively + a settle delay** before any
  write. With that pre-warm, batches succeed first time.

**This is the same idle-sleep documented above, and it is exactly what handover
`05-handover-browser-keepalive.md` fixes.** It was deferred by operator choice, so the retry pattern persisted.
Recommendation: implement the keepalive (Feature #122) to eliminate cold boots, and keep the "root-stable-×3
before writes" pre-warm in any bulk script. Nothing was ever written incorrectly — the gate blocked cleanly
every time; the cost was wall-clock re-runs, not data risk.
