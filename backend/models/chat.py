"""Chat models"""
from pydantic import BaseModel
from typing import Optional


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
