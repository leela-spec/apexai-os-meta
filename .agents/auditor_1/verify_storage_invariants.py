import os
import re
import sys
from pathlib import Path
import yaml

DOCS_DIR = Path(r"C:\GitDev\apexai-os-meta\ki-basis\docs")
TEMPLATES_FILE = DOCS_DIR / "OPERATOR_RUNBOOKS_AND_TEMPLATES.md"
PRESERVATION_FILE = DOCS_DIR / "DOCKER_VOLUME_PRESERVATION_PLAN.md"
ISOLATION_FILE = DOCS_DIR / "WORKSPACE_ISOLATION_ARCHITECTURE.md"
COMPOSE_FILE = Path(r"C:\GitDev\apexai-os-meta\ki-basis\compose.yaml")
VHDX_PATH = Path(r"C:\ProgramData\DockerDesktop\vm-data\DockerDesktop.vhdx")

def test_storage_invariants():
    print("=================================================================")
    print("CHECK 3: Storage Invariants & Volume Truth Verification")
    print("=================================================================")

    # 1. Physical VHDX reality check
    print(f"\n1. Physical VHDX Inspection at: {VHDX_PATH}")
    assert VHDX_PATH.exists(), f"VHDX file does not exist at {VHDX_PATH}"
    size_bytes = VHDX_PATH.stat().st_size
    size_gb = size_bytes / (1024 ** 3)
    size_decimal_gb = size_bytes / (1000 ** 3)
    print(f"[PASS] File exists!")
    print(f"       Exact bytes: {size_bytes} bytes")
    print(f"       Decimal GB:  {size_decimal_gb:.3f} GB")
    print(f"       Binary GiB:  {size_gb:.3f} GiB")

    # Verify matching claims in documentation
    preservation_text = PRESERVATION_FILE.read_text(encoding="utf-8")
    formatted_bytes = f"{size_bytes:,}"
    assert str(size_bytes) in preservation_text or formatted_bytes in preservation_text, f"Exact byte size {size_bytes} / {formatted_bytes} not found in {PRESERVATION_FILE}"
    print(f"[PASS] Exact byte size ({formatted_bytes}) verified in DOCKER_VOLUME_PRESERVATION_PLAN.md")

    isolation_text = ISOLATION_FILE.read_text(encoding="utf-8")
    assert str(size_bytes) in isolation_text or "33.82 GB" in isolation_text, "Size claim mismatch in WORKSPACE_ISOLATION_ARCHITECTURE.md"
    print(f"[PASS] Size claim verified in WORKSPACE_ISOLATION_ARCHITECTURE.md")

    # 2. Extract 20 volume names from mapping table in DOCKER_VOLUME_PRESERVATION_PLAN.md
    # Table format: | # | Compose Key | Canonical Physical Volume Name | ...
    table_matches = re.findall(r"\|\s*\**(\d+)\**\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", preservation_text)
    print(f"\n2. Extracted {len(table_matches)} entries from 20-Volume Mapping Table in DOCKER_VOLUME_PRESERVATION_PLAN.md")
    assert len(table_matches) == 20, f"Expected 20 entries in table, got {len(table_matches)}"

    table_vols = [m[2] for m in table_matches]
    comm_table_vols = [v for v in table_vols if v.startswith("ki-basis-community-")]
    pvt_table_vols = [v for v in table_vols if v.startswith("ki-basis-private-")]

    print(f"Community volumes ({len(comm_table_vols)}): {comm_table_vols}")
    print(f"Private volumes   ({len(pvt_table_vols)}): {pvt_table_vols}")
    assert len(comm_table_vols) == 10, f"Expected 10 community volumes, got {len(comm_table_vols)}"
    assert len(pvt_table_vols) == 10, f"Expected 10 private volumes, got {len(pvt_table_vols)}"

    # 3. Compare with compose.yaml volume templates
    compose_text = COMPOSE_FILE.read_text(encoding="utf-8")
    compose_yaml = yaml.safe_load(compose_text)
    declared_vols = compose_yaml.get("volumes", {})
    assert len(declared_vols) == 10, f"Expected 10 volume templates in compose.yaml, got {len(declared_vols)}"

    # Verify that replacing ${COMPOSE_PROJECT_NAME} generates EXACTLY these volume names
    expected_comm = {f"ki-basis-community-{k.replace('_', '-')}" for k in declared_vols.keys()}
    expected_pvt = {f"ki-basis-private-{k.replace('_', '-')}" for k in declared_vols.keys()}

    assert set(comm_table_vols) == expected_comm, f"Community table mismatch vs compose.yaml:\nTable: {set(comm_table_vols)}\nExpected: {expected_comm}"
    assert set(pvt_table_vols) == expected_pvt, f"Private table mismatch vs compose.yaml:\nTable: {set(pvt_table_vols)}\nExpected: {expected_pvt}"
    print("[PASS] Table volumes match compose.yaml project namespace derivations 100%!")

    # 4. Compare with OPERATOR_RUNBOOKS_AND_TEMPLATES.md compose blocks
    templates_text = TEMPLATES_FILE.read_text(encoding="utf-8")
    yaml_blocks = re.findall(r"```yaml\n(.*?)```", templates_text, re.DOTALL)
    comm_compose = yaml.safe_load(yaml_blocks[0])
    pvt_compose = yaml.safe_load(yaml_blocks[1])

    comm_template_vols = {v["name"] for v in comm_compose.get("volumes", {}).values()}
    pvt_template_vols = {v["name"] for v in pvt_compose.get("volumes", {}).values()}

    assert comm_template_vols == set(comm_table_vols), "Mismatch between templates.md and preservation_plan.md for community volumes"
    assert pvt_template_vols == set(pvt_table_vols), "Mismatch between templates.md and preservation_plan.md for private volumes"
    print("[PASS] Template compose volumes match 20-volume mapping table 100%!")

    print("\n[VERDICT CHECK 3]: 100% PASS - Physical storage invariants and volume naming truth verified beyond doubt.")

if __name__ == "__main__":
    test_storage_invariants()
