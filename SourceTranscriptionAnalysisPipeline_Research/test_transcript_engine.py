"""
test_transcript_engine.py
End-to-end unit tests for the deterministic 3-tier engine (KR4 requirement).
Run with: pytest test_transcript_engine.py -v
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import pytest
from transcript_engine import (
    hhmmss_to_seconds, seconds_to_hhmmss, MacroResult, SpeakerProfile,
    MesoModule, MicroClaim, KnowledgeEngine, VerificationHook, VERDICTS
)

def test_timestamp_roundtrip():
    assert hhmmss_to_seconds("[00:12:34]") == 754
    assert seconds_to_hhmmss(754) == "00:12:34"

def test_timestamp_invalid_raises():
    with pytest.raises(ValueError):
        hhmmss_to_seconds("[bad]")

def test_micro_claim_validates_timestamp():
    with pytest.raises(ValueError):
        MicroClaim(claim_id="1", proposition="x", quote="y", timestamp="99:99",
                   internal_confidence="anecdote")

def test_micro_claim_validates_verdict():
    with pytest.raises(ValueError):
        MicroClaim(claim_id="1", proposition="x", quote="y", timestamp="00:01:00",
                   internal_confidence="anecdote", verdict="MAYBE")

def test_macro_markdown_contains_wikilinks():
    macro = MacroResult(
        core_thesis="Deterministic pipelines beat ad-hoc summarization.",
        global_takeaways=["Whisper params matter", "VAD prevents hallucination loops"],
        taxonomy_tags=["[[AI Orchestration]]", "[[Whisper]]"],
        speakers=[SpeakerProfile(label="Speaker 0", name="Host", credentials="ML engineer")],
    )
    md = macro.to_markdown()
    assert "[[AI Orchestration]]" in md
    assert "Core Thesis" in md

def test_meso_module_renders_timestamp_range():
    mod = MesoModule(
        title="Whisper Ingestion Standards",
        start_ts="00:00:00", end_ts="00:08:12",
        arguments=["int8 quantization halves RAM with no WER loss"],
        protocol_steps=["Condition audio to 16kHz mono", "Apply Silero VAD", "Run faster-whisper"],
        caveats=["GPU float16 recommended for beam_size=5"],
    )
    md = mod.to_markdown()
    assert "[00:00:00 - 00:08:12]" in md
    assert "1. Condition audio to 16kHz mono" in md

def test_micro_claim_default_verdict_is_unverified():
    c = MicroClaim(claim_id="1", proposition="int8 quantization causes zero WER loss",
                   quote="int8 has zero word error rate loss", timestamp="00:02:15",
                   internal_confidence="hypothesis")
    assert c.verdict == "UNVERIFIED"
    assert c.verdict in VERDICTS

def test_verification_hook_injects_sources_without_network():
    def fake_search(query):
        return [{"url": "https://example.org/paper"}, {"url": "https://example.org/2"}]
    hook = VerificationHook(fake_search)
    c = MicroClaim(claim_id="2", proposition="Silero VAD reduces hallucination loops",
                   quote="VAD eliminates silence hallucination", timestamp="00:03:40",
                   internal_confidence="peer-reviewed")
    verified = hook.verify(c)
    assert verified.external_sources == ["https://example.org/paper", "https://example.org/2"]

def test_engine_end_to_end_renders_full_wiki_markdown(tmp_path):
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
        internal_confidence="peer-reviewed", verdict="CONFIRMED",
        external_sources=["https://arxiv.org/abs/2401.18059"],
    ))
    md = engine.render_wiki_markdown("Test Session")
    assert "[[Claim-1]]" in md
    assert "[CONFIRMED]" in md
    engine.write(str(tmp_path), "test_session", "Test Session")
    assert (tmp_path / "test_session.md").exists()
    assert (tmp_path / "test_session.json").exists()

def test_engine_json_serializable_roundtrip():
    import json
    engine = KnowledgeEngine()
    engine.set_macro(MacroResult("thesis", ["t1"], ["[[Tag]]"], [SpeakerProfile("Speaker 0")]))
    data = json.loads(engine.to_json())
    assert data["macro"]["core_thesis"] == "thesis"
