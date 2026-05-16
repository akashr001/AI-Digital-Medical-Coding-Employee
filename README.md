# AI Digital Medical Coding Employee

An enterprise-style agentic AI service for assisting medical coding workflows. The project exposes a FastAPI API that accepts a medical coding query, routes it through a LangGraph multi-agent workflow, retrieves relevant coding context from a vector database, validates the answer, checks compliance, and returns an auditable response.

## What This Project Does

This system is designed as a digital medical coding employee that can help analyze coding-related questions with a structured, reviewable workflow instead of a single direct LLM response.

The workflow includes:

- Planning the request and deciding whether retrieval is needed
- Retrieving medical code context from Qdrant
- Validating the retrieved or generated coding response
- Applying compliance review
- Producing an audit-friendly final response

## Architecture

The application is built around a FastAPI service and a LangGraph state machine.

```text
Client
  |
  v
FastAPI /analyze
  |
  v
Planner Agent
  |
  +--> Retriever Agent --> Validator Agent --> Compliance Agent --> Audit Agent
  |
  +----------------------> Validator Agent --> Compliance Agent --> Audit Agent
```

## Main Components

- `app/main.py` - FastAPI app entry point with health routes.
- `app/api/routes.py` - API route for `/analyze`.
- `app/graph/workflow.py` - LangGraph workflow definition.
- `app/graph/router.py` - Conditional routing logic after planning.
- `app/agents/` - Specialized agents for planning, retrieval, validation, compliance, and audit.
- `app/models/llm.py` - LiteLLM integration with Ollama.
- `app/vectordb/` - Qdrant vector search and ingestion-related code.
- `app/embeddings/` - Sentence transformer embedding model.
- `app/evaluations/` - Evaluation placeholders for DeepEval and RAGAS.
- `deployment/` - Docker and Kubernetes deployment files.

## Agents

### Planner Agent

Reads the user query and creates a structured plan. The planner decides whether the request should go through retrieval or move directly to validation.

### Retriever Agent

Searches Qdrant for relevant medical coding context and sends that context to the LLM for a retrieval-grounded response.

### Validator Agent

Reviews the retrieved or generated information for correctness and consistency.

### Compliance Agent

Checks whether the response satisfies compliance-oriented requirements for medical coding workflows.

### Audit Agent

Creates the final response object containing the query, retrieved context, validation result, compliance result, and audit output.

## Tech Stack

- Python
- FastAPI
- LangGraph
- LangChain
- LiteLLM
- Ollama
- Qdrant
- Sentence Transformers
- Redis
- LangSmith tracing
- DeepEval and RAGAS for evaluation
- Docker and Kubernetes deployment manifests

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Analyze Medical Coding Query

```http
POST /analyze
Content-Type: application/json
```

Request:

```json
{
  "query": "What ICD-10 code should be used for type 2 diabetes without complications?"
}
```

Response:

```json
{
  "query": "What ICD-10 code should be used for type 2 diabetes without complications?",
  "retrieved_context": "...",
  "validation": "...",
  "compliance": "...",
  "audit": "..."
}
```

## Local Setup

### 1. Create and Activate a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
OLLAMA_BASE_URL=http://localhost:11434
```

Add any other local service keys or tracing configuration required for your environment.

### 4. Start Ollama

```bash
ollama serve
```

Pull the local models used by the project:

```bash
ollama pull llama3.1:8b
ollama pull mistral:7b
```

### 5. Start Qdrant

The retriever expects Qdrant to be available on `localhost:6333`.

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 6. Run the FastAPI App

```bash
uvicorn app.main:app --reload
```

Open the API docs:

```text
http://localhost:8000/docs
```

## Docker

Docker Compose is available under `deployment/docker/docker-compose.yml`.

```bash
cd deployment/docker
docker compose up --build
```

This starts:

- API service
- Qdrant
- Redis

## Kubernetes

Kubernetes manifests are available in `deployment/kubernetes`.

```bash
kubectl apply -f deployment/kubernetes/
```

The manifests include deployments and services for:

- API
- Qdrant
- Redis
- Ollama
- Ingress

## Project Status

The project is evolving from a proof-of-concept agentic AI workflow into an enterprise-style AI systems engineering platform for medical coding assistance.

Current implementation includes:

- Multi-agent orchestration using LangGraph
- Medical RAG pipeline with Qdrant
- LiteLLM + Ollama model integration
- Validation, compliance, and audit workflows
- Docker and Kubernetes deployment setup
- LangSmith tracing and evaluation integration

Recent Infrastructure Upgrades:

- NGINX API Gateway integration
- JWT-based authentication system
- Role-Based Access Control (RBAC)
- API rate limiting and request protection
- Enterprise-style backend restructuring
- Structured logging and observability foundations

Planned Enterprise Features:

- Microservice architecture
- Async task queues and distributed workers
- Event-driven workflows
- OpenTelemetry + Prometheus monitoring
- Envoy/Istio service mesh integration
- Human-in-the-loop medical review workflows
- Advanced RAG optimization and reranking
- CI/CD pipelines and automated testing
- Production-grade healthcare security patterns

This repository is intended for AI systems engineering, platform engineering, and distributed AI workflow demonstration purposes.



## Disclaimer

This project is for software engineering and AI workflow demonstration purposes. It should not be used as a substitute for certified medical coding review, clinical judgment, compliance review, or professional healthcare billing guidance.
