import streamlit as st
import pymupdf
from langchain_google_genai import ChatGoogleGenerativeAI
import scrubadub
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that compares user resume content with job description, give rating to resume, selection chances of resume and area for improvement, and strictly give response in 100 to 200 words.",
    ),
]

def generate_response(job_description, resume_file):
    if job_description:
        pass
        # st.write("Job Description: ", job_description)
        
    if resume_file:       
        doc = pymupdf.open(stream = resume_file) 
        resume_content = ""
        for page in doc:
            resume_content += page.get_text()
            
        # st.write("Resume content: ", resume_content)
        parsed_resume_content = scrubadub.clean(resume_content)
        # st.write("Resume after removing PII:", parsed_resume_content)
            
        prompt = f"""
        <job_description>
        {job_description}
        </job_description>
        
        <resume_content>
        {parsed_resume_content}
        </resume_content>
        
        """
        messages.append(("human", prompt))
        st.write("AI Response: ", llm.stream(messages))
        