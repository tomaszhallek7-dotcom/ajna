"""Agent data models"""
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class AgentRole(str, Enum):
    """Agent roles in the system"""
    MAIN = "main"
    ANALYST = "analyst"
    CODER = "coder"
    RESEARCHER = "researcher"


class Agent(BaseModel):
    """Agent model"""
    id: str
    name: str
    role: AgentRole
    model: str
    status: str


class AgentRequest(BaseModel):
    """Request to create or manage agents"""
    name: str
    role: AgentRole
    model: str = "claude"
