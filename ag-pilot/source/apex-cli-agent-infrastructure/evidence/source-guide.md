---
type: Reference
id: APEX-INFRA-SOURCE-GUIDE-20261112
title: Evidence Sources and Access Boundaries
description: Source authority, frozen retrieval provenance, primary external evidence and reproducible access limits.
status: draft
tags: [sources, provenance, evidence, limitations]
---

# Source guide

**The source registers preserve evidence; they do not decide authority by themselves.** Current operator instructions and live Apex owners govern intended behavior. Accepted choices apply within their recorded scope. Configurations, implementations and traces show what exists or was observed. Historical candidates remain evidence. Current external sources establish capabilities and inform proposals without overruling accepted Apex meaning.

## Repository evidence

[repository-sources.json](repository-sources.json) lists 83 authenticated source snapshots at `6c93ad31e42a72de74119218b9365bdd9d6ee386`, with root-relative path, Git blob SHA-1, SHA-256, byte length, line count and snapshot path. Full files were retrieved to preserve exact bytes; semantic review was targeted to the relevant owner sections, claims, implementation boundaries and source conflicts. Full retrieval is not a claim that every line was independently reviewed.

All seven named starting sources are included. Expansion covered the current XML’s owners; live carriers/settings; current skills and agent doctrine; handoff/authority schemas; accepted scoped decisions; distribution tools; actual scorer/fixture code; and design-changing retained research. The [top-50 comparison](reading-guide-comparison.json) records 49 selected entries, all with unchanged file hashes compared with the older guide revision. The current source revision and verified line anchors are nevertheless recorded explicitly.

The frozen tree is under `evidence/repository/`, preserving original root-relative structure. For example, the XML is [the exact source snapshot](repository/apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml). Relative links inside snapshots retain their original source context and may be stale; they were not silently repaired. The registry records resolved owners and the integration map supplies concrete corrections.

| Evidence group | Why it matters | Starting owner or register |
|---|---|---|
| Current contract and modules | Actual rule identities, scope and authored metrics | XML plus FA/WP/AD/GS and execution-mode owners in `registry/rules.json` |
| Accepted and historical decisions | Preserve original rationale and distinguish supersession from deployment | `registry/history.json`; scoped Hermes, Claude KB and local-engine sources |
| Runtime configuration and carriers | What is present in the repository, with no installed-state inference | Root carriers, `.claude/settings.json`, existing skill paths and carrier tools |
| Orchestration and authority | Preserve separate named systems, backbone and confirmed mutation | Current manifest, architecture, handoff/authority/verdict schemas |
| Retained agent evaluations | Reuse real failures without losing method limits | Read-trace pilot, Stage-1 corrected report/code, Round-2 report/scorer/hook fixture |
| New diagnostic execution | Establish specific reproducible scorer and schema counterexamples | `evaluation/scorer-probe-results.json`; `examples/native/*results.json` |

## Primary external evidence

[external-sources.json](external-sources.json) consolidates 62 current primary sources: 47 platform documentation/schema sources and 15 original empirical studies or open/primary methodology references. The platform subset is maintained in [compatibility sources](../compatibility/sources.json), with 49 claim records in [compatibility claims](../compatibility/claims.json). The empirical subset is appraised in [empirical findings](empirical-findings.md), including publication version, task/model scope, denominators, confounds, contrary results and transfer limits.

The capability research distinguishes Codex local CLI/App/IDE, execution/SDK/hosted surfaces; Claude interactive/normal print/bare/SDK/hosted; Antigravity CLI/App/IDE/SDK; and retained Gemini profiles. Source URLs are direct public primary URLs. Vendor documentation is a moving source; where a behavior is version-critical, the claim records the release boundary or pinned schema. Codex schemas are frozen at `rust-v0.167.2`, with upstream license and notice. Their exact blobs are checked independently from runtime semantic fixtures.

Current primary evidence includes both supportive and contrary findings. Skills can help with curated task procedures but regress on some tasks and lose benefit under realistic noisy selection. Context files can increase cost or have null/negative effects. Learned context compression does not validate an ordinary checkpoint prompt. Two independent configuration checkers can share the same semantic error. These limits affect the design and test requirements, not merely the bibliography.

## Explicit access and execution limits

Six authenticated exact-path fetches returned 404 at the pinned Apex revision: `.codex/config.toml`, `.codex/hooks.json`, `.agents/hooks.json`, `apex-meta/informatics/standard.md`, `apex-meta/informatics/final/specs/index.md`, and `apex-meta/informatics/final/specs/migration.md`. This establishes only that those exact repository locators were unavailable through the authenticated contents fetch at that revision. It does not establish absence from a workstation, another branch or another path. The actual standard/index/migration owners were retrieved through current navigation.

The original `C:/tmp/apex-eval` trace directory, other-repository runtime roots, global/account settings and workstation installations were not available to this run. Historical reports retain `source_reported_execution` status. There is no claimed reproduction of their pass rates. Local deterministic checks use frozen source, synthetic fixtures and native wire/schema examples only.

The research container’s Codex version fingerprint is recorded in [environment observation](../compatibility/environment-observation.json). No CLI host was launched for an adherence, loader or hook test. All 14 native probes and 22 new behavioral cases are explicitly unexecuted. The native canaries are complete offline examples, not installed production guardrails.

## Reproducible evidence checks

From the extracted package root, run `python validation/validate_package.py`. The validator checks frozen bytes against Git blob/SHA-256 records, registry source excerpts, identities, recorded raw tags, cross-artifact links and proposed schemas. The recorded invocation and its limits are in [the validation report](../07-validation-report.md). Offline native examples and scorer diagnostics have separate reproduction commands and report their evidence class.

**Failure guard:** do not replace a missing source with plausible content, infer installation from repository presence, or convert a recorded result into a newly measured effect. Reopen the actual current owner or exact platform/version before changing a material conclusion.
