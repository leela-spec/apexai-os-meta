# DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW

## Purpose

This workflow turns deep research into a bounded patch specification without allowing source drift, fake diffs, or silent promotion.

## Flow

### Scope lock

Capture:

- repo
- branch
- commit anchor
- target surfaces
- non-goals
- blocked or missing files
- source-access method for each required surface
- citation or evidence format expected by the final output
- explicit assumptions that must not be re-researched

Stop if a claimed required file is inaccessible and its absence would make a later patch unsafe.

### Deep-research prompt preflight

Before launching a deep-research prompt, separate the prompt into:

- locked assumptions
- required source surfaces
- optional context surfaces
- excluded research paths
- required final-output contract
- validation tests

For each required source surface, specify the access path the research agent should use first. If the source is local or repo-internal, require direct file reads or exact-path fetches before broad connector search. If the source may be missing or renamed, require the agent to report the mismatch once and continue from the nearest authoritative available surface instead of repeatedly searching.

For each excluded research path, define a detour budget. A detour budget is the maximum effort allowed before the agent must convert ambiguity into a validation test or open question. Locked tool-capability assumptions, generic product documentation, generic architecture theory, and citation mechanics should normally have a detour budget of zero unless the prompt explicitly asks to verify them.

The prompt must tell the research agent how to handle citation or evidence requirements. If exact citations are required, say which source families need citation. If citations are not load-bearing, say that internal file-path references or evidence notes are enough. Do not let citation mechanics outrank the main task.

The prompt must include a failure-routing line:

- if a required source cannot be reached, report the missing source once, state the consequence, and continue only within the safe remaining scope
- if a locked assumption appears false, do not re-litigate it; record a validation test or open question
- if connector or tool behavior is unclear, do not spend output budget researching generic tool behavior; convert it into an implementation validation test
- if the output contract is too large, complete the specified Phase 1 subset rather than broadening research

### Source alignment

Produce:

- strongest starting KB files
- role map
- current managed surfaces already expressing the architecture
- missing managed infrastructure

Use source files as evidence, not automatic authority.

### KB infrastructure design

Define:

- existing files to patch
- new files to create
- final agent seed set
- KB lanes and starting sources
- overlap validation model
- promotion model
- boundary rule keeping staging surfaces non-runtime

### Patch specification

Before diffs, record for each planned patch or new file:

- exact path
- purpose
- source basis
- validation partner
- risk note
- promotion status

### Unified diffs and new file contents

Only write exact unified diffs for files whose current content has actually been read.
Anything else is blocked, not guessed.

Unified diffs are review artifacts first and transport artifacts only when they are generated and checked in the actual repo checkout. Do not use chat-authored unified diffs as the default for Markdown governance rewrites.

Use this artifact hierarchy:

1. full final body for new files and rewrite-class Markdown files
2. one-file live-edit instruction for bounded Markdown patches
3. Git-generated diff from the actual checkout for review
4. pre-authored unified diff only when generated and checked in the actual checkout
5. blocked patch when exact context, line endings, or byte safety are not guaranteed

Before any existing-file patch manufacturing, record line-ending state with `git ls-files --eol <target>`. CRLF files should normally use live-edit instructions and real `git diff` review, not chat-carried patch bytes.

Malformed fenced diffs must become live-edit recovery cases or blocked patches; never force-apply or repair patch bytes outside the live target and real Git diff review loop.

### Read-only research handoff

When research runs in a read-only chat or connector, it must state that it cannot apply, commit, or push changes.
It produces a patch package for the local executor.
The local executor validates context, applies changes, runs checks, commits, and pushes.

Read-only research must not spend task budget proving the executor's write capability when the prompt marks that capability as a safe assumption. It may list the assumption and add a validation test for the executor.

### Iteration checkpoints

For repo-governance patchspec work, preserve these checkpoints in the output:

1. exact context audit
2. overlap and authority validation
3. patch package or new-file package
4. executor instructions and validation checklist

Do not collapse the checkpoints into an unlabelled final answer when the task depends on auditability.

### Generated-file completeness validation

For every generated or restored file, validate more than path existence.
Check for required headings, schema anchors, closing fenced-code blocks, and acceptance markers.
Nested fenced-code blocks are a known extraction risk and must be verified by content readback.

## Required outputs

- patch plan
- new-file plan
- source-access and detour-control summary for deep-research prompts
- unified diffs only when safe in the actual checkout, otherwise live-edit instructions or blocked-patch notes
- full new-file contents
- cross-reference manifest
- validation checklist
- blocked-patches register
- executor boundary statement when the research author is read-only
- content-completeness checks for new or restored files

## Safety rules

- do not treat staging files as final runtime surfaces
- do not convert candidates into canon silently
- do not invent config behavior
- do not write fake diffs
- do not skip second-agent verification for durable change
- do not let connector exploration, citation mechanics, or generic tool documentation displace the locked source basis
- do not re-research excluded topics; convert unavoidable uncertainty into validation tests or open questions

## Linked files

- `managed/knowledge/KB_STARTING_SOURCE_MAP.md`
- `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`
- `managed/rules/PROMOTION_PROTOCOL.md`
