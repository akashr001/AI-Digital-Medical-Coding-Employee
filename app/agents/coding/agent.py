from app.models.llm import call_llm
from langsmith import traceable

@traceable(
    name="coding_agent"
)

def coding_agent(state):

    print("Coding Agent Started")

    patient_note = state["patient_note"]

    retrieved_context = state[
        "retrieved_context"
    ]

    print("Retrieved Context Loaded")

    with open(
        "app/agents/coding/skill.md",
        "r",
        encoding="utf-8"
    ) as f:

        skill = f.read()

    print("Calling NVIDIA API")

    response = call_llm(
        system_prompt=skill,
        user_query=f"""
Patient Note:

{patient_note}

Retrieved Context:

{retrieved_context}
"""
    )

    print("Response Received")

    state["coding_result"] = response

    return state