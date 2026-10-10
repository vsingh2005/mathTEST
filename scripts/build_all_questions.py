"""
scripts/build_all_questions.py
Master compiler and validator for Kids STEM Studio Math Questions.
Compiles Grades 3-8 into shared/data/ and website/shared/data/
100% mathematically verified, zero raw LaTeX/TikZ artifacts, 3-tier hints.
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.builders.helpers import validate_question
from scripts.builders.grade_3 import build_grade_3_questions
from scripts.builders.grade_4 import build_grade_4_questions
from scripts.builders.grade_5 import build_grade_5_questions
from scripts.builders.grade_6 import build_grade_6_questions
from scripts.builders.grade_7 import build_grade_7_questions
from scripts.builders.grade_8 import build_grade_8_questions

BUILDERS = {
    3: build_grade_3_questions,
    4: build_grade_4_questions,
    5: build_grade_5_questions,
    6: build_grade_6_questions,
    7: build_grade_7_questions,
    8: build_grade_8_questions
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARED_DATA_DIR = os.path.join(BASE_DIR, "shared", "data")
WEBSITE_DATA_DIR = os.path.join(BASE_DIR, "website", "shared", "data")

def main():
    print("=" * 60)
    print("Starting master compilation of all 150 lessons & 1,200 questions...")
    print("=" * 60)

    total_questions_count = 0
    type_counts = {"numeric-response": 0, "multiple-choice": 0}
    difficulty_counts = {1: 0, 2: 0, 3: 0}

    for grade in range(3, 9):
        builder_fn = BUILDERS[grade]
        questions = builder_fn()

        print(f"\n[Grade {grade}] Building questions...")
        assert len(questions) == 200, f"Grade {grade} must have 200 questions, got {len(questions)}"

        # Validate every question
        for q in questions:
            validate_question(q)
            type_counts[q["type"]] += 1
            difficulty_counts[q["difficulty"]] += 1

        total_questions_count += len(questions)

        # Load lessons metadata from existing shared/data/grade_{grade}.json
        grade_file_shared = os.path.join(SHARED_DATA_DIR, f"grade_{grade}.json")
        grade_file_website = os.path.join(WEBSITE_DATA_DIR, f"grade_{grade}.json")

        with open(grade_file_shared, "r", encoding="utf-8") as f:
            existing = json.load(f)

        lessons = existing.get("lessons", [])
        assert len(lessons) == 25, f"Grade {grade} must have 25 lessons, got {len(lessons)}"
        for l in lessons:
            l["questionCount"] = 8

        payload = {
            "grade": grade,
            "lessonCount": len(lessons),
            "questionCount": len(questions),
            "lessons": lessons,
            "questions": questions
        }

        # Write to shared/data/
        with open(grade_file_shared, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        print(f"  -> Wrote {grade_file_shared}")

        # Write to website/shared/data/
        os.makedirs(os.path.dirname(grade_file_website), exist_ok=True)
        with open(grade_file_website, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        print(f"  -> Wrote {grade_file_website}")

    # Update curriculum.json in both locations
    print("\nUpdating curriculum.json...")
    curriculum_shared = os.path.join(SHARED_DATA_DIR, "curriculum.json")
    curriculum_website = os.path.join(WEBSITE_DATA_DIR, "curriculum.json")

    with open(curriculum_shared, "r", encoding="utf-8") as f:
        curr_data = json.load(f)

    for l in curr_data.get("lessons", []):
        l["questionCount"] = 8

    with open(curriculum_shared, "w", encoding="utf-8") as f:
        json.dump(curr_data, f, indent=2, ensure_ascii=False)
    print(f"  -> Updated {curriculum_shared}")

    with open(curriculum_website, "w", encoding="utf-8") as f:
        json.dump(curr_data, f, indent=2, ensure_ascii=False)
    print(f"  -> Updated {curriculum_website}")

    print("\n" + "=" * 60)
    print("SUCCESSFULLY COMPILED ALL QUESTIONS!")
    print(f"Total Questions: {total_questions_count} / 1200 across 150 lessons")
    print(f"Question Types: Numeric: {type_counts['numeric-response']}, Multiple-Choice: {type_counts['multiple-choice']}")
    print(f"Difficulty Levels: Level 1: {difficulty_counts[1]}, Level 2: {difficulty_counts[2]}, Level 3: {difficulty_counts[3]}")
    print("All questions validated with zero LaTeX/TikZ remnants, exact mathematical answers, and 3-tier hints!")
    print("=" * 60)

if __name__ == "__main__":
    main()
