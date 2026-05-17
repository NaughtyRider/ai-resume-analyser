import os
import streamlit as st

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
try:
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )
except Exception as e:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

def analyze_resume(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content