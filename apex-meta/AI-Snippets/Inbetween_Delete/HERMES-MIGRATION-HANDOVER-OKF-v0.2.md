# Hermes G0.2 Single-Container Migration — Handover (OKF v0.2)

> ⚠️ **This file contains a local dashboard password (below). Do NOT commit/push it as-is; rotate the password or strip it before the repo syncs.** The GitHub PAT is **not** in this file (it was never seen by the assistant; it lives only in the container at `/opt/data/.git-credentials`).

---

## 0. Packet metadata

| Field | Value |
|---|---|
| Format | OKF v0.2 (best-effort; no canonical schema was available to the author) |
| Title | Hermes Architecture-3 single-container runtime migration (runbook G0.2) |
| Date | 2026-08-26 |
| Author | Claude (Opus) main-conversation session, working with operator AlexOG |
| Status | **BLOCKED / IN-PROGRESS** — gateway restart-loop; 20-min hands-off stability soak running at handover time |
| Machine | Windows 11 + WSL2 distro (registered name "Ubuntu", hostname `Apex`), root default user |
| Runtime | Docker **29.1.3**, **containerd 2.2.2** (containerd 2.x), runc v2, cgroup v2, WSL `systemd=true` |
| Hermes image | `nousresearch/hermes-agent:latest` = **v0.20.5** (code_sha dcfdc8de) |
| Subagent/Agent-tool calls used | **None** — all work done directly in main conversation |

---

## 1. Objective

Execute `apex-meta/orchestration/architecture-improvements/02-hermes-single-container-runtime/G0.2-MIGRATION-RUNBOOK.md`:
move Hermes from the old **Arch-2 split** (agent on WSL host + separate Docker sandbox, `terminal.backend: docker`)
to **Arch-3**: the whole agent in **one persistent container**, `terminal.backend: local`, repos mounted (§5b),
state on the `/opt/data` volume. Context/why: `apex-meta/AI-Snippets/AIFailure/HERMES-ARCHITECTURE-HISTORY-AND-DECISION.md`.

Hard constraints (respected throughout): never mount `/mnt/c`; never clone/mount any `leela` / `Leela-Cloud-2026` /
`leela-openclaw-beta` repo; only the 4 canonical repos.

---

## 2. CURRENT STATE (at handover)

- Container `hermes` was last rebuilt **docs-exact** and a **20-minute hands-off soak is running** (see §7 for the pending decision it feeds).
- **Last deployed run command** (docs-exact, no resource caps — this is the current one):
  ```bash
  docker run -d --name hermes --restart unless-stopped \
    -v /root/.hermes:/opt/data \
    -v /root/workspaces:/root/workspaces \
    -p 8642:8642 -p 9119:9119 \
    -e HERMES_DASHBOARD=1 \
    nousresearch/hermes-agent:latest gateway run
  ```
- If the soak wasn't finished when you pick this up: check `docker inspect --format='{{.State.StartedAt}} {{.RestartCount}}' hermes` repeatedly and `docker logs --since 1200s hermes | grep -c "Hermes Gateway Starting"`. A stable gateway logs **exactly 1** "Hermes Gateway Starting".

### Canonical facts (verified this session)
- **Data volume**: host `/root/.hermes` → container `/opt/data`. **All of `/root/.hermes` chowned to uid 10000** (the container's `hermes` user). Backup `/root/.hermes.backup-pre-arch3` is **root-owned** (intact rollback net).
- **Repos**: host `/root/workspaces` (ext4) → container `/root/workspaces`, also **chowned to uid 10000**. Contains exactly: `apexai-os-meta`, `MasterOfArts`, `Investment`, `acim-secular`. **No leela.** All origins `https://github.com/leela-spec/<repo>.git`.
- **Container user model**: the gateway runs as **`hermes` (uid 10000)** with **`HOME=/opt/data`** (set by `/opt/hermes/docker/main-wrapper.sh`). `docker exec hermes ...` defaults to **root, HOME=/root** — this mismatch caused several false readings; always test git/agent behavior with `docker exec -u 10000 -e HOME=/opt/data`.
- **`/root` is mode 700** in the image → the `hermes` user cannot traverse into `/root/workspaces` unless `chmod 711 /root` is applied. This was applied live but **does NOT persist across container recreate** (only across restart).
- **Env in container**: `HERMES_HOME=/opt/data`, `HERMES_WRITE_SAFE_ROOT=/opt/data`, gateway CLI at `/opt/hermes/.venv/bin/hermes`, install tree `/opt/hermes` is root-owned/immutable.
- **Boards (5)**: acim, apex, investment, masterofarts, website-research (`/opt/data/kanban/boards`).
- **Profiles (4)**: independent-reviewer, marketing-executive, research-strategist, workshop-designer (`/opt/data/profiles/*`); each has its own `state.db` + multi-MB WAL. They are **registered but not auto-started** (no per-profile `gateway_state.json`).
- **Data-safety check (mount, not fresh clone)**: `apexai-os-meta` ignored files ≈ **42,780**; `MasterOfArts` ≈ **460**. (Vendor repos / books-media not on GitHub — must survive.)

### config.yaml edits made this session (`/root/.hermes/config.yaml`)
1. `terminal.backend: docker` → **`local`** (Gate 2).
2. Added top-level `dashboard.basic_auth`: `username: admin`, `password_hash: <scrypt>`, `secret: <64-hex>`.
   - **Dashboard login: `admin` / `zhwGcgTMUcagANhe`** ← LOCAL SECRET, rotate/strip before commit.
3. `mcp_servers.qmd.enabled: true` → **`false`** (the `qmd` MCP server points to a host-only binary not present in the container; failed on every boot).

### GitHub token (Gate 4) — DONE and verified
- Fine-grained PAT, **Contents: R/W + Workflows: R/W**, scoped to `leela-spec/{apexai-os-meta,MasterOfArts,Investment,acim-secular}` only (Workflows needed because `acim-secular` has `.github/workflows/pipeline-ci.yml`). **No leela repos.**
- Stored at container `/opt/data/.git-credentials` (`https://leela-spec:<TOKEN>@github.com`, mode 600, owned 10000). Git global config in `/opt/data/.gitconfig` (as hermes): `credential.helper=store`, `user.name=AlexOG`, `user.email=gehmalexander@gmail.com`, `safe.directory=*`.
- **Verified**: `ls-remote` + `fetch` succeed on **all 4** repos when run as `docker exec -u 10000 -e HOME=/opt/data hermes git -C /root/workspaces/<r> ...`.
- **Gotcha discovered**: `printf "...\n"` through PowerShell→wsl→docker→bash **ate the backslash**, writing host `github.comn` (no newline) → auth failed for private repos. Fixed by re-running with **`echo`** instead of `printf`.

---

## 3. Root cause (confirmed environmental) + honest uncertainty

**Primary root cause (high confidence):** the Hermes image's **s6-overlay container supervision is incompatible with containerd 2.x** (this machine: containerd 2.2.2). Documented upstream bug: gateway enters a **restart loop** under s6-overlay on Docker ≥28.5.2 / containerd 2.x. The gateway is repeatedly (re)started (~every 40s) *inside* an otherwise-stable container; the dashboard "**Network error**" on sign-in is a **downstream symptom** (the api_server on 8642 is down during each restart window).

**DECISIVE SOAK RESULT (2026-08-26 ~15:40–16:00Z):** docs-exact run (both ports, no CPU cap), **hands-off 20 min** → 0 restarts, dashboard 302 on all 13 checks, gateway started once. **BUT** at ~t=1200s (16:00:21Z) `s6-supervise gateway-default` sent the gateway **SIGTERM at `loadavg_1m=0.02` (system idle)** with **no preceding gateway activity, no update, no config-reload, no scheduled task in the logs** — then it entered a rapid ~50s cycle again. So:
- **Load/CPU-starvation hypothesis: DISPROVEN.** The restart happened at idle (loadavg 0.02), not under my `docker exec`/`apt` load. Removing the `--cpus 2` cap did NOT fix it; it only lengthened the stable window.
- **Confirmed shape:** intermittent, **spurious, s6-initiated gateway restarts** (stable for a while — seen at ~90s/3m/5m/20m — then rapid cycling), independent of load, data, and config. A supervisor SIGTERM-ing a silent idle service with no logged reason is the signature of the **s6-overlay ↔ containerd-2.x spurious signal-delivery bug**.
- Remaining nuance: our signal reads `SIGTERM` (not the `signal=UNKNOWN` of #35394), so it's the same *class* but not a byte-identical match; could also involve an internal gateway restart request that leaves no log. Either way it is **environmental/runtime-level, not fixable by data/config edits.**

**The loop-liveness watchdog** exists (`gateway/config.py`: `loop_watchdog: true`, ~3 strikes ≈ 90–120s of blocked loop → hard-exit + all-thread stack dump; disable via `gateway.loop_watchdog: false`). It did **not** emit a stack dump in our logs, so it may not be the trigger — or the dump was suppressed. `systemd_watchdog_seconds` defaults to 0 (disabled).

---

## 4. Gate-by-gate execution log (what was done)

| Gate | Action | Result |
|---|---|---|
| 0 | Backup `/root/.hermes` → `.backup-pre-arch3`; confirm docker | PASS (backup pre-existed, valid; docker 29.1.3) |
| 1 | `pkill -f hermes-agent`; removed **12** old Arch-2 sandbox containers (`nikolaik/python-nodejs` `sleep infinity`, names `hermes-*`) | PASS (host Hermes stopped, sandboxes gone). NOTE: `pkill -f hermes-agent` self-killed the wrapper shell because the pattern matched the command text — use a narrower pattern. |
| 2 | `terminal.backend` → `local` | PASS |
| 3 | `docker run` single container (+ data-safety checks) | PASS (repos mounted, 5 boards, ignored-file counts matched) |
| 4 | GitHub token | DEFERRED then later DONE (see §2) |
| 5 | `bootstrap-tools.sh` | PASS but **tools are ephemeral** (see §5 failure #7) |
| 6 | Go/No-go | **NO-GO** — crash loop; root cause per §3 |

---

## 5. FAILURES + causes + fixes (chronological; each is a distinct problem found)

1. **Kanban permission crash-loop.** `PermissionError: /opt/data/kanban/boards/website-research/kanban.db.init.lock`. Cause: migrated data was **root-owned**, gateway runs as **uid 10000**; image's boot chown covers a fixed subdir list that **excludes `kanban`**. Fix: `chown -R 10000:10000 /root/.hermes`.
2. **Gateway couldn't read `config.yaml`.** `config.yaml` was 640 root → gateway (uid 10000) couldn't read → saw no `basic_auth` → dashboard refused to bind. Fixed by the same chown.
3. **Dashboard refuses non-loopback bind without auth.** Image (June-2026 hardening) refuses `0.0.0.0` dashboard without an auth provider. Fix: `dashboard.basic_auth` (username+password_hash) in config.yaml. `HERMES_DASHBOARD_INSECURE` is **ignored** now (#59113).
4. **Broken `qmd` MCP server.** `mcp_servers.qmd.command: qmd` — binary not in image → failed connect every boot. Fix: `enabled: false`.
5. **Repos unreachable by gateway.** `/root` is 700 → uid 10000 can't traverse to `/root/workspaces`. Fix (non-persistent): `chmod 711 /root`. **Durable fix TODO:** mount repos outside `/root` (e.g. `/workspaces`).
6. **git "dubious ownership"** when running git as root on 10000-owned repos. The gateway (uid 10000) is fine; `safe.directory=*` set in hermes global config.
7. **Bootstrapped tools vanish on recreate.** `pandoc`/`poppler-utils` install via **apt into the container layer** (`/usr/bin`), NOT `/opt/data`. Every `docker rm`+`run` wipes them; only the `/opt/data/tools/venv` (docx2python) survives. Must re-run `bootstrap-tools.sh` after any recreate. **TODO:** auto-run bootstrap on container start, or install into `/opt/data`.
8. **Gateway restart-loop (THE core blocker).** See §3. Container stays up (`RestartCount=0`, `StartedAt` stable) but the internal `s6-supervise gateway-default` SIGTERMs+restarts the gateway ~every 40s; `cont-init` re-runs repeatedly. `api_server`(8642) + dashboard(9119) go down each cycle → dashboard "Network error".
9. **Token file malformed** (`printf \n` eaten by PowerShell). See §2 — fixed with `echo`.

---

## 6. THINGS ALREADY TRIED — DO NOT REPEAT

- ❌ **`HERMES_GATEWAY_NO_SUPERVISE=1`** (the documented #35394 workaround). Made it **worse**: gateway runs as container main-process; on exit the whole **container** cycles every ~15–20s and the dashboard never comes up.
- ❌ **"Don't publish port 8642"** — this appeared to stabilize it but was a **WRONG CONCLUSION from a too-short/noisy test**. The official docs publish 8642 (it has `API_SERVER_KEY` auth) and the dashboard needs it. Do not treat unpublishing 8642 as the fix.
- ❌ **Blaming the migrated data.** Bisected exhaustively: fresh-empty, config.yaml-only, +gateway_state+profiles, +.env, +state.db+sessions+memories, +skills+kanban+hooks+cron+DBs — **all stable** (but those tests all had **dashboard off / no published ports**, which was itself a confound). Full migrated data with dashboard OFF + no ports = stable; the differentiator was the dashboard/ports/**environment**, not the data. **Data is not the cause.**
- ❌ **`docker exec` foreground diagnostics / diag containers** — the image tears down `sleep infinity` diag containers; `HERMES_LOG_LEVEL=DEBUG` does **not** enable debug logging; `ss`, `py-spy`, `xxd` are **not** in the image (use `/dev/tcp`, `/proc/net/tcp`, `/opt/hermes/.venv/bin/python`).
- ❌ **Model-call-hang theory** — DISPROVEN. Direct OpenRouter calls work fast (`stealth/ox-alpha` ~1.9s, `google/gemini-3.6-flash` ~1.5s, HTTP 200). Model provider + `OPENROUTER_API_KEY` are fine.
- ❌ **Loop-watchdog stack-dump hunt** — no dump emitted; not clearly the trigger.
- ✅ Ruled out: OOM (≈15 GB free), disk (928 GB free), state.db corruption (`integrity_check ok`), the 4 profiles (not auto-started), role-detection bug #49196 (0.20.5 reads container argv, not PID1).

---

## 7. NEXT STEPS / open decision

**Immediate:** read the soak result (background task `bd11f4s4u`, output file under the session `tasks/` dir).
- **Stable (0 restarts, dashboard 302 for 20 min)** → the crash was assistant-induced load; system is usable. Then verify the dashboard **login actually completes** (not just the login page) and that `api_server` 8642 responds.
- **Still cycling** → environmental containerd-2.x/s6 bug **confirmed**. Then choose:
  1. **Roll back** to the host install (backup intact; returns to Arch-2 limitations). Rollback = `docker stop hermes && docker rm hermes; rm -rf /root/.hermes && mv /root/.hermes.backup-pre-arch3 /root/.hermes`, revert `terminal.backend`, restart host Hermes.
  2. **Downgrade Docker/containerd** on the WSL host to a **containerd-1.x** version (Docker < 28.5.2) — documented-stable runtime; then the container migration should work. Host-level change.
  3. Pin an **older Hermes image (v0.14.x)** — pre-s6-overlay (tini); but config schema is `_config_version: 39` (from 0.20.5) and may be incompatible with a downgrade → risky.

**Do NOT** keep patching data/config/permissions — that path is exhausted (§6).

### Runbook (G0.2) corrections needed
1. Launch: the runbook's `--memory 4g --cpus 2` should be **removed** (docs impose no caps; the cap may starve the gateway). Publish **both** 8642 and 9119 (per docs), not 9119-only.
2. Data must be chowned to the container user (uid 10000); image boot-chown misses `kanban`.
3. Dashboard requires an auth provider on non-loopback bind — set `dashboard.basic_auth` (+ `secret` for session persistence).
4. Remove/disable host-only MCP servers (`qmd`) that aren't in the image.
5. Repos must NOT be mounted under `/root` (private, 700) — mount at a path the uid-10000 gateway can traverse (e.g. `/workspaces`), OR the launch must make `/root` traversable durably.
6. `bootstrap-tools.sh` installs apt tools into the ephemeral layer — make it auto-run on container start, or install to `/opt/data`.
7. Gate-1 `pkill -f 'hermes-agent'` matches its own invoking shell — narrow the pattern.
8. Add a **runtime pre-check**: `docker info | grep containerd` — if containerd 2.x, warn about the s6-overlay restart-loop risk.

---

## 8. Other blind spots flagged (not yet resolved)

- **Host nightly cron** `/etc/cron.d/hermes_nightly`: 4 jobs (03:00–06:00) run `scripts/hermes/scheduled_domain_runner.py` **as root** against `/root/workspaces/apexai-os-meta` (now uid-10000-owned) → likely git "dubious ownership" failures + decoupled from the container. Review/adjust.
- **Old host install** present but not running: `/usr/local/lib/hermes-agent`, `/usr/local/bin/hermes*` (+ `.orig.pre-archimp01` backups), and a guarded `hermes()` function in `/root/.bashrc` (ext4-guard). Footgun: could start a 2nd Hermes on the same `~/.hermes`. Consider neutralizing post-migration.
- **Reboot survival**: WSL `systemd=true` + docker `enabled` + `--restart unless-stopped` → recovers once WSL is up; but **WSL itself may not auto-start on Windows boot** — confirm if always-on is desired.
- **Cost**: auxiliary model uses a **paid** OpenRouter SKU (`google/gemini-3.6-flash`); default model `stealth/ox-alpha`. Set `auxiliary.free_only: true` to cap.
- **Provisioning red herring**: launching WSL via the Start-menu "Ubuntu" app triggered a first-run OOBE account wizard ("Create a default Unix user: gehma") that is unrelated — do not create that account; use `wsl -u root ...` from PowerShell.

---

## 9. Sources

### Web searches run (queries)
1. `nousresearch hermes-agent gateway restart loop docker container gateway-default`
2. `hermes-agent docker migrate host install to container ~/.hermes config profiles`
3. `hermes-agent gateway_state.json migrated_from legacy-container-cmd profiles reconcile`
4. `hermes-agent docker single container "gateway run" CMD s6 gateway-default restart loop dashboard`
5. `NousResearch hermes-agent docker dashboard "network error" sign in single container api_server not reachable`
6. `hermes-agent docker correct way run gateway and dashboard two containers vs one HERMES_DASHBOARD compose`
7. `NousResearch hermes-agent s6-overlay containerd 2.x signal restart loop fixed version resolution`
8. `hermes-agent docker restart loop containerd 2.x workaround docker run --init stop-signal S6_ environment fix`

### Key source URLs (verified)
- Restart loop / containerd 2.x (PRIMARY): https://github.com/NousResearch/hermes-agent/issues/35394 and https://github.com/NousResearch/hermes-agent/issues/35393
- Dashboard auth-gate ("no longer works"): https://github.com/NousResearch/hermes-agent/issues/59113
- Dashboard starts per-profile gateways / role detection: https://github.com/NousResearch/hermes-agent/issues/49196
- Signal-initiated shutdown persists stopped: https://github.com/NousResearch/hermes-agent/issues/42675
- s6-log lock collision (multi-container shared volume): https://github.com/NousResearch/hermes-agent/issues/34457
- `gateway run` auto-supervise PR: https://github.com/NousResearch/hermes-agent/pull/33583
- s6-overlay supervision PR: https://github.com/NousResearch/hermes-agent/pull/31760
- Dashboard STOPPED when active profile differs: https://github.com/NousResearch/hermes-agent/issues/23457
- Per-profile gateway status blind: https://github.com/NousResearch/hermes-agent/issues/69143
- Official Docker docs: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Official Docker docs (repo md): https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/docker.md
- Web dashboard docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard

### Local reference docs (in this repo)
- `apex-meta/AI-Snippets/AIFailure/HERMES-ARCHITECTURE-HISTORY-AND-DECISION.md`
- `apex-meta/orchestration/architecture-improvements/02-hermes-single-container-runtime/G0.2-MIGRATION-RUNBOOK.md`
- `scripts/hermes/bootstrap-tools.sh`, `scripts/hermes/tools-requirements.txt`
- `scripts/hermes/scheduled_domain_runner.py` (host cron target)

---

## 10. Fastest way for the next session to get oriented

1. Read the soak result first (§7).
2. Confirm the runtime: `wsl.exe -e bash -lc 'docker version; containerd --version'` — if containerd 2.x, expect the s6 restart-loop risk.
3. Check gateway health as the REAL user: `wsl.exe -e bash -lc 'docker exec -u 10000 -e HOME=/opt/data hermes /opt/hermes/.venv/bin/hermes gateway status'`.
4. Count internal restarts: `wsl.exe -e bash -lc 'docker logs --since 900s hermes | grep -c "Hermes Gateway Starting"'` (1 = stable).
5. Everything runs in WSL via `wsl.exe -e bash -lc '...'` as root; the container's gateway user is uid 10000 / HOME `/opt/data`.
