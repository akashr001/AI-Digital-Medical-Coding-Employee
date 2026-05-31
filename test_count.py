from app.vectorstore.client import (
    client,
    COLLECTION_NAME
)

info = client.get_collection(
    COLLECTION_NAME
)

print(info.points_count)

client.close()