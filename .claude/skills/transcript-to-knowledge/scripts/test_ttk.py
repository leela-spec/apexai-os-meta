#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

import ttk


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sample_segments(n=10):
    topics = [
        "Alpha planning discusses launch scope and customer research.",
        "Alpha planning confirms the prototype date is October 10 2026.",
        "Alpha risks include staffing and vendor delays.",
        "Beta architecture introduces an evidence ledger for provenance.",
        "Beta architecture keeps deterministic validation outside the model.",
        "Beta architecture routes only factual claims for verification.",
        "Gamma operations describes a three step review process.",
        "Gamma operations says first prepare evidence then validate then compile.",
        "Gamma risks include stale packets and mismatched quotes.",
        "Closing discussion preserves disagreement about the launch date.",
    ]
    out = []
    for i in range(n):
        out.append({
            "start": i * 15.0,
            "end": i * 15.0 + 12.0,
            "speaker": "Alice" if i % 2 == 0 else "Bob",
            "text": topics[i % len(topics)],
        })
    return out


def make_run(root: Path, n=10, context_segments=1):
    source = root / "source.json"
    write_json(source, {"segments": sample_segments(n)})
    run = root / "run"
    ttk.init_run(source, run, target_words=22, min_words=12, max_words=30, block_segments=2,
                 pause_weight=0.15, context_segments=context_segments)
    return source, run


def valid_map_result(packet: dict):
    core_segments = [s for s in packet["source_segments"] if s["role"] == "core"]
    first = core_segments[0]
    refs = [s["id"] for s in core_segments]
    return {
        "schema": ttk.MAP_RESULT_SCHEMA,
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "window_id": packet["window_id"],
        "subtopics": [{"label": "Primary theme", "source_segment_ids": refs}],
        "key_points": [{"text": first["text"], "source_segment_ids": [first["id"]]}],
        "mechanisms": [],
        "protocols": [],
        "arguments": [],
        "candidate_claims": [{
            "claim_text": first["text"],
            "claim_kind": "fact",
            "speaker": first.get("speaker"),
            "source_segment_ids": [first["id"]],
            "quote_evidence": [{"segment_id": first["id"], "quote": first["text"]}],
            "checkworthiness": "medium",
        }],
        "entities": [{"name": "Alice", "type": "person", "source_segment_ids": [first["id"]]}],
        "concepts": [{"name": "Evidence Ledger", "source_segment_ids": [first["id"]]}],
        "open_questions": [],
        "contradictions_or_uncertainty": [],
    }


def fill_maps(run: Path):
    for packet_path in sorted((run / "work" / "packets" / "map").glob("*.json")):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        write_json(run / "work" / "results" / "map" / packet_path.name, valid_map_result(packet))


def valid_reduce_result(run: Path):
    packet = json.loads((run / "work" / "packets" / "reduce.json").read_text(encoding="utf-8"))
    transcript = json.loads((run / "source" / "transcript.json").read_text(encoding="utf-8"))
    first, second = transcript["segments"][0], transcript["segments"][1]
    return {
        "schema": ttk.REDUCE_RESULT_SCHEMA,
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "macro": {
            "thesis": "The discussion develops a provenance-first transcript knowledge workflow.",
            "summary": "The speakers move from planning into architecture and operational safeguards.",
            "takeaways": [{
                "text": "Evidence provenance and deterministic validation are central.",
                "source_segment_ids": [first["id"]],
                "meso_refs": ["meso-001"],
            }],
            "taxonomy": ["Evidence Ledger", "Validation"],
            "speaker_context": ["Alice and Bob are transcript speaker labels."],
            "contradictions_or_uncertainty": ["The launch date is discussed with disagreement."],
        },
        "meso": [{
            "meso_ref": "meso-001",
            "title": "Evidence Pipeline",
            "summary": "The pipeline separates source evidence from semantic interpretation.",
            "source_segment_ids": [first["id"], second["id"]],
            "concepts": ["Evidence Ledger"],
            "entities": ["Alice"],
            "mechanisms": ["Deterministic validators reject malformed semantic outputs."],
            "protocols": ["Prepare evidence", "Validate outputs", "Compile wiki"],
            "arguments": [],
            "caveats": ["External truth is separate from transcript support."],
            "claim_refs": ["micro-001", "micro-002"],
        }],
        "micro": [
            {
                "claim_ref": "micro-001",
                "claim_text": first["text"],
                "claim_kind": "fact",
                "speaker": first.get("speaker"),
                "source_segment_ids": [first["id"]],
                "quote_evidence": [{"segment_id": first["id"], "quote": first["text"]}],
                "source_support": "SUPPORTED",
                "checkworthiness": "medium",
                "topics": ["Evidence Ledger"],
                "entities": ["Alice"],
                "context": "This proposition is retained from the transcript.",
            },
            {
                "claim_ref": "micro-002",
                "claim_text": "Bob recommends validating before compiling.",
                "claim_kind": "recommendation",
                "speaker": second.get("speaker"),
                "source_segment_ids": [second["id"]],
                "quote_evidence": [{"segment_id": second["id"], "quote": second["text"]}],
                "source_support": "SUPPORTED",
                "checkworthiness": "none",
                "topics": ["Validation"],
                "entities": ["Bob"],
                "context": "Recommendations are not externally fact-checked by default.",
            },
        ],
        "rejected_or_unresolved_candidates": [],
    }


class TTKTests(unittest.TestCase):
    def test_init_is_deterministic_and_windows_cover_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, run = make_run(root)
            before = (run / "windows" / "index.json").read_bytes()
            manifest = ttk.init_run(source, run, 22, 12, 30, 2, 0.15, 1)
            self.assertEqual(before, (run / "windows" / "index.json").read_bytes())
            windows = json.loads(before)
            core = [sid for w in windows["windows"] for sid in w["core_segment_ids"]]
            transcript = json.loads((run / "source" / "transcript.json").read_text())
            self.assertEqual(core, [s["id"] for s in transcript["segments"]])
            self.assertEqual(manifest["window_count"], len(windows["windows"]))
            self.assertGreater(manifest["window_count"], 1)

    def test_map_evidence_cannot_use_context_only_segment(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp), context_segments=1)
            packets = sorted((run / "work" / "packets" / "map").glob("*.json"))
            packet = json.loads(packets[1].read_text())
            self.assertTrue(packet["context_only_segment_ids"])
            result = valid_map_result(packet)
            context_id = packet["context_only_segment_ids"][0]
            text = next(s["text"] for s in packet["source_segments"] if s["id"] == context_id)
            result["candidate_claims"][0]["source_segment_ids"] = [context_id]
            result["candidate_claims"][0]["quote_evidence"] = [{"segment_id": context_id, "quote": text}]
            errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
            self.assertTrue(any("non-core" in e or "allowed core" in e for e in errors))

    def test_quote_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            packet_path = sorted((run / "work" / "packets" / "map").glob("*.json"))[0]
            packet = json.loads(packet_path.read_text())
            result = valid_map_result(packet)
            result["candidate_claims"][0]["quote_evidence"][0]["quote"] = "This sentence was never said."
            errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
            self.assertTrue(any("verbatim substring" in e for e in errors))

    def test_stale_packet_hash_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            packet_path = sorted((run / "work" / "packets" / "map").glob("*.json"))[0]
            packet = json.loads(packet_path.read_text())
            result = valid_map_result(packet)
            result["packet_sha256"] = "0" * 64
            errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
            self.assertTrue(any("packet_sha256" in e for e in errors))

    def test_untimed_text_never_fabricates_timestamps(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "plain.txt"
            source.write_text("Alice: first idea\nBob: second idea\n", encoding="utf-8")
            run = root / "run"
            ttk.init_run(source, run, 20, 5, 30, 1, 0.15, 0)
            manifest = json.loads((run / "manifest.json").read_text())
            transcript = json.loads((run / "source" / "transcript.json").read_text())
            self.assertEqual(manifest["timestamp_quality"], "none")
            self.assertTrue(all(s["start"] is None and s["end"] is None for s in transcript["segments"]))

    def test_full_pipeline_resume_validate_verify_compile(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            initial = ttk.status(run)
            self.assertEqual(initial["stage"], "map")
            fill_maps(run)
            self.assertEqual(ttk.status(run)["stage"], "reduce_packet_ready")
            ttk.make_reduce_packet(run)
            self.assertEqual(ttk.status(run)["stage"], "reduce")
            reduce_result = valid_reduce_result(run)
            write_json(run / "work" / "results" / "reduce.json", reduce_result)
            self.assertEqual(ttk.validate_reduce(run)["status"], "valid")
            queue = ttk.make_verify_queue(run, "medium")
            self.assertEqual(len(queue["items"]), 1)
            self.assertEqual(queue["items"][0]["claim_ref"], "micro-001")
            verification = {
                "schema": ttk.VERIFY_RESULT_SCHEMA,
                "queue_sha256": queue["queue_sha256"],
                "results": [{
                    "claim_ref": "micro-001",
                    "status": "CONFIRMED",
                    "rationale": "Primary evidence supports the claim.",
                    "evidence": [{
                        "title": "Primary Source",
                        "url": "https://example.org/primary",
                        "publisher": "Example",
                        "date": "2026-08-18",
                        "stance": "supports",
                        "note": "Direct support.",
                    }],
                }],
            }
            write_json(run / "work" / "results" / "verify" / "results.json", verification)
            self.assertEqual(ttk.validate_verify_results(run)["status"], "valid")
            compiled = ttk.compile_wiki(run)
            self.assertEqual(compiled["claim_count"], 2)
            self.assertTrue((run / "wiki" / "index.md").is_file())
            self.assertTrue((run / "wiki" / "summaries" / "Macro.md").is_file())
            wiki = run / "wiki"
            for md in wiki.rglob("*.md"):
                for target in re.findall(r"\[\[([^]|]+)", md.read_text(encoding="utf-8")):
                    self.assertTrue((wiki / (target + ".md")).exists(), f"orphan wikilink {target} in {md}")
            report = ttk.validate_run(run)
            self.assertTrue(report["ok"])
            self.assertTrue(report["complete"])
            self.assertTrue(report["compiled_current"])

    def test_compiled_wiki_becomes_stale_when_reduce_result_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            fill_maps(run)
            ttk.make_reduce_packet(run)
            result = valid_reduce_result(run)
            write_json(run / "work" / "results" / "reduce.json", result)
            ttk.make_verify_queue(run)
            ttk.compile_wiki(run)
            self.assertEqual(ttk.status(run)["stage"], "compiled")

            result["macro"]["thesis"] += " Updated after the first compile."
            write_json(run / "work" / "results" / "reduce.json", result)
            self.assertEqual(ttk.validate_reduce(run)["status"], "valid")
            state = ttk.status(run)
            self.assertEqual(state["stage"], "compile_stale")
            self.assertFalse(state["compiled_current"])
            report = ttk.validate_run(run)
            self.assertFalse(report["complete"])
            self.assertTrue(any("stale" in warning for warning in report["warnings"]))

    def test_recompile_removes_stale_generated_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            fill_maps(run)
            ttk.make_reduce_packet(run)
            write_json(run / "work" / "results" / "reduce.json", valid_reduce_result(run))
            ttk.make_verify_queue(run)
            ttk.compile_wiki(run)
            stale = run / "wiki" / "modules" / "stale-old-module.md"
            stale.write_text("# stale\n", encoding="utf-8")
            self.assertTrue(stale.exists())
            ttk.compile_wiki(run)
            self.assertFalse(stale.exists())

    def test_verification_requires_evidence_for_decisive_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            fill_maps(run)
            ttk.make_reduce_packet(run)
            write_json(run / "work" / "results" / "reduce.json", valid_reduce_result(run))
            queue = ttk.make_verify_queue(run)
            bad = {
                "schema": ttk.VERIFY_RESULT_SCHEMA,
                "queue_sha256": queue["queue_sha256"],
                "results": [{"claim_ref": "micro-001", "status": "CONFIRMED", "evidence": []}],
            }
            write_json(run / "work" / "results" / "verify" / "results.json", bad)
            state = ttk.validate_verify_results(run)
            self.assertEqual(state["status"], "invalid")
            self.assertTrue(any("requires external evidence" in e for e in state["errors"]))

    def test_nonfactual_claim_not_routed_for_web_verification(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            fill_maps(run)
            ttk.make_reduce_packet(run)
            write_json(run / "work" / "results" / "reduce.json", valid_reduce_result(run))
            queue = ttk.make_verify_queue(run, "low")
            refs = {item["claim_ref"] for item in queue["items"]}
            self.assertIn("micro-001", refs)
            self.assertNotIn("micro-002", refs)

    def test_near_duplicate_claims_are_flagged_not_silently_merged(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            packet_paths = sorted((run / "work" / "packets" / "map").glob("*.json"))
            for idx, packet_path in enumerate(packet_paths):
                packet = json.loads(packet_path.read_text())
                result = valid_map_result(packet)
                if idx < 2:
                    core = next(s for s in packet["source_segments"] if s["role"] == "core")
                    result["candidate_claims"][0]["claim_text"] = (
                        "The evidence ledger preserves source provenance for every important claim."
                        if idx == 0 else
                        "The evidence ledger preserves source provenance for each important claim."
                    )
                    result["candidate_claims"][0]["source_segment_ids"] = [core["id"]]
                    result["candidate_claims"][0]["quote_evidence"] = [{"segment_id": core["id"], "quote": core["text"]}]
                write_json(run / "work" / "results" / "map" / packet_path.name, result)
            ledger = ttk.build_evidence_ledger(run)
            self.assertGreaterEqual(len(ledger["near_duplicate_claim_candidates"]), 1)
            texts = [c["claim_text"] for c in ledger["candidate_claims"]]
            self.assertIn("The evidence ledger preserves source provenance for every important claim.", texts)
            self.assertIn("The evidence ledger preserves source provenance for each important claim.", texts)

    def test_doctor_has_no_network_or_llm_dependency(self):
        state = ttk.doctor()
        self.assertTrue(state["stdlib_only"])
        self.assertFalse(state["network_calls_in_cli"])
        self.assertFalse(state["llm_calls_in_cli"])

    def test_d35_factual_without_quote_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            packet_path = sorted((run / "work" / "packets" / "map").glob("*.json"))[0]
            packet = json.loads(packet_path.read_text())
            result = valid_map_result(packet)
            result["candidate_claims"][0]["claim_kind"] = "fact"
            result["candidate_claims"][0]["quote_evidence"] = []
            errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
            self.assertTrue(any("quote evidence" in e for e in errors))

    def test_d35_opinion_and_prediction_with_core_ref_no_quote_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            packet_path = sorted((run / "work" / "packets" / "map").glob("*.json"))[0]
            packet = json.loads(packet_path.read_text())
            result = valid_map_result(packet)
            # Change to opinion without quote
            result["candidate_claims"][0]["claim_kind"] = "opinion"
            result["candidate_claims"][0]["quote_evidence"] = []
            errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
            self.assertEqual(errors, [])

            # Change to prediction without quote
            result["candidate_claims"][0]["claim_kind"] = "prediction"
            errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
            self.assertEqual(errors, [])

    def test_d35_invalid_source_ref_fails_for_all_kinds(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            packet_path = sorted((run / "work" / "packets" / "map").glob("*.json"))[0]
            packet = json.loads(packet_path.read_text())
            for kind in ("fact", "opinion", "prediction", "mechanism"):
                result = valid_map_result(packet)
                result["candidate_claims"][0]["claim_kind"] = kind
                result["candidate_claims"][0]["source_segment_ids"] = ["non-existent-seg-999"]
                errors = ttk.validate_map_result(packet, result, ttk._segment_lookup(run))
                self.assertTrue(any("non-core or unknown segment" in e for e in errors))

    def test_d35_unresolved_reduce_claim_ref_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, run = make_run(Path(tmp))
            fill_maps(run)
            ttk.make_reduce_packet(run)
            reduce_result = valid_reduce_result(run)
            reduce_result["meso"][0]["claim_refs"].append("micro-unknown-999")
            errors = ttk.validate_reduce_result(
                json.loads((run / "work" / "packets" / "reduce.json").read_text()),
                reduce_result,
                ttk._segment_lookup(run)
            )
            self.assertTrue(any("references unknown claim_ref" in e for e in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
