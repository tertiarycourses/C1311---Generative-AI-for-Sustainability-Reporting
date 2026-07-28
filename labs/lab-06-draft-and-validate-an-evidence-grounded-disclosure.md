# Lab 6 — Draft and Validate an Evidence-Grounded Disclosure

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 3:** AI for Drafting and Structuring Reports  
**Maps to:** LO3: draft readable sustainability disclosures and validate every material claim  
**Duration:** 60 minutes  
**Tools:** Text editor · spreadsheet · approved AI assistant · disclosure-starters · prior-year-disclosure.md · Lab 4–5 outputs

---

## Goal

Produce an energy-and-emissions disclosure whose narrative, executive summary and claim ledger reconcile to approved evidence.

## What You Will Do

You will combine the approved reporting basis, emissions workpaper, materiality-gap analysis and a deliberately flawed prior-year disclosure into a controlled FY2025 draft. You will use AI for bounded drafting and critique, then verify every quantitative, causal, framework and target claim.

## What You Will Build

A style-sheet.md, disclosure-draft.md, claim-ledger.csv and executive-summary.md with source-linked claims, consistent units, balanced wording, unresolved limitations and recorded human decisions.

## Prerequisites

- Completed Labs 1–5 with approved metric summary and named gap owners.
- Open labs/assets/prior-year-disclosure.md and labs/assets/disclosure-brief.md.
- Copy labs/assets/style-sheet-starter.md and claim-ledger-starter.csv into the HLF-2025/draft folder.
- Use the FY2025 calculation workpaper as the canonical quantitative source.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Complete style-sheet-starter.md and save it as style-sheet.md. Record the canonical entity name, period, boundary, units, decimal places, names for Scope 1 and Scope 2, approved status terms, date style and words to avoid. Add rules that observed change is not automatically a cause and that a training factor must be disclosed as a limitation.

```text
Canonical terms: HarbourLight Foods Pte Ltd · FY2025 · tCO2e · tCO2e/S$ million
Avoid unless directly supported: achieved · ensured · eliminated · compliant · industry-leading · because of
```

### 2. Create an evidence outline in disclosure-draft.md with Reporting basis, Method, FY2025 results, Year-on-year comparison, Actions and governance, Limitations, and Next data priorities. Under each heading, list only approved source IDs or calculation IDs. Mark unsupported fields MISSING before asking for prose.

```text
Minimum evidence IDs: HLF-BRIEF-01 · CALC-FY2024 · CALC-FY2025 · HLF-FACTOR-TRAINING · MAT-GAP-01
No source ID → no factual sentence.
```

### 3. Give the evidence outline, style sheet and labs/assets/disclosure-brief.md to the approved AI assistant. Ask for a 300–400 word disclosure that keeps [SOURCE_ID] tags after each factual sentence and labels [INTERPRETATION] and [LIMITATION]. Save the raw response as review/P-006-raw-draft.md and add P-006 to prompt-log.csv with the five minimum evidence IDs and raw output filename.

```text
Required sequence: basis → method → absolute result → intensity result → balanced interpretation → actions/governance → limitation → next priority
Do not add targets, causes, external validation or framework claims.
```

### 4. Complete claim-ledger-starter.csv and save it as claim-ledger.csv with Claim_ID,Draft_Sentence,Claim_Type,Source_or_Calculation_ID,Verification_Test,Initial_Status,Reviewer,Resolution,Final_Status. Extract every number, comparison, cause, target, action, framework statement and other material claim from the raw draft and prior-year disclosure. Verify each one against original evidence. Use SUPPORTED, REVISE, REMOVE or UNRESOLVED.

```text
High-risk claim types: QUANTITATIVE · CAUSAL · TARGET · FRAMEWORK · GOVERNANCE · COMPARATIVE
The AI may extract candidate claims; the reviewer assigns final status. Update P-006 in prompt-log.csv with APPROVE/REVISE/STOP, reviewer and reason; retained edits must be traceable in claim-ledger.csv.
```

### 5. Rewrite disclosure-draft.md using only claims with final SUPPORTED status or a documented REVISE resolution. Remove working source tags from the reader-facing paragraphs but retain a source map below the draft. Then ask the assistant to create a 100–130 word executive summary using only the approved draft. Compare every executive-summary sentence with the claim ledger and save the corrected version as executive-summary.md.

```text
Final checks: entity · period · boundary · units · totals · intensity denominator · limitations · no unsupported cause · no new executive-summary claim
```

### 6. Run a final contradiction review across the style sheet, disclosure, executive summary and claim ledger. Record each difference in review/final-consistency-log.csv with Field,Canonical_Value,Conflicting_Value,Location,Resolution and Reviewer. Resolve all quantitative conflicts and assign an owner to any remaining text issue.

```text
Required fields to compare: entity name · reporting period · Scope 1 · Scope 2 · total · intensity · factor limitation
```

## Test It

The final disclosure must be 300–400 words and the executive summary 100–130 words. Both must match the canonical FY2025 Scope 1, Scope 2, total and intensity values from Lab 4. Every retained material claim must have a SUPPORTED or resolved REVISE row in claim-ledger.csv. No UNRESOLVED claim may appear as fact, no unsupported cause or target may remain, and the consistency log must contain no open quantitative conflict. prompt-log.csv must contain completed P-006 review fields and every retained change must be visible in the claim ledger.

## Checkpoint and Rejoin Point

Keep the final disclosure, executive summary, style sheet, claim ledger and consistency log. Rejoin by filtering Final_Status to SUPPORTED and using the source map as the narrative evidence trail for Lab 7.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The draft sounds promotional. | Reapply the style sheet and ask for neutral observed-result wording with limitations and no superlatives. |
| The assistant removes source tags too early. | Restore the evidence outline and retain tags until claim verification and final human editing are complete. |
| The executive summary introduces a new claim. | Delete it or return it to the claim ledger; a summary may only select from approved disclosure content. |

## Challenge

Create two versions for different audiences—management and general stakeholders—using the same approved claim set. Highlight changes in emphasis and explain why the evidence and quantitative content did not change.

## Reflection

Which claim type required the most human judgement, and how did the claim ledger prevent it from disappearing into prose?

---

[← Lab 5](lab-05-run-materiality-gap-and-visual-analysis.md) · [Lab 7 →](lab-07-build-the-framework-crosswalk-and-assurance-evidence-index.md)
