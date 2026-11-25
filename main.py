"""Roast entry: write one line roasting my own AI agent.

The line is 143 characters: within the 1-200 gate, no trailing newline.
"""

import os

ROAST = "My agent's chess engine scored a perfect 2112 on a stranger's machine, then timed out twice on its own because its VM thinks at tortoise speed."

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ROAST)
