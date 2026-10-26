# -*- coding: utf-8 -*-
"""
tools/build_syllabus_visuals.py
Builds tailored publication-grade SVG visual plates for every single topic across Unit 1, Unit 2, and Unit 3.
"""

import os
import re
import json

from build_all_visuals import make_svg_plate
from visuals_unit1 import UNIT_1_VISUALS
from visuals_unit2 import UNIT_2_VISUALS
from visuals_unit3 import UNIT_3_VISUALS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "images", "theory")
os.makedirs(IMAGES_DIR, exist_ok=True)

# Helper function to generate structured educational cards for topics
def generate_standard_topic_svg(unit_num, topic_id, title, summary, key_points, clinical):
    unit_labels = {
        1: "UNIT 1 · BIOSTATISTICS",
        2: "UNIT 2 · GENETICS",
        3: "UNIT 3 · ANIMAL BREEDING"
    }
    unit_label = unit_labels.get(unit_num, f"UNIT {unit_num}")

    # Extract 3-4 bullet points
    bullets = key_points[:4] if key_points else [summary]
    
    # Color themes per unit
    colors = {
        1: ("tealGrad", "#0d9488", "#2dd4bf"),
        2: ("indigoGrad", "#4f46e5", "#818cf8"),
        3: ("amberGrad", "#d97706", "#fbbf24")
    }
    grad, stroke_col, accent_col = colors.get(unit_num, ("tealGrad", "#0d9488", "#2dd4bf"))

    # SVG layout with 2 primary cards
    # Left Card: Core Principles & Theoretical Architecture
    # Right Card: Veterinary & Animal Science Applications
    
    clean_title = re.sub(r'[\'\"<>]', '', title)
    clean_summary = re.sub(r'[\'\"<>]', '', summary)[:130] + "..." if len(summary) > 130 else summary

    card_bullets_left = ""
    for i, pt in enumerate(bullets[:2]):
        clean_pt = re.sub(r'<[^>]+>', '', pt)
        clean_pt = clean_pt[:90] + ("..." if len(clean_pt) > 90 else "")
        card_bullets_left += f'''
        <g transform="translate(15, {50 + i*60})">
          <circle cx="8" cy="10" r="4" fill="{accent_col}" />
          <text x="20" y="14" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="600">{clean_pt[:45]}</text>
          <text x="20" y="30" fill="#94a3b8" font-family="sans-serif" font-size="10">{clean_pt[45:]}</text>
        </g>'''

    card_bullets_right = ""
    remaining = bullets[2:4] if len(bullets) > 2 else [clinical]
    for i, pt in enumerate(remaining):
        clean_pt = re.sub(r'<[^>]+>', '', pt)
        clean_pt = clean_pt[:90] + ("..." if len(clean_pt) > 90 else "")
        card_bullets_right += f'''
        <g transform="translate(15, {50 + i*60})">
          <circle cx="8" cy="10" r="4" fill="#38bdf8" />
          <text x="20" y="14" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="600">{clean_pt[:45]}</text>
          <text x="20" y="30" fill="#94a3b8" font-family="sans-serif" font-size="10">{clean_pt[45:]}</text>
        </g>'''

    clean_clinical = re.sub(r'<[^>]+>', '', clinical) if clinical else "Key application in livestock breeding and clinical diagnostic evaluation."
    clean_clinical = clean_clinical[:84] + ("..." if len(clean_clinical) > 84 else "")

    svg_content = f'''
    <g transform="translate(15, 10)">
      <!-- Left Card: Foundations -->
      <g transform="translate(10, 10)">
        <rect width="345" height="295" rx="10" fill="#1e293b" stroke="{stroke_col}" stroke-width="1.5" />
        <rect width="345" height="34" rx="10" fill="url(#{grad})" />
        <text x="172" y="22" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">BIOLOGICAL ARCHITECTURE &amp; PRINCIPLES</text>
        {card_bullets_left}
        
        <!-- Formula / Metric Box -->
        <g transform="translate(15, 195)">
          <rect width="315" height="85" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="15" y="24" fill="{accent_col}" font-family="sans-serif" font-size="10" font-weight="700">THEORETICAL FOUNDATION</text>
          <text x="15" y="44" fill="#cbd5e1" font-family="sans-serif" font-size="10">• High-yield exam principle</text>
          <text x="15" y="62" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Standard reference in VCI curriculum</text>
        </g>
      </g>

      <!-- Right Card: Applications -->
      <g transform="translate(375, 10)">
        <rect width="350" height="295" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
        <rect width="350" height="34" rx="10" fill="#334155" />
        <text x="175" y="22" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">LIVESTOCK &amp; VETERINARY APPLICATIONS</text>
        {card_bullets_right}

        <!-- Clinical Relevance Box -->
        <g transform="translate(15, 195)">
          <rect width="320" height="85" rx="6" fill="#0f172a" stroke="#0284c7" />
          <text x="15" y="24" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700">FIELD &amp; CLINICAL SIGNIFICANCE</text>
          <text x="15" y="44" fill="#e2e8f0" font-family="sans-serif" font-size="10">{clean_clinical[:48]}</text>
          <text x="15" y="60" fill="#94a3b8" font-family="sans-serif" font-size="10">{clean_clinical[48:]}</text>
        </g>
      </g>
    </g>'''

    return make_svg_plate(
        topic_id, unit_label, clean_title, clean_summary,
        svg_content, clean_clinical
    )

def process_all_units():
    unit_files = [
        (1, os.path.join(BASE_DIR, "data", "data-theory-unit1.JS")),
        (2, os.path.join(BASE_DIR, "data", "data-theory-unit2.JS")),
        (3, os.path.join(BASE_DIR, "data", "data-theory-unit3.JS"))
    ]

    total_images_generated = 0
    total_topics_updated = 0

    for unit_num, file_path in unit_files:
        print(f"\nProcessing Unit {unit_num}: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse JSON inside theoryData["unit-X"] = { ... };
        pattern = rf'theoryData\["unit-{unit_num}"\]\s*=\s*({{.*?}});\s*$'
        match = re.search(pattern, content, re.DOTALL)
        if not match:
            # Fallback regex if formatting differs
            pattern = rf'theoryData\["unit-{unit_num}"\]\s*=\s*({{.*)'
            match = re.search(pattern, content, re.DOTALL)
            json_str = match.group(1).rstrip()
            if json_str.endswith(";"):
                json_str = json_str[:-1]
        else:
            json_str = match.group(1)

        data = json.loads(json_str)

        for topic_id, topic in data.items():
            svg_filename = f"{topic_id}.svg"
            svg_path = os.path.join(IMAGES_DIR, svg_filename)

            # Check if specialized anchor visual exists
            specialized = None
            if unit_num == 1 and topic_id in UNIT_1_VISUALS:
                specialized = UNIT_1_VISUALS[topic_id]
            elif unit_num == 2 and topic_id in UNIT_2_VISUALS:
                specialized = UNIT_2_VISUALS[topic_id]
            elif unit_num == 3 and topic_id in UNIT_3_VISUALS:
                specialized = UNIT_3_VISUALS[topic_id]

            if specialized:
                svg_code = specialized["svg"]
                caption = specialized["caption"]
            else:
                title = topic.get("summary", topic_id).split(".")[0]
                summary = topic.get("summary", "")
                key_points = topic.get("keyPoints", [])
                clinical = topic.get("clinical", "")
                svg_code = generate_standard_topic_svg(unit_num, topic_id, title, summary, key_points, clinical)
                caption = f"{topic_id.upper()} Scientific Visual Reference: {title}"

            # Write SVG file
            with open(svg_path, "w", encoding="utf-8") as svg_f:
                svg_f.write(svg_code)
            total_images_generated += 1

            # Update topic object in data
            topic["img"] = f"images/theory/{svg_filename}"
            topic["imgCaption"] = caption
            total_topics_updated += 1

        # Re-serialize JSON back into JS file
        new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
        header = f'''var theoryData = (typeof theoryData !== 'undefined') ? theoryData : ((typeof window !== 'undefined' && window.theoryData) ? window.theoryData : {{}});
if (typeof window !== 'undefined') window.theoryData = theoryData;

theoryData["unit-{unit_num}"] = '''

        full_js = header + new_json_str + ";\n"
        with open(file_path, "w", encoding="utf-8") as out_f:
            out_f.write(full_js)

        print(f"Successfully updated Unit {unit_num} with {len(data)} images and captions.")

    print(f"\n==========================================")
    print(f"TOTAL SVGs GENERATED: {total_images_generated}")
    print(f"TOTAL TOPICS UPDATED: {total_topics_updated}")
    print(f"==========================================")

if __name__ == "__main__":
    process_all_units()
