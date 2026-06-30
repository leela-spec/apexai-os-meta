---
okf_version: "0.1"
document_type: "lika_event_apex_pipeline_report"
project: "lika-verein-taxes-accounting"
event_case_source: "Location - Fundraiser Hamburg .xlsx"
source_policy: "project/repo sources only; no web research"
tax_boundary: "validation model only; no final tax/legal advice"
---

# 1. Executive Summary

```yaml
summary:
  event_case_source_used: "Location - Fundraiser Hamburg .xlsx inspected; sheets EQUINOX and cOMPARED"
  kb_sufficiency_0_100: 74
  apex_pipeline_sufficiency_0_100: 70
  strongest_domains: ["GoBD archive", "invoice/ticket receipt fields", "KSK", "ticketing exports"]
  weakest_domains: ["venue settlement/minimum bar revenue", "7% vs 19% ticket VAT", "support/donation wording", "foreign services operationalization"]
  immediate_operator_decisions:
    - "VAT default for tickets"
    - "support tier vs separated voluntary contribution"
    - "written venue minimum bar revenue definition"
    - "ticketing provider/export standard"
    - "named owners for finance, ticketing, archive, booking/KSK, venue, crew"
  files_written_or_proposed:
    - "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/lika_event_apex_pipeline_report.okf.md"
    - "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/lika_event_apex_plan_packet.yaml"
    - "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/handoff-preview/*.md"
```

# 2. Source Basis

| Domain | Source files used | Authority level | Transfer risk | Notes |
|---|---|---:|---|---|
| event description | `Location - Fundraiser Hamburg .xlsx` | project primary | low | Concrete event case. |
| ticketing and pricing | `pretix_Fiscal-Requirements-Germany.md`, `pretix_Taxes-Guide.md`, provider export docs | provider/practice | medium | Operational, not tax authority. |
| invoice / ticket receipt | IHK/BMJ `§33 UStDV`, `§14 UStG`, IHK Pflichtangaben | official/IHK | low | Strong for fields; provider role still check. |
| E-Rechnung | BMF FAQ, IHK E-Rechnung | official/IHK | low | Mainly B2B intake/outgoing invoices. |
| GoBD archive | BMF GoBD, DATEV, AWV | official/professional | low | Strongest workflow area. |
| payout reconciliation | pretix/Eventbrite/ticket.io export docs | provider | medium | Provider-specific. |
| venue settlement | xlsx + venue/contract sources | weak/mixed | high | Evidence gap; validation required. |
| VAT rate | IHK/BFH/BMF UStAE culture sources | official/case law/IHK | high | Decision gate only. |
| KSK | KSK Info 04, DRV K5001 | official | low | Strong onboarding basis. |
| artists / contractors | KSK/DRV + contractor sources | official/mixed | medium | Per-person facts required. |
| foreign services / §50a | BZSt §50a, reverse-charge sources | official/IHK | medium | Gate before payment. |
| crew / minijob / Scheinselbstständigkeit | Minijob-Zentrale, DRV | official | medium | Classification matrix needed. |
| EÜR / association accounting | Finanzverwaltung NRW, DATEV SKR42, Vereins sources | official/professional | medium/high | Mark Gemeinnützigkeit contamination. |

# 3. Event Assumption Extraction

```yaml
event_assumptions:
  event_name: "Equinox / Fundraiser Hamburg"
  location: "Equinox venue; exact street/address unknown"
  capacity: "official 300-350; recommended 310-320"
  date_or_timing: "Friday, November 20; Friday evening to Saturday morning; end 05:00-05:30; vacate by Saturday noon"
  ticketing_assumptions: "provider, prices, door sales, support tier unknown"
  pricing_assumptions: "minimum bar revenue EUR 7,500; no advance payment; settlement based on revenue generated during event"
  venue_deal: "venue manages bar, admission, security, cleaning; house rights stay with venue"
  bar_or_minimum_revenue: "EUR 7,500; exact definition/calculation unknown; validation_required"
  staffing: "organizer: greeting, DJs, performers, event crew, program; venue: bar/admission/security/cleaning"
  artists: "DJs/performers required or likely; names, residence, status unknown"
  payment_flows: "tickets unknown; bar via venue; artist/crew/expenses unknown"
  open_unknowns: ["ticket provider", "ticket prices", "VAT rate", "support wording", "written venue terms", "artist/crew status", "catering/welcome drink treatment"]
  source_file: "Location - Fundraiser Hamburg .xlsx"
```

# 4. Macro Operating Model

```yaml
macro_operating_model:
  governance_and_responsibility: {purpose: "assign owners and approval gates", owner_role: "event lead + board finance", core_decisions: ["RACI", "signing authority", "archive owner"], source_basis: ["satzung", "stammdaten", "source index"], risks: ["unapproved commitments"], outputs_artifacts: ["RACI", "decision log"]}
  ticketing_and_pricing: {purpose: "configure sellable products safely", owner_role: "ticketing + finance", core_decisions: ["provider", "cap", "tiers", "VAT", "support wording"], source_basis: ["provider docs", "invoice sources", "VAT cluster"], risks: ["wrong VAT", "misleading donation wording"], outputs_artifacts: ["product matrix", "test order"]}
  tax_classification: {purpose: "hold validation gates", owner_role: "finance + tax advisor", core_decisions: ["19% vs 7%", "support treatment", "venue settlement"], source_basis: ["VAT/venue/foreign clusters"], risks: ["underpaid VAT", "missed §50a/reverse charge"], outputs_artifacts: ["tax memo"]}
  invoicing_and_receipts: {purpose: "valid ticket and invoice evidence", owner_role: "finance", core_decisions: ["<=250 small invoice", ">250/B2B full invoice", "E-Rechnung intake"], source_basis: ["IHK/BMJ/BMF"], risks: ["bad Vorsteuer evidence"], outputs_artifacts: ["receipt checklist"]}
  payment_and_payout_reconciliation: {purpose: "tie orders, refunds, fees, tax, bank", owner_role: "finance + ticketing", core_decisions: ["export cadence", "bank match"], source_basis: ["provider exports", "GoBD"], risks: ["incomplete exports"], outputs_artifacts: ["reconciliation sheet"]}
  venue_and_settlement: {purpose: "document minimum bar revenue", owner_role: "event lead + finance", core_decisions: ["definition", "shortfall invoice", "included services"], source_basis: ["xlsx", "venue sources"], risks: ["misclassified settlement"], outputs_artifacts: ["venue closeout packet"]}
  artists_and_ksk: {purpose: "classify all artistic services", owner_role: "booking + finance", core_decisions: ["KSK relevance", "foreign check", "invoice fields"], source_basis: ["KSK/DRV/BZSt"], risks: ["unreported KSK/§50a"], outputs_artifacts: ["artist register"]}
  crew_and_contractors: {purpose: "avoid worker misclassification", owner_role: "ops + finance", core_decisions: ["volunteer vs paid", "expense vs fee", "employment route"], source_basis: ["Minijob/DRV"], risks: ["Scheinselbstständigkeit"], outputs_artifacts: ["crew matrix"]}
  foreign_services: {purpose: "pre-payment country/service gate", owner_role: "booking + finance", core_decisions: ["§50a", "reverse charge"], source_basis: ["BZSt/reverse-charge"], risks: ["withholding missed"], outputs_artifacts: ["foreign checklist"]}
  document_archive_and_gobd: {purpose: "preserve immutable evidence", owner_role: "archive + finance", core_decisions: ["folder scheme", "export timestamps", "read-only policy"], source_basis: ["BMF/DATEV/AWV"], risks: ["missing exports"], outputs_artifacts: ["archive log"]}
  event_closeout: {purpose: "accounting-ready final packet", owner_role: "event lead + finance", core_decisions: ["closeout deadline", "exceptions"], source_basis: ["all clusters"], risks: ["unreconciled docs"], outputs_artifacts: ["closeout packet"]}
  reporting_and_next_event_learning: {purpose: "capture reusable SOP deltas", owner_role: "APEX/session owner", core_decisions: ["standard vs risk gate"], source_basis: ["apex-session", "source index"], risks: ["unsafe assumptions become templates"], outputs_artifacts: ["findings/progress/next-session"]}
```

# 5. Meso Workflow Layer

```yaml
meso_workflows:
  governance_and_responsibility: {objective: "event control layer", trigger: "venue selected", inputs: ["venue terms", "budget"], process_steps: ["name owners", "approval thresholds", "decision log", "archive opened"], decisions: ["who signs/pays/reconciles"], required_documents: ["RACI", "decision log"], accounting_or_tax_touchpoints: ["audit trail"], handoff_to: ["ticketing", "venue", "archive"], done_when: "every money domain has owner", unresolved_risks: ["owners missing"], kb_sources_to_use: ["README", "source index"]}
  ticketing_and_pricing: {objective: "documented ticket shop", trigger: "provider chosen", inputs: ["cap", "prices", "VAT gate"], process_steps: ["product matrix", "tax class", "test order", "export sample"], decisions: ["VAT", "support model"], required_documents: ["product matrix", "sample receipt"], accounting_or_tax_touchpoints: ["USt", "gross/net", "Ist timing"], handoff_to: ["reconciliation", "archive"], done_when: "test order/export pass", unresolved_risks: ["provider unknown"], kb_sources_to_use: ["pretix", "invoice", "VAT"]}
  tax_classification: {objective: "explicit validation gates", trigger: "before sales/contracts", inputs: ["program", "ticket matrix", "venue agreement", "artist list"], process_steps: ["advisor questions", "defaults", "risk flags"], decisions: ["VAT/support/venue/foreign"], required_documents: ["tax memo"], accounting_or_tax_touchpoints: ["USt", "§50a", "§13b", "KSK"], handoff_to: ["ticketing", "venue", "artists"], done_when: "each risk has default or validation", unresolved_risks: ["multiple"], kb_sources_to_use: ["VAT", "venue", "foreign"]}
  invoicing_and_receipts: {objective: "valid docs", trigger: "ticket/invoice setup", inputs: ["sample ticket", "invoices"], process_steps: ["field check", "<=250/>250 split", "archive"], decisions: ["receipt wording", "B2B full invoice"], required_documents: ["checklists"], accounting_or_tax_touchpoints: ["Vorsteuer", "E-Rechnung"], handoff_to: ["archive"], done_when: "templates pass", unresolved_risks: ["provider role"], kb_sources_to_use: ["IHK/BMJ/BMF"]}
  payment_and_payout_reconciliation: {objective: "match exports to bank", trigger: "payout/closeout", inputs: ["orders", "refunds", "payout", "bank"], process_steps: ["freeze exports", "split fees/refunds/tax", "match bank", "exceptions"], decisions: ["export cadence"], required_documents: ["CSV", "statement", "reconciliation"], accounting_or_tax_touchpoints: ["USt", "fees", "Ist"], handoff_to: ["EÜR", "closeout"], done_when: "differences explained", unresolved_risks: ["provider unknown"], kb_sources_to_use: ["provider exports", "GoBD"]}
  venue_and_settlement: {objective: "settlement-ready terms", trigger: "contract and closeout", inputs: ["written terms", "bar report", "invoice"], process_steps: ["terms", "included services", "shortfall logic", "invoice VAT"], decisions: ["bar ownership", "shortfall treatment"], required_documents: ["agreement", "settlement", "Z-Bon", "invoice"], accounting_or_tax_touchpoints: ["Vorsteuer", "location cost"], handoff_to: ["reconciliation"], done_when: "written settlement exists", unresolved_risks: ["weak evidence"], kb_sources_to_use: ["xlsx", "venue cluster"]}
  artists_and_ksk: {objective: "classify artistic payments", trigger: "booking", inputs: ["artist data", "fee", "contract"], process_steps: ["classify", "KSK", "foreign", "archive"], decisions: ["KSK/§50a"], required_documents: ["onboarding", "invoice", "register"], accounting_or_tax_touchpoints: ["KSK", "§50a", "expense"], handoff_to: ["payment"], done_when: "every artist classified", unresolved_risks: ["lineup unknown"], kb_sources_to_use: ["KSK", "DRV", "BZSt"]}
  crew_and_contractors: {objective: "classify helpers", trigger: "crew list", inputs: ["role", "payment", "working conditions"], process_steps: ["volunteer/expense/fee/employment", "docs", "approval"], decisions: ["minijob/contractor"], required_documents: ["crew matrix"], accounting_or_tax_touchpoints: ["payroll", "Scheinselbstständigkeit"], handoff_to: ["payment"], done_when: "no undocumented payment", unresolved_risks: ["model unknown"], kb_sources_to_use: ["Minijob", "DRV"]}
  foreign_services: {objective: "pre-payment tax gate", trigger: "non-German service", inputs: ["country", "contract", "invoice"], process_steps: ["classify", "§50a", "reverse charge", "advisor"], decisions: ["withholding/reverse charge"], required_documents: ["checklist"], accounting_or_tax_touchpoints: ["§50a", "§13b"], handoff_to: ["payment"], done_when: "gate documented", unresolved_risks: ["unknown foreign suppliers"], kb_sources_to_use: ["BZSt", "reverse-charge"]}
  document_archive_and_gobd: {objective: "immutable event evidence", trigger: "event opened", inputs: ["contracts", "exports", "invoices", "bank"], process_steps: ["folder tree", "source originals", "export log", "read-only"], decisions: ["owner/tool"], required_documents: ["archive index"], accounting_or_tax_touchpoints: ["GoBD"], handoff_to: ["closeout"], done_when: "all source docs archived", unresolved_risks: ["tooling unknown"], kb_sources_to_use: ["BMF", "DATEV", "AWV"]}
  event_closeout: {objective: "accounting-ready packet", trigger: "all final statements", inputs: ["exports", "bank", "venue", "artist/crew docs"], process_steps: ["reconcile", "close venue", "registers", "P&L", "risk flags"], decisions: ["exceptions"], required_documents: ["closeout packet"], accounting_or_tax_touchpoints: ["EÜR", "USt", "KSK"], handoff_to: ["tax advisor"], done_when: "bookkeeping can proceed", unresolved_risks: ["depends on docs"], kb_sources_to_use: ["all"]}
  reporting_and_next_event_learning: {objective: "reusable learning", trigger: "closeout complete", inputs: ["closeout", "exceptions"], process_steps: ["findings", "SOP deltas", "next-session"], decisions: ["standard vs risk"], required_documents: ["findings/progress/next-session"], accounting_or_tax_touchpoints: ["no unresolved tax as rule"], handoff_to: ["orchestrator"], done_when: "next event has improved checklist", unresolved_risks: ["validation pass"], kb_sources_to_use: ["apex-session"]}
```

# 6. Micro SOP Layer

```yaml
micro_sops:
  ticket_product_setup: {purpose: "configure products", owner: "ticketing", trigger: "before sales", steps: ["cap", "matrix", "VAT gate", "test order", "archive"], required_inputs: ["capacity", "prices", "VAT"], required_outputs: ["product matrix", "test PDF"], source_basis: ["provider", "invoice"], validation_required: ["VAT", "support"], done_when: "test order/export passes"}
  ticket_as_invoice_field_check: {purpose: "check receipt fields", owner: "finance", trigger: "template setup", steps: ["name/address", "date", "service", "gross", "VAT", "archive"], required_inputs: ["sample"], required_outputs: ["field checklist"], source_basis: ["§33 UStDV", "§14 UStG"], validation_required: ["provider legal role"], done_when: "pass or exception"}
  support_ticket_or_voluntary_contribution_wording: {purpose: "avoid false donation", owner: "ticketing+finance", trigger: "support planned", steps: ["avoid donation wording", "choose product vs optional", "no donation receipt", "test receipt"], required_inputs: ["pricing"], required_outputs: ["approved wording"], source_basis: ["stammdaten", "gap research"], validation_required: ["tax wording"], done_when: "wording safe"}
  ticket_vat_rate_decision_gate: {purpose: "block unvalidated VAT", owner: "finance", trigger: "before tax rule", steps: ["describe event", "program", "19% default", "7% evidence only if validated", "memo"], required_inputs: ["program"], required_outputs: ["VAT memo"], source_basis: ["VAT cluster"], validation_required: ["7 vs 19"], done_when: "approved or conservative VAT used"}
  payout_reconciliation: {purpose: "tie payouts", owner: "finance", trigger: "payout", steps: ["orders", "refunds", "payout", "bank", "split", "exceptions", "archive"], required_inputs: ["exports", "bank"], required_outputs: ["reconciliation"], source_basis: ["provider", "GoBD"], validation_required: ["fields"], done_when: "tie-out complete"}
  refund_or_cancellation: {purpose: "refund audit trail", owner: "ticketing+finance", trigger: "refund", steps: ["record", "process", "export", "archive", "reconcile"], required_inputs: ["order id"], required_outputs: ["refund log"], source_basis: ["order lifecycle"], validation_required: ["credit/correction"], done_when: "status/payment/accounting agree"}
  venue_settlement_closeout: {purpose: "close venue", owner: "event+finance", trigger: "settlement", steps: ["statement", "bar evidence", "included services", "shortfall", "VAT invoice", "archive"], required_inputs: ["agreement", "invoice"], required_outputs: ["venue packet"], source_basis: ["xlsx", "venue cluster"], validation_required: ["shortfall/VAT"], done_when: "accounting-ready"}
  ksk_artist_onboarding: {purpose: "KSK facts", owner: "booking", trigger: "artist booking", steps: ["data", "classify", "fee", "KSK", "invoice", "register"], required_inputs: ["artist", "fee"], required_outputs: ["KSK entry"], source_basis: ["KSK", "DRV"], validation_required: ["edge cases"], done_when: "no unclassified artist payment"}
  foreign_artist_check: {purpose: "§50a/reverse charge", owner: "booking+finance", trigger: "foreign artist/supplier", steps: ["country", "classify", "§50a", "reverse charge", "advisor"], required_inputs: ["country", "invoice"], required_outputs: ["checklist"], source_basis: ["BZSt", "reverse-charge"], validation_required: ["withholding"], done_when: "payment gate documented"}
  contractor_or_crew_status_check: {purpose: "worker classification", owner: "ops", trigger: "crew role", steps: ["role", "payment", "control", "status path", "docs"], required_inputs: ["role", "payment"], required_outputs: ["crew matrix"], source_basis: ["Minijob", "DRV"], validation_required: ["employment path"], done_when: "every worker classified"}
  expense_reimbursement: {purpose: "document expenses", owner: "finance", trigger: "claim", steps: ["receipt", "purpose", "payment proof", "approval", "bank", "archive"], required_inputs: ["receipt"], required_outputs: ["reimbursement packet"], source_basis: ["GoBD", "expense sources"], validation_required: ["no blanket honorarium"], done_when: "receipt/purpose/approval/payment proof"}
  incoming_invoice_check: {purpose: "valid input invoices", owner: "finance", trigger: "invoice received", steps: ["supplier", "recipient", "date/number", "service", "VAT", "foreign/E-Rechnung", "archive"], required_inputs: ["invoice"], required_outputs: ["invoice check"], source_basis: ["IHK", "E-Rechnung"], validation_required: ["foreign/KSK"], done_when: "accepted/queried/rejected"}
  e_invoice_intake: {purpose: "structured B2B invoices", owner: "finance", trigger: "B2B invoice", steps: ["check structured file", "store original", "readable view", "archive"], required_inputs: ["XML/ZUGFeRD/XRechnung"], required_outputs: ["e-invoice entry"], source_basis: ["BMF", "IHK"], validation_required: ["transition rules"], done_when: "structured file archived"}
  gobd_archive_daily_or_event_closeout: {purpose: "freeze evidence", owner: "archive", trigger: "daily/closeout", steps: ["export", "save docs", "timestamp", "no edits", "missing list"], required_inputs: ["exports/docs"], required_outputs: ["archive log"], source_basis: ["BMF/DATEV/AWV"], validation_required: ["tool immutability"], done_when: "complete archive index"}
  event_closeout_packet: {purpose: "accounting packet", owner: "finance+event", trigger: "final docs", steps: ["reconcile", "venue", "KSK", "crew", "P&L", "risks", "archive"], required_inputs: ["all outputs"], required_outputs: ["closeout packet"], source_basis: ["all clusters"], validation_required: ["all high-risk flags"], done_when: "bookkeeping can proceed"}
```

# 7. APEX Plan Packet

See companion file: `apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/lika_event_apex_plan_packet.yaml`.

# 8. APEX Sync Validation

```yaml
apex_sync_validation:
  mode: "conceptual_preview"
  commands_run: []
  commands_not_run_reason: "No local cloned repo with canonical task files and scripts/apex_sync.py available; GitHub file API used for targeted reads/writes only."
  canonical_commands_to_run_when_repo_available:
    - "python scripts/apex_sync.py next --root . --json --dry-run true"
    - "python scripts/apex_sync.py blockers --root . --json --dry-run true"
    - "python scripts/apex_sync.py score --root . --json --dry-run true"
  likely_blockers: ["no canonical task files", "dependencies not script-validated", "owners/due dates missing"]
  dependency_risks: ["103 should wait for 102", "107 should wait for 101/103/104/105"]
  focus_candidates: ["venue settlement", "VAT/support wording", "ticketing setup", "GoBD archive"]
  exact_next_action_candidates: ["request written venue terms", "prepare tax memo", "choose provider/test export"]
  registry_or_drift_notes: ["no registry rebuild", "no status mutation"]
  review_flags: ["conceptual_preview_only", "script_not_run", "no_task_files_mutated"]
```

# 9. APEX Session Handoff Preview

Drafts written under `outputs/execution/handoff-preview/`: `task_plan.md`, `findings.md`, `progress.md`, `next-session.md`. `next-session.md` uses exactly: Current Step, Open Items, Risks, Decisions Made, Next Actions.

# 10. Risk Register

| Risk | Domain | Severity | Why it matters | Source basis | Validation owner | Next action |
|---|---|---|---|---|---|---|
| 7% vs. 19% ticket VAT | VAT | high | Underpayment/repricing | VAT cluster | tax advisor/finance | VAT memo before sales |
| support/donation wording | ticketing | high | misleading for non-charitable e.V. | stammdaten/gap research | finance | approve wording |
| venue minimum bar revenue | venue | high | settlement/VAT unclear | xlsx + weak sources | event/tax advisor | written definition |
| KSK | artists | high | reporting/payment obligations | KSK/DRV | booking/finance | KSK register |
| foreign artists / §50a | foreign | high | withholding before payment | BZSt | finance/advisor | country/residence check |
| reverse charge | foreign | medium/high | wrong VAT accounting | reverse-charge cluster | finance | invoice gate |
| crew status | crew | high | employment/minijob risk | Minijob/DRV | ops/finance | crew matrix |
| Scheinselbstständigkeit | contractors | high | false contractor setup | DRV | finance | status check |
| GoBD archive failure | archive | high | weak evidence | BMF/DATEV/AWV | archive | archive before sales |
| incomplete exports | reconciliation | high | cannot tie bank/tax/refunds | provider docs | ticketing/finance | test export fields |

# 11. Operator Decisions Needed

```yaml
operator_decisions:
  - {id: D01, decision: "Ticket VAT default", recommended_answer: "19% unless 7% is validated", option_a: "19%", option_b: "7% after validation", option_c: "segmented after validation", consequence: "controls pricing/receipts/USt"}
  - {id: D02, decision: "Support payment model", recommended_answer: "support ticket incl. USt unless truly separated optional contribution is validated", option_a: "product tier", option_b: "optional contribution", option_c: "no support amount", consequence: "controls wording/accounting"}
  - {id: D03, decision: "Venue written terms", recommended_answer: "require written confirmation", option_a: "full contract", option_b: "email key terms", option_c: "verbal", consequence: "controls settlement evidence"}
  - {id: D04, decision: "Ticketing provider", recommended_answer: "provider with receipts/tax/refunds/export", option_a: "pretix", option_b: "ticket.io/Eventbrite", option_c: "manual", consequence: "controls reconciliation/GoBD"}
  - {id: D05, decision: "Owner roles", recommended_answer: "assign named domain owners", option_a: "finance lead with deputies", option_b: "distributed owners", option_c: "unassigned", consequence: "controls execution reliability"}
  - {id: D06, decision: "Artist/crew payment policy", recommended_answer: "no payment without classification/evidence", option_a: "strict pre-payment gate", option_b: "post-event cleanup", option_c: "informal", consequence: "controls KSK/employment risk"}
  - {id: D07, decision: "Archive implementation", recommended_answer: "open archive before sales", option_a: "cloud folder + log", option_b: "DMS/bookkeeping tool", option_c: "ad hoc", consequence: "controls auditability"}
```

# 12. Process Weakness Report

| Weakness | Evidence | Impact | Workaround used | Suggested Improvement |
|---|---|---|---|---|
| unclear combined skill boundary | plan/sync/session asked together | overclaim risk | separated outputs | combined executor wrapper |
| missing event ontology | source clusters not lifecycle | inconsistent domains | prompt domain map | add `event-domain-ontology.okf.yaml` |
| missing tax gates | sources list risks, not gates | SOP drift | created gates | add `tax-decision-gates.yaml` |
| missing SOP templates | source-oriented KB | invented SOP shape | used prompt schema | add SOP template/examples |
| weak authority labels in index | ranking separate | manual merge | used ranking + index | merge scores into index |
| token/tool inefficiency | raw corpus large | call waste | targeted reads | per-domain evidence cards |
| repo write ambiguity | branch/commit conventions absent | unwanted writes | derived paths only | add execution README/write gate |
| no local sync execution | GitHub API only | no exact validation | conceptual preview | provide mounted repo/CI action |

# 13. Written Artifact Summary

```yaml
written_artifacts:
  - {path: "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/lika_event_apex_pipeline_report.okf.md", purpose: "main executor report", status: "written_repo", next_consumer: "operator | orchestrator_chat | future_executor"}
  - {path: "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/lika_event_apex_plan_packet.yaml", purpose: "machine-readable plan packet", status: "written_repo", next_consumer: "apex-plan | apex-sync"}
  - {path: "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/handoff-preview/task_plan.md", purpose: "handoff preview", status: "written_repo", next_consumer: "apex-session"}
  - {path: "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/handoff-preview/findings.md", purpose: "handoff preview", status: "written_repo", next_consumer: "apex-session"}
  - {path: "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/handoff-preview/progress.md", purpose: "handoff preview", status: "written_repo", next_consumer: "apex-session"}
  - {path: "apex-meta/kb/lika-verein-taxes-accounting/outputs/execution/handoff-preview/next-session.md", purpose: "handoff preview", status: "written_repo", next_consumer: "apex-session"}
```

# 14. Handoff to Orchestrator Chat

```yaml
orchestrator_handoff:
  executor_result_summary: "Source-grounded Equinox/Fundraiser Hamburg operating model plus APEX plan/sync/session preview created without final tax advice."
  strongest_outputs: ["event assumptions", "macro/meso/micro workflow", "risk register", "APEX boundary-aware packet"]
  weakest_outputs: ["no actual apex-sync run", "no advisor validation", "venue settlement evidence gap", "provider unknown"]
  source_gaps: ["venue minimum bar revenue", "7% vs 19%", "support wording"]
  process_gaps: ["event ontology", "tax gates", "source authority index", "repo write conventions"]
  decisions_needed: ["VAT", "support model", "venue terms", "provider", "owners", "payment policy", "archive"]
  files_written_or_proposed: "outputs/execution/"
```
