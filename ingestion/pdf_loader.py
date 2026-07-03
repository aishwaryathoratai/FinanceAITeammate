from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_pdfs(pdf_folder: str):
    documents = []          
    pdf_folder = Path(pdf_folder)
    for file in pdf_folder.glob("*.pdf"):
        loader = PyPDFLoader(str(file))  
        docs = loader.load()
        documents.extend(docs)
    return documents