from app.agents.retrieval.agent import retrieval_agent
from app.agents.coding.agent import coding_agent
from app.agents.audit.agent import audit_agent
from app.agents.qa.agent import qa_agent
from app.agents.supervisor.agent import supervisor_agent

state = {
    "patient_note":
    "Patient has type 2 diabetes."
}

state = retrieval_agent(state)
state = coding_agent(state)
state = audit_agent(state)
state = qa_agent(state)
state = supervisor_agent(state)

print(state["final_report"])