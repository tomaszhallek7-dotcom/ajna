import { useState } from 'react'
import ChatInterface from './components/ChatInterface'
import ModelSelector from './components/ModelSelector'
import './App.css'

function App() {
  const [selectedModel, setSelectedModel] = useState('claude')
  const [messages, setMessages] = useState([
    { id: 1, role: 'assistant', content: 'Cześć! Jestem AJNA. Wybierz model AI i zacznij rozmowę.' }
  ])

  return (
    <div className="app-container">
      <header className="ajna-header">
        <h1>AJNA</h1>
        <p>AI-Human Synthesis Workspace</p>
      </header>
      
      <div className="workspace">
        <aside className="sidebar">
          <ModelSelector selected={selectedModel} onSelect={setSelectedModel} />
        </aside>
        
        <main className="chat-area">
          <ChatInterface messages={messages} model={selectedModel} />
        </main>
      </div>
    </div>
  )
}

export default App