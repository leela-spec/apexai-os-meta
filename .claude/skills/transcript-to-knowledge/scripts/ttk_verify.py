#!/usr/bin/env python3
"""Reduce validation and selective external-verification routing/validation."""
from ttk_map import *
def _validate_named_refs(value: Any, field: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{field} must be a list")
        return []
    if not all(isinstance(x, str) and x.strip() for x in value):
        errors.append(f"{field} must contain only non-empty strings")
        return []
    return value


def validate_reduce_result(packet: dict[str, Any], result: Any, lookup: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["reduce result must be a JSON object"]
    if result.get("schema") != REDUCE_RESULT_SCHEMA:
        errors.append(f"schema must be {REDUCE_RESULT_SCHEMA}")
    if not _packet_hash_valid(packet):
        errors.append("reduce packet hash is internally invalid")
    for field in ("packet_id", "packet_sha256"):
        if result.get(field) != packet.get(field):
            errors.append(f"{field} does not match reduce packet")
    allowed_segments = set(lookup)
    macro = result.get("macro")
    if not isinstance(macro, dict):
        errors.append("macro must be an object")
        macro = {}
    for field in ("thesis", "summary"):
        if not isinstance(macro.get(field), str) or not macro.get(field, "").strip():
            errors.append(f"macro.{field} must be non-empty text")
    takeaways = macro.get("takeaways")
    if not isinstance(takeaways, list):
        errors.append("macro.takeaways must be a list")
    else:
        for i, item in enumerate(takeaways):
            if not isinstance(item, dict) or not isinstance(item.get("text"), str) or not item.get("text", "").strip():
                errors.append(f"macro.takeaways[{i}] must be an object with non-empty text")
                continue
            _validate_source_refs(item.get("source_segment_ids"), allowed_segments, f"macro.takeaways[{i}].source_segment_ids", errors)
            _validate_named_refs(item.get("meso_refs", []), f"macro.takeaways[{i}].meso_refs", errors)
    for field in ("taxonomy", "speaker_context", "contradictions_or_uncertainty"):
        _require_list(macro, field, errors)
    meso = _require_list(result, "meso", errors)
    meso_ids: set[str] = set()
    for i, module in enumerate(meso):
        prefix = f"meso[{i}]"
        if not isinstance(module, dict):
            errors.append(f"{prefix} must be an object")
            continue
        ref = module.get("meso_ref")
        if not isinstance(ref, str) or not ref.strip() or ref in meso_ids:
            errors.append(f"{prefix}.meso_ref must be a unique non-empty string")
        else:
            meso_ids.add(ref)
        for field in ("title", "summary"):
            if not isinstance(module.get(field), str) or not module.get(field, "").strip():
                errors.append(f"{prefix}.{field} must be non-empty text")
        _validate_source_refs(module.get("source_segment_ids"), allowed_segments, f"{prefix}.source_segment_ids", errors)
        for field in ("concepts", "entities", "mechanisms", "protocols", "arguments", "caveats", "claim_refs"):
            _require_list(module, field, errors)
    claims = _require_list(result, "micro", errors)
    claim_refs: set[str] = set()
    for i, claim in enumerate(claims):
        prefix = f"micro[{i}]"
        if not isinstance(claim, dict):
            errors.append(f"{prefix} must be an object")
            continue
        ref = claim.get("claim_ref")
        if not isinstance(ref, str) or not ref.strip() or ref in claim_refs:
            errors.append(f"{prefix}.claim_ref must be a unique non-empty string")
        else:
            claim_refs.add(ref)
        if not isinstance(claim.get("claim_text"), str) or not claim.get("claim_text", "").strip():
            errors.append(f"{prefix}.claim_text must be non-empty text")
        if claim.get("claim_kind") not in CLAIM_KINDS:
            errors.append(f"{prefix}.claim_kind must be one of {sorted(CLAIM_KINDS)}")
        if claim.get("source_support") not in SOURCE_SUPPORT:
            errors.append(f"{prefix}.source_support must be one of {sorted(SOURCE_SUPPORT)}")
        if claim.get("checkworthiness") not in CHECKWORTHINESS:
            errors.append(f"{prefix}.checkworthiness must be one of {sorted(CHECKWORTHINESS)}")
        refs = _validate_source_refs(claim.get("source_segment_ids"), allowed_segments, f"{prefix}.source_segment_ids", errors)
        is_factual = claim.get("claim_kind") in {"fact", "estimate"}
        _validate_quote_evidence(claim.get("quote_evidence"), set(refs), lookup, f"{prefix}.quote_evidence", errors, required=is_factual)
        for field in ("topics", "entities"):
            _validate_named_refs(claim.get(field, []), f"{prefix}.{field}", errors)
    for i, module in enumerate(meso):
        if not isinstance(module, dict):
            continue
        for ref in module.get("claim_refs", []) if isinstance(module.get("claim_refs"), list) else []:
            if ref not in claim_refs:
                errors.append(f"meso[{i}].claim_refs references unknown claim_ref {ref!r}")
    for i, item in enumerate(takeaways if isinstance(takeaways, list) else []):
        if not isinstance(item, dict):
            continue
        for ref in item.get("meso_refs", []) if isinstance(item.get("meso_refs"), list) else []:
            if ref not in meso_ids:
                errors.append(f"macro.takeaways[{i}].meso_refs references unknown meso_ref {ref!r}")
    rejected = result.get("rejected_or_unresolved_candidates", [])
    if not isinstance(rejected, list):
        errors.append("rejected_or_unresolved_candidates must be a list")
    return errors


def validate_reduce(run_dir: Path) -> dict[str, Any]:
    packet_path = run_dir / "work" / "packets" / "reduce.json"
    result_path = run_dir / "work" / "results" / "reduce.json"
    if not packet_path.exists():
        return {"status": "packet_missing", "errors": []}
    if not result_path.exists():
        return {"status": "result_missing", "errors": []}
    try:
        packet = read_json(packet_path)
        result = read_json(result_path)
        errors = validate_reduce_result(packet, result, _segment_lookup(run_dir))
    except TTKError as exc:
        errors = [str(exc)]
    return {"status": "valid" if not errors else "invalid", "errors": errors}


def make_verify_queue(run_dir: Path, min_checkworthiness: str = "medium") -> dict[str, Any]:
    reduce_state = validate_reduce(run_dir)
    if reduce_state["status"] != "valid":
        raise TTKError(f"cannot make verification queue: reduce result is {reduce_state['status']}")
    if min_checkworthiness not in {"high", "medium", "low"}:
        raise TTKError("min_checkworthiness must be high, medium, or low")
    rank = {"none": 0, "low": 1, "medium": 2, "high": 3}
    threshold = rank[min_checkworthiness]
    reduce_result = read_json(run_dir / "work" / "results" / "reduce.json")
    items = []
    for claim in reduce_result.get("micro", []):
        if claim.get("claim_kind") != "fact":
            continue
        if claim.get("source_support") == "UNSUPPORTED":
            continue
        if rank.get(claim.get("checkworthiness"), 0) < threshold:
            continue
        items.append({
            "claim_ref": claim["claim_ref"],
            "claim_text": claim["claim_text"],
            "checkworthiness": claim["checkworthiness"],
            "source_support": claim["source_support"],
            "source_segment_ids": claim["source_segment_ids"],
            "quote_evidence": claim["quote_evidence"],
            "search_question": claim.get("verification_question") or claim["claim_text"],
            "preferred_source_types": claim.get("preferred_source_types", ["official primary source", "primary research"]),
        })
    queue = {
        "schema": VERIFY_QUEUE_SCHEMA,
        "source_sha256": read_json(run_dir / "manifest.json")["source_sha256"],
        "reduce_result_sha256": file_hash(run_dir / "work" / "results" / "reduce.json"),
        "minimum_checkworthiness": min_checkworthiness,
        "items": items,
    }
    queue["queue_sha256"] = obj_hash({k: v for k, v in queue.items() if k != "queue_sha256"})
    write_json(run_dir / "work" / "packets" / "verify-queue.json", queue)
    return queue


def _queue_hash_valid(queue: dict[str, Any]) -> bool:
    return queue.get("queue_sha256") == obj_hash({k: v for k, v in queue.items() if k != "queue_sha256"})


def validate_verify_results(run_dir: Path) -> dict[str, Any]:
    queue_path = run_dir / "work" / "packets" / "verify-queue.json"
    result_path = run_dir / "work" / "results" / "verify" / "results.json"
    if not queue_path.exists():
        return {"status": "queue_missing", "errors": []}
    queue = read_json(queue_path)
    if not result_path.exists():
        return {"status": "result_missing", "errors": []}
    result = read_json(result_path)
    errors: list[str] = []
    if not _queue_hash_valid(queue):
        errors.append("verification queue hash is internally invalid")
    if not isinstance(result, dict) or result.get("schema") != VERIFY_RESULT_SCHEMA:
        errors.append(f"schema must be {VERIFY_RESULT_SCHEMA}")
        result = result if isinstance(result, dict) else {}
    if result.get("queue_sha256") != queue.get("queue_sha256"):
        errors.append("queue_sha256 does not match current verification queue")
    expected = {item["claim_ref"] for item in queue.get("items", [])}
    seen: set[str] = set()
    rows = result.get("results")
    if not isinstance(rows, list):
        errors.append("results must be a list")
        rows = []
    for i, row in enumerate(rows):
        prefix = f"results[{i}]"
        if not isinstance(row, dict):
            errors.append(f"{prefix} must be an object")
            continue
        ref = row.get("claim_ref")
        if ref not in expected:
            errors.append(f"{prefix}.claim_ref is not in current queue: {ref!r}")
        if ref in seen:
            errors.append(f"{prefix}.claim_ref is duplicated: {ref!r}")
        seen.add(ref)
        status = row.get("status")
        if status not in EXTERNAL_STATUS:
            errors.append(f"{prefix}.status must be one of {sorted(EXTERNAL_STATUS)}")
        evidence = row.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{prefix}.evidence must be a list")
            evidence = []
        if status in {"CONFIRMED", "CONTRADICTED", "MIXED"} and not evidence:
            errors.append(f"{prefix} status {status} requires external evidence")
        for j, item in enumerate(evidence):
            ep = f"{prefix}.evidence[{j}]"
            if not isinstance(item, dict):
                errors.append(f"{ep} must be an object")
                continue
            url = item.get("url")
            if not isinstance(url, str) or urlparse(url).scheme not in {"http", "https"} or not urlparse(url).netloc:
                errors.append(f"{ep}.url must be an http(s) URL")
            if item.get("stance") not in EVIDENCE_STANCE:
                errors.append(f"{ep}.stance must be one of {sorted(EVIDENCE_STANCE)}")
            if not isinstance(item.get("title"), str) or not item.get("title", "").strip():
                errors.append(f"{ep}.title must be non-empty text")
    missing = expected - seen
    return {
        "status": "valid" if not errors else "invalid",
        "errors": errors,
        "expected": len(expected),
        "completed": len(expected & seen),
        "missing_claim_refs": sorted(missing),
    }



__all__ = [name for name in globals() if not name.startswith("__")]
