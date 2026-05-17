def build_prompt(resume_text, job_description):

    return f"""
You are an elite ATS resume reviewer.

Analyze the resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

IMPORTANT:
Return ONLY valid JSON.

Format:
{{
    "ats_score": number,
    "missing_skills": [],
    "strengths": [],
    "weak_areas": [],
    "suggested_improvements": [],
    "final_verdict": ""
}}
"""