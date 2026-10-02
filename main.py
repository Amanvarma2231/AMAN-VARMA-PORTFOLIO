import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

from backend.ai_engine import AMAN_PROFILE, analyze_text_nlp, generate_prompt_response, chat_with_aman_ai
from backend.api_tester import get_available_endpoints, execute_simulated_endpoint
from backend.contact import ContactMessage, save_contact_message

app = FastAPI(
    title="Aman Varma - Portfolio API",
    description="Backend API powering Aman Varma's Python, FastAPI, GenAI & NLP Engineer Portfolio.",
    version="1.0.0"
)

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Models
class NLPRequest(BaseModel):
    text: str = Field(..., description="Text content to analyze")

class PromptRequest(BaseModel):
    prompt: str = Field(..., description="User prompt for LLM processing")
    system_prompt: Optional[str] = Field(default="", description="System instruction persona")
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=1.5)
    mode: Optional[str] = Field(default="assistant")

class ChatRequest(BaseModel):
    message: str = Field(..., description="Question for Aman AI Assistant")

class SandboxExecutionRequest(BaseModel):
    endpoint_id: str
    payload: Optional[Dict[str, Any]] = None

# API Endpoints
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Aman Varma Portfolio Backend",
        "version": "1.0.0",
        "stack": ["Python 3.13", "FastAPI", "Uvicorn", "NLP Engine", "GenAI Studio"],
        "endpoints_active": True
    }

@app.get("/api/profile")
async def get_profile():
    return AMAN_PROFILE

@app.get("/api/download-resume")
async def download_resume():
    resume_path = os.path.join(os.path.dirname(__file__), "frontend", "assets", "Aman_Varma_Resume.pdf")
    if os.path.exists(resume_path):
        return FileResponse(
            path=resume_path,
            filename="Aman_Varma_Resume.pdf",
            media_type="application/pdf"
        )
    raise HTTPException(status_code=404, detail="Resume file not found.")


@app.post("/api/contact")
async def handle_contact(msg: ContactMessage):
    result = save_contact_message(msg)
    return result

@app.post("/api/ai/nlp-analyze")
async def run_nlp_analysis(req: NLPRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")
    res = analyze_text_nlp(req.text)
    return res

@app.post("/api/ai/genai-prompt")
async def run_genai_prompt(req: PromptRequest):
    if not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt field cannot be empty.")
    res = generate_prompt_response(
        prompt=req.prompt,
        system_prompt=req.system_prompt or "",
        temperature=req.temperature or 0.7,
        mode=req.mode or "assistant"
    )
    return res

@app.post("/api/ai/chat")
async def chat_assistant(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message field cannot be empty.")
    answer = chat_with_aman_ai(req.message)
    return {"reply": answer}

@app.get("/api/sandbox/endpoints")
async def list_sandbox_endpoints():
    return {"endpoints": get_available_endpoints()}

@app.post("/api/sandbox/execute")
async def run_sandbox_endpoint(req: SandboxExecutionRequest):
    res = execute_simulated_endpoint(req.endpoint_id, req.payload)
    return res

# Mount static directory if it exists
static_dir = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    index_path = os.path.join(os.path.dirname(__file__), "frontend", "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Aman Varma Portfolio Backend is Running! (index.html starting...)</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
