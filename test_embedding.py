from app.models.embedding_model import get_embedding

vector = get_embedding("diabetes")

print("Length:", len(vector))
print("First 5 values:", vector[:5])