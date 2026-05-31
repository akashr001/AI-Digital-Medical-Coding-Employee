from app.rag.retriever import retrieve

results = retrieve(
    "patient has diabetes"
)

for item in results:
    print(item.payload)