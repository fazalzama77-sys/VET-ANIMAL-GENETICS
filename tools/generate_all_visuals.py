# -*- coding: utf-8 -*-
"""
tools/generate_all_visuals.py
Generates 100% legal, standalone SVG visual plates for all 79 theory topics
in Animal Genetics and Breeding, and links them into data/data-theory-unit*.JS
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_THEORY_DIR = os.path.join(BASE_DIR, "images", "theory")
os.makedirs(IMAGES_THEORY_DIR, exist_ok=True)

from visuals_unit1 import UNIT_1_VISUALS
from visuals_unit2 import UNIT_2_VISUALS
from visuals_unit3 import UNIT_3_VISUALS

def svg_card(x, y, w, h, title, color_grad, content_lines, stroke="#334155"):
    lines_html = ""
    for i, line in enumerate(content_lines):
        fill = "#f8fafc" if line.startswith("•") else "#94a3b8"
        weight = "700" if line.startswith("•") else "400"
        lines_html += f'<text x="14" y="{48 + i*18}" fill="{fill}" font-family="sans-serif" font-size="11" font-weight="{weight}">{line}</text>'
    
    return f'''
    <g transform="translate({x}, {y})">
      <rect width="{w}" height="{h}" rx="8" fill="#1e293b" stroke="{stroke}" stroke-width="1.5" />
      <rect width="{w}" height="28" rx="8" fill="url(#{color_grad})" />
      <text x="{w/2}" y="18" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">{title}</text>
      {lines_html}
    </g>'''

def make_plate(unit_label, topic_id, title, subtitle, svg_content, takeaway):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="800" height="480">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d9488" />
      <stop offset="100%" stop-color="#14b8a6" />
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4f46e5" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#f59e0b" />
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#e11d48" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="50%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#475569" />
    </linearGradient>
    <pattern id="gridPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#334155" stroke-width="0.5" stroke-opacity="0.25" />
    </pattern>
  </defs>

  <rect width="800" height="480" fill="url(#bgGrad)" rx="16" />
  <rect width="800" height="480" fill="url(#gridPattern)" rx="16" />
  <rect width="798" height="478" x="1" y="1" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" rx="15" />

  <!-- Top Header Banner -->
  <g transform="translate(24, 20)">
    <rect width="130" height="24" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="65" y="16" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" letter-spacing="1" text-anchor="middle">{unit_label}</text>

    <rect x="138" y="0" width="65" height="24" rx="6" fill="url(#tealGrad)" />
    <text x="170" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="800" text-anchor="middle">{topic_id.upper()}</text>

    <text x="215" y="17" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700">{title[:58]}</text>
    <text x="215" y="34" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">{subtitle[:68]}</text>
  </g>

  <!-- Central Scientific Diagram Canvas -->
  <g transform="translate(24, 68)">
    {svg_content}
  </g>

  <!-- High-Yield Takeaway Footer Bar -->
  <g transform="translate(24, 424)">
    <rect width="752" height="38" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1" />
    <circle cx="20" cy="19" r="6" fill="#14b8a6" />
    <text x="36" y="23" fill="#38bdf8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">HIGH-YIELD CORE TAKEAWAY:</text>
    <text x="205" y="23" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">{takeaway[:88]}</text>
  </g>
</svg>'''

print("Generator core loaded.")
