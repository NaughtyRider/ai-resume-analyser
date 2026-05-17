from PyPDF2 import PdfReader
from docx import Document

def extract_text(file, filename):
    text = ""

    if filename.endswith(".pdf"):

        pdf = PdfReader(file)

        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    elif filename.endswith(".docx"):

        doc = Document(file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text