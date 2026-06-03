"""ASTRA v2 Main Backend Server"""
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from backend.core.config import settings
from backend.routes import chat, voice, synthesis, agents

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="ASTRA v2",
    description="AI-Human Synthesis Workspace with Voice Agent",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(voice.router, prefix="/api/voice", tags=["voice"])
app.include_router(synthesis.router, prefix="/api/synthesis", tags=["synthesis"])
app.include_router(agents.router, prefix="/api/agents", tags=["agents"])


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "name": "ASTRA v2",
        "status": "active",
        "version": "2.0.0",
        "agent": "ASTRA (AI-Synthesis Tactical Response Agent)"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "voice_enabled": True,
        "agents_active": 1,
        "models_available": ["claude", "gpt-4", "gemini"]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.backend_host,
        port=settings.backend_port,
        reload=settings.environment == "development"
    )
