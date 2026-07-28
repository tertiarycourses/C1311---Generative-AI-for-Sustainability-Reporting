# Lab 8 — Design the Recurring Reporting Workflow and Final Pack

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 4:** AI for Compliance, Frameworks and Continuous Reporting  
**Maps to:** LO4: design a governed recurring workflow for multi-year sustainability reporting  
**Duration:** 55 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · all Lab 1–7 artifacts

---

## Goal

Turn the course artifacts into a repeatable reporting operating model with entry gates, owners, exceptions and change control.

## What You Will Do

You will design a reporting calendar and workflow board that reuses controlled structures without copying stale claims. You will specify source-owner data contracts, AI task boundaries, review gates, change triggers and a final pack index that lets another preparer continue the process.

## What You Will Build

A reporting-calendar.csv, workflow-board.csv, data-contracts.md, final-pack-index.md and post-cycle-review.md covering the complete scope-to-publication cycle and its evidence-controlled AI tasks.

## Prerequisites

- Completed Labs 1–7 and retained all current-version controls, exceptions and owner assignments.
- Create an HLF-2025/final-pack folder; do not move or overwrite the original source files.
- Copy reporting-calendar-starter.csv, workflow-board-starter.csv and post-cycle-review-starter.md from labs/assets.
- Use the crosswalk and control matrix to define gates instead of relying on a generic reporting checklist.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Complete reporting-calendar-starter.csv and save it as reporting-calendar.csv with Phase,Start,Finish,Entry_Criteria,Output,Owner,Reviewer and Escalation. Include Scope and applicability, Source intake, Data validation, Calculation, Materiality and gaps, Drafting, Framework mapping, Review and approval, Publication archive, and Post-cycle improvement.

```text
Entry criteria must be observable—for example, 'all required source IDs received or exception owner assigned'.
```

### 2. Create data-contracts.md with one section each for electricity, fuel, revenue, material-topic evidence and governance evidence. For each, state owner, source system, schema, unit, frequency, due date, validation, retention, change notification and exception route. Add a rule that raw values are immutable and corrections create a new version with a reason.

```text
Data contract fields: Owner · Source · Schema · Unit · Frequency · Due · Validation · Retention · Change trigger · Exception owner
```

### 3. Complete workflow-board-starter.csv and save it as workflow-board.csv with Stage,Task_ID,Task,Input_IDs,AI_Role,Human_Decision,Control_ID,Output_ID,Status and Reopen_Trigger. Add at least twelve tasks across the ten phases. Limit AI_Role to NONE, STRUCTURE, COMPARE, DRAFT or CRITIQUE; no task may assign materiality, applicability, approval or publication to AI.

```text
Human decisions reserved: scope · materiality · estimate · factor approval · causal claim · framework applicability · exception acceptance · final publication
```

### 4. Ask the approved AI assistant to critique the calendar and board for missing handoffs, circular dependencies, unowned exceptions, stale-prior-year risk and gates that cannot be tested. Save the raw critique as review/P-008-workflow-critique.md and add P-008 to prompt-log.csv. Verify every suggestion and record accepted and rejected changes in review/workflow-change-log.csv with Change_ID,Reason,Affected_Task,Decision and Reviewer. Update P-008 with output filename, reviewer, final decision and reason.

```text
Critique only the supplied workflow. Do not invent organisational roles, service levels or reporting obligations.
```

### 5. Create a provisional final-pack-index.md. List each current artifact already completed in Labs 1–8 with Version,Owner,Reviewer,Status,Key_Source_IDs and Reopen_Trigger. Include a Start Here section that tells a new preparer how to confirm applicability, inspect open exceptions, rerun calculations and avoid copying stale narrative. Copy only approved current outputs—not raw AI responses—into HLF-2025/final-pack.

```text
Required groups: governance · requirements · source data · calculations · materiality/gaps · narrative · evidence/control · recurring workflow
```

### 6. Complete post-cycle-review-starter.md and save it as post-cycle-review.md with five metrics: source timeliness, control exception rate, unsupported-claim rate, review rework count and cycle time. For rates, define numerator and denominator. For a count or duration, set Denominator=N/A and define Unit_or_Basis. Name the owner and improvement trigger for each. Add three lessons and one controlled improvement for the next cycle.

```text
Measure credibility and rework—not number of generated words. Count basis: reviewed change records. Cycle-time basis: elapsed calendar days from approved scope to publication archive.
```

### 7. After post-cycle-review.md is complete, update final-pack-index.md so it indexes the final calendar, board, data contracts, P-008 review records and post-cycle review as well as every approved artifact from Labs 1–7. Recheck file locations, versions, owners, reviewers, statuses, source IDs, open items and reopen triggers; then copy the final index into HLF-2025/final-pack.

```text
Final sequencing rule: post-cycle review first → final index update second → Start Here path verification last.
```

## Test It

The calendar must contain all ten phases with owner, reviewer, entry criteria, output and escalation. data-contracts.md must cover all five evidence classes and versioned corrections. The workflow board must contain at least twelve tasks, allowed AI roles only, named human decisions and reopen triggers. The final pack must index every Lab 1–8 artifact, identify open items and give a reproducible Start Here path. The post-cycle review must define all five metrics with the rate numerator/denominator or count/duration Unit_or_Basis, owner and trigger. prompt-log.csv must contain P-008, and final-pack-index.md must be updated after the post-cycle review so every Lab 1–8 artifact is indexed.

## Checkpoint and Rejoin Point

The final-pack folder is the course endpoint. A new preparer should be able to start with final-pack-index.md, locate every approved artifact, see all unresolved items and know which changes reopen earlier work.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A workflow gate says 'data ready'. | Replace it with observable criteria, required control results and an exception path. |
| The next-year process copies the prior narrative. | Use prior wording only as a comparison source; reopen claims whenever data, boundary, factor, method or requirement changes. |
| An exception has no owner. | Stop the affected task, assign an accountable owner and record an escalation date before continuing. |

## Challenge

Create a RACI view from the workflow board and identify any stage where one person prepares, reviews and approves a high-risk item. Propose a proportionate segregation-of-duties improvement.

## Reflection

Which reopen trigger is most important for preventing a fast but inaccurate next-year report?

---

[← Lab 7](lab-07-build-the-framework-crosswalk-and-assurance-evidence-index.md) · [Labs index →](README.md)
