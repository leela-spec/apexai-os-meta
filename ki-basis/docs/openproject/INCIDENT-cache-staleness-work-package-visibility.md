---
okf_version: "0.2"
type: incident
title: Work-package writes intermittently invisible until OpenProject restart — cache architecture needs review
description: Creating Epic/Feature/User story/Bug work packages, and separately a Hermes/Telegram-bot write, have each appeared to fail or go missing, then shown up correctly only after an OpenProject container restart or the next day. Root cause not proven; the instance's memcache-backed Rails cache (with no confirmed invalidation on type-to-project changes) is the leading suspect. A separate, confirmed DNS-alias collision on the shared Docker network was found during this investigation and is recorded as a related latent risk, not a proven cause.
tags: [openproject, caching, memcache, docker, dns, architecture, incident]
status: open
opened: 2026-10-03
program_ref: none — operational gap, not tied to a program task
---

# Work-package writes intermittently invisible until restart — cache/staleness investigation

## Symptom (reported twice, two different access paths)

1. **2026-10-03, earlier the same day** (via the `openproject` skill / API, Windows host →
   `leela-op178-openproject`): creating Epic/Feature/User story/Bug work packages failed or appeared
   not to take effect. After restarting the OpenProject container and starting a fresh chat session,
   the same operation succeeded immediately — verified live later this session (see "What's confirmed"
   below: all 4 types created and read back cleanly in Demo project on the first try, work package ids
   140–143).
2. **Earlier, a different system** — a Telegram bot driven by a Hermes agent, writing into OpenProject,
   produced a work package that "did not land" (wasn't visible on read) and only appeared the next day.
   Reported by the operator as the same general failure shape: a write that should be immediate instead
   needed a delay, or an unrelated event, before it was readable.

Both cases share the same shape: **a write, or an admin config change that should affect the next
write, is not reflected in the next read — and only becomes visible after some unrelated event
(container restart, elapsed time) rather than immediately.** That shape points at a caching or
read-path staleness problem, not at the underlying Postgres data itself (neither case showed actual
data loss — only delayed visibility).

## What's confirmed (2026-10-03, this session)

- `leela-op178-openproject` sets `OPENPROJECT_RAILS__CACHE__STORE=memcache`. Verified live:
  `docker exec leela-op178-openproject env | grep -i cache` → `OPENPROJECT_RAILS__CACHE__STORE=memcache`.
- The Rails cache backend is live and wired: `Rails.cache` is an `ActiveSupport::Cache::MemCacheStore`
  backed by a Dalli client connected to `127.0.0.1:11211` **inside the container's own network
  namespace** (verified via `bundle exec rails runner 'puts Rails.cache.inspect'`).
- `memcached` runs as an **in-container process** (`/usr/bin/memcached`, confirmed via `ps aux` inside
  the container) — it is not a separate shared container, and it is not shared between
  `leela-op178-openproject` and `community-openproject`; each has its own isolated memcached. **Cross-
  instance cache contamination between the two OpenProject instances is ruled out.**
- `community-openproject` has the **identical** `OPENPROJECT_RAILS__CACHE__STORE=memcache` config — the
  same cache architecture exists in both stacks, relevant if the Hermes/Telegram incident (item 2 above)
  shares a root cause with item 1.
- All 4 previously-problematic types (Epic, Feature, User story, Bug) **do** create successfully in
  Demo project right now (work package ids 140–143, created and read back clean this session) — the
  instance is not currently in the broken state, consistent with "restart cleared something and it has
  stayed clear since."
- **Separate, confirmed finding** (not proven to cause either symptom above, but a real landmine worth
  fixing on its own merits): `leela-op178-openproject` and `community-openproject` are both joined to
  the shared Docker network `shared-db-net` (created so both stacks can reach one Postgres cluster), and
  **both register the same DNS alias `openproject`** on that network — confirmed via
  `docker network inspect shared-db-net` (lists both containers) and `docker inspect <container>`
  (`Aliases` includes `openproject` for both, on that network). This is the same incident *class*
  already hit once before on this exact network (see the Docker/WSL2 migration history: a DNS alias
  collision between an orphaned old Postgres container and the new shared cluster caused real, if
  temporary, outages). Currently this does **not** reach either Hermes bot: `ki-basis-hermes` sits on
  `ki-basis-net` (only `leela-op178-openproject` carries the `openproject` alias there) and
  `community-hermes` sits on `community_internal` (only `community-openproject` carries it there) —
  neither Hermes container is attached to `shared-db-net` itself, confirmed via the same network
  inspection. So this is a latent risk, not currently an active cause — but it should be fixed (distinct
  aliases, or drop the generic one) before any new service is attached to `shared-db-net` and does a
  plain hostname lookup for `openproject`.

## Leading hypothesis (not yet proven)

OpenProject caches work-package **type-to-project enablement** (and/or other admin-config reads) via
`Rails.cache`, and the cache key for "types enabled for project N" is not invalidated when an admin
toggles a type's "Enable for all projects" switch in the UI. The DB row changes immediately, but a
stale cached answer keeps being served to API/UI create-attempts until either (a) the cache entry's TTL
expires naturally (could explain "the next day"), or (b) the memcached process is cleared, which a full
container restart does implicitly (explains why restarting `leela-op178-openproject` fixed today's
symptom). This would also explain why the type-enablement work documented in
`FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md` looked inconsistent in the moment — the UI toggle
may have worked correctly every time, with only the cache read lagging behind.

This has **not** been proven — no cache key was inspected directly, and no reproduction was attempted
(enable a type, immediately try to create against it, observe a 422, then flush memcache and retry
without restarting). That reproduction is the highest-value next step below.

## Cross-reference: a separate chat's full type-enablement attempt log (2026-10-03)

A different session that same day ran its own independent investigation into getting all 7 types
(Task, Milestone, Summary task, Feature, Epic, User story, Bug) usable everywhere — not yet aware
of this incident file when it ran. Recording its full attempt sequence here because at least one
step reproduces this incident's exact symptom shape (write/config-change not reflected on
immediate reread), and because it was interrupted before finishing a planned research step that
overlaps with "What's untried" below.

1. **API attempt**: `PATCH /api/v3/projects/8` with `_links.types` listing all 7 type hrefs →
   returned **`200 OK`**. Immediate reread (`type.list --project 8`, same session, no delay, no
   restart) → still only 3 types. At the time this was read as "the API silently ignores an
   unrecognized `_links` key" — **but no cache-flush-without-restart reproduction was attempted**,
   so this symptom alone cannot distinguish "the write was never applied" from "the write landed
   in Postgres but the read was served a stale cached answer," which is exactly this incident's
   open question. Do not treat this as independent confirmation of either hypothesis on its own.
2. **Schema probe** (a stronger, more likely cache-independent signal): `GET /api/v3/projects/schema`
   returns no `types` field in the resource schema at all; `GET /api/v3/projects/{id}/types` returns
   only a `self` link with no update/form affordance; `GET /api/v3/types/schema` 404s. A resource's
   *available-fields* schema is normally derived from application code, not a per-request cached
   value, so this is better evidence that no REST write path exists for this at all — independent
   of the caching question. Residual uncertainty, not fully ruled out: whether `.../schema` itself
   can also be served stale from `Rails.cache`.
3. **Live UI walkthrough** (operator-driven, not cached-data-dependent — these are checks for
   whether a *control exists on a page*, not whether a *value is current*): all 7 tabs on a Type's
   edit page (Details, Defaults, Form configuration, Workflows, Project attributes, Projects,
   Generate PDF) were opened live. None has an "active in new projects" control.
4. **"Enable for all projects" toggle** (Projects tab, type "User story"): operator switched it on
   and checked all 7 existing projects — confirmed via screenshot, all boxes checked. This was a
   successful write *and* read in the same session, no restart needed — relevant data point against
   "every admin-config write is currently stuck," though it doesn't rule out that this specific
   write/read pair uses a different (or already-flushed) cache key than type-to-new-project defaults.
   The separate Types-list "Active in new projects" column stayed unchecked for User story
   afterward — plausibly just a genuinely different, independently-tracked flag (see
   `FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md`), not necessarily a caching contradiction.
5. **Direct click on the "Active in new projects" column** in the Types list — confirmed
   not interactive.
6. **Subscription/licensing tangent**: checked `GET /api/v3/configuration` →
   `availableFeatures: []`, `triallingFeatures: []` — confirmed no Enterprise features active or
   trialing. Operator clarified the real question was whether the *Community* edition itself might
   be misconfigured, not an Enterprise-gating question. A web-research task was queued to check
   OpenProject's actual GitHub source for the `Type` model's `is_default` field (is it admin-settable
   at all, e.g. via `rails runner`, versus seed-only) and to check OpenProject's own community
   forum/issue tracker for this exact question — **that research was not completed; the session was
   interrupted before it ran.** This overlaps directly with item 2 below and should be done together.

## What's untried — do these next, in this order

1. **Reproduce without a full restart.** Pick a project + type currently disabled, enable it via the
   UI, immediately attempt `wp.create` via the skill. If it 422s, flush memcache directly from inside
   the container (e.g. `printf 'flush_all\r\n' | timeout 2 bash -c 'cat > /dev/tcp/127.0.0.1/11211'`)
   without restarting the container or process. If the create then succeeds, the cache-invalidation
   hypothesis is confirmed and narrowed specifically to memcache (rules out in-process Puma-worker
   memoization as the alternative explanation).
2. **Check OpenProject's own issue tracker** (`community.openproject.org`, `github.com/opf/openproject`)
   for known cache-invalidation bugs around `Type`/`Project` association changes — may be a known,
   already-fixed-in-a-later-version issue (this instance is pinned to 17.8.0). While there, check the
   actual `Type` model source for the `is_default` field (what sets it, whether it's admin-settable
   post-seed at all, e.g. via `docker exec leela-op178-openproject bundle exec rails runner
   "Type.find(4).update(is_default: true)"` — a normal, supported way to run one-off admin commands
   against a Dockerized OpenProject, not the same as writing to Postgres directly) versus seed-only
   with no runtime mutation path in any edition. This is the research step item 6 above queued but
   did not complete.
3. **Decide whether `OPENPROJECT_RAILS__CACHE__STORE=memcache` is the right choice for a single-
   container, low-traffic private pilot instance.** `:memory_store` (per-process, no network hop,
   trivially cleared on restart, no separate daemon to keep healthy) may remove this entire failure
   class for an instance running exactly one Puma process. This is an architecture decision for whoever
   owns `leela-op178`'s compose file, not something to change unilaterally.
4. **Fix the `shared-db-net` DNS alias collision** (`leela-op178-openproject` / `community-openproject`
   both aliased `openproject`) independently of the above — give each an explicit, distinct alias (or
   none) in their compose files' `shared-db-net` block, so a future service added to that network can't
   accidentally resolve to the wrong instance. Low urgency (nothing currently depends on the ambiguous
   alias) but cheap to fix now versus expensive to debug later.
5. **Get the actual timeline for the Telegram-bot/Hermes-agent incident** (item 2) — which OpenProject
   instance, what was read versus written, whether a restart happened in between. Without that, item 2
   stays an analogous prior incident, not a confirmed match to item 1's root cause.

## Accepted workaround until this is resolved

If a work-package create fails right after an admin enables a type for a project, don't assume the
enablement itself didn't take — retry in a few minutes, or restart the `leela-op178-openproject`
container (`docker restart leela-op178-openproject`, ~80s cold boot per
`RUNBOOK-openproject-17.8-operations.md` §4) before concluding the enablement is broken.

## Related
- [FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md](FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md) — the type-enablement gap this may have been masking or compounding.
- [RUNBOOK-openproject-17.8-operations.md](RUNBOOK-openproject-17.8-operations.md) §4 (keepalive) and §7 (ports) — container restart/health commands used in this investigation.
- `C:\GitDev\apexai-os-meta\ki-basis\scripts\hermes_telegram_intake.py` — the generic
  `check_reachable("openproject", 80)` hostname-resolution pattern that would be exposed if the
  `shared-db-net` alias collision above were ever triggered by a new service.
- [README.md](README.md) — this folder's index.
