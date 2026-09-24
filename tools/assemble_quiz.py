# tools/assemble_quiz.py
# Validates and writes data/data-quiz.JS and repo/data/data-quiz.JS

import json
import os
import re
import shutil
from unit1_data import unit1_mcq, unit1_tf, unit1_fib
from unit2_data import unit2_mcq, unit2_tf, unit2_fib
from unit3_data import unit3_mcq, unit3_tf, unit3_fib
from exam_top50 import (exam_unit1_mcq, exam_unit1_tf, exam_unit1_fib,
                        exam_unit2_mcq, exam_unit2_tf, exam_unit2_fib,
                        exam_unit3_mcq, exam_unit3_tf, exam_unit3_fib)

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

base_data = {
    "unit-1": {"mcq": unit1_mcq, "tf": unit1_tf, "fib": unit1_fib},
    "unit-2": {"mcq": unit2_mcq, "tf": unit2_tf, "fib": unit2_fib},
    "unit-3": {"mcq": unit3_mcq, "tf": unit3_tf, "fib": unit3_fib}
}

# "Exam Top 50" — the 50 most examinable questions per unit (tools/exam_top50.py).
exam_data = {
    "unit-1": {"mcq": exam_unit1_mcq, "tf": exam_unit1_tf, "fib": exam_unit1_fib},
    "unit-2": {"mcq": exam_unit2_mcq, "tf": exam_unit2_tf, "fib": exam_unit2_fib},
    "unit-3": {"mcq": exam_unit3_mcq, "tf": exam_unit3_tf, "fib": exam_unit3_fib}
}

# The original bank must stay intact and in its original order: question keys
# are "<unit>:<format>:<index>", and spaced-repetition history and saved
# attempts are stored against them. The exam set is therefore APPENDED.
for unit_id in base_data:
    b = base_data[unit_id]
    assert (len(b["mcq"]), len(b["tf"]), len(b["fib"])) == (90, 45, 45), f"Original bank changed size in {unit_id}"
    x = exam_data[unit_id]
    assert len(x["mcq"]) + len(x["tf"]) + len(x["fib"]) == 50, f"Exam Top 50 for {unit_id} is not 50 questions"
    assert all(q.get("exam") is True for f in x for q in x[f]), f"Untagged exam question in {unit_id}"
    assert not any(q.get("exam") for f in b for q in b[f]), f"Original bank question tagged as exam in {unit_id}"

units_data = {
    u: {f: base_data[u][f] + exam_data[u][f] for f in ("mcq", "tf", "fib")}
    for u in base_data
}

# No question text may appear twice anywhere in the bank.
_seen = {}
for u in units_data:
    for f in units_data[u]:
        for i, q in enumerate(units_data[u][f]):
            k = " ".join(q["q"].lower().split())
            assert k not in _seen, f"Duplicate question text: {u}:{f}:{i} repeats {_seen[k]}"
            _seen[k] = f"{u}:{f}:{i}"

total_count = 0

for unit_id, formats in units_data.items():
    print(f"\n--- Validating {unit_id} ---")
    mcq_count = len(formats["mcq"])
    tf_count = len(formats["tf"])
    fib_count = len(formats["fib"])
    unit_total = mcq_count + tf_count + fib_count
    total_count += unit_total

    print(f"MCQs: {mcq_count} | TF: {tf_count} | FIB: {fib_count} | Total: {unit_total}")
    assert unit_total == 230, f"Expected 230 questions for {unit_id} (180 + 50 exam), got {unit_total}"

    # Validate MCQs
    for idx, item in enumerate(formats["mcq"]):
        assert "q" in item and item["q"].strip(), f"Empty question in {unit_id} MCQ {idx}"
        assert len(item["o"]) == 4, f"MCQ {idx} in {unit_id} must have 4 options, got {len(item['o'])}"
        assert isinstance(item["a"], int) and 0 <= item["a"] <= 3, f"Invalid answer index in {unit_id} MCQ {idx}: {item['a']}"
        assert item["topicId"] in valid_topics, f"Invalid topicId in {unit_id} MCQ {idx}: {item['topicId']}"
        assert item["subSection"] in valid_subsections[unit_id], f"Invalid subSection in {unit_id} MCQ {idx}: {item['subSection']}"
        assert item["diff"] in (1, 2, 3), f"Invalid diff in {unit_id} MCQ {idx}: {item['diff']}"
        assert "e" in item and item["e"].strip(), f"Missing explanation in {unit_id} MCQ {idx}"
        assert len(set(item["o"])) == 4, f"Duplicate option text in {unit_id} MCQ {idx}"

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
fmt_totals = {f: sum(len(units_data[u][f]) for u in units_data) for f in ("mcq", "tf", "fib")}
exam_total = sum(len(exam_data[u][f]) for u in exam_data for f in exam_data[u])
print(f"Grand Total Questions: {total_count} ({fmt_totals['mcq']} MCQs, {fmt_totals['tf']} T/F, {fmt_totals['fib']} FIB)")
print(f"Of which Exam Top 50: {exam_total} (50 per unit)")
print(f"==================================================")

# Generate JavaScript string
js_content = "/* ============================================================\n"
js_content += "   data-quiz.JS  —  The Animal Genetics & Breeding Question Bank\n"
js_content += "   Strictly aligned with VCI MSVE 2016 Second Year Curriculum\n"
js_content += f"   Total Questions: {total_count} (230 per unit = 180 core + 50 Exam Top 50)\n"
js_content += f"   Formats: {fmt_totals['mcq']} MCQ : {fmt_totals['tf']} TF : {fmt_totals['fib']} FIB\n"
js_content += "   Exam Top 50 questions carry exam: true and are APPENDED after the core\n"
js_content += "   bank, so existing question keys (unit:format:index) never move.\n"
js_content += "   GENERATED by tools/assemble_quiz.py - edit the tools/*.py sources, not this file.\n"
js_content += "   ============================================================ */\n\n"
js_content += "var quizBank = " + json.dumps(units_data, indent=2, ensure_ascii=False) + ";\n"

with open(QUIZ_OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated: {QUIZ_OUTPUT_PATH} ({os.path.getsize(QUIZ_OUTPUT_PATH):,} bytes)")

if os.path.exists(os.path.dirname(REPO_QUIZ_PATH)):
    with open(REPO_QUIZ_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Successfully mirrored: {REPO_QUIZ_PATH} ({os.path.getsize(REPO_QUIZ_PATH):,} bytes)")
