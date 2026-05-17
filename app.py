import json

import streamlit as st

from utils.parser import extract_text
from utils.prompts import build_prompt
from utils.llm import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -------------------------
# HEADER
# -------------------------

st.markdown("""
# 📄 AI Resume Analyzer

Optimize resumes for ATS systems using AI.
""")

st.divider()

# -------------------------
# INPUTS
# -------------------------

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

with col2:

    job_description = st.text_area(
        "Paste Job Description",
        height=220
    )

# -------------------------
# ANALYZE
# -------------------------

if st.button(
    "🚀 Analyze Resume",
    use_container_width=True
):

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
            result = result.replace("```json", "").replace("```", "")
            print("result:",type(result), result)
            result = json.loads(result)  # Convert JSON string to Python dict
            print("result:",type(result), result)

            ats_score = int(result["ats_score"])*10
            print("ats_score:", ats_score)

            # -------------------------
            # SCORE SECTION
            # -------------------------

            st.divider()

            score_col1, score_col2 = st.columns([1, 4])

            with score_col1:

                st.metric(
                    "ATS Score",
                    f"{ats_score}/100"
                )

            with score_col2:

                st.progress(ats_score / 100)

                if ats_score >= 80:
                    st.success("Strong ATS compatibility")
                elif ats_score >= 60:
                    st.warning("Moderate ATS compatibility")
                else:
                    st.error("Low ATS compatibility")

            st.divider()

            # -------------------------
            # CONTENT CARDS
            # -------------------------

            col1, col2 = st.columns(2)

            with col1:

                with st.container(border=True):

                    st.subheader("✅ Strengths")

                    for item in result["strengths"]:
                        st.markdown(f"- {item}")

                with st.container(border=True):

                    st.subheader("⚠ Weak Areas")

                    for item in result["weak_areas"]:
                        st.markdown(f"- {item}")

            with col2:

                with st.container(border=True):

                    st.subheader("❌ Missing Skills")

                    for item in result["missing_skills"]:
                        st.markdown(f"- {item}")

                with st.container(border=True):

                    st.subheader("🚀 Improvements")

                    for item in result[
                        "suggested_improvements"
                    ]:
                        st.markdown(f"- {item}")

            st.divider()

            # -------------------------
            # FINAL VERDICT
            # -------------------------

            with st.container(border=True):

                st.subheader("📌 Final Verdict")

                st.write(result["final_verdict"])

    else:

        st.warning(
            "Please upload resume and paste job description."
        )