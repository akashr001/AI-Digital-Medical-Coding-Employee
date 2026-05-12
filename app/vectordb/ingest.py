from qdrant_client import QdrantClient
from app.embeddings.embedding_model import embedding_model

client = QdrantClient("localhost", port=6333)

documents = [
    "E11.9 - Type 2 diabetes mellitus without complications",
    "I10 - Essential primary hypertension"
]

vectors = embedding_model.encode(documents)