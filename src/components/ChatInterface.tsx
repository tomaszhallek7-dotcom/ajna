import { useState } from 'react'
import { MessageSquare, Send } from 'lucide-react'

interface Message {
  id: number
  role: 'user' | 'assistant'
  content: string
}

interface ChatInterfaceProps {
  messages: Message[]
  model: string
}

export default function ChatInterface({ messages, model }: ChatInterfaceProps) {
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSend = async () => {
    if (!input.trim()) return

    setLoading(true)
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input, model }),
      })
      const data = await response.json()
      console.log('Response:', data)
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setLoading(false)
      setInput('')
    }
  }

  return (
    <div className="chat-interface">
      <div className="messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.role}`}>
            {msg.role === 'assistant' && <MessageSquare size={16} />}
            <div className="content">{msg.content}</div>
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Napisz swoją wiadomość..."
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading}>
          <Send size={20} />
        </button>
      </div>
    </div>
  )
}