#!/usr/bin/env python3
"""
AJNA Video Generator - Auto-generates YouTube video with narration
Generates: screencast simulation + text-to-speech narration + subtitles
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple

try:
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    HAS_VISION = True
except ImportError:
    HAS_VISION = False
    print("⚠️  Install dependencies: pip install opencv-python pillow pyttsx3")

try:
    import pyttsx3
    HAS_TTS = True
except ImportError:
    HAS_TTS = False
    print("⚠️  pyttsx3 not installed")


class AJNAVideoScript:
    """Video script with timestamps and narration"""
    
    SCRIPT = [
        # (timestamp_start, timestamp_end, text, visual_hint)
        (0, 2, "Cześć! Jestem [Your name].", "SHOW_AJNA_LOGO"),
        (2, 5, "Dziś pokazuję Ci AJNA - platformę, która zmienia wszystko w pracy z AI.", "SHOW_GITHUB_REPO"),
        (5, 8, "Zamiast tradycyjnego chatu gdzie piszesz prompt i AI odpowiada raz...", "SHOW_CHATGPT"),
        (8, 11, "Tutaj my pracujemy razem. To jest syntezy. To jest przyszłość pracy z AI.", "SHOW_AJNA_INTERFACE"),
        (11, 15, "Tradycyjne AI tools mają problem: tylko jeden model, brak historii, nie ma współpracy.", "SHOW_PROBLEMS"),
        (15, 18, "Ale AJNA? Zmienia to wszystko.", "SHOW_SOLUTION"),
        (18, 22, "Pierwszy - widzisz tutaj? Mogę wybrać model: Claude, GPT-4, Gemini, lokalna Ollama.", "SHOW_MODEL_SELECTOR"),
        (22, 25, "Zmieniam w locie. Żaden reset. Ten sam kontekst.", "ANIMATE_MODEL_SWITCH"),
        (25, 30, "Teraz pytam coś: 'Pomóż mi stworzyć elevator pitch dla AJNA na YouTubie'", "SHOW_USER_INPUT"),
        (30, 35, "Claude odpowiada tutaj. Ale to nie koniec. Ja mogę edytować, poprawiać, prosić o więcej.", "SHOW_AI_RESPONSE"),
        (35, 40, "I mogę zmienić model - prosić GPT-4 o to samo - porównać odpowiedzi.", "ANIMATE_MODEL_SWITCH_2"),
        (40, 45, "Rezultat? Mogę wyeksportować do JSON, Markdown, Plain text.", "SHOW_EXPORT"),
        (45, 50, "I integruje się z n8n - co znaczy mogę zautomatyzować procesy.", "SHOW_AUTOMATION"),
        (50, 55, "Dlaczego AJNA? Syntezy - ty plus AI razem.", "SHOW_BENEFITS_1"),
        (55, 60, "Wielkie modele - jeden klik. Historia - uczysz się na każdej rozmowie.", "SHOW_BENEFITS_2"),
        (60, 65, "100% darmowe. Serverless. Dla każdego.", "SHOW_BENEFITS_3"),
        (65, 70, "AJNA jest dostępne teraz na ajna.vercel.app", "SHOW_LINK"),
        (70, 75, "GitHub: github.com/tomaszhallek7-dotcom/ajna", "SHOW_GITHUB"),
        (75, 80, "Spróbuj sam. Jest darmowe. Nie trzeba się rejestrować.", "SHOW_CALL_TO_ACTION"),
        (80, 85, "A jeśli się podoba - subskrybuj. Następny video: Building AJNA from Scratch.", "SHOW_SUBSCRIBE"),
        (85, 90, "Dziękuję! Co myślisz? Będziesz używać AJNA? Komentarz poniżej!", "SHOW_OUTRO"),
    ]

    def __init__(self, output_dir: str = "videos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.fps = 30
        self.width = 1920
        self.height = 1080
        self.total_duration = 90  # 90 seconds

    def generate_narration_audio(self) -> str:
        """Generate text-to-speech narration"""
        if not HAS_TTS:
            print("❌ pyttsx3 not available, skipping audio generation")
            return ""

        print("🎙️  Generating narration audio...")
        engine = pyttsx3.init()
        engine.setProperty('rate', 140)  # Polish-friendly speed
        engine.setProperty('volume', 0.95)

        # Combine all narration
        narration = " ".join([text for _, _, text, _ in self.SCRIPT])
        
        audio_file = self.output_dir / "narration.wav"
        engine.save_to_file(narration, str(audio_file))
        engine.runAndWait()
        
        print(f"✅ Audio saved: {audio_file}")
        return str(audio_file)

    def generate_subtitle_file(self) -> str:
        """Generate SRT subtitle file"""
        print("📝 Generating subtitles...")
        
        srt_content = ""
        for idx, (start, end, text, _) in enumerate(self.SCRIPT, 1):
            srt_content += f"{idx}\n"
            srt_content += f"{self._format_time(start)} --> {self._format_time(end)}\n"
            srt_content += f"{text}\n\n"

        srt_file = self.output_dir / "ajna_video_pl.srt"
        srt_file.write_text(srt_content, encoding="utf-8")
        
        print(f"✅ Subtitles saved: {srt_file}")
        return str(srt_file)

    @staticmethod
    def _format_time(seconds: int) -> str:
        """Convert seconds to SRT timestamp format"""
        mins, secs = divmod(seconds, 60)
        return f"00:{mins:02d}:{secs:02d},000"

    def generate_storyboard_md(self) -> str:
        """Generate markdown storyboard"""
        print("📋 Generating storyboard...")
        
        md_content = "# AJNA Video 1 - Storyboard\n\n"
        
        for idx, (start, end, text, visual_hint) in enumerate(self.SCRIPT, 1):
            duration = end - start
            md_content += f"## Scene {idx} ({start}s - {end}s, {duration}s)\n\n"
            md_content += f"**Narration:**\n{text}\n\n"
            md_content += f"**Visual:**\n{visual_hint}\n\n"
            md_content += "---\n\n"

        storyboard_file = self.output_dir / "STORYBOARD.md"
        storyboard_file.write_text(md_content, encoding="utf-8")
        
        print(f"✅ Storyboard saved: {storyboard_file}")
        return str(storyboard_file)

    def generate_production_guide(self) -> str:
        """Generate step-by-step production guide"""
        print("📖 Generating production guide...")
        
        guide = """# AJNA Video 1 - Production Guide

## ⏱️ Total Duration: 90 seconds

## 🎬 What You'll Need
- Screen recording software (OBS, ScreenFlow, or ffmpeg)
- Your voice/microphone
- AJNA deployed on ajna.vercel.app
- Video editor (DaVinci Resolve free, or CapCut)

## 📹 Recording Steps

### 1. Setup (5 min)
- [ ] Open OBS or ScreenFlow
- [ ] Set resolution: 1920x1080 (1080p)
- [ ] Set FPS: 60
- [ ] Create scene: "AJNA Demo"
- [ ] Add browser source: https://ajna.vercel.app
- [ ] Test microphone audio levels

### 2. Record Segments (by visual_hint)

**SHOW_AJNA_LOGO** (0-2s)
- Show static: AJNA logo with subtitle "AI-Human Synthesis"
- Music: Upbeat intro track (YouTube Audio Library)

**SHOW_GITHUB_REPO** (2-5s)
- Browser: Open GitHub (tomaszhallek7-dotcom/ajna)
- Pan/zoom on repo name
- Show star count ("0 stars soon to be 1000s!")

**SHOW_CHATGPT** (5-8s)
- Browser: Quick comparison shot of ChatGPT interface
- Highlight: Single model only
- Text overlay: "Traditional AI"

**SHOW_AJNA_INTERFACE** (8-11s)
- Browser: ajna.vercel.app home page
- Highlight: Multi-model selector
- Text overlay: "AJNA - AI-Human Synthesis"

**SHOW_PROBLEMS** (11-15s)
- Create slide with:
  ❌ Only one model
  ❌ No history
  ❌ No collaboration
  ❌ No automation
- Dramatic zoom on each bullet

**SHOW_SOLUTION** (15-18s)
- Green screen: You explaining (or just text)
- Text overlay: "AJNA Solution"

**SHOW_MODEL_SELECTOR** (18-22s)
- Browser: AJNA model selector
- Hover over each model
- Show: Claude, GPT-4, Gemini, Ollama

**ANIMATE_MODEL_SWITCH** (22-25s)
- Click model, show instant switch
- Zoom on selector
- Add transition effect

**SHOW_USER_INPUT** (25-30s)
- Type in chat: "Pomóż mi stworzyć elevator pitch dla AJNA na YouTubie"
- Slow typing (not too fast)

**SHOW_AI_RESPONSE** (30-35s)
- AI responds (you can fake/pre-write response)
- Scroll through response
- Highlight key parts

**ANIMATE_MODEL_SWITCH_2** (35-40s)
- Switch to different model
- Show different response
- Side-by-side comparison (if possible)

**SHOW_EXPORT** (40-45s)
- Click export button (when built)
- Show format options:
  - JSON
  - Markdown
  - Plain Text
- Download one

**SHOW_AUTOMATION** (45-50s)
- Show n8n logo
- Explain automation possibilities
- Text overlay: Examples

**SHOW_BENEFITS_1 to 3** (50-65s)
- Create engaging slides:
  ✅ Synthesis - You + AI
  ✅ Multiple Models - One Click
  ✅ History - Learn Each Time
  ✅ 100% Free
  ✅ Serverless
  ✅ For Everyone

**SHOW_LINK** (65-70s)
- Big text: ajna.vercel.app
- QR code (optional)
- Description: "Try it now"

**SHOW_GITHUB** (70-75s)
- GitHub link
- Text: "Open source (coming soon)"

**SHOW_CALL_TO_ACTION** (75-80s)
- You on camera: "Try it. It's free."
- Text overlay: "GitHub Link in Description"

**SHOW_SUBSCRIBE** (80-85s)
- YouTube subscribe button animation
- Text: "Next: Building AJNA from Scratch"

**SHOW_OUTRO** (85-90s)
- Montage: Quick cuts of features
- Background music fades
- End screen: Subscribe + Playlist

## 🎵 Music Suggestions (YouTube Audio Library)
- Intro (0-5s): Upbeat tech music (no lyrics)
- Narration (5-80s): Calm, professional background
- Outro (80-90s): Energetic tech outro

## 🎙️ Voice Recording
- Record narration separately (higher quality)
- Read from script at natural pace (140 wpm)
- Add pauses for visual transitions
- Record in quiet room
- Use microphone (not built-in laptop mic)

## ✂️ Editing Checklist
- [ ] Trim silence
- [ ] Sync narration with visuals
- [ ] Add subtitles (use SRT file: ajna_video_pl.srt)
- [ ] Add text overlays
- [ ] Color correction (if needed)
- [ ] Add transitions (fast paced, not overdone)
- [ ] Sound design (whoosh effects, ding sounds)
- [ ] Final export (H.264, 1080p, MP4)

## 📤 Upload to YouTube
1. Title: "AJNA - Syntezy Między Tobą a AI" (or similar)
2. Description:
   ```
   AJNA - AI-Human Synthesis Workspace
   
   🔗 Try AJNA: https://ajna.vercel.app
   🐙 GitHub: https://github.com/tomaszhallek7-dotcom/ajna
   
   Real-time collaboration between humans and AI.
   Switch between models, maintain history, and synthesize ideas together.
   
   100% free. Serverless. For everyone.
   
   Timestamps:
   0:00 - Intro
   2:00 - Why AJNA?
   5:00 - The Problem
   8:00 - The Solution
   15:00 - Demo
   65:00 - Links & CTA
   
   #AI #OpenAI #ChatGPT #Programming
   ```
3. Tags: AI, ChatGPT, GPT-4, Gemini, Ollama, Programming, Developer
4. Thumbnail: AJNA logo + "AI Synthesis" text
5. Playlist: Add to "AJNA" playlist (create new)
6. Premiere: Schedule for best engagement time

## 🎯 Success Metrics
- Views: Target 500+ in first week
- Engagement: Aim for 5%+ CTR on CTA
- Subscribers: Track channel growth
- GitHub: Monitor repo stars
- Website: Track ajna.vercel.app traffic

## 💡 Pro Tips
- Hook viewers in first 3 seconds
- Use pattern interrupts (cuts, zoom, sound)
- Speak directly to camera (builds connection)
- End with clear CTA (link, subscribe)
- Respond to comments in first 24h (algorithm boost)

Good luck! You've got this! 🚀
"""
        
        guide_file = self.output_dir / "PRODUCTION_GUIDE.md"
        guide_file.write_text(guide, encoding="utf-8")
        
        print(f"✅ Production guide saved: {guide_file}")
        return str(guide_file)

    def generate_all(self):
        """Generate all video assets"""
        print("\n" + "="*60)
        print("🎬 AJNA VIDEO GENERATOR")
        print("="*60 + "\n")

        files_generated = []

        # Generate subtitles
        srt = self.generate_subtitle_file()
        files_generated.append(srt)

        # Generate storyboard
        storyboard = self.generate_storyboard_md()
        files_generated.append(storyboard)

        # Generate production guide
        guide = self.generate_production_guide()
        files_generated.append(guide)

        # Generate audio (if available)
        if HAS_TTS:
            audio = self.generate_narration_audio()
            files_generated.append(audio)

        print("\n" + "="*60)
        print("✅ VIDEO GENERATION COMPLETE!")
        print("="*60)
        print(f"\n📂 Output directory: {self.output_dir}")
        print(f"\n📋 Generated files:")
        for f in files_generated:
            print(f"   - {f}")
        print(f"\n⏱️  Total video duration: {self.total_duration}s (1m 30s)")
        print(f"\n📝 Next steps:")
        print(f"   1. Read: {self.output_dir}/PRODUCTION_GUIDE.md")
        print(f"   2. Record video using storyboard")
        print(f"   3. Edit in your favorite video editor")
        print(f"   4. Add subtitles from: {self.output_dir}/ajna_video_pl.srt")
        print(f"   5. Upload to YouTube @TechVoid-h8p")
        print(f"\n🎙️  Optional: Use narration audio if available\n")


if __name__ == "__main__":
    generator = AJNAVideoScript()
    generator.generate_all()
