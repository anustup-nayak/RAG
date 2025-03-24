import streamlit as st
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file (BytesIO): The PDF file in bytes.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.getvalue()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"An error occurred while extracting text: {e}")
        return ""

# Streamlit app
def main():
    st.title("PDF Text Extractor")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.info("Extracting text from the uploaded PDF file...")
        extracted_text = extract_text_from_pdf(uploaded_file)
        if extracted_text:
            st.text_area("Extracted Text", extracted_text, height=300)
        else:
            st.warning("No text could be extracted from the PDF file.")

if __name__ == "__main__":
    main()
