from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.pipeline import run_ingestion

class HybridRetriever:
    def __init__(self):
        self.embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store=FAISS.load_local("vectorstore/faiss_index",self.embedding,allow_dangerous_deserialization=True)

        self.faiss=self.vector_store.as_retriever(search_kwargs={"k":3})
        #BM25
        documents= run_ingestion()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks=text_splitter.split_documents(documents)
        self.bm25=BM25Retriever.from_documents(chunks)

        self.bm25.k=3
    def retrieve(self,question):


        faiss_docs=self.faiss.invoke(question)
        bm25_docs=self.bm25.invoke(question)

        all_docs=faiss_docs+bm25_docs
        unique_docs=[]
        seen=set()
        for doc in all_docs:

            text=doc.page_content
            if text not in seen:

                unique_docs.append(doc)
                seen.add(text)
    
        return unique_docs[:5]

if __name__=="__main__":
    hybrid_retriever=HybridRetriever()
    question="What is the hotel reimbursement limit?"
    results=hybrid_retriever.retrieve(question)
    for i,doc in enumerate(results,1):
        print(f"Document {i}")
        print(doc.page_content)
        print(doc.metadata)