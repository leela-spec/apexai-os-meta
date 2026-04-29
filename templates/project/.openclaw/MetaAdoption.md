---
class: trace
role: LOG
surface: meta_adoption
quality: developing
scope: project
purpose: Record which ApexAI_OS meta release or commit this project has adopted.
dependencies:
  - .openclaw/ProjCard.md
  - .openclaw/SSOT_INDEX.md
---

# Meta Adoption Record

## Boundary

MetaAdoption records the reviewable adoption trace from the meta repo into this project. It is not runtime config and must not replace `openclaw.json` or any local runtime setup.

Meta releases move downward only through reviewable project PRs.

## adoption_record

| Field | Value |
|---|---|
| `adopted_release` | `none_yet` |
| `adopted_commit` | `none_yet` |
| `adoption_status` | `not_adopted` |
| `adopted_at` | `TBD` |
| `adoption_pr` | `TBD` |
| `local_overlay_notes` | `none_yet` |
| `deferred_items` | `none_yet` |

## adopted_release

| Release | Manifest path | Status | Notes |
|---|---|---|---|
| `TBD` | `TBD` | `not_adopted` | `TBD` |

## adopted_commit

| Repo | Commit | Status | Notes |
|---|---|---|---|
| `leela-spec/apexai-os-meta` | `TBD` | `not_adopted` | `TBD` |

## adoption_status

Allowed values:

- `not_adopted`
- `adoption_proposed`
- `adoption_in_review`
- `adopted`
- `partially_adopted`
- `superseded`
- `blocked`

Current status:

```text
not_adopted
```

## adopted_at

```text
TBD
```

## adoption_pr

```text
TBD
```

## local_overlay_notes

Local overlays may tighten the managed floor. They must not weaken managed governance, bypass escalation, bypass promotion, or create project-to-project authority.

```text
none_yet
```

## deferred_items

| Item | Reason deferred | Follow-up path |
|---|---|---|
| `TBD` | `TBD` | `TBD` |

## Update rules

- Update this file when a meta release or commit is proposed, adopted, superseded, or blocked.
- Keep adoption trace reviewable through PRs.
- Do not store runtime config here.
- Do not record private or project-raw data here.
