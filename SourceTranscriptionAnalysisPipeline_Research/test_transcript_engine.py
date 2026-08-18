"""
test_transcript_engine.py
End-to-end unit tests for the deterministic 3-tier engine (KR4 requirement).
Run with: python -m unittest test_transcript_engine.py -v
"""
import sys, os
import unittest
import tempfile
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from transcript_engine import (
    hhmmss_to_seconds, seconds_to_hhmmss, MacroResult, SpeakerProfile,
    MesoModule, MicroClaim, KnowledgeEngine, VerificationHook, VERDICTS,
    GroundingError, parse_srt_spoken_text, parse_srt_segments
)


class TestTranscriptEngine(unittest.TestCase):

    def test_timestamp_roundtrip(self):
        self.assertEqual(hhmmss_to_seconds("[00:12:34]"), 754)
        self.assertEqual(seconds_to_hhmmss(754), "00:12:34")

    def test_timestamp_invalid_raises(self):
        with self.assertRaises(ValueError):
            hhmmss_to_seconds("[bad]")

    def test_micro_claim_validates_timestamp(self):
        with self.assertRaises(ValueError):
            MicroClaim(claim_id="1", proposition="x", quote="y", timestamp="99:99",
                       internal_confidence="anecdote")

    def test_micro_claim_validates_verdict(self):
        with self.assertRaises(ValueError):
            MicroClaim(claim_id="1", proposition="x", quote="y", timestamp="00:01:00",
                       internal_confidence="anecdote", verdict="MAYBE")

    def test_micro_claim_validates_claim_type(self):
        with self.assertRaises(ValueError):
            MicroClaim(claim_id="1", proposition="x", quote="y", timestamp="00:01:00",
                       claim_type="INVALID_TYPE")

    def test_macro_markdown_contains_wikilinks(self):
        macro = MacroResult(
            core_thesis="Deterministic pipelines beat ad-hoc summarization.",
            global_takeaways=["Whisper params matter", "VAD prevents hallucination loops"],
            taxonomy_tags=["[[AI Orchestration]]", "[[Whisper]]"],
            speakers=[SpeakerProfile(label="Speaker 0", name="Host", credentials="ML engineer")],
        )
        md = macro.to_markdown()
        self.assertIn("[[AI Orchestration]]", md)
        self.assertIn("Core Thesis", md)

    def test_meso_module_renders_timestamp_range(self):
        mod = MesoModule(
            title="Whisper Ingestion Standards",
            start_ts="00:00:00", end_ts="00:08:12",
            arguments=["int8 quantization halves RAM with no WER loss"],
            protocol_steps=["Condition audio to 16kHz mono", "Apply Silero VAD", "Run faster-whisper"],
            caveats=["GPU float16 recommended for beam_size=5"],
            source_segment_ids=["seg-0001", "seg-0002"]
        )
        md = mod.to_markdown()
        self.assertIn("[00:00:00 - 00:08:12]", md)
        self.assertIn("1. Condition audio to 16kHz mono", md)
        self.assertIn("seg-0001", md)

    def test_empty_protocol_steps_is_valid(self):
        mod = MesoModule(
            title="Descriptive Section",
            start_ts="00:00:00", end_ts="00:05:00",
            arguments=["Descriptive narrative of historic events."],
            protocol_steps=[],
            caveats=[]
        )
        md = mod.to_markdown()
        self.assertIn("No discrete protocol steps defined", md)

    def test_micro_claim_default_verdict_is_unverified(self):
        c = MicroClaim(claim_id="1", proposition="int8 quantization causes zero WER loss",
                       quote="int8 has zero word error rate loss", timestamp="00:02:15",
                       internal_confidence="hypothesis")
        self.assertEqual(c.verdict, "UNVERIFIED")
        self.assertIn(c.verdict, VERDICTS)

    def test_verification_hook_leaves_verdict_unverified(self):
        def fake_search(query):
            return [{"url": "https://example.org/paper"}, {"url": "https://example.org/2"}]
        hook = VerificationHook(fake_search)
        c = MicroClaim(claim_id="2", proposition="Silero VAD reduces hallucination loops",
                       quote="VAD eliminates silence hallucination", timestamp="00:03:40",
                       internal_confidence="peer-reviewed")
        verified = hook.verify(c)
        self.assertEqual(verified.external_sources, ["https://example.org/paper", "https://example.org/2"])
        # Crucial anti-fabrication check: external_verdict MUST remain UNVERIFIED
        self.assertEqual(verified.verdict, "UNVERIFIED")

    def test_from_semantic_result_validates_and_rejects_invented_quote(self):
        sample_srt = "Hello world and welcome to quantitative cycle modeling."
        data = {
            "macro": {
                "core_thesis": "Cycle models reveal periodicity.",
                "global_takeaways": ["Takeaway 1"],
                "taxonomy_tags": ["[[Cycles]]"],
                "speakers": []
            },
            "meso": [],
            "micro": [
                {
                    "claim_id": "1",
                    "proposition": "Invented claim",
                    "quote": "This quote does not exist in the SRT audio.",
                    "timestamp": "00:00:01",
                    "claim_type": "FACT",
                    "verdict": "UNVERIFIED"
                }
            ]
        }
        with self.assertRaises(GroundingError) as ctx:
            KnowledgeEngine.from_semantic_result(data, spoken_text=sample_srt)
        self.assertIn("NOT present verbatim", str(ctx.exception))

    def test_from_semantic_result_validates_segment_provenance(self):
        segments = [
            {"id": "seg-0001", "start": 0, "end": 5, "start_ts": "00:00:00", "end_ts": "00:00:05", "text": "Hello world and welcome."}
        ]
        data = {
            "macro": {
                "core_thesis": "Thesis",
                "global_takeaways": ["T1"],
                "taxonomy_tags": [],
                "speakers": []
            },
            "meso": [],
            "micro": [
                {
                    "claim_id": "1",
                    "proposition": "Greeting",
                    "quote": "Hello world and welcome.",
                    "timestamp": "00:00:00",
                    "source_segment_ids": ["seg-0001"]
                }
            ]
        }
        engine = KnowledgeEngine.from_semantic_result(data, spoken_text="Hello world and welcome.", segments=segments)
        self.assertEqual(len(engine.micro), 1)
        self.assertEqual(engine.micro[0].source_segment_ids, ["seg-0001"])
        self.assertEqual(engine.micro[0].source_start, "00:00:00")
        self.assertEqual(engine.micro[0].source_end, "00:00:05")
        self.assertIsNotNone(engine.coverage_stats)
        self.assertEqual(engine.coverage_stats["coverage_pct"], 100.0)

    def test_from_semantic_result_rejects_unknown_segment_id(self):
        segments = [
            {"id": "seg-0001", "start": 0, "end": 5, "start_ts": "00:00:00", "end_ts": "00:00:05", "text": "Hello world and welcome."}
        ]
        data = {
            "macro": {
                "core_thesis": "Thesis",
                "global_takeaways": ["T1"],
                "taxonomy_tags": [],
                "speakers": []
            },
            "meso": [],
            "micro": [
                {
                    "claim_id": "1",
                    "proposition": "Greeting",
                    "quote": "Hello world and welcome.",
                    "timestamp": "00:00:00",
                    "source_segment_ids": ["seg-9999"]
                }
            ]
        }
        with self.assertRaises(GroundingError) as ctx:
            KnowledgeEngine.from_semantic_result(data, spoken_text="Hello world and welcome.", segments=segments)
        self.assertIn("unknown source_segment_id", str(ctx.exception))

    def test_from_semantic_result_rejects_srt_metadata_quote(self):
        sample_srt = "00:00:01,000 --> 00:00:05,000 Spoken text"
        data = {
            "macro": {
                "core_thesis": "Thesis",
                "global_takeaways": ["T1"],
                "taxonomy_tags": [],
                "speakers": []
            },
            "meso": [],
            "micro": [
                {
                    "claim_id": "1",
                    "proposition": "SRT corrupted",
                    "quote": "00:00:01,000 --> 00:00:05,000 Spoken text",
                    "timestamp": "00:00:01"
                }
            ]
        }
        with self.assertRaises(GroundingError) as ctx:
            KnowledgeEngine.from_semantic_result(data, spoken_text=sample_srt)
        self.assertIn("raw SRT formatting metadata", str(ctx.exception))

    def test_engine_end_to_end_renders_full_wiki_markdown(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            engine = KnowledgeEngine()
            engine.set_macro(MacroResult(
                core_thesis="Macro-Meso-Micro decomposition preserves fidelity at scale.",
                global_takeaways=["Atomic claims enable fact-checking"],
                taxonomy_tags=["[[Knowledge Extraction]]"],
                speakers=[SpeakerProfile(label="Speaker 0")],
            ))
            engine.add_meso_module(MesoModule(
                title="Framework Overview", start_ts="00:00:00", end_ts="00:05:00",
                arguments=["Monolithic summaries lose detail"], protocol_steps=["Tier 1", "Tier 2", "Tier 3"],
                caveats=[],
            ))
            engine.add_micro_claim(MicroClaim(
                claim_id="1", proposition="RAPTOR uses recursive clustering",
                quote="RAPTOR recursively clusters and summarizes", timestamp="00:04:10",
                claim_type="FACT", internal_confidence="peer-reviewed", verdict="CONFIRMED",
                external_sources=["https://arxiv.org/abs/2401.18059"],
            ))
            md = engine.render_wiki_markdown("Test Session")
            self.assertIn("[[Claim-1]]", md)
            self.assertIn("[CONFIRMED]", md)
            engine.write(str(tmp_path), "test_session", "Test Session")
            self.assertTrue((tmp_path / "test_session.md").exists())
            self.assertTrue((tmp_path / "test_session.json").exists())


if __name__ == "__main__":
    unittest.main()
