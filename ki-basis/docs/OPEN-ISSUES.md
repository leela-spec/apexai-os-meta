---
type: Issue Register
title: ki-basis open issues — machine-readable tracker
description: >
  Every unresolved item surfaced by the 2026-09-29 handover and performance review, as structured data.
  One entry per issue: why it exists, what could go wrong, the fix, and priority/impact/effort. Source of
  truth for what to test/change next; supersedes the prose checklist in HANDOVER-2026-09-29-open-items.md §4.
created: 2026-09-29
okf_version: "0.2"
schema:
  id: "durable, stable across edits"
  title: "short imperative"
  why: "why this condition exists (root cause / origin)"
  risk: "what happens if left unaddressed"
  fix: "concrete next action"
  priority: "P0 critical | P1 high | P2 medium | P3 low"
  impact: "quantified where measured, else qualitative"
  effort: "low | med | high"
  status: "open | in_progress | resolved | wontfix"
  verified_live: "true = confirmed by direct inspection 2026-09-29; false = inferred from file read only"
  relates_to: "register ID(s) in InstallationInsights.md, if any"
  source: "file/section this issue was surfaced from"
see_also:
  - HANDOVER-2026-09-29-open-items.md — full prose context and evidence for each issue below
  - InstallationInsights.md — R1–R12 ranked failure register (relates_to targets)
  - PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md
current_truth: ki-basis/docs/INFRASTRUCTURE.md
---

# ki-basis open issues

Read `schema` above once; every entry below follows it exactly. Ordered by priority, then impact.

```yaml
issues:
  - id: I08
    title: Verify leela-op178 SECRET_KEY_BASE is not committed to git in plaintext
    why: "compose.shared-db.yaml was authored with SECRET_KEY_BASE inline as a literal value, not a ${VAR}"
    risk: "credential leak if committed; matches a recurring pattern (Paperless token leaked twice earlier in this project)"
    fix: "git log --all -- leela-op178/compose.shared-db.yaml; if tracked with the literal value, rotate SECRET_KEY_BASE and move it to .env.shared-db"
    priority: P0
    impact: "full OpenProject session-signing key compromise if leaked"
    effort: low
    status: open
    verified_live: true
    relates_to: [R1]
    source: "leela-op178/compose.shared-db.yaml (read directly, 2026-09-29)"

  - id: I03
    title: Re-audit Paperless/Firefly/Nginx/Hermes for the same 127.0.0.1-vs-0.0.0.0 publish bug fixed on OpenProject
    why: "OpenProject was ECONNREFUSED from Windows until its port was republished to 0.0.0.0; Paperless/Firefly/Nginx/Hermes still publish as 127.0.0.1:{PORT}:... on both stacks and had never been re-tested after that fix"
    risk: "closed by live test -- kept for provenance. All 12 ports (OpenProject/Firefly/Paperless/Nginx/Hermes-gateway/Hermes-dashboard x private+community) answered from Windows via curl on 127.0.0.1, despite most still being published as 127.0.0.1 (not 0.0.0.0) in compose. WSL2's default localhostForwarding relays Windows-localhost to the VM's own localhost regardless of which local address the container's docker-proxy bound to, for this native-WSL2-dockerd setup -- so the 0.0.0.0 republish was sufficient for OpenProject but is not a universal requirement for every service. A first pass with a 3s curl timeout falsely showed 2 ports as unreachable (private Firefly :8086, community OpenProject :9082) -- both were only slow to answer, not blocked; re-tested at 8s and both returned HTTP 302. First-hit latency on a cold WSL2 localhost-forward, not a connectivity fault -- worth remembering before re-flagging a port as broken."
    fix: "no fix required -- resolved. If a future port genuinely fails, retest at >=8s timeout before concluding it is blocked (see why); only then apply the OpenProject-style 0.0.0.0 republish."
    priority: P3
    impact: "none currently; all agent-facing service ports on both stacks are confirmed Windows-reachable"
    effort: low
    status: resolved
    verified_live: true
    relates_to: [R11]
    source: "live curl sweep from Windows (git-bash), 2026-09-29: private 8083/8086/8010/8084/8642/9119 and community 9082/9086/9010/9084/9642/9219, all HTTP 200/302/404 (listening+responding)"

  - id: I01
    title: Cap leela-op178-openproject worker env vars
    why: "private OpenProject runs on defaults (no OPENPROJECT_WEB_WORKERS/BACKGROUND_WORKERS set); community's equivalent instance already sets both to 1 and uses ~1GB less RAM for the same workload"
    risk: "none if left alone beyond continued excess RAM use; contributes to host memory pressure under load"
    fix: "add OPENPROJECT_WEB_WORKERS=1, OPENPROJECT_BACKGROUND_WORKERS=1 to leela-op178/.env.shared-db; docker compose up -d to recreate; measure with docker stats before/after"
    priority: P1
    impact: "~0.5-1.0 GB RAM saved, measured delta from live community comparison"
    effort: low
    status: open
    verified_live: true
    relates_to: []
    source: "PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md #1"

  - id: I02
    title: Add MALLOC_ARENA_MAX=2 to both OpenProject containers
    why: "glibc's default per-thread memory-arena behavior bloats Ruby/Puma RSS under Rails; env-only fix, no image change"
    risk: "none beyond continued excess RAM use; slight CPU tradeoff if applied"
    fix: "add MALLOC_ARENA_MAX=2 to both leela-op178 and community-openproject env, recreate, measure with docker stats"
    priority: P1
    impact: "~10-30% of Ruby RSS, roughly 0.4-1.0 GB combined across both instances"
    effort: low
    status: open
    verified_live: false
    relates_to: []
    source: "PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md #2"

  - id: I07
    title: Add per-container mem_limit to both OpenProject instances and Paperless
    why: "no container in either stack (private or community) currently has any memory limit set"
    risk: "a single runaway service can consume unbounded host memory; this exact failure mode (unbounded VM memory) is what caused the Docker-Desktop host-freeze incident (R1 performance evidence)"
    fix: "add mem_limit (e.g. 1.5G for OpenProject, 768M for Paperless) under each service in the relevant compose file"
    priority: P1
    impact: "bounds worst-case memory use; prevents recurrence of the Sep 3-4 OOM/freeze incident class"
    effort: low
    status: open
    verified_live: true
    relates_to: [R1]
    source: "PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md #6; docker inspect confirms no limits set"

  - id: I04
    title: Create a dedicated least-privilege OpenProject agent account
    why: "the agent-skills openproject client currently authenticates as the built-in admin account (login: admin, admin: true), not a scoped agent identity"
    risk: "any skill bug or prompt-injection through the skill has full OpenProject admin blast radius instead of a scoped one"
    fix: "follow ki-basis/docs/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md; create the account, issue its own token, update ~/.config/openproject/op.env"
    priority: P2
    impact: "reduces blast radius of a compromised or misbehaving skill call; not currently exploited, hardening only"
    effort: med
    status: open
    verified_live: true
    relates_to: [R11]
    source: "live opCall.js whoami output, 2026-09-29; ki-basis/docs/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md"

  - id: I05
    title: Decide and fix community Hermes' empty repo-clone workspace
    why: "community Hermes uses a Docker named volume (community_hermes_workspaces) for /root/workspaces instead of private Hermes' bind mount; the volume was created fresh at the 2026-09-26 WSL2 cutover and nothing has been cloned into it since"
    risk: "if community Hermes is expected to operate on repo clones the way private Hermes does, it currently cannot -- silent capability gap, not a crash"
    fix: "check lika-community/SOUL.md and its actual task scope first (may be Telegram/PM-facing only, not a code agent, by design); if clones are needed, populate the volume"
    priority: P2
    impact: "unknown until scope is confirmed; private Hermes has 3.5GB of real clones (apexai-os-meta 1.8G, MasterOfArts 1.7G, Investment 35M, acim-secular 17M) as the comparison baseline"
    effort: low
    status: open
    verified_live: true
    relates_to: []
    source: "docker volume inspect community_hermes_workspaces, 2026-09-29"

  - id: I10
    title: Do not enable .wslconfig experimental autoMemoryReclaim=gradual
    why: "documented as a candidate RAM-reclaim tuning option"
    risk: "reported (microsoft/WSL#11066) to break a natively-run dockerd inside WSL2 -- exactly this engine's setup -- and to conflict with zswap"
    fix: "no action required; this is a do-not, not a to-do -- leave .wslconfig as-is"
    priority: P2
    impact: "prevents a self-inflicted engine break if someone applies this later without checking prior findings"
    effort: low
    status: wontfix
    verified_live: false
    relates_to: []
    source: "PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md #7"

  - id: I11
    title: Guard against community's legacy Docker-Desktop-era compose.yaml being run by accident
    why: "lika-community/compose.yaml (the pre-WSL2 original, kept as rollback reference) still binds a OneDrive-synced host path directly into the Hermes container; the live variant (compose.wsl.yaml) already replaced this with a proper named volume"
    risk: "a cloud-sync client can rewrite/lock files underneath a running container; this is the exact R6 anti-pattern from the failure register -- currently dormant, not active"
    fix: "rename the legacy file (e.g. compose.yaml.docker-desktop-rollback-only) or add a runtime guard that refuses to start it against live data"
    priority: P2
    impact: "dormant risk; would only trigger if the wrong compose file is invoked"
    effort: low
    status: open
    verified_live: true
    relates_to: [R6]
    source: "lika-community/compose.yaml vs compose.wsl.yaml (read directly, 2026-09-29)"

  - id: I06
    title: Cap private Paperless worker env vars
    why: "private Paperless runs on defaults; community's equivalent already sets PAPERLESS_WORKERS/TASK_WORKERS/THREADS_PER_WORKER=1"
    risk: "none beyond continued minor excess RAM use"
    fix: "add PAPERLESS_WORKERS=1, PAPERLESS_TASK_WORKERS=1, PAPERLESS_THREADS_PER_WORKER=1 to ki-basis/.env, recreate"
    priority: P3
    impact: "~0.1-0.2 GB RAM, small but free and already proven safe on the community side"
    effort: low
    status: open
    verified_live: false
    relates_to: []
    source: "PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md #5"

  - id: I09
    title: Prune 3 stale exited Hermes containers
    why: "hermes-d04f865b, hermes-d397cf57 (exited 3 weeks ago), hermes-preext-20260826 (exited 4 weeks ago) are leftovers from earlier Hermes runtime experiments (single-container Arch-3 attempt, R3)"
    risk: "none functionally; clutters docker ps output, trivial disk use"
    fix: "confirm no current compose project references them, then docker rm each"
    priority: P3
    impact: "cosmetic/hygiene only"
    effort: low
    status: open
    verified_live: true
    relates_to: [R3]
    source: "docker ps -a, 2026-09-29"

  - id: I12
    title: Apply the R1-R10 install-script requirements as acceptance criteria for any future from-scratch install
    why: "InstallationInsights.md distills 3 months of rebuilds into 10 concrete install-script requirements; this issue register only adds to that baseline, it does not replace it"
    risk: "a future install attempt that skips this checklist risks repeating the Docker-Desktop detour and its dependent failures"
    fix: "treat InstallationInsights.md section 3 as a literal pre-flight checklist before any reinstall or new-machine setup"
    priority: P3
    impact: "prevents a repeat of the ~3-month rebuild cycle this project already paid for once"
    effort: low
    status: open
    verified_live: false
    relates_to: [R1, R1b, R2, R3, R4, R5, R6, R7, R8, R9, R10]
    source: "InstallationInsights.md §3"
```
