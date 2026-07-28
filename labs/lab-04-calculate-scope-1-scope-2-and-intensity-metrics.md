# Lab 4 — Calculate Scope 1, Scope 2 and Intensity Metrics

**Course:** Generative AI for Sustainability Reporting  
**Course Code:** C1311  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** AI for ESG Data Collection and Analysis  
**Maps to:** LO2: calculate and interpret selected emissions and intensity metrics with transparent lineage  
**Duration:** 55 minutes  
**Tools:** Spreadsheet · approved AI assistant · structured-esg-data.csv · emission-factors-training.csv

---

## Goal

Produce a calculation workpaper that can be recalculated from activity data through factor and conversion to final metric.

## What You Will Do

You will join verified activity data to synthetic training emission factors, calculate FY2024 and FY2025 Scope 1 and Scope 2 emissions, and compare absolute and revenue-intensity results. You will ask AI to review the workpaper structure and draft observations, not to supply factors.

## What You Will Build

An emissions-workpaper.xlsx or emissions-workpaper.csv set containing calculation rows, annual summaries, intensity metrics, control checks, a variance note and complete factor provenance.

## Prerequisites

- Completed Lab 3 with C01–C04 resolved or assigned.
- Copy labs/assets/emission-factors-training.csv into HLF-2025/calculation.
- Treat every supplied factor as a synthetic training value; never reuse it for an actual inventory.

> **Data note.** Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

## Step-by-Step

### 1. Create a calculation sheet with Calculation_ID,Year,Site,Controlled_Metric,Scope,Activity_Value,Activity_Unit,Transformation_ID,Factor_Source_ID,Factor_ID,Factor_Value,Factor_Unit,Conversion,Result_kgCO2e,Result_tCO2e,Source_ID and Reviewer. Filter the structured dataset by Controlled_Metric to ELECTRICITY_KWH, DIESEL_L and NATURAL_GAS_KWH. Use Normalised_Value and Normalised_Unit as the activity fields and join Controlled_Metric to the factor table's Metric field.

```text
Scope 1: DIESEL_L and NATURAL_GAS_KWH
Scope 2: ELECTRICITY_KWH
Set Factor_Source_ID=HLF-FACTOR-TRAINING and use CALC-<Row_ID> for detail rows. Reject any row with missing Transformation_ID or Factor_ID, incompatible units or non-reviewed activity status.
```

### 2. Calculate Result_kgCO2e = Activity_Value × Factor_Value and Result_tCO2e = Result_kgCO2e ÷ 1,000. Keep formulas in the spreadsheet. Sum by Year and Scope, then add Total_Scope_1_2. Assign the approved annual summary rows Calculation_ID CALC-FY2024 and CALC-FY2025. Round display values to two decimals but retain full-precision formulas.

```text
Expected training totals:
FY2024 Scope 1 = 159.22 tCO2e · Scope 2 = 326.40 tCO2e · Total = 485.62 tCO2e
FY2025 Scope 1 = 151.77 tCO2e · Scope 2 = 314.16 tCO2e · Total = 465.93 tCO2e
```

### 3. Lookup rows whose Controlled_Metric is REVENUE_SGD_M for each year and calculate Total_Scope_1_2_tCO2e ÷ Normalised_Value. Add an Intensity_Unit column with tCO2e/S$ million. Calculate absolute and intensity percentage change as (FY2025 − FY2024) ÷ FY2024 × 100, guarding against a zero denominator.

```text
Expected training intensity:
FY2024 = 7.14 tCO2e/S$ million · FY2025 = 6.43 tCO2e/S$ million
Use the unrounded totals for percentage-change formulas.
```

### 4. Create controls C05–C09: factor-unit compatibility, factor-ID completeness, row recalculation, scope-summary reconciliation and denominator period match. A second learner or trainer must independently recalculate at least one diesel row, one electricity row and both annual totals.

```text
Control result values: PASS · FAIL · OPEN
A FAIL may not be hidden by rounding.
```

### 5. Provide the annual summary and control results to the approved AI assistant. Ask for three observations that separate absolute change, intensity change and unresolved cause. Save the raw response as review/P-004-observations.md, then edit it so no sentence attributes the change to an initiative unless a supplied source supports that cause. Add P-004 to prompt-log.csv with CALC-FY2024, CALC-FY2025, HLF-FACTOR-TRAINING, output filename, reviewer, final decision and reason.

```text
Return: Observation | Evidence fields | What cannot be concluded | Follow-up owner
Do not claim performance beyond Scope 1 and Scope 2 or imply an official factor.
```

## Test It

The workpaper must reproduce the expected training totals within 0.01 tCO2e and the displayed intensities within 0.01 tCO2e/S$ million. Every calculation row must retain Calculation_ID, activity source, Transformation_ID, factor source HLF-FACTOR-TRAINING, factor ID, units and formula. C05–C09 must be PASS or have a named OPEN owner. The variance note must distinguish absolute and intensity movement and must not state an unsupported cause. prompt-log.csv must contain a completed P-004 row.

## Checkpoint and Rejoin Point

Keep the workpaper, controls and variance note. Rejoin by using the approved annual summary rows and the training-factor limitation in Labs 5–8.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The result is 1,000 times too high or low. | Check whether the factor is kg per unit and confirm the single division by 1,000 when converting to tonnes. |
| A factor joins to the wrong metric. | Use the controlled Metric field and reject many-to-many joins or incompatible Factor_Unit values. |
| Intensity improves while the narrative says emissions performance improved. | Report absolute and intensity results separately and inspect the denominator before interpreting. |

## Challenge

Add a Factor_Sensitivity column and recalculate FY2025 Scope 2 with a ±5% training factor range. Explain why sensitivity is not a substitute for selecting the correct official factor.

## Reflection

Which single workpaper field would most quickly expose a boundary or unit error during review?

---

[← Lab 3](lab-03-create-the-esg-evidence-register-and-data-dictionary.md) · [Lab 5 →](lab-05-run-materiality-gap-and-visual-analysis.md)
