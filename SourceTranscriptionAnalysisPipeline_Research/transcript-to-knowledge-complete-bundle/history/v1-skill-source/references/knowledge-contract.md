# Transcript Knowledge Contract

## Purpose

Use this contract after deterministic transcript preparation. The prepared transcript is source evidence; generated Macro, Meso, and Micro notes are derived knowledge and must remain traceable to source anchors.

## Epistemic tiers

### Macro

Create a compact global synthesis after Meso outputs exist.

Required content:
- one central thesis;
- 3-5 global takeaways;
- topic/entity taxonomy using `[[Wiki Links]]`;
- speaker/context profile limited to what the transcript or verified sources support;
- major contradictions, uncertainties, and raw-source reopen triggers.

Prefer validated Meso outputs as Macro input. Reopen raw transcript segments only for contradictions, missing evidence, or quote checks.

### Meso

Compile each bounded transcript chunk into one or more thematic modules.

Required content:
- module title and source time range;
- concepts/mechanisms and how they relate;
- arguments, premises, counterarguments, caveats, and scope limits;
- protocols/processes as ordered steps when actually present;
- `[[Topic]]` and `[[Entity]]` links;
- segment anchors for every important derived statement.

Chunk boundaries are transport boundaries, not semantic chapter boundaries. Merge or split themes semantically when evidence supports it.

### Micro

Extract only atomic, testable claims. Do not turn opinions, advice, predictions, or rhetorical statements into factual claims.

Each claim must contain:
- `claim_id`;
- one falsifiable proposition;
- exact quote copied from the transcript;
- source segment ID and timestamp if present;
- speaker label if present;
- speaker certainty/evidence posture as stated in the transcript;
- verification status;
- external evidence only when a live verifier actually found it.

Allowed verification statuses:
- `[CONFIRMED]`
- `[CONTRADICTED]`
- `[MIXED]`
- `[UNVERIFIED]`
- `[OPINION]`

Never promote a claim above `[UNVERIFIED]` merely because it sounds plausible.

## Source anchors

The deterministic preparer creates stable segment IDs such as `seg-000123`. Preserve them exactly.

When word timestamps exist in `transcript.json`, use them to narrow the quote span. Otherwise use the segment timestamp. If timestamps are absent, cite the segment ID and explicitly mark timing unavailable.

Never invent a timestamp, speaker, quote, DOI, URL, or verification result.

## Wiki output

Use normal Markdown plus Obsidian-compatible links:
- `[[Topic Name]]`
- `[[Entity Name]]`
- `[[Claim-<stable-id>]]`

Recommended destinations:

```text
wiki/
  summaries/
  concepts/
  entities/
  claims/
  index.md
```

Keep raw normalized transcript artifacts outside `wiki/`; they are source evidence, not compiled doctrine.

## External verification boundary

Web verification is a semantic/research action, not a deterministic parser step.

For each testable claim:
1. formulate a narrow search question from the proposition;
2. prefer official/primary documentation, first-party data, or primary research;
3. preserve disagreement rather than silently reconciling it;
4. record source title plus URL/DOI and access/publication date when material;
5. leave the claim `[UNVERIFIED]` when evidence is insufficient or live search is unavailable.

## Apex KB integration

Apex KB remains lifecycle authority. This skill may prepare source artifacts and semantic guidance, but it must not:
- choose an Apex KB lifecycle stage;
- write run state or manifest files owned by Apex KB;
- bypass generated semantic task packet allowlists;
- replace Apex KB import/validation with a parallel compiler.

When an Apex KB semantic task packet exists, obey that packet first and use this contract only inside its permitted source/output boundary.
