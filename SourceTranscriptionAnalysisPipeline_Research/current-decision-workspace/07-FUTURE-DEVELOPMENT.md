# Future Development — Deferred Transcript/Video Knowledge Features

**Status:** OUT OF CURRENT SCOPE  
**Date:** 2026-08-20

This file prevents deferred ideas from silently returning to the current production architecture.

## FD01 — Visual-only video evidence

**Operator decision:** out of scope for the current transcript-to-knowledge project.

Future project question:
- when charts, slides, code, demonstrations, or other visual information materially exceed the spoken transcript, add a conditional visual/multimodal evidence path.

Candidates to re-research at that time:
- current multimodal long-context models;
- existing video indexing/evidence systems;
- frame/scene selection before semantic analysis;
- evidence alignment between transcript timestamps and visual events.

Do not add this branch to current architecture merely because a multimodal model exists.

## FD02 — Non-factual provenance policy

**Operator decision:** out of scope for now.

Future question:
- what provenance should be required for opinions, predictions, anecdotes, interpretations, recommendations, and externally enriched knowledge when exact source evidence is not mandatory?

The future design may need claim-type-specific provenance rather than one universal quote requirement.

## FD03 — Broader knowledge-base integration

After a trustworthy per-source knowledge product exists, evaluate how it should feed a persistent KB/wiki, including:
- source-to-many-page compilation;
- contradiction preservation;
- entity/concept updates;
- retrieval/indexing;
- external information enrichment;
- incremental source updates.

Do not use future KB requirements to overbuild the first working transcript-to-knowledge pipeline.