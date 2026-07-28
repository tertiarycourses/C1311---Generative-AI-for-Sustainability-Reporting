"""Topic 1 labs for C1311."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Set the Reporting Boundary and AI Control Contract",
        duration=40,
        objective="LO1: establish a responsible, evidence-controlled generative AI reporting workflow",
        goal="Create the control files that keep every later AI-assisted task inside a defined reporting and evidence boundary.",
        workflow=["Define the basis", "Set AI controls", "Write the prompt contract", "Test and log"],
        desc=(
            "You will set up the synthetic HarbourLight Foods reporting workspace, define the reporting "
            "entity, period, audience and evidence boundary, and write an AI-use charter. You will then "
            "run one bounded transformation task and record the sources, output and human decision."
        ),
        build=(
            "A reporting-basis.md, ai-use-charter.md and prompt-log.csv that define scope, permitted data, "
            "prompt controls, review gates and a reproducible first AI-assisted task."
        ),
        services="Text editor · approved AI assistant · labs/assets/harbourlight-company-brief.md · source-pack-index.md",
        prerequisites=[
            "Create the HLF-2025/source, calculation, draft and review folders described in the Learner Guide.",
            "Open labs/assets/source-pack-index.md and labs/assets/harbourlight-company-brief.md.",
            "Use only the synthetic course files; do not paste workplace records into the class assistant.",
        ],
        steps=[
            (
                "Create reporting-basis.md. Record Entity, Reporting period, Reporting boundary, Primary audiences, "
                "Reporting purposes, Frameworks to investigate, Prepared by, Reviewed by and Unresolved questions. "
                "Use the company brief for facts and write MISSING for anything not supplied.",
                "Entity: HarbourLight Foods Pte Ltd\nReporting period: 1 January–31 December 2025\n"
                "Boundary: Singapore manufacturing and distribution sites listed in HLF-BRIEF-01\n"
                "Primary audiences: management, customers, investors and other affected stakeholders\n"
                "Rule: source ID, documented calculation, documented judgement or MISSING",
            ),
            (
                "Create ai-use-charter.md with five headings: Permitted tasks, Prohibited inputs, Required output controls, "
                "Human review gates and Recordkeeping. Under each heading add at least three specific rules. Include a rule "
                "that AI may structure, compare, draft or critique supplied evidence but may not invent a metric, factor, "
                "stakeholder view, applicability conclusion or approval.",
                "Required output controls:\n- cite supplied source IDs\n- preserve units and periods\n"
                "- label calculations and assumptions\n- write MISSING for unsupported fields\n"
                "- separate observed facts, interpretation and recommended follow-up",
            ),
            (
                "Create prompt-log.csv with columns Prompt_ID,Date,Model_or_Service,Purpose,Source_IDs,Input_Data_Class,"
                "Output_File,Reviewer,Decision,Decision_Reason. Add row P-001. Then write a six-part prompt in "
                "review/P-001-prompt.md using Goal, Context, Constraints, Sources, Output and Review.",
                "Goal: Extract the supplied company profile into a reporting-scope table.\n"
                "Context: This is a synthetic FY2025 sustainability-reporting exercise.\n"
                "Constraints: Use only HLF-BRIEF-01; preserve names and dates; write MISSING where silent.\n"
                "Sources: <PASTE HLF-BRIEF-01>\n"
                "Output: Field | Extracted value | Source ID | Status.\n"
                "Review: Flag any inferred boundary, audience or obligation.",
            ),
            (
                "Run P-001 in one approved AI assistant. Save the response as review/P-001-output.md. Compare every row "
                "with HLF-BRIEF-01, add a Human_check column, and mark each row SUPPORTED, REVISE or REMOVE. Update "
                "prompt-log.csv with the service name, output file, reviewer, final decision and a specific reason.",
                "Decision values: APPROVE · REVISE · STOP\n"
                "APPROVE only if every retained value is supported and all missing items remain visible.",
            ),
        ],
        test=(
            "Open the three control files. reporting-basis.md must state entity, FY2025 period, boundary, audiences, "
            "owners and unresolved questions. ai-use-charter.md must contain all five headings and at least fifteen "
            "specific rules. prompt-log.csv must contain P-001 with source HLF-BRIEF-01, output filename, reviewer, "
            "decision and reason. P-001-output.md must have no unsupported row marked SUPPORTED."
        ),
        checkpoint=(
            "Keep reporting-basis.md, ai-use-charter.md, prompt-log.csv and the P-001 files. If you need to rejoin, "
            "use these files as the reporting and AI-control boundary for Labs 2–8."
        ),
        troubleshooting=[
            (
                "The AI fills missing fields with plausible detail.",
                "Add 'write MISSING; do not infer or complete' to Constraints and rerun under a new prompt-log row.",
            ),
            (
                "The output contains no source IDs.",
                "Make Source ID a required column and reject any row that does not cite HLF-BRIEF-01.",
            ),
            (
                "The charter is generic.",
                "Replace words such as 'careful' with observable rules, named files, allowed statuses and review gates.",
            ),
        ],
        challenge=(
            "Add a risk rating from 1–3 to the prompt log. Define anchors based on data sensitivity, decision impact "
            "and ease of verification, then assign and justify the rating for P-001."
        ),
        reflection=(
            "Which control most reduced the chance that fluent language would be mistaken for reporting evidence, "
            "and what artifact proves that control operated?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Build the Framework and Materiality-Lens Register",
        duration=45,
        objective="LO1: distinguish GRI, SASB, TCFD and ISSB purposes and record current applicability",
        goal="Create a source-backed register that keeps framework purpose, audience, materiality lens and applicability distinct.",
        workflow=["Open official sources", "Classify the lenses", "Map reporting needs", "Critique and verify"],
        desc=(
            "You will inspect the supplied official-source links, complete a framework register for GRI, "
            "ISSB, SASB and TCFD, and add Singapore applicability checks. An AI assistant may compare "
            "the supplied summaries, but you will verify every retained statement against the official page."
        ),
        build=(
            "A framework-and-applicability-register.csv plus materiality-lenses.md showing purpose, audience, "
            "lens, requirement source, effective-date check, applicability owner and unresolved questions."
        ),
        services="Browser · spreadsheet · approved AI assistant · framework-starter-register.csv",
        prerequisites=[
            "Completed Lab 1 reporting basis and AI-use charter.",
            "Open labs/assets/framework-starter-register.csv and source-pack-index.md.",
            "Use the current official links in the starter register; do not rely on the model's memory of standards.",
        ],
        steps=[
            (
                "Time box: 12 minutes. Copy framework-starter-register.csv to framework-and-applicability-register.csv. "
                "The nine source rows already contain a short starter classification. In three pairs, assign three rows per "
                "pair, open each Official_URL, record the actual access date in Checked_Date, and verify or revise "
                "Current_Status, Audience, Materiality_Lens and Purpose_Summary. Working alone, verify one GRI row, one "
                "ISSB/SASB row, the TCFD row and one Singapore row; mark the other rows PENDING CHECK with an owner. "
                "For TCFD, record that the task force completed its work and that its recommendations are incorporated into IFRS S2.",
                "Required rows: GRI Universal Standards · GRI 3 · GRI Topic Standards · IFRS S1 · IFRS S2 · "
                "SASB Standards · TCFD bridge · SGX Rule 711B · Singapore requirements timeline",
            ),
            (
                "Time box: 6 minutes. Create materiality-lenses.md with a two-column comparison. Under Impact lens, record significant impacts "
                "on the economy, environment and people. Under Investor lens, record sustainability-related risks and "
                "opportunities that could affect the entity's prospects. Add a third section explaining that one evidence "
                "item may inform both lenses but needs a separate conclusion and rationale.",
                "Impact lens → evidence → significance judgement → GRI material topic\n"
                "Investor lens → risk/opportunity evidence → effects on prospects → ISSB material information",
            ),
            (
                "Time box: 8 minutes. Add five HarbourLight Reporting_Need rows using the supplied register columns: "
                "energy and emissions, packaging waste, worker safety, "
                "climate transition risk, and governance of sustainability information. For each, enter Candidate_Framework, "
                "Candidate_Requirement, Lens, Rationale, Applicability_Owner and Status. Use PENDING where the current evidence "
                "does not support a conclusion.",
                "Allowed Status values: CURRENT · PENDING · NOT APPLICABLE · NEEDS INTERPRETATION\n"
                "Never use a framework acronym alone as the rationale.",
            ),
            (
                "Time box: 10 minutes. Paste only the completed comparison fields—not the URLs alone—into the approved AI assistant. Ask it to find "
                "lens conflicts, missing requirement IDs, obsolete treatment of TCFD and unsupported applicability claims. "
                "Save the raw critique as review/P-002-framework-critique.md. The supplied register already contains "
                "Review_Result and Reviewer_Reason; complete both fields for every accepted or rejected suggestion. Add P-002 "
                "to prompt-log.csv with source IDs, output filename, reviewer, decision and decision reason.",
                "Return: Row_ID | Possible_issue | Official_source_to_check | Proposed_fix\n"
                "Do not declare compliance, conformity or legal applicability.",
            ),
            (
                "Time box: 5 minutes, leaving 4 minutes for the Test It check. Write a five-sentence framework-selection note below the materiality comparison. State which lenses HarbourLight "
                "will explore, what remains hypothetical in this course, why official requirements control, and which named owner "
                "must confirm jurisdiction and reporting basis before publication.",
                "Decision pattern: audience + lens + requirement + applicability owner + evidence status",
            ),
        ],
        test=(
            "The register must contain all nine required framework or jurisdiction rows, official URL, "
            "and either an actual checked date or PENDING CHECK with a named owner. Each row must have "
            "audience, lens, current-status note and owner. It must contain five HarbourLight reporting-need rows and no "
            "unsupported applicability claim marked CURRENT. materiality-lenses.md must keep the two lenses separate, "
            "explain shared evidence correctly and identify the owner of final applicability decisions. prompt-log.csv must "
            "contain P-002 and the register must record a reviewer result and reason for every AI-proposed change."
        ),
        checkpoint=(
            "Use framework-and-applicability-register.csv as the controlled requirements source in Labs 5 and 7. "
            "Rejoin by filtering Status to CURRENT or PENDING and retaining every official URL, P-002 record and reviewer reason."
        ),
        troubleshooting=[
            (
                "A framework row has no materiality lens.",
                "Return to its official purpose and audience; record impact, investor, jurisdiction-specific or guidance bridge.",
            ),
            (
                "The assistant describes TCFD as a new standalone standard.",
                "Replace the wording from the current IFRS Foundation TCFD page and retain the official link.",
            ),
            (
                "The register says a rule applies to HarbourLight.",
                "Change the status to PENDING until the entity scope, listing status and responsible owner confirm applicability.",
            ),
        ],
        challenge=(
            "Add Effective_From and Last_Changed columns. Define a quarterly review trigger and show how a changed official "
            "source would create a controlled follow-up rather than silently altering the report."
        ),
        reflection=(
            "Which pair of frameworks is most easily confused in an AI-generated answer, and what fields in your register "
            "prevent that confusion?"
        ),
    ),
]
