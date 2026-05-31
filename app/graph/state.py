from typing import TypedDict

class AgentState(TypedDict):

    document_path: str

    ocr_text: str

    patient_note: str

    retrieved_context: list

    coding_result: str

    audit_result: str

    qa_result: str

    final_report: str