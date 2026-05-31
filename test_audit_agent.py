from app.agents.retrieval.agent import (
    retrieval_agent
)

from app.agents.coding.agent import (
    coding_agent
)

from app.agents.audit.agent import (
    audit_agent
)

state = {
    "patient_note":
    "Patient has type 2 diabetes."
}

state = retrieval_agent(state)

state = coding_agent(state)

state = audit_agent(state)

print(
    state["audit_result"]
)