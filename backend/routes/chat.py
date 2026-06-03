"""Chat endpoint handler"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from backend.services.chat_service import chat_service

router = APIRouter()


class ChatRequest(BaseModel):
    """Chat request model"""
    message: str
    model: str = "claude"
    context: Optional[str] = None
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Chat response model"""
    response: str
    model: str
    session_id: str
    timestamp: str


@router.post("/")
async def chat(request: ChatRequest) -> ChatResponse:
    """Handle chat messages"""
    try:
        result = await chat_service.process_message(
            message=request.message,
            model=request.model,
            session_id=request.session_id,
            context=request.context
        )
        
        return ChatResponse(
            response=result["response"],
            model=result["model"],
            session_id=result["session_id"],
            timestamp=datetime.utcnow().isoformat() + "Z"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
