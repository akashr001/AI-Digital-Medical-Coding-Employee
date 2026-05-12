from langsmith import traceable
from app.models.llm import call_llm
from app.utils.file_loader import load_skill

@traceable(name="compliance_agent")
def compliance_agent(state):

    skill = load_skill(
        "app/agents/compliance/skill.md"
    )

    response = call_llm(
        system_prompt=skill,
        user_query=state["validation"]
    )

    state["compliance"] = response

    return state