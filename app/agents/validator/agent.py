from langsmith import traceable
from app.models.llm import call_llm
from app.utils.file_loader import load_skill

@traceable(name="validator_agent")
def validator_agent(state):

    skill = load_skill(
        "app/agents/validator/skill.md"
    )

    response = call_llm(
        system_prompt=skill,
        user_query=state["retrieved_context"]
    )

    state["validation"] = response

    return state