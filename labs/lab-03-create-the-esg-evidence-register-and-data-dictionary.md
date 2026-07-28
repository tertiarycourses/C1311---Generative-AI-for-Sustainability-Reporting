# Lab 3 — Create the ESG Evidence Register and Data Dictionary

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** AI for ESG Data Collection and Analysis  
**Maps to:** LO2: structure ESG source data with traceable provenance, units and quality status  
**Duration:** 50 minutes  
**Tools:** Spreadsheet · approved AI assistant · esg-activity-data.csv · esg-evidence-register-starter.csv

---

## Goal

Turn the synthetic source pack into a controlled table without losing raw values, units or evidence lineage.

## What You Will Do

You will inspect HarbourLight's synthetic activity records, define a data dictionary and create a structured ESG dataset. An AI assistant may propose field classifications and normalisation rules, but you will reconcile every retained value to its source row.

## What You Will Build

A data-dictionary.csv, esg-evidence-register.csv and structured-esg-data.csv containing raw and normalised values, source IDs, owners, periods, boundaries and review status.

## Prerequisites

- Completed Labs 1–2 and retained the reporting basis and AI-use charter.
- Open labs/assets/esg-activity-data.csv and esg-evidence-register-starter.csv.
- Do not edit the original files in labs/assets; work on copies in HLF-2025/source.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Copy the two CSV files into HLF-2025/source. Complete esg-evidence-register.csv with one row per Source_ID. Record Owner, Entity_or_Site, Reporting_Period, Evidence_Type, Location, Data_Class, Completeness_Status and Reviewer. Use COMPLETE, PARTIAL, MISSING or PENDING CHECK only.

```text
Evidence register control: Source_ID must be unique and every activity-data row must reference one registered source.
```

### 2. Create data-dictionary.csv with columns Field,Definition,Data_Type,Allowed_Unit,Allowed_Values,Null_Treatment,Transformation_Rule and Control_Check. Define at least the fields Year,Entity,Site,Metric,Controlled_Metric,Raw_Value,Raw_Unit,Normalised_Value,Normalised_Unit,Source_ID,Source_Row,Transformation_ID and Verification_Status.

```text
Controlled mapping:
ELECTRICITY → ELECTRICITY_KWH · DIESEL → DIESEL_L · NATURAL_GAS → NATURAL_GAS_KWH · REVENUE → REVENUE_SGD_M
Reject any uncontrolled metric name.
```

### 3. Paste the Metric, Raw_Value and Raw_Unit columns into the approved AI assistant and ask for a proposed controlled metric name, normalised unit and transformation note. Require the assistant to preserve row IDs and return NO RULE when a conversion is not defined. Save the raw response as review/P-003-normalisation-proposal.csv. Add P-003 to prompt-log.csv before review.

```text
Return: Row_ID | Proposed_Metric | Proposed_Unit | Proposed_Transformation | Uncertainty
Do not calculate or fill missing values.
```

### 4. Create structured-esg-data.csv. Copy the raw fields unchanged, then enter Controlled_Metric, reviewed Normalised_Value, Normalised_Unit, Transformation_Rule, a unique Transformation_ID and Verification_Status. Use TR-<Row_ID> for each reviewed row. For MWh, multiply by 1,000 to obtain kWh; for every other supplied row preserve the given unit unless the data dictionary defines a rule. Reject or revise every AI proposal that changes a value without a documented rule.

```text
Verification_Status: VERIFIED · REVISED · MISSING · REJECTED
Keep Raw_Value and Raw_Unit immutable. Update P-003 in prompt-log.csv with output filename, reviewer, APPROVE/REVISE/STOP decision and reason; retained corrections must be visible in the reviewed structured file.
```

### 5. Run four spreadsheet controls: Source_ID lookup completeness, duplicate Row_ID count, raw-to-normalised conversion check and year/metric totals. Add a control-log sheet or control-log.csv with Control_ID,Result,Exception_Count,Resolution and Reviewer. Resolve exceptions or mark them OPEN with a named owner.

```text
Required controls: C01 all sources registered · C02 Row_ID unique · C03 conversions recalculate · C04 totals reconcile
```

## Test It

data-dictionary.csv must define all required fields and their controls. Every structured row must retain Row_ID, Controlled_Metric, raw value, raw unit, source ID, source row and unique Transformation_ID. All MWh rows must convert exactly to kWh, no other value may change without a rule, and every source lookup must resolve. The control log must contain C01–C04 with reviewer, result and resolution or named open owner. prompt-log.csv must contain completed P-003 review fields.

## Checkpoint and Rejoin Point

Use structured-esg-data.csv and data-dictionary.csv as the only metric inputs in Labs 4–8. Rejoin by filtering Verification_Status to VERIFIED or REVISED and keeping OPEN exceptions visible.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The assistant combines site rows. | Require one output row per original Row_ID and prohibit aggregation during normalisation. |
| A value changed but the unit did not. | Reject the row, restore the raw value and apply only the explicit transformation rule from the dictionary. |
| A source lookup fails. | Do not invent a source; mark the record MISSING or PENDING CHECK and assign an evidence owner. |

## Challenge

Add Minimum, Maximum and Decimal_Places to the dictionary for three metrics. Create a range control and show how an outlier is quarantined without deleting the raw record.

## Reflection

Which field in your structured dataset is most important for reproducing a reported number later, and why?

---

[← Lab 2](lab-02-build-the-framework-and-materiality-lens-register.md) · [Lab 4 →](lab-04-calculate-scope-1-scope-2-and-intensity-metrics.md)
