from app.agents.retrieval.agent import (
    retrieval_agent
)

state = {
    "patient_note":
    "Patient has diabetes"
}

result = retrieval_agent(
    state
)

print(
    result["retrieved_context"]
)