# OpenProject Resource-Hub Smoke-Matrix (Entwurf)

Ziel: automatische Happy-Path-Smokes gegen AnythingLLM-Handler / OpenProject API.
Scope: **aktive Resource-Hubs** mit `operation=` (kein Deprecated).

Anzahl Hubs: **58**

## Stufen

| Stufe | Was | Risiko | CI |
| --- | --- | --- | --- |
| **L0** | Health / Auth (token, `/api/v3`) | keines | immer |
| **L1** | `operation=list` (ggf. leere Collection ok) | read-only | immer |
| **L2** | `list` → erstes Element → `get` | read-only | immer |
| **L3** | `create` → assert → `delete` (oder mark cancel) | schreibt Testdaten | nightly / manual gate |
| **L4** | Domain-Flows (Meeting+Participant, WP create+comment) | höher | selektiv |

## Assertions (gemeinsam)

- HTTP/`handler` nicht `OpenProject-Fehler 4xx/5xx` (außer bewusst 403)
- Return **nicht** rohes HAL-`{` für Collections → Markdown-Tabelle mit Header `| --- |`
- `create`-Returns: ID erkennbar (Tabelle oder `#n`)
- Timeout Skill ≤ 15s (Meetings/Ingest separat)

## L1 — list

| Hub | list | Notes |
| --- | --- | --- |
| `openproject-documents` | ✓ | leer ok |
| `openproject-grids` | ✓ |  |
| `openproject-groups` | ✓ | leer ok |
| `openproject-help-texts` | ✓ |  |
| `openproject-meetings` | ✓ |  |
| `openproject-memberships` | ✓ |  |
| `openproject-news` | ✓ |  |
| `openproject-notifications` | ✓ | 403 möglich → expect/skip |
| `openproject-portfolios` | ✓ | leer ok |
| `openproject-principals` | ✓ |  |
| `openproject-programs` | ✓ | leer ok |
| `openproject-project-phase-definitions` | ✓ |  |
| `openproject-projects` | ✓ |  |
| `openproject-queries` | ✓ |  |
| `openproject-recurring-meetings` | ✓ |  |
| `openproject-relations` | ✓ |  |
| `openproject-reminders` | ✓ |  |
| `openproject-roles` | ✓ |  |
| `openproject-sprints` | ✓ | leer ok |
| `openproject-statuses` | ✓ |  |
| `openproject-time-entries` | ✓ | leer ok |
| `openproject-users` | ✓ |  |
| `openproject-versions` | ✓ |  |
| `openproject-views` | ✓ |  |
| `openproject-work-packages` | ✓ |  |
| `openproject-workspaces` | ✓ |  |

## L2 — list→get

| Hub | Quelle ID | get |
| --- | --- | --- |
| `openproject-documents` | aus list-Zeile | ✓ |
| `openproject-grids` | aus list-Zeile | ✓ |
| `openproject-groups` | aus list-Zeile | ✓ |
| `openproject-help-texts` | aus list-Zeile | ✓ |
| `openproject-meetings` | aus list-Zeile | ✓ |
| `openproject-memberships` | aus list-Zeile | ✓ |
| `openproject-news` | aus list-Zeile | ✓ |
| `openproject-notifications` | aus list-Zeile | ✓ |
| `openproject-portfolios` | aus list-Zeile | ✓ |
| `openproject-programs` | aus list-Zeile | ✓ |
| `openproject-project-phase-definitions` | aus list-Zeile | ✓ |
| `openproject-projects` | aus list-Zeile | ✓ |
| `openproject-queries` | aus list-Zeile | ✓ |
| `openproject-recurring-meetings` | aus list-Zeile | ✓ |
| `openproject-relations` | aus list-Zeile | ✓ |
| `openproject-roles` | aus list-Zeile | ✓ |
| `openproject-sprints` | aus list-Zeile | ✓ |
| `openproject-time-entries` | aus list-Zeile | ✓ |
| `openproject-users` | aus list-Zeile | ✓ |
| `openproject-versions` | aus list-Zeile | ✓ |
| `openproject-views` | aus list-Zeile | ✓ |
| `openproject-work-packages` | aus list-Zeile | ✓ |

## L3 — create→cleanup

**Write-confirm (DEC-0054):** If `OP_SKILL_WRITE_CONFIRM` is on (default; or via `LEXICON_OP_WRITE_CONFIRM`), mutating creates without `confirmed=true` return „Bestätigung erforderlich (Skill)“. The smoke runner treats that as **expected SKIP/PASS** (no write, no orphan) so `--level L3` stays green without disabling the gate. To exercise real create→delete, pass `confirmed=true` in fixtures or set `OP_SKILL_WRITE_CONFIRM=0` for a dedicated write lab.


| Hub | create params (Minimum) | cleanup |
| --- | --- | --- |
| `openproject-attachments` | aus plugin/OpenAPI form ableiten | delete |
| `openproject-grids` | aus plugin/OpenAPI form ableiten | manuell / cancel state |
| `openproject-groups` | name; delete | delete |
| `openproject-meetings` | title, startTime ISO+TZ, duration PT1H, project_id; optional participant_ids | delete |
| `openproject-memberships` | project + principal + roles; delete | delete |
| `openproject-news` | title + project; delete | delete |
| `openproject-projects` | name, identifier (unique); delete mit confirmed | delete |
| `openproject-queries` | name; delete | delete |
| `openproject-recurring-meetings` | aus plugin/OpenAPI form ableiten | delete |
| `openproject-relations` | aus plugin/OpenAPI form ableiten | delete |
| `openproject-time-entries` | hours, spentOn, project/wp; delete | delete |
| `openproject-users` | login/email… vorsichtig; eher skip in shared demo | delete |
| `openproject-versions` | name + project; delete | delete |
| `openproject-views` | aus plugin/OpenAPI form ableiten | manuell / cancel state |
| `openproject-work-packages` | subject + project link/id; delete | delete |

## L4 — Flows (Beispiele)

1. **Meeting:** create (ki-pm) → get → optional participant → delete
2. **Work package:** create in ki-pm → get → comment-add (falls Hub) → delete
3. **Memory:** memory-store Fakt → memory-recall gleiche group_id (Graphiti-safe)

## Nicht in L1–L3 (andere Ops / Forms)

- `openproject-actions-and-capabilities`: `list_actions, get_action, list_capabilities, get_global_context, get_capabilities`
- `openproject-activities`: `get, update, list_attachments, add_attachment, list_emoji_reactions, toggle_emoji_reaction`
- `openproject-budgets`: `get, get_of_a_project`
- `openproject-categories`: `get, list_of_a_project, list_of_a_workspace`
- `openproject-collections`: `get_aggregated_result`
- `openproject-configuration`: `get, get_project`
- `openproject-custom-actions`: `get, execute`
- `openproject-custom-fields`: `get_item, get_item_branch, get_items`
- `openproject-custom-options`: `get`
- `openproject-file-links`: `delete, get, download, open, list_project_storages, get_project_storage, open_project_storage, list_storages`…
- `openproject-forms`: `get_or_validate`
- `openproject-oauth-2`: `get_oauth_application, get_oauth_client_credentials`
- `openproject-posts`: `get`
- `openproject-previewing`: `preview_markdown_document, preview_plain_document`
- `openproject-priorities`: `list_all, get`
- `openproject-project-phases`: `get`
- `openproject-query-columns`: `get`
- `openproject-query-filter-instance-schema`: `list_query_filter_instance_schemas_for_project, list_query_filter_instance_schemas, get, list_query_filter_instance_schemas_for_workspace`
- `openproject-query-filters`: `get`
- `openproject-query-operators`: `get`
- `openproject-query-sort-bys`: `get`
- `openproject-revisions`: `get`
- `openproject-root`: `get`
- `openproject-schemas`: `get_the`
- `openproject-time-entry-activities`: `get_time_entries_activity`
- `openproject-types`: `list_available_in_a_project, list_all, get, list_available_in_a_workspace`
- `openproject-user-preferences`: `get_my_preferences, update`
- `openproject-user-working-times`: `list_user_non_working_times, create_user_non_working_time, delete_user_non_working_time, get_user_non_working_time, update_user_non_working_time, list_user_working_hours, create_user_working_hours, delete_user_working_hours_record`…
- `openproject-values-property`: `get_values_schema`
- `openproject-wiki-pages`: `get`
- `openproject-work-schedule`: `list_days, list_non_working_days, create_non_working_day, delete_non_working_day, get_non_working_day, update_non_working_day, list_week_days, update_week_days`…

## Laufumgebung

- Container-Netz: Skills wie AnythingLLM (`openproject_base_url=http://web:8080`)
- Token: provision-secrets (nicht committen)
- Fixture-Projekt: **ki-pm** (`project_id=3`), User Admin (`4`)
- Parallelität: L1 parallel ok; L3 seriell (Lock/Conflicts)

## Runner (L0–L3)

```bash
cd ~/dev/skills/agent-skills
node scripts/smoke-openproject-skills.cjs              # L0–L2 (default)
node scripts/smoke-openproject-skills.cjs --level L3   # + create→delete (writes!)
node scripts/smoke-openproject-skills.cjs --level L1
```

Liest `OPENPROJECT_API_KEY` aus Env oder `~/dev/ki-basis/docker/.env`.
Default base: `http://127.0.0.1:8084`. Fixture: `SMOKE_FIXTURE_PROJECT_ID=3` (ki-pm).
L3 priority (serial): meetings, work-packages, news, versions, time-entries — users skip.
Exit ≠0 bei Regression.



## Slot-bind pilot (schema-aware fill)

Phase A meta-skill `platform/ops/slot-bind` binds utterance → hub args before `openproject-work-packages` `create_project`.

- Direct smoke (from skill dir): `GLINER_SERVICE_URL=http://127.0.0.1:8087 node -e '… h.runPipeline({utterance, hubId, operation, group_id}) …'` — expect `decision=execute`, `id="3"` (ki-pm), `subject=<quoted title>`.
- Fail-open: unreachable GLiNER must still execute via lexicon + heuristics.
- Hub L3 still covers create→delete; slot-bind smoke is binder-only unless you chain hub create with bound args.
- Do not delete fixture WP **#59** in ad-hoc probes.
- UI/agent path: Chat Prompt Slot-Bind block; Phase B aibitat hook is design-only / flag-off (see ki-basis plan).

## Umsetzung (Vorschlag)

1. `scripts/smoke-openproject-skills.cjs` (oder pytest) liest CATALOG/plugin.json
2. Filter: `active && operation param && !Deprecated`
3. Matrix-YAML: overrides (skip, expect_empty, expect_403, create_fixture)
4. Exit ≠0 bei Regression (Format/5xx)
