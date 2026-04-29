# ApexAI_OS Project Template

## Purpose

This template is the minimal project-local scaffold for an isolated ApexAI_OS project repo.

It is not a second meta repo and not a project-to-project bridge.

## Use

Apply this template when creating a project repo such as `apexai-project-app-dev`.

A project repo should receive:

1. an adopted copy of the current meta kernel release (`managed/` and `docs/`)
2. this `.openclaw/` project control package
3. project-local expert agents or project files as needed
4. project-local overlays only where they tighten the managed floor

## Included project control surfaces

- `.openclaw/ProjCard.md`
- `.openclaw/OpState.md`
- `.openclaw/SSOT_INDEX.md`
- `.openclaw/SigMat.md`
- `.openclaw/MetaAdoption.md`
- `.openclaw/SessionExports/`
- `.openclaw/NightReports/`
- `.openclaw/QA/`
- `.openclaw/LearningCandidates/`
- `user/AGENTS.md`
- `agents/`

## Direction of movement

- Meta releases move down into projects by reviewable project PR.
- Project learnings move up only as sanitized `LearningCandidate` packets.
- Project truth changes remain project-local unless explicitly promoted to meta through review.

## First validation

Before treating a project as active, verify:

- all four required `.openclaw` control surfaces exist
- `MetaAdoption.md` names the adopted meta release or commit
- `OpState.md` has a bounded next queue
- `SSOT_INDEX.md` does not claim truth ownership that does not exist yet
- `SigMat.md` uses reference-backed evidence rather than unsupported scores
