from app.graph.workflow import graph

result = graph.invoke(
    {
        "patient_note":
        "Patient has type 2 diabetes."
    }
)

print(
    result["final_report"]
)