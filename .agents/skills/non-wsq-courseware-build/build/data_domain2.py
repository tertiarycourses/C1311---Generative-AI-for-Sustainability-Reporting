"""Topic 2 labs for C1311."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Create the ESG Evidence Register and Data Dictionary",
        duration=50,
        objective="LO2: structure ESG source data with traceable provenance, units and quality status",
        goal="Turn the synthetic source pack into a controlled table without losing raw values, units or evidence lineage.",
        workflow=["Inventory sources", "Define the schema", "Normalise carefully", "Reconcile and log"],
        desc=(
            "You will inspect HarbourLight's synthetic activity records, define a data dictionary and "
            "create a structured ESG dataset. An AI assistant may propose field classifications and "
            "normalisation rules, but you will reconcile every retained value to its source row."
        ),
        build=(
            "A data-dictionary.csv, esg-evidence-register.csv and structured-esg-data.csv containing "
            "raw and normalised values, source IDs, owners, periods, boundaries and review status."
        ),
        services="Spreadsheet · approved AI assistant · esg-activity-data.csv · esg-evidence-register-starter.csv",
        prerequisites=[
            "Completed Labs 1–2 and retained the reporting basis and AI-use charter.",
            "Open labs/assets/esg-activity-data.csv and esg-evidence-register-starter.csv.",
            "Do not edit the original files in labs/assets; work on copies in HLF-2025/source.",
        ],
        steps=[
            (
                "Copy the two CSV files into HLF-2025/source. Complete esg-evidence-register.csv with one row per "
                "Source_ID. Record Owner, Entity_or_Site, Reporting_Period, Evidence_Type, Location, Data_Class, "
                "Completeness_Status and Reviewer. Use COMPLETE, PARTIAL, MISSING or PENDING CHECK only.",
                "Evidence register control: Source_ID must be unique and every activity-data row must reference one registered source.",
            ),
            (
                "Create data-dictionary.csv with columns Field,Definition,Data_Type,Allowed_Unit,Allowed_Values,"
                "Null_Treatment,Transformation_Rule and Control_Check. Define at least the fields Year,Entity,Site,"
                "Metric,Controlled_Metric,Raw_Value,Raw_Unit,Normalised_Value,Normalised_Unit,Source_ID,Source_Row,"
                "Transformation_ID and Verification_Status.",
                "Controlled mapping:\nELECTRICITY → ELECTRICITY_KWH · DIESEL → DIESEL_L · "
                "NATURAL_GAS → NATURAL_GAS_KWH · REVENUE → REVENUE_SGD_M\n"
                "Reject any uncontrolled metric name.",
            ),
            (
                "Paste the Metric, Raw_Value and Raw_Unit columns into the approved AI assistant and ask for a proposed "
                "controlled metric name, normalised unit and transformation note. Require the assistant to preserve row IDs "
                "and return NO RULE when a conversion is not defined. Save the raw response as "
                "review/P-003-normalisation-proposal.csv. Add P-003 to prompt-log.csv before review.",
                "Return: Row_ID | Proposed_Metric | Proposed_Unit | Proposed_Transformation | Uncertainty\n"
                "Do not calculate or fill missing values.",
            ),
            (
                "Create structured-esg-data.csv. Copy the raw fields unchanged, then enter Controlled_Metric, reviewed "
                "Normalised_Value, Normalised_Unit, Transformation_Rule, a unique Transformation_ID and Verification_Status. "
                "Use TR-<Row_ID> for each reviewed row. For MWh, multiply by 1,000 to obtain kWh; "
                "for every other supplied row preserve the given unit unless the data dictionary defines a rule. "
                "Reject or revise every AI proposal that changes a value without a documented rule.",
                "Verification_Status: VERIFIED · REVISED · MISSING · REJECTED\n"
                "Keep Raw_Value and Raw_Unit immutable. Update P-003 in prompt-log.csv with output filename, reviewer, "
                "APPROVE/REVISE/STOP decision and reason; retained corrections must be visible in the reviewed structured file.",
            ),
            (
                "Run four spreadsheet controls: Source_ID lookup completeness, duplicate Row_ID count, raw-to-normalised "
                "conversion check and year/metric totals. Add a control-log sheet or control-log.csv with Control_ID,Result,"
                "Exception_Count,Resolution and Reviewer. Resolve exceptions or mark them OPEN with a named owner.",
                "Required controls: C01 all sources registered · C02 Row_ID unique · C03 conversions recalculate · C04 totals reconcile",
            ),
        ],
        test=(
            "data-dictionary.csv must define all required fields and their controls. Every structured row must retain "
            "Row_ID, Controlled_Metric, raw value, raw unit, source ID, source row and unique Transformation_ID. "
            "All MWh rows must convert exactly to kWh, no other value "
            "may change without a rule, and every source lookup must resolve. The control log must contain C01–C04 with "
            "reviewer, result and resolution or named open owner. prompt-log.csv must contain completed P-003 review fields."
        ),
        checkpoint=(
            "Use structured-esg-data.csv and data-dictionary.csv as the only metric inputs in Labs 4–8. Rejoin by filtering "
            "Verification_Status to VERIFIED or REVISED and keeping OPEN exceptions visible."
        ),
        troubleshooting=[
            (
                "The assistant combines site rows.",
                "Require one output row per original Row_ID and prohibit aggregation during normalisation.",
            ),
            (
                "A value changed but the unit did not.",
                "Reject the row, restore the raw value and apply only the explicit transformation rule from the dictionary.",
            ),
            (
                "A source lookup fails.",
                "Do not invent a source; mark the record MISSING or PENDING CHECK and assign an evidence owner.",
            ),
        ],
        challenge=(
            "Add Minimum, Maximum and Decimal_Places to the dictionary for three metrics. Create a range control and show "
            "how an outlier is quarantined without deleting the raw record."
        ),
        reflection=(
            "Which field in your structured dataset is most important for reproducing a reported number later, and why?"
        ),
    ),
    dict(
        num=4,
        topic=2,
        title="Calculate Scope 1, Scope 2 and Intensity Metrics",
        duration=55,
        objective="LO2: calculate and interpret selected emissions and intensity metrics with transparent lineage",
        goal="Produce a calculation workpaper that can be recalculated from activity data through factor and conversion to final metric.",
        workflow=["Confirm boundaries", "Join factors", "Calculate and reconcile", "Interpret cautiously"],
        desc=(
            "You will join verified activity data to synthetic training emission factors, calculate FY2024 "
            "and FY2025 Scope 1 and Scope 2 emissions, and compare absolute and revenue-intensity results. "
            "You will ask AI to review the workpaper structure and draft observations, not to supply factors."
        ),
        build=(
            "An emissions-workpaper.xlsx or emissions-workpaper.csv set containing calculation rows, annual summaries, "
            "intensity metrics, control checks, a variance note and complete factor provenance."
        ),
        services="Spreadsheet · approved AI assistant · structured-esg-data.csv · emission-factors-training.csv",
        prerequisites=[
            "Completed Lab 3 with C01–C04 resolved or assigned.",
            "Copy labs/assets/emission-factors-training.csv into HLF-2025/calculation.",
            "Treat every supplied factor as a synthetic training value; never reuse it for an actual inventory.",
        ],
        steps=[
            (
                "Create a calculation sheet with Calculation_ID,Year,Site,Controlled_Metric,Scope,Activity_Value,"
                "Activity_Unit,Transformation_ID,Factor_Source_ID,Factor_ID,Factor_Value,Factor_Unit,Conversion,"
                "Result_kgCO2e,Result_tCO2e,Source_ID and Reviewer. Filter the structured dataset by Controlled_Metric "
                "to ELECTRICITY_KWH, DIESEL_L and NATURAL_GAS_KWH. Use Normalised_Value and Normalised_Unit as the "
                "activity fields and join Controlled_Metric to the factor table's Metric field.",
                "Scope 1: DIESEL_L and NATURAL_GAS_KWH\nScope 2: ELECTRICITY_KWH\n"
                "Set Factor_Source_ID=HLF-FACTOR-TRAINING and use CALC-<Row_ID> for detail rows. Reject any row with missing "
                "Transformation_ID or Factor_ID, incompatible units or non-reviewed activity status.",
            ),
            (
                "Calculate Result_kgCO2e = Activity_Value × Factor_Value and Result_tCO2e = Result_kgCO2e ÷ 1,000. "
                "Keep formulas in the spreadsheet. Sum by Year and Scope, then add Total_Scope_1_2. Assign the approved "
                "annual summary rows Calculation_ID CALC-FY2024 and CALC-FY2025. Round display values "
                "to two decimals but retain full-precision formulas.",
                "Expected training totals:\n"
                "FY2024 Scope 1 = 159.22 tCO2e · Scope 2 = 326.40 tCO2e · Total = 485.62 tCO2e\n"
                "FY2025 Scope 1 = 151.77 tCO2e · Scope 2 = 314.16 tCO2e · Total = 465.93 tCO2e",
            ),
            (
                "Lookup rows whose Controlled_Metric is REVENUE_SGD_M for each year and calculate "
                "Total_Scope_1_2_tCO2e ÷ Normalised_Value. Add an "
                "Intensity_Unit column with tCO2e/S$ million. Calculate absolute and intensity percentage change as "
                "(FY2025 − FY2024) ÷ FY2024 × 100, guarding against a zero denominator.",
                "Expected training intensity:\nFY2024 = 7.14 tCO2e/S$ million · FY2025 = 6.43 tCO2e/S$ million\n"
                "Use the unrounded totals for percentage-change formulas.",
            ),
            (
                "Create controls C05–C09: factor-unit compatibility, factor-ID completeness, row recalculation, "
                "scope-summary reconciliation and denominator period match. A second learner or trainer must independently "
                "recalculate at least one diesel row, one electricity row and both annual totals.",
                "Control result values: PASS · FAIL · OPEN\nA FAIL may not be hidden by rounding.",
            ),
            (
                "Provide the annual summary and control results to the approved AI assistant. Ask for three observations "
                "that separate absolute change, intensity change and unresolved cause. Save the raw response as "
                "review/P-004-observations.md, then edit it so no sentence attributes the change to an initiative unless a "
                "supplied source supports that cause. Add P-004 to prompt-log.csv with CALC-FY2024, CALC-FY2025, "
                "HLF-FACTOR-TRAINING, output filename, reviewer, final decision and reason.",
                "Return: Observation | Evidence fields | What cannot be concluded | Follow-up owner\n"
                "Do not claim performance beyond Scope 1 and Scope 2 or imply an official factor.",
            ),
        ],
        test=(
            "The workpaper must reproduce the expected training totals within 0.01 tCO2e and the displayed intensities "
            "within 0.01 tCO2e/S$ million. Every calculation row must retain Calculation_ID, activity source, "
            "Transformation_ID, factor source HLF-FACTOR-TRAINING, factor ID, units and formula. "
            "C05–C09 must be PASS or have a named OPEN owner. The variance note must distinguish absolute and intensity "
            "movement and must not state an unsupported cause. prompt-log.csv must contain a completed P-004 row."
        ),
        checkpoint=(
            "Keep the workpaper, controls and variance note. Rejoin by using the approved annual summary rows and the "
            "training-factor limitation in Labs 5–8."
        ),
        troubleshooting=[
            (
                "The result is 1,000 times too high or low.",
                "Check whether the factor is kg per unit and confirm the single division by 1,000 when converting to tonnes.",
            ),
            (
                "A factor joins to the wrong metric.",
                "Use the controlled Metric field and reject many-to-many joins or incompatible Factor_Unit values.",
            ),
            (
                "Intensity improves while the narrative says emissions performance improved.",
                "Report absolute and intensity results separately and inspect the denominator before interpreting.",
            ),
        ],
        challenge=(
            "Add a Factor_Sensitivity column and recalculate FY2025 Scope 2 with a ±5% training factor range. "
            "Explain why sensitivity is not a substitute for selecting the correct official factor."
        ),
        reflection=(
            "Which single workpaper field would most quickly expose a boundary or unit error during review?"
        ),
    ),
    dict(
        num=5,
        topic=2,
        title="Run Materiality, Gap and Visual Analysis",
        duration=50,
        objective="LO2: perform transparent materiality and gap analysis and communicate results with an honest visual",
        goal="Prioritise five candidate topics under separate lenses, show framework evidence gaps and create one decision-useful chart.",
        workflow=["Set scoring anchors", "Score with evidence", "Map the gaps", "Visualise and review"],
        desc=(
            "You will use synthetic stakeholder and business evidence to score five topics under separate "
            "impact and investor lenses, map each topic to the framework register and classify evidence gaps. "
            "You will then create a chart and a short summary that avoids causal overreach."
        ),
        build=(
            "A materiality-gap-analysis.xlsx or CSV set with scoring anchors, topic evidence, two separate lens scores, "
            "framework-gap status, a labelled chart, reviewer decisions and a follow-up plan."
        ),
        services="Spreadsheet · approved AI assistant · stakeholder-impact-notes.md · framework-and-applicability-register.csv",
        prerequisites=[
            "Completed Labs 2–4 and retained the framework register, structured dataset and approved metric summary.",
            "Open labs/assets/stakeholder-impact-notes.md.",
            "Do not ask the AI assistant to invent stakeholder views, impacts, risks or requirement status.",
        ],
        steps=[
            (
                "Create scoring-anchors.md before scoring. Define 0–4 anchors for Impact_Significance and "
                "Impact_Likelihood, plus 0–4 anchors for Investor_Effect and Investor_Likelihood. Define Evidence_Strength "
                "as 0 none, 1 one indirect note, 2 one direct source, 3 two corroborating sources. Do not combine the lenses.",
                "Impact lens result = significance + likelihood (0–8)\n"
                "Investor lens result = effect on prospects + likelihood (0–8)\n"
                "Evidence strength is a visible confidence input, not extra materiality points.",
            ),
            (
                "Create materiality-gap-analysis.csv with rows Energy and emissions, Packaging waste, Worker safety, "
                "Climate transition risk, and Sustainability-information governance. For each row cite Source_IDs from "
                "stakeholder-impact-notes.md and the prior labs, classify each statement as OBSERVED, INTERPRETATION or UNKNOWN, "
                "then enter proposed component scores with a one-sentence evidence rationale.",
                "Required fields: Analysis_ID | Topic | Proposed_Impact_Significance | Proposed_Impact_Likelihood | "
                "Proposed_Investor_Effect | Proposed_Investor_Likelihood | Final_Impact_Significance | "
                "Final_Impact_Likelihood | Final_Impact_Total | Final_Investor_Effect | Final_Investor_Likelihood | "
                "Final_Investor_Total | Adjustment_Reason | Evidence_Strength | Source_IDs | Rationale | Reviewer\n"
                "Use Analysis_ID=MAT-GAP-01 for the controlled five-topic analysis.",
            ),
            (
                "Give only the five evidence summaries and written anchors to the approved AI assistant. Ask for proposed "
                "scores, missing evidence and possible lens conflicts. Save the raw response as review/P-005-score-proposals.csv "
                "and add P-005 to prompt-log.csv. Enter AI proposals in Proposed_* columns, then make your own Final_* "
                "decisions. Calculate totals only from the Final_* component scores. Record Adjustment_Reason whenever the "
                "final score differs, and update P-005 with reviewer, decision and reason.",
                "AI role: organise and challenge the supplied evidence.\nHuman role: decide scores, thresholds and next action.",
            ),
            (
                "Join each topic to the framework register and add Candidate_Requirement, Available_Evidence, Gap_Status,"
                "Gap_Description, Owner and Due_Date. Use COMPLETE, PARTIAL, MISSING, NOT APPLICABLE or PENDING INTERPRETATION. "
                "A high materiality score does not turn a partial evidence set into a complete disclosure.",
                "Gap rule: status describes evidence against a named requirement—not the importance of the topic.",
            ),
            (
                "Create a scatter chart with Final_Investor_Total on the x-axis, Final_Impact_Total on the y-axis and Topic as the "
                "point label, or a grouped bar chart with both lens totals by Topic. Show the 0–8 scale, use a neutral title, "
                "include a source note and write three sentences: observation, interpretation and required follow-up.",
                "Title: HarbourLight Candidate Topic Scores by Reporting Lens\n"
                "Source note: Synthetic HLF evidence; human-scored using documented 0–4 anchors; not an organisational materiality conclusion.",
            ),
        ],
        test=(
            "MAT-GAP-01 must contain all five topics with Proposed_* and Final_* component scores, formulas based on Final_* "
            "scores, source IDs, evidence strength, final reviewer and any "
            "adjustment reason. Impact and investor totals must remain separate and range from 0–8. Every gap must map to "
            "a named candidate requirement and owner. The chart must encode both lenses visibly, label axes and topics, "
            "include the synthetic-source limitation and reconcile to the data table. prompt-log.csv must contain P-005."
        ),
        checkpoint=(
            "Keep the final score table, gap register and chart. Rejoin by using only Final_* scores, named evidence gaps "
            "and human-approved follow-up actions in Labs 6–8."
        ),
        troubleshooting=[
            (
                "Every topic receives a high score.",
                "Reapply the written anchors independently and use lower scores when evidence or likelihood does not meet the anchor.",
            ),
            (
                "The assistant merges the two lenses.",
                "Reject the combined score and require separate impact and investor component columns.",
            ),
            (
                "The chart implies a formal conclusion.",
                "Use 'candidate topic scores', add the synthetic limitation and retain the human decision note.",
            ),
        ],
        challenge=(
            "Have a partner score the five topics independently. Flag component differences of two points or more and "
            "record what extra evidence or anchor clarification would resolve each difference."
        ),
        reflection=(
            "Which topic changed most when you separated the two materiality lenses, and what does that reveal about audience?"
        ),
    ),
]
