from langchain_groq import ChatGroq
from prompts.prompts import ROUTER_PROMPT
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()
from dotenv import load_dotenv
import os

load_dotenv()


class RouteDecision(BaseModel):
    agent: str = Field(
        description="Selected agent (policy, finance, or support)"
    )
class SupervisorAgent:
    def __init__(self):
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", 
                            api_key=os.getenv("GROQ_API_KEY"),temperature=0)
        self.route=self.llm.with_structured_output(RouteDecision)
    def route_query(self,question:str):
        prompt=ROUTER_PROMPT.format(question=question)
        response=self.route.invoke(prompt)
        print(f"selected agent:{response.agent}")
        return response.agent
if __name__ == "__main__":

    supervisor = SupervisorAgent()

    question = "Show me HR email regarding travel"

    route = supervisor.route_query(question)

    print(route)
