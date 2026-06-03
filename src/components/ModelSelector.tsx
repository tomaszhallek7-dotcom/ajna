import { Brain } from 'lucide-react'

const MODELS = [
  { id: 'claude', name: '🧠 Claude', provider: 'Anthropic' },
  { id: 'gpt4', name: '🤖 GPT-4', provider: 'OpenAI' },
  { id: 'gemini', name: '✨ Gemini', provider: 'Google' },
  { id: 'ollama', name: '🏠 Ollama (Local)', provider: 'Local' },
]

interface ModelSelectorProps {
  selected: string
  onSelect: (model: string) => void
}

export default function ModelSelector({ selected, onSelect }: ModelSelectorProps) {
  return (
    <div className="model-selector">
      <h3>
        <Brain size={20} /> Modele AI
      </h3>
      <div className="model-list">
        {MODELS.map((model) => (
          <button
            key={model.id}
            className={`model-button ${selected === model.id ? 'active' : ''}`}
            onClick={() => onSelect(model.id)}
          >
            <div className="model-name">{model.name}</div>
            <div className="model-provider">{model.provider}</div>
          </button>
        ))}
      </div>
    </div>
  )
}