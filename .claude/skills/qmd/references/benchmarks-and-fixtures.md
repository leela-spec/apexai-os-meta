---
type: Reference
id: REF-QMD-BENCHMARKS-AND-FIXTURES
title: QMD Benchmark Specifications, Quality Metrics & Test Fixtures
description: Ground-truth benchmark specifications, quality scoring methodology, and test fixtures for running qmd bench against the apex-informatics-final corpus.
status: current
tags: [qmd, benchmark, quality, precision, recall, fixtures]
---

# QMD Benchmark Specifications, Quality Metrics & Test Fixtures

> **Governance Authority:** Decision `DEC-QMD-04` and `DEC-QMD-05` in [`07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md).  
> **Complements:** [`SKILL.md`](../SKILL.md), [`search-speed-protocol.md`](search-speed-protocol.md).

---

## 1. Quality Scoring Metrics (`qmd bench`)

QMD's native benchmark harness evaluates search performance across four retrieval pipelines (`bm25`, `vector`, `hybrid`, `full` with reranking):

- **Precision@k (P@k):** Proportion of top-$k$ returned documents that are relevant.
- **Recall@k (R@k):** Proportion of expected target documents retrieved in the top-$k$.
- **Mean Reciprocal Rank (MRR):** Inverse rank of the first relevant document ($1/\text{rank}$).
- **F1 Score:** Harmonic mean of Precision and Recall ($2 \cdot \frac{P \cdot R}{P + R}$).
- **Latency (ms):** Mean search duration per query.

---

## 2. Canonical Apex Informatics Fixture Specification

The following benchmark fixture uses 100% verified disk paths and tests the live `apex-informatics-final` collection:

```json
{
  "description": "Apex Informatics Final - Quality & Retrieval Benchmark",
  "version": 1,
  "collection": "apex-informatics-final",
  "queries": [
    {
      "id": "q1-specbench-failure",
      "query": "SpecBench self-authored acceptance criteria proxy failure",
      "type": "exact",
      "description": "RP-05 empirical finding on proxy test failure rates",
      "expected_files": [
        "research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md"
      ],
      "expected_in_top_k": 3
    },
    {
      "id": "q2-fixedbench-bias",
      "query": "FixedBench over-building unwanted modifications on already-fixed states",
      "type": "semantic",
      "description": "RP-07 finding on RLHF modification bias and no-op legitimacy",
      "expected_files": [
        "research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md"
      ],
      "expected_in_top_k": 3
    },
    {
      "id": "q3-two-strike-rule",
      "query": "two-strike rule subsystem failure stop repairing bounded iterations",
      "type": "topical",
      "description": "Rule 10 and AD-02 stop repairing invariant",
      "expected_files": [
        "research/06-layered-rule-kb/rule-10-stop-repairing.md"
      ],
      "expected_in_top_k": 3
    },
    {
      "id": "q4-cool-blue-register",
      "query": "Cool Blue register warranted uncertainty calibration Insights Discovery",
      "type": "alias",
      "description": "RP-04 communication tone and uncertainty calibration",
      "expected_files": [
        "research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md"
      ],
      "expected_in_top_k": 3
    }
  ]
}
```

### Running the Benchmark:
```bash
qmd bench .agents/skills/qmd/references/apex-benchmark-fixture.json
```

---

## 3. Empirical Baseline Results (`apex-informatics-final`)

Measured on Windows 11 host (Intel Core Ultra 7 258V / Arc 140V Vulkan / 32 GB RAM):

| Retrieval Pipeline | Mean Latency | Precision@k | Recall@1 | Recall@3 | Recall@5 | MRR | F1 Score |
|---|---|---|---|---|---|---|---|
| **`bm25` (FTS5)** | **9 ms** | 0.250 | 0.250 | 0.250 | 0.250 | 0.250 | 0.250 |
| **`vector` (Gemma-300M)** | **2,097 ms** (2.1s) | **0.750** | **0.500** | **0.750** | **1.000** | **0.633** | **0.750** |
| **`hybrid` (BM25 + Vector)** | **3,375 ms** (3.4s) | **0.750** | 0.250 | **0.750** | **1.000** | **0.521** | **0.750** |
| **`full` (+ 1.7B LLM expansion)** | **24,322 ms** (24.3s) | 0.250 | 0.250 | 0.250 | 0.750 | 0.406 | 0.250 |

> **Key Architectural Takeaways:**
> 1. **Vector & Hybrid achieve 100% Recall@5 (`R@5 = 1.000`)** in **2.1s to 3.4s**, proving extreme retrieval efficacy.
> 2. **BM25 executes in 9 milliseconds**, ideal for exact keyword anchors.
> 3. **Unconstrained LLM query expansion (`full`) is 7x to 11x slower (24.3s)** and degrades Precision@k from 0.750 down to 0.250.
> 4. This confirms **Decision `DEC-QMD-01`**: agents must run BM25/Vector hybrid searches with caller-authored `intent:` and avoid unconstrained query expansion.
