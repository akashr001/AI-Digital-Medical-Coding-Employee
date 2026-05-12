from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Enterprise Agentic Medical AI",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Enterprise Agentic Medical AI Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}