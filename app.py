import streamlit as st
from extractor import extract_text_from_pdf, extract_text_from_docx, extract_resume_info
from evaluator import evaluate_resume
from summarizer import summarize_resume

st.title("AI Resume Screener")

# File upload
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    # Extract text
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)
    
    # Extract entities
    entities = extract_resume_info(text)
    st.subheader("Extracted Info")
    st.write(entities)
    
    # Evaluate resume
    score = evaluate_resume(text)
    st.subheader("AI Evaluation Score")
    st.write(score)
    
    # Generate summary
    summary = summarize_resume(text)
    st.subheader("Feedback Summary")
    st.write(summary)