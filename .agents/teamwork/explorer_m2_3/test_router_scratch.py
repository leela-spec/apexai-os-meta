import sys
from pathlib import Path

sys.path.insert(0, r"c:\GitDev\apexai-os-meta\apex-meta\scripts")
sys.path.insert(0, r"c:\GitDev\apexai-os-meta\apex-meta\informatics\tests")

import okf_validator
import test_informatics_e2e as t

sample_router = """---
type: Router
id: RTR-GEN-v0.2
title: Apex General Router
description: JIT router and conditional dispatch surface for Apex OS.
---

# Apex General Informatics Router

## 1. P0 Critical Invariants

- [P0 | I98/E98/R05] Target Dominance: Realize intended outcomes. Tests are evidence, not proxies.
- [P0 | I96/E95/R05] JIT Retrieval: Zero eager @path imports. Read files via tools on trigger match.
- [P0 | I95/E95/R10] Surgical Mutation: Never rewrite whole files. Modify files via exact-match patch blocks.
- [P0 | I95/E98/R05] Substance Over Ceremony: Technical correctness overrides metrics. Ceilings yield to truth.

## 2. P1 Core JIT Dispatch Gates

<informatics when="writing_or_documentation" ref="writing-profile.md" deepen_when="ste_limits">
  [P1 | I92/E95/R10] Information Mapping and STE limits for governed docs.
</informatics>

<informatics when="file_creation_or_structure" ref="file-architecture.md" deepen_when="five_planes">
  [P1 | I90/E92/R12] Five-Plane IA, flat frontmatter, and current-truth separation.
</informatics>

<informatics when="task_execution_adapter" ref="execution-modes.md" deepen_when="task_adapters">
  [P1 | I92/E94/R10] Decision Matrices, Bake-Offs, Patches, Handovers, and MMM.
</informatics>

<informatics when="operational_anti_drift" ref="anti-drift-rules.md" deepen_when="two_strike_pivots">
  [P1 | I94/E95/R08] 8 Anti-Drift Laws, Two-Strike pivot rule, and task minimalism.
</informatics>

<informatics when="governance_and_schemas" ref="governance-schemas.md" deepen_when="patch_schemas">
  [P1 | I88/E92/R10] Frontmatter schemas, AST patch intent, and directive limits.
</informatics>

## 3. P2 Standard Practices

- [P2 | I85/E90/R10] Sizing Orientations: Ceilings (~100L/~400T) guide efficiency. Target governs.
- [P2 | I80/E85/R15] Autonomous Decisions: Resolve routine reversible choices autonomously from evidence.

## 4. P3 Advisory Polish

- [P3 | I65/E80/R08] Heading Scannability: Constrain markdown headings to <= 3 levels.
"""

def test_template():
    lines = len(sample_router.splitlines())
    tokens = t.estimate_tokens(sample_router)
    chars = len(sample_router)
    eager = t.check_router_eager_imports(sample_router)
    tags = t.extract_all_significance_tags(sample_router)
    valid_order, order_err = t.validate_tags_descending_order(tags)
    is_top, token_pos = t.check_top_loaded_primacy(sample_router, token_ceiling=500)
    parsed_xml = t.parse_router_tags(sample_router)
    fm, body, fm_err = okf_validator.parse_frontmatter(sample_router)
    advisories = okf_validator.check_writing_style("test.md", body)

    print(f"Lines: {lines} (target ~100, test limit <= 120)")
    print(f"Chars: {chars}")
    print(f"Tokens: {tokens} (target ~400, test limit <= 500)")
    print(f"Eager imports detected: {eager}")
    print(f"Significance tags count: {len(tags)}")
    print(f"Descending order valid: {valid_order} (err: {order_err})")
    print(f"Top-loaded primacy valid: {is_top} (first P0 token pos: {token_pos})")
    print(f"Parsed XML tags count: {len(parsed_xml)}")
    print(f"Frontmatter parse error: {fm_err}")
    print(f"Frontmatter parsed type: {fm.get('type') if fm else None}")
    print(f"Advisory warnings count: {len(advisories)}")

if __name__ == "__main__":
    test_template()


sample_index = """---
okf_version: "0.2"
title: Apex Informatics Standard & Consolidated General Router
description: Canonical entrypoint, OKF v0.2 bundle index, and conditional JIT routing layer for Apex OS AI agents.
---

# Apex Informatics Standard & Consolidated General Router

Canonical entrypoint and conditional JIT routing index for the Apex OS knowledge and instruction architecture.

## 1. P0 Critical Invariants

- [P0 | I98/E98/R05] Target Dominance: Realize and validate substantive intended outcomes. Tests and schemas are evidence, not substitutes.
- [P0 | I96/E95/R05] Strict JIT Retrieval: Zero eager @path imports. Read referenced specifications via tools only when triggers match.
- [P0 | I95/E95/R10] Surgical Mutation: Never rewrite whole files. Modify existing files strictly via exact-match patch blocks.
- [P0 | I95/E98/R05] Substance Over Ceremony: Technical correctness overrides mechanical metrics. Ceilings yield to truth.

## 2. P1 Core JIT Dispatch Gates

<informatics when="writing_or_documentation" ref="writing-profile.md" deepen_when="ste_word_limits">
  [P1 | I92/E95/R10] Apply Information Mapping and STE word limits to governed docs.
</informatics>

<informatics when="file_creation_or_structure" ref="file-architecture.md" deepen_when="five_plane_isolation">
  [P1 | I90/E92/R12] Apply Five-Plane IA, flat OKF frontmatter, and current-truth separation.
</informatics>

<informatics when="task_execution_adapter" ref="execution-modes.md" deepen_when="decision_matrices_or_patches">
  [P1 | I92/E94/R10] Apply Decision Matrices, Bake-Offs, Patches, Handovers, or MMM.
</informatics>

<informatics when="operational_anti_drift" ref="anti-drift-rules.md" deepen_when="two_strike_pivots">
  [P1 | I94/E95/R08] Apply 8 Anti-Drift Laws, Two-Strike pivot rule, and task minimalism.
</informatics>

<informatics when="governance_and_schemas" ref="governance-schemas.md" deepen_when="patch_intent_json">
  [P1 | I88/E92/R10] Validate frontmatter schemas, AST patch intent, and directive limits.
</informatics>

## 3. Governed Modular Specification Suite

- [Writing Profile & Prose Ergonomics](writing-profile.md) — Information Mapping, STE sentence limits, visual block targets, and durable IDs.
- [File Architecture & Bundle Structure](file-architecture.md) — Five-Plane Architecture, OKF v0.2 frontmatter schemas, and current-truth separation.
- [Execution Modes & Task Adapters](execution-modes.md) — Task adapters for Q&A Decision Matrices, Comparison Bake-Offs, Exact-Match Patching, Handover, and MMM.
- [Anti-Drift Rules & Operational Lore](anti-drift-rules.md) — 8 Anti-Drift Laws, Two-Strike pivot rule, Sunk-Cost Prohibition, and Task Minimalism.
- [Governance Schemas & Directive Ceilings](governance-schemas.md) — Frontmatter schemas, AST patch intent specifications, and model directive ceilings.
- [General Informatics Router](general-informatics-router.md) — Compact standalone agent-facing embeddable JIT router template.

## 4. Supporting Governance & History

- [Apex Informatics Standard](standard.md) — Master 14-section governance standard combining OKF v0.2, Information Mapping, and STE prose.
- [Migration & Onboarding Policy](migration.md) — Rules governing repository knowledge conformance and migration.
- [Change Log](log.md) — Chronological version history and audit log.
- [Agent Setup Sub-Bundle](Agent_Setup/index.md) — Sub-bundle boundary index for agent setup and legacy artifacts.

## 5. P2 Standard Operational Practices

- [P2 | I85/E90/R10] Operational Sizing: Sizing targets (~100L / ~400T) orient router efficiency. Target outcome governs.
- [P2 | I80/E85/R15] Autonomous Decisions: Resolve routine reversible choices autonomously from evidence.

## 6. P3 Advisory Polish

- [P3 | I65/E80/R08] Heading Scannability: Constrain markdown heading hierarchy to <= 3 levels.
"""

def test_index_template():
    print("\\n=== Testing Index Template ===")
    lines = len(sample_index.splitlines())
    tokens = t.estimate_tokens(sample_index)
    chars = len(sample_index)
    eager = t.check_router_eager_imports(sample_index)
    tags = t.extract_all_significance_tags(sample_index)
    valid_order, order_err = t.validate_tags_descending_order(tags)
    is_top, token_pos = t.check_top_loaded_primacy(sample_index, token_ceiling=500)
    parsed_xml = t.parse_router_tags(sample_index)
    fm, body, fm_err = okf_validator.parse_frontmatter(sample_index)
    links = okf_validator.extract_links(sample_index)

    print(f"Index Lines: {lines}")
    print(f"Index Chars: {chars}")
    print(f"Index Tokens: {tokens}")
    print(f"Index Eager imports: {eager}")
    print(f"Index Significance tags: {len(tags)}")
    print(f"Index Descending order valid: {valid_order} (err: {order_err})")
    print(f"Index Top-loaded primacy valid: {is_top} (first P0 token pos: {token_pos})")
    print(f"Index Parsed XML tags: {len(parsed_xml)}")
    print(f"Index Frontmatter error: {fm_err}")
    print(f"Index OKF version: {fm.get('okf_version') if fm else None}")
    print(f"Index Links extracted: {len(links)}")
    for l in links:
        print(f"  Link: {l}")

test_index_template()
