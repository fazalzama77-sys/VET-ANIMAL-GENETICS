# -*- coding: utf-8 -*-
"""
Builder script to assemble all 22 topics of Unit 1 into data/data-theory-unit1.JS
"""
import json
import os

from unit1_part1 import topics as p1
from unit1_part2 import topics as p2
from unit1_part3 import topics as p3

all_topics = {}
all_topics.update(p1)
all_topics.update(p2)
all_topics.update(p3)

print(f"Total Unit 1 topics collected: {len(all_topics)}")
expected_keys = [f"u1-t{i:02d}" for i in range(1, 23)]
missing = [k for k in expected_keys if k not in all_topics]
if missing:
    print(f"ERROR: Missing topics: {missing}")
    exit(1)

js_content = """var theoryData = (typeof theoryData !== 'undefined') ? theoryData : ((typeof window !== 'undefined' && window.theoryData) ? window.theoryData : {});
if (typeof window !== 'undefined') window.theoryData = theoryData;

theoryData["unit-1"] = """

js_content += json.dumps(all_topics, indent=2, ensure_ascii=False)
js_content += ";\n"

output_path = os.path.join(os.path.dirname(__file__), "..", "data", "data-theory-unit1.JS")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote Unit 1 theory data to {output_path} ({len(js_content)} characters)")
