"""Single source of truth for C1311 courseware."""

TITLE = "Generative AI for Sustainability Reporting"
SHORT_TITLE = "Generative AI for Sustainability Reporting"
COURSE_CODE = "C1311"
COURSE_URL = "https://www.tertiarycourses.com.sg/generative-ai-for-sustainability-reporting.html"
VERSION = "v1.0"
VERSION_DATE = "28 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am – 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Establish a responsible, evidence-controlled generative AI workflow and distinguish the purposes of GRI, SASB, TCFD and ISSB reporting guidance.",
    "LO2: Structure ESG source data, calculate and interpret selected emissions and intensity metrics, and perform transparent materiality and gap analysis.",
    "LO3: Draft readable, evidence-grounded sustainability disclosures and executive summaries, then validate claims, consistency and limitations.",
    "LO4: Map report content to applicable frameworks, maintain an assurance-ready audit trail, and design a governed recurring reporting workflow.",
]

LO_TITLES = [
    "Ground & Govern",
    "Structure & Analyse",
    "Draft & Validate",
    "Map & Operationalise",
]


TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Generative AI for Sustainability Reporting",
        subtitle=(
            "ESG and sustainability reporting · AI-assisted work · reporting frameworks · "
            "prompt design · responsible and transparent use"
        ),
        weighting="Day 1 morning · 2 labs",
        concepts=[
            ("Reporting purpose", "Connect material impacts, risks and opportunities to decision-useful, traceable disclosures."),
            ("Framework lenses", "Use GRI for significant impacts and ISSB/SASB for investor-focused risks and opportunities; retain TCFD as a useful climate bridge."),
            ("Grounded generation", "Ask an AI assistant to transform supplied evidence, never to manufacture missing evidence."),
            ("Human accountability", "A named preparer reviews scope, calculations, claims, privacy, rights and applicability before use."),
            ("Prompt contract", "State goal, reporting context, constraints, sources, output schema and review tests."),
            ("Transparent use", "Record model, date, inputs, revisions, source links and final human decision."),
        ],
        sections=[
            dict(
                title="ESG, Sustainability Reporting and Generative AI",
                definition=(
                    "Sustainability reporting explains an organisation's material impacts, risks, "
                    "opportunities, governance, actions and performance. Generative AI is a drafting "
                    "and transformation aid within that process; it is not a source of corporate evidence."
                ),
                why=(
                    "Readers rely on reported information for decisions. A fluent AI response can hide "
                    "unsupported claims, boundary errors or omitted uncertainty unless the reporting team "
                    "keeps evidence and judgement separate from language generation."
                ),
                how=[
                    "Define the reporting objective, audience, period, entities and operational boundary.",
                    "Collect approved records and label observed facts, calculations, interpretations and unknowns.",
                    "Use AI for bounded tasks such as structuring, summarising, comparing or critiquing.",
                    "Verify every material statement and retain the approved evidence trail.",
                ],
                example=[
                    "HarbourLight Foods has electricity invoices, diesel records and a prior-year narrative.",
                    "The assistant organises those records into a disclosure outline and labels missing data.",
                    "The preparer calculates the metrics, confirms the boundary and approves the final wording.",
                ],
                use_when=[
                    "The task has a clear owner, approved evidence and a review checklist.",
                    "The output can be traced back to a source record or transparent calculation.",
                ],
                avoid_when=[
                    "The assistant would receive confidential or personal data outside approved controls.",
                    "The task asks the model to invent a figure, legal conclusion or assurance opinion.",
                ],
                quality=[
                    ("Failure signal", "The draft contains precise claims but no source identifiers or boundary statement."),
                    ("Repair move", "Add an evidence table, explicit unknown labels and a named human approval gate."),
                    ("Quality evidence", "Each material claim links to a record, calculation or documented judgement."),
                ],
            ),
            dict(
                title="Set Up AI Tools for Reporting",
                definition=(
                    "An AI reporting workspace combines an approved assistant, a synthetic or authorised source pack, "
                    "a structured working folder and a versioned log of prompts, outputs and human decisions."
                ),
                why=(
                    "Setup choices determine what data is exposed, whether work can be reproduced and whether later "
                    "reviewers can distinguish raw evidence from AI-generated working text."
                ),
                how=[
                    "Confirm approved tools, access controls, retention settings and prohibited data classes.",
                    "Create separate folders for sources, calculations, drafts, review notes and approved output.",
                    "Use stable source IDs and a prompt log with model, date, purpose and input references.",
                    "Test the workflow with synthetic data before introducing authorised organisational records.",
                ],
                example=[
                    "The team creates HLF-2025/source, calculation, draft and review folders.",
                    "Invoice INV-E-012 and factor EF-SG-2025-TRAINING remain referenced by stable IDs.",
                    "Prompt P-001 uses only synthetic extracts and the reviewer records APPROVE, REVISE or STOP.",
                ],
                use_when=[
                    "The organisation has approved the tool and defined its data-handling rules.",
                    "A reviewer can reproduce the task from saved source IDs and prompt instructions.",
                ],
                avoid_when=[
                    "Consumer accounts are used for restricted records without organisational approval.",
                    "Source files and generated drafts are mixed in one unversioned folder.",
                ],
                quality=[
                    ("Failure signal", "No one can tell which input or model produced a sentence."),
                    ("Repair move", "Introduce stable IDs, version names, a prompt log and separate source and draft areas."),
                    ("Quality evidence", "A second reviewer can reproduce the draft lineage without guessing."),
                ],
            ),
            dict(
                title="GRI, SASB, TCFD and ISSB at a Glance",
                definition=(
                    "GRI focuses on an organisation's most significant impacts on the economy, environment and people. "
                    "ISSB Standards establish an investor-focused baseline; SASB supplies industry-based topics and metrics. "
                    "TCFD's governance, strategy, risk management, and metrics-and-targets architecture is incorporated into IFRS S2."
                ),
                why=(
                    "Framework names are not interchangeable. Selecting a disclosure only because an AI response mentioned "
                    "a familiar acronym can create materiality, audience and completeness errors."
                ),
                how=[
                    "Identify the reporting audience, jurisdiction, applicable rules and stated reporting basis.",
                    "Apply the relevant materiality lens before selecting disclosures or metrics.",
                    "Use official standards and current applicability guidance as the requirements register.",
                    "Map one evidence item to multiple requirements only where definitions and boundaries genuinely align.",
                ],
                example=[
                    "Water stress may be significant as an impact under GRI even when it is not financially material.",
                    "A climate transition risk may be material to investors under IFRS S1 and IFRS S2.",
                    "A food-sector SASB metric can add industry specificity while the TCFD architecture supports transition to IFRS S2.",
                ],
                use_when=[
                    "Building a framework register or explaining why a disclosure belongs in the report.",
                    "Reconciling impact-focused and investor-focused information without merging their tests.",
                ],
                avoid_when=[
                    "Declaring broad compliance from a keyword match or incomplete checklist.",
                    "Treating TCFD as an additional current layer where IFRS S2 already covers it, unless a rule still requires it.",
                ],
                quality=[
                    ("Failure signal", "The framework column contains several acronyms but no requirement IDs or rationale."),
                    ("Repair move", "Record audience, lens, official source, requirement identifier and applicability decision."),
                    ("Quality evidence", "Every mapping explains both why the item is relevant and what evidence supports it."),
                ],
            ),
            dict(
                title="Effective Prompting and Responsible, Transparent AI Use",
                definition=(
                    "A reporting prompt is a controlled work instruction containing a goal, context, constraints, "
                    "source boundaries, output schema and review criteria. Transparent use records the assistant's role "
                    "and the human checks that converted working text into approved content."
                ),
                why=(
                    "Generic prompts reward plausible prose. A structured prompt and adversarial review make missing "
                    "evidence, inconsistent units, unsupported causal language and invented requirements easier to detect."
                ),
                how=[
                    "State one task, audience, reporting period and intended decision.",
                    "Paste or reference only approved source extracts and forbid unsupported completion.",
                    "Require a structured output with claim, source, confidence and unresolved-question fields.",
                    "Run a separate critique prompt, then verify the critique against the original evidence.",
                ],
                example=[
                    "Goal: draft a 150-word energy disclosure for FY2025 using sources HLF-E01 to HLF-E06.",
                    "Constraint: preserve units, label calculated values and write MISSING where evidence is absent.",
                    "Review: return a claim ledger and flag wording that implies causation, certainty or compliance.",
                ],
                use_when=[
                    "Drafting, restructuring or reviewing content from a bounded evidence pack.",
                    "The output format exposes uncertainty and supports line-by-line verification.",
                ],
                avoid_when=[
                    "The prompt asks for a current legal or standards conclusion without checking the official source.",
                    "The model is asked to conceal its role or remove known caveats to sound more confident.",
                ],
                quality=[
                    ("Failure signal", "The answer is polished but fills evidence gaps silently."),
                    ("Repair move", "Require MISSING labels, a claim ledger and an independent human source check."),
                    ("Quality evidence", "Uncertainty remains visible and all accepted claims survive source verification."),
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="AI for ESG Data Collection and Analysis",
        subtitle=(
            "Source registers · data dictionaries · metric calculations · emissions boundaries · "
            "materiality · gap analysis · charts and summaries"
        ),
        weighting="Day 1 afternoon · 3 labs",
        concepts=[
            ("Evidence register", "Track source owner, period, boundary, unit, status and location before analysis."),
            ("Data dictionary", "Define each field, unit, allowed value, calculation and missing-data treatment."),
            ("Calculation lineage", "Preserve activity data, factor source, formula, unit conversion and reviewer."),
            ("Materiality lenses", "Assess significant impacts separately from investor-focused risks and opportunities."),
            ("Gap status", "Distinguish complete, partial, missing, not applicable and pending verification."),
            ("Visual integrity", "Use consistent denominators, labelled units, honest scales and visible limitations."),
        ],
        sections=[
            dict(
                title="Gather and Structure ESG Data with AI",
                definition=(
                    "ESG data collection turns heterogeneous records into a controlled dataset with stable identifiers, "
                    "defined fields, consistent units, reporting boundaries and visible evidence status."
                ),
                why=(
                    "AI can extract or normalise repeated fields quickly, but unreviewed extraction may change units, "
                    "merge entities, duplicate records or convert blanks into invented values."
                ),
                how=[
                    "Inventory source records and assign source, entity, site, period and owner identifiers.",
                    "Define a data dictionary before asking AI to extract or transform values.",
                    "Require raw value, raw unit, normalised value, normalised unit and transformation note.",
                    "Validate totals, duplicates, ranges and missing fields against the original records.",
                ],
                example=[
                    "Three sites provide electricity in kWh, MWh and invoice line-item extracts.",
                    "The target schema normalises energy to kWh while retaining raw values and source pages.",
                    "A pivot check compares extracted totals with invoice totals and flags one duplicate month.",
                ],
                use_when=[
                    "The source set is bounded and the extraction schema is explicit.",
                    "A human can sample and reconcile extracted values to original records.",
                ],
                avoid_when=[
                    "Scanned records are unreadable or the model cannot preserve page-level provenance.",
                    "The workflow overwrites raw values or discards missing-data reasons.",
                ],
                quality=[
                    ("Failure signal", "Normalised values exist without raw values or transformation notes."),
                    ("Repair move", "Restore immutable raw columns, units, source IDs and reconciliation checks."),
                    ("Quality evidence", "A reviewer can trace every reported number to the original record and conversion."),
                ],
            ),
            dict(
                title="Calculate and Interpret Metrics and Emissions",
                definition=(
                    "A sustainability metric combines a precisely defined numerator, denominator, boundary, period and unit. "
                    "A basic greenhouse-gas calculation multiplies activity data by an appropriate emission factor and converts units consistently."
                ),
                why=(
                    "Seemingly small choices—scope, factor year, consolidation boundary, denominator or rounding—can materially "
                    "change a trend and make year-on-year comparison misleading."
                ),
                how=[
                    "Confirm organisational and operational boundaries plus the metric definition.",
                    "Validate activity units and select a documented factor with geography, year and source.",
                    "Calculate result = activity data × factor × unit conversion and retain each component.",
                    "Review totals, intensity denominators, trend drivers, estimation status and restatements.",
                ],
                example=[
                    "520,000 kWh × 0.408 kg CO2e/kWh = 212,160 kg CO2e, or 212.16 tCO2e.",
                    "Revenue intensity = total tCO2e ÷ S$ million revenue, using the same reporting period.",
                    "The narrative states that the electricity factor is a synthetic training value, not an official inventory factor.",
                ],
                use_when=[
                    "Inputs, factors, conversions and boundaries are documented and reviewed.",
                    "Comparisons use consistent periods and explain any recalculation or estimation.",
                ],
                avoid_when=[
                    "A model supplies an emission factor without an authoritative, current source.",
                    "An intensity improvement is presented without also checking the absolute metric and denominator change.",
                ],
                quality=[
                    ("Failure signal", "A result has no unit, factor version, boundary or calculation trail."),
                    ("Repair move", "Rebuild the calculation table from activity data through conversion to final metric."),
                    ("Quality evidence", "The figure recalculates exactly and its comparison basis is explicit."),
                ],
            ),
            dict(
                title="Conduct Materiality and Gap Analysis",
                definition=(
                    "Materiality analysis prioritises significant impacts and/or sustainability-related risks and opportunities "
                    "using the stated reporting lens. Gap analysis compares required or chosen disclosures with available evidence."
                ),
                why=(
                    "AI can cluster evidence and surface candidate topics, but it cannot replace stakeholder engagement, "
                    "management judgement, legal applicability decisions or the documented basis for prioritisation."
                ),
                how=[
                    "Record candidate topics, evidence, affected stakeholders and the reporting lens.",
                    "Score impact significance and investor relevance separately using defined anchors.",
                    "Map priority topics to requirements and classify evidence as complete, partial, missing or not applicable.",
                    "Review thresholds, outliers, omitted sector topics and management decisions.",
                ],
                example=[
                    "Packaging waste scores high for environmental impact while energy price volatility scores high for financial effect.",
                    "The framework register shows complete energy data but only partial supplier-screening evidence.",
                    "The decision log records the threshold, reviewer and reason for each included or deferred item.",
                ],
                use_when=[
                    "Scoring anchors are written before scoring and evidence remains attached to each judgement.",
                    "The output supports a decision log rather than claiming to automate materiality.",
                ],
                avoid_when=[
                    "One combined score hides the difference between impact and financial materiality.",
                    "Stakeholder views or sector guidance are generated instead of collected and verified.",
                ],
                quality=[
                    ("Failure signal", "Every topic is labelled material with identical reasoning."),
                    ("Repair move", "Separate lenses, define scoring anchors and allow evidence-based non-priority decisions."),
                    ("Quality evidence", "A reviewer can reproduce the ranking and challenge each judgement."),
                ],
            ),
            dict(
                title="Visualise and Summarise ESG Data",
                definition=(
                    "A reporting visual encodes a defined metric across time, entity or category so a reader can compare values "
                    "without losing units, denominators, boundaries or uncertainty."
                ),
                why=(
                    "Charts compress complex data, which also makes them capable of hiding denominator shifts, missing periods, "
                    "inconsistent scales and estimation changes."
                ),
                how=[
                    "Choose the decision and comparison before choosing a chart type.",
                    "Validate tidy data, units, ordering, baselines and missing-value treatment.",
                    "Use a descriptive title, direct labels, source note and concise limitation.",
                    "Write a summary that separates observation, interpretation and recommended follow-up.",
                ],
                example=[
                    "A two-year bar chart shows absolute Scope 1 and Scope 2 tCO2e by year.",
                    "A small companion table shows revenue and tCO2e per S$ million to expose denominator effects.",
                    "The summary notes the observed change and asks for operations evidence before assigning a cause.",
                ],
                use_when=[
                    "The visual materially improves comparison and all plotted fields share a coherent grain.",
                    "Readers can see units, time period, boundary, source and limitations.",
                ],
                avoid_when=[
                    "A decorative chart replaces a short table or implies precision unsupported by the data.",
                    "A causal explanation is generated from correlation or two aggregated points.",
                ],
                quality=[
                    ("Failure signal", "The chart has a clever title but no unit, boundary or source note."),
                    ("Repair move", "Restore neutral labelling, units, data notes and a separate interpretation sentence."),
                    ("Quality evidence", "The visual and source table reconcile exactly and support the same conclusion."),
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="AI for Drafting and Structuring Reports",
        subtitle=(
            "Evidence-grounded narrative · executive summaries · report architecture · "
            "tone and readability · claim validation"
        ),
        weighting="Day 2 morning · 1 lab",
        concepts=[
            ("Disclosure logic", "State boundary and method before performance, interpretation, actions and limitations."),
            ("Claim ledger", "Link every quantitative and material qualitative claim to evidence and review status."),
            ("Connected information", "Keep governance, strategy, risks, metrics, targets and financial effects coherent."),
            ("Plain language", "Prefer precise verbs, defined terms, short sentences and visible uncertainty."),
            ("Consistency controls", "Lock names, periods, units, totals, targets, baselines and framework references."),
            ("Fact-check loop", "Extract claims, verify sources and calculations, repair or remove unsupported wording."),
        ],
        sections=[
            dict(
                title="Draft Narrative Disclosures and Executive Summaries",
                definition=(
                    "A disclosure narrative converts verified evidence into a balanced account of context, method, performance, "
                    "actions and limitations. An executive summary selects only the most decision-relevant messages."
                ),
                why=(
                    "AI is useful for structure and variation, but it tends to smooth over caveats and make ordinary changes sound "
                    "strategic. A source-led outline prevents language quality from outrunning evidence quality."
                ),
                how=[
                    "Create an evidence table and disclosure outline before asking for prose.",
                    "Draft one section at a time with source IDs embedded in the working version.",
                    "Require balanced treatment of positive, negative and uncertain information.",
                    "Reduce the approved sections into an executive summary without adding new claims.",
                ],
                example=[
                    "The energy section states boundary, method, absolute result, intensity result and limitation.",
                    "A decrease is described as observed; its cause remains unconfirmed pending operations evidence.",
                    "The executive summary reuses approved claims and includes one priority data gap.",
                ],
                use_when=[
                    "The evidence table is complete enough to support the intended claims.",
                    "A human editor owns materiality, balance and final wording.",
                ],
                avoid_when=[
                    "The prompt asks for a complete report before framework mapping and data validation.",
                    "Positive tone is used to remove adverse results, uncertainty or missed targets.",
                ],
                quality=[
                    ("Failure signal", "The narrative contains strategy claims that do not appear in source records."),
                    ("Repair move", "Return to the evidence table and delete, qualify or source every unsupported claim."),
                    ("Quality evidence", "The executive summary contains no claim absent from approved disclosures."),
                ],
            ),
            dict(
                title="Structure Reports and Sections with AI",
                definition=(
                    "Report structure is the intentional hierarchy that connects reporting basis, governance, strategy, "
                    "material topics, performance, targets, methods and reference indexes."
                ),
                why=(
                    "A long generated table of contents can duplicate content or separate metrics from their methods. "
                    "A requirements-to-section map makes structure serve coverage and reader navigation."
                ),
                how=[
                    "List audiences, reporting basis, frameworks and applicable requirements.",
                    "Group disclosures by decision purpose and define one owner for each section.",
                    "Map every requirement to a section, evidence set and review gate.",
                    "Use AI to test navigation, duplication and missing connections, then decide manually.",
                ],
                example=[
                    "Governance and strategy appear once, with cross-references from material topic sections.",
                    "Metric tables include basis, boundary and methods immediately before the results.",
                    "The GRI content index and ISSB cross-reference table point to approved sections.",
                ],
                use_when=[
                    "The structure is driven by requirements and reader questions rather than generated headings.",
                    "Cross-references can be maintained without duplicating inconsistent claims.",
                ],
                avoid_when=[
                    "The assistant invents a generic report architecture before applicability is established.",
                    "The same target or metric is restated differently in several sections.",
                ],
                quality=[
                    ("Failure signal", "A requirement maps to multiple sections with different owners and values."),
                    ("Repair move", "Assign a canonical source and one approved statement, then cross-reference it."),
                    ("Quality evidence", "Each requirement, section, owner and evidence set has a single current status."),
                ],
            ),
            dict(
                title="Ensure Consistency, Tone and Readability",
                definition=(
                    "Consistency control checks facts, terminology, units, periods, targets and narrative stance across the report. "
                    "Readability makes complex information understandable without removing necessary precision."
                ),
                why=(
                    "Large reports are edited by many people. AI can detect differences, but it can also standardise away "
                    "important distinctions or introduce a preferred term that changes a defined meaning."
                ),
                how=[
                    "Create a style sheet for names, acronyms, units, tense, dates and approved terminology.",
                    "Extract repeated facts and compare them against the canonical data table.",
                    "Rewrite for sentence length, active voice and defined technical terms without changing meaning.",
                    "Run a final contradiction and cross-reference review after layout changes.",
                ],
                example=[
                    "The style sheet specifies tCO2e, FY2025 and 'HarbourLight Foods Pte Ltd'.",
                    "A consistency check finds 212.16 tCO2e in the table but 221 tCO2e in the summary.",
                    "The editor corrects the summary from the approved calculation, not from the AI suggestion.",
                ],
                use_when=[
                    "Canonical facts and terminology are available for comparison.",
                    "The editor can compare original and revised meaning line by line.",
                ],
                avoid_when=[
                    "A 'make this stronger' prompt encourages promotional or absolute claims.",
                    "Readability edits remove boundaries, assumptions or material caveats.",
                ],
                quality=[
                    ("Failure signal", "The same metric appears with different values, units or periods."),
                    ("Repair move", "Link every repetition to a canonical source and rerun contradiction checks."),
                    ("Quality evidence", "All repeated facts reconcile and the plain-language version preserves limitations."),
                ],
            ),
            dict(
                title="Fact-Check and Validate AI Output",
                definition=(
                    "Validation decomposes AI output into checkable claims and tests each one against source evidence, calculations, "
                    "current official requirements and the intended reporting boundary."
                ),
                why=(
                    "An AI response may contain confabulated facts, inaccurate citations, outdated requirements or unjustified causation. "
                    "Reviewing overall plausibility is not enough."
                ),
                how=[
                    "Extract quantitative, qualitative, framework, comparative and causal claims into a ledger.",
                    "Verify each claim against the original source, calculation or current official requirement.",
                    "Mark supported, revise, remove, unresolved or not applicable and record the reviewer.",
                    "Run targeted checks for totals, units, dates, names, targets, citations and causal language.",
                ],
                example=[
                    "Claim C-014 states emissions fell because of equipment upgrades.",
                    "The dataset confirms the fall, but no source record confirms the cause.",
                    "The reviewer changes the wording to an observation and logs the cause as unresolved.",
                ],
                use_when=[
                    "The output can be decomposed into claims and relevant evidence is accessible.",
                    "A separate reviewer can challenge high-impact or high-uncertainty items.",
                ],
                avoid_when=[
                    "The same model is treated as the sole judge of its own accuracy.",
                    "A citation is accepted because its title looks credible without opening the source.",
                ],
                quality=[
                    ("Failure signal", "The review says 'looks accurate' without claim-level status."),
                    ("Repair move", "Build a claim ledger and prioritise quantitative, compliance and causal claims."),
                    ("Quality evidence", "Every retained material claim has a source, reviewer, status and resolution."),
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="AI for Compliance, Frameworks and Continuous Reporting",
        subtitle=(
            "Framework crosswalks · current applicability · assurance readiness · governance · "
            "recurring and multi-year workflows"
        ),
        weighting="Day 2 afternoon · 2 labs",
        concepts=[
            ("Applicability register", "Record entity scope, jurisdiction, framework basis, effective date and source owner."),
            ("Requirement crosswalk", "Map identifiers to report sections, evidence, owner and status without claiming more than supported."),
            ("Audit trail", "Retain source, transformation, calculation, prompt, review and approval lineage."),
            ("Segregation of duties", "Separate preparer, reviewer and approver for material claims and calculations."),
            ("Change control", "Detect changes in data, factors, methods, requirements and approved narrative."),
            ("Recurring workflow", "Use a calendar, data contracts, controlled templates, quality gates and post-cycle improvement."),
        ],
        sections=[
            dict(
                title="Map Content to GRI, SASB, TCFD and ISSB",
                definition=(
                    "A framework crosswalk records each requirement or guidance item, why it applies, where it is addressed, "
                    "which evidence supports it and what status remains."
                ),
                why=(
                    "AI can accelerate comparisons, but keyword similarity is not compliance. Definitions, materiality, industry, "
                    "effective dates and jurisdiction determine whether a mapping is valid."
                ),
                how=[
                    "Create a current register from official sources with identifiers, dates and applicability notes.",
                    "Map report claims and sections to requirements using exact evidence references.",
                    "Classify status as complete, partial, missing, not applicable or pending interpretation.",
                    "Have the responsible owner review mappings and avoid unsupported statements of conformity.",
                ],
                example=[
                    "GRI 3 supports the documented process for determining impact material topics.",
                    "IFRS S1 and S2 use governance, strategy, risk management, and metrics-and-targets content areas.",
                    "A SASB food-industry topic adds industry detail; TCFD is recorded as a legacy bridge incorporated into IFRS S2.",
                ],
                use_when=[
                    "Official sources, applicability decisions and requirement IDs are recorded.",
                    "The crosswalk is a working control with owners and evidence statuses.",
                ],
                avoid_when=[
                    "A generated checklist substitutes for reading the applicable standard or rule.",
                    "The report claims alignment or conformity when required items remain partial or missing.",
                ],
                quality=[
                    ("Failure signal", "Mappings contain page numbers but no evidence or applicability rationale."),
                    ("Repair move", "Add requirement ID, lens, official source, owner, evidence and status."),
                    ("Quality evidence", "A reviewer can trace each mapping and see unresolved items immediately."),
                ],
            ),
            dict(
                title="Build Assurance-Ready Audit Trails and Governance",
                definition=(
                    "Assurance readiness means evidence, methods, controls, roles and changes are documented so an independent reviewer "
                    "can understand how a reported statement was produced."
                ),
                why=(
                    "AI introduces another transformation layer. Without logs, version control and approval records, a team may be unable "
                    "to reproduce a calculation or explain why generated wording was accepted."
                ),
                how=[
                    "Assign preparer, reviewer, approver and requirement owners with clear handoffs.",
                    "Retain immutable sources, calculation workpapers, prompt logs, claim ledgers and approvals.",
                    "Apply access control, version naming, change reasons and exception management.",
                    "Test high-risk samples for completeness, accuracy, occurrence, consistency and cut-off.",
                ],
                example=[
                    "Metric M-008 links to invoices, factor EF-03, calculation CALC-02 and reviewer sign-off REV-17.",
                    "Draft D-04 links each retained sentence to claim-ledger rows and an approval record.",
                    "A changed factor triggers recalculation, narrative review and a documented restatement decision.",
                ],
                use_when=[
                    "Material metrics and claims need reproducible lineage and independent review.",
                    "The team wants to reduce late-cycle evidence requests and rework.",
                ],
                avoid_when=[
                    "AI logs contain restricted source data that should not be retained in that system.",
                    "Approval is implied by silence or performed by the same person for every high-risk item.",
                ],
                quality=[
                    ("Failure signal", "The final report exists but its working papers cannot reproduce key figures."),
                    ("Repair move", "Reconstruct lineage from source through calculation, draft, review and approval."),
                    ("Quality evidence", "A reviewer can select a claim and follow its complete evidence chain."),
                ],
            ),
            dict(
                title="Automate Recurring and Multi-Year Reporting",
                definition=(
                    "Recurring reporting uses controlled templates, data contracts, calendars and exception workflows to repeat stable tasks "
                    "while preserving human review for material judgement and change."
                ),
                why=(
                    "Copying last year's report carries forward stale claims and methods. Uncontrolled automation can reproduce errors faster "
                    "and conceal changes in boundaries, factors or requirements."
                ),
                how=[
                    "Separate repeatable data transformations from judgement-intensive reporting decisions.",
                    "Define input owners, due dates, schemas, validations, approvals and escalation rules.",
                    "Compare current and prior periods for boundary, factor, method, target and requirement changes.",
                    "Generate drafts only after data gates pass, then preserve review and publication controls.",
                ],
                example=[
                    "Monthly source files load into a locked schema with duplicate and range checks.",
                    "The annual close flags new sites, factor changes and restatement triggers before trend calculations.",
                    "AI drafts variance commentary from approved data, while owners verify explanations and actions.",
                ],
                use_when=[
                    "Inputs are standardised, controls are testable and exceptions have named owners.",
                    "The process keeps human approval for materiality, estimates, causal claims and publication.",
                ],
                avoid_when=[
                    "The workflow republishes prior narrative without current evidence.",
                    "Automation is introduced before definitions, ownership and quality gates are stable.",
                ],
                quality=[
                    ("Failure signal", "The process is fast but no one owns rejected records or changed requirements."),
                    ("Repair move", "Add exception queues, owners, service levels and change-control gates."),
                    ("Quality evidence", "The cycle is repeatable, exceptions are visible and all published changes are approved."),
                ],
            ),
            dict(
                title="Build an Efficient Sustainability Reporting Workflow",
                definition=(
                    "An efficient workflow sequences scoping, evidence intake, calculation, materiality, drafting, framework mapping, review, "
                    "approval and publication so defects are caught near their source."
                ),
                why=(
                    "Late reconciliation is expensive. Efficiency comes from clear entry criteria and controls, not from generating more text "
                    "earlier in the cycle."
                ),
                how=[
                    "Plan the reporting basis, applicability, roles, calendar and source inventory.",
                    "Validate data and calculations before narrative work begins.",
                    "Use AI in bounded stages with prompt logs, claim ledgers and reviewer gates.",
                    "Close with cross-report reconciliation, approvals, publication archive and lessons learned.",
                ],
                example=[
                    "HarbourLight's eight-stage board assigns one owner, entry gate and output to each stage.",
                    "A missing energy invoice blocks the metric and narrative but not unrelated governance sections.",
                    "The post-cycle review converts recurring defects into next-year data-contract improvements.",
                ],
                use_when=[
                    "The team needs an end-to-end operating model and clear handoffs.",
                    "Management wants transparent status, exceptions and evidence readiness.",
                ],
                avoid_when=[
                    "A single AI prompt is expected to perform data validation, materiality, drafting and sign-off.",
                    "Speed is measured only by draft completion rather than rework, evidence gaps and review findings.",
                ],
                quality=[
                    ("Failure signal", "Drafting begins while scope, data owners or framework basis remain undecided."),
                    ("Repair move", "Introduce entry gates and stop affected work until foundational decisions are recorded."),
                    ("Quality evidence", "Each stage has an owner, input, control, output, status and escalation path."),
                ],
            ),
        ],
    ),
]


DAY_THEMES = {
    1: "Ground the AI workflow and turn ESG evidence into trustworthy metrics",
    2: "Turn verified evidence into framework-mapped, review-ready reporting",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:45", 15, "admin", "Welcome, course orientation and responsible-use ground rules"),
                ("9:45", "10:25", 40, "topic", "Topic 1 — Reporting purpose, AI roles and evidence boundaries"),
                ("10:25", "11:05", 40, "lab", "Hands-on: " + lab_titles([1])),
                ("11:05", "11:20", 15, "break", "Tea break"),
                ("11:20", "12:00", 40, "topic", "Topic 1 — Framework lenses, prompting and transparent AI use"),
                ("12:00", "12:45", 45, "lab", "Hands-on: " + lab_titles([2])),
                ("12:45", "13:00", 15, "recap", "Topic 1 recap mapped to LO1"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "14:45", 45, "topic", "Topic 2 — Evidence registers, data dictionaries and collection controls"),
                ("14:45", "15:35", 50, "lab", "Hands-on: " + lab_titles([3])),
                ("15:35", "15:50", 15, "break", "Tea break"),
                ("15:50", "16:30", 40, "topic", "Topic 2 — Metrics, emissions, materiality, gaps and visual integrity"),
                ("16:30", "17:25", 55, "lab", "Hands-on: " + lab_titles([4])),
                ("17:25", "18:15", 50, "lab", "Hands-on: " + lab_titles([5])),
                ("18:15", "18:30", 15, "recap", "Day 1 integrated recap mapped to LO1 and LO2"),
            ],
        ),
        2: (
            DAY_THEMES[2],
            [
                ("9:30", "9:45", 15, "admin", "Day 1 retrieval practice and Day 2 reporting brief"),
                ("9:45", "10:30", 45, "topic", "Topic 3 — Evidence-led narrative and executive-summary logic"),
                ("10:30", "11:30", 60, "lab", "Hands-on: " + lab_titles([6])),
                ("11:30", "11:45", 15, "break", "Tea break"),
                ("11:45", "12:30", 45, "topic", "Topic 3 — Structure, connected information, tone and readability"),
                ("12:30", "13:00", 30, "topic", "Topic 3 — Claim-level fact-check and validation demonstration"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "14:45", 45, "topic", "Topic 4 — Framework crosswalks and current applicability"),
                ("14:45", "15:40", 55, "lab", "Hands-on: " + lab_titles([7])),
                ("15:40", "15:55", 15, "break", "Tea break"),
                ("15:55", "16:40", 45, "topic", "Topic 4 — Assurance readiness, governance and change control"),
                ("16:40", "17:35", 55, "lab", "Hands-on: " + lab_titles([8])),
                ("17:35", "18:15", 40, "topic", "Topic 4 — Recurring workflow, Singapore applicability and continuous improvement"),
                ("18:15", "18:30", 15, "recap", "Course integration, action plan and Q&A mapped to all outcomes"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="The Evidence-Controlled AI Reporting System",
    concepts_title="Six Ideas That Keep Reporting Credible",
    concepts=[
        ("Reporting basis", "Audience, period, boundary, materiality lens, framework and applicability."),
        ("Evidence first", "Stable source IDs, raw values, owners, status and immutable originals."),
        ("Transparent calculations", "Activity data, factor, formula, conversion, result and reviewer."),
        ("Bounded AI tasks", "Transform, compare, draft or critique supplied evidence—one controlled task at a time."),
        ("Human judgement", "People decide materiality, applicability, estimates, balance and publication."),
        ("Reproducible lineage", "Source → transformation → calculation → claim → review → approval."),
    ],
    framework_title="The Eight-Stage Reporting Workflow",
    framework=[
        ("1 · Scope", "Define reporting basis, boundary, audience and applicability."),
        ("2 · Register", "Inventory sources, owners, periods, units and evidence status."),
        ("3 · Structure", "Normalise data while retaining raw values and provenance."),
        ("4 · Calculate", "Apply documented methods, factors, conversions and checks."),
        ("5 · Prioritise", "Assess materiality and framework gaps with explicit anchors."),
        ("6 · Draft", "Generate source-led sections and claim ledgers."),
        ("7 · Review", "Reconcile claims, mappings, controls and approvals."),
        ("8 · Publish", "Archive the evidence pack and improve the next cycle."),
    ],
    statement=dict(
        headline="AI accelerates reporting work. It does not own the evidence, judgement or conclusion.",
        body="Credibility comes from traceable sources, transparent calculations, current requirements and accountable human review.",
        kicker="OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Controlled evidence", ["AI use charter and prompt log", "Framework and applicability register", "Structured ESG dataset and data dictionary"]),
        ("Verified reporting", ["Emissions and intensity workpaper", "Materiality and gap matrix", "Disclosure draft and claim ledger"]),
        ("Repeatable governance", ["Framework crosswalk", "Assurance evidence index", "Recurring reporting workflow board"]),
    ],
    arc_title="The Review Loop Used in Every Lab",
    arc=[
        "Ground the task in synthetic evidence and an explicit reporting boundary.",
        "Ask for a structured transformation, calculation check, draft or critique.",
        "Compare output with original sources, formulas and current official requirements.",
        "Record unresolved items and make the human decision to approve, revise or stop.",
        "Carry the versioned artifact and evidence trail into the next lab.",
    ],
    deep_dives=[
        dict(
            title="Keep the Materiality Lenses Separate",
            kicker="TWO QUESTIONS · TWO EVIDENCE TESTS",
            items=[
                ("Impact lens", "Which impacts on the economy, environment and people are most significant?"),
                ("Investor lens", "Which sustainability-related risks and opportunities could affect the entity's prospects?"),
                ("Shared evidence", "One source may inform both lenses, but each conclusion needs its own rationale."),
                ("Documented judgement", "Thresholds, stakeholders, owners and decisions remain visible."),
            ],
        ),
        dict(
            title="The Reporting Evidence Chain",
            kicker="FROM RECORD TO APPROVED CLAIM",
            items=[
                ("Source", "Original record, owner, date, period, boundary and stable identifier."),
                ("Transformation", "Extraction, normalisation and missing-data treatment."),
                ("Calculation", "Formula, factor, conversion, result and independent check."),
                ("Claim", "Draft statement linked to evidence, limitation and framework mapping."),
                ("Approval", "Named reviewer, resolution, date and final version."),
            ],
        ),
    ],
)


LG_INTRO = (
    "This Learner Guide accompanies Generative AI for Sustainability Reporting (C1311). "
    "It teaches the reporting concepts behind eight connected labs before presenting the practical workflow. "
    "The four-topic sequence matches the published course outline and uses the synthetic HarbourLight Foods scenario."
)
LG_INTRO2 = (
    "Work through the labs in order. Treat every AI output as working material: preserve source IDs, "
    "recalculate metrics, verify official requirements and record the human decision. The framework summaries "
    "support learning but do not replace the current standards or jurisdiction-specific professional advice."
)

LG_SETUP = dict(
    needs=[
        "A laptop with a spreadsheet application and text editor.",
        "Access to one organisation-approved generative AI assistant such as ChatGPT, Claude or Gemini.",
        "The synthetic files in labs/assets; do not substitute confidential organisational records during class.",
        "A browser for opening the current official framework sources listed in the guide.",
    ],
    verify_text=(
        "Create a working folder named HLF-2025 with source, calculation, draft and review subfolders. "
        "Open the synthetic CSV files without changing their raw columns, and confirm that your AI assistant can return a Markdown table."
    ),
    verify_code=(
        "HLF-2025/\n"
        "  source/\n"
        "  calculation/\n"
        "  draft/\n"
        "  review/"
    ),
    conventions=[
        "Use source IDs exactly as supplied and write MISSING when evidence is absent.",
        "Keep raw values and normalised values in separate columns.",
        "Record every factor, formula, unit conversion, reviewer and version.",
        "Use synthetic training factors only for the class calculations; obtain current approved factors for real reporting.",
        "Never paste restricted data, credentials or personal information into an unapproved service.",
    ],
)

LAB_NOTE = (
    "Use only the synthetic HarbourLight Foods data supplied with this course. "
    "For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, "
    "and verify current official requirements and emission factors."
)

LG_WRAPUP = dict(
    title="Wrap-Up and Authoritative Reference Set",
    intro=(
        "The workflow is complete when the reporting pack can be traced from each retained claim back to an approved source, "
        "calculation or documented judgement. Recheck the official sources whenever applicability, effective dates or methods may have changed."
    ),
    sections=[
        dict(
            title="Final quality gate",
            bullets=[
                "Reporting basis, entities, period, boundaries and materiality lens are explicit.",
                "Metrics recalculate from retained activity data, factor sources, formulas and conversions.",
                "Every material claim has a source, status, reviewer and resolution.",
                "Framework mappings use current official identifiers and recorded applicability decisions.",
                "AI use, limitations, revisions and human approvals are transparent.",
            ],
        ),
        dict(
            title="Primary sources used to prepare this course (accessed 28 July 2026)",
            bullets=[
                "GRI Standards and Universal Standards: https://www.globalreporting.org/standards/",
                "GRI 3: Material Topics 2021: https://www.globalreporting.org/publications/documents/english/gri-3-material-topics-2021/",
                "ISSB and IFRS Sustainability Disclosure Standards: https://www.ifrs.org/sustainability/knowledge-hub/introduction-to-issb-and-ifrs-sustainability-disclosure-standards/",
                "SASB Standards under ISSB stewardship: https://www.ifrs.org/issued-standards/sasb-standards/",
                "ISSB and the completed TCFD work: https://www.ifrs.org/sustainability/tcfd/",
                "GHG Protocol Corporate Standard FAQ: https://ghgprotocol.org/corporate-standard-frequently-asked-questions",
                "NIST AI 600-1 Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence",
                "Singapore sustainability reporting requirements: https://www.acra.gov.sg/regulations/sustainability-reporting/requirements-timeline/",
                "SGX Rule 711B Sustainability Report: https://rulebook.sgx.com/rulebook/sustainability-report",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Within one week, adapt the evidence-register and claim-ledger templates to one approved internal reporting process.",
    "Within two weeks, confirm the current reporting basis, jurisdictional applicability and official factor sources with responsible owners.",
    "Within one month, pilot one bounded AI-assisted task and measure evidence defects, review time and rework—not just drafting speed.",
    "Before the next reporting cycle, convert recurring defects into data-contract, ownership and change-control improvements.",
]

LG_GLOSSARY = [
    ("Activity data", "A measured quantity such as kWh, litres or tonnes used as an input to a metric calculation."),
    ("Applicability", "A documented decision about whether a requirement or guidance item applies to an entity and reporting basis."),
    ("Assurance readiness", "The state in which evidence, methods, controls and approvals are reproducible for independent review."),
    ("Claim ledger", "A table linking each material statement to its source, calculation, status, reviewer and resolution."),
    ("Emission factor", "A coefficient that converts activity data into greenhouse-gas emissions for a defined source, geography and period."),
    ("Evidence register", "An inventory of source records with owner, period, boundary, location and verification status."),
    ("Generative AI", "A model that produces text or other content from instructions and context; it does not establish corporate evidence."),
    ("GRI", "A modular reporting system focused on an organisation's significant impacts on the economy, environment and people."),
    ("Impact materiality", "Prioritisation of an organisation's most significant impacts under the stated impact-reporting basis."),
    ("ISSB", "The International Sustainability Standards Board, which issues IFRS Sustainability Disclosure Standards."),
    ("Material information", "Information whose omission, misstatement or obscuring could influence decisions under the applicable reporting basis."),
    ("SASB Standards", "Industry-based disclosure topics and metrics maintained by the ISSB."),
    ("Scope 1", "Direct greenhouse-gas emissions from sources owned or controlled by the reporting company."),
    ("Scope 2", "Indirect emissions from the generation of purchased energy consumed by the reporting company."),
    ("Scope 3", "Other indirect value-chain emissions not included in Scope 2."),
    ("Source ID", "A stable identifier that allows a reported item to be traced to an original record."),
    ("TCFD", "The completed climate-disclosure initiative whose recommendations are fully incorporated into IFRS S2."),
]

NEXT_STEPS = dict(
    title="A Practical 30-Day Application Plan",
    items=[
        "Week 1 — confirm scope, owners, approved tools and source inventory.",
        "Week 2 — pilot one data-to-metric workpaper with complete lineage.",
        "Week 3 — draft one disclosure and close every high-risk claim-ledger item.",
        "Week 4 — review the workflow, exceptions, rework and next-cycle controls.",
    ],
)

THANK_YOU = dict(
    body=(
        "You now have an evidence-controlled workflow for collecting, analysing, drafting, "
        "mapping and reviewing sustainability information with accountable human oversight."
    ),
    kicker="C1311 · KEEP THE EVIDENCE VISIBLE",
)

TRAINER_TEAM = [
    (
        "Ng Herk Low",
        "Sustainability professional and trainer with leadership experience in strategy, governance, "
        "social impact and stakeholder-focused sustainability reporting.",
    ),
    (
        "Lynn Foo",
        "Sustainability and ESG practitioner with experience in carbon measurement, reporting, "
        "environmental management, circular economy and organisational governance.",
    ),
]

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release: PPT, Learner Guide, Lesson Plan and eight connected labs.", TRAINER),
]
