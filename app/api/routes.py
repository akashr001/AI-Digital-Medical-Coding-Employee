from fastapi import APIRouter
from app.schemas.request_response import QueryRequest
from app.graph.workflow import graph

router = APIRouter()

@router.post("/analyze")
def analyze(request: QueryRequest):

    initial_state = {
        "query": request.query,
        "plan": {},
        "retrieved_context": "",
        "validation": "",
        "compliance": "",
        "audit": "",
        "final_response": "",
        "error": ""
    }

    result = graph.invoke(initial_state)

    return result["final_response"]