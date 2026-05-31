from app.rag.retriever import retrieve
from langsmith import traceable

@traceable(
    name="retrieval_agent"
)

def retrieval_agent(state):

    patient_note = state["patient_note"]

    results = retrieve(patient_note)

    retrieved_context = []

    for item in results:

        retrieved_context.append(
            item.payload
        )

    state["retrieved_context"] = (
        retrieved_context
    )

    return state