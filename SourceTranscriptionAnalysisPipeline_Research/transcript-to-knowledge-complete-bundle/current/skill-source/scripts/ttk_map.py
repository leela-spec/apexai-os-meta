#!/usr/bin/env python3
"""Map validation, deterministic evidence ledger, and Reduce packet construction."""
from ttk_source import *
def _require_list(obj: dict[str, Any], key: str, errors: list[str]) -> list[Any]:
    value = obj.get(key)
    if not isinstance(value, list):
        errors.append(f"{key} must be a list")
        return []
    return value


def _segment_lookup(run_dir: Path) -> dict[str, dict[str, Any]]:
    transcript = read_json(run_dir / "source" / "transcript.json")
    return {row["id"]: row for row in transcript.get("segments", [])}


def _validate_source_refs(refs: Any, allowed: set[str], field: str, errors: list[str], require_nonempty: bool = True) -> list[str]:
    if not isinstance(refs, list) or (require_nonempty and not refs):
        errors.append(f"{field} must be a {'non-empty ' if require_nonempty else ''}list")
        return []
    out: list[str] = []
    for ref in refs:
        if not isinstance(ref, str) or ref not in allowed:
            errors.append(f"{field} contains non-core or unknown segment: {ref!r}")
        else:
            out.append(ref)
    return out


def _validate_quote_evidence(value: Any, allowed: set[str], lookup: dict[str, dict[str, Any]], field: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{field} must contain at least one quote evidence item")
        return
    for index, item in enumerate(value):
        prefix = f"{field}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        sid = item.get("segment_id")
        quote = item.get("quote")
        if sid not in allowed:
            errors.append(f"{prefix}.segment_id is not an allowed core segment: {sid!r}")
            continue
        if not isinstance(quote, str) or not quote.strip():
            errors.append(f"{prefix}.quote must be non-empty text")
            continue
        if quote not in lookup[sid]["text"]:
            errors.append(f"{prefix}.quote is not a verbatim substring of {sid}")


def validate_map_result(packet: dict[str, Any], result: Any, lookup: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["result must be a JSON object"]
    if result.get("schema") != MAP_RESULT_SCHEMA:
        errors.append(f"schema must be {MAP_RESULT_SCHEMA}")
    if not _packet_hash_valid(packet):
        errors.append("map packet hash is internally invalid")
    for field in ("packet_id", "packet_sha256", "window_id"):
        if result.get(field) != packet.get(field):
            errors.append(f"{field} does not match packet")
    core = set(packet.get("core_segment_ids", []))
    for key in (
        "subtopics", "key_points", "mechanisms", "protocols", "arguments",
        "candidate_claims", "entities", "concepts", "open_questions", "contradictions_or_uncertainty",
    ):
        _require_list(result, key, errors)
    for key in ("subtopics", "key_points", "mechanisms", "arguments", "open_questions", "contradictions_or_uncertainty"):
        for i, item in enumerate(result.get(key, []) if isinstance(result.get(key), list) else []):
            if not isinstance(item, dict):
                errors.append(f"{key}[{i}] must be an object")
                continue
            _validate_source_refs(item.get("source_segment_ids"), core, f"{key}[{i}].source_segment_ids", errors)
    for i, item in enumerate(result.get("protocols", []) if isinstance(result.get("protocols"), list) else []):
        if not isinstance(item, dict):
            errors.append(f"protocols[{i}] must be an object")
            continue
        _validate_source_refs(item.get("source_segment_ids"), core, f"protocols[{i}].source_segment_ids", errors)
        steps = item.get("steps")
        if not isinstance(steps, list) or not all(isinstance(step, str) and step.strip() for step in steps):
            errors.append(f"protocols[{i}].steps must be a list of non-empty strings")
    for key in ("entities", "concepts"):
        for i, item in enumerate(result.get(key, []) if isinstance(result.get(key), list) else []):
            if not isinstance(item, dict):
                errors.append(f"{key}[{i}] must be an object")
                continue
            if not isinstance(item.get("name"), str) or not item.get("name", "").strip():
                errors.append(f"{key}[{i}].name must be non-empty text")
            _validate_source_refs(item.get("source_segment_ids"), core, f"{key}[{i}].source_segment_ids", errors)
    for i, claim in enumerate(result.get("candidate_claims", []) if isinstance(result.get("candidate_claims"), list) else []):
        prefix = f"candidate_claims[{i}]"
        if not isinstance(claim, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if not isinstance(claim.get("claim_text"), str) or not claim.get("claim_text", "").strip():
            errors.append(f"{prefix}.claim_text must be non-empty text")
        if claim.get("claim_kind") not in CLAIM_KINDS:
            errors.append(f"{prefix}.claim_kind must be one of {sorted(CLAIM_KINDS)}")
        if claim.get("checkworthiness") not in CHECKWORTHINESS:
            errors.append(f"{prefix}.checkworthiness must be one of {sorted(CHECKWORTHINESS)}")
        _validate_source_refs(claim.get("source_segment_ids"), core, f"{prefix}.source_segment_ids", errors)
        _validate_quote_evidence(claim.get("quote_evidence"), core, lookup, f"{prefix}.quote_evidence", errors)
    return errors


def validate_maps(run_dir: Path) -> dict[str, Any]:
    lookup = _segment_lookup(run_dir)
    packet_dir = run_dir / "work" / "packets" / "map"
    result_dir = run_dir / "work" / "results" / "map"
    rows: list[dict[str, Any]] = []
    for packet_path in sorted(packet_dir.glob("window-*.json")):
        packet = read_json(packet_path)
        result_path = result_dir / packet_path.name
        if not result_path.exists():
            rows.append({"window_id": packet.get("window_id"), "status": "missing", "errors": []})
            continue
        try:
            result = read_json(result_path)
            errors = validate_map_result(packet, result, lookup)
        except TTKError as exc:
            errors = [str(exc)]
        rows.append({"window_id": packet.get("window_id"), "status": "valid" if not errors else "invalid", "errors": errors})
    return {
        "total": len(rows),
        "valid": sum(r["status"] == "valid" for r in rows),
        "missing": sum(r["status"] == "missing" for r in rows),
        "invalid": sum(r["status"] == "invalid" for r in rows),
        "windows": rows,
    }


def _merge_named(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for item in items:
        name = clean(item.get("name"))
        if not name:
            continue
        key = name.casefold()
        row = grouped.setdefault(key, {"name": name, "source_segment_ids": []})
        for sid in item.get("source_segment_ids", []):
            if sid not in row["source_segment_ids"]:
                row["source_segment_ids"].append(sid)
        for optional in ("type", "description"):
            value = clean(item.get(optional))
            if value and not row.get(optional):
                row[optional] = value
    return list(grouped.values())


def _claim_similarity(a: str, b: str) -> float:
    left, right = set(tokens(a)), set(tokens(b))
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def build_evidence_ledger(run_dir: Path) -> dict[str, Any]:
    report = validate_maps(run_dir)
    if report["missing"] or report["invalid"]:
        raise TTKError(f"cannot build evidence ledger: map results valid={report['valid']} missing={report['missing']} invalid={report['invalid']}")
    result_dir = run_dir / "work" / "results" / "map"
    map_results = [read_json(path) for path in sorted(result_dir.glob("window-*.json"))]
    claims_exact: dict[str, dict[str, Any]] = {}
    all_entities: list[dict[str, Any]] = []
    all_concepts: list[dict[str, Any]] = []
    categories = {key: [] for key in (
        "subtopics", "key_points", "mechanisms", "protocols", "arguments",
        "open_questions", "contradictions_or_uncertainty",
    )}
    for result in map_results:
        for key in categories:
            for item in result.get(key, []):
                categories[key].append({**item, "source_window_id": result["window_id"]})
        all_entities.extend(result.get("entities", []))
        all_concepts.extend(result.get("concepts", []))
        for claim in result.get("candidate_claims", []):
            key = norm_text(claim["claim_text"])
            row = claims_exact.get(key)
            if row is None:
                row = {**claim, "source_window_ids": [result["window_id"]]}
                claims_exact[key] = row
            else:
                if result["window_id"] not in row["source_window_ids"]:
                    row["source_window_ids"].append(result["window_id"])
                for sid in claim.get("source_segment_ids", []):
                    if sid not in row["source_segment_ids"]:
                        row["source_segment_ids"].append(sid)
                for quote in claim.get("quote_evidence", []):
                    if quote not in row["quote_evidence"]:
                        row["quote_evidence"].append(quote)
    claims = list(claims_exact.values())
    near_duplicates: list[dict[str, Any]] = []
    for i in range(len(claims)):
        for j in range(i + 1, len(claims)):
            sim = _claim_similarity(claims[i]["claim_text"], claims[j]["claim_text"])
            if sim >= 0.80:
                near_duplicates.append({
                    "left": claims[i]["claim_text"], "right": claims[j]["claim_text"],
                    "token_jaccard": round(sim, 4), "threshold": 0.80, "action": "semantic_reduce_should_review_not_auto_merge",
                })
    manifest = read_json(run_dir / "manifest.json")
    packet_hashes = [read_json(path).get("packet_sha256") for path in sorted((run_dir / "work" / "packets" / "map").glob("window-*.json"))]
    ledger = {
        "schema": EVIDENCE_SCHEMA,
        "source_sha256": manifest["source_sha256"],
        "map_packet_sha256": packet_hashes,
        "map_result_sha256": [file_hash(path) for path in sorted(result_dir.glob("window-*.json"))],
        **categories,
        "candidate_claims": claims,
        "entities": _merge_named(all_entities),
        "concepts": _merge_named(all_concepts),
        "near_duplicate_claim_candidates": near_duplicates,
    }
    write_json(run_dir / "ledger" / "evidence.json", ledger)
    coverage = {
        "schema": "ttk.coverage.v2",
        "source_segment_count": manifest["segment_count"],
        "map_window_count": report["total"],
        "valid_map_window_count": report["valid"],
        "all_windows_valid": report["total"] == report["valid"],
    }
    write_json(run_dir / "ledger" / "coverage.json", coverage)
    return ledger


def make_reduce_packet(run_dir: Path) -> dict[str, Any]:
    ledger = build_evidence_ledger(run_dir)
    manifest = read_json(run_dir / "manifest.json")
    compact = {
        key: ledger[key]
        for key in (
            "subtopics", "key_points", "mechanisms", "protocols", "arguments",
            "open_questions", "contradictions_or_uncertainty", "candidate_claims",
            "entities", "concepts", "near_duplicate_claim_candidates",
        )
    }
    packet = _attach_packet_hash({
        "schema": REDUCE_PACKET_SCHEMA,
        "contract_version": CONTRACT_VERSION,
        "packet_id": "reduce-final",
        "source_sha256": manifest["source_sha256"],
        "evidence_ledger_sha256": file_hash(run_dir / "ledger" / "evidence.json"),
        "evidence": compact,
        "result_path": "work/results/reduce.json",
        "rules": [
            "Build Macro and Meso from this validated evidence ledger; do not reread the whole transcript by default.",
            "Every final claim and load-bearing Macro/Meso statement must retain source segment IDs.",
            "Keep source support separate from external truth verification.",
            "Review near-duplicate candidates semantically; do not collapse non-equivalent claims.",
            "Preserve disagreement and uncertainty.",
        ],
    })
    write_json(run_dir / "work" / "packets" / "reduce.json", packet)
    return packet



__all__ = [name for name in globals() if not name.startswith("__")]
