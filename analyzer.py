import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_resume(text):

    prompt = f"""
    Analyze this resume.

    Resume:
    {text}

    Give:
    1. ATS Score
    2. Strengths
    3. Weaknesses
    4. Suggestions
    """

    response = model.generate_content(prompt)

    return response.text

def match_resume(resume_text, jd_text):

    prompt = f"""
    Compare the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Return:

    Match Score (%)
    Missing Skills
    Matching Skills
    Suggestions
    """

    response = model.generate_content(prompt)

    return response.text

def generate_questions(resume_text):

    prompt = f"""
    Based on this resume,
    generate 10 interview questions.

    Resume:

    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text