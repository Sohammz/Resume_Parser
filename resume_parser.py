import pdfplumber
import docx

def extract_text(path):

    text = ""

    if path.endswith(".pdf"):

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()

    elif path.endswith(".docx"):

        doc = docx.Document(path)

        for para in doc.paragraphs:
            text += para.text

    elif path.endswith(".txt"):

        with open(path,"r",encoding="utf-8") as f:
            text = f.read()

    return text.lower()