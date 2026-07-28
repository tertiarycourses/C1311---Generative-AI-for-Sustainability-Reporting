# Lab 1 — Set the Reporting Boundary and AI Control Contract

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Generative AI for Sustainability Reporting  
**Maps to:** LO1: establish a responsible, evidence-controlled generative AI reporting workflow  
**Duration:** 40 minutes  
**Tools:** Text editor · approved AI assistant · labs/assets/harbourlight-company-brief.md · source-pack-index.md

---

## Goal

Create the control files that keep every later AI-assisted task inside a defined reporting and evidence boundary.

## What You Will Do

You will set up the synthetic HarbourLight Foods reporting workspace, define the reporting entity, period, audience and evidence boundary, and write an AI-use charter. You will then run one bounded transformation task and record the sources, output and human decision.

## What You Will Build

A reporting-basis.md, ai-use-charter.md and prompt-log.csv that define scope, permitted data, prompt controls, review gates and a reproducible first AI-assisted task.

## Prerequisites

- Create the HLF-2025/source, calculation, draft and review folders described in the Learner Guide.
- Open labs/assets/source-pack-index.md and labs/assets/harbourlight-company-brief.md.
- Use only the synthetic course files; do not paste workplace records into the class assistant.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Create reporting-basis.md. Record Entity, Reporting period, Reporting boundary, Primary audiences, Reporting purposes, Frameworks to investigate, Prepared by, Reviewed by and Unresolved questions. Use the company brief for facts and write MISSING for anything not supplied.

```text
Entity: HarbourLight Foods Pte Ltd
Reporting period: 1 January–31 December 2025
Boundary: Singapore manufacturing and distribution sites listed in HLF-BRIEF-01
Primary audiences: management, customers, investors and other affected stakeholders
Rule: source ID, documented calculation, documented judgement or MISSING
```

### 2. Create ai-use-charter.md with five headings: Permitted tasks, Prohibited inputs, Required output controls, Human review gates and Recordkeeping. Under each heading add at least three specific rules. Include a rule that AI may structure, compare, draft or critique supplied evidence but may not invent a metric, factor, stakeholder view, applicability conclusion or approval.

```text
Required output controls:
- cite supplied source IDs
- preserve units and periods
- label calculations and assumptions
- write MISSING for unsupported fields
- separate observed facts, interpretation and recommended follow-up
```

### 3. Create prompt-log.csv with columns Prompt_ID,Date,Model_or_Service,Purpose,Source_IDs,Input_Data_Class,Output_File,Reviewer,Decision,Decision_Reason. Add row P-001. Then write a six-part prompt in review/P-001-prompt.md using Goal, Context, Constraints, Sources, Output and Review.

```text
Goal: Extract the supplied company profile into a reporting-scope table.
Context: This is a synthetic FY2025 sustainability-reporting exercise.
Constraints: Use only HLF-BRIEF-01; preserve names and dates; write MISSING where silent.
Sources: <PASTE HLF-BRIEF-01>
Output: Field | Extracted value | Source ID | Status.
Review: Flag any inferred boundary, audience or obligation.
```

### 4. Run P-001 in one approved AI assistant. Save the response as review/P-001-output.md. Compare every row with HLF-BRIEF-01, add a Human_check column, and mark each row SUPPORTED, REVISE or REMOVE. Update prompt-log.csv with the service name, output file, reviewer, final decision and a specific reason.

```text
Decision values: APPROVE · REVISE · STOP
APPROVE only if every retained value is supported and all missing items remain visible.
```

## Test It

Open the three control files. reporting-basis.md must state entity, FY2025 period, boundary, audiences, owners and unresolved questions. ai-use-charter.md must contain all five headings and at least fifteen specific rules. prompt-log.csv must contain P-001 with source HLF-BRIEF-01, output filename, reviewer, decision and reason. P-001-output.md must have no unsupported row marked SUPPORTED.

## Checkpoint and Rejoin Point

Keep reporting-basis.md, ai-use-charter.md, prompt-log.csv and the P-001 files. If you need to rejoin, use these files as the reporting and AI-control boundary for Labs 2–8.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The AI fills missing fields with plausible detail. | Add 'write MISSING; do not infer or complete' to Constraints and rerun under a new prompt-log row. |
| The output contains no source IDs. | Make Source ID a required column and reject any row that does not cite HLF-BRIEF-01. |
| The charter is generic. | Replace words such as 'careful' with observable rules, named files, allowed statuses and review gates. |

## Challenge

Add a risk rating from 1–3 to the prompt log. Define anchors based on data sensitivity, decision impact and ease of verification, then assign and justify the rating for P-001.

## Reflection

Which control most reduced the chance that fluent language would be mistaken for reporting evidence, and what artifact proves that control operated?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-build-the-framework-and-materiality-lens-register.md)
