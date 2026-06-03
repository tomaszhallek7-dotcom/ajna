"""ASTRA Configuration Settings"""
import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Backend Configuration
    backend_host: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    backend_port: int = int(os.getenv("BACKEND_PORT", "8000"))
    environment: str = os.getenv("ENVIRONMENT", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # API Keys
    claude_api_key: Optional[str] = os.getenv("CLAUDE_API_KEY")
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # Voice Configuration
    voice_model: str = os.getenv("VOICE_MODEL", "tts-1-hd")
    voice_provider: str = os.getenv("VOICE_PROVIDER", "openai")
    
    # Agent Configuration
    agent_name: str = os.getenv("AGENT_NAME", "ASTRA")
    agent_personality: str = os.getenv("AGENT_PERSONALITY", "professional_helpful")
    max_agents: int = int(os.getenv("MAX_AGENTS", "5"))
    
    # MCP Configuration
    mcp_enabled: bool = os.getenv("MCP_ENABLED", "true").lower() == "true"
    
    # Database
    supabase_url: Optional[str] = os.getenv("SUPABASE_URL")
    supabase_key: Optional[str] = os.getenv("SUPABASE_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
