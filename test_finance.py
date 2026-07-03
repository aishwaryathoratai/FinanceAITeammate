from schemas import AgentRequest
from agents.finance_agent import FinanceAgent

agent = FinanceAgent()

request = AgentRequest(
    question="How can I claim travel reimbursement?"
)

response = agent.answer(request)

print(response.answer)
print(response.sources)