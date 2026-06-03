#!/bin/bash
# Quick setup for video generation

echo "🎬 Installing AJNA video generator dependencies..."

pip install -r requirements-video.txt

echo "✅ Done!"
echo ""
echo "🎥 Generate video assets:"
echo "   python generate_video.py"
echo ""
echo "📂 Output: ./videos/"
