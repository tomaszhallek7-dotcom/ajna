# 🎬 VIDEO 1 PRODUCTION GUIDE - AJNA
## YouTube: @TechVoid-h8p

**Total Duration:** 90 seconds (1:30)
**Format:** Screen recording + Narration
**Language:** Polish
**Target:** Tech audience + AI enthusiasts

---

## 📋 QUICK CHECKLIST

### Before Recording
- [ ] Vercel deployed (ajna.vercel.app working)
- [ ] OBS/ScreenFlow installed + configured (1920x1080, 60fps)
- [ ] Microphone tested (quiet room)
- [ ] Narration script memorized (from storyboard)
- [ ] Background music downloaded (YouTube Audio Library)

### During Recording
- [ ] Screen recording at 1080p 60fps
- [ ] Clear audio capture
- [ ] Smooth mouse movements
- [ ] Follow storyboard timing exactly
- [ ] Don't skip scenes

### After Recording
- [ ] Download SRT subtitles (videos/ajna_pl.srt)
- [ ] Edit in video editor
- [ ] Add subtitles
- [ ] Add text overlays
- [ ] Add transitions
- [ ] Color correction
- [ ] Export as H.264 MP4 (1080p)

---

## 🎥 RECORDING SETUP

### Software Options
1. **OBS Studio** (FREE, all platforms) ← RECOMMENDED
   - Download: https://obsproject.com/
   - Setup: New Scene → Browser Source → Add "https://ajna.vercel.app"

2. **ScreenFlow** (macOS, ~$130)
   - Good for Mac users
   - Built-in editing

3. **Camtasia** (Windows/Mac, ~$200/year)
   - Professional tools
   - Easy editing

4. **OBS + ffmpeg** (FREE, advanced)
   - Record with OBS
   - Process with ffmpeg

### OBS Configuration
```
Scene: "AJNA Demo"
Sources:
  - Browser: https://ajna.vercel.app (1920x1080)
  - Microphone audio
  
Output Settings:
  - Video Bitrate: 6000-8000 kbps
  - Audio Bitrate: 128 kbps
  - Encoder: H.264
  - Format: MP4
```

---

## 🎙️ VOICE RECORDING (3 OPTIONS)

### Option 1: Record Live with Screen (Easiest)
- Pro: Perfect sync with visuals
- Con: Needs practiced delivery
- Do: Practice 2-3 times before recording

### Option 2: Record Voice Separately (Better Quality)
- Pro: Better audio quality
- Con: Need to sync manually
- Process:
  1. Record voice in Audacity/GarageBand
  2. Record screen muted
  3. Sync in video editor
  4. Adjust timing as needed

### Option 3: Use Text-to-Speech (AI)
- Pro: Perfect timing
- Con: Less personal
- Tool: Use generated narration from generate_video.py
- Process:
  1. Run: `python generate_video.py` (generates narration.wav)
  2. Import audio into video editor
  3. Align with screen recording

**RECOMMENDATION:** Option 2 (separate voice recording for best quality)

---

## 📹 STEP-BY-STEP RECORDING

### 1. Record Narration (10 min)
```bash
# If using Audacity or GarageBand:
- Open app
- Set quality: 44.1kHz, Stereo, 16-bit
- Read script slowly and clearly
- Add 0.5s pauses after key points
- Export as WAV (uncompressed)
- Name: narration.wav
```

### 2. Setup OBS (5 min)
```bash
# OBS Studio
1. Launch OBS
2. Create New Scene: "AJNA Video 1"
3. Add Source: Browser
   - URL: https://ajna.vercel.app
   - Resolution: 1920x1080
4. Add Audio: Microphone (if recording live)
5. Configure Output:
   - File: ~/Desktop/ajna-video-raw.mp4
   - Encoder: H.264
   - Bitrate: 6000 kbps
6. Test: Click "Preview Stream" → Check audio/video
```

### 3. Record Screen (15 min)
```
- Make sure narration script is visible (phone/tablet)
- Follow storyboard exactly
- Click "Start Recording"
- Perform scenes:
  - Navigate to GitHub (scene 2)
  - Show ChatGPT interface (scene 3) [pre-tab]
  - Show ajna.vercel.app (scenes 4-18)
  - Model switching animations
  - Type in chat
  - Click export (fake if not implemented)
  - Show links
- Click "Stop Recording"
- Check file: ~/Desktop/ajna-video-raw.mp4
```

### 4. Prepare for Editing
```
Files needed:
✓ ajna-video-raw.mp4 (screen recording)
✓ narration.wav (voice)
✓ ajna_pl.srt (subtitles)
✓ Background music (downloaded from YouTube Audio Library)
✓ Music outro track
```

---

## ✂️ VIDEO EDITING

### Recommended Editors
1. **DaVinci Resolve** (FREE) ← BEST FOR FREE
   - Professional quality
   - Free version is full-featured
   - Learn: https://www.youtube.com/results?search_query=davinci+resolve+tutorial

2. **CapCut** (FREE)
   - Easy to use
   - Good for beginners
   - Limited advanced features

3. ** Adobe Premiere Pro** ($55/month)
   - Professional standard
   - Lots of presets
   - Expensive

### EDITING WORKFLOW (DaVinci Resolve)

**Step 1: Import Files**
```
File → New Project
Name: ajna-video-1
Timeline Resolution: 1920x1080
Frame Rate: 60fps
```

**Step 2: Add Video Track**
```
Drag: ajna-video-raw.mp4 → Timeline
Trim: Cut silence at start/end
```

**Step 3: Add Audio**
```
Drag: narration.wav → Audio Track 1
Sync with video (adjust timing)
Adjust levels: -6dB for narration
```

**Step 4: Add Background Music**
```
Drag: background_music.mp3 → Audio Track 2
Set level: -15dB (behind narration)
Fade in/out at beginning/end
```

**Step 5: Add Subtitles**
```
Timeline → Subtitles → Import
File: ajna_pl.srt
Font: Roboto, 48pt, White, Shadow
Position: Bottom center
Sync: Check against narration
```

**Step 6: Add Text Overlays**
- Scene 2-3: "GitHub Repo" 
- Scene 4: "AJNA: Multi-Model AI"
- Scene 7: "Model Selector"
- Scene 17: "ajna.vercel.app" (large, centered)
- Scene 18: "GitHub Link" (large)
- Scene 19: "Try It Now • No Registration"
- Scene 20: "Subscribe for More!"
- Scene 21: "Thank You! Comment Below 👇"

**Step 7: Add Transitions**
```
Transition Type: Dissolve or Fade
Duration: 0.3 seconds
Apply to: Key scene changes (model switches, export, links)
```

**Step 8: Add Sound Effects**
```
Wheal Whoosh on model switches
Ding on links
Keyboard typing sounds

Sources:
- Freesound.org
- YouTube Audio Library
- Zapsplat.com
```

**Step 9: Color Correction** (Optional)
```
Fusion Tab → Color Grade
LUTs: "Cinematic" or "Tech Vibes"
Brightness: +5%
Saturation: +10%
Contrast: +5%
```

**Step 10: Export**
```
File → Export → Add to Render Queue
Format: MP4
Codec: H.264 (High Quality)
Bitrate: 8000 kbps
Resolution: 1920x1080
Frame Rate: 60fps
Audio: 128kbps AAC Stereo

Output: ~/Desktop/AJNA_Video_1_Final.mp4

Wait: 5-10 minutes for encoding
```

---

## 🎬 FINAL VIDEO CHECKS

- [ ] Audio synced perfectly
- [ ] Subtitles readable (no typos)
- [ ] Text overlays visible (contrast OK)
- [ ] Transitions smooth
- [ ] Music levels balanced
- [ ] Total duration: ~90s (±2s)
- [ ] No random cuts/glitches
- [ ] File size: <500MB
- [ ] Video plays in VLC (compatibility check)

---

## 📺 YOUTUBE UPLOAD

### Metadata

**Title:** (Choose one)
- "AJNA - Syntezy Między Tobą a AI" (Best)
- "AI-Human Synthesis: Meet AJNA"
- "Co Jeśli AI i Człowiek Pracowali Razem?"

**Description:**
```
AJNA - AI-Human Synthesis Workspace

🚀 Try AJNA: https://ajna.vercel.app
💻 GitHub: https://github.com/tomaszhallek7-dotcom/ajna

Real-time collaboration between humans and artificial intelligence.
Switch between models (Claude, GPT-4, Gemini, Ollama), maintain conversation context, and synthesize ideas together.

100% free. Serverless. For everyone.

Timestamps:
0:00 - Intro
2:00 - The Hook
5:00 - Problems with Traditional AI
8:00 - Meet AJNA
15:00 - Why AJNA?
18:00 - Multi-Model Demo
45:00 - Automation (n8n)
60:00 - Key Benefits
75:00 - How to Get Started
80:00 - Call to Action

#AI #ChatGPT #OpenAI #GPT4 #Gemini #Ollama #Coding #Developer #Automation
```

**Tags:** (10-15)
- AI
- ChatGPT
- GPT-4
- Gemini
- Ollama
- Coding
- Programming
- Automation
- Developer Tools
- AI Synthesis
- Machine Learning
- No Code

**Thumbnail:**
- AJNA logo (center)
- Text: "AI Synthesis" or "Multiple AI Models"
- Your face (top corner, surprised/excited expression)
- Bright colors (purple + cyan, matching AJNA branding)
- Text contrast: White on dark background
- Dimensions: 1280x720px

### Upload Process

1. **Go to:** https://www.youtube.com/studio
2. **Click:** "Create" → "Upload Video"
3. **Select:** AJNA_Video_1_Final.mp4
4. **Add Details:**
   - Title
   - Description
   - Thumbnail
   - Visibility: Public (not unlisted)
5. **Advanced Settings:**
   - Video Language: Polish
   - Caption Certification: Checked (for subtitles)
   - Recording Date: Today
6. **Monetization:** Not enabled (new channel requirement)
7. **Click:** "Publish" or "Schedule" (best time: Wed/Thu 7-9 PM)

### Post-Upload

- [ ] Add subtitles: YouTube → Captions → Upload file (ajna_pl.srt)
- [ ] Create Playlist: "AJNA" + add video
- [ ] Pin comment: Link to GitHub + discord/community (when available)
- [ ] Share: Reddit, Twitter, Dev.to, IndieHackers
- [ ] Respond to comments within 24h (algorithm boost)

---

## 🚀 LAUNCH CHECKLIST

### Before Video Goes Live
- [ ] Vercel deployment live and tested
- [ ] GitHub repo accessible
- [ ] All links work
- [ ] Description has timestamps
- [ ] Subtitles imported and reviewed
- [ ] Thumbnail created
- [ ] Playlist created

### At Launch Time
- [ ] Publish video
- [ ] Immediately post on Reddit:
  - r/OpenAI
  - r/ChatGPT
  - r/learnprogramming
  - r/webdev (if web-focused)
- [ ] Tweet on Twitter (with video link)
- [ ] Post on Dev.to (technical post)
- [ ] Share on IndieHackers
- [ ] Join relevant Discord communities

### After Launch (24-48h)
- [ ] Check analytics
- [ ] Respond to all comments
- [ ] Monitor GitHub stars
- [ ] Track website traffic
- [ ] Collect feedback

---

## 📊 SUCCESS METRICS

**Target for First Week:**
- Views: 300-500
- Engagement Rate: 5%+ (likes + comments)
- Click-through Rate: 10%+ to website
- GitHub Stars: 10-20
- Subscribers: 5-10 new followers

**Interpretation:**
- If you hit these: Content resonates, plan Video 2
- If below: Analyze comments, iterate for Video 2
- If above: Accelerate content production

---

## 💡 PRO TIPS

1. **Hook in first 3 seconds** - Viewers decide immediately
2. **Pattern interrupts** - Change scene every 3-5 seconds
3. **Clear audio** - Most people leave if audio is bad
4. **Fast pacing** - Don't let it drag
5. **CTAs are key** - Tell viewers exactly what to do
6. **Respond to comments** - Builds community + algorithm boost
7. **Thumbnail matters** - Test A/B versions
8. **Consistency** - Upload regularly (weekly if possible)
9. **Thumbnails with faces** - Get 20-30% more CTR
10. **Call to action early** - Don't wait until end

---

## ❓ TROUBLESHOOTING

**Problem:** Audio is out of sync
**Solution:** Manually adjust video/audio offset in editor (±100ms)

**Problem:** Video is too long
**Solution:** Speed up less important sections (1.1x)

**Problem:** Subtitles don't match narration
**Solution:** Re-download SRT and re-import

**Problem:** Video looks compressed/pixelated
**Solution:** Export bitrate higher (10000+ kbps) or reduce resolution

**Problem:** YouTube rejected subtitle file
**Solution:** Use YouTube's auto-generate feature (less accurate but works)

---

**YOU'VE GOT THIS! 🚀 Make the video, publish it, and let's grow AJNA together!**
