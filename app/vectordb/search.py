from qdrant_client import QdrantClient
from app.embeddings.embedding_model import embedding_model

client = QdrantClient(
    "localhost",
    port=6333
)

def search_documents(query):

    query_vector = embedding_model.encode(query)

    results = client.search(
        collection_name="medical_docs",
        query_vector=query_vector,
        limit=3
    )

    return results