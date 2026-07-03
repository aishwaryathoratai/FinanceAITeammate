
from langchain_community.vectorstores import FAISS
from ingestion.pipeline import run_ingestion
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter 


def create_vector_db():
    documents= run_ingestion()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_db=FAISS.from_documents(docs,embedding)
    vector_db.save_local("vectorstore/faiss_index")

    
print("Vector database created and saved successfully.")

if __name__ == "__main__":
    create_vector_db()