# Kylene Render Pipeline

Script text → ElevenLabs narration (frozen voice settings) → HeyGen avatar render →
download → automatic frame analysis. Every run writes a `receipt.json`.

## Status

**Code ready; environment not yet enabled.** Verified 2026-07-03: the cloud
environment's network policy blocks `api.elevenlabs.io` and `api.heygen.com`
(403 at the egress proxy). To enable, the environment owner must do two things
in the Claude Code environment settings on claude.ai:

1. **Secrets** — add environment variables (values never go in chat or this repo):
   - `ELEVENLABS_API_KEY` — from ElevenLabs → Developers → API Keys
   - `HEYGEN_API_KEY` — from HeyGen → Settings → Developers → API Keys
   - `KYLENE_VOICE_ID` — the locked voice's ID (ElevenLabs → My Voices → view ID)
   - `KYLENE_AVATAR_ID` — the locked avatar's ID (HeyGen avatar page / API list-avatars)
   - Optional overrides: `KYLENE_STABILITY` (0.6), `KYLENE_SIMILARITY` (0.75),
     `KYLENE_STYLE` (0.0), `KYLENE_SPEED` (0.95)
2. **Network allowlist** — permit these hosts:
   - `api.elevenlabs.io`
   - `api.heygen.com`
   - `upload.heygen.com`
   - `*.heygen.ai` (render download URLs are served from heygen.ai resource hosts)

## Usage

```bash
# render a script (writes narration.mp3, render.mp4, receipt.json)
python3 pipeline/render_pipeline.py --script scripts/test3.txt --out renders/test3

# frame analysis (full frame + whole-clip mouth sheet + 12fps burst)
python3 pipeline/analyze_render.py renders/test3/render.mp4
```

## Rules

- **Spend control:** HeyGen renders cost credits. Sessions confirm with the owner
  before render-spending runs unless a standing budget has been agreed.
- **Frozen persona settings:** voice settings live in env vars and default to the
  locked values; changing them is a persona decision → update `brand/KYLENE.md` first.
- Endpoint shapes were written against HeyGen v2 / ElevenLabs v1 docs; the scripts
  print raw API error bodies, so any API drift is diagnosable from the run output.
  Expect to verify on the first live run.
- Known render constraint (see PRODUCTION.md rules 20–24): no long on-camera
  silences — the engine parks the mouth in a held-tongue idle during pauses.
  Write flowing sentences; cover deliberate pauses with title cards in the edit.
