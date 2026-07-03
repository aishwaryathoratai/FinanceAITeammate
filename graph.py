from typing import TypedDict,List
from langgraph.graph import StateGraph,START,END
from schemas import AgentRequest,AgentResponse
from agents.supervisor_agent import SupervisorAgent
from agents.finance_agent import FinanceAgent
from agents.policy_agent import PolicyAgent
from agents.support_agent import SupportAgent

class AgentState(TypedDict):
    question:str
    route:str
    answer:str
    sources: List[str]

supervisor = SupervisorAgent()
finance_agent = FinanceAgent()
policy_agent = PolicyAgent()
support_agent = SupportAgent()

#create nodes

def supervisor_node(state:AgentState):
    route = supervisor.route_query(state["question"])
    return {"route":route}
    

def finance_node(state:AgentState):
    request=AgentRequest(question=state['question'])
    response=finance_agent.answer(request)
    return{"answer":response.answer,
           "sources":response.sources}

def policy_node(state:AgentState):
    request=AgentRequest(question=state['question'])
    response=policy_agent.answer(request)
    return {"answer":response.answer,
            "sources":response.sources}

def support_node(state:AgentState):
    request=AgentRequest(question=state['question'])
    response=support_agent.answer(request)
    return {"answer":response.answer,
            "sources":response.sources}

def route_question(state:AgentState):
    return state["route"]

#build graph
workflow=StateGraph(AgentState)

workflow.add_node("supervisor",supervisor_node)
workflow.add_node("finance",finance_node)
workflow.add_node("policy",policy_node)
workflow.add_node("support",support_node)
workflow.set_entry_point("supervisor")
workflow.add_conditional_edges("supervisor",route_question,
                               {"finance": "finance",
                                 "policy": "policy",
                                "support": "support"})

#add edges
workflow.add_edge("finance",END)
workflow.add_edge("policy",END)
workflow.add_edge("support",END)

graph=workflow.compile()

if __name__== "__main__":
    result=graph.invoke({"question":"after building this graph.py what next"})
    print("\nAnswer:\n")
    print(result["answer"])

    print("\nSources:\n")
    print(result["sources"])
