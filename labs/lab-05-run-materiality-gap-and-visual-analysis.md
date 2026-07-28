# Lab 5 — Run Materiality, Gap and Visual Analysis

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** AI for ESG Data Collection and Analysis  
**Maps to:** LO2: perform transparent materiality and gap analysis and communicate results with an honest visual  
**Duration:** 50 minutes  
**Tools:** Spreadsheet · approved AI assistant · stakeholder-impact-notes.md · framework-and-applicability-register.csv

---

## Goal

Prioritise five candidate topics under separate lenses, show framework evidence gaps and create one decision-useful chart.

## What You Will Do

You will use synthetic stakeholder and business evidence to score five topics under separate impact and investor lenses, map each topic to the framework register and classify evidence gaps. You will then create a chart and a short summary that avoids causal overreach.

## What You Will Build

A materiality-gap-analysis.xlsx or CSV set with scoring anchors, topic evidence, two separate lens scores, framework-gap status, a labelled chart, reviewer decisions and a follow-up plan.

## Prerequisites

- Completed Labs 2–4 and retained the framework register, structured dataset and approved metric summary.
- Open labs/assets/stakeholder-impact-notes.md.
- Do not ask the AI assistant to invent stakeholder views, impacts, risks or requirement status.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Create scoring-anchors.md before scoring. Define 0–4 anchors for Impact_Significance and Impact_Likelihood, plus 0–4 anchors for Investor_Effect and Investor_Likelihood. Define Evidence_Strength as 0 none, 1 one indirect note, 2 one direct source, 3 two corroborating sources. Do not combine the lenses.

```text
Impact lens result = significance + likelihood (0–8)
Investor lens result = effect on prospects + likelihood (0–8)
Evidence strength is a visible confidence input, not extra materiality points.
```

### 2. Create materiality-gap-analysis.csv with rows Energy and emissions, Packaging waste, Worker safety, Climate transition risk, and Sustainability-information governance. For each row cite Source_IDs from stakeholder-impact-notes.md and the prior labs, classify each statement as OBSERVED, INTERPRETATION or UNKNOWN, then enter proposed component scores with a one-sentence evidence rationale.

```text
Required fields: Analysis_ID | Topic | Proposed_Impact_Significance | Proposed_Impact_Likelihood | Proposed_Investor_Effect | Proposed_Investor_Likelihood | Final_Impact_Significance | Final_Impact_Likelihood | Final_Impact_Total | Final_Investor_Effect | Final_Investor_Likelihood | Final_Investor_Total | Adjustment_Reason | Evidence_Strength | Source_IDs | Rationale | Reviewer
Use Analysis_ID=MAT-GAP-01 for the controlled five-topic analysis.
```

### 3. Give only the five evidence summaries and written anchors to the approved AI assistant. Ask for proposed scores, missing evidence and possible lens conflicts. Save the raw response as review/P-005-score-proposals.csv and add P-005 to prompt-log.csv. Enter AI proposals in Proposed_* columns, then make your own Final_* decisions. Calculate totals only from the Final_* component scores. Record Adjustment_Reason whenever the final score differs, and update P-005 with reviewer, decision and reason.

```text
AI role: organise and challenge the supplied evidence.
Human role: decide scores, thresholds and next action.
```

### 4. Join each topic to the framework register and add Candidate_Requirement, Available_Evidence, Gap_Status,Gap_Description, Owner and Due_Date. Use COMPLETE, PARTIAL, MISSING, NOT APPLICABLE or PENDING INTERPRETATION. A high materiality score does not turn a partial evidence set into a complete disclosure.

```text
Gap rule: status describes evidence against a named requirement—not the importance of the topic.
```

### 5. Create a scatter chart with Final_Investor_Total on the x-axis, Final_Impact_Total on the y-axis and Topic as the point label, or a grouped bar chart with both lens totals by Topic. Show the 0–8 scale, use a neutral title, include a source note and write three sentences: observation, interpretation and required follow-up.

```text
Title: HarbourLight Candidate Topic Scores by Reporting Lens
Source note: Synthetic HLF evidence; human-scored using documented 0–4 anchors; not an organisational materiality conclusion.
```

## Test It

MAT-GAP-01 must contain all five topics with Proposed_* and Final_* component scores, formulas based on Final_* scores, source IDs, evidence strength, final reviewer and any adjustment reason. Impact and investor totals must remain separate and range from 0–8. Every gap must map to a named candidate requirement and owner. The chart must encode both lenses visibly, label axes and topics, include the synthetic-source limitation and reconcile to the data table. prompt-log.csv must contain P-005.

## Checkpoint and Rejoin Point

Keep the final score table, gap register and chart. Rejoin by using only Final_* scores, named evidence gaps and human-approved follow-up actions in Labs 6–8.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Every topic receives a high score. | Reapply the written anchors independently and use lower scores when evidence or likelihood does not meet the anchor. |
| The assistant merges the two lenses. | Reject the combined score and require separate impact and investor component columns. |
| The chart implies a formal conclusion. | Use 'candidate topic scores', add the synthetic limitation and retain the human decision note. |

## Challenge

Have a partner score the five topics independently. Flag component differences of two points or more and record what extra evidence or anchor clarification would resolve each difference.

## Reflection

Which topic changed most when you separated the two materiality lenses, and what does that reveal about audience?

---

[← Lab 4](lab-04-calculate-scope-1-scope-2-and-intensity-metrics.md) · [Lab 6 →](lab-06-draft-and-validate-an-evidence-grounded-disclosure.md)
