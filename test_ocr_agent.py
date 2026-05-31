from app.agents.ocr.agent import (
    ocr_agent
)

state = {

    "document_path":
    "documents/neuro.jpg"

}

state = ocr_agent(
    state
)

print(
    state["ocr_text"]
)