from app.agents.retrieval.agent import (
    retrieval_agent
)

from app.agents.coding.agent import (
    coding_agent
)

state = {
    "patient_note":
    "Patient has type 2 diabetes."
}

state = retrieval_agent(
    state
)

state = coding_agent(
    state
)

print(
    state["coding_result"]
)