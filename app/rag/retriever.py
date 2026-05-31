from app.models.embedding_model import get_embedding

from app.vectorstore.client import (
    client,
    COLLECTION_NAME
)


def retrieve(query: str):

    vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=3
    )

    return results.points