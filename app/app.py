import streamlit as st

st.set_page_config(
    page_title='Resume Evaluator',
    page_icon='🤗'
)

st.title("Resume Evaluator")

# Job Description
st.text_area(label="Enter job description")

# Resume file uploader
resume_file = st.file_uploader(label="Upload your resume", accept_multiple_files=False)

st.button("Evaluate")