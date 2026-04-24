# FastAPI service configuration for LangChain deployment
# This allows the CLI tool to be deployed as an API service

from fastapi import FastAPI
from pydantic import BaseModel
import os
import subprocess
import json

app = FastAPI(title="Seko AI Video Tool API")

class ProposalRequest(BaseModel):
    prompt: str
    api_key: str = None

class VideoRequest(BaseModel):
    doc_id: str
    api_key: str = None

@app.get("/")
def root():
    return {"message": "Seko AI Video Tool API", "status": "running"}

@app.post("/api/generate_proposal")
def generate_proposal(req: ProposalRequest):
    api_key = req.api_key or os.environ.get("SEKO_API_KEY")
    if not api_key:
        return {"error": "SEKO_API_KEY required"}
    
    result = subprocess.run(
        ["python3", "scripts/gen_proposal.py", "--prompt", req.prompt, "--seko_api_key", api_key],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

@app.get("/api/health")
def health():
    return {"status": "healthy"}