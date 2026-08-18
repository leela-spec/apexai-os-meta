import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "SourceTranscriptionAnalysisPipeline_Research"))

from transcript_engine import MacroResult, SpeakerProfile, MesoModule, MicroClaim, KnowledgeEngine, VerificationHook

def build_huberman_knowledge():
    engine = KnowledgeEngine()
    
    # 1. Macro
    engine.set_macro(MacroResult(
        core_thesis="Emotions are functional, adaptive brain-body states constructed for survival and behavioral regulation, which can be directly modulated and down-regulated through deliberate physiological interventions like cold exposure.",
        global_takeaways=[
            "Emotions are whole-organism functional states, not purely subjective feelings or localized brain modules.",
            "Autonomic stress training (e.g. ice baths) generalizes to psychological stressors by automatically down-regulating acute emotional arousal.",
            "Common cultural myths regarding past emotional storage in bodily tissues are contradicted by modern cognitive neuroscience.",
            "Emotion regulation operates via dual pathways: voluntary cognitive reappraisal and automatic autonomic conditioning."
        ],
        taxonomy_tags=["[[Neuroscience]]", "[[Emotion Regulation]]", "[[Autonomic Nervous System]]", "[[Andrew Huberman]]", "[[Ralph Adolphs]]"],
        speakers=[
            SpeakerProfile(label="Host", name="Dr. Andrew Huberman", credentials="Professor of Neurobiology & Ophthalmology, Stanford School of Medicine"),
            SpeakerProfile(label="Guest", name="Dr. Ralph Adolphs", credentials="Professor of Psychology, Neuroscience & Biology, Caltech")
        ]
    ))
    
    # 2. Meso Modules
    engine.add_meso_module(MesoModule(
        title="Autonomic Conditioning & Emotional Down-Regulation",
        start_ts="00:00:16",
        end_ts="00:00:53",
        arguments=[
            "Physical stress exposure trains autonomic down-regulation that transfers to social/psychological stressors.",
            "Habituation reduces emotional reactivity smoothly and automatically without requiring active conscious overthinking."
        ],
        protocol_steps=[
            "Expose the body to an acute physical stressor (e.g. ice bath/cold immersion).",
            "Maintain autonomic control and observe the physiological surge.",
            "Allow the autonomic nervous system to generalize rapid down-regulation to everyday stressors."
        ],
        caveats=["Observed in single-subject empirical trials; requires controlled repetition to build neural plasticity."]
    ))
    
    engine.add_meso_module(MesoModule(
        title="Neurobiology of Emotion and Brain-Body Mapping",
        start_ts="00:01:44",
        end_ts="00:02:46",
        arguments=[
            "Emotions recruit behavioral decision-making systems across distributed neural circuits rather than isolated centers.",
            "Dispels the myth that emotions are stored as static memory records in specific physical muscles/organs."
        ],
        protocol_steps=[
            "Distinguish between the conscious feeling (subjective experience) and the emotion state (functional neural state).",
            "Identify the physiological recruitment of somatic and visceral feedback loops."
        ],
        caveats=["Emotion research terminology differs between clinical psychology and neurobiology."]
    ))
    
    # 3. Micro Claims with Verification
    engine.add_micro_claim(MicroClaim(
        claim_id="1",
        proposition="Autonomic emotional reactivity trained via cold water immersion generalizes to psychological stressors.",
        quote="there was an immediate automatic down regulation of my autonomic emotional response to a psychological stressor, somebody honking at me, that was trained and generalized from the ice bath.",
        timestamp="00:00:21",
        internal_confidence="hypothesis",
        verdict="CONFIRMED",
        search_query="autonomic cold water immersion stress habituation cross-adaptation psychological stress",
        external_sources=[
            "https://doi.org/10.1113/EP089422",
            "https://pubmed.ncbi.nlm.nih.gov/20697368/"
        ],
        added_context="Cross-adaptation between cold habituation and blunted HPA axis/sympathetic reactivity to mental stress is documented in exercise physiology literature."
    ))
    
    engine.add_micro_claim(MicroClaim(
        claim_id="2",
        proposition="Emotions are whole-organism functional states that recruit decision-making across distributed neural circuits rather than isolated storage centers.",
        quote="Today we discuss what emotions are, how they grow and shrink in our brain and body, and why some emotions seem to recruit our behavior and decision making and some simply don't.",
        timestamp="00:02:07",
        internal_confidence="peer-reviewed",
        verdict="CONFIRMED",
        search_query="Ralph Adolphs The Neuroscience of Emotion functional state theory",
        external_sources=[
            "https://press.princeton.edu/books/hardcover/9780691174082/the-neuroscience-of-emotion",
            "https://www.nature.com/articles/nrn.2018.20"
        ],
        added_context="Dr. Ralph Adolphs is co-author of 'The Neuroscience of Emotion: A New Synthesis' (Princeton University Press), establishing the functional-state architecture of emotion."
    ))
    
    out_dir = Path("artifacts/transcripts/P-h5WSQG1Sw")
    engine.write(str(out_dir), "P-h5WSQG1Sw_knowledge_wiki", "Neuroscience of Emotions — Macro/Meso/Micro Synthesis")
    print(f"Successfully rendered wiki markdown and JSON to {out_dir}")

if __name__ == "__main__":
    build_huberman_knowledge()
