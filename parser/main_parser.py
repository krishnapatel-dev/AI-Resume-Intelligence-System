from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

def parse_resume(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_pdf_text(file)
    elif filename.endswith(".docx"):
        return extract_docx_text(file)
    else:
        return "Unsupported file format"