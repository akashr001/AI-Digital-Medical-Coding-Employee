from app.models.llm import (
    call_llm
)


def extraction_agent(
    state
):

    print(
        "Extraction Agent Started"
    )

    ocr_text = state[
        "ocr_text"
    ]

    system_prompt = """
You are a Clinical Document
Extraction Agent.

Convert OCR text into a
clean clinical summary.

Extract:

- Diagnoses
- Symptoms
- Medications
- Procedures
- Medical History
- Clinical Findings

Rules:

1. Remove OCR noise.
2. Do not hallucinate.
3. Keep only medically relevant information.
4. Create a coding-ready patient note.

Output Format:

Patient Summary:
...

Diagnoses:
...

Symptoms:
...

Medications:
...

Procedures:
...

Clinical Findings:
...
"""

    print(
        "Calling NVIDIA API"
    )

    patient_note = (
        call_llm(
            system_prompt=
            system_prompt,
            user_query=
            ocr_text
        )
    )

    state[
        "patient_note"
    ] = patient_note

    print(
        "Extraction Completed"
    )

    return state