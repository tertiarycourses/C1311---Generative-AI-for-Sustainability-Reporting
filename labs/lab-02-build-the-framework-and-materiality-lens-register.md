# Lab 2 — Build the Framework and Materiality-Lens Register

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Generative AI for Sustainability Reporting  
**Maps to:** LO1: distinguish GRI, SASB, TCFD and ISSB purposes and record current applicability  
**Duration:** 45 minutes  
**Tools:** Browser · spreadsheet · approved AI assistant · framework-starter-register.csv

---

## Goal

Create a source-backed register that keeps framework purpose, audience, materiality lens and applicability distinct.

## What You Will Do

You will inspect the supplied official-source links, complete a framework register for GRI, ISSB, SASB and TCFD, and add Singapore applicability checks. An AI assistant may compare the supplied summaries, but you will verify every retained statement against the official page.

## What You Will Build

A framework-and-applicability-register.csv plus materiality-lenses.md showing purpose, audience, lens, requirement source, effective-date check, applicability owner and unresolved questions.

## Prerequisites

- Completed Lab 1 reporting basis and AI-use charter.
- Open labs/assets/framework-starter-register.csv and source-pack-index.md.
- Use the current official links in the starter register; do not rely on the model's memory of standards.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Time box: 12 minutes. Copy framework-starter-register.csv to framework-and-applicability-register.csv. The nine source rows already contain a short starter classification. In three pairs, assign three rows per pair, open each Official_URL, record the actual access date in Checked_Date, and verify or revise Current_Status, Audience, Materiality_Lens and Purpose_Summary. Working alone, verify one GRI row, one ISSB/SASB row, the TCFD row and one Singapore row; mark the other rows PENDING CHECK with an owner. For TCFD, record that the task force completed its work and that its recommendations are incorporated into IFRS S2.

```text
Required rows: GRI Universal Standards · GRI 3 · GRI Topic Standards · IFRS S1 · IFRS S2 · SASB Standards · TCFD bridge · SGX Rule 711B · Singapore requirements timeline
```

### 2. Time box: 6 minutes. Create materiality-lenses.md with a two-column comparison. Under Impact lens, record significant impacts on the economy, environment and people. Under Investor lens, record sustainability-related risks and opportunities that could affect the entity's prospects. Add a third section explaining that one evidence item may inform both lenses but needs a separate conclusion and rationale.

```text
Impact lens → evidence → significance judgement → GRI material topic
Investor lens → risk/opportunity evidence → effects on prospects → ISSB material information
```

### 3. Time box: 8 minutes. Add five HarbourLight Reporting_Need rows using the supplied register columns: energy and emissions, packaging waste, worker safety, climate transition risk, and governance of sustainability information. For each, enter Candidate_Framework, Candidate_Requirement, Lens, Rationale, Applicability_Owner and Status. Use PENDING where the current evidence does not support a conclusion.

```text
Allowed Status values: CURRENT · PENDING · NOT APPLICABLE · NEEDS INTERPRETATION
Never use a framework acronym alone as the rationale.
```

### 4. Time box: 10 minutes. Paste only the completed comparison fields—not the URLs alone—into the approved AI assistant. Ask it to find lens conflicts, missing requirement IDs, obsolete treatment of TCFD and unsupported applicability claims. Save the raw critique as review/P-002-framework-critique.md. The supplied register already contains Review_Result and Reviewer_Reason; complete both fields for every accepted or rejected suggestion. Add P-002 to prompt-log.csv with source IDs, output filename, reviewer, decision and decision reason.

```text
Return: Row_ID | Possible_issue | Official_source_to_check | Proposed_fix
Do not declare compliance, conformity or legal applicability.
```

### 5. Time box: 5 minutes, leaving 4 minutes for the Test It check. Write a five-sentence framework-selection note below the materiality comparison. State which lenses HarbourLight will explore, what remains hypothetical in this course, why official requirements control, and which named owner must confirm jurisdiction and reporting basis before publication.

```text
Decision pattern: audience + lens + requirement + applicability owner + evidence status
```

## Test It

The register must contain all nine required framework or jurisdiction rows, official URL, and either an actual checked date or PENDING CHECK with a named owner. Each row must have audience, lens, current-status note and owner. It must contain five HarbourLight reporting-need rows and no unsupported applicability claim marked CURRENT. materiality-lenses.md must keep the two lenses separate, explain shared evidence correctly and identify the owner of final applicability decisions. prompt-log.csv must contain P-002 and the register must record a reviewer result and reason for every AI-proposed change.

## Checkpoint and Rejoin Point

Use framework-and-applicability-register.csv as the controlled requirements source in Labs 5 and 7. Rejoin by filtering Status to CURRENT or PENDING and retaining every official URL, P-002 record and reviewer reason.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A framework row has no materiality lens. | Return to its official purpose and audience; record impact, investor, jurisdiction-specific or guidance bridge. |
| The assistant describes TCFD as a new standalone standard. | Replace the wording from the current IFRS Foundation TCFD page and retain the official link. |
| The register says a rule applies to HarbourLight. | Change the status to PENDING until the entity scope, listing status and responsible owner confirm applicability. |

## Challenge

Add Effective_From and Last_Changed columns. Define a quarterly review trigger and show how a changed official source would create a controlled follow-up rather than silently altering the report.

## Reflection

Which pair of frameworks is most easily confused in an AI-generated answer, and what fields in your register prevent that confusion?

---

[← Lab 1](lab-01-set-the-reporting-boundary-and-ai-control-contract.md) · [Lab 3 →](lab-03-create-the-esg-evidence-register-and-data-dictionary.md)
