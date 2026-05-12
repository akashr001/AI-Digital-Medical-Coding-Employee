from typing import TypedDict

class AgentState(TypedDict):
    query: str
    plan: dict
    retrieved_context: str
    validation: str
    compliance: str
    audit: str
    final_response: str
    error: str