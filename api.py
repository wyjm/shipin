# FastAPI service for Seko AI Video Tool
# Supports deployment as an API service

import os
import sys
import subprocess
import json
from typing import Optional, Dict, Any

# Try to import fastapi, show helpful error if not installed
try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    print("Warning: fastapi not installed. Run: pip install fastapi uvicorn")

# Create FastAPI app
app = FastAPI(
    title="Seko AI Video Tool API",
    description="AI视频创作工具API服务 - 调用Suko API生成策划案和视频",
    version="1.0.0"
)

# Request models
class ProposalRequest(BaseModel):
    prompt: str
    api_key: Optional[str] = None
    project_dir: Optional[str] = "./project"

class VideoRequest(BaseModel):
    doc_id: str
    api_key: Optional[str] = None
    project_dir: Optional[str] = "./project"

class ProposalQueryRequest(BaseModel):
    task_id: str
    api_key: Optional[str] = None
    project_dir: Optional[str] = "./project"
    wait: bool = True
    interval: int = 20

class VideoQueryRequest(BaseModel):
    task_id: str
    api_key: Optional[str] = None
    project_dir: Optional[str] = "./project"
    wait: bool = True
    interval: int = 30

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "message": "Seko AI Video Tool API",
        "status": "running",
        "version": "1.0.0",
        "fastapi_available": FASTAPI_AVAILABLE
    }

@app.get("/health")
@app.get("/api/health")
def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "seko-ai-video",
        "fastapi_installed": FASTAPI_AVAILABLE
    }

def run_script(script_name: str, args: list, api_key: Optional[str] = None, cwd: Optional[str] = None) -> Dict[str, Any]:
    """Run a Python script and return the result"""
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    
    if not os.path.exists(script_path):
        return {"error": f"Script not found: {script_name}"}
    
    # Build command
    cmd = ["python3", script_path] + args
    
    # Add API key if provided
    if api_key:
        cmd.extend(["--seko_api_key", api_key])
    
    # Set environment
    env = os.environ.copy()
    if api_key:
        env["SEKO_API_KEY"] = api_key
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            cwd=cwd or BASE_DIR,
            env=env
        )
        
        # Try to parse JSON output
        try:
            output = json.loads(result.stdout)
        except json.JSONDecodeError:
            output = {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        
        return output
        
    except subprocess.TimeoutExpired:
        return {"error": "Script execution timeout"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/generate_proposal")
def generate_proposal(req: ProposalRequest):
    """Generate video proposal"""
    api_key = req.api_key or os.environ.get("SEKO_API_KEY")
    
    if not api_key:
        return {"error": "SEKO_API_KEY is required. Please provide api_key in request or set SEKO_API_KEY environment variable."}
    
    # Create project directory if needed
    os.makedirs(req.project_dir, exist_ok=True)
    
    result = run_script(
        "gen_proposal.py",
        ["--prompt", req.prompt],
        api_key=api_key,
        cwd=req.project_dir
    )
    
    return result

@app.post("/api/get_proposal")
def get_proposal(req: ProposalQueryRequest):
    """Get proposal result"""
    api_key = req.api_key or os.environ.get("SEKO_API_KEY")
    
    if not api_key:
        return {"error": "SEKO_API_KEY is required"}
    
    # Build arguments
    args = ["--taskid", req.task_id]
    
    if req.wait:
        args.append("--wait")
        args.extend(["--interval", str(req.interval)])
    
    args.extend(["--download", os.path.join(req.project_dir, "assets")])
    args.extend(["--output", os.path.join(req.project_dir, "proposal_result.json")])
    
    result = run_script("get_proposal.py", args, api_key=api_key, cwd=req.project_dir)
    
    return result

@app.post("/api/generate_video")
def generate_video(req: VideoRequest):
    """Generate video from proposal"""
    api_key = req.api_key or os.environ.get("SEKO_API_KEY")
    
    if not api_key:
        return {"error": "SEKO_API_KEY is required"}
    
    result = run_script(
        "gen_video.py",
        ["--docid", req.doc_id],
        api_key=api_key,
        cwd=req.project_dir
    )
    
    return result

@app.post("/api/get_video")
def get_video(req: VideoQueryRequest):
    """Get video result"""
    api_key = req.api_key or os.environ.get("SEKO_API_KEY")
    
    if not api_key:
        return {"error": "SEKO_API_KEY is required"}
    
    # Build arguments
    args = ["--taskid", req.task_id]
    
    if req.wait:
        args.append("--wait")
        args.extend(["--interval", str(req.interval)])
    
    args.extend(["--download", os.path.join(req.project_dir, "outputs")])
    args.extend(["--output", os.path.join(req.project_dir, "video_result.json")])
    
    result = run_script("get_video.py", args, api_key=api_key, cwd=req.project_dir)
    
    return result

# For local testing
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)