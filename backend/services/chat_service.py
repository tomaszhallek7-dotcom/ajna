"""Chat service for handling conversations"""
import os
from typing import Optional
from anthropic import Anthropic


class ChatService:
    """Service for handling chat interactions"""
    
    def __init__(self):
        self.claude_client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
        self.conversations = {}
    
    async def process_message(
        self,
        message: str,
        model: str = "claude",
        session_id: Optional[str] = None,
        context: Optional[str] = None
    ) -> dict:
        """Process a chat message and return response"""
        
        if model == "claude":
            return await self._chat_with_claude(message, session_id, context)
        else:
            raise ValueError(f"Unsupported model: {model}")
    
    async def _chat_with_claude(
        self,
        message: str,
        session_id: Optional[str],
        context: Optional[str]
    ) -> dict:
        """Chat with Claude model"""
        try:
            system_prompt = f"""You are ASTRA, an AI-Human Synthesis agent.
You are helpful, professional, and focused on real-time collaboration.
You understand context and maintain conversation history.
{f'Context: {context}' if context else ''}"""
            
            response = self.claude_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            
            return {
                "response": response.content[0].text,
                "model": "claude",
                "session_id": session_id or "default",
                "status": "success"
            }
        except Exception as e:
            return {
                "response": f"Error: {str(e)}",
                "model": "claude",
                "session_id": session_id or "default",
                "status": "error"
            }


chat_service = ChatService()
