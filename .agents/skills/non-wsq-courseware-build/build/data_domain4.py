"""Topic 4 labs for C1311."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Build the Framework Crosswalk and Assurance Evidence Index",
        duration=55,
        objective="LO4: map approved content to current framework sources and maintain an assurance-ready audit trail",
        goal="Connect every approved disclosure and metric to requirements, evidence, controls, owners and review status without overstating applicability.",
        workflow=["Confirm applicability", "Map requirements", "Index evidence", "Test the lineage"],
        desc=(
            "You will extend the framework register into a requirement crosswalk, map the Lab 6 disclosure "
            "and Lab 4 metrics, and build an evidence index from source through calculation, claim and approval. "
            "You will also record current Singapore applicability questions for responsible-owner confirmation."
        ),
        build=(
            "A framework-crosswalk.csv, assurance-evidence-index.csv and control-matrix.csv with requirement IDs, "
            "report locations, evidence lineage, owners, statuses, exceptions and reviewer sign-off."
        ),
        services="Spreadsheet · browser · approved AI assistant · Lab 2 register · Lab 4 workpaper · Lab 6 claim ledger",
        prerequisites=[
            "Completed Labs 2, 4 and 6 and retained their official URLs, approved calculations and claim statuses.",
            "Open labs/assets/framework-crosswalk-starter.csv, assurance-evidence-index-starter.csv and control-matrix-starter.csv.",
            "Treat HarbourLight's entity and listing status as a synthetic scenario; record jurisdiction decisions as PENDING OWNER CONFIRMATION.",
        ],
        steps=[
            (
                "Time box: 8 minutes. Copy framework-crosswalk-starter.csv to framework-crosswalk.csv. Reuse the checked "
                "dates and status notes from Lab 2; reopen any source marked PENDING CHECK or changed since that check. "
                "The starter already contains REFERENCE source rows and seven ACTIVE mapping rows for reporting basis, "
                "energy and emissions methods, Scope 1 and Scope 2 results, material-topic process, governance and limitations.",
                "Required source families: GRI 1/2/3 and relevant Topic Standard · IFRS S1 · IFRS S2 · "
                "SASB industry guidance · TCFD bridge · SGX Rule 711B · Singapore requirements timeline",
            ),
            (
                "Time box: 12 minutes. For each ACTIVE mapping row, complete Audience,Lens,Applicability_Status,Applicability_Owner,Report_Location,"
                "Claim_IDs,Metric_IDs,Evidence_Status,Gap,Action_Owner and Due_Date. Use COMPLETE, PARTIAL, MISSING, "
                "NOT APPLICABLE or PENDING INTERPRETATION for evidence; use PENDING OWNER CONFIRMATION where entity scope "
                "or jurisdiction has not been established. Keep REFERENCE rows as source controls rather than duplicating "
                "a report-location mapping on them.",
                "Mapping test: exact requirement + rationale + current source + report location + evidence + owner + status",
            ),
            (
                "Time box: 8 minutes. Give the seven ACTIVE crosswalk rows and official-source summaries to the approved AI assistant. Ask it to identify "
                "keyword-only mappings, lens conflicts, obsolete TCFD treatment, missing owners and any unsupported statement "
                "of alignment. Save the raw critique as review/P-007-crosswalk-critique.md and add P-007 to prompt-log.csv. "
                "Verify every proposed change against the official URL before editing; record the reviewer decision and "
                "reason in P-007 and retain accepted or rejected changes in the reviewed crosswalk fields.",
                "Return: Crosswalk_ID | Issue | Why_it_matters | Official_source_to_check | Proposed_status\n"
                "Do not declare applicability or conformity.",
            ),
            (
                "Time box: 12 minutes. Complete the five supplied rows in assurance-evidence-index-starter.csv and save it as assurance-evidence-index.csv with "
                "Evidence_ID,Evidence_Type,Original_Source_ID,Transformation_ID,"
                "Calculation_ID,Claim_ID,Crosswalk_ID,File_Location,Version,Prepared_By,Reviewed_By,Approval_Status and "
                "Exception_ID. Create at least one complete chain for FY2025 Scope 1, Scope 2, total, intensity and the "
                "factor limitation.",
                "Lineage pattern: source → structured row → calculation → claim → disclosure location → framework mapping → approval",
            ),
            (
                "Time box: 10 minutes, leaving 5 minutes for the Test It check. Complete the seven supplied rows in "
                "control-matrix-starter.csv and save it as control-matrix.csv with "
                "Control_ID,Risk,Control_Activity,Frequency,Preparer,Reviewer,Evidence,"
                "Exception_Route and Status. Add controls for source completeness, factor approval, formula accuracy, "
                "claim verification, framework change, access/version control and publication approval. Sample two metric "
                "chains and one narrative chain; record PASS, FAIL or OPEN and resolve or assign every exception.",
                "Minimum controls: CTL-01 source · CTL-02 factor · CTL-03 calculation · CTL-04 claim · "
                "CTL-05 framework change · CTL-06 version/access · CTL-07 publication",
            ),
        ],
        test=(
            "Every ACTIVE crosswalk row must contain an official source, requirement or guidance ID, lens, applicability "
            "status, report location, evidence status and owner; every REFERENCE row must retain its current official URL "
            "and checked or PENDING CHECK status. No synthetic jurisdiction decision may be stated as confirmed. "
            "The evidence index must contain complete reproducible chains for the four metrics and factor limitation. "
            "CTL-01–CTL-07 must have preparer, reviewer, evidence and status, with no unowned FAIL or OPEN item. "
            "prompt-log.csv must contain completed P-007 review fields."
        ),
        checkpoint=(
            "Keep the crosswalk, evidence index and control matrix. Rejoin by filtering to the current version and using "
            "OPEN or PENDING rows as explicit inputs to the recurring workflow in Lab 8."
        ),
        troubleshooting=[
            (
                "A crosswalk row maps only by similar wording.",
                "Return to the exact requirement, materiality lens and evidence definition; downgrade to PARTIAL or remove the mapping.",
            ),
            (
                "The evidence chain skips from source to final claim.",
                "Add the structured-row and calculation or transformation IDs that explain how the evidence changed."),
            (
                "A Singapore rule is marked applicable without entity confirmation.",
                "Set PENDING OWNER CONFIRMATION and name the legal, governance or reporting owner who must decide.",
            ),
        ],
        challenge=(
            "Add a Change_Trigger and Last_Reviewed field to each framework row. Simulate one changed requirement and show "
            "which calculations, claims, controls and approvals must be reopened."
        ),
        reflection=(
            "Which link in your evidence chain would be hardest for an independent reviewer to reconstruct if it were missing, and why?"
        ),
    ),
    dict(
        num=8,
        topic=4,
        title="Design the Recurring Reporting Workflow and Final Pack",
        duration=55,
        objective="LO4: design a governed recurring workflow for multi-year sustainability reporting",
        goal="Turn the course artifacts into a repeatable reporting operating model with entry gates, owners, exceptions and change control.",
        workflow=["Define the cycle", "Set data contracts", "Place quality gates", "Package and improve"],
        desc=(
            "You will design a reporting calendar and workflow board that reuses controlled structures without "
            "copying stale claims. You will specify source-owner data contracts, AI task boundaries, review gates, "
            "change triggers and a final pack index that lets another preparer continue the process."
        ),
        build=(
            "A reporting-calendar.csv, workflow-board.csv, data-contracts.md, final-pack-index.md and post-cycle-review.md "
            "covering the complete scope-to-publication cycle and its evidence-controlled AI tasks."
        ),
        services="Spreadsheet · text editor · approved AI assistant · all Lab 1–7 artifacts",
        prerequisites=[
            "Completed Labs 1–7 and retained all current-version controls, exceptions and owner assignments.",
            "Create an HLF-2025/final-pack folder; do not move or overwrite the original source files.",
            "Copy reporting-calendar-starter.csv, workflow-board-starter.csv and post-cycle-review-starter.md from labs/assets.",
            "Use the crosswalk and control matrix to define gates instead of relying on a generic reporting checklist.",
        ],
        steps=[
            (
                "Complete reporting-calendar-starter.csv and save it as reporting-calendar.csv with "
                "Phase,Start,Finish,Entry_Criteria,Output,Owner,Reviewer and Escalation. "
                "Include Scope and applicability, Source intake, Data validation, Calculation, Materiality and gaps, Drafting, "
                "Framework mapping, Review and approval, Publication archive, and Post-cycle improvement.",
                "Entry criteria must be observable—for example, 'all required source IDs received or exception owner assigned'.",
            ),
            (
                "Create data-contracts.md with one section each for electricity, fuel, revenue, material-topic evidence and "
                "governance evidence. For each, state owner, source system, schema, unit, frequency, due date, validation, "
                "retention, change notification and exception route. Add a rule that raw values are immutable and corrections "
                "create a new version with a reason.",
                "Data contract fields: Owner · Source · Schema · Unit · Frequency · Due · Validation · Retention · "
                "Change trigger · Exception owner",
            ),
            (
                "Complete workflow-board-starter.csv and save it as workflow-board.csv with "
                "Stage,Task_ID,Task,Input_IDs,AI_Role,Human_Decision,Control_ID,Output_ID,"
                "Status and Reopen_Trigger. Add at least twelve tasks across the ten phases. Limit AI_Role to NONE, "
                "STRUCTURE, COMPARE, DRAFT or CRITIQUE; no task may assign materiality, applicability, approval or publication to AI.",
                "Human decisions reserved: scope · materiality · estimate · factor approval · causal claim · "
                "framework applicability · exception acceptance · final publication",
            ),
            (
                "Ask the approved AI assistant to critique the calendar and board for missing handoffs, circular dependencies, "
                "unowned exceptions, stale-prior-year risk and gates that cannot be tested. Save the raw critique as "
                "review/P-008-workflow-critique.md and add P-008 to prompt-log.csv. Verify every suggestion and record accepted "
                "and rejected changes in review/workflow-change-log.csv with Change_ID,Reason,Affected_Task,Decision and Reviewer. "
                "Update P-008 with output filename, reviewer, final decision and reason.",
                "Critique only the supplied workflow. Do not invent organisational roles, service levels or reporting obligations.",
            ),
            (
                "Create a provisional final-pack-index.md. List each current artifact already completed in Labs 1–8 with "
                "Version,Owner,Reviewer,Status,"
                "Key_Source_IDs and Reopen_Trigger. Include a Start Here section that tells a new preparer how to confirm "
                "applicability, inspect open exceptions, rerun calculations and avoid copying stale narrative. Copy only "
                "approved current outputs—not raw AI responses—into HLF-2025/final-pack.",
                "Required groups: governance · requirements · source data · calculations · materiality/gaps · "
                "narrative · evidence/control · recurring workflow",
            ),
            (
                "Complete post-cycle-review-starter.md and save it as post-cycle-review.md with five metrics: source timeliness, "
                "control exception rate, unsupported-claim rate, review rework count and cycle time. For rates, define "
                "numerator and denominator. For a count or duration, set Denominator=N/A and define Unit_or_Basis. Name the "
                "owner and improvement trigger for each. Add three lessons and one controlled improvement for the next cycle.",
                "Measure credibility and rework—not number of generated words. Count basis: reviewed change records. "
                "Cycle-time basis: elapsed calendar days from approved scope to publication archive.",
            ),
            (
                "After post-cycle-review.md is complete, update final-pack-index.md so it indexes the final calendar, board, "
                "data contracts, P-008 review records and post-cycle review as well as every approved artifact from Labs 1–7. "
                "Recheck file locations, versions, owners, reviewers, statuses, source IDs, open items and reopen triggers; "
                "then copy the final index into HLF-2025/final-pack.",
                "Final sequencing rule: post-cycle review first → final index update second → Start Here path verification last.",
            ),
        ],
        test=(
            "The calendar must contain all ten phases with owner, reviewer, entry criteria, output and escalation. "
            "data-contracts.md must cover all five evidence classes and versioned corrections. The workflow board must "
            "contain at least twelve tasks, allowed AI roles only, named human decisions and reopen triggers. The final pack "
            "must index every Lab 1–8 artifact, identify open items and give a reproducible Start Here path. The post-cycle "
            "review must define all five metrics with the rate numerator/denominator or count/duration Unit_or_Basis, "
            "owner and trigger. prompt-log.csv must contain P-008, and final-pack-index.md must be updated after the "
            "post-cycle review so every Lab 1–8 artifact is indexed."
        ),
        checkpoint=(
            "The final-pack folder is the course endpoint. A new preparer should be able to start with final-pack-index.md, "
            "locate every approved artifact, see all unresolved items and know which changes reopen earlier work."
        ),
        troubleshooting=[
            (
                "A workflow gate says 'data ready'.",
                "Replace it with observable criteria, required control results and an exception path."),
            (
                "The next-year process copies the prior narrative.",
                "Use prior wording only as a comparison source; reopen claims whenever data, boundary, factor, method or requirement changes."),
            (
                "An exception has no owner.",
                "Stop the affected task, assign an accountable owner and record an escalation date before continuing."),
        ],
        challenge=(
            "Create a RACI view from the workflow board and identify any stage where one person prepares, reviews and approves "
            "a high-risk item. Propose a proportionate segregation-of-duties improvement."
        ),
        reflection=(
            "Which reopen trigger is most important for preventing a fast but inaccurate next-year report?"
        ),
    ),
]
