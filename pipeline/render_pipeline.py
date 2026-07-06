#!/usr/bin/env python3
"""Kylene render pipeline: script text -> ElevenLabs audio -> HeyGen avatar video.

Stdlib-only (urllib). Reads all credentials/IDs from environment variables — never
hardcode keys in this file or commit them anywhere in this repo.

Required environment:
    ELEVENLABS_API_KEY   ElevenLabs API key
    HEYGEN_API_KEY       HeyGen API key
    KYLENE_VOICE_ID      ElevenLabs voice ID for the locked Kylene voice
    KYLENE_AVATAR_ID     HeyGen avatar ID for the locked Kylene Hayes look

Optional environment (defaults are the frozen persona settings):
    KYLENE_STABILITY=0.6  KYLENE_SIMILARITY=0.75  KYLENE_STYLE=0.0  KYLENE_SPEED=0.95

Usage:
    python3 pipeline/render_pipeline.py --script path/to/script.txt --out renders/test3
    python3 pipeline/render_pipeline.py --script - --out renders/test3   # read stdin

Every run writes a receipt JSON (request params, response IDs, timings) next to the
output — receipts are the brand, including for our own production.

Network note: this repo's cloud environment must allow these hosts in its network
policy before the script can run there (verified blocked 2026-07-03):
    api.elevenlabs.io, api.heygen.com, upload.heygen.com, *.heygen.ai
Endpoint shapes below are as documented at time of writing; the script surfaces raw
API error bodies so any drift is diagnosable from the receipt.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

ELEVEN_TTS = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128"
HEYGEN_UPLOAD = "https://upload.heygen.com/v1/asset"
HEYGEN_GENERATE = "https://api.heygen.com/v2/video/generate"
HEYGEN_STATUS = "https://api.heygen.com/v1/video_status.get?video_id={video_id}"


def env(name, default=None, required=False):
    v = os.environ.get(name, default)
    if required and not v:
        sys.exit(f"Missing required environment variable: {name}")
    return v


def http(url, method="GET", headers=None, body=None, timeout=120):
    req = urllib.request.Request(url, data=body, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def tts(text, receipt):
    """Generate narration audio. Returns MP3 bytes."""
    voice_id = env("KYLENE_VOICE_ID", required=True)
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": float(env("KYLENE_STABILITY", "0.6")),
            "similarity_boost": float(env("KYLENE_SIMILARITY", "0.75")),
            "style": float(env("KYLENE_STYLE", "0.0")),
            "use_speaker_boost": True,
            "speed": float(env("KYLENE_SPEED", "0.95")),
        },
    }
    receipt["elevenlabs_request"] = {k: v for k, v in payload.items() if k != "text"}
    receipt["script_chars"] = len(text)
    status, data = http(
        ELEVEN_TTS.format(voice_id=voice_id),
        method="POST",
        headers={"xi-api-key": env("ELEVENLABS_API_KEY", required=True),
                 "Content-Type": "application/json"},
        body=json.dumps(payload).encode(),
    )
    if status != 200:
        sys.exit(f"ElevenLabs TTS failed ({status}): {data[:500]!r}")
    return data


def heygen_upload_audio(mp3_bytes, receipt):
    """Upload narration to HeyGen as an asset. Returns asset id."""
    status, data = http(
        HEYGEN_UPLOAD,
        method="POST",
        headers={"x-api-key": env("HEYGEN_API_KEY", required=True),
                 "Content-Type": "audio/mpeg"},
        body=mp3_bytes,
    )
    if status != 200:
        sys.exit(f"HeyGen asset upload failed ({status}): {data[:500]!r}")
    asset = json.loads(data)
    asset_id = asset.get("data", {}).get("id") or asset.get("data", {}).get("asset_id")
    if not asset_id:
        sys.exit(f"HeyGen upload: no asset id in response: {data[:500]!r}")
    receipt["heygen_audio_asset_id"] = asset_id
    return asset_id


def heygen_generate(audio_asset_id, receipt, width=1920, height=1080):
    """Submit the render. Returns video id."""
    payload = {
        "video_inputs": [{
            "character": {"type": "avatar",
                          "avatar_id": env("KYLENE_AVATAR_ID", required=True),
                          "avatar_style": "normal"},
            "voice": {"type": "audio", "audio_asset_id": audio_asset_id},
        }],
        "dimension": {"width": width, "height": height},
    }
    receipt["heygen_request"] = payload
    status, data = http(
        HEYGEN_GENERATE,
        method="POST",
        headers={"x-api-key": env("HEYGEN_API_KEY", required=True),
                 "Content-Type": "application/json"},
        body=json.dumps(payload).encode(),
    )
    if status != 200:
        sys.exit(f"HeyGen generate failed ({status}): {data[:500]!r}")
    video_id = json.loads(data).get("data", {}).get("video_id")
    if not video_id:
        sys.exit(f"HeyGen generate: no video_id in response: {data[:500]!r}")
    receipt["heygen_video_id"] = video_id
    return video_id


def heygen_wait(video_id, receipt, poll_seconds=15, timeout_minutes=30):
    """Poll until the render completes. Returns the download URL."""
    deadline = time.time() + timeout_minutes * 60
    while time.time() < deadline:
        status, data = http(
            HEYGEN_STATUS.format(video_id=video_id),
            headers={"x-api-key": env("HEYGEN_API_KEY", required=True)},
        )
        info = json.loads(data).get("data", {}) if status == 200 else {}
        state = info.get("status")
        print(f"  render status: {state}", flush=True)
        if state == "completed":
            receipt["video_url"] = info.get("video_url")
            return info.get("video_url")
        if state == "failed":
            sys.exit(f"HeyGen render failed: {json.dumps(info)[:500]}")
        time.sleep(poll_seconds)
    sys.exit("Timed out waiting for HeyGen render")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script", required=True, help="path to script text file, or - for stdin")
    ap.add_argument("--out", required=True, help="output directory for mp3/mp4/receipt")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    args = ap.parse_args()

    text = sys.stdin.read() if args.script == "-" else open(args.script, encoding="utf-8").read()
    os.makedirs(args.out, exist_ok=True)
    receipt = {"started_unix": time.time(), "dimension": [args.width, args.height]}

    print("1/4 ElevenLabs TTS…", flush=True)
    mp3 = tts(text, receipt)
    mp3_path = os.path.join(args.out, "narration.mp3")
    open(mp3_path, "wb").write(mp3)
    print(f"    saved {mp3_path} ({len(mp3)} bytes)")

    print("2/4 Upload audio to HeyGen…", flush=True)
    asset_id = heygen_upload_audio(mp3, receipt)

    print("3/4 Submit render…", flush=True)
    video_id = heygen_generate(asset_id, receipt, args.width, args.height)

    print("4/4 Waiting for render…", flush=True)
    url = heygen_wait(video_id, receipt)
    status, data = http(url)
    if status != 200:
        sys.exit(f"Video download failed ({status}) — URL host may need network allowlisting: {url}")
    mp4_path = os.path.join(args.out, "render.mp4")
    open(mp4_path, "wb").write(data)
    receipt["finished_unix"] = time.time()
    receipt["render_bytes"] = len(data)

    receipt_path = os.path.join(args.out, "receipt.json")
    json.dump(receipt, open(receipt_path, "w"), indent=2)
    print(f"Done: {mp4_path}\nReceipt: {receipt_path}")
    print("Next: python3 pipeline/analyze_render.py " + mp4_path)


if __name__ == "__main__":
    main()
