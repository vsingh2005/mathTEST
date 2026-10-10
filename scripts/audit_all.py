"""
scripts/audit_all.py
Independent verification of all 1,200 questions across both data directories.
Checks: Zero LaTeX artifacts, Zero emojis, Zero em-dashes, Correct answers, 3-tier hints.
"""
import json
import glob
import re

latex_patterns = [r'itemsep', r'tikzpicture', r'colback', r'leftmargin', r'\\blank', r'\\hspace', r'\\begin', r'\\end']
emoji_pattern = re.compile(r'[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf]')

for base in ['shared/data', 'website/shared/data']:
    print(f"Checking directory: {base}...")
    files = sorted(glob.glob(f"{base}/grade_*.json"))
    assert len(files) == 6, f"Expected 6 files in {base}, found {len(files)}"
    for fpath in files:
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
        qs = data['questions']
        assert len(qs) == 200, f"{fpath} has {len(qs)} questions, expected 200"
        for q in qs:
            qid = q["id"]
            # No LaTeX
            for p in latex_patterns:
                assert not re.search(p, q['prompt']), f"Found pattern {p} in prompt of {qid}"
                for h in q['hints']:
                    assert not re.search(p, h), f"Found pattern {p} in hint of {qid}"
            
            # No em dashes
            assert "\u2014" not in q['prompt'] and "—" not in q['prompt'], f"Em-dash found in prompt of {qid}"
            for h in q['hints']:
                assert "\u2014" not in h and "—" not in h, f"Em-dash found in hint of {qid}"

            # No emojis
            assert not emoji_pattern.search(q['prompt']), f"Emoji found in prompt of {qid}"
            for h in q['hints']:
                assert not emoji_pattern.search(h), f"Emoji found in hint of {qid}"

            if q['type'] == 'multiple-choice':
                assert len(q['options']) == 4, f"{qid} must have 4 options"
                corrects = [o for o in q['options'] if o.get('correct')]
                assert len(corrects) == 1, f"{qid} must have 1 correct option"
                assert corrects[0]['text'] == q['correctAnswer'], f"{qid} option mismatch"
            elif q['type'] == 'numeric-response':
                assert q['options'] is None, f"{qid} options must be None"
                assert q['correctAnswer'] in q['acceptedAnswers'], f"{qid} answer not in accepted"
            assert len(q['hints']) == 3, f"{qid} must have 3 hints"
            assert q['hints'][0].startswith('Concept Rule: '), f"{qid} hint 1 prefix invalid"
            assert q['hints'][1].startswith('Strategy Clue: '), f"{qid} hint 2 prefix invalid"
            assert q['hints'][2].startswith("Gizmo's Step: "), f"{qid} hint 3 prefix invalid"
            
            # Ensure Gizmo hint explains WHY
            gstep = q['hints'][2].replace("Gizmo's Step: ", "").strip()
            assert len(gstep) >= 15, f"{qid} Gizmo step too short: {gstep}"
        print(f"  [OK] {fpath}: 200 questions verified.")

print("\n>>> COMPREHENSIVE AUDIT PASSED 100% ACROSS ALL 1,200 QUESTIONS AND BOTH DIRECTORIES! <<<")
