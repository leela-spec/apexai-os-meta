import os
import sys
import datetime
import json
import re

BASE_DIR = r"C:\Quasi Desktop\AI_PreperationUntil_06-26"
LONG_PREFIX = "\\\\?\\" + os.path.abspath(BASE_DIR)

TARGETS = [
    # Scope 1: Managed Agent KB
    {"scope": "Scope 1: Managed Agent KB", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb"},
    # Scope 2: Source Indexes
    {"scope": "Scope 2: Source Indexes", "rel": r"agent_kb_source_indexes"},
    # Scope 3: Managed Companion Systems
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\agents"},
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\rules"},
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\rituals"},
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\processes"},
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\knowledge"},
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\config"},
    # Scope 4: Modernization Revisions & Factory Artifacts
    {"scope": "Scope 4: Modernization Revisions & Factory Artifacts", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\NewFinals"},
    {"scope": "Scope 4: Modernization Revisions & Factory Artifacts", "rel": r"kb4agents"},
    {"scope": "Scope 4: Modernization Revisions & Factory Artifacts", "rel": r"Apex_Vision_previous_Mastery"},
    {"scope": "Scope 4: Modernization Revisions & Factory Artifacts", "rel": r"AI API Cost & Performance"},
    # Scope 5: Uncurated Operational Corpora
    {"scope": "Scope 5: Uncurated Operational Corpora", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\user"},
    {"scope": "Scope 5: Uncurated Operational Corpora", "rel": r"AIHowTo"},
    {"scope": "Scope 5: Uncurated Operational Corpora", "rel": r"How to AI general"},
    {"scope": "Scope 5: Uncurated Operational Corpora", "rel": r"OpenClaw Infrastructure Files"},
    {"scope": "Scope 5: Uncurated Operational Corpora", "rel": r"OpenClaw_Setup"},
]

SINGLE_FILES = [
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\managed\README-FolderManaged.md"},
    {"scope": "Scope 3: Managed Companion Systems", "rel": r"Previous_OpenClaw\07_finalopenclawsystem\README-OpenClaw.md"},
]

def get_format(fname, content):
    lower = fname.lower()
    if lower.endswith(".md"):
        if content.strip().startswith("---"):
            return "Markdown (YAML Frontmatter)"
        if "EMPTY_STATE" in content:
            return "Markdown (Scaffold)"
        if "```yaml" in content:
            return "Markdown (YAML Schema)"
        return "Markdown"
    elif lower.endswith(".yaml") or lower.endswith(".yml"):
        return "YAML Specification"
    elif lower.endswith(".json"):
        return "JSON Data/Config"
    elif lower.endswith(".py"):
        return "Python Script"
    elif lower.endswith(".diff") or ".patch" in lower:
        return "Diff / Patch"
    elif lower.endswith(".pdf"):
        return "PDF Document"
    elif lower.endswith(".txt") or lower.endswith(".env"):
        return "Plain Text / Config"
    else:
        return "Unclassified Document"

def determine_domain(rel_path, fname, content):
    p_lower = rel_path.lower().replace("/", "\\")
    f_lower = fname.lower()
    
    # 1. Alfred
    if "agent_kb\\alfred" in p_lower or f_lower == "alfred.md" or "alfred_kb_base_build" in f_lower:
        return "Alfred"
    
    # 2. Meta Detective
    if "agent_kb\\meta_detective" in p_lower or f_lower == "meta_detective.md" or "meta_detective" in p_lower:
        return "Meta Detective"
    if "how to ai general" in p_lower:
        # Check if mishap / failure / forensic
        return "Meta Detective"
        
    # 3. Meta Strategy
    if "agent_kb\\meta_strategy" in p_lower or f_lower == "meta_strategy.md" or "apex_vision" in p_lower:
        return "Meta Strategy"
    if "newfinals\\metaheadskbupdatestate" in p_lower and ("meta_strategy" in p_lower or "role_boundary" in f_lower or "current_state_audit" in f_lower):
        return "Meta Strategy"
    if f_lower == "night_planning_protocol.md":
        return "Meta Strategy"
        
    # 4. Meta Ops
    if "agent_kb\\meta_ops" in p_lower or f_lower == "meta_ops.md":
        return "Meta Ops"
    if "managed\\rules" in p_lower:
        return "Meta Ops"
    if "managed\\rituals" in p_lower:
        return "Meta Ops"
    if f_lower == "holding_orchestration_flow.md":
        return "Meta Ops"
    if "openclaw infrastructure files" in p_lower:
        return "Meta Ops"
        
    # 5. Knowledge Bank
    if "special_ops__knowledge_bank" in p_lower or f_lower == "special_ops__knowledge_bank.md":
        return "Knowledge Bank"
    if "managed\\knowledge" in p_lower:
        return "Knowledge Bank"
    if f_lower in ["agent_kb_index.md", "kb_system_reliability_audit_v1", "meta_heads_kb_base_build_index.md"]:
        return "Knowledge Bank"
    if "special_ops_kb_factory_output" in p_lower and ("manifest" in f_lower or "registry" in f_lower or "cross_agent_audit" in f_lower):
        return "Knowledge Bank"
        
    # 6. Informatics Design
    if "special_ops__informatics_design" in p_lower or f_lower == "special_ops__informatics_design.md":
        return "Informatics Design"
    if "informatics_deep_research" in f_lower or "information_design" in p_lower or "informationsdesign" in p_lower:
        return "Informatics Design"
        
    # 7. Prompts & Workflows
    if "special_ops__prompts_workflows" in p_lower or f_lower == "special_ops__prompts_workflows.md":
        return "Prompts & Workflows"
    if f_lower in ["agent_handoff_contracts.md", "deep_research_to_patchspec_workflow.md"]:
        return "Prompts & Workflows"
    if "promptdesign" in p_lower or "chat thinking" in f_lower or "chatgpt_agent_mode_kb_factory" in f_lower:
        return "Prompts & Workflows"
    if "special_ops_kb_factory_output\\agents\\prompt_design" in p_lower or "special_ops_kb_factory_output\\agents\\workflow_process" in p_lower:
        return "Prompts & Workflows"
        
    # 8. AI Routing / Special Ops
    if "special_ops__ai_handling_routing" in p_lower or f_lower == "special_ops__ai_handling_routing.md":
        return "AI Routing / Special Ops"
    if "special_ops__hygiene_clean" in p_lower or f_lower == "special_ops__hygiene_clean.md":
        return "AI Routing / Special Ops"
    if "special_ops_kb_base_build" in f_lower or "research agent api calls" in f_lower or "ai api cost" in p_lower:
        return "AI Routing / Special Ops"
    if "openclaw_setup" in p_lower:
        return "AI Routing / Special Ops"
    if "07_finalopenclawsystem\\user" in p_lower:
        return "AI Routing / Special Ops"
    if "special_ops_kb_factory_output" in p_lower:
        return "AI Routing / Special Ops"
        
    return "Meta Ops"

def evaluate_file(rel_path, fname, size, lines, content, domain):
    f_lower = fname.lower()
    p_lower = rel_path.lower()
    
    # 1. Check for empty / trivial scaffold
    if size == 0:
        return {
            "quality": 1,
            "quantity": 1,
            "readability": 1,
            "value": 1,
            "status": "Empty Scaffold / Stub",
            "rationale": "0-byte file containing zero bytes of data or instructions."
        }
    if size < 50 and (".patch" in f_lower or "untitled" in f_lower):
        return {
            "quality": 1,
            "quantity": 1,
            "readability": 2,
            "value": 1,
            "status": "Empty Scaffold / Stub",
            "rationale": "Truncated or abandoned scaffold fragment without executable content."
        }
    if "EMPTY_STATE" in content and lines < 50:
        return {
            "quality": 3,
            "quantity": 2,
            "readability": 7,
            "value": 3,
            "status": "Empty Scaffold / Stub",
            "rationale": "Unpopulated template scaffold containing only placeholder schema and EMPTY_STATE marker."
        }
        
    # 2. Check for distilled essence / core definitions
    if f_lower in ["essence.md", "alfred.md", "meta_ops.md", "meta_strategy.md", "meta_detective.md"]:
        return {
            "quality": 8,
            "quantity": min(8, max(4, lines // 15)),
            "readability": 8,
            "value": 8,
            "status": "Distilled / Migrated",
            "rationale": "Core role definition and agent boundary specification; foundational doctrine distilled into modern contracts."
        }
        
    # 3. Check for high-value canons & contracts
    if f_lower in ["operating_spine_canon.md", "agent_swarm_interaction_canon.md", "agent_handoff_contracts.md", "qa_hygiene_protocol.md", "escalation_exception_block.md"]:
        return {
            "quality": 9,
            "quantity": 9,
            "readability": 8,
            "value": 9,
            "status": "Distilled / Migrated",
            "rationale": "Authoritative system canon defining execution boundaries, swarm interactions, and strict handoff contracts."
        }
        
    # 4. Check for massive failure ledgers & research
    if f_lower == "failure_and_anti_drift_ledger.md" or "constantfailure" in f_lower:
        return {
            "quality": 9,
            "quantity": 10,
            "readability": 8,
            "value": 9,
            "status": "Reference-Only / Historical",
            "rationale": "Exhaustive empirical ledger documenting failure modes, prompt drift patterns, and anti-drift validation rules."
        }
    if "studies" in p_lower or f_lower.endswith(".pdf"):
        return {
            "quality": 8,
            "quantity": min(10, max(5, lines // 50)),
            "readability": 6,
            "value": 7,
            "status": "Reference-Only / Historical",
            "rationale": "Academic research paper and empirical study analyzing multi-agent failures, long-context dynamics, and diffusion processes."
        }
        
    # 5. Check for patches and diffs
    if f_lower.endswith(".diff") or ".patch" in f_lower:
        return {
            "quality": 6,
            "quantity": min(7, max(3, lines // 30)),
            "readability": 7,
            "value": 5,
            "status": "Reference-Only / Historical",
            "rationale": "Historical unified diff artifact created during iterative KB patching and schema normalization."
        }
        
    # 6. Check for Source Indexes
    if "agent_kb_source_indexes" in p_lower:
        return {
            "quality": 8,
            "quantity": min(8, max(5, lines // 30)),
            "readability": 9,
            "value": 8,
            "status": "Distilled / Migrated",
            "rationale": "Curated source authority index mapping external repo baselines to agent KB build requirements."
        }

    # 7. Check for populated Special Ops KB files
    if "special_ops__" in p_lower:
        if f_lower in ["best_practices.md", "mistakes.md", "templates.md", "learning_queue.md"]:
            return {
                "quality": 8,
                "quantity": min(9, max(5, lines // 25)),
                "readability": 8,
                "value": 8,
                "status": "Distilled / Migrated",
                "rationale": "Populated domain knowledge base containing concrete production rules, error patterns, and template schemas."
            }
        if "appendix" in f_lower:
            return {
                "quality": 7,
                "quantity": min(9, max(4, lines // 30)),
                "readability": 7,
                "value": 7,
                "status": "Reference-Only / Historical",
                "rationale": "Specialized domain appendix detailing ranking ledgers, anti-drift evidence, or execution contracts."
            }

    # 8. Check for uncurated corpora (AIHowTo, How to AI general, Setup, Infrastructure)
    if "aihowto" in p_lower:
        return {
            "quality": 7,
            "quantity": min(8, max(4, lines // 30)),
            "readability": 7,
            "value": 7,
            "status": "Reference-Only / Historical",
            "rationale": "Prompt engineering rules and information design synthesis from early agent design experiments."
        }
    if "how to ai general" in p_lower:
        return {
            "quality": 6,
            "quantity": min(9, max(4, lines // 40)),
            "readability": 5,
            "value": 6,
            "status": "Reference-Only / Historical",
            "rationale": "Raw incident report, mishap postmortem, or empirical debugging notes from multi-agent orchestration trials."
        }
    if "openclaw infrastructure files" in p_lower:
        return {
            "quality": 7,
            "quantity": min(8, max(4, lines // 25)),
            "readability": 7,
            "value": 6,
            "status": "Reference-Only / Historical",
            "rationale": "Operational infrastructure policy memos, approval matrices, and rollout assumptions for legacy swarm."
        }
    if "openclaw_setup" in p_lower:
        return {
            "quality": 6,
            "quantity": min(8, max(3, lines // 35)),
            "readability": 6,
            "value": 5,
            "status": "Reference-Only / Historical",
            "rationale": "Setup runbook, recovery procedure, or migration handover for legacy OpenClaw runtime instances."
        }
        
    # Default balanced scoring
    q = min(8, max(4, 5 + (1 if lines > 100 else 0) + (1 if "```" in content else 0)))
    qty = min(9, max(3, lines // 35))
    r = min(8, max(4, 6 + (1 if content.startswith("#") else 0) + (1 if "---" in content else 0)))
    v = min(8, max(4, 6 if lines > 50 else 4))
    
    return {
        "quality": q,
        "quantity": qty,
        "readability": r,
        "value": v,
        "status": "Reference-Only / Historical",
        "rationale": f"Legacy reference document containing {lines} lines of domain-specific specifications and working context."
    }

def scan_all():
    records = []
    seen = set()
    
    # 1. Walk targets
    for t in TARGETS:
        scope_name = t["scope"]
        rel_target = t["rel"]
        full_dir = os.path.join(LONG_PREFIX, rel_target)
        if not os.path.exists(full_dir):
            continue
            
        for root, dirs, files in os.walk(full_dir):
            clean_root = root.replace("\\\\?\\", "")
            for f in sorted(files):
                clean_full = os.path.join(clean_root, f)
                if clean_full in seen:
                    continue
                seen.add(clean_full)
                
                long_full = os.path.join(root, f)
                st = os.stat(long_full)
                size = st.st_size
                mtime = datetime.datetime.fromtimestamp(st.st_mtime, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                
                content = ""
                lines = 0
                try:
                    with open(long_full, "r", encoding="utf-8", errors="ignore") as fl:
                        content = fl.read()
                        lines = len(content.splitlines())
                except:
                    pass
                
                rel_from_base = os.path.relpath(clean_full, BASE_DIR)
                fmt = get_format(f, content)
                domain = determine_domain(rel_from_base, f, content)
                eval_res = evaluate_file(rel_from_base, f, size, lines, content, domain)
                
                comp = round(0.35 * eval_res["quality"] + 0.30 * eval_res["value"] + 0.20 * eval_res["quantity"] + 0.15 * eval_res["readability"], 2)
                
                records.append({
                    "scope": scope_name,
                    "file_name": f,
                    "rel_path": rel_from_base,
                    "absolute_path": clean_full,
                    "size_bytes": size,
                    "line_count": lines,
                    "mtime": mtime,
                    "format": fmt,
                    "domain": domain,
                    "quality": eval_res["quality"],
                    "quantity": eval_res["quantity"],
                    "readability": eval_res["readability"],
                    "value": eval_res["value"],
                    "composite": comp,
                    "status": eval_res["status"],
                    "rationale": eval_res["rationale"],
                    "has_frontmatter": content.strip().startswith("---")
                })
                
    # 2. Check single files
    for sf in SINGLE_FILES:
        scope_name = sf["scope"]
        rel_target = sf["rel"]
        clean_full = os.path.join(BASE_DIR, rel_target)
        long_full = os.path.join(LONG_PREFIX, rel_target)
        if clean_full in seen or not os.path.exists(long_full):
            continue
        seen.add(clean_full)
        st = os.stat(long_full)
        size = st.st_size
        mtime = datetime.datetime.fromtimestamp(st.st_mtime, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        content = ""
        lines = 0
        try:
            with open(long_full, "r", encoding="utf-8", errors="ignore") as fl:
                content = fl.read()
                lines = len(content.splitlines())
        except:
            pass
        f = os.path.basename(clean_full)
        fmt = get_format(f, content)
        domain = determine_domain(rel_target, f, content)
        eval_res = evaluate_file(rel_target, f, size, lines, content, domain)
        comp = round(0.35 * eval_res["quality"] + 0.30 * eval_res["value"] + 0.20 * eval_res["quantity"] + 0.15 * eval_res["readability"], 2)
        records.append({
            "scope": scope_name,
            "file_name": f,
            "rel_path": rel_target,
            "absolute_path": clean_full,
            "size_bytes": size,
            "line_count": lines,
            "mtime": mtime,
            "format": fmt,
            "domain": domain,
            "quality": eval_res["quality"],
            "quantity": eval_res["quantity"],
            "readability": eval_res["readability"],
            "value": eval_res["value"],
            "composite": comp,
            "status": eval_res["status"],
            "rationale": eval_res["rationale"],
            "has_frontmatter": content.strip().startswith("---")
        })
        
    return records

if __name__ == "__main__":
    records = scan_all()
    print(f"Total verified files scanned: {len(records)}")
    
    # Save json for internal use
    with open("legacy_inventory.json", "w", encoding="utf-8") as jf:
        json.dump(records, jf, indent=2)
    print("Saved legacy_inventory.json")
