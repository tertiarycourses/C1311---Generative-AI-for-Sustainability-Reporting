# C1311---Generative-AI-for-Sustainability-Reporting

Aligned courseware for **Generative AI for Sustainability Reporting** (`C1311`).

## Current release

- Version: `v1.0`
- Slide deck: `courseware/Generative AI for Sustainability Reporting-v1.0.pptx`
- Learner slides: `courseware/Generative AI for Sustainability Reporting-v1.0.pdf`
- Learner Guide: `courseware/LG-Generative AI for Sustainability Reporting.docx` and `.pdf`
- Lesson Plan: `courseware/LP-Generative AI for Sustainability Reporting.docx` and `.pdf`
- Learner Guide Markdown mirror: `LG-Generative AI for Sustainability Reporting.md`
- Hands-on activities: `labs/README.md` and eight connected lab files
- Synthetic classroom data: `labs/assets/`

## Alignment model

The PPT, Learner Guide, Lesson Plan and lab Markdown are generated from the same
course model in:

- `.agents/skills/non-wsq-courseware-build/build/course_data.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain1.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain2.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain3.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain4.py`

Lab titles, order, durations, objectives, instructions and verification criteria
therefore remain consistent across every artifact.

## Rebuild

From Git Bash on Windows:

```bash
COURSE_REPO="$(pwd)" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

Run the required QA scan before publishing:

```bash
python ".agents/skills/non-wsq-courseware-qa/scan_prohibited.py" "$(pwd)"
```

The synthetic HarbourLight Foods values and emission factors are training data
only. Real reporting work must use current approved sources, factors, governance
and applicability decisions.
