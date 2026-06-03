# AJNA 🧠
## AI-Human Synthesis Workspace

**Real-time collaboration between humans and artificial intelligence.**

AJNA is a clean, serverless platform designed for seamless human-AI interaction. Switch between models (Claude, GPT-4, Gemini, Ollama), maintain conversation context, and synthesize ideas together.

### Features
- ✅ **Multi-Model Support** - Claude, GPT-4, Gemini, local Ollama
- ✅ **Real-Time Synthesis** - Human + AI ideas merge in real-time
- ✅ **Conversation History** - Never lose context
- ✅ **100% Free** - Serverless on Vercel, free-tier AI APIs
- ✅ **No Bloat** - Clean architecture, no unnecessary dependencies

### Tech Stack
- **Frontend**: React 19 + TypeScript + Vite
- **Backend**: Vercel Functions (Serverless)
- **Database**: Supabase (Free tier)
- **Deployment**: Vercel + Netlify
- **UI**: Lucide icons + custom CSS (no heavy frameworks)

### Getting Started

#### Local Development
```bash
npm install
npm run dev
```

#### Build
```bash
npm run build
```

#### Deploy to Vercel
```bash
npm i -g vercel
vercel
```

### Environment Variables
```env
VITE_API_URL=http://localhost:3001
VERCEL_ENV=development
CLAUDE_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

### Architecture

```
ajna/
├── src/                    # React frontend
│   ├── components/         # UI components
│   ├── App.tsx            # Main app
│   └── index.css          # Styling
├── api/                   # Vercel Functions
│   ├── chat.ts            # Chat endpoint
│   ├── synthesize.ts      # Synthesis logic
│   └── health.ts          # Health check
├── vercel.json            # Deployment config
└── package.json           # Dependencies
```

### API Endpoints

**POST /api/chat**
```json
{
  "message": "Your prompt",
  "model": "claude"
}
```

**POST /api/synthesize**
```json
{
  "prompt": "Human idea",
  "context": "Previous context",
  "model": "gpt4"
}
```

### Roadmap
- [ ] AI API integrations (Claude, OpenAI, Gemini)
- [ ] Supabase database for persistence
- [ ] User authentication
- [ ] Conversation export (JSON, Markdown, PDF)
- [ ] n8n workflow integration
- [ ] Mobile app
- [ ] Real-time collaborative sessions

### Contributing
We welcome contributions! See issues for planned features.

### License
MIT

### Built with ❤️ at TechVoid
