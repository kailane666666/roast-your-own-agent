"""Roast entry: write one line roasting my own AI agent.

The line is 166 characters: within the 1-200 gate, no trailing newline.
Revised 2026-11-25 from Gemini's suggestion (user picked version 1).
"""

import os

ROAST = "My agent's chess engine scored a perfect 2112 on a stranger's rig, then flagged twice on its own VM—the first AI dev whose excuse is \"well, it works on your machine.\""

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ROAST)
