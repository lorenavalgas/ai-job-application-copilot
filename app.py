import json
import os

import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Job Application Copilot", page_icon="🧭", layout="centered")
st.title("🧭 AI Job Application Copilot")
st.caption("Map a job description to your real experience, then draft an honest introduction.")
st.info("Use only information you are comfortable sending to the OpenAI API. Review every generated claim before using it.")

job = st.text_area("Job description", height=220, placeholder="Paste the role description...")
evidence = st.text_area("Your relevant experience", height=220, placeholder="Add projects, skills, and results you can support...")

api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Configure OPENAI_API_KEY in the app's Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)
    prompt = f"""Analyze a job description against candidate-provided experience.
Use only facts explicitly present in the candidate evidence. Never infer or invent qualifications, employers, dates, metrics, or outcomes.
Return valid JSON with exactly these keys:
- requirements: array of objects with requirement (short phrase), evidence (short exact quote from candidate text, or 'No evidence provided'), and match (Strong, Partial, or Missing)
- introduction: a first-person draft of 3-4 sentences using only supported facts; if evidence is insufficient, say so plainly.

JOB DESCRIPTION:
{job}

CANDIDATE EVIDENCE:
{evidence}
"""
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )
        result = json.loads(response.output_text)
        st.subheader("Requirements and evidence")
        st.dataframe(result["requirements"], use_container_width=True, hide_index=True)
        st.subheader("Draft introduction")
        st.write(result["introduction"])
        st.caption("Draft only. Confirm that every statement is accurate before using it.")
    except json.JSONDecodeError:
        st.error("The model returned an unexpected format. Please try again.")
    except Exception as exc:
        st.error(f"Request failed: {exc}")
