import type { VercelRequest, VercelResponse } from '@vercel/node'

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method === 'POST') {
    const { message, model } = req.body

    // TODO: Integrate with actual AI APIs
    const mockResponses: Record<string, string> = {
      claude: 'Ą Claude tutaj. Może pomogę w...',
      gpt4: '🤖 GPT-4 tutaj. Z przyjemność pomogę...',
      gemini: '??? Gemini tutaj. Jak się masz?',
      ollama: '?🏠 Ollama local. Czym się słęża?',
    }

    res.status(200).json({
      message: mockResponses[model] || 'Unknown model',
      model,
      timestamp: new Date().toISOString(),
    })
  } else {
    res.status(405).json({ error: 'Method not allowed' })
  }
}