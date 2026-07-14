## 1. Output-format insertion

Place this **immediately before `REQUIRED OUTPUT`**. It governs how the entire result is delivered.

OUTPUT DELIVERY CONTRACT

Return the complete authoritative result as one native ChatGPT Deep Research report.

- Use ordinary report headings, concise prose, tables, lists, and diagrams where they improve clarity.
- Attach citations or source links directly to supported claims.
- Do not wrap the complete report in a Markdown code fence.
- Do not make a ZIP archive, generated attachment, repository file, or external document the only location of substantive findings.
- Do not write to GitHub, create branches, commits, pull requests, issues, patches, or repository mutations.
- Do not execute Apex KB or apply implementation changes.
- The complete research findings, decisions, implementation guidance, uncertainties, and acceptance criteria must remain readable in the native report.
- The operator may export the completed native report through ChatGPT as Markdown, Word, or PDF.
- Use code fences only for short schemas, commands, pseudocode, or exact interface examples.
- Prefer compact tables for repeated fields, but do not compress evidence or rationale until it becomes ambiguous.
- Avoid repeating the same conclusion in the executive summary, module report, decision register, and implementation plan. Cross-reference earlier sections instead.
- If report capacity becomes constrained, preserve content in this priority order:
    1. evidence truth and limitations;
    2. final architectural decisions;
    3. lifecycle and module contracts;
    4. file-and-script implementation guidance;
    5. validation and acceptance criteria;
    6. risks, alternatives, and unresolved evidence;
    7. explanatory background.
- Never omit a material unresolved fact merely to make the report shorter.

Deep Research natively returns a structured, cited report in a full-screen report view, and completed reports can be downloaded as Markdown, Word, or PDF. Connected-app use during Deep Research is read-only.

## 2. Capacity-use addendum

Place this **after the complete `REQUIRED OUTPUT` section and before `VALIDATION BEFORE RETURNING`**.

Your original wording is risky because “final files” could be interpreted as generating repository-ready replacements, which the prompt otherwise prohibits. Use this instead:

ADDITIONAL CAPACITY USE

First complete every mandatory report section and validation requirement. Do not shorten, weaken, or skip the primary report in order to produce supplemental material.

If meaningful output capacity remains after the mandatory report is complete, use it to produce additional implementation-design artifacts in descending priority order.

Create only artifacts that materially reduce later implementation rediscovery. Examples include:

1. a consolidated final file-tree and change matrix;
2. detailed design records for the highest-priority files;
3. detailed design records for the highest-priority scripts;
4. interface and schema specifications;
5. migration and compatibility matrices;
6. fixture and acceptance-test specifications;
7. unresolved-evidence probes for decisions that could not be verified.

For each supplemental artifact:

- label it clearly as `Supplemental Implementation Design`;
- keep it inside the native Deep Research report;
- state its priority and downstream consumer;
- include evidence, assumptions, dependencies, validation, and risks;
- do not present a hypothesis as a finalized implementation contract;
- do not produce finished executable code, repository patches, complete replacement files, Git operations, or ZIP archives.

Continue through the prioritized supplemental artifacts only while each new artifact adds substantive implementation value. Do not fill remaining capacity with repetition, verbose restatement, speculative features, or low-priority documentation.

## Why this is more resilient

Your proposed sentence asks the model to “max out” output. That can encourage:

- repetition;
- incomplete trailing sections;
- low-value filler;
- full repository files that conflict with the research-only scope;
- prioritizing optional files over the required report.

The revised version instead says:

> **Finish the mandatory report first, then spend remaining capacity on ranked implementation-design artifacts.**

That is the safest practical way to encourage a long, useful report. OpenAI documents that a good Deep Research prompt should specify the desired outcome and constraints, but it does not document a phrase, format, Pro toggle, ZIP, or attachment strategy that increases the model’s maximum output-token allowance.


# instructions for changing prompt

You have the **right prompt**. The drift was in my wording, not in your file.

Your prompt does not contain a heading called `REQUIRED OUTPUT`. It uses:

> `## 15. Required final report structure`

That is the correct equivalent.

## Current status

|Item|Status|
|---|---|
|Final report structure|Present in Section 15|
|Additional capacity addendum|Present, correctly placed after Section 15|
|Validation before returning|Present as Section 16|
|No code, patches, Git operations or ZIPs|Present|
|Native Deep Research output-delivery instruction|**Still missing**|

Your `ADDITIONAL CAPACITY USE` section is already in the correct location:

```
## 15. Required final report structure
...
## ADDITIONAL CAPACITY USE
...
## 16. Validation before returning
```

## Where the missing insertion goes

Insert the following **immediately before**:

```
## 15. Required final report structure
```

Therefore, the sequence becomes:

```
## 14. Durable source-map and index design

...

## Output delivery contract

...

## 15. Required final report structure
```

### Exact insertion

```
## Output delivery contract

Return the complete authoritative result as one native ChatGPT Deep Research report.

- Present all substantive research findings, decisions, implementation guidance, uncertainties, and acceptance criteria directly in the native report.
- Use ordinary report headings, concise prose, tables, lists, and diagrams where they improve clarity.
- Attach citations or source links directly to supported claims.
- Do not wrap the complete report in a Markdown code fence.
- Use code fences only for short schemas, commands, pseudocode, formulas, or exact interface examples.
- Do not create a ZIP archive, generated attachment, repository file, or external document as the primary or only location of substantive findings.
- Do not write to GitHub or create branches, commits, pull requests, issues, patches, or other repository mutations.
- Do not execute Apex KB or apply implementation changes.
- Keep the complete authoritative result readable and reviewable in the native Deep Research report.
- Structure the report so it remains suitable for native export as Markdown, Word, or PDF.
- Prefer compact tables for repeated fields, but do not compress evidence, uncertainty, or rationale until it becomes ambiguous.
- Avoid repeating the same conclusion across the executive sections, module reports, decision records, and implementation plan. Cross-reference earlier sections instead.
- If report capacity becomes constrained, preserve material in this priority order:
  1. evidence truth, access limitations, and uncertainty;
  2. final architectural decisions;
  3. lifecycle and module contracts;
  4. file-and-script implementation guidance;
  5. validation and acceptance criteria;
  6. risks, alternatives, and unresolved evidence;
  7. explanatory background.
- Never omit a material unresolved fact merely to shorten the report.
```

This matches the native Deep Research workflow: it produces a structured report with citations, a table of contents and source history, and supports downloading the completed report as Markdown, Word, or PDF. Deep Research uses connected apps only for read actions, while GitHub writes belong in Codex.

## One small correction to the existing capacity addendum

Change:

```
keep it inside the native Deep Research report;
```

to:

```
keep every supplemental artifact as a clearly labeled section or appendix inside the same native Deep Research report;
```

This prevents “artifact” from being interpreted as a downloadable file.

**Verdict:** no structural prompt drift. The prior placement reference was inaccurate; use **immediately before Section 15**.