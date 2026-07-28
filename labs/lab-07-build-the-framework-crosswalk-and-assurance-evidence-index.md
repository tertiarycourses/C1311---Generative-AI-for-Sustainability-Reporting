# Lab 7 — Build the Framework Crosswalk and Assurance Evidence Index

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 4:** AI for Compliance, Frameworks and Continuous Reporting  
**Maps to:** LO4: map approved content to current framework sources and maintain an assurance-ready audit trail  
**Duration:** 55 minutes  
**Tools:** Spreadsheet · browser · approved AI assistant · Lab 2 register · Lab 4 workpaper · Lab 6 claim ledger

---

## Goal

Connect every approved disclosure and metric to requirements, evidence, controls, owners and review status without overstating applicability.

## What You Will Do

You will extend the framework register into a requirement crosswalk, map the Lab 6 disclosure and Lab 4 metrics, and build an evidence index from source through calculation, claim and approval. You will also record current Singapore applicability questions for responsible-owner confirmation.

## What You Will Build

A framework-crosswalk.csv, assurance-evidence-index.csv and control-matrix.csv with requirement IDs, report locations, evidence lineage, owners, statuses, exceptions and reviewer sign-off.

## Prerequisites

- Completed Labs 2, 4 and 6 and retained their official URLs, approved calculations and claim statuses.
- Open labs/assets/framework-crosswalk-starter.csv, assurance-evidence-index-starter.csv and control-matrix-starter.csv.
- Treat HarbourLight's entity and listing status as a synthetic scenario; record jurisdiction decisions as PENDING OWNER CONFIRMATION.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Time box: 8 minutes. Copy framework-crosswalk-starter.csv to framework-crosswalk.csv. Reuse the checked dates and status notes from Lab 2; reopen any source marked PENDING CHECK or changed since that check. The starter already contains REFERENCE source rows and seven ACTIVE mapping rows for reporting basis, energy and emissions methods, Scope 1 and Scope 2 results, material-topic process, governance and limitations.

```text
Required source families: GRI 1/2/3 and relevant Topic Standard · IFRS S1 · IFRS S2 · SASB industry guidance · TCFD bridge · SGX Rule 711B · Singapore requirements timeline
```

### 2. Time box: 12 minutes. For each ACTIVE mapping row, complete Audience,Lens,Applicability_Status,Applicability_Owner,Report_Location,Claim_IDs,Metric_IDs,Evidence_Status,Gap,Action_Owner and Due_Date. Use COMPLETE, PARTIAL, MISSING, NOT APPLICABLE or PENDING INTERPRETATION for evidence; use PENDING OWNER CONFIRMATION where entity scope or jurisdiction has not been established. Keep REFERENCE rows as source controls rather than duplicating a report-location mapping on them.

```text
Mapping test: exact requirement + rationale + current source + report location + evidence + owner + status
```

### 3. Time box: 8 minutes. Give the seven ACTIVE crosswalk rows and official-source summaries to the approved AI assistant. Ask it to identify keyword-only mappings, lens conflicts, obsolete TCFD treatment, missing owners and any unsupported statement of alignment. Save the raw critique as review/P-007-crosswalk-critique.md and add P-007 to prompt-log.csv. Verify every proposed change against the official URL before editing; record the reviewer decision and reason in P-007 and retain accepted or rejected changes in the reviewed crosswalk fields.

```text
Return: Crosswalk_ID | Issue | Why_it_matters | Official_source_to_check | Proposed_status
Do not declare applicability or conformity.
```

### 4. Time box: 12 minutes. Complete the five supplied rows in assurance-evidence-index-starter.csv and save it as assurance-evidence-index.csv with Evidence_ID,Evidence_Type,Original_Source_ID,Transformation_ID,Calculation_ID,Claim_ID,Crosswalk_ID,File_Location,Version,Prepared_By,Reviewed_By,Approval_Status and Exception_ID. Create at least one complete chain for FY2025 Scope 1, Scope 2, total, intensity and the factor limitation.

```text
Lineage pattern: source → structured row → calculation → claim → disclosure location → framework mapping → approval
```

### 5. Time box: 10 minutes, leaving 5 minutes for the Test It check. Complete the seven supplied rows in control-matrix-starter.csv and save it as control-matrix.csv with Control_ID,Risk,Control_Activity,Frequency,Preparer,Reviewer,Evidence,Exception_Route and Status. Add controls for source completeness, factor approval, formula accuracy, claim verification, framework change, access/version control and publication approval. Sample two metric chains and one narrative chain; record PASS, FAIL or OPEN and resolve or assign every exception.

```text
Minimum controls: CTL-01 source · CTL-02 factor · CTL-03 calculation · CTL-04 claim · CTL-05 framework change · CTL-06 version/access · CTL-07 publication
```

## Test It

Every ACTIVE crosswalk row must contain an official source, requirement or guidance ID, lens, applicability status, report location, evidence status and owner; every REFERENCE row must retain its current official URL and checked or PENDING CHECK status. No synthetic jurisdiction decision may be stated as confirmed. The evidence index must contain complete reproducible chains for the four metrics and factor limitation. CTL-01–CTL-07 must have preparer, reviewer, evidence and status, with no unowned FAIL or OPEN item. prompt-log.csv must contain completed P-007 review fields.

## Checkpoint and Rejoin Point

Keep the crosswalk, evidence index and control matrix. Rejoin by filtering to the current version and using OPEN or PENDING rows as explicit inputs to the recurring workflow in Lab 8.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A crosswalk row maps only by similar wording. | Return to the exact requirement, materiality lens and evidence definition; downgrade to PARTIAL or remove the mapping. |
| The evidence chain skips from source to final claim. | Add the structured-row and calculation or transformation IDs that explain how the evidence changed. |
| A Singapore rule is marked applicable without entity confirmation. | Set PENDING OWNER CONFIRMATION and name the legal, governance or reporting owner who must decide. |

## Challenge

Add a Change_Trigger and Last_Reviewed field to each framework row. Simulate one changed requirement and show which calculations, claims, controls and approvals must be reopened.

## Reflection

Which link in your evidence chain would be hardest for an independent reviewer to reconstruct if it were missing, and why?

---

[← Lab 6](lab-06-draft-and-validate-an-evidence-grounded-disclosure.md) · [Lab 8 →](lab-08-design-the-recurring-reporting-workflow-and-final-pack.md)
