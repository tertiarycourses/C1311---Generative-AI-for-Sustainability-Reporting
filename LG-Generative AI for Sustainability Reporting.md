# Generative AI for Sustainability Reporting — Learner Guide

**Course Code:** C1311  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 28 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Generative AI for Sustainability Reporting  (Day 1 morning · 2 labs)](#topic-01--getting-started-with-generative-ai-for-sustainability-reporting--day-1-morning--2-labs)
  - [ESG, Sustainability Reporting and Generative AI](#esg-sustainability-reporting-and-generative-ai)
  - [Set Up AI Tools for Reporting](#set-up-ai-tools-for-reporting)
  - [GRI, SASB, TCFD and ISSB at a Glance](#gri-sasb-tcfd-and-issb-at-a-glance)
  - [Effective Prompting and Responsible, Transparent AI Use](#effective-prompting-and-responsible-transparent-ai-use)
  - [Lab 1 — Set the Reporting Boundary and AI Control Contract](#lab-1--set-the-reporting-boundary-and-ai-control-contract)
  - [Lab 2 — Build the Framework and Materiality-Lens Register](#lab-2--build-the-framework-and-materiality-lens-register)
- [Topic 02 — AI for ESG Data Collection and Analysis  (Day 1 afternoon · 3 labs)](#topic-02--ai-for-esg-data-collection-and-analysis--day-1-afternoon--3-labs)
  - [Gather and Structure ESG Data with AI](#gather-and-structure-esg-data-with-ai)
  - [Calculate and Interpret Metrics and Emissions](#calculate-and-interpret-metrics-and-emissions)
  - [Conduct Materiality and Gap Analysis](#conduct-materiality-and-gap-analysis)
  - [Visualise and Summarise ESG Data](#visualise-and-summarise-esg-data)
  - [Lab 3 — Create the ESG Evidence Register and Data Dictionary](#lab-3--create-the-esg-evidence-register-and-data-dictionary)
  - [Lab 4 — Calculate Scope 1, Scope 2 and Intensity Metrics](#lab-4--calculate-scope-1-scope-2-and-intensity-metrics)
  - [Lab 5 — Run Materiality, Gap and Visual Analysis](#lab-5--run-materiality-gap-and-visual-analysis)
- [Topic 03 — AI for Drafting and Structuring Reports  (Day 2 morning · 1 lab)](#topic-03--ai-for-drafting-and-structuring-reports--day-2-morning--1-lab)
  - [Draft Narrative Disclosures and Executive Summaries](#draft-narrative-disclosures-and-executive-summaries)
  - [Structure Reports and Sections with AI](#structure-reports-and-sections-with-ai)
  - [Ensure Consistency, Tone and Readability](#ensure-consistency-tone-and-readability)
  - [Fact-Check and Validate AI Output](#fact-check-and-validate-ai-output)
  - [Lab 6 — Draft and Validate an Evidence-Grounded Disclosure](#lab-6--draft-and-validate-an-evidence-grounded-disclosure)
- [Topic 04 — AI for Compliance, Frameworks and Continuous Reporting  (Day 2 afternoon · 2 labs)](#topic-04--ai-for-compliance-frameworks-and-continuous-reporting--day-2-afternoon--2-labs)
  - [Map Content to GRI, SASB, TCFD and ISSB](#map-content-to-gri-sasb-tcfd-and-issb)
  - [Build Assurance-Ready Audit Trails and Governance](#build-assurance-ready-audit-trails-and-governance)
  - [Automate Recurring and Multi-Year Reporting](#automate-recurring-and-multi-year-reporting)
  - [Build an Efficient Sustainability Reporting Workflow](#build-an-efficient-sustainability-reporting-workflow)
  - [Lab 7 — Build the Framework Crosswalk and Assurance Evidence Index](#lab-7--build-the-framework-crosswalk-and-assurance-evidence-index)
  - [Lab 8 — Design the Recurring Reporting Workflow and Final Pack](#lab-8--design-the-recurring-reporting-workflow-and-final-pack)
- [Wrap-Up and Authoritative Reference Set](#wrap-up-and-authoritative-reference-set)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies Generative AI for Sustainability Reporting (C1311). It teaches the reporting concepts behind eight connected labs before presenting the practical workflow. The four-topic sequence matches the published course outline and uses the synthetic HarbourLight Foods scenario.

Work through the labs in order. Treat every AI output as working material: preserve source IDs, recalculate metrics, verify official requirements and record the human decision. The framework summaries support learning but do not replace the current standards or jurisdiction-specific professional advice.


## Course Learning Outcomes

- LO1: Establish a responsible, evidence-controlled generative AI workflow and distinguish the purposes of GRI, SASB, TCFD and ISSB reporting guidance.
- LO2: Structure ESG source data, calculate and interpret selected emissions and intensity metrics, and perform transparent materiality and gap analysis.
- LO3: Draft readable, evidence-grounded sustainability disclosures and executive summaries, then validate claims, consistency and limitations.
- LO4: Map report content to applicable frameworks, maintain an assurance-ready audit trail, and design a governed recurring reporting workflow.


## Before You Start — Preparation

**What you need**

- A laptop with a spreadsheet application and text editor.
- Access to one organisation-approved generative AI assistant such as ChatGPT, Claude or Gemini.
- The synthetic files in labs/assets; do not substitute confidential organisational records during class.
- A browser for opening the current official framework sources listed in the guide.

**Verify your setup**

Create a working folder named HLF-2025 with source, calculation, draft and review subfolders. Open the synthetic CSV files without changing their raw columns, and confirm that your AI assistant can return a Markdown table.

```bash
HLF-2025/
  source/
  calculation/
  draft/
  review/
```

**Conventions used in every lab**

- Use source IDs exactly as supplied and write MISSING when evidence is absent.
- Keep raw values and normalised values in separate columns.
- Record every factor, formula, unit conversion, reviewer and version.
- Use synthetic training factors only for the class calculations; obtain current approved factors for real reporting.
- Never paste restricted data, credentials or personal information into an unapproved service.


## Topic 01 — Getting Started with Generative AI for Sustainability Reporting  (Day 1 morning · 2 labs)

ESG and sustainability reporting · AI-assisted work · reporting frameworks · prompt design · responsible and transparent use

**Key concepts**

- Reporting purpose — Connect material impacts, risks and opportunities to decision-useful, traceable disclosures.
- Framework lenses — Use GRI for significant impacts and ISSB/SASB for investor-focused risks and opportunities; retain TCFD as a useful climate bridge.
- Grounded generation — Ask an AI assistant to transform supplied evidence, never to manufacture missing evidence.
- Human accountability — A named preparer reviews scope, calculations, claims, privacy, rights and applicability before use.
- Prompt contract — State goal, reporting context, constraints, sources, output schema and review tests.
- Transparent use — Record model, date, inputs, revisions, source links and final human decision.


### ESG, Sustainability Reporting and Generative AI

Sustainability reporting explains an organisation's material impacts, risks, opportunities, governance, actions and performance. Generative AI is a drafting and transformation aid within that process; it is not a source of corporate evidence.

Readers rely on reported information for decisions. A fluent AI response can hide unsupported claims, boundary errors or omitted uncertainty unless the reporting team keeps evidence and judgement separate from language generation.

**How it works**

- Define the reporting objective, audience, period, entities and operational boundary.
- Collect approved records and label observed facts, calculations, interpretations and unknowns.
- Use AI for bounded tasks such as structuring, summarising, comparing or critiquing.
- Verify every material statement and retain the approved evidence trail.

**Worked example**

- HarbourLight Foods has electricity invoices, diesel records and a prior-year narrative.
- The assistant organises those records into a disclosure outline and labels missing data.
- The preparer calculates the metrics, confirms the boundary and approves the final wording.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task has a clear owner, approved evidence and a review checklist. | The assistant would receive confidential or personal data outside approved controls. |
| The output can be traced back to a source record or transparent calculation. | The task asks the model to invent a figure, legal conclusion or assurance opinion. |

**Practitioner quality lens**

- Failure signal: The draft contains precise claims but no source identifiers or boundary statement.
- Repair move: Add an evidence table, explicit unknown labels and a named human approval gate.
- Quality evidence: Each material claim links to a record, calculation or documented judgement.

---


### Set Up AI Tools for Reporting

An AI reporting workspace combines an approved assistant, a synthetic or authorised source pack, a structured working folder and a versioned log of prompts, outputs and human decisions.

Setup choices determine what data is exposed, whether work can be reproduced and whether later reviewers can distinguish raw evidence from AI-generated working text.

**How it works**

- Confirm approved tools, access controls, retention settings and prohibited data classes.
- Create separate folders for sources, calculations, drafts, review notes and approved output.
- Use stable source IDs and a prompt log with model, date, purpose and input references.
- Test the workflow with synthetic data before introducing authorised organisational records.

**Worked example**

- The team creates HLF-2025/source, calculation, draft and review folders.
- Invoice INV-E-012 and factor EF-SG-2025-TRAINING remain referenced by stable IDs.
- Prompt P-001 uses only synthetic extracts and the reviewer records APPROVE, REVISE or STOP.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The organisation has approved the tool and defined its data-handling rules. | Consumer accounts are used for restricted records without organisational approval. |
| A reviewer can reproduce the task from saved source IDs and prompt instructions. | Source files and generated drafts are mixed in one unversioned folder. |

**Practitioner quality lens**

- Failure signal: No one can tell which input or model produced a sentence.
- Repair move: Introduce stable IDs, version names, a prompt log and separate source and draft areas.
- Quality evidence: A second reviewer can reproduce the draft lineage without guessing.

---


### GRI, SASB, TCFD and ISSB at a Glance

GRI focuses on an organisation's most significant impacts on the economy, environment and people. ISSB Standards establish an investor-focused baseline; SASB supplies industry-based topics and metrics. TCFD's governance, strategy, risk management, and metrics-and-targets architecture is incorporated into IFRS S2.

Framework names are not interchangeable. Selecting a disclosure only because an AI response mentioned a familiar acronym can create materiality, audience and completeness errors.

**How it works**

- Identify the reporting audience, jurisdiction, applicable rules and stated reporting basis.
- Apply the relevant materiality lens before selecting disclosures or metrics.
- Use official standards and current applicability guidance as the requirements register.
- Map one evidence item to multiple requirements only where definitions and boundaries genuinely align.

**Worked example**

- Water stress may be significant as an impact under GRI even when it is not financially material.
- A climate transition risk may be material to investors under IFRS S1 and IFRS S2.
- A food-sector SASB metric can add industry specificity while the TCFD architecture supports transition to IFRS S2.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Building a framework register or explaining why a disclosure belongs in the report. | Declaring broad compliance from a keyword match or incomplete checklist. |
| Reconciling impact-focused and investor-focused information without merging their tests. | Treating TCFD as an additional current layer where IFRS S2 already covers it, unless a rule still requires it. |

**Practitioner quality lens**

- Failure signal: The framework column contains several acronyms but no requirement IDs or rationale.
- Repair move: Record audience, lens, official source, requirement identifier and applicability decision.
- Quality evidence: Every mapping explains both why the item is relevant and what evidence supports it.

---


### Effective Prompting and Responsible, Transparent AI Use

A reporting prompt is a controlled work instruction containing a goal, context, constraints, source boundaries, output schema and review criteria. Transparent use records the assistant's role and the human checks that converted working text into approved content.

Generic prompts reward plausible prose. A structured prompt and adversarial review make missing evidence, inconsistent units, unsupported causal language and invented requirements easier to detect.

**How it works**

- State one task, audience, reporting period and intended decision.
- Paste or reference only approved source extracts and forbid unsupported completion.
- Require a structured output with claim, source, confidence and unresolved-question fields.
- Run a separate critique prompt, then verify the critique against the original evidence.

**Worked example**

- Goal: draft a 150-word energy disclosure for FY2025 using sources HLF-E01 to HLF-E06.
- Constraint: preserve units, label calculated values and write MISSING where evidence is absent.
- Review: return a claim ledger and flag wording that implies causation, certainty or compliance.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Drafting, restructuring or reviewing content from a bounded evidence pack. | The prompt asks for a current legal or standards conclusion without checking the official source. |
| The output format exposes uncertainty and supports line-by-line verification. | The model is asked to conceal its role or remove known caveats to sound more confident. |

**Practitioner quality lens**

- Failure signal: The answer is polished but fills evidence gaps silently.
- Repair move: Require MISSING labels, a claim ledger and an independent human source check.
- Quality evidence: Uncertainty remains visible and all accepted claims survive source verification.

---


### Lab 1 — Set the Reporting Boundary and AI Control Contract

Learning outcome: LO1: establish a responsible, evidence-controlled generative AI reporting workflow.

Duration: 40 minutes.

Goal: Create the control files that keep every later AI-assisted task inside a defined reporting and evidence boundary.

You will set up the synthetic HarbourLight Foods reporting workspace, define the reporting entity, period, audience and evidence boundary, and write an AI-use charter. You will then run one bounded transformation task and record the sources, output and human decision.

**What you'll build**

A reporting-basis.md, ai-use-charter.md and prompt-log.csv that define scope, permitted data, prompt controls, review gates and a reproducible first AI-assisted task.   (Tools: Text editor · approved AI assistant · labs/assets/harbourlight-company-brief.md · source-pack-index.md.)

**Prerequisites**

- Create the HLF-2025/source, calculation, draft and review folders described in the Learner Guide.
- Open labs/assets/source-pack-index.md and labs/assets/harbourlight-company-brief.md.
- Use only the synthetic course files; do not paste workplace records into the class assistant.

**Step-by-step**

1. Create reporting-basis.md. Record Entity, Reporting period, Reporting boundary, Primary audiences, Reporting purposes, Frameworks to investigate, Prepared by, Reviewed by and Unresolved questions. Use the company brief for facts and write MISSING for anything not supplied.

   ```bash
   Entity: HarbourLight Foods Pte Ltd
Reporting period: 1 January–31 December 2025
Boundary: Singapore manufacturing and distribution sites listed in HLF-BRIEF-01
Primary audiences: management, customers, investors and other affected stakeholders
Rule: source ID, documented calculation, documented judgement or MISSING
   ```

2. Create ai-use-charter.md with five headings: Permitted tasks, Prohibited inputs, Required output controls, Human review gates and Recordkeeping. Under each heading add at least three specific rules. Include a rule that AI may structure, compare, draft or critique supplied evidence but may not invent a metric, factor, stakeholder view, applicability conclusion or approval.

   ```bash
   Required output controls:
- cite supplied source IDs
- preserve units and periods
- label calculations and assumptions
- write MISSING for unsupported fields
- separate observed facts, interpretation and recommended follow-up
   ```

3. Create prompt-log.csv with columns Prompt_ID,Date,Model_or_Service,Purpose,Source_IDs,Input_Data_Class,Output_File,Reviewer,Decision,Decision_Reason. Add row P-001. Then write a six-part prompt in review/P-001-prompt.md using Goal, Context, Constraints, Sources, Output and Review.

   ```bash
   Goal: Extract the supplied company profile into a reporting-scope table.
Context: This is a synthetic FY2025 sustainability-reporting exercise.
Constraints: Use only HLF-BRIEF-01; preserve names and dates; write MISSING where silent.
Sources: <PASTE HLF-BRIEF-01>
Output: Field | Extracted value | Source ID | Status.
Review: Flag any inferred boundary, audience or obligation.
   ```

4. Run P-001 in one approved AI assistant. Save the response as review/P-001-output.md. Compare every row with HLF-BRIEF-01, add a Human_check column, and mark each row SUPPORTED, REVISE or REMOVE. Update prompt-log.csv with the service name, output file, reviewer, final decision and a specific reason.

   ```bash
   Decision values: APPROVE · REVISE · STOP
APPROVE only if every retained value is supported and all missing items remain visible.
   ```


**Test it**

Open the three control files. reporting-basis.md must state entity, FY2025 period, boundary, audiences, owners and unresolved questions. ai-use-charter.md must contain all five headings and at least fifteen specific rules. prompt-log.csv must contain P-001 with source HLF-BRIEF-01, output filename, reviewer, decision and reason. P-001-output.md must have no unsupported row marked SUPPORTED.

**Checkpoint and rejoin point**

Keep reporting-basis.md, ai-use-charter.md, prompt-log.csv and the P-001 files. If you need to rejoin, use these files as the reporting and AI-control boundary for Labs 2–8.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The AI fills missing fields with plausible detail. | Add 'write MISSING; do not infer or complete' to Constraints and rerun under a new prompt-log row. |
| The output contains no source IDs. | Make Source ID a required column and reject any row that does not cite HLF-BRIEF-01. |
| The charter is generic. | Replace words such as 'careful' with observable rules, named files, allowed statuses and review gates. |

**Challenge**

Add a risk rating from 1–3 to the prompt log. Define anchors based on data sensitivity, decision impact and ease of verification, then assign and justify the rating for P-001.

**Reflection**

Which control most reduced the chance that fluent language would be mistaken for reporting evidence, and what artifact proves that control operated?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


### Lab 2 — Build the Framework and Materiality-Lens Register

Learning outcome: LO1: distinguish GRI, SASB, TCFD and ISSB purposes and record current applicability.

Duration: 45 minutes.

Goal: Create a source-backed register that keeps framework purpose, audience, materiality lens and applicability distinct.

You will inspect the supplied official-source links, complete a framework register for GRI, ISSB, SASB and TCFD, and add Singapore applicability checks. An AI assistant may compare the supplied summaries, but you will verify every retained statement against the official page.

**What you'll build**

A framework-and-applicability-register.csv plus materiality-lenses.md showing purpose, audience, lens, requirement source, effective-date check, applicability owner and unresolved questions.   (Tools: Browser · spreadsheet · approved AI assistant · framework-starter-register.csv.)

**Prerequisites**

- Completed Lab 1 reporting basis and AI-use charter.
- Open labs/assets/framework-starter-register.csv and source-pack-index.md.
- Use the current official links in the starter register; do not rely on the model's memory of standards.

**Step-by-step**

1. Time box: 12 minutes. Copy framework-starter-register.csv to framework-and-applicability-register.csv. The nine source rows already contain a short starter classification. In three pairs, assign three rows per pair, open each Official_URL, record the actual access date in Checked_Date, and verify or revise Current_Status, Audience, Materiality_Lens and Purpose_Summary. Working alone, verify one GRI row, one ISSB/SASB row, the TCFD row and one Singapore row; mark the other rows PENDING CHECK with an owner. For TCFD, record that the task force completed its work and that its recommendations are incorporated into IFRS S2.

   ```bash
   Required rows: GRI Universal Standards · GRI 3 · GRI Topic Standards · IFRS S1 · IFRS S2 · SASB Standards · TCFD bridge · SGX Rule 711B · Singapore requirements timeline
   ```

2. Time box: 6 minutes. Create materiality-lenses.md with a two-column comparison. Under Impact lens, record significant impacts on the economy, environment and people. Under Investor lens, record sustainability-related risks and opportunities that could affect the entity's prospects. Add a third section explaining that one evidence item may inform both lenses but needs a separate conclusion and rationale.

   ```bash
   Impact lens → evidence → significance judgement → GRI material topic
Investor lens → risk/opportunity evidence → effects on prospects → ISSB material information
   ```

3. Time box: 8 minutes. Add five HarbourLight Reporting_Need rows using the supplied register columns: energy and emissions, packaging waste, worker safety, climate transition risk, and governance of sustainability information. For each, enter Candidate_Framework, Candidate_Requirement, Lens, Rationale, Applicability_Owner and Status. Use PENDING where the current evidence does not support a conclusion.

   ```bash
   Allowed Status values: CURRENT · PENDING · NOT APPLICABLE · NEEDS INTERPRETATION
Never use a framework acronym alone as the rationale.
   ```

4. Time box: 10 minutes. Paste only the completed comparison fields—not the URLs alone—into the approved AI assistant. Ask it to find lens conflicts, missing requirement IDs, obsolete treatment of TCFD and unsupported applicability claims. Save the raw critique as review/P-002-framework-critique.md. The supplied register already contains Review_Result and Reviewer_Reason; complete both fields for every accepted or rejected suggestion. Add P-002 to prompt-log.csv with source IDs, output filename, reviewer, decision and decision reason.

   ```bash
   Return: Row_ID | Possible_issue | Official_source_to_check | Proposed_fix
Do not declare compliance, conformity or legal applicability.
   ```

5. Time box: 5 minutes, leaving 4 minutes for the Test It check. Write a five-sentence framework-selection note below the materiality comparison. State which lenses HarbourLight will explore, what remains hypothetical in this course, why official requirements control, and which named owner must confirm jurisdiction and reporting basis before publication.

   ```bash
   Decision pattern: audience + lens + requirement + applicability owner + evidence status
   ```


**Test it**

The register must contain all nine required framework or jurisdiction rows, official URL, and either an actual checked date or PENDING CHECK with a named owner. Each row must have audience, lens, current-status note and owner. It must contain five HarbourLight reporting-need rows and no unsupported applicability claim marked CURRENT. materiality-lenses.md must keep the two lenses separate, explain shared evidence correctly and identify the owner of final applicability decisions. prompt-log.csv must contain P-002 and the register must record a reviewer result and reason for every AI-proposed change.

**Checkpoint and rejoin point**

Use framework-and-applicability-register.csv as the controlled requirements source in Labs 5 and 7. Rejoin by filtering Status to CURRENT or PENDING and retaining every official URL, P-002 record and reviewer reason.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A framework row has no materiality lens. | Return to its official purpose and audience; record impact, investor, jurisdiction-specific or guidance bridge. |
| The assistant describes TCFD as a new standalone standard. | Replace the wording from the current IFRS Foundation TCFD page and retain the official link. |
| The register says a rule applies to HarbourLight. | Change the status to PENDING until the entity scope, listing status and responsible owner confirm applicability. |

**Challenge**

Add Effective_From and Last_Changed columns. Define a quarterly review trigger and show how a changed official source would create a controlled follow-up rather than silently altering the report.

**Reflection**

Which pair of frameworks is most easily confused in an AI-generated answer, and what fields in your register prevent that confusion?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


## Topic 02 — AI for ESG Data Collection and Analysis  (Day 1 afternoon · 3 labs)

Source registers · data dictionaries · metric calculations · emissions boundaries · materiality · gap analysis · charts and summaries

**Key concepts**

- Evidence register — Track source owner, period, boundary, unit, status and location before analysis.
- Data dictionary — Define each field, unit, allowed value, calculation and missing-data treatment.
- Calculation lineage — Preserve activity data, factor source, formula, unit conversion and reviewer.
- Materiality lenses — Assess significant impacts separately from investor-focused risks and opportunities.
- Gap status — Distinguish complete, partial, missing, not applicable and pending verification.
- Visual integrity — Use consistent denominators, labelled units, honest scales and visible limitations.


### Gather and Structure ESG Data with AI

ESG data collection turns heterogeneous records into a controlled dataset with stable identifiers, defined fields, consistent units, reporting boundaries and visible evidence status.

AI can extract or normalise repeated fields quickly, but unreviewed extraction may change units, merge entities, duplicate records or convert blanks into invented values.

**How it works**

- Inventory source records and assign source, entity, site, period and owner identifiers.
- Define a data dictionary before asking AI to extract or transform values.
- Require raw value, raw unit, normalised value, normalised unit and transformation note.
- Validate totals, duplicates, ranges and missing fields against the original records.

**Worked example**

- Three sites provide electricity in kWh, MWh and invoice line-item extracts.
- The target schema normalises energy to kWh while retaining raw values and source pages.
- A pivot check compares extracted totals with invoice totals and flags one duplicate month.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The source set is bounded and the extraction schema is explicit. | Scanned records are unreadable or the model cannot preserve page-level provenance. |
| A human can sample and reconcile extracted values to original records. | The workflow overwrites raw values or discards missing-data reasons. |

**Practitioner quality lens**

- Failure signal: Normalised values exist without raw values or transformation notes.
- Repair move: Restore immutable raw columns, units, source IDs and reconciliation checks.
- Quality evidence: A reviewer can trace every reported number to the original record and conversion.

---


### Calculate and Interpret Metrics and Emissions

A sustainability metric combines a precisely defined numerator, denominator, boundary, period and unit. A basic greenhouse-gas calculation multiplies activity data by an appropriate emission factor and converts units consistently.

Seemingly small choices—scope, factor year, consolidation boundary, denominator or rounding—can materially change a trend and make year-on-year comparison misleading.

**How it works**

- Confirm organisational and operational boundaries plus the metric definition.
- Validate activity units and select a documented factor with geography, year and source.
- Calculate result = activity data × factor × unit conversion and retain each component.
- Review totals, intensity denominators, trend drivers, estimation status and restatements.

**Worked example**

- 520,000 kWh × 0.408 kg CO2e/kWh = 212,160 kg CO2e, or 212.16 tCO2e.
- Revenue intensity = total tCO2e ÷ S$ million revenue, using the same reporting period.
- The narrative states that the electricity factor is a synthetic training value, not an official inventory factor.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Inputs, factors, conversions and boundaries are documented and reviewed. | A model supplies an emission factor without an authoritative, current source. |
| Comparisons use consistent periods and explain any recalculation or estimation. | An intensity improvement is presented without also checking the absolute metric and denominator change. |

**Practitioner quality lens**

- Failure signal: A result has no unit, factor version, boundary or calculation trail.
- Repair move: Rebuild the calculation table from activity data through conversion to final metric.
- Quality evidence: The figure recalculates exactly and its comparison basis is explicit.

---


### Conduct Materiality and Gap Analysis

Materiality analysis prioritises significant impacts and/or sustainability-related risks and opportunities using the stated reporting lens. Gap analysis compares required or chosen disclosures with available evidence.

AI can cluster evidence and surface candidate topics, but it cannot replace stakeholder engagement, management judgement, legal applicability decisions or the documented basis for prioritisation.

**How it works**

- Record candidate topics, evidence, affected stakeholders and the reporting lens.
- Score impact significance and investor relevance separately using defined anchors.
- Map priority topics to requirements and classify evidence as complete, partial, missing or not applicable.
- Review thresholds, outliers, omitted sector topics and management decisions.

**Worked example**

- Packaging waste scores high for environmental impact while energy price volatility scores high for financial effect.
- The framework register shows complete energy data but only partial supplier-screening evidence.
- The decision log records the threshold, reviewer and reason for each included or deferred item.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Scoring anchors are written before scoring and evidence remains attached to each judgement. | One combined score hides the difference between impact and financial materiality. |
| The output supports a decision log rather than claiming to automate materiality. | Stakeholder views or sector guidance are generated instead of collected and verified. |

**Practitioner quality lens**

- Failure signal: Every topic is labelled material with identical reasoning.
- Repair move: Separate lenses, define scoring anchors and allow evidence-based non-priority decisions.
- Quality evidence: A reviewer can reproduce the ranking and challenge each judgement.

---


### Visualise and Summarise ESG Data

A reporting visual encodes a defined metric across time, entity or category so a reader can compare values without losing units, denominators, boundaries or uncertainty.

Charts compress complex data, which also makes them capable of hiding denominator shifts, missing periods, inconsistent scales and estimation changes.

**How it works**

- Choose the decision and comparison before choosing a chart type.
- Validate tidy data, units, ordering, baselines and missing-value treatment.
- Use a descriptive title, direct labels, source note and concise limitation.
- Write a summary that separates observation, interpretation and recommended follow-up.

**Worked example**

- A two-year bar chart shows absolute Scope 1 and Scope 2 tCO2e by year.
- A small companion table shows revenue and tCO2e per S$ million to expose denominator effects.
- The summary notes the observed change and asks for operations evidence before assigning a cause.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The visual materially improves comparison and all plotted fields share a coherent grain. | A decorative chart replaces a short table or implies precision unsupported by the data. |
| Readers can see units, time period, boundary, source and limitations. | A causal explanation is generated from correlation or two aggregated points. |

**Practitioner quality lens**

- Failure signal: The chart has a clever title but no unit, boundary or source note.
- Repair move: Restore neutral labelling, units, data notes and a separate interpretation sentence.
- Quality evidence: The visual and source table reconcile exactly and support the same conclusion.

---


### Lab 3 — Create the ESG Evidence Register and Data Dictionary

Learning outcome: LO2: structure ESG source data with traceable provenance, units and quality status.

Duration: 50 minutes.

Goal: Turn the synthetic source pack into a controlled table without losing raw values, units or evidence lineage.

You will inspect HarbourLight's synthetic activity records, define a data dictionary and create a structured ESG dataset. An AI assistant may propose field classifications and normalisation rules, but you will reconcile every retained value to its source row.

**What you'll build**

A data-dictionary.csv, esg-evidence-register.csv and structured-esg-data.csv containing raw and normalised values, source IDs, owners, periods, boundaries and review status.   (Tools: Spreadsheet · approved AI assistant · esg-activity-data.csv · esg-evidence-register-starter.csv.)

**Prerequisites**

- Completed Labs 1–2 and retained the reporting basis and AI-use charter.
- Open labs/assets/esg-activity-data.csv and esg-evidence-register-starter.csv.
- Do not edit the original files in labs/assets; work on copies in HLF-2025/source.

**Step-by-step**

1. Copy the two CSV files into HLF-2025/source. Complete esg-evidence-register.csv with one row per Source_ID. Record Owner, Entity_or_Site, Reporting_Period, Evidence_Type, Location, Data_Class, Completeness_Status and Reviewer. Use COMPLETE, PARTIAL, MISSING or PENDING CHECK only.

   ```bash
   Evidence register control: Source_ID must be unique and every activity-data row must reference one registered source.
   ```

2. Create data-dictionary.csv with columns Field,Definition,Data_Type,Allowed_Unit,Allowed_Values,Null_Treatment,Transformation_Rule and Control_Check. Define at least the fields Year,Entity,Site,Metric,Controlled_Metric,Raw_Value,Raw_Unit,Normalised_Value,Normalised_Unit,Source_ID,Source_Row,Transformation_ID and Verification_Status.

   ```bash
   Controlled mapping:
ELECTRICITY → ELECTRICITY_KWH · DIESEL → DIESEL_L · NATURAL_GAS → NATURAL_GAS_KWH · REVENUE → REVENUE_SGD_M
Reject any uncontrolled metric name.
   ```

3. Paste the Metric, Raw_Value and Raw_Unit columns into the approved AI assistant and ask for a proposed controlled metric name, normalised unit and transformation note. Require the assistant to preserve row IDs and return NO RULE when a conversion is not defined. Save the raw response as review/P-003-normalisation-proposal.csv. Add P-003 to prompt-log.csv before review.

   ```bash
   Return: Row_ID | Proposed_Metric | Proposed_Unit | Proposed_Transformation | Uncertainty
Do not calculate or fill missing values.
   ```

4. Create structured-esg-data.csv. Copy the raw fields unchanged, then enter Controlled_Metric, reviewed Normalised_Value, Normalised_Unit, Transformation_Rule, a unique Transformation_ID and Verification_Status. Use TR-<Row_ID> for each reviewed row. For MWh, multiply by 1,000 to obtain kWh; for every other supplied row preserve the given unit unless the data dictionary defines a rule. Reject or revise every AI proposal that changes a value without a documented rule.

   ```bash
   Verification_Status: VERIFIED · REVISED · MISSING · REJECTED
Keep Raw_Value and Raw_Unit immutable. Update P-003 in prompt-log.csv with output filename, reviewer, APPROVE/REVISE/STOP decision and reason; retained corrections must be visible in the reviewed structured file.
   ```

5. Run four spreadsheet controls: Source_ID lookup completeness, duplicate Row_ID count, raw-to-normalised conversion check and year/metric totals. Add a control-log sheet or control-log.csv with Control_ID,Result,Exception_Count,Resolution and Reviewer. Resolve exceptions or mark them OPEN with a named owner.

   ```bash
   Required controls: C01 all sources registered · C02 Row_ID unique · C03 conversions recalculate · C04 totals reconcile
   ```


**Test it**

data-dictionary.csv must define all required fields and their controls. Every structured row must retain Row_ID, Controlled_Metric, raw value, raw unit, source ID, source row and unique Transformation_ID. All MWh rows must convert exactly to kWh, no other value may change without a rule, and every source lookup must resolve. The control log must contain C01–C04 with reviewer, result and resolution or named open owner. prompt-log.csv must contain completed P-003 review fields.

**Checkpoint and rejoin point**

Use structured-esg-data.csv and data-dictionary.csv as the only metric inputs in Labs 4–8. Rejoin by filtering Verification_Status to VERIFIED or REVISED and keeping OPEN exceptions visible.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The assistant combines site rows. | Require one output row per original Row_ID and prohibit aggregation during normalisation. |
| A value changed but the unit did not. | Reject the row, restore the raw value and apply only the explicit transformation rule from the dictionary. |
| A source lookup fails. | Do not invent a source; mark the record MISSING or PENDING CHECK and assign an evidence owner. |

**Challenge**

Add Minimum, Maximum and Decimal_Places to the dictionary for three metrics. Create a range control and show how an outlier is quarantined without deleting the raw record.

**Reflection**

Which field in your structured dataset is most important for reproducing a reported number later, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


### Lab 4 — Calculate Scope 1, Scope 2 and Intensity Metrics

Learning outcome: LO2: calculate and interpret selected emissions and intensity metrics with transparent lineage.

Duration: 55 minutes.

Goal: Produce a calculation workpaper that can be recalculated from activity data through factor and conversion to final metric.

You will join verified activity data to synthetic training emission factors, calculate FY2024 and FY2025 Scope 1 and Scope 2 emissions, and compare absolute and revenue-intensity results. You will ask AI to review the workpaper structure and draft observations, not to supply factors.

**What you'll build**

An emissions-workpaper.xlsx or emissions-workpaper.csv set containing calculation rows, annual summaries, intensity metrics, control checks, a variance note and complete factor provenance.   (Tools: Spreadsheet · approved AI assistant · structured-esg-data.csv · emission-factors-training.csv.)

**Prerequisites**

- Completed Lab 3 with C01–C04 resolved or assigned.
- Copy labs/assets/emission-factors-training.csv into HLF-2025/calculation.
- Treat every supplied factor as a synthetic training value; never reuse it for an actual inventory.

**Step-by-step**

1. Create a calculation sheet with Calculation_ID,Year,Site,Controlled_Metric,Scope,Activity_Value,Activity_Unit,Transformation_ID,Factor_Source_ID,Factor_ID,Factor_Value,Factor_Unit,Conversion,Result_kgCO2e,Result_tCO2e,Source_ID and Reviewer. Filter the structured dataset by Controlled_Metric to ELECTRICITY_KWH, DIESEL_L and NATURAL_GAS_KWH. Use Normalised_Value and Normalised_Unit as the activity fields and join Controlled_Metric to the factor table's Metric field.

   ```bash
   Scope 1: DIESEL_L and NATURAL_GAS_KWH
Scope 2: ELECTRICITY_KWH
Set Factor_Source_ID=HLF-FACTOR-TRAINING and use CALC-<Row_ID> for detail rows. Reject any row with missing Transformation_ID or Factor_ID, incompatible units or non-reviewed activity status.
   ```

2. Calculate Result_kgCO2e = Activity_Value × Factor_Value and Result_tCO2e = Result_kgCO2e ÷ 1,000. Keep formulas in the spreadsheet. Sum by Year and Scope, then add Total_Scope_1_2. Assign the approved annual summary rows Calculation_ID CALC-FY2024 and CALC-FY2025. Round display values to two decimals but retain full-precision formulas.

   ```bash
   Expected training totals:
FY2024 Scope 1 = 159.22 tCO2e · Scope 2 = 326.40 tCO2e · Total = 485.62 tCO2e
FY2025 Scope 1 = 151.77 tCO2e · Scope 2 = 314.16 tCO2e · Total = 465.93 tCO2e
   ```

3. Lookup rows whose Controlled_Metric is REVENUE_SGD_M for each year and calculate Total_Scope_1_2_tCO2e ÷ Normalised_Value. Add an Intensity_Unit column with tCO2e/S$ million. Calculate absolute and intensity percentage change as (FY2025 − FY2024) ÷ FY2024 × 100, guarding against a zero denominator.

   ```bash
   Expected training intensity:
FY2024 = 7.14 tCO2e/S$ million · FY2025 = 6.43 tCO2e/S$ million
Use the unrounded totals for percentage-change formulas.
   ```

4. Create controls C05–C09: factor-unit compatibility, factor-ID completeness, row recalculation, scope-summary reconciliation and denominator period match. A second learner or trainer must independently recalculate at least one diesel row, one electricity row and both annual totals.

   ```bash
   Control result values: PASS · FAIL · OPEN
A FAIL may not be hidden by rounding.
   ```

5. Provide the annual summary and control results to the approved AI assistant. Ask for three observations that separate absolute change, intensity change and unresolved cause. Save the raw response as review/P-004-observations.md, then edit it so no sentence attributes the change to an initiative unless a supplied source supports that cause. Add P-004 to prompt-log.csv with CALC-FY2024, CALC-FY2025, HLF-FACTOR-TRAINING, output filename, reviewer, final decision and reason.

   ```bash
   Return: Observation | Evidence fields | What cannot be concluded | Follow-up owner
Do not claim performance beyond Scope 1 and Scope 2 or imply an official factor.
   ```


**Test it**

The workpaper must reproduce the expected training totals within 0.01 tCO2e and the displayed intensities within 0.01 tCO2e/S$ million. Every calculation row must retain Calculation_ID, activity source, Transformation_ID, factor source HLF-FACTOR-TRAINING, factor ID, units and formula. C05–C09 must be PASS or have a named OPEN owner. The variance note must distinguish absolute and intensity movement and must not state an unsupported cause. prompt-log.csv must contain a completed P-004 row.

**Checkpoint and rejoin point**

Keep the workpaper, controls and variance note. Rejoin by using the approved annual summary rows and the training-factor limitation in Labs 5–8.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The result is 1,000 times too high or low. | Check whether the factor is kg per unit and confirm the single division by 1,000 when converting to tonnes. |
| A factor joins to the wrong metric. | Use the controlled Metric field and reject many-to-many joins or incompatible Factor_Unit values. |
| Intensity improves while the narrative says emissions performance improved. | Report absolute and intensity results separately and inspect the denominator before interpreting. |

**Challenge**

Add a Factor_Sensitivity column and recalculate FY2025 Scope 2 with a ±5% training factor range. Explain why sensitivity is not a substitute for selecting the correct official factor.

**Reflection**

Which single workpaper field would most quickly expose a boundary or unit error during review?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


### Lab 5 — Run Materiality, Gap and Visual Analysis

Learning outcome: LO2: perform transparent materiality and gap analysis and communicate results with an honest visual.

Duration: 50 minutes.

Goal: Prioritise five candidate topics under separate lenses, show framework evidence gaps and create one decision-useful chart.

You will use synthetic stakeholder and business evidence to score five topics under separate impact and investor lenses, map each topic to the framework register and classify evidence gaps. You will then create a chart and a short summary that avoids causal overreach.

**What you'll build**

A materiality-gap-analysis.xlsx or CSV set with scoring anchors, topic evidence, two separate lens scores, framework-gap status, a labelled chart, reviewer decisions and a follow-up plan.   (Tools: Spreadsheet · approved AI assistant · stakeholder-impact-notes.md · framework-and-applicability-register.csv.)

**Prerequisites**

- Completed Labs 2–4 and retained the framework register, structured dataset and approved metric summary.
- Open labs/assets/stakeholder-impact-notes.md.
- Do not ask the AI assistant to invent stakeholder views, impacts, risks or requirement status.

**Step-by-step**

1. Create scoring-anchors.md before scoring. Define 0–4 anchors for Impact_Significance and Impact_Likelihood, plus 0–4 anchors for Investor_Effect and Investor_Likelihood. Define Evidence_Strength as 0 none, 1 one indirect note, 2 one direct source, 3 two corroborating sources. Do not combine the lenses.

   ```bash
   Impact lens result = significance + likelihood (0–8)
Investor lens result = effect on prospects + likelihood (0–8)
Evidence strength is a visible confidence input, not extra materiality points.
   ```

2. Create materiality-gap-analysis.csv with rows Energy and emissions, Packaging waste, Worker safety, Climate transition risk, and Sustainability-information governance. For each row cite Source_IDs from stakeholder-impact-notes.md and the prior labs, classify each statement as OBSERVED, INTERPRETATION or UNKNOWN, then enter proposed component scores with a one-sentence evidence rationale.

   ```bash
   Required fields: Analysis_ID | Topic | Proposed_Impact_Significance | Proposed_Impact_Likelihood | Proposed_Investor_Effect | Proposed_Investor_Likelihood | Final_Impact_Significance | Final_Impact_Likelihood | Final_Impact_Total | Final_Investor_Effect | Final_Investor_Likelihood | Final_Investor_Total | Adjustment_Reason | Evidence_Strength | Source_IDs | Rationale | Reviewer
Use Analysis_ID=MAT-GAP-01 for the controlled five-topic analysis.
   ```

3. Give only the five evidence summaries and written anchors to the approved AI assistant. Ask for proposed scores, missing evidence and possible lens conflicts. Save the raw response as review/P-005-score-proposals.csv and add P-005 to prompt-log.csv. Enter AI proposals in Proposed_* columns, then make your own Final_* decisions. Calculate totals only from the Final_* component scores. Record Adjustment_Reason whenever the final score differs, and update P-005 with reviewer, decision and reason.

   ```bash
   AI role: organise and challenge the supplied evidence.
Human role: decide scores, thresholds and next action.
   ```

4. Join each topic to the framework register and add Candidate_Requirement, Available_Evidence, Gap_Status,Gap_Description, Owner and Due_Date. Use COMPLETE, PARTIAL, MISSING, NOT APPLICABLE or PENDING INTERPRETATION. A high materiality score does not turn a partial evidence set into a complete disclosure.

   ```bash
   Gap rule: status describes evidence against a named requirement—not the importance of the topic.
   ```

5. Create a scatter chart with Final_Investor_Total on the x-axis, Final_Impact_Total on the y-axis and Topic as the point label, or a grouped bar chart with both lens totals by Topic. Show the 0–8 scale, use a neutral title, include a source note and write three sentences: observation, interpretation and required follow-up.

   ```bash
   Title: HarbourLight Candidate Topic Scores by Reporting Lens
Source note: Synthetic HLF evidence; human-scored using documented 0–4 anchors; not an organisational materiality conclusion.
   ```


**Test it**

MAT-GAP-01 must contain all five topics with Proposed_* and Final_* component scores, formulas based on Final_* scores, source IDs, evidence strength, final reviewer and any adjustment reason. Impact and investor totals must remain separate and range from 0–8. Every gap must map to a named candidate requirement and owner. The chart must encode both lenses visibly, label axes and topics, include the synthetic-source limitation and reconcile to the data table. prompt-log.csv must contain P-005.

**Checkpoint and rejoin point**

Keep the final score table, gap register and chart. Rejoin by using only Final_* scores, named evidence gaps and human-approved follow-up actions in Labs 6–8.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Every topic receives a high score. | Reapply the written anchors independently and use lower scores when evidence or likelihood does not meet the anchor. |
| The assistant merges the two lenses. | Reject the combined score and require separate impact and investor component columns. |
| The chart implies a formal conclusion. | Use 'candidate topic scores', add the synthetic limitation and retain the human decision note. |

**Challenge**

Have a partner score the five topics independently. Flag component differences of two points or more and record what extra evidence or anchor clarification would resolve each difference.

**Reflection**

Which topic changed most when you separated the two materiality lenses, and what does that reveal about audience?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


## Topic 03 — AI for Drafting and Structuring Reports  (Day 2 morning · 1 lab)

Evidence-grounded narrative · executive summaries · report architecture · tone and readability · claim validation

**Key concepts**

- Disclosure logic — State boundary and method before performance, interpretation, actions and limitations.
- Claim ledger — Link every quantitative and material qualitative claim to evidence and review status.
- Connected information — Keep governance, strategy, risks, metrics, targets and financial effects coherent.
- Plain language — Prefer precise verbs, defined terms, short sentences and visible uncertainty.
- Consistency controls — Lock names, periods, units, totals, targets, baselines and framework references.
- Fact-check loop — Extract claims, verify sources and calculations, repair or remove unsupported wording.


### Draft Narrative Disclosures and Executive Summaries

A disclosure narrative converts verified evidence into a balanced account of context, method, performance, actions and limitations. An executive summary selects only the most decision-relevant messages.

AI is useful for structure and variation, but it tends to smooth over caveats and make ordinary changes sound strategic. A source-led outline prevents language quality from outrunning evidence quality.

**How it works**

- Create an evidence table and disclosure outline before asking for prose.
- Draft one section at a time with source IDs embedded in the working version.
- Require balanced treatment of positive, negative and uncertain information.
- Reduce the approved sections into an executive summary without adding new claims.

**Worked example**

- The energy section states boundary, method, absolute result, intensity result and limitation.
- A decrease is described as observed; its cause remains unconfirmed pending operations evidence.
- The executive summary reuses approved claims and includes one priority data gap.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The evidence table is complete enough to support the intended claims. | The prompt asks for a complete report before framework mapping and data validation. |
| A human editor owns materiality, balance and final wording. | Positive tone is used to remove adverse results, uncertainty or missed targets. |

**Practitioner quality lens**

- Failure signal: The narrative contains strategy claims that do not appear in source records.
- Repair move: Return to the evidence table and delete, qualify or source every unsupported claim.
- Quality evidence: The executive summary contains no claim absent from approved disclosures.

---


### Structure Reports and Sections with AI

Report structure is the intentional hierarchy that connects reporting basis, governance, strategy, material topics, performance, targets, methods and reference indexes.

A long generated table of contents can duplicate content or separate metrics from their methods. A requirements-to-section map makes structure serve coverage and reader navigation.

**How it works**

- List audiences, reporting basis, frameworks and applicable requirements.
- Group disclosures by decision purpose and define one owner for each section.
- Map every requirement to a section, evidence set and review gate.
- Use AI to test navigation, duplication and missing connections, then decide manually.

**Worked example**

- Governance and strategy appear once, with cross-references from material topic sections.
- Metric tables include basis, boundary and methods immediately before the results.
- The GRI content index and ISSB cross-reference table point to approved sections.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The structure is driven by requirements and reader questions rather than generated headings. | The assistant invents a generic report architecture before applicability is established. |
| Cross-references can be maintained without duplicating inconsistent claims. | The same target or metric is restated differently in several sections. |

**Practitioner quality lens**

- Failure signal: A requirement maps to multiple sections with different owners and values.
- Repair move: Assign a canonical source and one approved statement, then cross-reference it.
- Quality evidence: Each requirement, section, owner and evidence set has a single current status.

---


### Ensure Consistency, Tone and Readability

Consistency control checks facts, terminology, units, periods, targets and narrative stance across the report. Readability makes complex information understandable without removing necessary precision.

Large reports are edited by many people. AI can detect differences, but it can also standardise away important distinctions or introduce a preferred term that changes a defined meaning.

**How it works**

- Create a style sheet for names, acronyms, units, tense, dates and approved terminology.
- Extract repeated facts and compare them against the canonical data table.
- Rewrite for sentence length, active voice and defined technical terms without changing meaning.
- Run a final contradiction and cross-reference review after layout changes.

**Worked example**

- The style sheet specifies tCO2e, FY2025 and 'HarbourLight Foods Pte Ltd'.
- A consistency check finds 212.16 tCO2e in the table but 221 tCO2e in the summary.
- The editor corrects the summary from the approved calculation, not from the AI suggestion.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Canonical facts and terminology are available for comparison. | A 'make this stronger' prompt encourages promotional or absolute claims. |
| The editor can compare original and revised meaning line by line. | Readability edits remove boundaries, assumptions or material caveats. |

**Practitioner quality lens**

- Failure signal: The same metric appears with different values, units or periods.
- Repair move: Link every repetition to a canonical source and rerun contradiction checks.
- Quality evidence: All repeated facts reconcile and the plain-language version preserves limitations.

---


### Fact-Check and Validate AI Output

Validation decomposes AI output into checkable claims and tests each one against source evidence, calculations, current official requirements and the intended reporting boundary.

An AI response may contain confabulated facts, inaccurate citations, outdated requirements or unjustified causation. Reviewing overall plausibility is not enough.

**How it works**

- Extract quantitative, qualitative, framework, comparative and causal claims into a ledger.
- Verify each claim against the original source, calculation or current official requirement.
- Mark supported, revise, remove, unresolved or not applicable and record the reviewer.
- Run targeted checks for totals, units, dates, names, targets, citations and causal language.

**Worked example**

- Claim C-014 states emissions fell because of equipment upgrades.
- The dataset confirms the fall, but no source record confirms the cause.
- The reviewer changes the wording to an observation and logs the cause as unresolved.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The output can be decomposed into claims and relevant evidence is accessible. | The same model is treated as the sole judge of its own accuracy. |
| A separate reviewer can challenge high-impact or high-uncertainty items. | A citation is accepted because its title looks credible without opening the source. |

**Practitioner quality lens**

- Failure signal: The review says 'looks accurate' without claim-level status.
- Repair move: Build a claim ledger and prioritise quantitative, compliance and causal claims.
- Quality evidence: Every retained material claim has a source, reviewer, status and resolution.

---


### Lab 6 — Draft and Validate an Evidence-Grounded Disclosure

Learning outcome: LO3: draft readable sustainability disclosures and validate every material claim.

Duration: 60 minutes.

Goal: Produce an energy-and-emissions disclosure whose narrative, executive summary and claim ledger reconcile to approved evidence.

You will combine the approved reporting basis, emissions workpaper, materiality-gap analysis and a deliberately flawed prior-year disclosure into a controlled FY2025 draft. You will use AI for bounded drafting and critique, then verify every quantitative, causal, framework and target claim.

**What you'll build**

A style-sheet.md, disclosure-draft.md, claim-ledger.csv and executive-summary.md with source-linked claims, consistent units, balanced wording, unresolved limitations and recorded human decisions.   (Tools: Text editor · spreadsheet · approved AI assistant · disclosure-starters · prior-year-disclosure.md · Lab 4–5 outputs.)

**Prerequisites**

- Completed Labs 1–5 with approved metric summary and named gap owners.
- Open labs/assets/prior-year-disclosure.md and labs/assets/disclosure-brief.md.
- Copy labs/assets/style-sheet-starter.md and claim-ledger-starter.csv into the HLF-2025/draft folder.
- Use the FY2025 calculation workpaper as the canonical quantitative source.

**Step-by-step**

1. Complete style-sheet-starter.md and save it as style-sheet.md. Record the canonical entity name, period, boundary, units, decimal places, names for Scope 1 and Scope 2, approved status terms, date style and words to avoid. Add rules that observed change is not automatically a cause and that a training factor must be disclosed as a limitation.

   ```bash
   Canonical terms: HarbourLight Foods Pte Ltd · FY2025 · tCO2e · tCO2e/S$ million
Avoid unless directly supported: achieved · ensured · eliminated · compliant · industry-leading · because of
   ```

2. Create an evidence outline in disclosure-draft.md with Reporting basis, Method, FY2025 results, Year-on-year comparison, Actions and governance, Limitations, and Next data priorities. Under each heading, list only approved source IDs or calculation IDs. Mark unsupported fields MISSING before asking for prose.

   ```bash
   Minimum evidence IDs: HLF-BRIEF-01 · CALC-FY2024 · CALC-FY2025 · HLF-FACTOR-TRAINING · MAT-GAP-01
No source ID → no factual sentence.
   ```

3. Give the evidence outline, style sheet and labs/assets/disclosure-brief.md to the approved AI assistant. Ask for a 300–400 word disclosure that keeps [SOURCE_ID] tags after each factual sentence and labels [INTERPRETATION] and [LIMITATION]. Save the raw response as review/P-006-raw-draft.md and add P-006 to prompt-log.csv with the five minimum evidence IDs and raw output filename.

   ```bash
   Required sequence: basis → method → absolute result → intensity result → balanced interpretation → actions/governance → limitation → next priority
Do not add targets, causes, external validation or framework claims.
   ```

4. Complete claim-ledger-starter.csv and save it as claim-ledger.csv with Claim_ID,Draft_Sentence,Claim_Type,Source_or_Calculation_ID,Verification_Test,Initial_Status,Reviewer,Resolution,Final_Status. Extract every number, comparison, cause, target, action, framework statement and other material claim from the raw draft and prior-year disclosure. Verify each one against original evidence. Use SUPPORTED, REVISE, REMOVE or UNRESOLVED.

   ```bash
   High-risk claim types: QUANTITATIVE · CAUSAL · TARGET · FRAMEWORK · GOVERNANCE · COMPARATIVE
The AI may extract candidate claims; the reviewer assigns final status. Update P-006 in prompt-log.csv with APPROVE/REVISE/STOP, reviewer and reason; retained edits must be traceable in claim-ledger.csv.
   ```

5. Rewrite disclosure-draft.md using only claims with final SUPPORTED status or a documented REVISE resolution. Remove working source tags from the reader-facing paragraphs but retain a source map below the draft. Then ask the assistant to create a 100–130 word executive summary using only the approved draft. Compare every executive-summary sentence with the claim ledger and save the corrected version as executive-summary.md.

   ```bash
   Final checks: entity · period · boundary · units · totals · intensity denominator · limitations · no unsupported cause · no new executive-summary claim
   ```

6. Run a final contradiction review across the style sheet, disclosure, executive summary and claim ledger. Record each difference in review/final-consistency-log.csv with Field,Canonical_Value,Conflicting_Value,Location,Resolution and Reviewer. Resolve all quantitative conflicts and assign an owner to any remaining text issue.

   ```bash
   Required fields to compare: entity name · reporting period · Scope 1 · Scope 2 · total · intensity · factor limitation
   ```


**Test it**

The final disclosure must be 300–400 words and the executive summary 100–130 words. Both must match the canonical FY2025 Scope 1, Scope 2, total and intensity values from Lab 4. Every retained material claim must have a SUPPORTED or resolved REVISE row in claim-ledger.csv. No UNRESOLVED claim may appear as fact, no unsupported cause or target may remain, and the consistency log must contain no open quantitative conflict. prompt-log.csv must contain completed P-006 review fields and every retained change must be visible in the claim ledger.

**Checkpoint and rejoin point**

Keep the final disclosure, executive summary, style sheet, claim ledger and consistency log. Rejoin by filtering Final_Status to SUPPORTED and using the source map as the narrative evidence trail for Lab 7.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The draft sounds promotional. | Reapply the style sheet and ask for neutral observed-result wording with limitations and no superlatives. |
| The assistant removes source tags too early. | Restore the evidence outline and retain tags until claim verification and final human editing are complete. |
| The executive summary introduces a new claim. | Delete it or return it to the claim ledger; a summary may only select from approved disclosure content. |

**Challenge**

Create two versions for different audiences—management and general stakeholders—using the same approved claim set. Highlight changes in emphasis and explain why the evidence and quantitative content did not change.

**Reflection**

Which claim type required the most human judgement, and how did the claim ledger prevent it from disappearing into prose?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


## Topic 04 — AI for Compliance, Frameworks and Continuous Reporting  (Day 2 afternoon · 2 labs)

Framework crosswalks · current applicability · assurance readiness · governance · recurring and multi-year workflows

**Key concepts**

- Applicability register — Record entity scope, jurisdiction, framework basis, effective date and source owner.
- Requirement crosswalk — Map identifiers to report sections, evidence, owner and status without claiming more than supported.
- Audit trail — Retain source, transformation, calculation, prompt, review and approval lineage.
- Segregation of duties — Separate preparer, reviewer and approver for material claims and calculations.
- Change control — Detect changes in data, factors, methods, requirements and approved narrative.
- Recurring workflow — Use a calendar, data contracts, controlled templates, quality gates and post-cycle improvement.


### Map Content to GRI, SASB, TCFD and ISSB

A framework crosswalk records each requirement or guidance item, why it applies, where it is addressed, which evidence supports it and what status remains.

AI can accelerate comparisons, but keyword similarity is not compliance. Definitions, materiality, industry, effective dates and jurisdiction determine whether a mapping is valid.

**How it works**

- Create a current register from official sources with identifiers, dates and applicability notes.
- Map report claims and sections to requirements using exact evidence references.
- Classify status as complete, partial, missing, not applicable or pending interpretation.
- Have the responsible owner review mappings and avoid unsupported statements of conformity.

**Worked example**

- GRI 3 supports the documented process for determining impact material topics.
- IFRS S1 and S2 use governance, strategy, risk management, and metrics-and-targets content areas.
- A SASB food-industry topic adds industry detail; TCFD is recorded as a legacy bridge incorporated into IFRS S2.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Official sources, applicability decisions and requirement IDs are recorded. | A generated checklist substitutes for reading the applicable standard or rule. |
| The crosswalk is a working control with owners and evidence statuses. | The report claims alignment or conformity when required items remain partial or missing. |

**Practitioner quality lens**

- Failure signal: Mappings contain page numbers but no evidence or applicability rationale.
- Repair move: Add requirement ID, lens, official source, owner, evidence and status.
- Quality evidence: A reviewer can trace each mapping and see unresolved items immediately.

---


### Build Assurance-Ready Audit Trails and Governance

Assurance readiness means evidence, methods, controls, roles and changes are documented so an independent reviewer can understand how a reported statement was produced.

AI introduces another transformation layer. Without logs, version control and approval records, a team may be unable to reproduce a calculation or explain why generated wording was accepted.

**How it works**

- Assign preparer, reviewer, approver and requirement owners with clear handoffs.
- Retain immutable sources, calculation workpapers, prompt logs, claim ledgers and approvals.
- Apply access control, version naming, change reasons and exception management.
- Test high-risk samples for completeness, accuracy, occurrence, consistency and cut-off.

**Worked example**

- Metric M-008 links to invoices, factor EF-03, calculation CALC-02 and reviewer sign-off REV-17.
- Draft D-04 links each retained sentence to claim-ledger rows and an approval record.
- A changed factor triggers recalculation, narrative review and a documented restatement decision.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Material metrics and claims need reproducible lineage and independent review. | AI logs contain restricted source data that should not be retained in that system. |
| The team wants to reduce late-cycle evidence requests and rework. | Approval is implied by silence or performed by the same person for every high-risk item. |

**Practitioner quality lens**

- Failure signal: The final report exists but its working papers cannot reproduce key figures.
- Repair move: Reconstruct lineage from source through calculation, draft, review and approval.
- Quality evidence: A reviewer can select a claim and follow its complete evidence chain.

---


### Automate Recurring and Multi-Year Reporting

Recurring reporting uses controlled templates, data contracts, calendars and exception workflows to repeat stable tasks while preserving human review for material judgement and change.

Copying last year's report carries forward stale claims and methods. Uncontrolled automation can reproduce errors faster and conceal changes in boundaries, factors or requirements.

**How it works**

- Separate repeatable data transformations from judgement-intensive reporting decisions.
- Define input owners, due dates, schemas, validations, approvals and escalation rules.
- Compare current and prior periods for boundary, factor, method, target and requirement changes.
- Generate drafts only after data gates pass, then preserve review and publication controls.

**Worked example**

- Monthly source files load into a locked schema with duplicate and range checks.
- The annual close flags new sites, factor changes and restatement triggers before trend calculations.
- AI drafts variance commentary from approved data, while owners verify explanations and actions.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Inputs are standardised, controls are testable and exceptions have named owners. | The workflow republishes prior narrative without current evidence. |
| The process keeps human approval for materiality, estimates, causal claims and publication. | Automation is introduced before definitions, ownership and quality gates are stable. |

**Practitioner quality lens**

- Failure signal: The process is fast but no one owns rejected records or changed requirements.
- Repair move: Add exception queues, owners, service levels and change-control gates.
- Quality evidence: The cycle is repeatable, exceptions are visible and all published changes are approved.

---


### Build an Efficient Sustainability Reporting Workflow

An efficient workflow sequences scoping, evidence intake, calculation, materiality, drafting, framework mapping, review, approval and publication so defects are caught near their source.

Late reconciliation is expensive. Efficiency comes from clear entry criteria and controls, not from generating more text earlier in the cycle.

**How it works**

- Plan the reporting basis, applicability, roles, calendar and source inventory.
- Validate data and calculations before narrative work begins.
- Use AI in bounded stages with prompt logs, claim ledgers and reviewer gates.
- Close with cross-report reconciliation, approvals, publication archive and lessons learned.

**Worked example**

- HarbourLight's eight-stage board assigns one owner, entry gate and output to each stage.
- A missing energy invoice blocks the metric and narrative but not unrelated governance sections.
- The post-cycle review converts recurring defects into next-year data-contract improvements.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The team needs an end-to-end operating model and clear handoffs. | A single AI prompt is expected to perform data validation, materiality, drafting and sign-off. |
| Management wants transparent status, exceptions and evidence readiness. | Speed is measured only by draft completion rather than rework, evidence gaps and review findings. |

**Practitioner quality lens**

- Failure signal: Drafting begins while scope, data owners or framework basis remain undecided.
- Repair move: Introduce entry gates and stop affected work until foundational decisions are recorded.
- Quality evidence: Each stage has an owner, input, control, output, status and escalation path.

---


### Lab 7 — Build the Framework Crosswalk and Assurance Evidence Index

Learning outcome: LO4: map approved content to current framework sources and maintain an assurance-ready audit trail.

Duration: 55 minutes.

Goal: Connect every approved disclosure and metric to requirements, evidence, controls, owners and review status without overstating applicability.

You will extend the framework register into a requirement crosswalk, map the Lab 6 disclosure and Lab 4 metrics, and build an evidence index from source through calculation, claim and approval. You will also record current Singapore applicability questions for responsible-owner confirmation.

**What you'll build**

A framework-crosswalk.csv, assurance-evidence-index.csv and control-matrix.csv with requirement IDs, report locations, evidence lineage, owners, statuses, exceptions and reviewer sign-off.   (Tools: Spreadsheet · browser · approved AI assistant · Lab 2 register · Lab 4 workpaper · Lab 6 claim ledger.)

**Prerequisites**

- Completed Labs 2, 4 and 6 and retained their official URLs, approved calculations and claim statuses.
- Open labs/assets/framework-crosswalk-starter.csv, assurance-evidence-index-starter.csv and control-matrix-starter.csv.
- Treat HarbourLight's entity and listing status as a synthetic scenario; record jurisdiction decisions as PENDING OWNER CONFIRMATION.

**Step-by-step**

1. Time box: 8 minutes. Copy framework-crosswalk-starter.csv to framework-crosswalk.csv. Reuse the checked dates and status notes from Lab 2; reopen any source marked PENDING CHECK or changed since that check. The starter already contains REFERENCE source rows and seven ACTIVE mapping rows for reporting basis, energy and emissions methods, Scope 1 and Scope 2 results, material-topic process, governance and limitations.

   ```bash
   Required source families: GRI 1/2/3 and relevant Topic Standard · IFRS S1 · IFRS S2 · SASB industry guidance · TCFD bridge · SGX Rule 711B · Singapore requirements timeline
   ```

2. Time box: 12 minutes. For each ACTIVE mapping row, complete Audience,Lens,Applicability_Status,Applicability_Owner,Report_Location,Claim_IDs,Metric_IDs,Evidence_Status,Gap,Action_Owner and Due_Date. Use COMPLETE, PARTIAL, MISSING, NOT APPLICABLE or PENDING INTERPRETATION for evidence; use PENDING OWNER CONFIRMATION where entity scope or jurisdiction has not been established. Keep REFERENCE rows as source controls rather than duplicating a report-location mapping on them.

   ```bash
   Mapping test: exact requirement + rationale + current source + report location + evidence + owner + status
   ```

3. Time box: 8 minutes. Give the seven ACTIVE crosswalk rows and official-source summaries to the approved AI assistant. Ask it to identify keyword-only mappings, lens conflicts, obsolete TCFD treatment, missing owners and any unsupported statement of alignment. Save the raw critique as review/P-007-crosswalk-critique.md and add P-007 to prompt-log.csv. Verify every proposed change against the official URL before editing; record the reviewer decision and reason in P-007 and retain accepted or rejected changes in the reviewed crosswalk fields.

   ```bash
   Return: Crosswalk_ID | Issue | Why_it_matters | Official_source_to_check | Proposed_status
Do not declare applicability or conformity.
   ```

4. Time box: 12 minutes. Complete the five supplied rows in assurance-evidence-index-starter.csv and save it as assurance-evidence-index.csv with Evidence_ID,Evidence_Type,Original_Source_ID,Transformation_ID,Calculation_ID,Claim_ID,Crosswalk_ID,File_Location,Version,Prepared_By,Reviewed_By,Approval_Status and Exception_ID. Create at least one complete chain for FY2025 Scope 1, Scope 2, total, intensity and the factor limitation.

   ```bash
   Lineage pattern: source → structured row → calculation → claim → disclosure location → framework mapping → approval
   ```

5. Time box: 10 minutes, leaving 5 minutes for the Test It check. Complete the seven supplied rows in control-matrix-starter.csv and save it as control-matrix.csv with Control_ID,Risk,Control_Activity,Frequency,Preparer,Reviewer,Evidence,Exception_Route and Status. Add controls for source completeness, factor approval, formula accuracy, claim verification, framework change, access/version control and publication approval. Sample two metric chains and one narrative chain; record PASS, FAIL or OPEN and resolve or assign every exception.

   ```bash
   Minimum controls: CTL-01 source · CTL-02 factor · CTL-03 calculation · CTL-04 claim · CTL-05 framework change · CTL-06 version/access · CTL-07 publication
   ```


**Test it**

Every ACTIVE crosswalk row must contain an official source, requirement or guidance ID, lens, applicability status, report location, evidence status and owner; every REFERENCE row must retain its current official URL and checked or PENDING CHECK status. No synthetic jurisdiction decision may be stated as confirmed. The evidence index must contain complete reproducible chains for the four metrics and factor limitation. CTL-01–CTL-07 must have preparer, reviewer, evidence and status, with no unowned FAIL or OPEN item. prompt-log.csv must contain completed P-007 review fields.

**Checkpoint and rejoin point**

Keep the crosswalk, evidence index and control matrix. Rejoin by filtering to the current version and using OPEN or PENDING rows as explicit inputs to the recurring workflow in Lab 8.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A crosswalk row maps only by similar wording. | Return to the exact requirement, materiality lens and evidence definition; downgrade to PARTIAL or remove the mapping. |
| The evidence chain skips from source to final claim. | Add the structured-row and calculation or transformation IDs that explain how the evidence changed. |
| A Singapore rule is marked applicable without entity confirmation. | Set PENDING OWNER CONFIRMATION and name the legal, governance or reporting owner who must decide. |

**Challenge**

Add a Change_Trigger and Last_Reviewed field to each framework row. Simulate one changed requirement and show which calculations, claims, controls and approvals must be reopened.

**Reflection**

Which link in your evidence chain would be hardest for an independent reviewer to reconstruct if it were missing, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-07-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


### Lab 8 — Design the Recurring Reporting Workflow and Final Pack

Learning outcome: LO4: design a governed recurring workflow for multi-year sustainability reporting.

Duration: 55 minutes.

Goal: Turn the course artifacts into a repeatable reporting operating model with entry gates, owners, exceptions and change control.

You will design a reporting calendar and workflow board that reuses controlled structures without copying stale claims. You will specify source-owner data contracts, AI task boundaries, review gates, change triggers and a final pack index that lets another preparer continue the process.

**What you'll build**

A reporting-calendar.csv, workflow-board.csv, data-contracts.md, final-pack-index.md and post-cycle-review.md covering the complete scope-to-publication cycle and its evidence-controlled AI tasks.   (Tools: Spreadsheet · text editor · approved AI assistant · all Lab 1–7 artifacts.)

**Prerequisites**

- Completed Labs 1–7 and retained all current-version controls, exceptions and owner assignments.
- Create an HLF-2025/final-pack folder; do not move or overwrite the original source files.
- Copy reporting-calendar-starter.csv, workflow-board-starter.csv and post-cycle-review-starter.md from labs/assets.
- Use the crosswalk and control matrix to define gates instead of relying on a generic reporting checklist.

**Step-by-step**

1. Complete reporting-calendar-starter.csv and save it as reporting-calendar.csv with Phase,Start,Finish,Entry_Criteria,Output,Owner,Reviewer and Escalation. Include Scope and applicability, Source intake, Data validation, Calculation, Materiality and gaps, Drafting, Framework mapping, Review and approval, Publication archive, and Post-cycle improvement.

   ```bash
   Entry criteria must be observable—for example, 'all required source IDs received or exception owner assigned'.
   ```

2. Create data-contracts.md with one section each for electricity, fuel, revenue, material-topic evidence and governance evidence. For each, state owner, source system, schema, unit, frequency, due date, validation, retention, change notification and exception route. Add a rule that raw values are immutable and corrections create a new version with a reason.

   ```bash
   Data contract fields: Owner · Source · Schema · Unit · Frequency · Due · Validation · Retention · Change trigger · Exception owner
   ```

3. Complete workflow-board-starter.csv and save it as workflow-board.csv with Stage,Task_ID,Task,Input_IDs,AI_Role,Human_Decision,Control_ID,Output_ID,Status and Reopen_Trigger. Add at least twelve tasks across the ten phases. Limit AI_Role to NONE, STRUCTURE, COMPARE, DRAFT or CRITIQUE; no task may assign materiality, applicability, approval or publication to AI.

   ```bash
   Human decisions reserved: scope · materiality · estimate · factor approval · causal claim · framework applicability · exception acceptance · final publication
   ```

4. Ask the approved AI assistant to critique the calendar and board for missing handoffs, circular dependencies, unowned exceptions, stale-prior-year risk and gates that cannot be tested. Save the raw critique as review/P-008-workflow-critique.md and add P-008 to prompt-log.csv. Verify every suggestion and record accepted and rejected changes in review/workflow-change-log.csv with Change_ID,Reason,Affected_Task,Decision and Reviewer. Update P-008 with output filename, reviewer, final decision and reason.

   ```bash
   Critique only the supplied workflow. Do not invent organisational roles, service levels or reporting obligations.
   ```

5. Create a provisional final-pack-index.md. List each current artifact already completed in Labs 1–8 with Version,Owner,Reviewer,Status,Key_Source_IDs and Reopen_Trigger. Include a Start Here section that tells a new preparer how to confirm applicability, inspect open exceptions, rerun calculations and avoid copying stale narrative. Copy only approved current outputs—not raw AI responses—into HLF-2025/final-pack.

   ```bash
   Required groups: governance · requirements · source data · calculations · materiality/gaps · narrative · evidence/control · recurring workflow
   ```

6. Complete post-cycle-review-starter.md and save it as post-cycle-review.md with five metrics: source timeliness, control exception rate, unsupported-claim rate, review rework count and cycle time. For rates, define numerator and denominator. For a count or duration, set Denominator=N/A and define Unit_or_Basis. Name the owner and improvement trigger for each. Add three lessons and one controlled improvement for the next cycle.

   ```bash
   Measure credibility and rework—not number of generated words. Count basis: reviewed change records. Cycle-time basis: elapsed calendar days from approved scope to publication archive.
   ```

7. After post-cycle-review.md is complete, update final-pack-index.md so it indexes the final calendar, board, data contracts, P-008 review records and post-cycle review as well as every approved artifact from Labs 1–7. Recheck file locations, versions, owners, reviewers, statuses, source IDs, open items and reopen triggers; then copy the final index into HLF-2025/final-pack.

   ```bash
   Final sequencing rule: post-cycle review first → final index update second → Start Here path verification last.
   ```


**Test it**

The calendar must contain all ten phases with owner, reviewer, entry criteria, output and escalation. data-contracts.md must cover all five evidence classes and versioned corrections. The workflow board must contain at least twelve tasks, allowed AI roles only, named human decisions and reopen triggers. The final pack must index every Lab 1–8 artifact, identify open items and give a reproducible Start Here path. The post-cycle review must define all five metrics with the rate numerator/denominator or count/duration Unit_or_Basis, owner and trigger. prompt-log.csv must contain P-008, and final-pack-index.md must be updated after the post-cycle review so every Lab 1–8 artifact is indexed.

**Checkpoint and rejoin point**

The final-pack folder is the course endpoint. A new preparer should be able to start with final-pack-index.md, locate every approved artifact, see all unresolved items and know which changes reopen earlier work.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A workflow gate says 'data ready'. | Replace it with observable criteria, required control results and an exception path. |
| The next-year process copies the prior narrative. | Use prior wording only as a comparison source; reopen claims whenever data, boundary, factor, method or requirement changes. |
| An exception has no owner. | Stop the affected task, assign an accountable owner and record an escalation date before continuing. |

**Challenge**

Create a RACI view from the workflow board and identify any stage where one person prepares, reviews and approves a high-risk item. Propose a proportionate segregation-of-duties improvement.

**Reflection**

Which reopen trigger is most important for preventing a fast but inaccurate next-year report?

> **Note:** The complete lab and its support-file references are in labs/lab-08-*.md. Use only the synthetic HarbourLight Foods data supplied with this course. For workplace use, follow your organisation's privacy, security, records, AI and reporting policies, and verify current official requirements and emission factors.

---


## Wrap-Up and Authoritative Reference Set

The workflow is complete when the reporting pack can be traced from each retained claim back to an approved source, calculation or documented judgement. Recheck the official sources whenever applicability, effective dates or methods may have changed.

**Final quality gate**

- Reporting basis, entities, period, boundaries and materiality lens are explicit.
- Metrics recalculate from retained activity data, factor sources, formulas and conversions.
- Every material claim has a source, status, reviewer and resolution.
- Framework mappings use current official identifiers and recorded applicability decisions.
- AI use, limitations, revisions and human approvals are transparent.

**Primary sources used to prepare this course (accessed 28 July 2026)**

- GRI Standards and Universal Standards: https://www.globalreporting.org/standards/
- GRI 3: Material Topics 2021: https://www.globalreporting.org/publications/documents/english/gri-3-material-topics-2021/
- ISSB and IFRS Sustainability Disclosure Standards: https://www.ifrs.org/sustainability/knowledge-hub/introduction-to-issb-and-ifrs-sustainability-disclosure-standards/
- SASB Standards under ISSB stewardship: https://www.ifrs.org/issued-standards/sasb-standards/
- ISSB and the completed TCFD work: https://www.ifrs.org/sustainability/tcfd/
- GHG Protocol Corporate Standard FAQ: https://ghgprotocol.org/corporate-standard-frequently-asked-questions
- NIST AI 600-1 Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Singapore sustainability reporting requirements: https://www.acra.gov.sg/regulations/sustainability-reporting/requirements-timeline/
- SGX Rule 711B Sustainability Report: https://rulebook.sgx.com/rulebook/sustainability-report

---


## Next Steps

- Within one week, adapt the evidence-register and claim-ledger templates to one approved internal reporting process.
- Within two weeks, confirm the current reporting basis, jurisdictional applicability and official factor sources with responsible owners.
- Within one month, pilot one bounded AI-assisted task and measure evidence defects, review time and rework—not just drafting speed.
- Before the next reporting cycle, convert recurring defects into data-contract, ownership and change-control improvements.


## Glossary

- **Activity data** — A measured quantity such as kWh, litres or tonnes used as an input to a metric calculation.
- **Applicability** — A documented decision about whether a requirement or guidance item applies to an entity and reporting basis.
- **Assurance readiness** — The state in which evidence, methods, controls and approvals are reproducible for independent review.
- **Claim ledger** — A table linking each material statement to its source, calculation, status, reviewer and resolution.
- **Emission factor** — A coefficient that converts activity data into greenhouse-gas emissions for a defined source, geography and period.
- **Evidence register** — An inventory of source records with owner, period, boundary, location and verification status.
- **Generative AI** — A model that produces text or other content from instructions and context; it does not establish corporate evidence.
- **GRI** — A modular reporting system focused on an organisation's significant impacts on the economy, environment and people.
- **Impact materiality** — Prioritisation of an organisation's most significant impacts under the stated impact-reporting basis.
- **ISSB** — The International Sustainability Standards Board, which issues IFRS Sustainability Disclosure Standards.
- **Material information** — Information whose omission, misstatement or obscuring could influence decisions under the applicable reporting basis.
- **SASB Standards** — Industry-based disclosure topics and metrics maintained by the ISSB.
- **Scope 1** — Direct greenhouse-gas emissions from sources owned or controlled by the reporting company.
- **Scope 2** — Indirect emissions from the generation of purchased energy consumed by the reporting company.
- **Scope 3** — Other indirect value-chain emissions not included in Scope 2.
- **Source ID** — A stable identifier that allows a reported item to be traced to an original record.
- **TCFD** — The completed climate-disclosure initiative whose recommendations are fully incorporated into IFRS S2.
