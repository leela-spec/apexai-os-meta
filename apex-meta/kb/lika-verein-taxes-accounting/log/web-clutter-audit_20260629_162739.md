# Web Clutter Audit

- Generated at: 2026-06-29T16:34:05Z
- Markdown files scanned: 77
- Candidates reported: 69
- Candidate JSONL: `audit/web-clutter-candidates_20260629_162739.jsonl`

## Top candidates

- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/AWV_GoBD-Praxisleitfaden.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:cookie, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, noise_phrase:menu
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/BMF_GoBD-2024.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, heading_noise_warning, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/Buergergesellschaft_Ehrenamt-Auslagen.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, noise_phrase:menu, noise_phrase:newsletter
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/DATEV_SKR42-Kontenrahmen.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/DATEV_Verfahrensdokumentation-GoBD.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:cookie, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/DRV_Minijob-Kurzfristige-Beschaeftigung.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, heading_noise_warning, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, noise_phrase:newsletter
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/FinanzamtNRW_Vereine-Umsatzsteuer.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, repeated_boilerplate_sequence
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/StBK-Hamburg_Mindestumsatzgarantien-Gastronomie.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/VUT_KSK-Abgabepflicht-Elektronische-Musik.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt
- `raw/notes/New_Research_Taxes_Accounting/HTML-MD/Vereinswelt_Auslagenerstattung-Muster.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:newsletter, noise_phrase:search
- `raw/refs/AWV_GoBD-Praxisleitfaden.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:cookie, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, noise_phrase:menu
- `raw/refs/BMF_GoBD-2024.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, heading_noise_warning, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum
- `raw/refs/BZSt_50a-Abzugsteuer.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum
- `raw/refs/Buergergesellschaft_Ehrenamt-Auslagen.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, noise_phrase:menu, noise_phrase:newsletter
- `raw/refs/DATEV_SKR42-Kontenrahmen.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum
- `raw/refs/DATEV_Verfahrensdokumentation-GoBD.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:cookie, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt
- `raw/refs/DRV_Minijob-Kurzfristige-Beschaeftigung.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, heading_noise_warning, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, noise_phrase:newsletter
- `raw/refs/FinanzamtNRW_Vereine-Umsatzsteuer.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:anzeige, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt, repeated_boilerplate_sequence
- `raw/refs/IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md` score=100 recommendation=exclude_from_phase1_until_review signals=very_high_link_density, noise_phrase:cookie, noise_phrase:cookies, noise_phrase:datenschutz, noise_phrase:impressum, noise_phrase:kontakt

## Future script improvement

```yaml
future_script_improvement:
  add command: apex_kb.py web-clutter-audit
  role: detect noisy web captures before semantic ingest
  output: audit/web-clutter-candidates_20260629_162739.jsonl
  non_goal: automatic deletion or semantic cleanup
```
