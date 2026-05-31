from app.graph.workflow import graph

result = graph.invoke(
    {
        "document_path":
        "documents/neuro.jpg"
    }
)

print(
    result["final_report"]
)