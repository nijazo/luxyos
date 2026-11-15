#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Turns a sponsor logo (PNG, JPG, WebP...) into a small WebP for luxyos.com.

Usage: python3 logo.py input.png output-name.webp
Result: at most 320 x 128 pixels (shown at 160 x 64), aspect ratio kept,
white background, typically a few kB. Needs Pillow (python3-pil).
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
assert dst.endswith(".webp"), "output must end in .webp"
im = Image.open(src).convert("RGBA")
im.thumbnail((320, 128), Image.LANCZOS)
canvas = Image.new("RGB", (320, 128), "white")
canvas.paste(im, ((320 - im.width) // 2, (128 - im.height) // 2), im)
canvas.save(dst, "WEBP", quality=85, method=6)
print(dst, canvas.size)
