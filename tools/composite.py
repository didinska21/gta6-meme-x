#!/usr/bin/env python3
"""Composite the final meme: variant1.png + make.fun's real press mark.

The generated scene already stars the make.fun ghost (sparkle eyes, magenta
star coin in hand). This step pastes the crisp press mark (assets/mark-1024.png,
from https://make.fun/press/) onto the gaming chair's headrest, where a brand
emblem naturally sits, so the official ghost badge is in the picture pixel-exact
and still reads when the judge shrinks the picture to 480x480.

    python3 tools/composite.py
"""
from PIL import Image

BASE = "meme/variant1.png"
MARK = "assets/mark-1024.png"
OUT = "meme/final.png"
MARK_SIZE = 210
CENTRE = (1364, 736)  # gaming-chair headrest, in the 1600x1600 scene


def main():
    base = Image.open(BASE).convert("RGBA")
    mark = Image.open(MARK).convert("RGBA").resize(
        (MARK_SIZE, MARK_SIZE), Image.LANCZOS)
    x = CENTRE[0] - MARK_SIZE // 2
    y = CENTRE[1] - MARK_SIZE // 2
    base.alpha_composite(mark, (x, y))
    base.convert("RGB").save(OUT)
    print("wrote", OUT, base.size)


if __name__ == "__main__":
    main()
