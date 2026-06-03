import type { VercelRequest, VercelResponse } from '@vercel/node'

export default async function handler(_req: VercelRequest, res: VercelResponse) {
  res.status(200).json({
    status: 'ok',
    message: 'AJNA API v1 running',
    endpoints: ['/api/chat', '/api/synthesize', '/api/health'],
  })
}