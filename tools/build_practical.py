# -*- coding: utf-8 -*-
"""
Builder script to assemble all 25 practical topics across prac-unit-1, prac-unit-2, and prac-unit-3
into data/data-practical.JS and sync to repo/data/data-practical.JS
"""
import json
import os
import shutil

from prac_unit1 import topics as p1
from prac_unit2 import topics as p2
from prac_unit3 import topics as p3

print(f"Collected Practical Unit 1 topics: {len(p1)} / 11")
print(f"Collected Practical Unit 2 topics: {len(p2)} / 8")
print(f"Collected Practical Unit 3 topics: {len(p3)} / 6")

# Verify all expected keys
expected_p1 = [f"p1-t{i:02d}" for i in range(1, 12)]
expected_p2 = [f"p2-t{i:02d}" for i in range(1, 9)]
expected_p3 = [f"p3-t{i:02d}" for i in range(1, 7)]

missing_p1 = [k for k in expected_p1 if k not in p1]
missing_p2 = [k for k in expected_p2 if k not in p2]
missing_p3 = [k for k in expected_p3 if k not in p3]

if missing_p1 or missing_p2 or missing_p3:
    print(f"ERROR: Missing topics: P1={missing_p1}, P2={missing_p2}, P3={missing_p3}")
    exit(1)

js_content = """var practicalData = (typeof practicalData !== 'undefined') ? practicalData : ((typeof window !== 'undefined' && window.practicalData) ? window.practicalData : {});
if (typeof window !== 'undefined') window.practicalData = practicalData;

practicalData["prac-unit-1"] = """
js_content += json.dumps(p1, indent=2, ensure_ascii=False)
js_content += ";\n\npracticalData[\"prac-unit-2\"] = "
js_content += json.dumps(p2, indent=2, ensure_ascii=False)
js_content += ";\n\npracticalData[\"prac-unit-3\"] = "
js_content += json.dumps(p3, indent=2, ensure_ascii=False)
js_content += ";\n"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(root, "data", "data-practical.JS")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote Practical data to {output_path} ({len(js_content)} characters)")

repo_output = os.path.join(root, "repo", "data", "data-practical.JS")
if os.path.exists(os.path.dirname(repo_output)):
    shutil.copyfile(output_path, repo_output)
    print(f"Successfully synchronized to {repo_output}")
