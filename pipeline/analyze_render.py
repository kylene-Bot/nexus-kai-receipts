#!/usr/bin/env python3
"""Frame-by-frame mouth analysis for avatar renders.

Extracts a full reference frame, a whole-clip mouth sheet (2.5 fps), and a dense
12 fps burst over a chosen window, so lip-sync artifacts (held-tongue idles,
smeared consonants, idle grins) can be spotted at a glance.

Requires: pip install imageio-ffmpeg   (bundles a static ffmpeg binary)

Usage:
    python3 pipeline/analyze_render.py render.mp4 [--out DIR] [--burst-start 1.5]
        [--crop W:H:X:Y]   # mouth region; default tuned for the Kylene chest-up frame

The default crop (460:340:310:580) assumes 1080-wide portrait or the face centered
as in the standard Kylene framing; pass --crop after checking full_frame.png if the
framing changes (e.g. 16:9 renders).
"""
import argparse
import os
import subprocess
import sys

try:
    import imageio_ffmpeg
except ImportError:
    sys.exit("pip install imageio-ffmpeg first")

FF = imageio_ffmpeg.get_ffmpeg_exe()


def run(*args):
    r = subprocess.run([FF, "-hide_banner", "-loglevel", "error", *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffmpeg failed: {r.stderr[-800:]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("video")
    ap.add_argument("--out", default=None, help="output dir (default: <video>_analysis)")
    ap.add_argument("--crop", default="460:340:310:580", help="mouth crop as W:H:X:Y")
    ap.add_argument("--burst-start", type=float, default=1.5)
    ap.add_argument("--burst-seconds", type=float, default=4.0)
    args = ap.parse_args()

    out = args.out or os.path.splitext(args.video)[0] + "_analysis"
    os.makedirs(out, exist_ok=True)
    crop = f"crop={args.crop},scale=230:170"

    run("-ss", "5", "-i", args.video, "-frames:v", "1", f"{out}/full_frame.png")
    run("-i", args.video,
        "-vf", f"fps=2.5,{crop},tile=8x8:padding=4:color=black",
        "-frames:v", "1", f"{out}/mouth_sheet.png")
    run("-ss", str(args.burst_start), "-t", str(args.burst_seconds), "-i", args.video,
        "-vf", f"fps=12,{crop},tile=8x6:padding=4:color=black",
        "-frames:v", "1", f"{out}/mouth_burst.png")

    print(f"Wrote {out}/full_frame.png (check crop placement)")
    print(f"Wrote {out}/mouth_sheet.png (whole clip @2.5fps)")
    print(f"Wrote {out}/mouth_burst.png ({args.burst_start}s–"
          f"{args.burst_start + args.burst_seconds}s @12fps)")
    print("Look for: held tongue across 5+ consecutive burst frames (pause idle), "
          "smeared teeth on consonants, unmotivated grins between sentences.")


if __name__ == "__main__":
    main()
