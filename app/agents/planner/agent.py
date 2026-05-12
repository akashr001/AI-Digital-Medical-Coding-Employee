from langsmith import traceable
from app.models.llm import call_llm
from app.utils.file_loader import load_skill
from app.utils.parser import parse_json_response

@traceable(name="planner_agent")
def planner_agent(state):

    skill = load_skill(
        "app/agents/planner/skill.md"
    )

    response = call_llm(
        system_prompt=skill,
        user_query=state["query"]
    )

    state["plan"] = parse_json_response(response)

    return state