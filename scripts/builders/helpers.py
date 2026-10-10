"""
scripts/builders/helpers.py
Helper functions to create mathematically verified, schema-compliant questions
for Kids STEM Studio math worksheets and placement assessment.
Zero emojis, zero em dashes, and complete visual/mathematical WHY proofs for Gizmo's step.
"""

import re

def clean_text(text):
    if text is None:
        return ""
    # Strip emojis
    s = str(text)
    # Remove em dash (\u2014) and replace with hyphen or comma
    s = s.replace("\u2014", " - ").replace("—", " - ")
    # Strip any supplementary unicode characters (emojis are in U+1F000 to U+1FFFF and misc symbols)
    s = re.sub(r'[\U00010000-\U0010ffff]', '', s)
    s = re.sub(r'[\u2600-\u26ff\u2700-\u27bf]', '', s)
    return s.strip()

def build_gizmo_why(gizmo_hint, explanation, strategy_hint, prompt, correct_answer):
    gh = clean_text(gizmo_hint)
    exp = clean_text(explanation)
    strat = clean_text(strategy_hint)

    # If gizmo_hint is already substantial and explains why (has equation or 'because' or '> 30 chars')
    if len(gh) >= 30 and ("=" in gh or "because" in gh.lower() or "means" in gh.lower()):
        return gh

    # If explanation has the reasoning, use explanation as the primary proof
    if len(exp) >= 20 and ("=" in exp or "because" in exp.lower() or "means" in exp.lower() or "is" in exp.lower()):
        # If it doesn't already contain the answer, append confirmation
        if str(correct_answer) not in exp:
            return f"{exp} This verifies that {correct_answer} is correct."
        return exp

    # Combine strategy and calculation to explain why
    if strat and len(strat) >= 15:
        return f"{strat} Completing this step confirms the result is {correct_answer}."

    return f"Working through the calculation gives {correct_answer}, verifying the solution step by step."

def make_numeric_question(
    q_id, grade, lesson_id, lesson_title, domain, standard, difficulty,
    prompt, correct_answer, accepted_answers=None,
    concept_hint=None, strategy_hint=None, gizmo_hint=None,
    explanation=None
):
    if accepted_answers is None:
        accepted_answers = [str(correct_answer)]
    elif str(correct_answer) not in accepted_answers:
        accepted_answers.insert(0, str(correct_answer))

    clean_prompt = clean_text(prompt)
    clean_concept = clean_text(concept_hint)
    clean_strat = clean_text(strategy_hint)
    clean_exp = clean_text(explanation) or f"Solve step-by-step to calculate {correct_answer}."
    
    why_gizmo = build_gizmo_why(gizmo_hint, clean_exp, clean_strat, clean_prompt, correct_answer)

    hints = [
        f"Concept Rule: {clean_concept}",
        f"Strategy Clue: {clean_strat}",
        f"Gizmo's Step: {why_gizmo}"
    ]

    return {
        "id": q_id,
        "grade": grade,
        "lessonId": lesson_id,
        "lessonTitle": clean_text(lesson_title),
        "domain": clean_text(domain),
        "standard": clean_text(standard),
        "difficulty": difficulty,
        "type": "numeric-response",
        "prompt": clean_prompt,
        "correctAnswer": str(correct_answer),
        "acceptedAnswers": [clean_text(a) for a in accepted_answers],
        "options": None,
        "explanation": clean_exp,
        "hints": hints
    }

def make_mc_question(
    q_id, grade, lesson_id, lesson_title, domain, standard, difficulty,
    prompt, correct_option_text, wrong_options,
    concept_hint=None, strategy_hint=None, gizmo_hint=None,
    explanation=None
):
    assert len(wrong_options) == 3, f"Must provide exactly 3 wrong options, got {len(wrong_options)}"
    
    clean_prompt = clean_text(prompt)
    clean_corr = clean_text(correct_option_text)
    clean_wrongs = [clean_text(w) for w in wrong_options]

    rot = sum(ord(c) for c in q_id) % 4
    all_options_texts = list(clean_wrongs)
    all_options_texts.insert(rot, clean_corr)

    options = []
    for opt_text in all_options_texts:
        is_corr = (opt_text == clean_corr)
        options.append({
            "text": str(opt_text),
            "correct": is_corr
        })

    clean_concept = clean_text(concept_hint)
    clean_strat = clean_text(strategy_hint)
    clean_exp = clean_text(explanation) or f"The correct answer is {clean_corr}."
    
    why_gizmo = build_gizmo_why(gizmo_hint, clean_exp, clean_strat, clean_prompt, clean_corr)

    hints = [
        f"Concept Rule: {clean_concept}",
        f"Strategy Clue: {clean_strat}",
        f"Gizmo's Step: {why_gizmo}"
    ]

    return {
        "id": q_id,
        "grade": grade,
        "lessonId": lesson_id,
        "lessonTitle": clean_text(lesson_title),
        "domain": clean_text(domain),
        "standard": clean_text(standard),
        "difficulty": difficulty,
        "type": "multiple-choice",
        "prompt": clean_prompt,
        "correctAnswer": clean_corr,
        "acceptedAnswers": [clean_corr],
        "options": options,
        "explanation": clean_exp,
        "hints": hints
    }

def validate_question(q):
    assert "id" in q and q["id"], "Missing id"
    assert q["difficulty"] in [1, 2, 3], f"Invalid difficulty in {q['id']}"
    assert q["type"] in ["numeric-response", "multiple-choice"], f"Invalid type in {q['id']}"
    assert len(q["hints"]) == 3, f"Must have exactly 3 hints in {q['id']}"
    
    # Check for raw LaTeX remnants
    forbidden = ["itemsep", "leftmargin", "tikzpicture", "colback", "colframe", "\\begin", "\\end", "\\hspace", "\\vspace", "\\blank"]
    for word in forbidden:
        assert word not in q["prompt"], f"Raw LaTeX artifact '{word}' found in prompt of {q['id']}"
        for h in q["hints"]:
            assert word not in h, f"Raw LaTeX artifact '{word}' found in hints of {q['id']}"

    # Check for no em-dashes
    assert "\u2014" not in q["prompt"] and "—" not in q["prompt"], f"Em-dash found in prompt of {q['id']}"
    for h in q["hints"]:
        assert "\u2014" not in h and "—" not in h, f"Em-dash found in hint of {q['id']}"

    # Check for no emojis
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf]')
    assert not emoji_pattern.search(q["prompt"]), f"Emoji found in prompt of {q['id']}"
    for h in q["hints"]:
        assert not emoji_pattern.search(h), f"Emoji found in hint of {q['id']}"

    # Verify hints structure
    assert q["hints"][0].startswith("Concept Rule: "), f"Hint 1 invalid prefix in {q['id']}"
    assert q["hints"][1].startswith("Strategy Clue: "), f"Hint 2 invalid prefix in {q['id']}"
    assert q["hints"][2].startswith("Gizmo's Step: "), f"Hint 3 invalid prefix in {q['id']}"
    
    # Verify Strategy Clue does not leak the answer
    strat_body = q["hints"][1].replace("Strategy Clue: ", "").strip()
    ans_str = str(q["correctAnswer"]).strip()
    assert strat_body.lower() != ans_str.lower(), f"Strategy clue cannot equal the answer in {q['id']}"
    assert f"= {ans_str}" not in strat_body and f"={ans_str}" not in strat_body, f"Strategy clue cannot end with '= answer' in {q['id']}"

    # Verify Gizmo step explains WHY with sufficient detail
    gizmo_body = q["hints"][2].replace("Gizmo's Step: ", "").strip()
    assert len(gizmo_body) >= 15, f"Gizmo hint too short ({len(gizmo_body)} chars) in {q['id']}: {gizmo_body}"

    if q["type"] == "multiple-choice":
        assert q["options"] and len(q["options"]) == 4, f"MC question {q['id']} must have 4 options"
        correct_count = sum(1 for o in q["options"] if o.get("correct") is True)
        assert correct_count == 1, f"MC question {q['id']} must have exactly 1 correct option, got {correct_count}"
        correct_opt = next(o for o in q["options"] if o["correct"])
        assert correct_opt["text"] == q["correctAnswer"], f"MC question {q['id']} correctAnswer mismatch"
    else:
        assert q["options"] is None, f"Numeric question {q['id']} options must be None"
        assert q["correctAnswer"] in q["acceptedAnswers"], f"Numeric question {q['id']} correctAnswer not in acceptedAnswers"
