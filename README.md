# Nexus Kai — Receipts

Raw, unedited outputs from the experiments on the **[Nexus Kai](https://www.youtube.com/@nexuskaiai)** YouTube channel.

The whole point of the channel: **real numbers, no hype, every claim cited.** When a video says "Claude scored 93.2" or "GPT-5.5's fix was brittle," the actual model output and the scoring live here so you can check the work yourself.

## EXP-0002 — ChatGPT vs Claude vs Gemini (3 tasks, 18 runs)
- **Models:** Claude Opus 4.7 · GPT-5.5 · Gemini 3.1 Pro
- **Tasks:** debug a broken shell script · write a cold email · summarize a fresh arXiv paper
- **Method:** 2 trials each, fresh session per call, every output saved to disk *before* scoring

In [`EXP-0002/`](EXP-0002/):
- `*.txt` — the 18 raw model outputs (`<task>-<model>-t<trial>.txt`)
- `_results.json` — run log: per-call latency, char counts, the live-fetched paper
- `SCORING.md` — the rubric, per-task scoring, and the overall scoreboard
- `EXP-0002.md` — the experiment definition

Latencies are measured. Scores are a rubric judgment of the real outputs. Small sample by design (3 tasks × 2 trials = 18 runs) — not a benchmark, an honest look. Check the work.
