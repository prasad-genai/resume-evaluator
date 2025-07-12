import streamlit as st
from utils import ai
from rate_limiting import is_rate_limited

st.set_page_config(
    page_title='Resume Evaluator',
    page_icon='🤗'
)

st.title("Resume Evaluator")

# Job Description
job_description = st.text_area(label="Enter job description")

# Resume file uploader
resume_file = st.file_uploader(label="Upload your resume PDF file", accept_multiple_files=False)

if st.button("Evaluate"):
    if is_rate_limited():
        st.warning("Rate limit exceeded. You are allowed 1 request per second. Please try again later.")
    else:
        ai.generate_response(job_description, resume_file)
 