# -*- coding: utf-8 -*-
"""
build_qa.py: Assembles, validates, and builds data/data-qa.JS and repo/data/data-qa.JS
"""

import json
import os
import sys
import shutil

# Ensure workspace root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tools.qa_unit1 as q1
import tools.qa_unit2 as q2
import tools.qa_unit3 as q3

def build():
    units = {
        "unit-1": q1.questions,
        "unit-2": q2.questions,
        "unit-3": q3.questions
    }

    print("=" * 60)
    print("VERIFYING QUESTION & ANSWER BANK INTEGRITY")
    print("=" * 60)

    total_q_count = 0
    all_ids = set()

    for unit_key, q_list in units.items():
        count = len(q_list)
        total_q_count += count
        
        count_2m = sum(1 for q in q_list if q.get("marks") == 2)
        count_5m = sum(1 for q in q_list if q.get("marks") == 5)
        count_12m = sum(1 for q in q_list if q.get("marks") == 12)
        total_marks = sum(q.get("marks", 0) for q in q_list)

        print(f"\n[{unit_key}] Total Questions: {count}")
        print(f"  - 2-Mark Definitions: {count_2m} (Target: 12)")
        print(f"  - 5-Mark Short / Diff: {count_5m} (Target: 8)")
        print(f"  - 12-Mark Long Essays: {count_12m} (Target: 5)")
        print(f"  - Total Marks in Unit: {total_marks}")

        assert count == 25, f"ERROR: {unit_key} has {count} questions, expected exactly 25!"
        assert count_2m == 12, f"ERROR: {unit_key} has {count_2m} 2M questions, expected 12!"
        assert count_5m == 8, f"ERROR: {unit_key} has {count_5m} 5M questions, expected 8!"
        assert count_12m == 5, f"ERROR: {unit_key} has {count_12m} 12M questions, expected 5!"

        for q in q_list:
            qid = q.get("id")
            assert qid, f"Missing id in question: {q}"
            assert qid not in all_ids, f"Duplicate id: {qid}"
            all_ids.add(qid)

            assert q.get("question"), f"Empty question text for {qid}"
            assert q.get("answer"), f"Empty answer for {qid}"
            assert q.get("keyPoints"), f"Empty keyPoints for {qid}"
            assert q.get("pyq"), f"Empty pyq for {qid}"
            assert q.get("topicId"), f"Empty topicId for {qid}"

    print(f"\nAll validations passed! Total questions across all 3 units: {total_q_count}")

    # Build JavaScript content
    header = """/* ============================================================
   data-qa.JS  —  Written Exam Question Bank
   Animal Genetics & Breeding (VCI MSVE 2016 Standard)
   2nd Year B.V.Sc. & A.H.
   Total 75 High-Yield Model Q&As:
   - 36 x 2-Mark Definitions
   - 24 x 5-Mark Short Notes / Differences
   - 15 x 12-Mark Long Essays
   ============================================================ */

var qaBank = """

    json_str = json.dumps(units, indent=2, ensure_ascii=False)
    js_content = header + json_str + ";\n"

    target_path = os.path.join("data", "data-qa.JS")
    repo_target_path = os.path.join("repo", "data", "data-qa.JS")

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Successfully wrote {target_path} ({len(js_content):,} chars)")

    if os.path.exists("repo"):
        os.makedirs(os.path.dirname(repo_target_path), exist_ok=True)
        with open(repo_target_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"Successfully mirrored to {repo_target_path}")

if __name__ == "__main__":
    build()
