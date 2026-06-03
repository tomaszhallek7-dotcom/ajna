"""Multi-agent orchestration"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

router = APIRouter()


class AgentRole(str, Enum):
    """Agent roles"""
    MAIN = "main"
    ANALYST = "analyst"
    CODER = "coder"
    RESEARCHER = "researcher"


class Agent(BaseModel):
    """Agent model"""
    id: str
    name: str
    role: AgentRole
    status: str
    model: str


class AgentRequest(BaseModel):
    """Request to create or manage agents"""
    name: str
    role: AgentRole
    model: str = "claude"


@router.get("/list")
async def list_agents() -> List[Agent]:
    """List all active agents"""
    try:
        return [
            Agent(
                id="astra-001",
                name="ASTRA",
                role=AgentRole.MAIN,
                status="active",
                model="claude"
            )
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{agent_id}")
async def get_agent(agent_id: str) -> Agent:
    """Get specific agent details"""
    try:
        return Agent(
            id=agent_id,
            name="ASTRA",
            role=AgentRole.MAIN,
            status="active",
            model="claude"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_agent(request: AgentRequest) -> Agent:
    """Create new agent"""
    try:
        return Agent(
            id="agent-new",
            name=request.name,
            role=request.role,
            status="created",
            model=request.model
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
