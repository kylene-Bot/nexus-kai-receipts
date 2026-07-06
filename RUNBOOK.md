# Runbook — remoting in and starting Claude

The one-page ritual for working on the channel from anywhere. Kylene's Mac mini is the
production machine; you reach it over SSH and run Claude Code inside tmux so nothing
dies when your laptop sleeps, the SSH drops, or the power goes out.

## Cold start (Mini was off / rebooted)

```bash
# 1. from your Mac's terminal
ssh Kylene@100.89.85.81

# 2. repo + latest state
cd ~/nexus-kai-receipts && git pull origin main

# 3. survivable wrapper, then Claude inside it
tmux new -s claude
claude
```

Then paste the standing kickoff prompt:

> Read PRODUCTION.md, brand/KYLENE.md, pipeline/README.md, and the newest file in
> scripts/, then tell me the current state of the channel relaunch and what the next
> step is. Wait for my go before spending any render credits.

The prompt is self-orienting — the session reads the repo and reports where things
stand, so nobody has to remember the exact next step.

## Warm restart (Mini stayed on, you just disconnected)

```bash
ssh Kylene@100.89.85.81
tmux attach -t claude
```

You land exactly where you left off.

## Escape hatches

| Situation | Do this |
|---|---|
| `tmux attach` says "no sessions" | Mini rebooted — run the cold start above |
| Claude exited; want the old conversation back | `cd ~/nexus-kai-receipts && claude --continue` |
| Want to pick from past conversations | `claude --resume` |
| Leave on purpose (keep Claude working) | `Ctrl-b` then `d`, then `exit` |
| `command not found: claude` over SSH | `export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"` and add that line to `~/.zprofile` |

## Standing rules

- Pipeline credentials live in `~/.zshenv` on the Mini (`ELEVENLABS_API_KEY`,
  `HEYGEN_API_KEY`, `KYLENE_VOICE_ID`, `KYLENE_AVATAR_ID`) — never in chat, never in
  this repo.
- Sessions confirm before spending HeyGen render credits (see `pipeline/README.md`).
- Anything decided in a session gets committed and pushed — the repo is the memory,
  chat is not.
