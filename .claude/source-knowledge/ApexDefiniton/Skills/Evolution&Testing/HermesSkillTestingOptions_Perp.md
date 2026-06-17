**Important caveat upfront:** The Gemini answer you received contains fabricated sources — "MOSS (moss-evo)", "FairyClaw", and the cited arXiv papers (arXiv:2605.22794, arXiv:2605.19604) appear to be hallucinated. Do not trust those. Here is what I actually found with live web searches:

---

## What Hermes Curator Actually Is

The **built-in Curator** (by NousResearch) is _not_ what you're thinking of — it's a native Hermes feature that prunes and consolidates agent-generated skills automatically. It runs weekly, tracks usage analytics, and merges or removes redundant skills via `hermes curator run`. This is the "housekeeping" layer, not the external test-and-rewrite tool you remember.[[x](https://x.com/NousResearch/status/2049719457808093231)]

## The Community Tool You're Likely Remembering

The closest real match to your description is **`hermes-curator-evolver`** by [pingchesu on GitHub](https://github.com/pingchesu/hermes-curator-evolver). It is tagged `hermes-plugin` and described as:[[github](https://github.com/topics/hermes-plugin)]

> _"Evidence-driven skill evolution for Hermes Agent — reports, dry-run proposals, candidate search, and guarded apply"_

Key features that match your memory:[[github](https://github.com/topics/hermes-plugin)]

- **Scans your skill database** against failure evidence
    
- **Dry-run proposals** — shows you what rewrites it would make before touching anything
    
- **Candidate search** — finds alternative skill formulations
    
- **Guarded apply** — only commits the rewrite after validation passes
    
- Built as a proper Hermes plugin (tagged `hermes-plugin`, `skill-evolution`, `skill-governance`)
    

It's small (19 stars), community-built, and very recent (May 28, 2026) — consistent with something you'd stumble across and think _"oh wow, this is exactly what I needed"_.[[github](https://github.com/topics/hermes-plugin)]

## Other Real Candidates Worth Checking

|Tool|What it does|Verification|
|---|---|---|

|Tool|What it does|Verification|
|---|---|---|
|[hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)|Official NousResearch GEPA-based evolutionary optimizer for skills + prompts|2.6k stars, official [[github](https://github.com/NousResearch/hermes-agent-self-evolution)]|
|[autocontext](https://github.com/greyhaven-ai/autocontext)|Recursive self-improving harness, supports Hermes CLI, auto-generates and refines context|945 stars [[get-hermes](https://get-hermes.ai/community/)]|
|[awesome-hermes-skills](https://github.com/ZeroPointRepo/awesome-hermes-skills)|Curated install-ready skill repo with community tools cross-compatible with Claude Code|Active 2026 [[github](https://github.com/ZeroPointRepo/awesome-hermes-skills)]|

## What Gemini Got Wrong

The Gemini response fabricated both MOSS/moss-evo and FairyClaw entirely — no such repositories exist under those names in the Hermes ecosystem, and the arXiv citations appear invented. The "hermes-dojo by Yonkoo11" is also unverifiable. Real community tools live at [get-hermes.ai/community](https://get-hermes.ai/community/) and the `hermes-plugin` GitHub topic.[[get-hermes](https://get-hermes.ai/community/)]

**Most likely candidate:** Start with [`hermes-curator-evolver`](https://github.com/pingchesu/hermes-curator-evolver) — it matches your description most precisely: external plugin, screens skill database, proposes rewrites, guarded apply. Does that ring a bell visually, or do you remember it being older/bigger/differently named?