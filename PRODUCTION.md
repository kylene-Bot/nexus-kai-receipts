# Nexus Kai — Production Rules

**Why this file exists:** reference videos and format ideas used to be shared in Telegram and
never made it into the work. This file is the durable home for that material. Any session
(human or AI) producing channel content **reads this file first**, and every new reference
gets logged in the table at the bottom — so "was it implemented?" is checkable, not vibes.

---

## Reference channels

### Julian Goldie SEO — ~400K subs
- Runs an **AI clone pipeline**: Claude writes scripts → HeyGen renders his avatar (trained
  from a ~30s clip of his real face) → ElevenLabs clones his voice (from a ~5-min clean
  sample, deliberately keeping slight imperfections) → CapCut for edit + B-roll.
- The avatar output **outperforms his human-filmed videos**. Live Q&As and member calls stay
  real; the volume content is the clone.
- Volume play: reportedly 3–4+ uploads/day (up to 8–12/day across the operation), n8n as the
  automation layer, ~$1–2 marginal cost per video, ~$400/mo tool stack.
- States **5–15 minutes** as the monetization sweet spot.
- **Steal:** the pipeline (Claude → HeyGen → ElevenLabs → edit), the "real face only where
  connection matters" split, the fast feedback loop on hooks/thumbnails.
- **Don't copy:** the spam-volume strategy. Nexus Kai's brand is *receipts and honesty* —
  10 low-trust videos/day would destroy the one asset the channel has.

### Julia McCoy / First Movers — ~250K subs, ~2M monthly views in 18 months
- "World's first 100% AI clone, humanly-run channel." Built the clone (HeyGen + ElevenLabs)
  after a health crash; spent **25+ hours refining** the avatar/voice source material.
- **Scripts written with Claude, trained on her own top-performing videos** so it learns her
  voice, pacing, and hooks. Scripts written in simple paragraphs with line breaks as pauses.
- Performance: the clone gets **3.8× the views** of her real-face videos, **7.8% CTR**,
  **8-minute average watch time**.
- Clone does the educational/news content; the real person does personal-connection content.
- **Steal:** the script-training loop (feed our best-retaining scripts back into the prompt),
  the quality bar on avatar source data, the transparency — she openly brands the clone
  ("Dr. McCoy"), which converts "is this AI?" suspicion into brand identity.

### The wider field (highest-subscriber comparables)
- **Matt Wolfe (~800K):** 2–3 videos/week, every video tied to his FutureTools database —
  a durable asset behind the channel. *Our receipts repo is exactly this kind of asset; the
  videos should point at it every time.*
- **Two Minute Papers (~1.6M):** short, enthusiastic, one-paper-per-video, signature catchphrase.
  Proof that a narrow honest format scales.
- **AI Explained:** low frequency, independently runs its own benchmark — trusted *because*
  it tests claims itself. Closest existing brand to what Nexus Kai claims to be.
- **3Blue1Brown:** visual explanation as the product. Graphics aren't decoration; they ARE
  the content.
- **Nate Herk (~600K in <2 years):** proof a new channel can still grow fast in this niche.

---

## Positioning

**Promise: "We test it so you don't pay to find out."**

The niche stays AI (top-of-market RPM, $15–40 CPM, professional audience). The angle shifts
from model horse-races to **purchase-intent testing**: the channel runs the tools, systems,
and claims that people are about to spend money on, and publishes the receipts. Trend
coverage stays (Goldie's real strength) but always as *the tester, not the seller* — when a
model or tool drops, the video is "here's what it actually did on real tasks, same day,"
never "here's my course about it."

**Editorial rules (the moat — never break these):**
- We never sell the thing we're testing.
- Affiliate links only for tools that **passed our tests**, always disclosed. Failed tools
  get named, not buried.
- Sponsors never see results early and can't buy verdicts. This policy is public.
- Every number said on camera recomputes from this repo.

**Money ladder, in order:** AdSense (high-RPM niche does the work) → affiliate on passing
tools → sponsorships under the published policy → the long-term asset: this receipts
database as a public, machine-verified record of what was tested (the FutureTools model).

---

## Launch slate (EXP-0003 →)

Each premise names the receipt up front — if we can't save a receipt for it, we don't make it.

1. **"I paid for the $99/mo AI SEO tool so you don't have to."** 30-day run on a real site.
   *Receipts:* daily ranking/traffic logs, every generated output, the invoice.
   *Why it earns:* pure purchase intent; affiliate slot if it passes, better video if it fails.
2. **"I built the '$7K/month faceless AI channel' the gurus sell."** Follow the sold blueprint
   exactly (our own Claude → HeyGen → ElevenLabs pipeline — disclosed).
   *Receipts:* cost per video, analytics, actual revenue.
   *Why it earns:* tests the biggest claim in the niche; dogfoods our avatar stack on camera.
3. **"New model drops → same-day receipts."** Recurring franchise: a fixed task battery run
   within 24h of any major release (the EXP battery, made harder — tasks with real stakes).
   *Receipts:* run log + outputs in this repo, per release.
   *Why it earns:* owns the trend-coverage slot with a format nobody can fake.
4. **"AI cold-outreach tools: do any actually book meetings?"** Same campaign, N tools,
   identical lists. *Receipts:* send logs, reply rates, meetings booked.
   *Why it earns:* B2B purchase intent — the highest-value advertiser audience in the niche.
5. **"Can you tell this video is AI?"** The disclosed clone-launch video: how the avatar was
   built, then the honest reveal + retention data from this channel as the experiment.
   *Receipts:* our own analytics, the avatar source-data process.
   *Why it earns:* converts the clone from suspicion into brand (the Dr. McCoy move) and is
   the natural channel-relaunch video.
6. **"I gave three AIs the same $500 freelance job."** Real brief, real client accept/reject —
   EXP-0002 rebuilt with stakes and a mechanical gate (did the work get accepted?).
   *Receipts:* briefs, outputs, client verdicts in the repo.
   *Why it earns:* the model comparison people actually have money riding on.

---

## Production rules (checkable, per video)

**Hook (0:00–0:30)**
1. Cold-open on the payoff or the claim. No logo, no "hey guys, welcome back," no channel intro.
2. One open loop in the first 15s ("only some of these fixes survive — here's which").
3. The first spoken sentence delivers the exact promise of the title + thumbnail.
4. Benchmark: ≥60% of viewers still watching at 0:30. Below that, the hook failed — iterate.

**Structure & retention**
5. 5–15 minutes. One claim per video; cut anything that doesn't serve it.
6. Pattern break (visual reset, new receipt on screen, scene change) at least every 30–45s.
7. Progress markers — the viewer always knows where they are ("fix 2 of 3").
8. Every claim shown as a **receipt on screen** (the actual output file), never just narrated.
9. End on payoff + one pointer to the repo ("every number recomputes from _results.json").

**Script**
10. Draft with Claude, with our top-retaining past scripts pasted into the prompt as voice/pacing
    training (the McCoy loop). Log which scripts were used.
11. Short paragraphs, line breaks as pauses (reads better through ElevenLabs).
12. Numbers spoken must match the repo exactly — CI-verifiable (see reboot spec, frame 5).

**Avatar**
13. HeyGen avatar + ElevenLabs voice; invest real hours in source-data quality (McCoy: 25h).
    Keep natural voice imperfections — don't over-smooth.
14. Avatar handles data/news videos; real face for anything personal or trust-critical.
15. **Disclose the clone on-screen and in-description.** It's on-brand (honesty is the
    differentiator) and hedges platform risk: multiple creator-tools blogs report a 2026
    YouTube "Creator Authenticity Framework" that deprioritizes undisclosed primarily-AI
    content in recommendations. (Reported, not confirmed from YouTube directly — verify
    before betting the strategy on it, but disclosure is correct either way.)

**Cadence & feedback**
16. Consistent 2–3/week (the Matt Wolfe model), not sporadic bursts, not spam volume.
17. Track per video: CTR, 30s retention, avg watch time. Targets to beat: 7.8% CTR /
    8-min watch time (McCoy's clone numbers).
18. Thumbnail/title: one specific promise, story or transformation — never a generic tip.

**Graphics** (see the reboot-pitch prototype for the visual system)
19. Dark ink ground, receipts as paper artifacts, one amber highlight per frame,
    model colors fixed (Claude orange / GPT green / Gemini blue), every run visible, n stated.

---

## Reference log

| Date | Reference | What to steal | Status |
|---|---|---|---|
| 2026-07-02 | [Julian Goldie SEO](https://www.youtube.com/@JulianGoldieSEO) | Clone pipeline; real-face split; hook feedback loop | Distilled into rules 1–4, 13–14, 16 |
| 2026-07-02 | [Julia McCoy](https://www.youtube.com/channel/UCqzK60-oUOEq36uU9B1MMUg) | Script-training loop; avatar quality bar; disclosed clone | Distilled into rules 10–15, 17 |
| 2026-07-02 | Matt Wolfe / AI Explained / Two Minute Papers / 3Blue1Brown | Asset-backed channel; self-run benchmarks; visuals-as-content | Distilled into rules 5–9, 16, 19 |

Sources: [Goldie clone workflow (Market Movers pod)](https://www.marketmoverspod.com/e/julian-goldie-reveals-his-ai-clone-workflow-how-ai-seo-agencies-scale-to-100m-viewsyear/) ·
[Goldie profile/setup](https://aisuccesslabjuliangoldie.com/blog/julian-goldie-ai/) ·
[McCoy clone story (First Movers)](https://firstmovers.ai/julia-mccoy-ai-clone/) ·
[McCoy × HeyGen customer story](https://www.heygen.com/customer-stories/first-movers) ·
[McCoy method breakdown](https://razbakov.com/blog/2026-04-09-julia-mccoy-method) ·
[2026 hook/retention guides](https://miraflow.ai/blog/youtube-video-hooks-2026-save-first-30-seconds) ·
[Top AI channels 2026](https://ryandoser.com/ai-youtube-channels/)
