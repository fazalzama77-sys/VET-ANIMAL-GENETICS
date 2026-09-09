# tools/assemble_quiz.py
# Validates and writes data/data-quiz.JS and repo/data/data-quiz.JS

import json
import os
import re
import shutil
from unit1_data import unit1_mcq, unit1_tf, unit1_fib
from unit2_data import unit2_mcq, unit2_tf, unit2_fib
from unit3_data import unit3_mcq, unit3_tf, unit3_fib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYLLABUS_PATH = os.path.join(BASE_DIR, "data", "data-syllabus.JS")
QUIZ_OUTPUT_PATH = os.path.join(BASE_DIR, "data", "data-quiz.JS")
REPO_QUIZ_PATH = os.path.join(BASE_DIR, "repo", "data", "data-quiz.JS")

# Extract all valid topic IDs from data-syllabus.JS
with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
    syllabus_text = f.read()

valid_topics = set(re.findall(r'"id":\s*"(u\d-t\d+)"', syllabus_text))
print(f"Loaded {len(valid_topics)} valid topic IDs from data-syllabus.JS")

valid_subsections = {
    "unit-1": {"u1-s1", "u1-s2", "u1-s3", "u1-s4", "u1-s5"},
    "unit-2": {"u2-s1", "u2-s2", "u2-s3", "u2-s4", "u2-s5"},
    "unit-3": {"u3-s1", "u3-s2", "u3-s3", "u3-s4", "u3-s5"}
}

units_data = {
    "unit-1": {"mcq": unit1_mcq, "tf": unit1_tf, "fib": unit1_fib},
    "unit-2": {"mcq": unit2_mcq, "tf": unit2_tf, "fib": unit2_fib},
    "unit-3": {"mcq": unit3_mcq, "tf": unit3_tf, "fib": unit3_fib}
}

total_count = 0

for unit_id, formats in units_data.items():
    print(f"\n--- Validating {unit_id} ---")
    mcq_count = len(formats["mcq"])
    tf_count = len(formats["tf"])
    fib_count = len(formats["fib"])
    unit_total = mcq_count + tf_count + fib_count
    total_count += unit_total

    print(f"MCQs: {mcq_count} | TF: {tf_count} | FIB: {fib_count} | Total: {unit_total}")
    assert mcq_count == 90, f"Expected 90 MCQs for {unit_id}, got {mcq_count}"
    assert tf_count == 45, f"Expected 45 TF for {unit_id}, got {tf_count}"
    assert fib_count == 45, f"Expected 45 FIB for {unit_id}, got {fib_count}"

    # Validate MCQs
    for idx, item in enumerate(formats["mcq"]):
        assert "q" in item and item["q"].strip(), f"Empty question in {unit_id} MCQ {idx}"
        assert len(item["o"]) == 4, f"MCQ {idx} in {unit_id} must have 4 options, got {len(item['o'])}"
        assert isinstance(item["a"], int) and 0 <= item["a"] <= 3, f"Invalid answer index in {unit_id} MCQ {idx}: {item['a']}"
        assert item["topicId"] in valid_topics, f"Invalid topicId in {unit_id} MCQ {idx}: {item['topicId']}"
        assert item["subSection"] in valid_subsections[unit_id], f"Invalid subSection in {unit_id} MCQ {idx}: {item['subSection']}"
        assert item["diff"] in (1, 2, 3), f"Invalid diff in {unit_id} MCQ {idx}: {item['diff']}"
        assert "e" in item and item["e"].strip(), f"Missing explanation in {unit_id} MCQ {idx}"

    # Validate TF
    for idx, item in enumerate(formats["tf"]):
        assert "q" in item and item["q"].strip(), f"Empty question in {unit_id} TF {idx}"
        assert isinstance(item["a"], bool), f"Invalid TF answer in {unit_id} TF {idx}: {item['a']}"
        assert item["topicId"] in valid_topics, f"Invalid topicId in {unit_id} TF {idx}: {item['topicId']}"
        assert item["subSection"] in valid_subsections[unit_id], f"Invalid subSection in {unit_id} TF {idx}: {item['subSection']}"
        assert item["diff"] in (1, 2, 3), f"Invalid diff in {unit_id} TF {idx}: {item['diff']}"
        assert "e" in item and item["e"].strip(), f"Missing explanation in {unit_id} TF {idx}"

    # Validate FIB
    for idx, item in enumerate(formats["fib"]):
        assert "q" in item and item["q"].strip(), f"Empty question in {unit_id} FIB {idx}"
        assert isinstance(item["a"], list) and len(item["a"]) > 0, f"Invalid FIB answer in {unit_id} FIB {idx}: {item['a']}"
        assert "a_display" in item and item["a_display"].strip(), f"Missing a_display in {unit_id} FIB {idx}"
        assert item["topicId"] in valid_topics, f"Invalid topicId in {unit_id} FIB {idx}: {item['topicId']}"
        assert item["subSection"] in valid_subsections[unit_id], f"Invalid subSection in {unit_id} FIB {idx}: {item['subSection']}"
        assert item["diff"] in (1, 2, 3), f"Invalid diff in {unit_id} FIB {idx}: {item['diff']}"
        assert "e" in item and item["e"].strip(), f"Missing explanation in {unit_id} FIB {idx}"

print(f"\n==================================================")
print(f"ALL VALIDATION CHECKS PASSED!")
print(f"Grand Total Questions: {total_count} (270 MCQs, 135 T/F, 135 FIB)")
print(f"Ratio: exactly 2 : 1 : 1 across all 3 units.")
print(f"==================================================")

# Generate JavaScript string
js_content = "/* ============================================================\n"
js_content += "   data-quiz.JS  —  The Animal Genetics & Breeding Question Bank\n"
js_content += "   Strictly aligned with VCI MSVE 2016 Second Year Curriculum\n"
js_content += f"   Total Questions: {total_count} (180 per unit | 90 MCQ : 45 TF : 45 FIB)\n"
js_content += "   ============================================================ */\n\n"
js_content += "var quizBank = " + json.dumps(units_data, indent=2, ensure_ascii=False) + ";\n"

with open(QUIZ_OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated: {QUIZ_OUTPUT_PATH} ({os.path.getsize(QUIZ_OUTPUT_PATH):,} bytes)")

if os.path.exists(os.path.dirname(REPO_QUIZ_PATH)):
    with open(REPO_QUIZ_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Successfully mirrored: {REPO_QUIZ_PATH} ({os.path.getsize(REPO_QUIZ_PATH):,} bytes)")
