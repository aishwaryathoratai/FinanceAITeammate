from agents.finance_agent import FinanceAgent
from schemas import AgentRequest

agent = FinanceAgent()

request = AgentRequest(
    question="What is the travel policy?"
)

response = agent.answer(request)

print("Answer:")
print(response.answer)

print("\nSources:")
print(response.sources)