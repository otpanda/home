"""Render PNG counterparts of the checked-in SVG artwork.
Requires Python 3 and CairoSVG (pip install cairosvg==2.8.2).
Run from anywhere: python assets/render-assets.py
"""
from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parent
for variant in ("light", "dark", "green", "transparent"):
    source = ROOT / f"otty-{variant}.svg"
    target = ROOT / f"otty-{variant}.png"
    cairosvg.svg2png(url=str(source), write_to=str(target), output_width=1200, output_height=1200)
    print(target.name)
