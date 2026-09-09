# -*- coding: utf-8 -*-
"""
Builder script to assemble all 29 topics of Unit 2 into data/data-theory-unit2.JS
"""
import json
import os

from unit2_part1 import topics as p1
from unit2_part2 import topics as p2
from unit2_part3 import topics as p3
from unit2_part4 import topics as p4

all_topics = {}
all_topics.update(p1)
all_topics.update(p2)
all_topics.update(p3)
all_topics.update(p4)

print(f"Total Unit 2 topics collected: {len(all_topics)}")
expected_keys = [f"u2-t{i:02d}" for i in range(1, 30)]
missing = [k for k in expected_keys if k not in all_topics]
if missing:
    print(f"ERROR: Missing topics: {missing}")
    exit(1)

js_content = """var theoryData = (typeof theoryData !== 'undefined') ? theoryData : ((typeof window !== 'undefined' && window.theoryData) ? window.theoryData : {});
if (typeof window !== 'undefined') window.theoryData = theoryData;

theoryData["unit-2"] = """

js_content += json.dumps(all_topics, indent=2, ensure_ascii=False)
js_content += ";\n"

output_path = os.path.join(os.path.dirname(__file__), "..", "data", "data-theory-unit2.JS")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote Unit 2 theory data to {output_path} ({len(js_content)} characters)")
