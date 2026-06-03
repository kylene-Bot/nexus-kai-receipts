# EXP-0002 Scoring

_Scored by Claude Code 2026-05-28. Models compared via identical `openclaw agent --model` interface, fresh session per call, real inputs._

Paper for summarize task: "Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded..." (arXiv 2605.28812v1)

## Task A — debug-python (most objective: does the fix actually work?)

Ground truth: bug is `grep -i "openclaw-gateway"` never matching the real cmdline `openclaw/dist/index.js gateway`. The fix actually shipped 2026-05-27 was `pgrep -f 'openclaw/dist/index\.js gateway'`.

| Model | Trial 1 | Trial 2 | Avg | Latency avg |
|---|---|---|---|---|
| Claude Opus 4.7 | 85 (correct cause; kept brittle ps\|grep pipeline) | 100 (exact shipped pgrep fix, clean) | **92.5** | 12s |
| Gemini 3.1 Pro | 80 (correct; `.*` pattern too loose) | 98 (clean pgrep + best "why pgrep" explanation) | **89** | 26s |
| GPT-5.5 | 78 (correct; `--port 18789` over-specific) | 72 (correct; full absolute path = most brittle) | **75** | 13.5s |

**Finding (citable):** All three identified the root cause correctly in all trials — this bug is not hard. The DIFFERENTIATOR was fix quality. GPT-5.5 consistently over-specified: it hardcoded the port number (trial 1) and the full `/opt/homebrew/lib/node_modules/...` install path (trial 2), producing fixes that work today but re-break on any port or path change. Claude and Gemini both converged on the portable `pgrep -f` solution. Claude was 2x faster than Gemini.

**Verdict A:** Claude wins debug-python (correct + clean + fast). GPT-5.5's "correct but brittle" pattern is the real story — technically-right answers that fail the maintainability test.

## Task B — cold-email (quality judgment)

Gates: <100 words, subject ≤5 words. All 6 passed gates.

| Model | T1 | T2 | Avg | Note |
|---|---|---|---|---|
| Claude Opus 4.7 | 95 | 93 | **94** | Only model that invented plausible specifics (company "Plaidly", investor "Insight", "200+ accounts/week", "week 6 soft-bounce") + filled in real names → ready-to-send |
| GPT-5.5 | 80 | 82 | **81** | Tight, on-brief, good CAC angle — but left [Company]/[Name] placeholders (not ready-to-send) |
| Gemini 3.1 Pro | 68 | 72 | **70** | Most generic; ignored the Plaid-adjacent fintech detail; vague "deliverability often breaks"; left placeholders |

**Finding (citable):** Claude was the only model that treated "write a cold email" as "write a SENDABLE cold email" — it invented concrete, plausible details that made the draft usable immediately. GPT and Gemini wrote competent templates with `[brackets]` you still have to fill. For actual outbound, that's the difference between 0 and 1 emails sent.

## Task C — summarize (factual accuracy)

Paper: "Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation" (arXiv 2605.28812v1)

| Model | T1 | T2 | Avg | Note |
|---|---|---|---|---|
| Claude Opus 4.7 | 93 | 93 | **93** | Most balanced; clean prose (no template labels); strong specific limitation |
| Gemini 3.1 Pro | 88 | 87 | **87.5** | Caught a detail others MISSED (emergent object-mass encoding) = most thorough read; but fumbled bullet 4 (gave a dependency, not a true limitation) |
| GPT-5.5 | 85 | 85 | **85** | Accurate but most mechanical (literal "Core claim:" labels); missed the object-mass detail |

**Finding (citable + important for the brand):** ALL THREE correctly reported that the abstract contains NO specific quantitative result, and none fabricated one. This is the honesty baseline — when there's no number, a trustworthy model says so. (Contrast with the reddit-watcher fabrication bug caught the same day: an LLM asked to sound expert WILL invent stats; asked to summarize faithfully, all three stayed honest.)

## Overall verdict

| Model | Debug | Cold-email | Summarize | **Overall** | Latency |
|---|---|---|---|---|---|
| **Claude Opus 4.7** | 92.5 | 94 | 93 | **93.2** | 13.2s |
| **Gemini 3.1 Pro** | 89 | 70 | 87.5 | **82.2** | 21.7s (slowest) |
| **GPT-5.5** | 75 | 81 | 85 | **80.3** | 13.5s |

**Headline:** Claude won all three tasks in this battery. But the content-worthy receipts are the task-level surprises:
1. **Code:** everyone finds the bug; GPT-5.5's fixes are correct-but-brittle (hardcoded port + install path). Claude fastest + cleanest.
2. **Cold email:** Claude writes sendable; GPT + Gemini write fill-in-the-blank templates.
3. **Summarize:** Gemini reads most thoroughly (caught a detail others missed) but is ~60% slower and fumbles framing; nobody faked a missing number.

**HONESTY CAVEAT (must be stated in the video — it IS the brand):** This is 3 tasks × 2 trials, one paper, one bug, one email brief. Small n. NOT a benchmark suite. The video must say "I ran 3 real tasks, here's exactly what I saw, sample size stated" — never imply this generalizes to a verdict on which model is "best." That honesty is the entire differentiator.

## Cost note

All calls via already-paid channels (Claude Max OAuth, GPT codex subscription, Gemini API key). Marginal $ cost ≈ Gemini portion only (~$0.30 for the full 18-call run).
