import spacy
from PyPDF2 import PdfReader
from docx import Document

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_resume_info(text):
    doc = nlp(text)
    entities = {"SKILLS": [], "EXPERIENCE": [], "EDUCATION": []}
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            entities["SKILLS"].append(ent.text)
        elif ent.label_ == "ORG":
            entities["EXPERIENCE"].append(ent.text)
        elif ent.label_ == "EDUCATION":
            entities["EDUCATION"].append(ent.text)
    return entities