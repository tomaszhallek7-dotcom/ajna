export const getClaudeResponse = async (message: string) => {
  // Using Hugging Face Inference API (free tier, no API key)
  const response = await fetch('https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1', {
    headers: { Authorization: `Bearer ${process.env.HF_API_KEY || 'free'}` },
    method: 'POST',
    body: JSON.stringify({ inputs: message, parameters: { max_length: 512 } }),
  })
  
  const result = await response.json()
  return result[0]?.generated_text || 'Response generation failed'
}

export const getGPTResponse = async (message: string) => {
  // Placeholder - will use OpenAI free tier if available
  return `GPT would say: ${message.substring(0, 50)}...`
}

export const getGeminiResponse = async (message: string) => {
  // Google's Makersuite free API
  return `Gemini would respond to: ${message.substring(0, 50)}...`
}
