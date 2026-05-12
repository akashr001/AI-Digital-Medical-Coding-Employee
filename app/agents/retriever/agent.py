from langsmith import traceable
from app.models.llm import call_llm
from app.utils.file_loader import load_skill
from app.vectordb.search import search_documents

@traceable(name="retriever_agent")
def retriever_agent(state):

    skill = load_skill(
        "app/agents/retriever/skill.md"
    )

    docs = search_documents(state["query"])

    context = "\n".join(
        [doc.payload["text"] for doc in docs]
    )

    response = call_llm(
        system_prompt=skill,
        user_query=context
    )

    state["retrieved_context"] = response

    return state