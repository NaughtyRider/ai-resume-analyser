import streamlit as st

from utils.parser import extract_text
from utils.prompts import build_prompt
from utils.llm import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("AI Resume Analyzer")

st.write(
    "Upload your resume and compare it against a job description."
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_text(
                uploaded_file,
                uploaded_file.name
            )

            prompt = build_prompt(
                resume_text,
                job_description
            )

            result = analyze_resume(prompt)

            st.markdown(result)

    else:
        st.warning(
            "Please upload resume and paste job description."
        )