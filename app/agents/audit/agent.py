from langsmith import traceable
from app.models.llm import call_llm
from app.utils.file_loader import load_skill

@traceable(name="audit_agent")
def audit_agent(state):

    skill = load_skill(
        "app/agents/audit/skill.md"
    )

    response = call_llm(
        system_prompt=skill,
        user_query=str(state)
    )

    state["audit"] = response

    state["final_response"] = {
        "query": state["query"],
        "retrieved_context": state["retrieved_context"],
        "validation": state["validation"],
        "compliance": state["compliance"],
        "audit": state["audit"]
    }

    return state