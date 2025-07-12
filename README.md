# 📄 Resume Evaluator App

An intelligent resume evaluation web app built with **Streamlit**, **LangChain**, and **Gemini LLM**, which analyzes a resume against a job description and provides a **rating**, **summary**, and **feedback** for improvement — while keeping sensitive information safe.

---

## 🔧 Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🚀 How to Run the Application
```bash
streamlit run app.py
```


## Features
- 📝 Upload a resume PDF and input a job description

- 🤖 Uses LangChain and Gemini model to:

    - Evaluate the resume

    - Give a score, summary, and custom feedback

- 🛡️ Automatically removes PII (Personally Identifiable Information) using scrubadub before sending data to the LLM

- 📄 Extracts structured data from PDF using PyMuPDF

- ⚙️ Implements rate limiting to restrict overuse (5 requests per minute per user)

## Security
This app ensures user data privacy by:
- Removing PII from resumes
- Never storing or logging personal information
- Limiting LLM exposure to sanitized content only
- Implemented rate limiting