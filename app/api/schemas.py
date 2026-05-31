from pydantic import BaseModel


class CodingResponse(BaseModel):

    status: str

    ocr_text: str

    patient_note: str

    coding_result: str

    audit_result: str

    qa_result: str

    final_report: str