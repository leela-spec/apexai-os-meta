import re
import sys
from pathlib import Path
import yaml

DOCS_DIR = Path(r"C:\GitDev\apexai-os-meta\ki-basis\docs")
TEMPLATES_FILE = DOCS_DIR / "OPERATOR_RUNBOOKS_AND_TEMPLATES.md"
PRESERVATION_FILE = DOCS_DIR / "DOCKER_VOLUME_PRESERVATION_PLAN.md"
ISOLATION_FILE = DOCS_DIR / "WORKSPACE_ISOLATION_ARCHITECTURE.md"

def test_yaml_blocks():
    print("=================================================================")
    print("CHECK 2A: Parse and validate YAML compose blocks in OPERATOR_RUNBOOKS_AND_TEMPLATES.md")
    print("=================================================================")
    content = TEMPLATES_FILE.read_text(encoding="utf-8")
    yaml_blocks = re.findall(r"```yaml\n(.*?)```", content, re.DOTALL)
    print(f"Total YAML blocks found: {len(yaml_blocks)}")
    
    assert len(yaml_blocks) >= 2, f"Expected at least 2 compose blocks, found {len(yaml_blocks)}"
    
    parsed_docs = []
    for idx, block in enumerate(yaml_blocks):
        print(f"\n--- Validating YAML Block {idx + 1} ---")
        try:
            parsed = yaml.safe_load(block)
            assert isinstance(parsed, dict), "Parsed YAML is not a dict"
            parsed_docs.append(parsed)
            proj_name = parsed.get("name")
            services = list(parsed.get("services", {}).keys())
            volumes = parsed.get("volumes", {})
            networks = parsed.get("networks", {})
            print(f"[PASS] Syntax valid!")
            print(f"       Project name: {proj_name}")
            print(f"       Services ({len(services)}): {services}")
            print(f"       Volumes ({len(volumes)}): {list(volumes.keys())}")
            print(f"       Networks ({len(networks)}): {list(networks.keys())}")
            
            # Check external: true on volumes
            for vol_key, vol_cfg in volumes.items():
                assert vol_cfg.get("external") is True, f"Volume {vol_key} missing external: true in block {idx+1}"
                assert "name" in vol_cfg, f"Volume {vol_key} missing explicit name in block {idx+1}"
            print(f"[PASS] All {len(volumes)} volumes explicitly specify external: true and explicit canonical name!")
            
            # Check services count
            assert len(services) == 7, f"Expected 7 services, got {len(services)}"
            assert set(services) == {"postgres", "valkey", "firefly", "paperless", "openproject", "nginx", "hermes"}
            
        except Exception as e:
            print(f"[FAIL] Error parsing YAML block {idx + 1}: {e}")
            raise

    # Compare Block 1 (Community) vs Block 2 (Private)
    comm_doc = parsed_docs[0]
    pvt_doc = parsed_docs[1]
    
    assert comm_doc.get("name") == "ki-basis-community", f"Block 1 project name mismatch: {comm_doc.get('name')}"
    assert pvt_doc.get("name") == "ki-basis-private", f"Block 2 project name mismatch: {pvt_doc.get('name')}"
    
    # Check volume names
    comm_vols = {v["name"] for v in comm_doc.get("volumes", {}).values()}
    pvt_vols = {v["name"] for v in pvt_doc.get("volumes", {}).values()}
    assert len(comm_vols) == 10, f"Expected 10 community volumes, got {len(comm_vols)}"
    assert len(pvt_vols) == 10, f"Expected 10 private volumes, got {len(pvt_vols)}"
    assert len(comm_vols & pvt_vols) == 0, f"Volume collision detected: {comm_vols & pvt_vols}"
    print("\n[PASS] Block 1 and Block 2 volume names are 100% disjoint (10 community, 10 private)!")

    # Check network names
    comm_net = list(comm_doc.get("networks", {}).values())[0].get("name")
    pvt_net = list(pvt_doc.get("networks", {}).values())[0].get("name")
    assert comm_net == "ki-basis-community-net", f"Unexpected comm network: {comm_net}"
    assert pvt_net == "ki-basis-private-net", f"Unexpected pvt network: {pvt_net}"
    assert comm_net != pvt_net, "Networks must be disjoint"
    print(f"[PASS] Networks are disjoint: {comm_net} vs {pvt_net}")

    # Check Hermes configurations
    comm_hermes = comm_doc["services"]["hermes"]
    pvt_hermes = pvt_doc["services"]["hermes"]
    
    # Telegram checks
    comm_tg = comm_hermes["environment"].get("TELEGRAM_BOT_TOKEN")
    pvt_tg = pvt_hermes["environment"].get("TELEGRAM_BOT_TOKEN")
    print(f"[INFO] Community Hermes TELEGRAM_BOT_TOKEN: {comm_tg}")
    print(f"[INFO] Private Hermes TELEGRAM_BOT_TOKEN: '{pvt_tg}'")
    assert pvt_tg == "", "Private Hermes TELEGRAM_BOT_TOKEN must be strictly empty"
    
    # Mount checks
    comm_mounts = comm_hermes.get("volumes", [])
    pvt_mounts = pvt_hermes.get("volumes", [])
    print(f"[INFO] Community Hermes volume mounts: {comm_mounts}")
    print(f"[INFO] Private Hermes volume mounts: {pvt_mounts}")
    
    # Check that equinox-intake is mounted only in community
    assert any("equinox-intake" in str(m) for m in comm_mounts), "Community Hermes missing equinox-intake skill mount"
    assert not any("equinox-intake" in str(m) for m in pvt_mounts), "Private Hermes must NOT mount equinox-intake skill"
    print("[PASS] Skill isolation: equinox-intake is mounted strictly in Community Hermes!")

    print("\n[VERDICT CHECK 2A]: 100% PASS - All YAML compose blocks are syntactically and structurally flawless.")

if __name__ == "__main__":
    test_yaml_blocks()
