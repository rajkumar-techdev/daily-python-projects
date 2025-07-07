import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text=""
        for page in pdf.pages:
            text+=page.extract_text()+"\n"
    return text

def extract_email(text):
    match=re.search(r'[\w\,-]+@[\w\,-]+',text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match=re.search(r'(\+91[-/s]?)?\d[10]',text)
    return match.group(0) if match else "Not found"

def extract_skills(text):
    skills=["python","java","html","css","javascript","sql","django","react","flask","node"]
    found=[skill for skill in skills if skill.lower() in text.lower()]
    return list(set(found)) or ["Not found"]

def main():
    path=input("Enter path to resume pdf: ").strip()
    try:
        text=extract_text_from_pdf(path)
        print("\n Resume Summary:")
        print("Email:",extract_email(text))
        print("Phone: ",extract_phone(text))
        print("Skills:  ",",".join(extract_skills(text)))
    except Exception as e:
        print("Error: ",e)

main()