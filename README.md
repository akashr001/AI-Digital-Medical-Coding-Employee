# Enterprise Agentic Medical AI

## Start Ollama
ollama serve

## Pull Models
ollama pull llama3.1:8b
ollama pull mistral:7b

## Install Requirements
pip install -r requirements.txt

## Run FastAPI
uvicorn app.main:app --reload

## Run Docker
docker compose up

## Run Kubernetes
kubectl apply -f deployment/kubernetes/