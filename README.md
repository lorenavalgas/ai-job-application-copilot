# AI Job Application Copilot

A small, transparent AI workflow that helps a candidate compare a job description with their own experience and draft an honest application summary.

## What it does

- Extracts the role's main requirements from a job description.
- Matches each requirement to evidence the candidate provides.
- Marks missing evidence instead of guessing or inventing qualifications.
- Drafts a concise introduction using only supplied facts.

## Run locally

1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Set `OPENAI_API_KEY` in your environment.
5. Run `streamlit run app.py`.

The app sends the entered job description and experience text to the OpenAI API. Do not enter confidential information. The API key stays in the environment and is never shown in the interface.

## Example inputs

**Job description**

> Senior Software Engineer. Build backend services in Python, collaborate across product and design, improve reliability, and communicate tradeoffs clearly.

**Candidate evidence**

> Built Python APIs for a payments product. Worked with product and design to scope features. Added monitoring that reduced incident resolution time. Presented technical tradeoffs to stakeholders.

The app returns a requirement-by-requirement evidence table and an editable draft introduction. It may miss nuance; review every claim before using it.

## Design choices

- The model is instructed to use only candidate-provided evidence.
- Each requirement receives an evidence quote or an explicit “No evidence provided” result.
- The generated introduction is clearly labeled as a draft for human review.
- No resume or job data is stored by this application.

## Tech

Python · Streamlit · OpenAI Responses API

## Project status

Portfolio demo. Validate all generated content before using it in a real application.
