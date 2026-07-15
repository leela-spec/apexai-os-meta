You are right about the core issue: the scanner creates useful data, but that data is then copied into an oversized topic-review process.

I wrote the thorough plain-language analysis here:

[Leela deterministic process explained](C:\\tmp\\leela-deterministic-process-explained.md)

## Direct answers

1. Are the 197 sources all files selected for this run?

**Yes.** They are the 197 files this corpus-map run was told to consider.

But only 146 are readable text files. The others are binary/non-text files that can be inventoried and hashed but not semantically read by this text pipeline.

2. Does `source-postings.json` contain all headings?

**Yes.** For every readable Markdown file, it contains all recognized headings from H1 through H6, including their original line numbers.

Example:

```
{
  "path": "LeelaAppDevelopment/01_Features/101 - Chunks & Chunk Database.md",
  "headings": [
    {"level": 2, "line": 2, "text": "0) Purpose & Scope"},
    {"level": 2, "line": 18, "text": "1) Core Concepts & Relationships"},
    {"level": 3, "line": 20, "text": "1.1 Conceptual Model"}
  ]
}
```

“Line 18” means: that heading appears on line 18 of the original source.

3. Is `heading-map.json` duplicating `source-postings.json`?

**Yes, substantially.**

Both contain exactly the same 4,310 extracted headings.

The heading map only has 146 records because those are the readable files. It adds:

- the first H1 as the title;
- parser warnings, such as an unclosed code block;
- a rough source-type guess.

Those additions have some value, but they do not justify storing all 4,310 headings again. This is genuine redundancy.

## What “197 candidates for every topic” means

A candidate is simply:

> “A source file that the semantic reviewer should consider for this topic.”

Unfortunately, the script currently does this:

```
Skill Tree:
    consider all 197 files

Path:
    consider all 197 files

Rhythm:
    consider all 197 files

...repeat for all 10 topics
```

So it creates 1,970 source-topic cards.

Worse, it includes files even when they have no topic keyword signal:

- Skill Tree: 62 of 197 have no Skill Tree signal.
- Path: 67 have no Path signal.
- User Stories: 77 have no User Stories signal.
- Across all topics: 586 of 1,970 cards have zero signal.

That overlap is real and confirmed.

## What `body` and `content_pointer` mean

`body` means the script searched the entire file text for a topic term.

It does not copy the body into the map. It merely records something like:

```
"body": ["epic", "content"]
```

That means those words appeared somewhere. It does not say where, how often, or in what sentence.

`content_pointer` is:

```
{
  "path": "the source file",
  "headings": ["all headings from that file"]
}
```

It is supposed to help someone navigate to the source. But those headings already exist elsewhere.

The topic map repeats all 4,310 headings ten times: 43,100 copied heading records.

## What the semantic ledger actually accomplished

For Skill Tree, the semantic run reviewed all 197 candidates and decided:

|Result|Files|
|---|---|
|Actually useful|5|
|Irrelevant|72|
|Unreadable|52|
|Exact duplicate|43|
|Historical/superseded|25|

So yes, the ledger performs a kind of rating—but it uses categories rather than scores.

A genuinely useful ledger result says:

```
{
  "source_path": "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md",
  "disposition": "material_source",
  "evidence_pointer": "Relevant feature data-model and contract headings.",
  "analysis_ref": ".../01-features-102-epics-database-skill-tree.md"
}
```

The actual semantic value then appears in the final dossier:

```
SKT-C001:
Skill Tree is a projection and selection surface over Epic content.

Evidence:
102 - Epics (Database + Skill Tree).md, lines 202–240.
```

So the ledger is the review receipt. The dossier is the useful knowledge product.

## The complete flow

```
197 source files
        ↓
Extract hashes, headings and links
        ↓
Copy all 197 files into each of 10 topic lists
        ↓
Semantic reviewer evaluates all 197 again
        ↓
Ledger records useful / irrelevant / duplicate / old / unreadable
        ↓
Only 5 Skill Tree sources survive as useful
        ↓
Final dossier creates 4 evidence-backed Skill Tree claims
```

## My honest assessment

The process is not completely worthless:

- The initial per-file scan is valuable.
- The semantic classification finds the few useful sources.
- The final dossier contains real evidence-backed conclusions.

But the middle is badly shaped:

- headings are stored repeatedly;
- “candidate” means every file, not a plausibly relevant file;
- exhaustive audit evidence is being used as a semantic work queue;
- the browser reviews enormous amounts of irrelevant, duplicate, and unreadable material;
- the ledger contains substantial boilerplate.

That is very plausibly why the semantic workflow struggles.

One clarification: H1–H5 were hypothesis labels, unrelated to Markdown headings H1–H6.

The direct hypothesis answers are:

- Corrupt artifacts: **No.**
- Combined map poorly shaped for browser work: **Yes.**
- Confirmed duplication: **Yes.**
- Raw Git timeout definitely caused failure: **Cannot be proven without connector logs.**
- Genuine semantic content gaps: **Yes.**

The smallest sensible correction is to retain the exhaustive map for audit custody, while giving semantic work a separate, genuinely topic-filtered work pack. No repository files were modified.