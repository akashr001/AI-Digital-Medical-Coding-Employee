from qdrant_client.models import PointStruct

from app.models.embedding_model import (
    get_embedding
)

from app.vectorstore.client import (
    client,
    COLLECTION_NAME
)


def ingest_documents():

    with open(
        "knowledge/icd10/sample.txt",
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.readlines()

    points = []

    for idx, line in enumerate(lines):

        if not line.strip():
            continue

        code, description = (
            line.strip().split("|")
        )

        vector = get_embedding(
            description
        )

        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "code": code,
                    "description":
                    description
                }
            )
        )

    client.upsert(
        collection_name=
        COLLECTION_NAME,
        points=points
    )

    print(
        "Ingestion Complete"
    )


if __name__ == "__main__":

    ingest_documents()

    client.close()