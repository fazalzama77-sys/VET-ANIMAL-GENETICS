# -*- coding: utf-8 -*-
"""
Builder script to assemble all 28 topics of Unit 3 into data/data-theory-unit3.JS
and sync to repo/data/data-theory-unit3.JS
"""
import json
import os
import shutil

from unit3_part1 import topics as p1
from unit3_part2 import topics as p2
from unit3_part3 import topics as p3
from unit3_part4 import topics as p4

all_topics = {}
all_topics.update(p1)
all_topics.update(p2)
all_topics.update(p3)
all_topics.update(p4)

print(f"Total Unit 3 topics collected: {len(all_topics)}")
expected_keys = [f"u3-t{i:02d}" for i in range(1, 29)]
missing = [k for k in expected_keys if k not in all_topics]
if missing:
    print(f"ERROR: Missing topics: {missing}")
    exit(1)

js_content = """var theoryData = (typeof theoryData !== 'undefined') ? theoryData : ((typeof window !== 'undefined' && window.theoryData) ? window.theoryData : {});
if (typeof window !== 'undefined') window.theoryData = theoryData;

theoryData["unit-3"] = """

js_content += json.dumps(all_topics, indent=2, ensure_ascii=False)
js_content += ";\n"

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(root, "data", "data-theory-unit3.JS")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote Unit 3 theory data to {output_path} ({len(js_content)} characters)")

repo_output = os.path.join(root, "repo", "data", "data-theory-unit3.JS")
if os.path.exists(os.path.dirname(repo_output)):
    shutil.copyfile(output_path, repo_output)
    print(f"Successfully synchronized to {repo_output}")
