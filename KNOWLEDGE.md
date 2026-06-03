# AJNA - Wiedza z AISITE

## Core Koncepty
- **AI-Human Synthesis**: Platforma gdzie człowiek i AI pracują razem w real-time
- **Multi-Model Support**: Claude, ChatGPT, Gemini, Ollama (local LLM)
- **Workflow Automation**: n8n integracja dla automatyzacji procesu
- **Development Workspace**: IDE-like environment dla prototypowania

## UX Principles
1. Real-time collaboration (Human prompt → AI response → Human iteration)
2. Model switching on the fly (wybór AI w locie)
3. Knowledge preservation (context carryover między sesji)
4. Automation triggers (n8n workflows triggered by AI outputs)

## Key Features (AJNA v1)
- Chat interface (multi-turn conversation)
- Model selector (Claude, GPT, Gemini, Ollama)
- Prompt templates/history
- Export results (JSON, Markdown, Code)
- Integrations: n8n, potential zapier
- Local mode (Ollama self-hosted)

## Architecture (Clean, No Bloat)
✅ Clean API separation
✅ Serverless backend
✅ Free DB for persistence
✅ Modular AI integrations
❌ No monolithic frontend
❌ No hard-coded API keys
❌ No single model dependency
