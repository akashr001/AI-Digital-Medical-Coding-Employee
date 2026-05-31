# Medical Coding AI

Medical Coding AI is a FastAPI application that runs a multi-agent medical coding workflow over uploaded clinical documents. It performs OCR, extracts a structured patient note, retrieves coding references from Qdrant, generates candidate medical codes, audits the result, performs QA, and streams each step back to a browser dashboard.

## Features

- FastAPI backend with CORS enabled
- Server-Sent Events endpoint for live agent progress
- LangGraph workflow orchestration
- OCR through Sarvam AI document intelligence
- LLM calls through NVIDIA's OpenAI-compatible API
- Retrieval-augmented coding context using SentenceTransformers and Qdrant
- Static HTML dashboard in `frontend/index.html`
- Optional evaluation modules for Ragas and DeepEval

## Architecture

The main workflow is defined in `app/graph/workflow.py`:

```text
OCR -> Extraction -> Retrieval -> Coding -> Audit -> QA -> Supervisor
```

Each agent stores its output in the shared LangGraph state:

- `ocr`: reads the uploaded document and produces Markdown text
- `extraction`: converts OCR output into a normalized patient note
- `retrieval`: searches the local `medical_codes` Qdrant collection
- `coding`: generates coding recommendations using retrieved context
- `audit`: checks the recommendations against the note and context
- `qa`: reviews the coding and audit output
- `supervisor`: produces the final consolidated report

## Project Structure

```text
app/
  agents/          Agent implementations and system prompts
  api/             FastAPI routes and schemas
  graph/           LangGraph state and workflow
  models/          LLM and embedding model wrappers
  rag/             Knowledge ingestion and retrieval
  vectorstore/     Qdrant client and collection setup
  evaluation/      Ragas and DeepEval helpers
frontend/
  index.html       Static browser dashboard
knowledge/
  icd10/           Sample ICD-10 knowledge data
deployment/
  docker/          Docker assets
  kubernetes/      Kubernetes manifests
documents/         Uploaded or sample clinical documents
```

## Prerequisites

- Python 3.10 or newer
- A running Qdrant instance on `localhost:6333`
- NVIDIA API key for chat completions
- Sarvam AI API key for OCR

The code imports these Python packages:

```text
fastapi
uvicorn
python-multipart
langgraph
langchain
langchain-core
langsmith
qdrant-client
redis
openai
sentence-transformers
sarvamai
watchdog
ragas
deepeval
python-dotenv
pydantic
```

Note: `requirements.txt` is currently empty, while the old README contained a partial dependency list. Install the packages above or update `requirements.txt` before using `pip install -r requirements.txt`.

## Environment Variables

Create a `.env` file in the project root:

```env
NVIDIA_API_KEY=your_nvidia_api_key
NVIDIA_MODEL=minimaxai/minimax-m2.7
SARVAM_API_KEY=your_sarvam_api_key

# Optional, if you use LangSmith tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=medical-coding-ai
```

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install fastapi uvicorn python-multipart langgraph langchain langchain-core langsmith qdrant-client redis openai sentence-transformers sarvamai watchdog ragas deepeval python-dotenv pydantic
```

3. Start Qdrant:

```powershell
docker run -p 6333:6333 -v ${PWD}\qdrant_data:/qdrant/storage qdrant/qdrant
```

4. Create the vector collection:

```powershell
python -m app.vectorstore.create_collection
```

5. Ingest the sample knowledge base:

```powershell
python -m app.rag.ingest
```

## Running the App

Start the FastAPI server:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Open the dashboard by loading:

```text
frontend/index.html
```

The dashboard posts uploaded files to:

```text
http://localhost:8000/code/stream
```

## API

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Medical Coding AI Running"
}
```

### Stream Coding Workflow

```http
POST /code/stream
Content-Type: multipart/form-data
```

Form field:

- `file`: clinical document file, such as PDF, PNG, JPG, JPEG, or TXT

The endpoint returns `text/event-stream` messages. Each event contains the completed graph node and its state update:

```json
{
  "node": "coding",
  "data": {
    "coding_result": "..."
  }
}
```

Example with `curl`:

```powershell
curl.exe -N -X POST "http://localhost:8000/code/stream" -F "file=@documents/Test Medical coding.pdf"
```

## Tests

Several smoke-test scripts are included at the repository root:

```powershell
python test_embedding.py
python test_retrieval.py
python test_workflow.py
python test_full_pipeline.py
```

Some tests call external services or require Qdrant and populated vector data, so make sure the environment variables and local services are configured first.

## Operational Notes

- Uploaded files are saved into `documents/`.
- OCR output is downloaded to `ocr_output.zip` and extracted into `ocr_output/`.
- The Qdrant collection name is `medical_codes`.
- The embedding model is `sentence-transformers/all-MiniLM-L6-v2`, which produces 384-dimensional vectors.
- The frontend is static and does not require a build step.

## Disclaimer

This project is intended as an AI-assisted coding workflow prototype. Medical coding output should be reviewed by qualified professionals before operational, billing, compliance, or clinical use.
