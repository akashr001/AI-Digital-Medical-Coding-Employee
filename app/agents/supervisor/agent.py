from app.models.llm import call_llm
from langsmith import traceable


@traceable(
    name="supervisor_agent"
)

def supervisor_agent(state):

    print("Supervisor Agent Started")

    patient_note = state["patient_note"]

    coding_result = state["coding_result"]

    audit_result = state["audit_result"]

    qa_result = state["qa_result"]

    with open(
        "app/agents/supervisor/skill.md",
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


QA Result:

{qa_result}
"""

    print("Calling Supervisor LLM")

    response = call_llm(
        system_prompt=skill,
        user_query=prompt
    )

    print("Supervisor Completed")

    state["final_report"] = response

    return state