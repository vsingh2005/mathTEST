"""
scripts/refactor_hints.py
Systematically refactors hints across all 1,200 questions (Grades 3-8):
- Hint 1 (Concept Rule): Pure conceptual definition, formula, or property. No final answer given.
- Hint 2 (Strategy Clue): Actionable setup and problem-solving method. NEVER gives away the answer.
- Hint 3 (Gizmo's Step): Mathematical and visual WHY proof showing full calculation and verifying answer.
- Zero emojis, zero em dashes.
"""

import json
import os
import re

def clean_text(text):
    if not text:
        return ""
    s = str(text)
    s = s.replace("\u2014", " - ").replace("—", " - ")
    s = re.sub(r'[\U00010000-\U0010ffff]', '', s)
    s = re.sub(r'[\u2600-\u26ff\u2700-\u27bf]', '', s)
    return s.strip()

def has_ans_leak(text, ans_str):
    if not text or not ans_str:
        return False
    t_clean = clean_text(text).lower().strip()
    a_clean = clean_text(ans_str).lower().strip()

    # Exact string match
    if a_clean in t_clean:
        return True

    # Check if text contains '='
    if "=" in t_clean:
        return True

    # Check phrases indicating final answer
    if "denominator is" in t_clean or "numerator is" in t_clean or "answer is" in t_clean:
        return True

    # Number match without currency/symbols (e.g. $19 -> 19)
    num_match = re.search(r'[\d\.]+', a_clean)
    if num_match:
        val = num_match.group(0)
        # Check if number appears after '=' or 'is ' or 'gives ' or as standalone number
        if re.search(r'=\s*' + re.escape(val) + r'(?!\d)', t_clean):
            return True
        if re.search(r'\bis\s*' + re.escape(val) + r'(?!\d)', t_clean):
            return True
        if re.search(r'(?<![\w\.\/])' + re.escape(val) + r'(?![\w\.\/])', t_clean):
            return True

    return False

def build_pure_concept(concept_raw, ans_str, prompt):
    c = clean_text(concept_raw).strip()
    if c.startswith("Concept Rule:"):
        c = c.replace("Concept Rule:", "").strip()

    # If concept contains the exact answer in an equation ending, trim it
    if f"= {ans_str}" in c:
        parts = c.split(f"= {ans_str}")
        if len(parts[0].strip()) >= 20:
            c = parts[0].strip().rstrip('.,;:') + "."

    # If c became too short or is just the answer
    if len(c) < 15 or c.strip('.').lower() == ans_str.lower():
        p_low = prompt.lower()
        if "ratio" in p_low:
            c = "A ratio compares two quantities in the specific order requested: first quantity to second quantity."
        elif "unit rate" in p_low or "unit price" in p_low:
            c = "Unit rate is the ratio of two measurements where the second measurement is one unit (Rate = Amount ÷ Units)."
        elif "area" in p_low:
            c = "Area measures the total two-dimensional space inside a boundary (Area = Base × Height)."
        elif "perimeter" in p_low:
            c = "Perimeter is the total continuous distance around the outside edge of a closed geometric figure."
        elif "volume" in p_low:
            c = "Volume measures the total three-dimensional capacity of a solid figure in cubic units."
        elif "pythagor" in p_low or "hypotenuse" in p_low:
            c = "The Pythagorean theorem states that in any right triangle, a² + b² = c², where c is the hypotenuse."
        elif "(" in prompt and ")" in prompt:
            c = "The order of operations (PEMDAS) establishes the sequence for evaluating expressions: parentheses first, then exponents, multiplication and division, then addition and subtraction."
        else:
            c = "Apply the foundational mathematical property to set up and solve the problem systematically."

    if not c.endswith("."):
        c += "."
    return c

def build_pure_strategy(prompt, ans_str, strat_raw, concept_raw, q_domain, q_standard):
    p_low = prompt.lower()
    s_clean = clean_text(strat_raw).strip()
    if s_clean.startswith("Strategy Clue:"):
        s_clean = s_clean.replace("Strategy Clue:", "").strip()

    # If s_clean already does NOT leak the answer and is descriptive, use it
    if not has_ans_leak(s_clean, ans_str) and len(s_clean) >= 20 and not s_clean.rstrip('.').endswith('='):
        if not s_clean.endswith('.'):
            s_clean += '.'
        return s_clean

    # Otherwise generate a pure procedural clue with zero answer
    # 1. Order of operations
    if "(" in prompt and ")" in prompt and any(op in prompt for op in ["+", "-", "*", "×", "÷", "/"]):
        return "Follow PEMDAS: evaluate inside the parentheses first, then complete the outside operations."
    if "order of operations" in p_low or ("evaluate" in p_low and any(w in p_low for w in ["expression", "numerical"])):
        return "Apply the order of operations: simplify parentheses first, then multiplication and division, then addition and subtraction."

    # 2. Linear Equations & Isolating Variable
    if "solve for" in p_low or re.search(r'\b[a-z]\s*[\+\-\*\/=]', prompt) or "what value of" in p_low:
        if "=" in prompt:
            return "Use inverse operations to isolate the variable on one side of the equation."
        return "Substitute the given value into the expression and compute the result step-by-step."

    # 3. Recipes, Scaling, & Proportions
    if any(w in p_low for w in ["recipe", "cups of", "for every", "how many cups", "scale factor"]):
        return "Find the scale factor between the known amounts, then multiply the other ingredient by that same factor."

    # 4. Ratios
    if "ratio" in p_low:
        if any(w in p_low for w in ["simplest", "simplified", "simplify"]):
            return "Write the ratio of the two quantities, then divide both numbers by their greatest common factor."
        if "equivalent" in p_low and "not" not in p_low:
            return "Multiply or divide both terms of the ratio by the same non-zero number to find an equivalent ratio."
        if "not equivalent" in p_low or "which ratio is not" in p_low:
            return "Simplify the original ratio to lowest terms, then test which choice does not simplify to the same fraction."
        return "Identify the count of each item and write them in the exact order requested by the prompt."

    # 5. Unit Rate & Speed
    if any(w in p_low for w in ["unit rate", "unit price", "per hour", "per pound", "per minute", "speed", "mph"]):
        return "Divide the total amount (or distance or cost) by the total units (or time) to find the unit rate."

    # 6. Pythagorean Theorem
    if "pythagor" in p_low or "hypotenuse" in p_low or ("right triangle" in p_low and any(w in p_low for w in ["leg", "side length"])):
        if "hypotenuse" in p_low:
            return "Use a² + b² = c²: calculate the sum of the squares of the legs, then take the square root."
        return "Use a² + b² = c²: subtract the square of the known leg from the square of the hypotenuse, then take the square root."

    # 7. Geometry - Area, Perimeter, Volume, Surface Area
    if "area" in p_low:
        if "triangle" in p_low:
            return "Use the triangle area formula: multiply base by height, then divide by 2."
        if "circle" in p_low:
            return "Use the circle area formula: multiply pi by the radius squared (A = πr²)."
        if "trapezoid" in p_low:
            return "Add the two parallel bases, multiply by the height, and divide by 2."
        return "Use the area formula: multiply the length (base) by the width (height)."

    if "perimeter" in p_low:
        if "circumference" in p_low or "circle" in p_low:
            return "Use C = 2πr or C = πd: multiply pi by the diameter."
        return "Add the lengths of all outer boundary sides together to find the perimeter."

    if "volume" in p_low:
        if "cylinder" in p_low:
            return "Multiply the area of the circular base (πr²) by the height of the cylinder."
        if "cone" in p_low:
            return "Calculate one-third of the base area times height: V = (1/3)πr²h."
        if "sphere" in p_low:
            return "Use the sphere volume formula: V = (4/3)πr³."
        return "Multiply length, width, and height together to calculate the volume."

    # 8. Transformations & Coordinates
    if "translat" in p_low:
        return "Apply the horizontal change to the x-coordinate and the vertical change to the y-coordinate."
    if "reflect" in p_low:
        return "Identify the line of reflection to determine which coordinate stays the same and which coordinate changes sign."
    if "rotat" in p_low:
        return "Apply the coordinate rule corresponding to the angle and direction of rotation about the origin."
    if "dilation" in p_low or "dilate" in p_low:
        return "Multiply both the x-coordinate and the y-coordinate by the given scale factor."

    # 9. Fractions Operations & Identifying Parts
    if any(w in p_low for w in ["fraction", "numerator", "denominator", "parts"]) or "/" in prompt:
        if "numerator" in p_low and "denominator" not in p_low:
            return "Identify the top number in the fraction which counts how many equal parts are selected."
        if "denominator" in p_low and "numerator" not in p_low:
            return "Identify the bottom number in the fraction which indicates the total number of equal parts in one whole."
        if "add" in p_low or "+" in prompt or "sum" in p_low:
            return "Rewrite the fractions with a common denominator if needed, then add the numerators."
        if "subtract" in p_low or "-" in prompt or "difference" in p_low:
            return "Rewrite the fractions with a common denominator if needed, then subtract the numerators."
        if "multiply" in p_low or "times" in p_low or "product" in p_low:
            return "Multiply the numerators together and the denominators together, then simplify to lowest terms."
        if "divide" in p_low or "divided by" in p_low:
            return "Multiply the first fraction by the reciprocal (flipped version) of the second fraction."
        return "Set up the fraction operation and simplify the resulting fraction to lowest terms."

    # 10. Decimals
    if "." in prompt and re.search(r'\d+\.\d+', prompt):
        if "multiply" in p_low or "times" in p_low:
            return "Multiply as with whole numbers, then count the total decimal places in both factors to place the decimal point."
        if "divide" in p_low:
            return "Shift decimal points if the divisor has decimals, then divide using standard long division."
        return "Line up the decimal points vertically before adding or subtracting place values."

    # 11. Statistics (Mean, Median, Mode, Range, IQR)
    if "mean" in p_low or "average" in p_low:
        return "Add all data values together, then divide the total sum by the count of numbers."
    if "median" in p_low:
        return "Arrange the numbers in ascending order from least to greatest and locate the middle value."
    if "range" in p_low:
        return "Subtract the minimum data value from the maximum data value."
    if "mode" in p_low:
        return "Identify the number or data value that appears most frequently in the set."

    # 12. Percentages & Money
    if "%" in prompt or "percent" in p_low:
        if "discount" in p_low or "sale" in p_low:
            return "Convert the percent to a decimal, multiply by the original price, and subtract the discount."
        if "tax" in p_low or "tip" in p_low:
            return "Convert the percent to a decimal, multiply by the bill amount, and add the result to the total."
        return "Convert the percentage to a decimal or fraction over one hundred, then multiply by the total amount."

    if "$" in prompt or "cost" in p_low or "spend" in p_low or "change" in p_low:
        return "Calculate the total cost of all items purchased, then subtract from the amount paid to find the remaining change."

    # 13. Exponents & Scientific Notation
    if "scientific notation" in p_low:
        return "Write the number as a factor between 1 and 10 multiplied by a power of 10."
    if "exponent" in p_low or "power" in p_low:
        return "Multiply the base by itself repeatedly for the number of times indicated by the exponent."

    # 14. Basic Division / Sharing Word Problems
    if any(w in p_low for w in ["divided by", " ÷ ", "share", "split", "each", "pack", "per student", "into groups"]):
        return "Divide the total dividend by the divisor using standard division."

    # 15. Basic Multiplication / Repeated Addition / Associative Property
    if any(w in p_low for w in ["associative", "grouping"]):
        return "Use the associative property: regroup the factors without changing their product."
    if any(w in p_low for w in ["times", " × ", "in total", "altogether", "baskets", "rows"]):
        return "Multiply the number of groups by the number of items in each group."

    # 16. Multiple Choice conceptual search
    if any(w in p_low for w in ["which statement", "which equation", "which of the following"]):
        return "Test each option against the mathematical rule to identify the statement that holds true."

    # Default procedural guidance
    return "Identify the quantities given in the problem, set up the required mathematical operation, and compute the result step-by-step."

def build_pure_gizmo(gizmo_raw, exp_raw, strat_raw, ans_str, prompt):
    g = clean_text(gizmo_raw).strip()
    if g.startswith("Gizmo's Step:"):
        g = g.replace("Gizmo's Step:", "").strip()

    exp = clean_text(exp_raw).strip()
    strat = clean_text(strat_raw).strip()
    if strat.startswith("Strategy Clue:"):
        strat = strat.replace("Strategy Clue:", "").strip()

    # If g is too short or lacks reasoning, enhance from exp or strat
    if len(g) < 20 or ans_str not in g:
        if len(exp) >= 20 and ("=" in exp or "because" in exp.lower() or "means" in exp.lower()):
            g = exp
        elif "=" in strat and len(strat) >= 15:
            g = strat
    
    # Ensure answer is verified with why reasoning
    if ans_str not in g:
        g = f"{g.rstrip('.')} Completing this calculation confirms that {ans_str} is the correct solution."
    elif not ("confirm" in g.lower() or "therefore" in g.lower() or "gives" in g.lower() or "=" in g):
        g = f"{g.rstrip('.')} Therefore, {ans_str} is the mathematically correct answer."

    if not g.endswith("."):
        g += "."
    return g

def refactor_all_grades():
    total_q = 0
    total_strat_fixed = 0
    for g in range(3, 9):
        path = f"shared/data/grade_{g}.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for q in data["questions"]:
            total_q += 1
            ans_str = str(q["correctAnswer"]).strip()
            prompt = q["prompt"]
            c_raw = q["hints"][0]
            s_raw = q["hints"][1]
            g_raw = q["hints"][2]
            exp = q.get("explanation", "")

            # 1. Concept Rule
            pure_concept = build_pure_concept(c_raw, ans_str, prompt)
            # 2. Strategy Clue
            pure_strat = build_pure_strategy(prompt, ans_str, s_raw, c_raw, q.get("domain", ""), q.get("standard", ""))
            
            # Strict safety fallback: If pure_strat somehow still contains ans_str, replace with generic procedural
            if has_ans_leak(pure_strat, ans_str):
                total_strat_fixed += 1
                pure_strat = "Identify the quantities given in the problem, set up the required mathematical operation, and compute the result step-by-step."

            # 3. Gizmo's Step
            pure_gizmo = build_pure_gizmo(g_raw, exp, s_raw, ans_str, prompt)

            q["hints"] = [
                f"Concept Rule: {pure_concept}",
                f"Strategy Clue: {pure_strat}",
                f"Gizmo's Step: {pure_gizmo}"
            ]

        # Save to shared/data/
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        # Save to website/shared/data/
        web_path = f"website/shared/data/grade_{g}.json"
        with open(web_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"[OK] Grade {g} refactored successfully ({len(data['questions'])} questions).")

    print(f"Total processed: {total_q}. Strategy safety triggers: {total_strat_fixed}")

if __name__ == "__main__":
    refactor_all_grades()
