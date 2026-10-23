---
type: Reference
id: RESULTS-02-vector-retrieval
title: Vector retrieval versus static dispatch - Findings
description: Determines whether instruction retrieval can replace manually routed always-on invariants.
status: current
tags: [research-result, retrieval, rp-02]
---

# RP-02 - Could vector retrieval replace static IF-dispatch?

**Verdict (confidence: high that vector retrieval cannot guarantee invariants, medium that skills/structured scoping are the better current complement):** **Retain an unconditional invariant layer; do not replace it with embedding-based instruction retrieval.** Vector retrieval has a strong case for discovering a large, changing body of noncritical guidance whose correct section is not known from filenames. But a nearest-neighbor search can miss a mandatory rule, and its output is evidence/data, not a reliable enforcement boundary. The most compelling *real* contemporary alternative is **harness-native, progressively disclosed instruction skills and path-scoped rules**, not pure instruction-RAG. Current static dispatch is **not materially behind** the state of coding-agent practice, but relying on model-interpreted custom `when=` instead of available native scoping is behind the stronger 2026 tool-specific options.

## Strongest case for retrieval - advocate's position

Hand-authored IF/THEN routers scale poorly as the repository accumulates dozens of specialized rules. Authors must anticipate which user phrasings correspond to each branch; unanticipated or cross-cutting tasks slip through. A semantic index allows agents to retrieve related instructions even when the task vocabulary does not match the module heading. Dense plus keyword/hybrid search can surface multiple complementary parts without manually growing a long routing table; vendors provide index/query APIs, so this is not a hypothetical retrieval technology. For **advisory instructions** (not hard invariants), dynamic retrieval becomes attractive when breadth and rapid updates overwhelm a small router. This is an **architectural inference** from mature retrieval infrastructure, not proof that an instruction-RAG production agent has superior rule compliance.

## Evidence

| Claim | Source link | Evidence type | Supports / undermines |
|---|---|---|---|
| OpenAI Agent Skills put names/descriptions in the model's discovery context and load instructions/references when selected; skill text is user-priority, not a machine-enforced invariant. | [OpenAI, Skills docs](https://developers.openai.com/api/docs/guides/tools-skills); [Skills usage](https://developers.openai.com/cookbook/examples/skills_in_api) | Vendor documentation of a shipped system | Supports hybrid: always-available routing metadata + deferred procedure |
| Cursor Project Rules have **Always**, glob **Auto Attached**, description **Agent Requested**, and **Manual** modes; AGENTS.md is a simple alternative. | [Cursor official rules](https://docs.cursor.com/context/rules-for-ai) | Vendor documentation of shipped agent feature | Supports native static + agent-selective hybrid; not evidence for vector policy retrieval |
| Claude Code can scope `.claude/rules/*.md` to file paths with `paths:` YAML and import additional files from CLAUDE.md. | [Anthropic project memory](https://code.claude.com/docs/en/memory) | Vendor documentation | Supports deterministic path-scoped detail vs free-text `when=` |
| Knowledge-base retrieval for agents exists: Bedrock agents have knowledge-base selection instructions, including querying company HR **policies** on relevant questions. This is retrieving **policy knowledge to answer**, NOT enforcement of unconditional behavioral rules. | [AWS Bedrock agents + knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-add.html) | Vendor documentation; production feature | Supports retrieval in policy-question answering; cannot validate instruction-RAG enforcement |
| AWS separately associates **Guardrails** with agents for input/output protections, rather than entrusting all protective policy to knowledge retrieval. | [AWS Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html) | Vendor documentation | Undermines unconditional-invariant-via-vector design |
| On BEIR's 18 heterogeneous retrieval datasets, BM25 is a robust baseline and dense retrieval can underperform for out-of-domain transfer; this does not isolate short imperative policy rules. | [Thakur et al., BEIR](https://arxiv.org/abs/2104.08663) | Controlled retrieval benchmark | Undermines assumption that embedding similarity is sufficient for all terse rules; no direct short-rule rate |
| Azure AI Search documents parallel vector+keyword hybrid retrieval and warns updates concurrent with search can temporarily return incomplete results. | [Azure vector index consistency](https://learn.microsoft.com/en-us/azure/search/vector-store); [Hybrid search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) | Vendor production documentation | Supports practical hybrid retrieval; exposes freshness/race and expense considerations |
| Context files can induce agents to explore more and spend >20% extra without generally improving coding success. | [Gloaguen et al., arXiv:2602.11988](https://arxiv.org/abs/2602.11988) | Controlled coding-agent study | Warns against flooding context with retrieved rule fragments |

## Comparison

| Dimension | Static IF file dispatch | Vector retrieval for instruction fragments | Hybrid invariant + skills/path rules (+ retrieval if warranted) |
|---|---|---|---|
| Guaranteed **presence** of universal rule | **Yes**, if always injected by supported harness | **No**: top-k recall can be <100% | **Yes** for the unconditional kernel |
| Guaranteed **obedience** | **No**: LLM may disobey | **No** | **No**, unless action is checked or blocked by programmatic policy/hook |
| Token consumption | Kernel + condition metadata + triggered file | Kernel/query description + top-k chunks; can be lower **or higher** depending on k/chunking | Small kernel + metadata; detail on actual trigger |
| Authoring and updates | Manual condition table; repo-local files | Chunking, embedding/index freshness, ranking and provenance | Module/skill descriptions and scoped rules; simpler owner chain |
| Editing/freshness | File edit is available to next read (subject to session caches) | Re-indexing delay; stale/contradictory chunks possible; read/edit races | Source file with native load behavior; explicit package/version updates |
| Failure | Wrong predicate, missed read, speculative opening | Missed critical rule, duplicate contradictory rules, stale embeddings, retrieval injection | Skill nonactivation or wrong glob, plus bounded kernel; context sync remains |
| Complexity | Low; largely portable | New index, embeddings, index lifecycle, telemetry, latency | Moderate; tool-specific configuration and version compatibility |

## Direct answer - unconditional rules

**There is no unconditional guarantee from semantic top-k retrieval.** The known pattern is **always-present policy/core prompt + retrieved knowledge or procedures**, commonly described as *hybrid static-and-retrieved context*, *progressive disclosure*, or *policy enforcement outside the model* when protections are mandatory. Distinguish: (1) **injection guarantee** by tool/harness, (2) **application/compliance** by the model, and (3) **hard enforcement** by authorized API/tool restrictions, permission checks or hooks. None is provided by cosine similarity alone. AWS's separate knowledge-base and guardrail components are a concrete instance of this separation.

## What the asker appears not to know

1. **Agent Skills are a shipping instruction-discovery mechanism**: small metadata first, `SKILL.md` only if the agent chooses it. They are stronger production evidence for conditional document loading than inventing an instruction vector database. [OpenAI](https://developers.openai.com/api/docs/guides/tools-skills).
2. **Cursor Auto Attached** and **Claude `paths:` rules** attach by file scope through the harness rather than expecting an XML `when` attribute to be honored. [Cursor](https://docs.cursor.com/context/rules-for-ai); [Claude](https://code.claude.com/docs/en/memory).
3. A **file-read prevention requirement** can be handled by a dedicated routing/tool policy *only if needed and supported*. A bare source link or vector result is never an access-control boundary.
4. **Current retrieval systems support hybrid keyword/vector matching** and still have index freshness/race concerns. For short similar imperatives, neither dense-only nor lexical-only is guaranteed. [Azure](https://learn.microsoft.com/en-us/azure/search/vector-search-overview).

## Strongest case against the verdict

Static gates rely on language-model task classification, which `RP-01` could show to be unreliable. If a large library of instructions covers many overlapping domains, manually maintaining hundreds of conditions could produce more misses, contradictions, and token overhead than indexing. A production instruction-retrieval system with (a) strong measured recall on held-out paraphrased task requests, (b) mandatory always-on invariants, (c) version pinning and stale-index safeguards, (d) end-to-end agent success gains, and (e) lower cost could change the recommendation. For *noncritical* guidance, such a system might already outperform a weak handwritten router. That is a conditional flip, not a dismissal of retrieval.

## What I could not find

- A well-documented 2026 production *coding agent* in which **mandatory behavioral instructions** are chosen solely by semantic vector retrieval and shown to have reliable invariant compliance.
- A controlled rule-retrieval benchmark limited to **short imperative agent instruction snippets**, with false-negative and contradiction rates comparable to the proposed contract.
- An end-to-end independent benchmark showing vectorized *instruction* retrieval (not ordinary document-RAG) beats native skills or path-scoped agent rules on task accuracy and total cost.
- Direct evidence on how this repo's 22 clauses perform under task-conditioned indexing.

## Consequence for the contract

- **Whole-architecture falsification condition:** **NOT MET.** There is insufficient evidence that vector retrieval dominates static IF dispatch here. Keep a guaranteed always-on core.
- **`DEC-16`, `DEC-M2`:** still need the local gating test. The viable alternative to evaluate first is **native scoped rules/skills**, not a new vector database.
- **Recommendation flips** toward instruction retrieval if the instruction corpus becomes large/volatile, lookup misses exceed specified thresholds, and independent agent traces demonstrate both better success and acceptable recall/cost. Never outsource hard invariants to unverified retrieval.
