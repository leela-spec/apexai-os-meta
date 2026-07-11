# APEX Operator Template System

**Package status:** Production-ready blank template family  
**Scope:** J1-J12 plus the conditional J6 Skip Marker  
**Repository authority checked:** `leela-spec/apexai-os-meta`, branch `main`, read only  
**Research and validation date:** 2026-07-11

This package turns the accepted APEX operator-output architecture into usable Markdown work artifacts. It does not replace skill contracts, create runtime behavior, authorize execution, write project state, or change the repository.

## Start here

1. Choose the artifact by operator job in [Template Family Overview](03_TEMPLATE_FAMILY_OVERVIEW.md).
2. Copy the matching blank file from [`templates/`](templates/).
3. Replace every `{{UPPER_SNAKE_CASE}}` placeholder, remove inapplicable optional sections, preserve the visible lifecycle language, and keep the compact machine handoff last.

Use [Master of Arts Example Fragments](examples/master-of-arts-example-fragments.md) only as illustrations. They are fictionalized demonstrations, not current project truth and not additional schema.

## Package contents

- [Research Findings](01_RESEARCH_FINDINGS.md): repository, user-story, project-source, and current web evidence translated into template implications.
- [Design Decision Matrix](02_DESIGN_DECISION_MATRIX.md): material alternatives, selections, evidence, and trade-offs.
- [Template Family Overview](03_TEMPLATE_FAMILY_OVERVIEW.md): lifecycle map, ownership boundaries, handoffs, and selection guide.
- [`templates/`](templates/): twelve primary templates plus the conditional Skip Marker.
- [Example Fragments](examples/master-of-arts-example-fragments.md): difficult sections demonstrated with Master of Arts workflow content.
- [Template Family Review](validation/template-family-review.md): final structural, lifecycle, non-duplication, and usability checks.
- [`package-manifest.yaml`](package-manifest.yaml): package inventory and authority metadata.

## Operating loop

```text
Project state
  -> weekly direction
  -> next-day outline
  -> executable flow
  -> prompt access
  -> execution evidence
  -> result interpretation
  -> usage learning
  -> status review
  -> durable KB update
  -> confirmed project overview
  -> advisory routing into later execution
```

The loop contains deliberate human gates. A result is not a merge. Approval is not proof of writing. A prepared update is not accepted truth. A recommendation is not execution authority.

## Shared template grammar

Every primary artifact begins with a compact operator result card that makes four items visible without scrolling:

> **State or result:** What is ready, current, changed, blocked, or proposed.  
> **Outcome:** The value created or the current operational situation.  
> **Next action:** One best operator action.  
> **Review needed:** The decision, evidence gap, conflict, or `None`.

After that first screen, templates move through action, essential content, material review flags, compact provenance, and a minimum downstream handoff. The J6a Skip Marker is intentionally smaller and does not use a result card.

## Placeholder and section conventions

- `{{UPPER_SNAKE_CASE}}` means replace with a concrete value.
- `{{NONE_OR_VALUE}}` means state `None` explicitly when no item exists; do not leave it blank.
- A heading marked **include when material** is optional and should be removed when it adds no decision value.
- A heading marked **repeat per ...** may be copied as many times as the work requires.
- Choice guidance appears only where the accepted design or owning contract defines the concept. It is guidance, not a replacement enum.
- Relative links should keep a visible file path so the artifact remains usable in Markdown viewers that do not activate the link.
- YAML blocks at the end are compact presentation handoffs. The referenced owning contract remains authoritative.

## State language that must not collapse

| Stage | Owner | Safe visible language | Must not imply |
|---|---|---|---|
| Flow result | J7 | completed, partial, blocked, skipped, unknown | project state accepted |
| Candidate change | J7 | candidate, proposed, no change proposed | merge approved or written |
| Merge review | J9 | approved for merge, rejected, deferred, unresolved | durable write confirmed |
| Durable write | J10 | prepared, awaiting confirmation, executed, partial, skipped, blocked | accepted overview truth without result evidence |
| Project overview | J11 | confirmed accepted state with freshness | new candidate truth |
| Routing | J12 | recommended, operator approved, overridden, deferred | execution automatically authorized |

## Complexity rule

Add structure only when it improves one of four outcomes: comprehension, action, review, or downstream handoff. Do not preserve empty sections, duplicate upstream content, copy full schemas, or expand a one-line decision into a dashboard.

## Consequential source limitations

The live `PrecapWeek` skill references `.claude/skills/PrecapWeek/references/weekly-plan-output-contract.md`, but that referenced file was not retrievable from `main` during this run. J2 therefore projects the verified Step 3 design and the live skill behavior without asserting an unverified weekly packet schema.

A dedicated live J1 owner entrypoint and the expected Prompt Engineering entrypoint were also not verified through repository search. J1 and J5 remain bounded to their accepted Step 3 designs and the adjacent live contracts named in their authority blocks.

## Non-goals

This package contains no scripts, agents, schedulers, API calls, calendar writes, prompt execution, repository patches, or durable project-state changes. It is a presentation and handoff system only.
