from app.models.llm import call_llm
from langsmith import traceable


@traceable(
    name="extraction_agent"
)
def extraction_agent(state):

    print(
        "Extraction Agent Started"
    )

    ocr_text = state[
        "ocr_text"
    ]

    with open(
        "app/agents/extraction/skill.md",
        "r",
        encoding="utf-8"
    ) as f:

        skill = f.read()

    prompt = f"""
OCR Output:

{ocr_text}
"""

    print(
        "Calling Extraction LLM"
    )

    response = call_llm(
        system_prompt=skill,
        user_query=prompt
    )

    print(
        "Extraction Completed"
    )

    state[
        "patient_note"
    ] = response

    return state