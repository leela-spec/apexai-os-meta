## Executive decision

After reconciling the three new reports with the earlier scan and checking the disputed repositories directly, I would **not** adopt the winner from either report blindly.

The reports disagree in a consequential way:

- The AntiG report selects the repository-local **TTK** pipeline, but that violates the original strategic objective: _find an existing external workflow rather than continue the bespoke transcript pipeline_.
    
- The CC report selects **`AgriciDaniel/claude-obsidian`** and claims deterministic transcript chunking.
    
- The GEM report also selects `claude-obsidian`, but correctly notes that **it does not actually have an explicit single-large-transcript chunk/checkpoint protocol**.
    
- Direct inspection confirms the GEM version: `claude-obsidian` has excellent SHA-based provenance, ledgers, transactions and recovery, but its current `wiki-ingest` says to read each source completely within a budget and mark it partial if that cannot be done. It does not prescribe or implement a progressive chunk loop for one huge transcript.
    
- **`Ar9av/obsidian-wiki` does explicitly say large files must be read using bounded `offset/limit` chunks**, while also performing cumulative concept/entity extraction, source hashing, existing-page reconciliation, cross-linking and repeated ingestion.
    

So under the **original hard filters**, my ranking is:

> **#1 `Ar9av/obsidian-wiki` — selected for bake-off.**  
> **#2 `giodra96/project-wiki` — technically excellent long-document challenger, but far too immature and project-engineering-specific to adopt directly.**  
> **Conditional #1 `AgriciDaniel/claude-obsidian` — if we relax the requirement that bounded long-document handling must already exist inside the package.**

---

# 1. Master capability matrix — primary / near-primary systems

Legend:

- **✅** strong / directly implemented
    
- **◐** partial, agent-driven or weaker
    
- **❌** absent / hard weakness
    
- **?** insufficiently verified
    
- **EXCL** strategically excluded rather than technically bad
    

Abbreviations are shortened only to keep the matrix readable.

|Attribute / capability|**Ar9av OW**|**Claude-Obsidian**|**Project-Wiki**|**Jack LLM Wiki**|**Cole KB**|**Compozy KB**|**Basic Memory**|**arronKler Wiki**|**AWS KA Skill**|**Louiswang KB**|**Business Ontology**|**TTK local**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Category**|LLM Wiki ingestion|AI second-brain / wiki|Project KB|LLM Wiki|YouTube→OKF|KB CLI + skill|MCP memory graph|Managed LLM wiki|LLM Wiki research skill|Claude KB|Business ontology|Transcript compiler|
|**External reusable solution**|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|**❌ custom local**|
|**General transcript fit**|**✅**|✅|◐|✅|◐ YouTube-centric|◐|◐|✅|◐|◐|❌ business-specific|**✅**|
|**Accept existing `.txt` transcript**|✅|✅|**✅**|✅|◐ raw transcript path possible|✅|◐|✅|✅|◐|✅|**✅**|
|**Host AI does semantics**|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|
|**Separate paid model API required**|**No**|**No**|**No**|**No**|**No**|No for local file workflow|**No**|**No**|**No**|**No**|**No**|**No**|
|**Claude Code**|✅|**✅ native**|✅|✅|✅|✅|✅|✅/Agent skill|◐|✅|✅|✅|
|**Codex CLI**|**✅**|✅|✅|✅|?/portable|✅|MCP route|◐|?|?|✅|✅|
|**Antigravity**|**✅**|◐ / portable|◐ IDE-neutral|?|?|?|?|◐|?|?|?|✅ skill layout possible|
|**Native ChatGPT Skill proven**|❌|❌|❌|❌|❌|❌|❌ skill; MCP is different|❌|❌|❌|❌|❌|
|**Persistent local canonical files**|**✅**|**✅**|**✅**|**✅**|**✅**|**✅**|✅ Markdown|**✅**|**✅**|✅|**✅**|**✅**|
|**Git-friendly**|**✅**|**✅**|**✅**|**✅**|**✅**|**✅**|✅|**✅**|**✅**|✅|**✅**|**✅**|
|**Human-readable Markdown**|**✅**|**✅**|**✅**|**✅**|**✅**|**✅**|**✅**|**✅**|**✅**|✅|**✅**|**✅**|
|**Machine-readable metadata**|✅ YAML|✅ YAML/ledgers|**✅ YAML/registry**|✅ YAML|**✅ OKF YAML**|✅ YAML/JSON|✅|**✅**|✅|✅|**✅ structured events**|**✅ JSON + MD**|
|**Explicit huge-single-file bounded reading**|**✅ offset/limit**|**❌**|**✅ deterministic chunks**|◐ manual/split guidance|**❌ full transcript**|**❌ compile full source**|❌|❌ verified mechanism|❌ verified mechanism|◐/manual|❌|**✅ deterministic windows**|
|**Deterministic chunk generation**|❌|❌|**✅ ~350-word files**|❌|❌|❌ semantic compile|❌|❌|❌|❌|❌|**✅**|
|**Progressive semantic reading**|**✅**|◐|**✅**|◐|❌ per-video full read|◐|❌|◐|◐|◐|◐|**✅**|
|**Mid-source checkpoint / resume**|◐ weak|❌ semantic chunk state|**✅ intake artifacts**|❌|❌ per transcript|❌|❌|?|?|?|❌|**✅ per-window**|
|**Source-level hash / dedupe**|**✅ SHA**|**✅ SHA**|**✅ SHA**|◐|✅ manifests|◐|◐|**✅**|◐|◐|✅ packet/hash|**✅ SHA**|
|**Immutable/raw evidence layer**|✅|**✅**|**✅**|**✅**|**✅**|✅|◐|**✅**|**✅**|◐|**✅ private raw**|**✅**|
|**Concept extraction**|**✅**|**✅**|◐ project categories|**✅**|**✅**|**✅**|◐|**✅**|**✅**|✅|✅ ontology|**✅**|
|**Entity extraction/pages**|**✅**|**✅**|◐|✅|**✅**|◐|◐|✅|✅|✅|✅|**✅**|
|**Dedicated source pages**|✅|✅|intake records|✅|**✅**|✅ raw|◐|**✅**|raw layer|◐|events/packets|✅|
|**Atomic claim layer**|◐|**✅ claim ledger**|◐|◐|◐ quotes|◐|❌|**✅ citations**|◐|◐|**✅ source events**|**✅**|
|**Search existing KB before writing**|**✅**|**✅**|**✅**|**✅ BM25/search**|canonicalization phase|**✅**|✅|**✅**|✅|✅|✅|◐ final reduce|
|**Merge/update existing concepts**|**✅**|**✅**|**✅**|**✅**|**✅**|✅|◐ agent judgment|**✅**|✅|✅|**✅ review model**|◐ weaker cross-source|
|**Duplicate concept prevention**|**✅ semantic + manifest**|**✅ semantic + ledgers**|✅ stable IDs|✅ search-first|**✅ canonicalization**|✅|◐|✅|◐|◐|✅|◐|
|**Contradictions preserved**|**✅**|**✅ strong**|**✅ alerts/review**|**✅**|◐|◐|◐|**✅**|✅|◐|**✅ strong**|**✅ support states**|
|**Cross-source compounding**|**✅**|**✅**|**✅**|**✅**|**✅ very strong**|**✅**|✅|**✅**|**✅**|✅|**✅**|◐|
|**Exact quote verification**|◐ not mandatory|◐ claim evidence|◐ source chunks|❌ deterministic|quote collection but not deterministic validator|❌|❌|◐|❌|❌|bounded excerpts|**✅ deterministic substring**|
|**Timestamp-level transcript anchors**|◐ if source supplies them|◐ supported as locator, not guaranteed|page/chunk/line|◐|**✅ timestamped quotes**|◐|❌|◐|◐|❌|segment IDs|**✅**|
|**Provenance strength**|**4/5**|**5/5**|**4.5/5**|3.5/5|**4.5/5**|3.5/5|2.5/5|**5/5**|4/5|3/5|**5/5**|**5/5**|
|**Deterministic structural lint**|✅|**✅**|✅ registries|✅ sync/lint|**✅ lint.py**|**✅**|✅ index sync|**✅**|✅|◐|✅ schemas|**✅**|
|**OKF native**|❌|❌|❌|❌|**✅**|◐ OKF mode available|❌|❌|❌|❌|❌|❌|
|**Vector DB required for correctness**|**No**|**No**|**No**|**No**|**No**|**No**|No; SQLite index|**No**|**No**|No|No|**No**|
|**SaaS custody required**|**No**|**No**|**No**|**No**|**No**|**No**|**No**|**No**|**No**|No|No|**No**|
|**Domain-neutral KB**|**✅**|**✅**|**❌ project engineering**|✅|◐ creator/channel|✅|✅|✅|research-oriented|✅|**❌ business ontology**|transcript-neutral|
|**Adoption / maturity**|**High: 3.3k★**|**Very high: 11.1k★**|**Very low: 5★**|Low–med: 99★|Low–med: ~105★|~100★|**High: 3.7k★**|lower|AWS sample but tiny adoption|87★, low activity|tiny|internal only|
|**Current activity**|**Aug 21**|Aug 1 push; repo active|Aug 19|Jul 10|Jul 28|Aug 20|**Aug 21**|current|Aug 17|Apr 7 push|Jul|current repo|
|**Operational complexity**|**Low–medium**|Medium|Medium|Low|Medium|Medium|Medium MCP stack|Medium|Medium|Medium|High|Medium/high|
|**Strict original hard-filter status**|**PASS**|**FAIL long-doc**|**PASS**|FAIL long-doc|FAIL long-doc|FAIL long-doc|FAIL transcript workflow|FAIL long-doc|FAIL long-doc|FAIL long-doc|FAIL long-doc/domain|**EXCL: custom**|

### What the source verification changes

`claude-obsidian`'s strengths are real: 11,104 stars, 1,283 forks, local Markdown ownership, SHA-256 source identity, claim/source ledgers and an inspect→apply→recover transaction lifecycle.

But the CC report's claim of a deterministic large-transcript chunking engine is not supported by its current `wiki-ingest` contract. The contract instead states: **read each source completely within the agreed budget; if that cannot be done, mark the result partial**.

Conversely, `Ar9av/obsidian-wiki` explicitly handles transcripts and conversational sources and states: **“Large files: read in chunks with offset/limit”**. It also hashes sources and only re-ingests changed material. Its current repository has about 3,257 stars, 324 forks, MIT licensing, and a push on August 21, 2026.

`giodra96/project-wiki` is the most explicit external implementation of deterministic large-document preprocessing: its script emits a manifest plus separate stable chunk files, defaults to ~350 words, and directs the agent to review them progressively. But it was only created on **August 19, 2026** and currently has **5 stars / 1 fork**.

---

# 2. Companion / baseline matrix

These should **not** be put into the same winner pool as a complete transcript→KB compiler.

|Attribute|**scaccogatto OKF**|**parkscloud OKF**|**Kepano Obsidian Skills**|**Fabric**|**Summarize**|**NotebookLM**|**Open Notebook / Khoj**|**Infranodus LLM Wiki**|**Transcript Critic**|**Nashsu Skill**|**Glebis Analyzer**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Role**|OKF author/validate/viz|OKF author/validator|Obsidian formatting/tools|extraction baseline|summary baseline|hosted KB|local RAG|SaaS/MCP KB|transcript analysis|client for app|transcript analyzer|
|**Complete transcript→persistent KB**|❌|❌|❌|❌|❌|◐|◐|◐|❌|◐|❌|
|**Long-doc handling**|N/A|N/A|N/A|❌ one-shot baseline|✅/chunk summary but summary-only|✅ hosted|✅ RAG chunks|?|◐|app-dependent|◐|
|**Cross-source canonicalization**|format only|format only|format only|❌|❌|proprietary|RAG rather than compiler|service-dependent|❌|app-dependent|❌|
|**Persistent local Markdown canonical state**|**✅**|**✅**|✅|output only|output only|❌ hosted|◐|❌/service|output only|app-dependent|output|
|**No separate model API**|**✅**|**✅**|✅|optional/local|✅ with authenticated coding CLI|UI subscription|local models possible|❌|?|local server|**❌ Cerebras per report**|
|**OKF v0.2 relevance**|**✅ strongest companion**|✅|❌|❌|❌|❌|❌|❌|❌|❌|❌|
|**Deterministic validation**|**✅ strong**|✅|syntax tooling|❌ KB|❌ KB|proprietary|DB checks|service|❌|?|❌|
|**Adoption evidence**|**325★ / 32 forks**|**1★ / 0 forks**|very high|very high|high|high SaaS|high/moderate|commercial|low|low|low|
|**Recommended role**|**YES — publication validator**|No reason to prefer over scaccogatto|optional authoring helper|**baseline**|**baseline**|external comparison|external comparison|reject|reject|reject|reject|

This is another place where one report needs correction: `parkscloud/okf-author` is implemented, but it currently has only **1 star and 0 forks**. `scaccogatto/okf-skills` has **325 stars / 32 forks**, is MIT-licensed, current, and explicitly targets Claude Code plus agent skills and OKF authoring/validation/visualization.

So for the **format/validator companion**, I would choose:

> **`scaccogatto/okf-skills` > `parkscloud/okf-author`**

not the reverse.

---

# 3. MCDA methodology

I would preserve your original rubric rather than inventing a different one now.

[  
\text{Score} =  
25%,PK +  
20%,LD +  
20%,Host +  
15%,Representation +  
10%,Maturity +  
10%,Ops  
]

Where each criterion is scored **1–5**:

|Criterion|Weight|What 5/5 means here|
|---|--:|---|
|**Persistent knowledge capability**|25%|repeated ingestion, concepts/entities, reconciliation, cross-source update|
|**Long-document resilience**|20%|bounded/progressive single-source reading, persistent state, no whole-source dependency|
|**Host / no-API compatibility**|20%|direct target-agent operation without separately billed semantic API|
|**Knowledge representation**|15%|human + agent readable, provenance, links, lifecycle/conflicts|
|**Maturity / reuse confidence**|10%|actual adoption, current maintenance, installation evidence|
|**Operational simplicity**|10%|simple install, repo-local files, few moving pieces, portable|

**Important:** MCDA comes **after hard filters**. A high weighted score does not rescue a candidate that violates a non-negotiable requirement.

---

# 4. MCDA — all serious candidates

The numeric score below is useful for comparing strengths even where the candidate fails a hard gate. `Eligibility` decides whether it can actually win.

|Rank by raw MCDA|Candidate|PK 25%|Long-doc 20%|Host 20%|Rep. 15%|Maturity 10%|Ops 10%|**Raw score**|Eligibility|
|--:|---|--:|--:|--:|--:|--:|--:|--:|---|
|**1**|**Ar9av/obsidian-wiki**|4.7|4.0|4.8|4.3|4.4|4.4|**89.2**|**PASS**|
|2|**TTK local benchmark**|4.2|**5.0**|4.6|4.5|2.8|3.6|**85.7**|**EXCLUDED — bespoke local solution**|
|3|**AgriciDaniel/claude-obsidian**|**4.9**|**2.2**|4.7|4.7|**5.0**|4.3|**84.8**|**FAIL — no implemented single-file bounded ingest**|
|4|**coleam00/cole-medin-kb**|4.8|**1.8**|4.4|**4.8**|3.2|4.2|**78.0**|FAIL long-doc|
|5|**arronKler/llm-wiki**|4.8|2.0|4.2|4.7|2.8|4.0|**76.5**|FAIL long-doc evidence|
|**6**|**giodra96/project-wiki**|3.5|**4.8**|4.4|3.6|**1.3**|4.0|**75.7**|**PASS, but experimental**|
|7|**jackwener/llm-wiki**|4.4|2.2|4.3|4.1|3.0|4.6|**75.5**|FAIL long-doc|
|8|**compozy/kb**|4.4|1.8|4.4|4.4|3.6|4.1|**75.4**|FAIL long-doc compiler|
|9|**basic-memory**|3.8|1.8|4.6|3.9|4.5|3.8|**72.9**|FAIL complete-ingest / long-doc|
|10|**business-ontology**|4.3|2.0|4.2|4.4|2.4|3.0|**70.3**|FAIL generic-fit / long-doc|
|11|**AWS knowledge-acquisition**|4.3|2.0|3.8|4.0|2.3|3.5|**68.3**|FAIL long-doc evidence|
|12|**louiswang KB**|4.0|2.0|3.2|3.7|2.2|3.8|**63.9**|FAIL long-doc / maturity|

### Why `claude-obsidian` still scores so high

It is probably the **better general knowledge-management product** than Ar9av in several dimensions. It has over 11k stars and sophisticated transaction and provenance semantics.

But the specific problem is not:

> “What is the best Obsidian AI knowledge system?”

It is:

> “What existing workflow can progressively compile a three-hour transcript without requiring whole-source semantic understanding?”

On that criterion, the current `claude-obsidian` skill is weaker.

That 20% long-document dimension is also a **hard gate**, so maturity cannot compensate for its absence.

---

# 5. Strict hard-gate result

Once the original hard filters are applied, the huge candidate field collapses to two defensible external primary candidates:

|Candidate|Existing external workflow|No model API|Persistent KB|Explicit bounded huge-document mechanism|Local inspectable state|Mature enough?|Result|
|---|--:|--:|--:|--:|--:|--:|---|
|**Ar9av/obsidian-wiki**|✅|✅|✅|**✅**|✅|**✅ 3.3k★**|**PASS / WINNER**|
|**giodra96/project-wiki**|✅|✅|✅|**✅ stronger chunker**|✅|**❌ only 5★ / 2 days old**|PASS technically, high adoption risk|
|Claude-Obsidian|✅|✅|**✅**|**❌**|**✅ excellent**|**✅ 11.1k★**|FAIL H3|
|Cole|✅|✅|**✅**|**❌ reads full transcript**|✅|◐|FAIL H3|
|Jack LLM Wiki|✅|✅|✅|◐ tells you to split|✅|◐|FAIL H3|
|Compozy|✅|✅ for file input|✅|**❌ compilation full-source**|✅|◐|FAIL H3|
|Basic Memory|✅|✅|✅|❌|✅|**✅**|FAIL H3/H9|
|TTK|**❌ external reuse objective**|✅|✅|**✅ best**|**✅**|internal|strategically excluded|

Cole's pipeline explicitly tells the agent to **read the full transcript** before extracting its per-video JSON; its batching is across videos, not within a single video.

Jack's skill similarly tells the workflow to split large chat logs/collections but provides no deterministic single-transcript slicing/checkpoint mechanism itself.

---

# 6. Decision analysis: what should we pick?

## #1 — `Ar9av/obsidian-wiki`

### Why it wins

It is the best current intersection of all four things you actually need:

```text
proven-enough ecosystem package
        ×
explicit bounded large-file reads
        ×
real cumulative knowledge integration
        ×
no external semantic API
```

It does not merely turn chunks into isolated summaries. Its ingest contract is explicitly:

```text
source
  ↓
hash / changed-source detection
  ↓
bounded reads for large input
  ↓
extract concepts / entities / claims / relationships
  ↓
inspect existing index + existing pages
  ↓
merge existing OR create new
  ↓
record provenance
  ↓
cross-link
  ↓
manifest / index / log
  ↓
next source
```

That is much closer to the required **knowledge compiler** than V4 Fabric.

### Main weakness

Its bounded reads are **agent-procedural**, not a TTK-style deterministic chunk ledger.

So:

```text
bounded reading        YES
persistent KB          YES
cross-source merging   YES

but

chunk N completed      not strongly persisted
chunk N hash           no
resume specifically N+1 no guaranteed primitive
```

That is why I score Long-doc at **4.0 rather than 5.0**.

---

# 7. #2 — `giodra96/project-wiki`

This one is technically very interesting.

Its implemented intake architecture is almost exactly what we wanted mechanically:

```text
large document
    ↓
ingest_document.py
    ↓
source SHA
    ↓
chunks.json
    ↓
CH-001.md
CH-002.md
CH-003.md
...
    ↓
agent progressively reviews chunks
    ↓
compare with canonical KB
    ↓
integrate / conflict / review
```

It defaults to 350-word chunks and explicitly says **not to load all chunks at once**.

### Why it does not win

Two reasons dominate:

**1. It is extremely immature.**

Created August 19; 5 stars as of today.

That is not battle-tested enough to replace your pipeline without a strong bake-off.

**2. Its ontology is the wrong ontology.**

The canonical KB is organized around:

```text
requirements/
changes/
technical/
implementation/
traceability/
ADRs
alerts
open questions
```

Its own skill describes itself as durable **project memory for coding agents**.

That is excellent for Leela/APEX engineering specifications.

It is much less natural for:

```text
scientific interview
→ fear conditioning
→ amygdala
→ prediction error
→ autonomic response
→ researcher/person entity
```

Adapting those categories materially starts becoming our architecture again.

---

# 8. Where `claude-obsidian` fits

I would **not discard it**.

It is the most important challenger.

## If one rule is relaxed...

If you decide:

> “A tiny deterministic transcript splitter in front of the skill is acceptable even though it is not part of the winning skill”

then the decision changes significantly.

You would get:

```text
V4 transcript
    ↓
tiny deterministic splitter
    ↓
claude-obsidian wiki-ingest
    ↓
high-maturity KB
```

In that world, `claude-obsidian` could plausibly beat Ar9av because:

- 11.1k versus 3.3k stars;
    
- stronger transactional writes;
    
- explicit source and claim ledgers;
    
- SHA-256 preconditions;
    
- operation recovery;
    
- better conflict/provenance discipline.
    

But that is **a different decision criterion** from the one initially specified.

### Therefore

|Policy|Winner|
|---|---|
|**Strict: candidate itself must handle giant source progressively**|**Ar9av/obsidian-wiki**|
|**Allow tiny deterministic pre-splitter**|**Bake off Ar9av vs claude-obsidian**|
|**Maximum deterministic transcript rigor regardless of reuse objective**|TTK|
|**Best huge engineering requirements-document intake**|project-wiki|
|**Best YouTube-channel→OKF compiler for modest individual videos**|Cole|
|**Best persistent generic MCP memory**|basic-memory|
|**Best OKF companion**|scaccogatto/okf-skills|

---

# 9. Why I reject the AntiG TTK recommendation as the strategic answer

TTK is not bad. In fact, its transcript machinery is stronger than every external candidate on deterministic custody:

- deterministic bounded map windows;
    
- core/context halos;
    
- packet hashes;
    
- verbatim quote checks;
    
- resumable map results;
    
- compact Reduce packet;
    
- Macro/Meso/Micro + concept/entity/claim compilation.
    

The AntiG report is therefore directionally correct about **technical robustness**.

But it answers:

> “Which architecture most robustly processes huge transcripts?”

rather than the stated question:

> “Which **existing external maintained workflow can we install instead of continuing our custom transcript pipeline?**”

Selecting TTK would effectively reverse the reuse-first decision and return us to maintaining the custom semantic orchestration ourselves.

So TTK should be kept as:

> **benchmark / fallback / source of acceptance criteria**

not the default implementation.

---

# 10. Knowledge representation decision

I would also **separate ingestion from publication**.

### Semantic working format

Let the winner use its native wiki representation first.

For Ar9av:

```text
Obsidian Markdown
+ YAML
+ manifest
+ index
+ wikilinks
```

Do not add another format conversion before knowing whether the semantic product is good.

### Portable publication format

After knowledge has stabilized:

> **OKF v0.2 remains the best candidate.**

### Validator/tool

> **Use `scaccogatto/okf-skills`, not `parkscloud/okf-author`, as the leading companion.**

Current adoption evidence materially favors it: 325 stars / 32 forks versus 1 / 0.

So the clean architecture is:

```text
TRANSCRIPT INGESTION
Ar9av wiki-ingest
        ↓
native cumulative wiki

OPTIONAL PUBLICATION BOUNDARY
        ↓
OKF v0.2
        ↓
scaccogatto validation
```

Not:

```text
every chunk
→ convert OKF
→ validate
→ reconvert
→ canonicalize
```

That would create unnecessary pipeline machinery.

---

# 11. Final MCDA recommendation

### Decision hierarchy

**1. Bake off `Ar9av/obsidian-wiki` first.**

It is the only current candidate I found that simultaneously has:

- explicit large-file bounded reads;
    
- generic transcript support;
    
- persistent cross-source KB integration;
    
- host-AI semantics;
    
- no separate semantic API;
    
- substantial real adoption;
    
- active maintenance.
    

**2. Include `claude-obsidian` as the challenger only if a deterministic pre-split is allowed.**

Its KB architecture is potentially superior, but the transcript boundary is currently missing.

**3. Keep `project-wiki` as a design reference rather than production pick.**

Its `chunks.json + CH-*.md` intake is exactly the kind of deterministic bounded preprocessing worth remembering, but 5 stars and a project/ADR ontology are insufficient for immediate adoption.

**4. Keep TTK frozen as the gold-standard deterministic control.**

Do not extend it unless the external bake-off proves the missing controls materially necessary.

---

## Recommended bake-off

I would therefore run **three lanes, not ten**:

|Lane|Why|
|---|---|
|**A — Ar9av/obsidian-wiki unchanged**|strict external winner|
|**B — claude-obsidian + minimal deterministic pre-split**|maturity challenger|
|**C — current TTK**|high-rigor reference control|

All three should ingest the **same existing** long V4 transcript and then a second transcript into the same KB.

The decision should be based overwhelmingly on the artifact:

> **Can a fresh human or AI recover the important reusable knowledge, including later corrections and qualifications, without rereading the transcript—and trace important claims back when necessary?**

If **A** achieves that, stop building infrastructure and adopt it.

If **B** materially beats A, the small splitter is justified.

If only **C** reliably preserves the important information, then the evidence finally justifies retaining the bespoke deterministic transcript layer.