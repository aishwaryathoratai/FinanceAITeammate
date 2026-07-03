
from abc import ABC
# creating abstract class that tells python this class to inheritated 
from typing import List
from langchain_groq import ChatGroq
from vectorstore.retriever import HybridRetriever
from schemas import AgentResponse,AgentRequest
import os
from dotenv import load_dotenv

load_dotenv()

class BaseAgent(ABC):
    prompt = None
    def __init__(self):
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", 
                            api_key=os.getenv("GROQ_API_KEY"),temperature=0
        )
        self.retriever = HybridRetriever()
    def retrieve_documents(self, question):

        return self.retriever.retrieve(question)
    def build_context(self, documents):
        return "\n\n".join(
            doc.page_content
            for doc in documents
        )
    def extract_sources(self, documents) -> List[str]:
        return list({
            doc.metadata.get(
                "source",
                "Unknown"
            )
            for doc in documents
        })

    def answer(self, request):
        documents = self.retrieve_documents(
            request.question
        )
        context = self.build_context(
            documents
        )
        formatted_prompt = self.prompt.format(
            context=context,
            question=request.question
        )
        response = self.llm.invoke(
            formatted_prompt
        )
        return AgentResponse(
            answer=response.content,
            sources=self.extract_sources(documents)
        )