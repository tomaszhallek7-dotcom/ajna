# 🚀 AJNA Setup Guide - 100% Free

## Setup w 10 minut

### Krok 1: Vercel Account (2 min)
1. Go: https://vercel.com/signup
2. Click: "Continue with GitHub"
3. Authorize Vercel
4. ✅ Done!

### Krok 2: Deploy AJNA (3 min)
1. https://vercel.com/import
2. Select: `tomaszhallek7-dotcom/ajna`
3. Click: "Import"
4. Framework: `Vite`
5. **Deploy** → Waits 1-2 min
6. ✅ Live at: `https://ajna.vercel.app`

### Krok 3: Supabase Database (2 min)
1. Go: https://supabase.com/dashboard
2. Click: "New Project"
3. Name: `ajna-db`
4. Region: EU (closest to Poland)
5. Create → Waits 1 min
6. ✅ Database ready!

### Krok 4: Custom Domain (2 min)
1. Free domain: https://www.freenom.com/
2. Search: `ajna.tk` (free!)
3. Register → Gets domain
4. Go to Vercel: Settings > Domains
5. Add: `ajna.tk`
6. Point DNS (Vercel gives instructions)
7. ✅ Live at: `https://ajna.tk` (in 24h)

---

## Environment Variables (for Vercel)

In Vercel Settings > Environment Variables, add:

```
VITE_API_URL=https://ajna.vercel.app
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

(Get Supabase URL/Key from Project Settings > API)

---

## AI APIs (Free Tiers)

### Option A: Use Free Hugging Face (No API key needed)
✅ Already integrated in code
✅ No signup needed
✅ Limited: ~30 requests/min

### Option B: Add Paid APIs Later
- Claude: https://console.anthropic.com (free $5 credit)
- OpenAI: https://platform.openai.com ($5 free credit)
- Google Gemini: https://makersuite.google.com/app/apikey (free tier)

---

## GitHub Actions Auto-Deploy

When you push to `main` branch:
1. GitHub Action runs automatically
2. Tests + builds
3. Deploys to Vercel
4. ✅ Live in ~2 minutes

No manual deploy needed! 🚀

---

## Quick Test

```bash
# Local development
npm install
npm run dev
# Go to http://localhost:5173

# Build for production
npm run build
npm run preview
```

---

## Next Steps

1. ✅ Deploy AJNA (follow steps above)
2. 📹 Film Video 1 on @TechVoid-h8p
3. 🚀 Publish to YouTube
4. 📢 Share on Reddit + Twitter
5. 💬 Build community

---

## Support

If anything breaks:
1. Check Vercel build logs: https://vercel.com/dashboard
2. Check GitHub Actions: Your repo > Actions tab
3. Check console errors: Open DevTools (F12) in browser

**You've got this!** 💜
