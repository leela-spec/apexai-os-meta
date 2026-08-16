---
title: "Apex Plan Packet — Business Invoicing"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
status: operator_review_needed
package: apex-plan
candidate_epic_slug: business-invoicing
target_week: 2026-W34
canonical_mutation_performed: false
---

# Business Invoicing

```yaml
project_capture_record:
  goal: >
    Complete the three currently outstanding invoices for Martial Arts,
    AkiiByte and AI Consulting using the existing MasterOfArts invoice SSOT
    and source/customer evidence, without inventing missing commercial data.
  requested_invoices:
    - Martial Arts
    - AkiiByte
    - AI Consulting
  due_date: null
  source:
    - operator portfolio input 2026-08-16
    - MasterOfArts/Business/Invoices/
    - Business/Invoices/ssot_rechnungserstellung_macro_meso_micro.md
    - Business/Invoices/SSOT – Rechnungsvorlage (DE) – Kleinunternehmer (§19 UStG).md

epic_record:
  slug: business-invoicing
  title: Business Invoicing
  status: open
  priority: medium
  due_date: null

proposed_task_records:
  - id: 1
    title: Create and send Martial Arts invoice
    status: open
    priority: medium
    due_date: null
    depends_on: []
    blocked_by:
      - missing_fields_if_not_present_in_source
    acceptance_criteria:
      - current customer/service/amount/period evidence is read before drafting
      - invoice follows current invoice SSOT numbering/date/tax/layout rules
      - missing values are not invented
      - final PDF is checked before sending
      - sent invoice is archived according to invoice process
    definition_of_done:
      - correct invoice PDF exists is sent and archival record is complete

  - id: 2
    title: Create and send AkiiByte invoice
    status: open
    priority: medium
    due_date: null
    depends_on: []
    blocked_by:
      - missing_month_or_service_period_if_not_confirmed
    acceptance_criteria:
      - existing Akibyte source/customer baseline is reused
      - correct current invoice number and service period are established
      - invoice follows current invoice SSOT
      - final PDF is checked sent and archived
    definition_of_done:
      - correct AkiiByte invoice PDF exists is sent and archival record is complete

  - id: 3
    title: Create and send AI Consulting invoice
    status: open
    priority: medium
    due_date: null
    depends_on: []
    blocked_by:
      - missing_fields_if_not_present_in_source
    acceptance_criteria:
      - customer/service/amount/period evidence is read before drafting
      - invoice follows current invoice SSOT
      - missing values are not invented
      - final PDF is checked sent and archived
    definition_of_done:
      - correct AI Consulting invoice PDF exists is sent and archival record is complete

  - id: 4
    title: Verify invoice ledger and numbering after all three invoices
    status: open
    priority: medium
    due_date: null
    depends_on: [1, 2, 3]
    blocked_by: []
    acceptance_criteria:
      - no invoice number is duplicated
      - sent PDFs and source Markdown are consistently archived
      - current numbering state for the next invoice is explicit
      - any customer-specific source updates are captured in the correct source area
    definition_of_done:
      - invoice archive/numbering state is internally consistent

dependency_plan:
  parallel_tasks: [1, 2, 3]
  final_check: 4
  apex_sync_handoff_requests: [validate_dependencies, compute_next_action]

priority_urgency_focus_rationale:
  priority: medium
  due_date: null
  priority_note: operator supplied no ranking among the three invoices
  provisional_focus: use Apex Sync later; do not invent an order among invoices

review_flags:
  - operator_review_needed
  - exact_invoice_fields_must_come_from_source_or_operator
  - no_deadline

handoff_requests:
  to_apex_session_after_operator_approval:
    - create canonical epic/task records

operator_gate:
  status: operator_review_needed
  recommended_decision: approved_for_handoff
```
