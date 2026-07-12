#!/usr/bin/env python3
"""Deterministic checks for the APEX orchestration system's shared contracts.

Standard library only, mirroring scripts/apex_sync.py conventions.
Fail-closed: any parse error, missing file, or unreadable input exits 2;
contract violations exit 1; clean pass exits 0. --json for machine output.

Subcommands
  packet FILE...            validate handoff-packet frontmatter (required keys + enums)
  digest FILE --expected H  recompute sha256 and compare
  verdict FILE              review-verdict consistency (pass requires all gates true)
  canon-write FILE          canon-changing-write precondition check: the gate file
                            declares operator_validation and authoritative inputs
                            (path/sha256/state); every input must be state=verified
                            with a digest that matches the recomputed file hash, and
                            operator_validation must be 'confirmed'.

Contracts: apex-meta/orchestration/schemas/handoff-packet.schema.md,
authority-state.schema.md, review-verdict.schema.md. Authority state may live in a
sidecar (design lesson DL-1) — canon-write therefore takes declared state per input
from the gate file, which must cite its sidecar.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

PACKET_REQUIRED_KEYS = [
    "packet_id", "role_accountability", "lifecycle_stage", "status",
    "target_surface", "next_state", "prerequisites", "expected_action",
    "sources_evidence", "uncertainties", "unresolved_risk", "stop_condition",
    "operator_validation", "authority",
]
AUTHORITY_REQUIRED_KEYS = ["state", "basis_digest", "verification_ref"]
ENUMS = {
    "lifecycle_stage": {"proposal", "computed", "confirmed"},
    "operator_validation": {"confirmed", "rejected", "needs_revision", "not_requested"},
    "authority.state": {"candidate", "verified", "invalidated"},
    "role_accountability": {
        "alfred", "meta_strategy", "meta_ops", "meta_detective",
        "knowledge_bank", "informatics_design", "prompts_workflows",
        "domain_worker", "operator",
    },
}
SHA_RE = re.compile(r"^(sha256:)?[a-f0-9]{64}$")


def read_text(path):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(path)
    return p.read_text(encoding="utf-8")


def frontmatter(text):
    """Return the YAML frontmatter block (between leading --- fences) or None."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def top_level_keys(block):
    """Keys at column 0 of a YAML block ('key:' or 'key: value')."""
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"^([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*)$", block, re.M)}


def nested_block(block, key):
    """Return the indented body under a top-level 'key:' line."""
    m = re.search(r"^" + re.escape(key) + r":[ \t]*(\{[^}]*\})?[ \t]*$", block, re.M)
    if m is None:
        return None
    if m.group(1):  # inline {..} form
        return m.group(1)
    start = m.end()
    body = []
    for line in block[start:].splitlines():
        if line.strip() == "" or line.startswith((" ", "\t")):
            body.append(line)
        else:
            break
    return "\n".join(body)


def scalar_in(blob, key):
    m = re.search(r"\b" + re.escape(key) + r":[ \t]*([^,}\n#]+)", blob)
    return m.group(1).strip().strip('"').strip("'") if m else None


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def norm_sha(value):
    return (value or "").removeprefix("sha256:").strip().strip('"').strip("'")


# ---------------------------------------------------------------- packet
def check_packet(path):
    violations = []
    fm = frontmatter(read_text(path))
    if fm is None:
        return [f"{path}: no YAML frontmatter block"]
    keys = top_level_keys(fm)
    for k in PACKET_REQUIRED_KEYS:
        if k not in keys:
            violations.append(f"{path}: missing required key '{k}' (absent key is illegal; [] / null are legal values)")
    for field in ("lifecycle_stage", "operator_validation", "role_accountability"):
        if field in keys and keys[field]:
            val = keys[field].strip().strip('"')
            if val and val not in ENUMS[field]:
                violations.append(f"{path}: {field}='{val}' not in {sorted(ENUMS[field])}")
    auth = nested_block(fm, "authority")
    if auth is not None:
        for k in AUTHORITY_REQUIRED_KEYS:
            if scalar_in(auth, k) is None:
                violations.append(f"{path}: authority.{k} missing")
        state = scalar_in(auth, "state")
        if state and state not in ENUMS["authority.state"]:
            violations.append(f"{path}: authority.state='{state}' invalid")
    elif "authority" in keys:
        violations.append(f"{path}: authority present but has no parseable body")
    # law: confirmed may only come from the apex-session path — a packet claiming
    # confirmed with authority.state candidate is candidate-to-canon leakage
    if keys.get("lifecycle_stage", "").startswith("confirmed"):
        state = scalar_in(auth or "", "state")
        if state != "verified":
            violations.append(f"{path}: lifecycle_stage confirmed but authority.state='{state}' (candidate-to-canon leakage)")
        if not keys.get("operator_validation", "").startswith("confirmed"):
            violations.append(f"{path}: lifecycle_stage confirmed without operator_validation confirmed")
    return violations


# ---------------------------------------------------------------- verdict
def check_verdict(path):
    text = read_text(path)
    violations = []
    overall = None
    m = re.search(r"\boverall_verdict:[ \t]*([a-z_]+)", text)
    if m:
        overall = m.group(1)
    else:
        return [f"{path}: overall_verdict not found"]
    if overall == "pass":
        gate = nested_block(text, "  evidence_free_pass_gate") or text
        for field in ("artifact_hash_verified", "required_sources_retrieved",
                      "every_pass_has_evidence", "every_pass_has_falsification_attempt",
                      "no_unresolved_critical_uncertainty"):
            fm_ = re.search(field + r":[ \t]*(\w+)", text)
            if fm_ is None or fm_.group(1) != "true":
                violations.append(f"{path}: overall pass but {field} != true (evidence-free pass forbidden)")
    for field in ("reviewer_did_not_modify_artifact", "reviewer_did_not_write_correction",
                  "reviewer_did_not_consult_other_lens_verdict"):
        fm_ = re.search(field + r":[ \t]*(\w+)", text)
        if fm_ is None:
            violations.append(f"{path}: prohibited_actions_confirmation.{field} missing")
        elif fm_.group(1) != "true":
            violations.append(f"{path}: {field}={fm_.group(1)} — reviewer violated a prohibited action; verdict invalid")
    return violations


# ---------------------------------------------------------------- canon-write
def check_canon_write(path):
    """Gate file format (YAML in frontmatter or fenced block):
    canon_write_request:
      operator_validation: confirmed
      inputs:
        - { path: <file>, sha256: <hex>, state: verified, sidecar: <file-or-null> }
    """
    text = read_text(path)
    violations = []
    ov = re.search(r"\boperator_validation:[ \t]*([a-z_]+)", text)
    if ov is None:
        violations.append(f"{path}: operator_validation missing")
    elif ov.group(1) != "confirmed":
        violations.append(f"{path}: operator_validation='{ov.group(1)}' — canon write requires confirmed")
    inputs = re.findall(r"-\s*\{([^}]*)\}", text)
    if not inputs:
        violations.append(f"{path}: no authoritative inputs declared")
    for blob in inputs:
        ipath = scalar_in(blob, "path")
        isha = norm_sha(scalar_in(blob, "sha256"))
        istate = scalar_in(blob, "state")
        if not ipath or not isha or not istate:
            violations.append(f"{path}: input entry incomplete ({blob.strip()})")
            continue
        if istate != "verified":
            violations.append(f"{ipath}: authority.state='{istate}' — canon write requires every input verified (candidate-to-canon leakage)")
        if not SHA_RE.match(isha):
            violations.append(f"{ipath}: declared sha256 malformed")
            continue
        target = Path(ipath)
        if not target.is_file():
            violations.append(f"{ipath}: declared input file does not exist (missing evidence)")
            continue
        actual = sha256_of(target)
        if actual != isha:
            violations.append(f"{ipath}: stale digest — declared {isha[:12]}…, recomputed {actual[:12]}… (re-review required)")
    return violations


# ---------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("packet"); p1.add_argument("files", nargs="+")
    p2 = sub.add_parser("digest"); p2.add_argument("file"); p2.add_argument("--expected", required=True)
    p3 = sub.add_parser("verdict"); p3.add_argument("files", nargs="+")
    p4 = sub.add_parser("canon-write"); p4.add_argument("file")
    args = ap.parse_args(argv)

    violations = []
    try:
        if args.cmd == "packet":
            for f in args.files:
                violations += check_packet(f)
        elif args.cmd == "digest":
            actual = sha256_of(args.file)
            if actual != norm_sha(args.expected):
                violations.append(f"{args.file}: digest mismatch — expected {norm_sha(args.expected)[:12]}…, got {actual[:12]}…")
        elif args.cmd == "verdict":
            for f in args.files:
                violations += check_verdict(f)
        elif args.cmd == "canon-write":
            violations += check_canon_write(args.file)
    except Exception as exc:  # fail closed
        out = {"check": args.cmd, "result": "error_fail_closed", "error": str(exc)}
        print(json.dumps(out, indent=2) if args.json else f"ERROR (fail closed): {exc}")
        return 2

    result = {"check": args.cmd, "result": "pass" if not violations else "fail",
              "violations": violations}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{args.cmd}: {'PASS' if not violations else 'FAIL'}")
        for v in violations:
            print(f"  ✗ {v}")
    return 0 if not violations else 1


if __name__ == "__main__":
    sys.exit(main())
