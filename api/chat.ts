import type { VercelRequest, VercelResponse } from '@vercel/node'
import { getClaudeResponse } from './llm-integrations'

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  const { message, model } = req.body

  if (!message) {
    return res.status(400).json({ error: 'Message required' })
  }

  try {
    let response

    switch (model) {
      case 'claude':
        response = await getClaudeResponse(message)
        break
      case 'gpt4':
        response = `GPT-4 response to: ${message.substring(0, 100)}...`
        break
      case 'gemini':
        response = `Gemini response to: ${message.substring(0, 100)}...`
        break
      case 'ollama':
        response = `Ollama local response to: ${message.substring(0, 100)}...`
        break
      default:
        response = `Unknown model: ${model}`
    }

    return res.status(200).json({
      message: response,
      model,
      timestamp: new Date().toISOString(),
    })
  } catch (error) {
    console.error('Chat error:', error)
    return res.status(500).json({ error: 'Internal server error' })
  }
}