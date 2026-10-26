# -*- coding: utf-8 -*-
"""
tools/build_all_visuals.py
Generates 100% legal, high-fidelity, publication-grade SVG visual plates
for all 79 syllabus topics across Unit 1, Unit 2, and Unit 3 in the
Animal Genetics & Breeding curriculum.
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_THEORY_DIR = os.path.join(BASE_DIR, "images", "theory")
os.makedirs(IMAGES_THEORY_DIR, exist_ok=True)

def make_svg_plate(topic_id, unit_label, title, subtitle, main_svg_elements, footer_takeaway):
    """
    Renders a unified, high-contrast, modern scientific plate with
    crisp typography, background blueprint grid, and accessible color coding.
    """
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="800" height="480">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9" />
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
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="800" height="480" fill="url(#bgGrad)" rx="16" />
  <rect width="800" height="480" fill="url(#gridPattern)" rx="16" />
  <rect width="798" height="478" x="1" y="1" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" rx="15" />

  <!-- Top Header Banner -->
  <g transform="translate(24, 20)">
    <rect width="130" height="24" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="65" y="16" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" letter-spacing="1" text-anchor="middle">{unit_label}</text>

    <rect x="138" y="0" width="65" height="24" rx="6" fill="url(#tealGrad)" />
    <text x="170" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="800" text-anchor="middle">{topic_id.upper()}</text>

    <text x="215" y="17" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700">{title}</text>
    <text x="215" y="34" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">{subtitle}</text>
  </g>

  <!-- Central Scientific Diagram Canvas -->
  <g transform="translate(24, 68)">
    {main_svg_elements}
  </g>

  <!-- High-Yield Takeaway Footer Bar -->
  <g transform="translate(24, 424)">
    <rect width="752" height="38" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1" />
    <circle cx="20" cy="19" r="6" fill="#14b8a6" />
    <text x="36" y="23" fill="#38bdf8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">CORE TAKEAWAY:</text>
    <text x="145" y="23" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">{footer_takeaway}</text>
  </g>
</svg>'''
    return svg

print("SVG helper loaded.")
