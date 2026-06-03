# ASTRA v2 - Setup & Installation Guide

## 🎯 Overview

ASTRA v2 to zaawansowany system AI-Human Synthesis z możliwościami:
- 🗣️ Voice synthesis i transcription
- 🤖 Multi-agent orchestration
- 🧠 Real-time idea synthesis
- 🔌 MCP integration
- 📚 Document processing

## 📦 Installation

### 1. Clone & Setup
```bash
git clone https://github.com/tomaszhallek7-dotcom/ajna.git
cd ajna
git checkout feature/astra-v2
```

### 2. Python Backend
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys
```

### 3. Frontend Setup
```bash
npm install
```

### 4. Run ASTRA v2

**Terminal 1 - Backend:**
```bash
python backend/main.py
# Server runs on http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
npm run dev
# Frontend runs on http://localhost:5173
```

## 🔧 Configuration

Edytuj `.env` ze swoimi kluczami API:

```env
# Anthropic Claude
CLAUDE_API_KEY=your_key_here

# OpenAI (dla GPT-4, voice)
OPENAI_API_KEY=your_key_here

# Google Gemini
GEMINI_API_KEY=your_key_here
```

## 📚 API Endpoints

### Chat
```
POST /api/chat/
Body: {"message": "Hello", "model": "claude"}
```

### Voice
```
POST /api/voice/synthesize
Body: {"text": "Hello world", "voice": "nova"}

POST /api/voice/transcribe
File: audio.wav
```

### Synthesis
```
POST /api/synthesis/merge
Body: {"human_input": "Your idea", "models": ["claude"]}
```

### Agents
```
GET /api/agents/list
GET /api/agents/{agent_id}
POST /api/agents/create
```

## 🚀 Next Steps (TODO)

- [ ] Implement OpenAI TTS integration
- [ ] Add Whisper speech-to-text
- [ ] Multi-agent coordination with agentscope
- [ ] Document processing pipeline
- [ ] MCP server tools
- [ ] Supabase database integration
- [ ] WebSocket real-time chat
- [ ] Voice streaming
- [ ] Agent memory system
- [ ] Skills marketplace

## 📝 Project Structure

```
ajna/
├── backend/
│   ├── core/
│   │   └── config.py       # Configuration
│   ├── models/             # Data models
│   ├── services/           # Business logic
│   ├── routes/             # API endpoints
│   └── main.py            # FastAPI app
├── src/
│   ├── components/         # React components
│   └── App.tsx            # Main React app
├── requirements.txt        # Python dependencies
├── package.json           # Node dependencies
└── .env.example           # Environment template
```

## 🐛 Troubleshooting

**Backend won't start:**
```bash
# Clear cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name '*.pyc' -delete
```

**CORS errors:**
Backend już ma CORS middleware, upewnij się że frontend działa na http://localhost:5173

## 📞 Support

Jeśli napotkasz problemy, sprawdź:
- API keys w `.env`
- Python version (3.10+)
- Node version (16+)
- Logi backendu (port 8000)
