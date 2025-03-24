import streamlit as st
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file):
  pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.getvalue()))
  text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
