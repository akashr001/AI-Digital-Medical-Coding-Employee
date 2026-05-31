from qdrant_client.models import (
    Distance,
    VectorParams
)

from app.vectorstore.client import (
    client,
    COLLECTION_NAME
)

if not client.collection_exists(
    COLLECTION_NAME
):

    client.create_collection(
        collection_name=COLLECTION_NAME,

        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection Created")

else:

    print("Collection Already Exists")