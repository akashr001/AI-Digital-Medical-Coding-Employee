import json
import os
import shutil
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

# Keeping your workflow import intact
from app.graph.workflow import graph

router = APIRouter()


@router.post("/code/stream")
async def stream_code_document(file: UploadFile = File(...)):

    # 1. Create directory if it doesn't exist
    os.makedirs("documents", exist_ok=True)

    file_path = f"documents/{file.filename}"

    # 2. Save the incoming file to disk exactly as before
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 3. Define the real-time event generator
    async def event_generator():
        try:
            # We use graph.astream instead of graph.invoke
            # This yields data immediately as each agent node finishes
            async for chunk in graph.astream({"document_path": file_path}):
                
                # 'chunk' is a dictionary: { "node_name": { "state_variable": "value" } }
                for node_name, state_update in chunk.items():
                    payload = {
                        "node": node_name,
                        "data": state_update
                    }
                    
                    # Package it as a Server-Sent Event (SSE) message
                    yield f"data: {json.dumps(payload)}\n\n"
                    
        except Exception as e:
            # Catching internal graph failures and notifying the frontend safely
            error_payload = {
                "node": "error",
                "data": {"message": str(e)}
            }
            yield f"data: {json.dumps(error_payload)}\n\n"

    # 4. Return the open live stream channel back to the browser
    return StreamingResponse(event_generator(), media_type="text/event-stream")