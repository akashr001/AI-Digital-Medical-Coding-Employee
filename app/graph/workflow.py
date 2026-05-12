from langgraph.graph import StateGraph

from app.state.state import AgentState

from app.graph.router import route_decision

from app.agents.planner.agent import planner_agent
from app.agents.retriever.agent import retriever_agent
from app.agents.validator.agent import validator_agent
from app.agents.compliance.agent import compliance_agent
from app.agents.audit.agent import audit_agent

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_agent)
workflow.add_node("retriever", retriever_agent)
workflow.add_node("validator", validator_agent)
workflow.add_node("compliance", compliance_agent)
workflow.add_node("audit", audit_agent)

workflow.set_entry_point("planner")

workflow.add_conditional_edges(
    "planner",
    route_decision,
    {
        "retriever": "retriever",
        "validator": "validator"
    }
)

workflow.add_edge("retriever", "validator")
workflow.add_edge("validator", "compliance")
workflow.add_edge("compliance", "audit")

workflow.set_finish_point("audit")

graph = workflow.compile()