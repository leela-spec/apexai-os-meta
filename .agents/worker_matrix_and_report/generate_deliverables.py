import os
import sys
import json
import csv

REPO_INV_PATH = r"c:\GitDev\apexai-os-meta\.agents\explorer_repo_inv\evaluated_inventory.json"
LEGACY_INV_PATH = r"c:\GitDev\apexai-os-meta\.agents\explorer_legacy_inv\legacy_inventory.json"
TARGET_DIR = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit"
CSV_PATH = os.path.join(TARGET_DIR, "agent_knowledge_matrix.csv")
JSON_PATH = os.path.join(TARGET_DIR, "agent_knowledge_matrix.json")

CANONICAL_DOMAINS = {
    "Alfred", "Meta Ops", "Meta Strategy", "Meta Detective",
    "Knowledge Bank", "Informatics Design", "Prompts & Workflows",
    "AI Routing / Special Ops"
}

CANONICAL_STATUSES = {
    "Canonical / Active", "Distilled / Migrated",
    "Empty Scaffold / Stub", "Reference-Only / Historical"
}

def generate_lineage_notes(item, is_legacy):
    rel = item.get("rel_path", "").replace("\\", "/")
    fn = item.get("file_name", "")
    fn_lower = fn.lower()
    rel_lower = rel.lower()
    domain = item.get("domain", "")
    status = item.get("status", "")
    scope = item.get("scope", "")

    # Priority 1: The 7 Critical Omitted Doctrine Assets and Core System Anchors
    if "2do_context_file_authority_reference" in fn_lower:
        return "Era 1 legacy asset omitted during 2026-07-11 migration. Defines empirical model directive ceilings (GPT-4o: 50, Claude: 50/80, Gemini/o3: 100), 500-token primacy rule (CD-01), modal verb ban (CD-04), 4-way file taxonomy, and Minimal Viable File Test (MVT)."

    if "decisionmakingprocessreseearch" in fn_lower:
        if not is_legacy:
            return "Legacy Meta Strategy appendix copied loose to .claude/skills/ as an unreferenced orphan file; codifies 5 formal cognitive decision frameworks (First Principles, Cynefin, WRAP, AoA, OODA Loop). Requires formal integration into meta-strategy contract."
        else:
            return "Era 1 legacy Meta Strategy research appendix detailing 5 cognitive decision architectures; omitted during 2026-07-11 migration and later copied loose to .claude/skills/ without active contract wiring."

    if "failure_and_anti_drift_ledger" in fn_lower:
        return "Era 1 legacy Meta Detective empirical failure archive cataloging 202 granular real-world AI failures, observed errors, tested safeguards, and validation rules; classified as reference-only and omitted from modern core."

    if "appendix_kb_preimage_checked_scaffold_mutation_process" in fn_lower or "preimage_checked" in fn_lower:
        return "Era 1 Prompts & Workflows appendix distinguishing deterministic Git storage from probabilistic AI generation; foundational source for AGENTS.md and GEMINI.md patch safety rules; prematurely marked obsolete in DOCTRINE-MANIFEST."

    if "appendix_kb_patch_transport_protocols" in fn_lower or "patch_transport" in fn_lower:
        return "Era 1 Prompts & Workflows patch protocol establishing the 5-way transport chooser matrix (full-body, search/replace, diff, live-edit, manual review); prematurely dismissed as obsolete."

    if "agent_patch_contract" in fn_lower:
        return "Era 1 Prompts & Workflows patch contract enforcing hard blocker prevention gates, strict patch stream hygiene, and prohibition of _v2 workaround sprawl."

    if "qa_hygiene_protocol" in fn_lower:
        return "Era 1 system governance protocol defining 8 formal QA finding classes and 4-tier P0-P3 severity model with concrete remediation gates; partially distilled into Meta Ops templates."

    if "escalation_exception_block" in fn_lower:
        return "Era 1 governance rule defining 4-tier E0-E3 escalation levels, authority ambiguity triggers, and truth-leakage stop conditions; foundational for handoff exception handling."

    if "doctrine-manifest" in fn_lower:
        return "Era 2 consolidation manifest (2026-07-11) recording audit of 227 legacy OpenClaw files, 39 sha256-verified moves, 5 translation rules, and empty scaffold skip decisions."

    if "integration-apex-plan-sync-session" in fn_lower:
        return "Modern Era 3 integration contract governing Meta Ops routing into the Plan-Sync-Session backbone (apex-plan, apex-sync, apex-session)."

    # Priority 2: Empty Scaffolds & Stubs
    if status == "Empty Scaffold / Stub":
        if is_legacy:
            return f"Era 1 OpenClaw empty scaffold stub ({fn}) containing EMPTY_STATE marker; forensically confirmed unpopulated in legacy archive and correctly omitted by DOCTRINE-MANIFEST."
        else:
            return f"Modern placeholder stub ({fn}) with zero substantive doctrine; reserved for future operational scaffolding."

    # Priority 3: Active Agent Contracts (.claude/agents/)
    if not is_legacy and ".claude/agents/" in rel_lower:
        return f"Modern Era 3 active agent contract governing {domain} execution boundaries, tools, and handoffs in the live APEX OS operating spine."

    # Priority 4: Modern Orchestration Agents (apex-meta/orchestration/agents/)
    if not is_legacy and "apex-meta/orchestration/agents/" in rel_lower:
        if fn_lower == "core.md":
            return f"Era 2 distilled operational core for {domain} created 2026-07-11; condenses 80/20 domain rules, practices, and templates into compact working reference to minimize token load."
        elif fn_lower == "essence.md":
            return f"Era 2 sha256-verified verbatim copy of legacy OpenClaw v2 {domain} boundary specification, preserved during 2026-07-11 consolidation."
        elif fn_lower.startswith("role-seed"):
            return f"Era 2 role seed initialization contract for {domain} moved verbatim from legacy OpenClaw on 2026-07-11."
        elif fn_lower in ["best_practices.md", "mistakes.md", "templates.md"] or fn_lower.startswith("appendix_"):
            return f"Era 2 sha256-verified verbatim copy of legacy OpenClaw v2 {domain} doctrine; preserved as on-demand reference behind CORE.md."
        elif fn_lower.startswith("legacy-hygiene-clean"):
            return f"Era 2 import from legacy hygiene_clean domain; provides P0-P3 severity cribs, checklists, and structural QA rules absorbed into {domain}."

    # Priority 5: System Core & Workflows (apex-meta/orchestration/)
    if not is_legacy and "apex-meta/orchestration/" in rel_lower:
        if fn_lower in ["00-start-here.md", "architecture.md"]:
            return "Modern Era 3 canonical system architecture and operating invariants governing single WSL2 engine and file-backed state."
        elif "/workflows/" in rel_lower:
            return f"Modern Era 3 operational workflow procedure defining run-loop execution, dual-blind review, and session lifecycle for {domain}."
        elif "/schemas/" in rel_lower:
            return f"Modern Era 3 canonical machine-readable schema defining universal handoff, authority-state, and review-verdict contracts ({fn})."
        elif "/user-stories/" in rel_lower:
            return f"Modern Era 3 requirement specifications and validation scenarios for APEX OS {domain} capabilities."
        elif "/architecture-improvements/" in rel_lower:
            return f"Modern Era 3 architectural migration dossier and ADR closeout plans (e.g. ADR-002 single-engine WSL2 consolidation) in {domain}."
        elif "/new_final_v4/" in rel_lower:
            return f"Modern Era 3 workflow and specification draft in finalization track for {domain}."

    # Priority 6: Skills
    if not is_legacy and (".claude/skills/" in rel_lower or "apex-meta/skills/" in rel_lower):
        if fn_lower == "skill.md":
            return f"Modern Era 3 skill definition package for {domain} domain operations in live APEX OS."
        elif any(s in rel_lower for s in ["apex-plan", "apex-sync", "apex-session", "weekly-orchestrator", "source-authority"]):
            return f"Modern Era 3 core operational skill implementation powering deterministic agent tooling and review loops ({fn})."
        elif "legacy-v2-doctrine" in rel_lower:
            return f"Era 2 legacy OpenClaw doctrine preserved in {domain} skill references for operational context."
        else:
            return f"Modern Era 3 active skill asset supporting {domain} domain execution in live repository ({fn})."

    # Priority 7: Legacy Managed Agent KB (managed/agent_kb/)
    if is_legacy and "managed\\agent_kb" in rel_lower:
        if fn_lower in ["essence.md", "role-seed.md"]:
            return f"Era 1 OpenClaw {domain} boundary specification; migrated verbatim to orchestration/agents/ on 2026-07-11."
        elif "/meta_detective" in rel_lower:
            return "Era 1 substantive OpenClaw adversarial review doctrine; migrated verbatim to orchestration on 2026-07-11 and distilled into CORE.md."
        elif any(d in rel_lower for d in ["special_ops__knowledge_bank", "special_ops__informatics_design", "special_ops__prompts_workflows", "special_ops__ai_handling_routing"]):
            return f"Era 1 OpenClaw {domain} domain doctrine; core assets migrated on 2026-07-11, specialized appendices retained in archive as reference."
        else:
            return f"Era 1 OpenClaw {domain} KB document; historical foundation for modern orchestration doctrine."

    # Priority 8: Legacy Managed Rules / Processes / Companion
    if is_legacy and any(p in rel_lower for p in ["managed\\rules", "managed\\processes", "managed\\rituals", "managed\\knowledge"]):
        return f"Era 1 OpenClaw {domain} governance rule/process; superseded by modern file-backed orchestration and single-engine architecture."

    # Priority 9: Legacy Source Indexes
    if is_legacy and "agent_kb_source_indexes" in rel_lower:
        return f"Era 1 OpenClaw source intake index ({fn}) used during initial KB compilation; historical reference."

    # Priority 10: Legacy Modernization & Factory Artifacts
    if is_legacy and any(p in rel_lower for p in ["newfinals", "kb4agents", "apex_vision", "ai api cost", "agent_kb_factory"]):
        return f"Era 1 intermediate modernization revision or KB factory artifact ({fn}) from legacy staging."

    # Priority 11: Legacy Uncurated Operational Corpora
    if is_legacy:
        return f"Era 1 historical staging corpus and research notes in legacy preparation archive ({fn}); retained for provenance."

    # Fallback
    return f"Active {domain} document in live repository tree supporting APEX OS operations ({fn})."

def main():
    os.makedirs(TARGET_DIR, exist_ok=True)

    with open(REPO_INV_PATH, "r", encoding="utf-8") as f:
        repo_inv = json.load(f)

    with open(LEGACY_INV_PATH, "r", encoding="utf-8") as f:
        legacy_inv = json.load(f)

    print(f"Loaded {len(repo_inv)} active repo records and {len(legacy_inv)} legacy archive records.")
    assert len(repo_inv) == 616, f"Expected 616 repo records, got {len(repo_inv)}"
    assert len(legacy_inv) == 537, f"Expected 537 legacy records, got {len(legacy_inv)}"
    total_expected = 1153
    assert len(repo_inv) + len(legacy_inv) == total_expected, "Total count mismatch!"

    unified_records = []

    # Process Active Repo files
    for item in repo_inv:
        domain = item["domain"]
        assert domain in CANONICAL_DOMAINS, f"Invalid domain: {domain}"
        status = item["status"]
        assert status in CANONICAL_STATUSES, f"Invalid status: {status}"

        q = int(item["quality"])
        qn = int(item["quantity"])
        mr = int(item["machine_readability"])
        ov = int(item["operational_value"])
        for metric_name, val in [("quality", q), ("quantity", qn), ("machine_readability", mr), ("operational_value", ov)]:
            assert 1 <= val <= 10, f"Score {metric_name}={val} out of 1-10 range"

        comp_score = round(float(item["composite_score"]), 2)
        lineage = generate_lineage_notes(item, is_legacy=False)
        rationale = item["rationale"].strip()

        record = {
            "agent": domain,
            "domain": domain,
            "file_name": item["file_name"],
            "absolute_path": item["absolute_path"],
            "quality": q,
            "quantity": qn,
            "machine_readability": mr,
            "operational_value": ov,
            "composite_score": comp_score,
            "status": status,
            "lineage_notes": lineage,
            "rationale": rationale,
            "byte_size": int(item["byte_size"]),
            "line_count": int(item["line_count"]),
            "modified_timestamp": item["last_modified"],
            "scope": item["scope"],
            "scores": {
                "quality": q,
                "quantity": qn,
                "machine_readability": mr,
                "operational_value": ov
            }
        }
        unified_records.append(record)

    # Process Legacy Archive files
    for item in legacy_inv:
        domain = item["domain"]
        assert domain in CANONICAL_DOMAINS, f"Invalid domain: {domain}"
        status = item["status"]
        assert status in CANONICAL_STATUSES, f"Invalid status: {status}"

        q = int(item["quality"])
        qn = int(item["quantity"])
        mr = int(item["readability"])
        ov = int(item["value"])
        for metric_name, val in [("quality", q), ("quantity", qn), ("machine_readability", mr), ("operational_value", ov)]:
            assert 1 <= val <= 10, f"Score {metric_name}={val} out of 1-10 range"

        comp_score = round(float(item["composite"]), 2)
        lineage = generate_lineage_notes(item, is_legacy=True)
        rationale = item["rationale"].strip()

        record = {
            "agent": domain,
            "domain": domain,
            "file_name": item["file_name"],
            "absolute_path": item["absolute_path"],
            "quality": q,
            "quantity": qn,
            "machine_readability": mr,
            "operational_value": ov,
            "composite_score": comp_score,
            "status": status,
            "lineage_notes": lineage,
            "rationale": rationale,
            "byte_size": int(item["size_bytes"]),
            "line_count": int(item["line_count"]),
            "modified_timestamp": item["mtime"],
            "scope": item["scope"],
            "scores": {
                "quality": q,
                "quantity": qn,
                "machine_readability": mr,
                "operational_value": ov
            }
        }
        unified_records.append(record)

    assert len(unified_records) == 1153, f"Expected 1153 records, got {len(unified_records)}"

    # Write JSON Deliverable
    print(f"Writing {JSON_PATH}...")
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(unified_records, f, indent=2, ensure_ascii=False)
    print("JSON deliverable successfully written.")

    # Write CSV Deliverable
    csv_columns = [
        "Agent", "File_Name", "Absolute_Path", "Quality", "Quantity",
        "Machine_Readability", "Operational_Value", "Composite_Score",
        "Status", "Lineage_Notes", "Rationale"
    ]

    print(f"Writing {CSV_PATH}...")
    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(csv_columns)
        for r in unified_records:
            writer.writerow([
                r["agent"],
                r["file_name"],
                r["absolute_path"],
                r["quality"],
                r["quantity"],
                r["machine_readability"],
                r["operational_value"],
                f"{r['composite_score']:.2f}",
                r["status"],
                r["lineage_notes"],
                r["rationale"]
            ])
    print("CSV deliverable successfully written.")

    # Verification of Written Files
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        verified_json = json.load(f)
    assert len(verified_json) == 1153

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        assert len(reader) == 1154  # header + 1153 rows
        assert reader[0] == csv_columns
        for row_idx, row in enumerate(reader[1:], start=1):
            assert len(row) == 11, f"Row {row_idx} has {len(row)} columns instead of 11"
            assert row[0] in CANONICAL_DOMAINS
            assert row[8] in CANONICAL_STATUSES
            # check numeric fields
            assert 1 <= int(row[3]) <= 10
            assert 1 <= int(row[4]) <= 10
            assert 1 <= int(row[5]) <= 10
            assert 1 <= int(row[6]) <= 10
            assert float(row[7]) >= 1.0

    print("Deliverables generation and internal verification COMPLETE.")

if __name__ == "__main__":
    main()
