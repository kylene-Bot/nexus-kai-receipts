# Runbook — remoting in and starting Claude

The one-page ritual for working on the channel from anywhere. Kylene's Mac mini is the
production machine; you reach it over SSH (Tailscale) and run Claude Code inside tmux so
nothing dies when your laptop sleeps, the SSH drops, or the power goes out.

## End a session (leave everything running — the normal way)

```
Ctrl-b then d        # detach from tmux; Claude keeps running on the Mini
exit                 # close the SSH connection
```
Closing the laptop without doing any of this is also fine.

## Resume later the same day

```bash
ssh Kylene@100.89.85.81
tmux attach -t claude
```
You land mid-conversation, exactly where you detached.

## New day / after a power outage / fresh start

```bash
ssh Kylene@100.89.85.81
tmux attach -t claude || tmux new -s claude
cd ~/nexus-kai-receipts && git pull origin main
claude                      # or: claude --continue  (reload last conversation)
```

Standing kickoff prompt:

> Read PRODUCTION.md, brand/KYLENE.md, pipeline/README.md, and the newest file in
> scripts/, then tell me the current state of the channel relaunch and what the next
> step is. Wait for my go before spending any render credits.

## Actually stopping things (rarely needed)

| Goal | Command |
|---|---|
| End Claude, keep the tmux wrapper | `/exit` inside Claude |
| Remove the wrapper too | `tmux kill-session -t claude` at the shell |

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ssh: Operation timed out` | Cold Tailscale tunnel: `ping -c 3 100.89.85.81`, wait, retry ssh |
| `tmux attach` → "no sessions" | Mini rebooted — run the new-day sequence |
| Mouse spews `35;47;30M…` garbage | Quit Terminal fully, reopen; keyboard-only in the SSH tab |
| Can't copy a URL out of the SSH tab | New LOCAL tab (`Carl@` prompt): `ssh Kylene@100.89.85.81 "tmux capture-pane -pt claude -J" \| grep -oE 'https://claude[^ ]+' \| tail -1 \| pbcopy` |
| Header says "Claude API" / 401 / Remote Control refused | A leftover `CLAUDE_CODE_OAUTH_TOKEN`/`ANTHROPIC_API_KEY` is overriding the login — clear with `launchctl unsetenv`, `tmux set-environment -gr`, `unset`, check `~/.claude/settings.json`, then `claude auth login` (resolved 2026-07-06; keep for reference) |

## Auth (settled 2026-07-06)

- Logged in with the Claude Max account; the credential persists across reboots.
- **Never run `/logout`** — the only command that forgets it.
- `/remote-control` in any session → watch/steer it from claude.ai or your phone, no SSH.
- Prompt tells you the machine: `Carl@CarlBerger` = your Mac, `kylene@Kylenes-Mini` = the Mini.
  Clipboard/browser things run at `Carl@`; Mini things run at `kylene@`.

## Standing rules

- Pipeline credentials live in `~/.zshenv` on the Mini (`ELEVENLABS_API_KEY`,
  `HEYGEN_API_KEY`, `KYLENE_VOICE_ID`, `KYLENE_AVATAR_ID`) — never in chat, never in
  this repo. (As of 2026-07-06 these are still TO-DO — .zshenv was empty.)
- Sessions confirm before spending HeyGen render credits (see `pipeline/README.md`).
- Anything decided in a session gets committed and pushed — the repo is the memory,
  chat is not.
- Mini settings that keep it always-on: System Settings → Energy → prevent sleep +
  wake for network access; Users & Groups → automatic login (unlocks the keychain
  after reboots so stored credentials work over SSH).
