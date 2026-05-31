from app.models.llm import call_llm
from langsmith import traceable

@traceable(
    name="audit_agent"
)

def audit_agent(state):

    print("Audit Agent Started")

    patient_note = state["patient_note"]

    retrieved_context = state[
        "retrieved_context"
    ]

    coding_result = state[
        "coding_result"
    ]

    with open(
        "app/agents/audit/skill.md",
        "r",
        encoding="utf-8"
    ) as f:

        skill = f.read()

    prompt = f"""
Patient Note:

{patient_note}


Retrieved Context:

{retrieved_context}


Coding Agent Output:

{coding_result}
"""

    print("Calling Audit LLM")

    response = call_llm(
        system_prompt=skill,
        user_query=prompt
    )

    print("Audit Completed")

    state["audit_result"] = response

    return state