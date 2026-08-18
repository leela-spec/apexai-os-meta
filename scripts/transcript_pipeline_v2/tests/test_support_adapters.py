"""Unit tests for support advisory models."""
import unittest
from scripts.transcript_pipeline_v2.adapters.support_nli import MDeBERTaNLIAdapter
from scripts.transcript_pipeline_v2.adapters.support_hhem import VectaraHHEMAdapter


class TestSupportAdapters(unittest.TestCase):

    def test_mdeberta_en_and_de(self):
        nli = MDeBERTaNLIAdapter()
        
        # Positive EN
        res_pos = nli.predict_entailment("Patient SM has amygdala damage and shows no fear.", "Amygdala damage in Patient SM reduces fear.")
        self.assertEqual(res_pos["label"], "entailment")
        
        # Negative DE
        res_neg = nli.predict_entailment("Die Zinsen stiegen auf 4 Prozent.", "Die Zinsen wurden auf 0 Prozent gesenkt.")
        self.assertIn(res_neg["label"], {"contradiction", "neutral"})

    def test_hhem_english_restriction(self):
        hhem = VectaraHHEMAdapter()
        
        # German should be blocked/unsupported
        res_de = hhem.score_consistency("Prämisse auf Deutsch", "Hypothese auf Deutsch", language="de")
        self.assertEqual(res_de["status"], "UNSUPPORTED_LANGUAGE")
        
        # English should be scored
        res_en = hhem.score_consistency("Adolphs researches emotions at Caltech.", "Ralph Adolphs is at Caltech.", language="en")
        self.assertEqual(res_en["status"], "SCORED")
        self.assertTrue(res_en["is_consistent"])


if __name__ == "__main__":
    unittest.main()
