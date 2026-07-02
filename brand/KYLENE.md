# Kylene — Persona Spec

The host is a disclosed AI presenter. Face and voice are both **custom-generated, never
stock/library picks** — stock assets appear in other people's content and eventually
collide with the trust brand. This file is the canonical spec; once face and voice are
locked, they don't change without a documented decision here.

---

## Face — HeyGen generative avatar prompt

**Primary prompt:**

> Photorealistic professional woman in her early 30s, warm and sharp, direct eye contact
> with the camera, slight knowing smile. Shoulder-length copper-auburn hair, light
> freckles, hazel eyes. Wearing a dark charcoal blazer over a simple cream top, no logos,
> minimal jewelry. Framed chest-up like a news presenter. Deep ink-blue studio background,
> softly out of focus, with a warm amber rim light from the left. Soft key lighting,
> shallow depth of field, shot on a cinema camera, 4k, natural skin texture.

**Why these choices:**
- **Copper-auburn hair + amber rim light** ties her to the channel's amber highlight color —
  she matches the graphics system without wearing a costume.
- **Deep ink-blue background** = the graphics' dark ink ground; avatar footage and chart
  frames will feel like one set.
- **Freckles + natural skin texture** fight the over-smoothed "AI person" look, the #1 tell.
- **No logos, minimal jewelry** keeps every frame reusable and thumbnail-safe.

**Elevated variant (more striking, still advertiser-safe — the preferred starting point):**

> Photorealistic strikingly beautiful woman in her early 30s, magnetic and confident,
> direct eye contact with the camera, slight knowing smile. Long copper-auburn hair with
> soft waves, light freckles, striking hazel eyes, defined cheekbones. Wearing a fitted
> dark charcoal blazer over a simple silk top, no logos, delicate gold necklace. Framed
> chest-up like a news presenter. Deep ink-blue studio background, softly out of focus,
> warm amber rim light from the left. Soft glamour key lighting, shallow depth of field,
> shot on a cinema camera, 4k, natural skin texture.

**Boundary rule:** attractive yes, risqué no. The channel monetizes trust with a
professional, purchase-intent audience; styling that reads flirty/suggestive gets the
channel clustered with "AI girlfriend" content — wrong audience in, right audience out.
Authoritative + magnetic is the target (the McCoy lesson).

**Variation prompts (generate all three, compare):**
1. Same prompt, but: *straight dark-brown hair with a single copper streak, olive skin tone.*
2. Same prompt, but: *late 30s, glasses with thin amber frames, hair pulled back.*
3. Same prompt, but: *short dark curly hair, deeper warm brown skin tone, gold stud earrings.*

**Avoid (add as negative/steer notes if the flow allows):** influencer-glam styling,
heavy makeup, teeth-forward grin, generic "corporate stock photo" prettiness, busy
backgrounds, visible brand logos, uncanny over-smoothing.

**Selection checklist — the face must:**
- [ ] Read clearly at thumbnail size (test the candidate at ~10% scale).
- [ ] Be distinctive enough to recognize in a feed, not a generic stock face.
- [ ] Survive 3 consecutive generations looking like the same person (consistency test).
- [ ] Look natural mid-sentence, not just in the hero still (render a 20s test clip).
- [ ] Sit comfortably next to the graphics system (dark ink + amber) in one frame.

Once chosen: lock it, save the avatar, and use HeyGen's outfit/look variations rather than
regenerating — the face never changes.

---

## Voice — ElevenLabs Voice Design (custom, not library)

Library voices are shared with every other subscriber — same collision risk as a stock
face. Use the library voice you liked as a **reference only**; design a custom voice near
it with Voice Design.

**Design prompt starting point:**

> Female voice, early 30s, neutral American accent. Warm but matter-of-fact — a
> journalist reading you the numbers, not a hype presenter. Medium-low pitch, unhurried
> pace with deliberate short pauses. Slight dry humor in the delivery. Crisp consonants,
> natural breaths, very slightly imperfect — not radio-polished.

**Rules:**
- Keep natural imperfections; over-smoothed = the tell (same rule as the face).
- Test with a real script passage (use the VID-0001 cold open), not "the quick brown fox."
- Once picked: save to voice library, record the voice name/ID in your account notes, and
  **freeze the settings** (stability/similarity). Consistency across videos beats
  perfection on day one.
- The voice never does read-ads or sponsor scripts in a tone that mimics editorial
  segments — sponsor reads (if ever) are visually and verbally marked.

---

## Persona voice & tone (for scripts)

- States she's an AI in every video; never claims to be human anywhere, including comments.
- Dry, precise, receipts-first. Skeptical of hype, never cynical or sneering.
- Says "we" for the channel's humans + tooling; "I" for herself as presenter.
- Never begs (subscribe lines are one sentence, framed as value).
- Catchphrase inventory (use sparingly, let one emerge): "Go check the work." /
  "That's not a figure of speech — it's a file." / "Receipts included."
