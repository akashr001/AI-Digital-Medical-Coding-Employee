from app.models.llm import call_llm
from langsmith import traceable

@traceable(
    name="qa_agent"
)
def qa_agent(state):

    print("QA Agent Started")

    patient_note = state["patient_note"]

    coding_result = state["coding_result"]

    audit_result = state["audit_result"]

    with open(
        "app/agents/qa/skill.md",
        "r",
        encoding="utf-8"
    ) as f:

        skill = f.read()

    prompt = f"""
Patient Note:

{patient_note}


Coding Result:

{coding_result}


Audit Result:

{audit_result}
"""

    print("Calling QA LLM")

    response = call_llm(
        system_prompt=skill,
        user_query=prompt
    )

    print("QA Completed")

    state["qa_result"] = response

    return state