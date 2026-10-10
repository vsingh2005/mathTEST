"""
scripts/generators/generate_grade_5.py
Script to generate the complete Grade 5 curriculum questions builder (Lessons 1-25).
"""

code = '''"""
scripts/builders/grade_5.py
High-fidelity mathematical question builder for Grade 5 (Lessons 1-25).
100% verified math answers, child-friendly prompts, and progressive 3-tier hints.
"""

from scripts.builders.helpers import make_numeric_question, make_mc_question

def build_grade_5_questions():
    questions = []
    G = 5

    # =========================================================================
    # LESSON 1: Writing & Evaluating Expressions (5.OA.A.1 / 5.OA.A.2)
    # =========================================================================
    LID = "G5_L01"
    LT = "Writing & Evaluating Expressions"
    DOM = "Operations & Algebraic Thinking"
    STD = "5.OA.A.1 / 5.OA.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Evaluate the numerical expression: (4 + 6) × 3.",
        30, ["30"],
        "Order of operations (PEMDAS): Evaluate inside parentheses first, then multiply.",
        "4 + 6 = 10. Then 10 × 3 = 30.",
        "30.",
        "(4 + 6) × 3 = 10 × 3 = 30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which numerical expression represents: 'Add 8 and 7, then multiply by 2'?",
        "(8 + 7) × 2",
        ["8 + 7 × 2", "8 × 2 + 7", "(8 × 7) + 2"],
        "Use parentheses to group the addition so it occurs before the multiplication.",
        "(8 + 7) × 2.",
        "(8 + 7) × 2.",
        "(8 + 7) × 2 represents adding first, then multiplying by 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Evaluate: 24 - (3 × 4 + 2).",
        10, ["10"],
        "Evaluate inside parentheses: multiply 3 × 4 = 12, then add 2 = 14. Finally, 24 - 14.",
        "24 - 14 = 10.",
        "10.",
        "24 - (12 + 2) = 24 - 14 = 10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Evaluate: [2 × (5 + 3)] - 6.",
        "10",
        ["12", "14", "8"],
        "Work from innermost parentheses outward: 5 + 3 = 8; 2 × 8 = 16; 16 - 6 = 10.",
        "10.",
        "10.",
        "[2 × 8] - 6 = 16 - 6 = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Evaluate: 50 - 4 × (6 + 2).",
        18, ["18"],
        "Parentheses first: 6 + 2 = 8. Multiply: 4 × 8 = 32. Subtract: 50 - 32.",
        "50 - 32 = 18.",
        "18.",
        "50 - 4 × 8 = 50 - 32 = 18."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate: 3 × [15 - (2 + 4)].",
        27, ["27"],
        "Innermost: 2 + 4 = 6. Brackets: 15 - 6 = 9. Multiply: 3 × 9.",
        "3 × 9 = 27.",
        "27.",
        "3 × [15 - 6] = 3 × 9 = 27."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Compare the value of 3 × (2,450 + 890) to the value of (2,450 + 890) without calculating.",
        "3 × (2,450 + 890) is 3 times as large",
        ["They have the same value", "(2,450 + 890) is 3 times as large", "3 × (2,450 + 890) is 3 more"],
        "Multiplying an expression by 3 produces a result 3 times as large.",
        "3 times as large.",
        "3 times as large.",
        "Multiplying by 3 makes the expression 3 times as large."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate: (18 ÷ 3) + (4 × 5) - 6.",
        20, ["20"],
        "18 ÷ 3 = 6; 4 × 5 = 20. Then: 6 + 20 - 6 = 20.",
        "20.",
        "20.",
        "6 + 20 - 6 = 20."
    ))

    # =========================================================================
    # LESSON 2: Generating Patterns & Graphing (5.OA.B.3)
    # =========================================================================
    LID = "G5_L02"
    LT = "Generating Patterns & Graphing"
    DOM = "Operations & Algebraic Thinking"
    STD = "5.OA.B.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Pattern A starts at 0 and adds 2: (0, 2, 4, 6...). Pattern B starts at 0 and adds 6: (0, 6, 12, 18...). What is the relationship between corresponding terms of B and A?",
        "Each term in Pattern B is 3 times the corresponding term in Pattern A",
        ["Each term in Pattern B is 4 more than Pattern A", "Each term in Pattern B is 2 times Pattern A", "They are equal"],
        "Compare terms: 6 = 3 × 2; 12 = 3 × 4; 18 = 3 × 6. The ratio is 6/2 = 3.",
        "Pattern B is 3 times Pattern A.",
        "Each term in B is 3 times the corresponding term in A.",
        "Since 6 = 3 × 2, each term in B is 3 times the term in A."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In Pattern A (starts at 0, adds 3), what is the 4th term? (0, 3, 6, ___)",
        9, ["9"],
        "0, 3, 6, 9. Add 3 to 6.",
        "9.",
        "9.",
        "The 4th term is 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Given x-values: (0, 1, 2, 3) and y-values: (0, 4, 8, 12). Which ordered pair represents the 3rd point?",
        "(2, 8)",
        ["(3, 12)", "(1, 4)", "(8, 2)"],
        "The 3rd x is 2 and 3rd y is 8, so the ordered pair is (2, 8).",
        "(2, 8).",
        "(2, 8).",
        "The 3rd point is (2, 8)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "If x starts at 0 and adds 5, what is the y-value when x = 15 if y is always twice x (y = 2x)?",
        30, ["30"],
        "Multiply 15 by 2: y = 2 × 15 = 30.",
        "30.",
        "30.",
        "y = 2 × 15 = 30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "When ordered pairs (0,0), (1,3), (2,6), (3,9) are plotted on a coordinate grid, what shape do the points form?",
        "A straight line passing through the origin",
        ["A curve", "A circle", "A triangle"],
        "Because the rate of change is constant (slope 3), the plotted points form a straight line.",
        "A straight line.",
        "A straight line passing through the origin.",
        "The points lie on a straight line y = 3x."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Pattern X rule: Add 4 (starts at 0). Pattern Y rule: Add 8 (starts at 0). When Pattern X is 20, what is Pattern Y?",
        40, ["40"],
        "Pattern Y is always twice Pattern X (8/4 = 2). 20 × 2 = 40.",
        "40.",
        "40.",
        "Y is double X: 20 × 2 = 40."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which point lies on the line connecting (0, 0), (2, 4), and (4, 8)?",
        "(5, 10)",
        ["(5, 9)", "(5, 12)", "(5, 7)"],
        "The rule is y = 2x. For x = 5, y = 2 × 5 = 10.",
        "(5, 10).",
        "(5, 10).",
        "y = 2x, so (5, 10) is on the line."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If a point has coordinates (6, 18), what is the ratio of y to x (y ÷ x)?",
        3, ["3"],
        "Divide 18 by 6: 18 ÷ 6 = 3.",
        "3.",
        "3.",
        "18 ÷ 6 = 3."
    ))

    # =========================================================================
    # LESSON 3: Understanding Powers of 10 (5.NBT.A.1 / 5.NBT.A.2)
    # =========================================================================
    LID = "G5_L03"
    LT = "Understanding Powers of 10"
    DOM = "Decimal Place Value & Computation"
    STD = "5.NBT.A.1 / 5.NBT.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is 10 to the 3rd power (10³) in standard form?",
        1000, ["1000", "1,000"],
        "10³ = 10 × 10 × 10 = 1,000. (The exponent 3 indicates 3 zeros).",
        "1,000.",
        "1,000.",
        "10³ = 1,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Calculate: 4.5 × 10².",
        450, ["450"],
        "Multiplying by 10² (100) shifts the decimal point 2 places to the right: 4.5 -> 450.",
        "450.",
        "450.",
        "4.5 × 100 = 450."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Calculate: 38 ÷ 10³.",
        "0.038",
        ["0.38", "3.8", "0.0038"],
        "Dividing by 10³ (1,000) shifts the decimal point 3 places to the left: 38 -> 0.038.",
        "0.038.",
        "0.038.",
        "38 ÷ 1,000 = 0.038."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Calculate: 7.25 × 10³.",
        7250, ["7250", "7,250"],
        "Shift decimal point 3 places to the right: 7.25 -> 7250.",
        "7,250.",
        "7,250.",
        "7.25 × 1,000 = 7,250."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What happens to the value of a digit when it moves one place to the left?",
        "Its value is multiplied by 10",
        ["Its value is divided by 10", "Its value increases by 10", "Its value stays the same"],
        "In our base-ten number system, each place value to the left is 10 times greater.",
        "Multiplied by 10.",
        "Its value is multiplied by 10.",
        "Moving one place to the left multiplies the digit\\'s value by 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Calculate: 850 ÷ 10².",
        8.5, ["8.5", "8.50"],
        "Shift decimal point 2 places to the left: 850 -> 8.5.",
        "8.5.",
        "8.5.",
        "850 ÷ 100 = 8.5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following is equivalent to 60,000?",
        "6 × 10⁴",
        ["6 × 10³", "6 × 10⁵", "60 × 10⁴"],
        "10⁴ = 10,000. 6 × 10,000 = 60,000.",
        "6 × 10⁴.",
        "6 × 10⁴.",
        "6 × 10⁴ = 60,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 0.09 × 10⁴.",
        900, ["900"],
        "Shift decimal point 4 places to the right: 0.09 -> 900.",
        "900.",
        "900.",
        "0.09 × 10,000 = 900."
    ))

    # =========================================================================
    # LESSON 4: Reading, Writing & Rounding Decimals (5.NBT.A.3 / 5.NBT.A.4)
    # =========================================================================
    LID = "G4_L04"
    LID = "G5_L04"
    LT = "Reading, Writing & Rounding Decimals"
    DOM = "Decimal Place Value & Computation"
    STD = "5.NBT.A.3 / 5.NBT.A.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Round 3.472 to the nearest tenth.",
        3.5, ["3.5"],
        "Look at the hundredths place (7). Since 7 >= 5, round up: 3.4 becomes 3.5.",
        "3.5.",
        "3.5.",
        "3.472 rounds to 3.5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the word form of 0.305?",
        "Three hundred five thousandths",
        ["Three tenths and five hundredths", "Thirty-five hundredths", "Three hundred five tenths"],
        "0.305 has three decimal places, ending in the thousandths place: three hundred five thousandths.",
        "Three hundred five thousandths.",
        "Three hundred five thousandths.",
        "0.305 is three hundred five thousandths."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Round 14.865 to the nearest hundredth.",
        14.87, ["14.87"],
        "Look at the thousandths place (5). Since 5 >= 5, round up: 14.86 becomes 14.87.",
        "14.87.",
        "14.87.",
        "14.865 rounds to 14.87."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Compare 2.45 and 2.409. Which symbol belongs in 2.45 ___ 2.409?",
        ">",
        ["<", "=", "+"],
        "Compare hundredths place: in 2.450, the hundredths digit is 5; in 2.409, the hundredths digit is 0. 5 > 0.",
        "2.45 > 2.409.",
        ">.",
        "2.450 > 2.409."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Round 9.96 to the nearest tenth.",
        10.0, ["10", "10.0"],
        "Hundredths is 6 (>= 5). Round 9.9 up: 9.9 + 0.1 = 10.0.",
        "10.0.",
        "10.0.",
        "9.96 rounds to 10.0."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which of the following numbers is the smallest?",
        "0.089",
        ["0.1", "0.09", "0.102"],
        "Compare tenths: 0.089 and 0.09 have 0 tenths. In hundredths: 8 < 9. So 0.089 is smallest.",
        "0.089.",
        "0.089.",
        "0.089 is smaller than 0.090 and 0.100."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the value of the digit 7 in 4.572? (Enter as a fraction: e.g. 7/100)",
        "7/100", ["7/100", "0.07"],
        "The 7 is in the hundredths place: 7/100 = 0.07.",
        "7/100.",
        "7/100.",
        "The 7 represents 7 hundredths (7/100)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Round 0.648 to the nearest tenth.",
        0.6, ["0.6"],
        "Hundredths is 4 (< 5). Round down to 0.6.",
        "0.6.",
        "0.6.",
        "0.648 rounds to 0.6."
    ))

    # =========================================================================
    # LESSON 5: Whole Number Multiplication (5.NBT.B.5)
    # =========================================================================
    LID = "G5_L05"
    LT = "Whole Number Multiplication"
    DOM = "Decimal Place Value & Computation"
    STD = "5.NBT.B.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 524 × 23.",
        12052, ["12052", "12,052"],
        "Multiply by 3: 524 × 3 = 1,572. Multiply by 20: 524 × 20 = 10,480. Add: 1,572 + 10,480 = 12,052.",
        "12,052.",
        "12,052.",
        "524 × 23 = 12,052."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Calculate: 345 × 18.",
        "6,210",
        ["6,110", "6,310", "5,210"],
        "345 × 18 = 345 × (10 + 8) = 3450 + 2760 = 6,210.",
        "6,210.",
        "6,210.",
        "345 × 18 = 6,210."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 1,248 × 35.",
        43680, ["43680", "43,680"],
        "1,248 × 30 = 37,440; 1,248 × 5 = 6,240. Add: 37,440 + 6,240 = 43,680.",
        "43,680.",
        "43,680.",
        "1,248 × 35 = 43,680."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A factory packs 248 crates of apples every day. How many crates do they pack in 45 days?",
        "11,160 crates",
        ["11,260 crates", "10,160 crates", "11,060 crates"],
        "Multiply 248 by 45: 248 × 40 = 9920; 248 × 5 = 1240. 9920 + 1240 = 11,160.",
        "11,160 crates.",
        "11,160 crates.",
        "248 × 45 = 11,160 crates."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 672 × 84.",
        56448, ["56448", "56,448"],
        "672 × 80 = 53,760; 672 × 4 = 2,688. 53,760 + 2,688 = 56,448.",
        "56,448.",
        "56,448.",
        "672 × 84 = 56,448."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 2,416 × 73.",
        176368, ["176368", "176,368"],
        "2,416 × 73 = 176,368.",
        "176,368.",
        "176,368.",
        "2,416 × 73 = 176,368."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A bookstore sells 185 novels per week. How many novels do they sell in a year (52 weeks)?",
        "9,620 novels",
        ["9,520 novels", "9,720 novels", "8,620 novels"],
        "Multiply 185 by 52: 185 × 50 = 9250; 185 × 2 = 370; 9250 + 370 = 9,620.",
        "9,620 novels.",
        "9,620 novels.",
        "185 × 52 = 9,620 novels."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 3,050 × 46.",
        140300, ["140300", "140,300"],
        "3,050 × 46 = 140,300.",
        "140,300.",
        "140,300.",
        "3,050 × 46 = 140,300."
    ))

    # =========================================================================
    # LESSON 6: Whole Number Division (5.NBT.B.6)
    # =========================================================================
    LID = "G5_L06"
    LT = "Whole Number Division"
    DOM = "Decimal Place Value & Computation"
    STD = "5.NBT.B.6"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 576 ÷ 24.",
        24, ["24"],
        "24 × 20 = 480; 576 - 480 = 96; 96 ÷ 24 = 4. 20 + 4 = 24.",
        "24.",
        "24.",
        "576 ÷ 24 = 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 864 ÷ 18.",
        "48",
        ["46", "44", "52"],
        "18 × 40 = 720; 864 - 720 = 144; 144 ÷ 18 = 8. 40 + 8 = 48.",
        "48.",
        "48.",
        "864 ÷ 18 = 48."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 1,512 ÷ 36.",
        42, ["42"],
        "36 × 40 = 1440; 1512 - 1440 = 72; 72 ÷ 36 = 2. Quotient is 42.",
        "42.",
        "42.",
        "1,512 ÷ 36 = 42."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A warehouse has 2,340 bottles packed into cases of 26 bottles each. How many cases are packed?",
        "90 cases",
        ["85 cases", "92 cases", "95 cases"],
        "Divide 2,340 by 26: 234 ÷ 26 = 9, so 2,340 ÷ 26 = 90.",
        "90 cases.",
        "90 cases.",
        "2,340 ÷ 26 = 90 cases."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 2,750 ÷ 25.",
        110, ["110"],
        "275 ÷ 25 = 11, so 2,750 ÷ 25 = 110.",
        "110.",
        "110.",
        "2,750 ÷ 25 = 110."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 3,456 ÷ 48.",
        72, ["72"],
        "48 × 70 = 3360; 3456 - 3360 = 96; 96 ÷ 48 = 2. 70 + 2 = 72.",
        "72.",
        "72.",
        "3,456 ÷ 48 = 72."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the remainder when 1,845 is divided by 30?",
        "15",
        ["5", "10", "20"],
        "30 × 61 = 1,830. 1,845 - 1,830 = 15.",
        "Remainder 15.",
        "15.",
        "1,845 ÷ 30 = 61 R15."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 4,896 ÷ 32.",
        153, ["153"],
        "32 × 100 = 3200; remaining 1696. 32 × 50 = 1600; remaining 96. 32 × 3 = 96. Total = 153.",
        "153.",
        "153.",
        "4,896 ÷ 32 = 153."
    ))

    # =========================================================================
    # LESSON 7: Adding & Subtracting Decimals (5.NBT.B.7)
    # =========================================================================
    LID = "G5_L07"
    LT = "Adding & Subtracting Decimals"
    DOM = "Decimal Place Value & Computation"
    STD = "5.NBT.B.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 4.35 + 2.42.",
        6.77, ["6.77"],
        "Line up the decimal points and add by place: 5+2=7, 3+4=7, 4+2=6.",
        "6.77.",
        "6.77.",
        "4.35 + 2.42 = 6.77."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 8.75 - 3.25.",
        5.5, ["5.5", "5.50"],
        "Line up decimals: 8.75 - 3.25 = 5.50.",
        "5.5.",
        "5.5.",
        "8.75 - 3.25 = 5.5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 12.8 + 4.65.",
        17.45, ["17.45"],
        "Write 12.8 as 12.80. Then add: 12.80 + 4.65 = 17.45.",
        "17.45.",
        "17.45.",
        "12.80 + 4.65 = 17.45."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 20.00 - 7.64.",
        "12.36",
        ["12.46", "13.36", "12.26"],
        "Regroup across zeros: 20.00 - 7.64 = 12.36.",
        "12.36.",
        "12.36.",
        "20.00 - 7.64 = 12.36."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Maya bought lunch for $8.45 and a dessert for $3.80. How much did she spend in total? (in dollars)",
        12.25, ["12.25", "$12.25"],
        "Add: 8.45 + 3.80 = 12.25.",
        "12.25.",
        "12.25.",
        "$8.45 + $3.80 = $12.25."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 35.6 - 18.75.",
        16.85, ["16.85"],
        "Write 35.60 - 18.75. Regroup: 35.60 - 18.75 = 16.85.",
        "16.85.",
        "16.85.",
        "35.60 - 18.75 = 16.85."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A runner ran 4.25 miles on Monday, 3.8 miles on Wednesday, and 5.15 miles on Friday. What was the total distance?",
        "13.2 miles",
        ["13.1 miles", "12.8 miles", "13.25 miles"],
        "4.25 + 3.80 + 5.15 = 13.20 miles.",
        "13.2 miles.",
        "13.2 miles.",
        "4.25 + 3.80 + 5.15 = 13.20 miles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 50.45 - 28.69.",
        21.76, ["21.76"],
        "Subtract with regrouping: 50.45 - 28.69 = 21.76.",
        "21.76.",
        "21.76.",
        "50.45 - 28.69 = 21.76."
    ))

    # =========================================================================
    # LESSON 8: Multiplying & Dividing Decimals (5.NBT.B.7)
    # =========================================================================
    LID = "G5_L08"
    LT = "Multiplying & Dividing Decimals"
    DOM = "Decimal Place Value & Computation"
    STD = "5.NBT.B.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: 0.4 × 0.6.",
        0.24, ["0.24"],
        "Multiply whole numbers: 4 × 6 = 24. Count total decimal places: 1 + 1 = 2 places -> 0.24.",
        "0.24.",
        "0.24.",
        "0.4 × 0.6 = 0.24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Calculate: 3.5 × 2.",
        "7",
        ["6.5", "7.5", "0.7"],
        "3.5 × 2 = 7.0 = 7.",
        "7.",
        "7.",
        "3.5 × 2 = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 2.5 × 1.4.",
        3.5, ["3.5", "3.50"],
        "25 × 14 = 350. Two decimal places: 3.50 = 3.5.",
        "3.5.",
        "3.5.",
        "2.5 × 1.4 = 3.5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 4.8 ÷ 6.",
        "0.8",
        ["0.08", "8.0", "1.2"],
        "48 tenths ÷ 6 = 8 tenths = 0.8.",
        "0.8.",
        "0.8.",
        "4.8 ÷ 6 = 0.8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 6.3 ÷ 0.9.",
        7, ["7"],
        "Multiply dividend and divisor by 10 to make divisor whole: 63 ÷ 9 = 7.",
        "7.",
        "7.",
        "6.3 ÷ 0.9 = 63 ÷ 9 = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 1.25 × 0.8.",
        1.0, ["1", "1.0", "1.00"],
        "125 × 8 = 1,000. Three decimal places (2 + 1): 1.000 = 1.",
        "1.",
        "1.",
        "1.25 × 0.8 = 1.0."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A ribbon of length 7.5 meters is cut into pieces of 0.5 meters. How many pieces are there?",
        "15 pieces",
        ["14 pieces", "16 pieces", "150 pieces"],
        "Divide 7.5 by 0.5: 75 ÷ 5 = 15 pieces.",
        "15 pieces.",
        "15 pieces.",
        "7.5 ÷ 0.5 = 15 pieces."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 14.4 ÷ 1.2.",
        12, ["12"],
        "Multiply by 10: 144 ÷ 12 = 12.",
        "12.",
        "12.",
        "14.4 ÷ 1.2 = 12."
    ))

    # =========================================================================
    # LESSON 9: Adding & Subtracting Fractions (5.NF.A.1)
    # =========================================================================
    LID = "G5_L09"
    LT = "Adding & Subtracting Fractions"
    DOM = "Fractions"
    STD = "5.NF.A.1"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 1/2 + 1/4.",
        "3/4",
        ["2/6", "2/4", "1/8"],
        "Find a common denominator: 1/2 = 2/4. Then 2/4 + 1/4 = 3/4.",
        "3/4.",
        "3/4.",
        "1/2 + 1/4 = 2/4 + 1/4 = 3/4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 2/3 - 1/6.",
        "3/6 (or 1/2)",
        ["1/3", "1/6", "3/3"],
        "2/3 = 4/6. Then 4/6 - 1/6 = 3/6 = 1/2.",
        "3/6 (1/2).",
        "3/6 (or 1/2).",
        "4/6 - 1/6 = 3/6 = 1/2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the numerator of: 1/3 + 2/5 when written with common denominator 15?",
        11, ["11"],
        "1/3 = 5/15; 2/5 = 6/15. Add: 5/15 + 6/15 = 11/15. Numerator is 11.",
        "11.",
        "11.",
        "5/15 + 6/15 = 11/15, numerator is 11."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 3/4 - 2/5.",
        "7/20",
        ["1/1", "1/20", "5/20"],
        "Common denominator 20: 3/4 = 15/20; 2/5 = 8/20. 15/20 - 8/20 = 7/20.",
        "7/20.",
        "7/20.",
        "15/20 - 8/20 = 7/20."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the numerator of the sum: 5/6 + 1/4 with least common denominator 12?",
        13, ["13"],
        "5/6 = 10/12; 1/4 = 3/12. 10/12 + 3/12 = 13/12. Numerator is 13.",
        "13.",
        "13.",
        "10/12 + 3/12 = 13/12, numerator is 13."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 2 and 1/3 + 1 and 1/2.",
        "3 and 5/6",
        ["3 and 2/5", "4 and 1/6", "3 and 1/6"],
        "Common denominator 6: 1/3 = 2/6; 1/2 = 3/6. Sum = (2 + 1) + (2/6 + 3/6) = 3 and 5/6.",
        "3 and 5/6.",
        "3 and 5/6.",
        "2 2/6 + 1 3/6 = 3 5/6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Solve: 4 and 1/4 - 1 and 2/3.",
        "2 and 7/12",
        ["2 and 1/12", "3 and 7/12", "2 and 5/12"],
        "Denominators 12: 4 3/12 - 1 8/12. Regroup 4 3/12 as 3 15/12. (3 - 1) + (15/12 - 8/12) = 2 and 7/12.",
        "2 and 7/12.",
        "2 and 7/12.",
        "3 15/12 - 1 8/12 = 2 7/12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the numerator of: 7/8 - 1/3 when written with common denominator 24?",
        13, ["13"],
        "7/8 = 21/24; 1/3 = 8/24. 21 - 8 = 13.",
        "13.",
        "13.",
        "21/24 - 8/24 = 13/24, numerator is 13."
    ))

    # =========================================================================
    # LESSON 10: Fraction Addition/Subtraction Problems (5.NF.A.2)
    # =========================================================================
    LID = "G5_L10"
    LT = "Fraction Addition/Subtraction Problems"
    DOM = "Fractions"
    STD = "5.NF.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Leo used 1/2 cup of sugar for cookies and 1/3 cup of sugar for frosting. How much sugar did he use in total?",
        "5/6 cup",
        ["2/5 cup", "2/6 cup", "1 cup"],
        "1/2 + 1/3 = 3/6 + 2/6 = 5/6 cup.",
        "5/6 cup.",
        "5/6 cup.",
        "3/6 + 2/6 = 5/6 cup."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A board is 7/8 meter long. A carpenter cuts off 1/4 meter. How long is the remaining piece?",
        "5/8 meter",
        ["6/8 meter", "3/8 meter", "1/2 meter"],
        "1/4 = 2/8. 7/8 - 2/8 = 5/8 meter.",
        "5/8 meter.",
        "5/8 meter.",
        "7/8 - 2/8 = 5/8 meter."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Estimate 3/8 + 7/12 using benchmark fractions 0, 1/2, 1. Which estimate is most reasonable?",
        "About 1",
        ["About 0", "About 1/2", "About 2"],
        "3/8 is close to 1/2; 7/12 is close to 1/2. 1/2 + 1/2 = 1.",
        "About 1.",
        "About 1.",
        "Both fractions are close to 1/2, so the sum is about 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Sofia walked 2 and 1/2 miles in the morning and 1 and 3/4 miles in the evening. How many miles did she walk altogether?",
        "4 and 1/4 miles",
        ["3 and 4/6 miles", "4 miles", "3 and 3/4 miles"],
        "2 2/4 + 1 3/4 = 3 5/4 = 4 1/4 miles.",
        "4 and 1/4 miles.",
        "4 and 1/4 miles.",
        "2 2/4 + 1 3/4 = 4 1/4 miles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A recipe called for 3/4 teaspoon of salt. Carlos accidentally used 1/2 teaspoon. What is the numerator of the fraction of salt he still needs to add (over 4)?",
        1, ["1"],
        "3/4 - 1/2 = 3/4 - 2/4 = 1/4. Numerator is 1.",
        "1.",
        "1.",
        "3/4 - 2/4 = 1/4, numerator is 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A tank had 5 and 1/6 gallons of water. 2 and 2/3 gallons were used. How many gallons are left?",
        "2 and 1/2 gallons",
        ["2 and 1/6 gallons", "3 gallons", "2 and 2/3 gallons"],
        "Common denominator 6: 5 1/6 - 2 4/6 = 4 7/6 - 2 4/6 = 2 3/6 = 2 1/2 gallons.",
        "2 and 1/2 gallons.",
        "2 and 1/2 gallons.",
        "4 7/6 - 2 4/6 = 2 3/6 = 2 1/2 gallons."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A student spent 1/4 of their allowance on books and 2/5 on food. What is the numerator of the total fraction spent (over 20)?",
        13, ["13"],
        "1/4 = 5/20; 2/5 = 8/20. 5/20 + 8/20 = 13/20. Numerator is 13.",
        "13.",
        "13.",
        "5/20 + 8/20 = 13/20, numerator is 13."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In problem Q07 (spent 13/20), what fraction of the allowance is saved?",
        "7/20",
        ["13/20", "1/20", "7/10"],
        "1 - 13/20 = 20/20 - 13/20 = 7/20.",
        "7/20.",
        "7/20.",
        "1 - 13/20 = 7/20."
    ))

    # =========================================================================
    # LESSON 11: Fractions as Division Word Problems (5.NF.B.3)
    # =========================================================================
    LID = "G5_L11"
    LT = "Fractions as Division Word Problems"
    DOM = "Fractions"
    STD = "5.NF.B.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "3 friends share 2 pizzas equally. What fraction of a pizza does each friend get?",
        "2/3",
        ["3/2", "1/3", "1/2"],
        "Fraction as division: (items) ÷ (people) = 2 ÷ 3 = 2/3.",
        "2/3.",
        "2/3.",
        "2 pizzas ÷ 3 friends = 2/3 pizza each."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which division expression is equivalent to the fraction 7/4?",
        "7 ÷ 4",
        ["4 ÷ 7", "7 × 4", "4 - 7"],
        "A fraction a/b represents a ÷ b.",
        "7 ÷ 4.",
        "7 ÷ 4.",
        "7/4 = 7 ÷ 4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "5 granola bars are shared equally among 4 campers. How many granola bars does each camper receive?",
        "1 and 1/4 bars",
        ["1 bar", "4/5 bar", "1 and 1/2 bars"],
        "5 ÷ 4 = 5/4 = 1 and 1/4 bars.",
        "1 and 1/4 bars.",
        "1 and 1/4 bars.",
        "5 ÷ 4 = 1 1/4 bars."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "8 yards of fabric are cut into 5 equal pieces. What is the numerator of each piece\\'s length when written as an improper fraction (8/5)?",
        8, ["8"],
        "8 ÷ 5 = 8/5. The numerator is 8.",
        "8.",
        "8.",
        "8 ÷ 5 = 8/5, numerator is 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Between which two whole numbers does 17 ÷ 3 lie?",
        "5 and 6",
        ["4 and 5", "6 and 7", "3 and 4"],
        "17 ÷ 3 = 5 R2 = 5 and 2/3, which is between 5 and 6.",
        "5 and 6.",
        "5 and 6.",
        "17/3 = 5 2/3, between 5 and 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "6 pounds of nuts are shared equally by 8 bags. How many pounds are in each bag in simplest form?",
        "3/4 pound",
        ["6/8 pound", "4/3 pound", "1/2 pound"],
        "6 ÷ 8 = 6/8 = 3/4 pound.",
        "3/4 pound.",
        "3/4 pound.",
        "6 ÷ 8 = 3/4 pound."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is 20 ÷ 6 written as a mixed number in simplest form? (Enter whole number part: e.g. 3)",
        3, ["3"],
        "20 ÷ 6 = 3 R2 = 3 and 2/6 = 3 and 1/3. Whole number part is 3.",
        "3.",
        "3.",
        "20/6 = 3 1/3, whole number is 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If 9 liters of water are poured equally into 4 jugs, each jug receives:",
        "2 and 1/4 liters",
        ["2 liters", "2 and 1/2 liters", "4/9 liter"],
        "9 ÷ 4 = 9/4 = 2 and 1/4 liters.",
        "2 and 1/4 liters.",
        "2 and 1/4 liters.",
        "9 ÷ 4 = 2 1/4 liters."
    ))

    # =========================================================================
    # LESSON 12: Multiplying Fractions (5.NF.B.4 / 5.NF.B.5)
    # =========================================================================
    LID = "G5_L12"
    LT = "Multiplying Fractions"
    DOM = "Fractions"
    STD = "5.NF.B.4 / 5.NF.B.5"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: (1/2) × (3/4).",
        "3/8",
        ["4/6", "3/6", "1/8"],
        "Multiply numerators and multiply denominators: (1 × 3) / (2 × 4) = 3/8.",
        "3/8.",
        "3/8.",
        "(1 × 3) / (2 × 4) = 3/8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the numerator of: (2/3) × (4/5)?",
        8, ["8"],
        "Multiply numerators: 2 × 4 = 8. (Result is 8/15).",
        "8.",
        "8.",
        "2 × 4 = 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rectangle has length 2/3 foot and width 3/4 foot. What is its area in square feet?",
        "1/2 sq ft",
        ["6/12 sq ft", "5/7 sq ft", "2/4 sq ft"],
        "Area = (2/3) × (3/4) = 6/12 = 1/2 square foot.",
        "1/2 sq ft.",
        "1/2 sq ft.",
        "2/3 × 3/4 = 6/12 = 1/2 sq ft."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "When you multiply 12 by 3/4, will the product be greater than or less than 12?",
        "Less than 12, because 3/4 is less than 1",
        ["Greater than 12, because multiplication always makes things bigger", "Equal to 12", "Cannot be determined"],
        "Multiplying a number by a fraction less than 1 scales the number down.",
        "Less than 12.",
        "Less than 12, because 3/4 < 1.",
        "12 × 3/4 = 9, which is less than 12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Calculate: (3/5) × (5/6). What is the simplest form numerator?",
        1, ["1"],
        "(3 × 5)/(5 × 6) = 15/30 = 1/2. The numerator is 1.",
        "1.",
        "1.",
        "15/30 = 1/2, numerator is 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 1 and 1/2 × 2 and 2/3.",
        "4",
        ["3 and 2/6", "4 and 1/3", "3 and 1/2"],
        "Convert to improper: (3/2) × (8/3) = 24/6 = 4.",
        "4.",
        "4.",
        "3/2 × 8/3 = 24/6 = 4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which product will be greater than 8?",
        "8 × (5/4)",
        ["8 × (4/5)", "8 × (1/2)", "8 × (7/8)"],
        "To get a product greater than 8, multiply by a factor greater than 1. 5/4 > 1.",
        "8 × (5/4).",
        "8 × (5/4).",
        "8 × 5/4 = 10 > 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: (4/7) × (7/8). What is the simplest form denominator?",
        2, ["2"],
        "(4 × 7)/(7 × 8) = 28/56 = 1/2. The denominator is 2.",
        "2.",
        "2.",
        "28/56 = 1/2, denominator is 2."
    ))

    # =========================================================================
    # LESSON 13: Fraction Multiplication Word Problems (5.NF.B.6)
    # =========================================================================
    LID = "G5_L13"
    LT = "Fraction Multiplication Word Problems"
    DOM = "Fractions"
    STD = "5.NF.B.6"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A recipe calls for 3/4 cup of milk. Carlos makes 1/2 of the recipe. How much milk does he need?",
        "3/8 cup",
        ["4/6 cup", "3/6 cup", "1/4 cup"],
        "Multiply: (1/2) × (3/4) = 3/8 cup.",
        "3/8 cup.",
        "3/8 cup.",
        "1/2 × 3/4 = 3/8 cup."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "There are 24 students in a class. 3/4 of them play an instrument. How many students play an instrument?",
        18, ["18", "18 students"],
        "Multiply: 24 × (3/4) = (24 ÷ 4) × 3 = 6 × 3 = 18.",
        "18.",
        "18 students.",
        "24 × 3/4 = 18 students."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rectangular painting is 3 and 1/2 feet long and 2 feet wide. What is its area in square feet?",
        "7 sq ft",
        ["6 sq ft", "5 and 1/2 sq ft", "8 sq ft"],
        "Area = length × width = (7/2) × 2 = 14/2 = 7 square feet.",
        "7 sq ft.",
        "7 sq ft.",
        "3 1/2 × 2 = 7 sq ft."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Marcus had $60. He spent 2/5 of his money on clothes. How much money did Marcus spend in dollars?",
        "$24",
        ["$30", "$20", "$36"],
        "60 × (2/5) = (60 ÷ 5) × 2 = 12 × 2 = $24.",
        "$24.",
        "$24.",
        "60 × 2/5 = $24."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "In problem Q04 (Marcus spent $24 out of $60), how many dollars does he have left?",
        36, ["36", "$36"],
        "60 - 24 = 36 (or 60 × 3/5 = 36).",
        "36.",
        "$36.",
        "60 - 24 = $36."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A garden bed has dimensions 4 and 1/2 meters by 1 and 1/3 meters. What is the area in square meters?",
        "6 sq meters",
        ["5 and 1/6 sq m", "4 and 1/3 sq m", "7 sq m"],
        "(9/2) × (4/3) = 36/6 = 6 square meters.",
        "6 sq meters.",
        "6 sq meters.",
        "9/2 × 4/3 = 36/6 = 6 sq m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A runner completed 2/3 of a 15-mile trail. How many miles did the runner complete?",
        10, ["10", "10 miles"],
        "15 × (2/3) = (15 ÷ 3) × 2 = 5 × 2 = 10 miles.",
        "10 miles.",
        "10.",
        "15 × 2/3 = 10 miles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A pet shelter has 36 animals. 5/12 of the animals are cats. How many cats are at the shelter?",
        "15 cats",
        ["12 cats", "18 cats", "10 cats"],
        "36 × (5/12) = (36 ÷ 12) × 5 = 3 × 5 = 15 cats.",
        "15 cats.",
        "15 cats.",
        "36 × 5/12 = 15 cats."
    ))

    # =========================================================================
    # LESSON 14: Dividing Unit Fractions by Wholes (5.NF.B.7a / 5.NF.B.7c)
    # =========================================================================
    LID = "G5_L14"
    LT = "Dividing Unit Fractions by Wholes"
    DOM = "Fractions"
    STD = "5.NF.B.7a / 5.NF.B.7c"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: (1/3) ÷ 4.",
        "1/12",
        ["4/3", "3/4", "1/7"],
        "Dividing a unit fraction by a whole number multiplies the denominator: 1/(3 × 4) = 1/12.",
        "1/12.",
        "1/12.",
        "1/3 ÷ 4 = 1/12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the denominator of (1/2) ÷ 5?",
        10, ["10"],
        "(1/2) ÷ 5 = 1/(2 × 5) = 1/10. The denominator is 10.",
        "10.",
        "10.",
        "1/2 ÷ 5 = 1/10, denominator is 10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Half of a cake is shared equally among 3 friends. What fraction of the original whole cake does each friend get?",
        "1/6 of the cake",
        ["1/5 of the cake", "2/3 of the cake", "1/3 of the cake"],
        "(1/2) ÷ 3 = 1/(2 × 3) = 1/6.",
        "1/6 of the cake.",
        "1/6 of the cake.",
        "1/2 ÷ 3 = 1/6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: (1/4) ÷ 2.",
        "1/8",
        ["2/4", "1/2", "1/6"],
        "(1/4) ÷ 2 = 1/(4 × 2) = 1/8.",
        "1/8.",
        "1/8.",
        "1/4 ÷ 2 = 1/8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A chef divides 1/5 pan of lasagna equally into 3 portions. What is the denominator of each portion (1/___)?",
        15, ["15"],
        "(1/5) ÷ 3 = 1/15. Denominator is 15.",
        "15.",
        "15.",
        "1/5 ÷ 3 = 1/15, denominator is 15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: (1/6) ÷ 4.",
        "1/24",
        ["4/6", "1/10", "24"],
        "(1/6) ÷ 4 = 1/(6 × 4) = 1/24.",
        "1/24.",
        "1/24.",
        "1/6 ÷ 4 = 1/24."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the denominator of (1/8) ÷ 3?",
        24, ["24"],
        "8 × 3 = 24. Result is 1/24.",
        "24.",
        "24.",
        "1/8 ÷ 3 = 1/24, denominator is 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If 1/3 pound of clay is divided equally among 6 art students, how much clay does each student receive?",
        "1/18 pound",
        ["2 pounds", "1/9 pound", "1/2 pound"],
        "(1/3) ÷ 6 = 1/18 pound.",
        "1/18 pound.",
        "1/18 pound.",
        "1/3 ÷ 6 = 1/18 pound."
    ))

    # =========================================================================
    # LESSON 15: Dividing Wholes by Unit Fractions (5.NF.B.7b / 5.NF.B.7c)
    # =========================================================================
    LID = "G5_L15"
    LT = "Dividing Wholes by Unit Fractions"
    DOM = "Fractions"
    STD = "5.NF.B.7b / 5.NF.B.7c"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 4 ÷ (1/3).",
        12, ["12"],
        "Dividing by 1/3 means finding how many thirds are in 4: 4 × 3 = 12.",
        "12.",
        "12.",
        "4 ÷ 1/3 = 4 × 3 = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 3 ÷ (1/2).",
        "6",
        ["1 and 1/2", "3/2", "5"],
        "There are two halves in each whole: 3 × 2 = 6.",
        "6.",
        "6.",
        "3 ÷ 1/2 = 6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A teacher has 5 yards of ribbon. She cuts it into pieces of 1/4 yard each. How many pieces can she make?",
        20, ["20", "20 pieces"],
        "Divide 5 by 1/4: 5 × 4 = 20 pieces.",
        "20 pieces.",
        "20.",
        "5 ÷ 1/4 = 20 pieces."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 6 ÷ (1/5).",
        "30",
        ["6/5", "1 and 1/5", "25"],
        "6 × 5 = 30.",
        "30.",
        "30.",
        "6 ÷ 1/5 = 30."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many 1/6-cup servings of juice are in 3 cups of juice?",
        18, ["18", "18 servings"],
        "3 ÷ (1/6) = 3 × 6 = 18 servings.",
        "18.",
        "18 servings.",
        "3 ÷ 1/6 = 18 servings."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 8 ÷ (1/4).",
        32, ["32"],
        "8 × 4 = 32.",
        "32.",
        "32.",
        "8 ÷ 1/4 = 32."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A track coach has 7 liters of water. Each water bottle holds 1/3 liter. How many bottles can be filled?",
        "21 bottles",
        ["14 bottles", "24 bottles", "7/3 bottles"],
        "7 ÷ (1/3) = 7 × 3 = 21 bottles.",
        "21 bottles.",
        "21 bottles.",
        "7 ÷ 1/3 = 21 bottles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 9 ÷ (1/5).",
        45, ["45"],
        "9 × 5 = 45.",
        "45.",
        "45.",
        "9 ÷ 1/5 = 45."
    ))

    # =========================================================================
    # LESSON 16: Measurement Conversions (5.MD.A.1)
    # =========================================================================
    LID = "G5_L16"
    LT = "Measurement Conversions"
    DOM = "Measurement & Data"
    STD = "5.MD.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Convert 3.5 meters to centimeters. (1 m = 100 cm)",
        350, ["350", "350 cm"],
        "Multiply meters by 100: 3.5 × 100 = 350 cm.",
        "350 cm.",
        "350.",
        "3.5 × 100 = 350 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Convert 4,500 grams to kilograms. (1 kg = 1,000 g)",
        "4.5 kg",
        ["45 kg", "0.45 kg", "450 kg"],
        "Divide grams by 1,000: 4,500 ÷ 1,000 = 4.5 kg.",
        "4.5 kg.",
        "4.5 kg.",
        "4,500 ÷ 1,000 = 4.5 kg."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "How many inches are in 4.5 feet? (1 foot = 12 inches)",
        54, ["54", "54 inches"],
        "4.5 × 12 = 54 inches.",
        "54 inches.",
        "54.",
        "4.5 × 12 = 54 inches."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "How many quarts are in 6 gallons? (1 gallon = 4 quarts)",
        "24 quarts",
        ["20 quarts", "18 quarts", "12 quarts"],
        "Multiply gallons by 4: 6 × 4 = 24 quarts.",
        "24 quarts.",
        "24 quarts.",
        "6 × 4 = 24 quarts."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Convert 2.8 liters to milliliters. (1 L = 1,000 mL)",
        2800, ["2800", "2,800", "2800 mL"],
        "2.8 × 1,000 = 2,800 mL.",
        "2,800 mL.",
        "2,800.",
        "2.8 × 1,000 = 2,800 mL."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rope is 54 feet long. How many yards long is the rope? (1 yard = 3 feet)",
        18, ["18", "18 yards"],
        "Divide feet by 3: 54 ÷ 3 = 18 yards.",
        "18 yards.",
        "18.",
        "54 ÷ 3 = 18 yards."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A package weighs 80 ounces. How many pounds is that? (1 lb = 16 oz)",
        "5 pounds",
        ["4 pounds", "6 pounds", "4.5 pounds"],
        "Divide 80 by 16: 80 ÷ 16 = 5 pounds.",
        "5 pounds.",
        "5 pounds.",
        "80 ÷ 16 = 5 pounds."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Convert 750 centimeters to meters.",
        7.5, ["7.5", "7.5 m"],
        "Divide by 100: 750 ÷ 100 = 7.5 meters.",
        "7.5 meters.",
        "7.5.",
        "750 ÷ 100 = 7.5 m."
    ))

    # =========================================================================
    # LESSON 17: Representing Data on Line Plots (5.MD.B.2)
    # =========================================================================
    LID = "G5_L17"
    LT = "Representing Data on Line Plots"
    DOM = "Measurement & Data"
    STD = "5.MD.B.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Four beakers have liquid amounts: 1/4 L, 1/4 L, 1/2 L, 1/2 L. What is the total liquid amount?",
        "1 and 1/2 liters",
        ["1 liter", "2 liters", "3/4 liter"],
        "1/4 + 1/4 = 1/2. 1/2 + 1/2 + 1/2 = 3/2 = 1 1/2 liters.",
        "1 and 1/2 liters.",
        "1 and 1/2 liters.",
        "1/4 + 1/4 + 1/2 + 1/2 = 1 1/2 L."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "If the 1 and 1/2 liters (6/4 L) from Q01 is distributed equally among all 4 beakers, what is the numerator of each beaker\\'s share (over 8)?",
        3, ["3"],
        "(6/4) ÷ 4 = 6/16 = 3/8 liter. Numerator is 3.",
        "3.",
        "3.",
        "1.5 ÷ 4 = 3/8 L, numerator is 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A line plot shows seed lengths in inches: 1/8, 1/8, 3/8, 5/8, 5/8. What is the difference between the longest and shortest seed?",
        "4/8 inch (1/2 inch)",
        ["5/8 inch", "3/8 inch", "2/8 inch"],
        "5/8 - 1/8 = 4/8 = 1/2 inch.",
        "4/8 inch (1/2 inch).",
        "4/8 inch (1/2 inch).",
        "5/8 - 1/8 = 1/2 inch."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the total combined weight of three gems that each weigh 3/4 ounce? (Enter improper fraction numerator over 4)",
        9, ["9"],
        "3 × 3/4 = 9/4 ounces. Numerator is 9.",
        "9.",
        "9.",
        "3 × 3/4 = 9/4 oz, numerator is 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the average of two lengths: 1/2 inch and 3/4 inch?",
        "5/8 inch",
        ["4/6 inch", "1/2 inch", "3/4 inch"],
        "Sum = 2/4 + 3/4 = 5/4. Average = (5/4) ÷ 2 = 5/8 inch.",
        "5/8 inch.",
        "5/8 inch.",
        "(1/2 + 3/4) ÷ 2 = 5/8 inch."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Five bags of trail mix weigh 1/4 lb, 1/4 lb, 1/2 lb, 1/2 lb, 1/2 lb. What is their total combined weight in pounds? (2.0 or 2)",
        2, ["2", "2.0", "2 lbs"],
        "1/4 + 1/4 = 1/2. Four halves = 2 whole pounds.",
        "2 pounds.",
        "2.",
        "Total weight is 2 pounds."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If the 2 pounds of trail mix from Q06 is redistributed equally into the 5 bags, how much does each bag weigh?",
        "2/5 pound",
        ["1/5 pound", "1/2 pound", "4/5 pound"],
        "2 ÷ 5 = 2/5 pound.",
        "2/5 pound.",
        "2/5 pound.",
        "2 ÷ 5 = 2/5 lb."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the sum of six measurements of 1/8 inch? (Enter simplest form numerator over 4)",
        3, ["3"],
        "6 × 1/8 = 6/8 = 3/4 inch. Numerator is 3.",
        "3.",
        "3.",
        "6/8 = 3/4, numerator is 3."
    ))

    # =========================================================================
    # LESSON 18: Understanding Volume (5.MD.C.3 / 5.MD.C.4)
    # =========================================================================
    LID = "G5_L18"
    LT = "Understanding Volume"
    DOM = "Measurement & Data"
    STD = "5.MD.C.3 / 5.MD.C.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A box is filled with unit cubes with side lengths of 1 cm. It holds 24 unit cubes with no gaps. What is the volume in cubic centimeters?",
        24, ["24", "24 cm³", "24 cubic cm"],
        "Volume is measured by the total number of unit cubes packed into the solid.",
        "24 unit cubes = 24 cubic centimeters.",
        "24.",
        "Volume = 24 cubic centimeters."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What unit is used to measure volume?",
        "Cubic units",
        ["Square units", "Linear units", "Degrees"],
        "Volume measures 3-dimensional space, so it is measured in cubic units (e.g., cm³, cubic inches).",
        "Cubic units.",
        "Cubic units.",
        "Volume is measured in cubic units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A prism is built with 3 layers. Each layer has 8 unit cubes. What is the total volume in cubic units?",
        24, ["24", "24 cubic units"],
        "Volume = (cubes per layer) × (number of layers) = 8 × 3.",
        "8 × 3 = 24 cubic units.",
        "24.",
        "8 × 3 = 24 cubic units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A cube has an edge length of 1 inch. What is its volume?",
        "1 cubic inch",
        ["1 square inch", "3 inches", "6 square inches"],
        "Volume = 1 in × 1 in × 1 in = 1 cubic inch.",
        "1 cubic inch.",
        "1 cubic inch.",
        "Volume of a unit cube is 1 cubic inch."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A rectangular prism is 4 cubes long, 3 cubes wide, and 2 cubes high. How many unit cubes fill the prism?",
        24, ["24"],
        "Multiply dimensions: 4 × 3 × 2 = 24 unit cubes.",
        "24.",
        "24.",
        "4 × 3 × 2 = 24 cubes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A tower is made of 5 layers of unit cubes. Each layer is 4 cubes long and 2 cubes wide. What is the total volume?",
        40, ["40", "40 cubic units"],
        "Base layer = 4 × 2 = 8 cubes. Total volume = 8 × 5 = 40 cubic units.",
        "40.",
        "40.",
        "4 × 2 × 5 = 40 cubic units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which solid figure has a volume of 30 cubic units?",
        "A prism with dimensions 5 by 3 by 2",
        ["A prism with dimensions 5 by 5 by 2", "A prism with dimensions 6 by 6 by 1", "A prism with dimensions 4 by 4 by 2"],
        "Multiply: 5 × 3 × 2 = 30.",
        "5 by 3 by 2.",
        "A prism with dimensions 5 by 3 by 2.",
        "5 × 3 × 2 = 30 cubic units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "How many cubic centimeters are in a rectangular solid that holds 60 one-centimeter unit cubes?",
        60, ["60", "60 cm³"],
        "Each cube is 1 cm³. 60 cubes = 60 cm³.",
        "60 cm³.",
        "60.",
        "60 cubic centimeters."
    ))

    # =========================================================================
    # LESSON 19: Volume of Rectangular Prisms (5.MD.C.5a-b)
    # =========================================================================
    LID = "G5_L19"
    LT = "Volume of Rectangular Prisms"
    DOM = "Measurement & Data"
    STD = "5.MD.C.5a-b"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the volume of a rectangular prism with length 6 cm, width 4 cm, and height 5 cm in cubic cm.",
        120, ["120", "120 cm³"],
        "Formula: Volume = length × width × height = 6 × 4 × 5.",
        "6 × 4 = 24; 24 × 5 = 120 cm³.",
        "120.",
        "6 × 4 × 5 = 120 cm³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which formula gives the volume of a rectangular prism?",
        "Volume = Base Area × height (V = Bh)",
        ["Volume = 2 × (length + width)", "Volume = Base Area + height", "Volume = length × width ÷ height"],
        "Volume = length × width × height = Base Area (B) × height (h).",
        "V = Bh.",
        "Volume = Base Area × height (V = Bh).",
        "V = lwh = Bh."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A storage container has a base area of 45 square feet and a height of 8 feet. What is its volume in cubic feet?",
        360, ["360", "360 cu ft"],
        "Volume = Base Area × height = 45 × 8.",
        "45 × 8 = 360 cubic feet.",
        "360.",
        "45 × 8 = 360 cu ft."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the volume of a cube with an edge length of 4 inches?",
        "64 cubic inches",
        ["16 cubic inches", "48 cubic inches", "96 cubic inches"],
        "For a cube, V = s³ = 4 × 4 × 4 = 64 cubic inches.",
        "64 cu in.",
        "64 cubic inches.",
        "4 × 4 × 4 = 64 cubic inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A box has a volume of 210 cubic inches. Its length is 7 inches and width is 5 inches. What is its height in inches?",
        6, ["6", "6 inches"],
        "Base area = 7 × 5 = 35 sq in. Height = Volume ÷ Base Area = 210 ÷ 35 = 6 inches.",
        "6 inches.",
        "6.",
        "210 ÷ 35 = 6 inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the volume of a shipping crate that is 12 feet long, 8 feet wide, and 10 feet high in cubic feet.",
        960, ["960", "960 cu ft"],
        "V = 12 × 8 × 10 = 96 × 10 = 960 cubic feet.",
        "960.",
        "960.",
        "12 × 8 × 10 = 960 cu ft."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A fish tank is 20 inches long, 10 inches wide, and 12 inches high. What is its volume in cubic inches?",
        "2,400 cubic inches",
        ["2,000 cubic inches", "2,200 cubic inches", "1,200 cubic inches"],
        "V = 20 × 10 × 12 = 200 × 12 = 2,400 cubic inches.",
        "2,400 cu in.",
        "2,400 cubic inches.",
        "20 × 10 × 12 = 2,400 cu in."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the volume of a prism with dimensions 15 cm by 6 cm by 4 cm?",
        360, ["360", "360 cm³"],
        "15 × 6 = 90; 90 × 4 = 360 cm³.",
        "360.",
        "360.",
        "15 × 6 × 4 = 360 cm³."
    ))

    # =========================================================================
    # LESSON 20: Volume of Composite Prisms (5.MD.C.5c)
    # =========================================================================
    LID = "G5_L20"
    LT = "Volume of Composite Prisms"
    DOM = "Measurement & Data"
    STD = "5.MD.C.5c"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A composite solid is made of two non-overlapping prisms. Prism A has volume 40 cm³ and Prism B has volume 25 cm³. What is the total volume?",
        65, ["65", "65 cm³"],
        "Additive property of volume: Total volume = Volume A + Volume B = 40 + 25.",
        "65 cm³.",
        "65.",
        "40 + 25 = 65 cm³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "To find the volume of an L-shaped solid, what is the best strategy?",
        "Decompose the solid into two non-overlapping rectangular prisms and add their volumes",
        ["Multiply all the numbers you see together", "Measure the perimeter of the base", "Subtract the smaller part from the larger part"],
        "Decompose into simpler rectangular prisms, calculate each volume, and add them.",
        "Decompose and add volumes.",
        "Decompose the solid into two non-overlapping rectangular prisms and add their volumes.",
        "Decomposing and adding the parts gives the total volume."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A solid is decomposed into Prism 1 (4 × 3 × 5 = 60 cu in) and Prism 2 (2 × 3 × 5 = 30 cu in). What is the total volume in cubic inches?",
        90, ["90", "90 cu in"],
        "Total Volume = 60 + 30 = 90 cubic inches.",
        "90.",
        "90.",
        "60 + 30 = 90 cu in."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A building has two towers. Tower 1 has dimensions 10m × 8m × 20m (volume 1,600 m³). Tower 2 has dimensions 6m × 8m × 15m (volume 720 m³). What is the total volume?",
        "2,320 cubic meters",
        ["2,420 cubic meters", "2,220 cubic meters", "1,880 cubic meters"],
        "1,600 + 720 = 2,320 m³.",
        "2,320 m³.",
        "2,320 cubic meters.",
        "1,600 + 720 = 2,320 m³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A step stool consists of two steps: Step 1 is 12 in × 6 in × 4 in (volume 288) and Step 2 is 12 in × 6 in × 8 in (volume 576). What is the total volume in cubic inches?",
        864, ["864", "864 cu in"],
        "288 + 576 = 864 cubic inches.",
        "864.",
        "864.",
        "288 + 576 = 864 cu in."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A composite sculpture has three blocks with volumes 50 cm³, 75 cm³, and 125 cm³. What is the total volume in cubic cm?",
        250, ["250", "250 cm³"],
        "50 + 75 + 125 = 250 cm³.",
        "250.",
        "250.",
        "50 + 75 + 125 = 250 cm³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A hollow concrete box has an outer volume of 500 cm³ and an inner hollow space of 180 cm³. What is the volume of concrete used?",
        "320 cm³",
        ["680 cm³", "350 cm³", "400 cm³"],
        "Subtract hollow space from outer volume: 500 - 180 = 320 cm³.",
        "320 cm³.",
        "320 cm³.",
        "500 - 180 = 320 cm³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Two identical prisms each have dimensions 5 cm by 4 cm by 3 cm (each volume 60). When joined, what is the combined volume?",
        120, ["120", "120 cm³"],
        "60 × 2 = 120 cm³.",
        "120.",
        "120.",
        "60 + 60 = 120 cm³."
    ))

    # =========================================================================
    # LESSON 21: Coordinate Plane Intro (5.G.A.1)
    # =========================================================================
    LID = "G5_L21"
    LT = "Coordinate Plane Intro"
    DOM = "Geometry & Graphs"
    STD = "5.G.A.1"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What are the coordinates of the origin on a coordinate plane?",
        "(0, 0)",
        ["(1, 1)", "(0, 1)", "(1, 0)"],
        "The origin is the intersection of the x-axis and y-axis at (0, 0).",
        "(0, 0).",
        "(0, 0).",
        "The origin is at (0, 0)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In the ordered pair (4, 7), which number represents the x-coordinate?",
        "4",
        ["7", "11", "0"],
        "In (x, y), the first coordinate is x (horizontal distance) and the second is y (vertical distance).",
        "4.",
        "4.",
        "In (4, 7), the x-coordinate is 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Starting at the origin (0, 0), you move 6 units right along the x-axis and 9 units up parallel to the y-axis. What is the y-coordinate of your ending point?",
        9, ["9"],
        "Moving up parallel to the y-axis increases the y-coordinate to 9.",
        "9.",
        "9.",
        "The ending point is (6, 9), so y = 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which point lies on the x-axis?",
        "(5, 0)",
        ["(0, 5)", "(5, 5)", "(1, 5)"],
        "Points on the x-axis have a y-coordinate of 0: (x, 0).",
        "(5, 0).",
        "(5, 0).",
        "(5, 0) is on the x-axis because y = 0."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "In the point (8, 3), how many units above the x-axis is the point?",
        3, ["3", "3 units"],
        "The y-coordinate tells the distance above the x-axis: 3 units.",
        "3.",
        "3 units.",
        "Distance above x-axis is y = 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which direction do you move first from the origin to plot the point (3, 8)?",
        "Right 3 units along the horizontal x-axis",
        ["Up 3 units along the vertical y-axis", "Left 3 units", "Down 8 units"],
        "First move horizontally (right) for x, then vertically (up) for y.",
        "Right 3 units.",
        "Right 3 units along the horizontal x-axis.",
        "Always move horizontal (x) first, then vertical (y)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which point lies on the vertical y-axis?",
        "(0, 7)",
        ["(7, 0)", "(7, 7)", "(1, 7)"],
        "Points on the y-axis have an x-coordinate of 0: (0, y).",
        "(0, 7).",
        "(0, 7).",
        "(0, 7) lies on the y-axis."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Point A is at (2, 5) and Point B is at (8, 5). What is the horizontal distance between Point A and Point B in units?",
        6, ["6", "6 units"],
        "Since the y-coordinates are the same (5), subtract the x-coordinates: 8 - 2 = 6.",
        "6 units.",
        "6.",
        "8 - 2 = 6 units."
    ))

    # =========================================================================
    # LESSON 22: Graphing Real-World Problems (5.G.A.2)
    # =========================================================================
    LID = "G5_L22"
    LT = "Graphing Real-World Problems"
    DOM = "Geometry & Graphs"
    STD = "5.G.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A graph shows time in hours on the x-axis and distance in miles on the y-axis. What distance does the point (3, 15) represent in miles?",
        15, ["15", "15 miles"],
        "The y-coordinate represents distance in miles: 15 miles.",
        "15 miles.",
        "15.",
        "(3, 15) means 15 miles in 3 hours."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In the graph from Q01, what does the x-coordinate 3 represent?",
        "3 hours of travel time",
        ["3 miles of distance", "3 miles per hour", "3 stops"],
        "The x-axis represents time in hours: 3 hours.",
        "3 hours of travel time.",
        "3 hours of travel time.",
        "The x-coordinate represents the time (3 hours)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A plant\\'s height is recorded: (Day 1, 2 cm), (Day 2, 4 cm), (Day 3, 6 cm). How tall in cm will the plant be on Day 5 if this linear trend continues?",
        10, ["10", "10 cm"],
        "The plant grows 2 cm each day: height = 2 × Day. On Day 5: 2 × 5 = 10 cm.",
        "10 cm.",
        "10.",
        "2 × 5 = 10 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A map has the library at (2, 4) and school at (2, 9). What is the distance between them?",
        "5 units",
        ["4 units", "9 units", "7 units"],
        "Same x-coordinate: distance = 9 - 4 = 5 units.",
        "5 units.",
        "5 units.",
        "9 - 4 = 5 units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Sam saves money each week: (Week 1, $10), (Week 2, $20), (Week 3, $30). How much money in dollars will Sam have saved in Week 6?",
        60, ["60", "$60"],
        "Savings = 10 × Week. In Week 6: 10 × 6 = $60.",
        "$60.",
        "60.",
        "10 × 6 = $60."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A taxi charges according to the points: (1 mile, $5), (2 miles, $8), (3 miles, $11). Following this rule (charge = 3 × miles + 2), how much does a 5-mile ride cost in dollars?",
        17, ["17", "$17"],
        "Cost = 3 × 5 + 2 = 15 + 2 = $17.",
        "$17.",
        "17.",
        "3 × 5 + 2 = $17."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "On a grid, Maya walks from (1, 2) to (5, 2), then walks from (5, 2) to (5, 6). What is her total walking distance?",
        "8 units",
        ["6 units", "10 units", "4 units"],
        "Horizontal distance: 5 - 1 = 4. Vertical distance: 6 - 2 = 4. Total = 4 + 4 = 8 units.",
        "8 units.",
        "8 units.",
        "4 + 4 = 8 units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A car travels at 50 mph: (1 hr, 50 mi), (2 hr, 100 mi). How many miles does it travel in 4 hours?",
        200, ["200", "200 miles"],
        "50 × 4 = 200 miles.",
        "200 miles.",
        "200.",
        "50 × 4 = 200 miles."
    ))

    # =========================================================================
    # LESSON 23: Properties of 2D Figures (5.G.B.3)
    # =========================================================================
    LID = "G5_L23"
    LT = "Properties of 2D Figures"
    DOM = "Geometry & Graphs"
    STD = "5.G.B.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "If all rectangles have 4 right angles, and all squares are rectangles, what must be true about all squares?",
        "All squares have 4 right angles",
        ["Squares have no right angles", "Squares have acute angles", "Only some squares have right angles"],
        "Hierarchy of properties: All subcategories inherit all properties of the parent category.",
        "All squares have 4 right angles.",
        "All squares have 4 right angles.",
        "Squares inherit all attributes of rectangles, including 4 right angles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which statement is always true about parallelograms?",
        "Opposite sides are parallel and equal in length",
        ["All 4 sides are always equal", "All 4 angles are always 90°", "There is only 1 pair of parallel sides"],
        "Parallelograms have two pairs of parallel opposite congruent sides.",
        "Opposite sides are parallel and equal.",
        "Opposite sides are parallel and equal in length.",
        "Parallelograms have two pairs of parallel, equal sides."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Is every rhombus a parallelogram?",
        "Yes, because a rhombus has two pairs of parallel opposite sides",
        ["No, because a rhombus has sides of different lengths", "No, because a rhombus cannot have right angles", "Only if it is a trapezoid"],
        "A rhombus is defined as a parallelogram with 4 equal sides.",
        "Yes.",
        "Yes, because a rhombus has two pairs of parallel opposite sides.",
        "Every rhombus is a parallelogram."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which attribute is shared by ALL quadrilaterals?",
        "They all have exactly 4 sides and 4 angles",
        ["They all have 4 right angles", "They all have parallel sides", "They all have equal sides"],
        "The defining attribute of any quadrilateral is having 4 sides and 4 interior angles.",
        "4 sides and 4 angles.",
        "They all have exactly 4 sides and 4 angles.",
        "All quadrilaterals have 4 sides and 4 angles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the sum of the interior angle measures of any quadrilateral in degrees?",
        360, ["360", "360°", "360 degrees"],
        "Any quadrilateral can be split into 2 triangles: 2 × 180° = 360°.",
        "360°.",
        "360.",
        "The interior angles of any quadrilateral sum to 360°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Why is a square also considered a rhombus?",
        "Because a square has 4 sides of equal length",
        ["Because a square has no right angles", "Because a square has only 1 pair of parallel sides", "It is not a rhombus"],
        "A rhombus is any quadrilateral with 4 equal sides; squares have 4 equal sides.",
        "It has 4 equal sides.",
        "Because a square has 4 sides of equal length.",
        "A square meets the definition of a rhombus (4 equal sides)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following figures does NOT have to have opposite sides that are parallel?",
        "Trapezoid",
        ["Rectangle", "Rhombus", "Square"],
        "A trapezoid only has ONE pair of parallel sides (not both opposite pairs).",
        "Trapezoid.",
        "Trapezoid.",
        "A trapezoid has only one pair of parallel sides."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "How many pairs of parallel sides does a rectangle have?",
        2, ["2", "2 pairs"],
        "A rectangle has 2 pairs of parallel opposite sides.",
        "2 pairs.",
        "2.",
        "A rectangle has 2 pairs of parallel sides."
    ))

    # =========================================================================
    # LESSON 24: Classifying Shapes (5.G.B.4)
    # =========================================================================
    LID = "G5_L24"
    LT = "Classifying Shapes"
    DOM = "Geometry & Graphs"
    STD = "5.G.B.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A triangle with all three sides of different lengths is called a:",
        "Scalene triangle",
        ["Equilateral triangle", "Isosceles triangle", "Right triangle"],
        "Scalene triangles have no equal sides.",
        "Scalene triangle.",
        "Scalene triangle.",
        "A triangle with no equal sides is scalene."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A triangle with at least two sides of equal length is called an:",
        "Isosceles triangle",
        ["Scalene triangle", "Right triangle", "Obtuse triangle"],
        "Isosceles triangles have at least 2 equal sides.",
        "Isosceles triangle.",
        "Isosceles triangle.",
        "An isosceles triangle has at least two equal sides."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In a hierarchy of quadrilaterals, which shape belongs inside the category of BOTH rectangles and rhombuses?",
        "Square",
        ["Trapezoid", "Parallelogram", "Kite"],
        "A square has 4 right angles (rectangle) and 4 equal sides (rhombus).",
        "Square.",
        "Square.",
        "The square is the intersection of rectangles and rhombuses."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the sum of the interior angle measures of any triangle in degrees?",
        180, ["180", "180°", "180 degrees"],
        "The angles of any triangle always add up to 180°.",
        "180°.",
        "180.",
        "Angle sum of a triangle is 180°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Can a triangle have more than one right angle?",
        "No, because two 90° angles would already equal 180°, leaving 0° for the third angle",
        ["Yes, any triangle can", "Yes, an equilateral triangle can", "Only in an isosceles triangle"],
        "180° total: 90° + 90° = 180°, so a triangle can have at most one right angle.",
        "No.",
        "No, because two 90° angles would already equal 180°, leaving 0° for the third angle.",
        "A triangle can have only one right angle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which category includes all the others: Quadrilaterals, Squares, Parallelograms, Rectangles?",
        "Quadrilaterals",
        ["Parallelograms", "Rectangles", "Squares"],
        "All squares are rectangles; all rectangles are parallelograms; all parallelograms are quadrilaterals.",
        "Quadrilaterals.",
        "Quadrilaterals.",
        "Quadrilaterals is the broadest category containing all 4-sided polygons."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "An isosceles triangle has two angles that each measure 50°. What is the measure of the third angle in degrees? (180 - 100)",
        80, ["80", "80°", "80 degrees"],
        "180 - (50 + 50) = 180 - 100 = 80°.",
        "80°.",
        "80.",
        "180° - 100° = 80°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Which type of triangle has all angles measuring less than 90°?",
        "Acute triangle",
        ["Right triangle", "Obtuse triangle", "Scalene triangle"],
        "An acute triangle has all three angles acute (< 90°).",
        "Acute triangle.",
        "Acute triangle.",
        "An acute triangle has three acute angles."
    ))

    # =========================================================================
    # LESSON 25: Cumulative Word Problems (5.MP.1--5.MP.8)
    # =========================================================================
    LID = "G5_L25"
    LT = "Cumulative Word Problems"
    DOM = "Geometry & Graphs"
    STD = "5.MP.1--5.MP.8"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A community garden has 4 plots. Each plot is 6.5 meters long and 4 meters wide. What is the total area of all 4 plots in square meters?",
        104, ["104", "104 sq m"],
        "Area of one plot = 6.5 × 4 = 26 sq m. For 4 plots: 26 × 4 = 104 sq m.",
        "104 sq m.",
        "104.",
        "4 × (6.5 × 4) = 104 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A water tank had 40.5 liters. 12.75 liters were drained in the morning and 8.25 liters in the evening. How many liters remain in the tank?",
        "19.5 liters",
        ["18.5 liters", "20.5 liters", "21.0 liters"],
        "Total drained = 12.75 + 8.25 = 21.0 liters. Remaining = 40.5 - 21.0 = 19.5 liters.",
        "19.5 liters.",
        "19.5 liters.",
        "40.5 - (12.75 + 8.25) = 19.5 L."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A baker had 12 pounds of flour. He used 2/3 of it for bread. How many pounds of flour did he use?",
        8, ["8", "8 pounds"],
        "12 × 2/3 = 24/3 = 8 pounds.",
        "8 pounds.",
        "8.",
        "12 × 2/3 = 8 pounds."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A rectangular prism fish tank has a base of 30 cm by 20 cm and water filled to a height of 15 cm. What is the volume of water in cubic cm?",
        "9,000 cm³",
        ["6,000 cm³", "8,000 cm³", "12,000 cm³"],
        "V = 30 × 20 × 15 = 600 × 15 = 9,000 cm³.",
        "9,000 cm³.",
        "9,000 cm³.",
        "30 × 20 × 15 = 9,000 cm³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Evaluate: [4 × (10 - 2)] + [15 ÷ (2 + 3)].",
        35, ["35"],
        "Left: 4 × 8 = 32. Right: 15 ÷ 5 = 3. Add: 32 + 3 = 35.",
        "35.",
        "35.",
        "32 + 3 = 35."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A runner jogs 3 and 1/4 miles on Saturday and 2 and 5/8 miles on Sunday. What is the total miles jogged? (Enter improper fraction numerator over 8)",
        47, ["47"],
        "3 2/8 + 2 5/8 = 5 7/8 = 47/8 miles. Numerator is 47.",
        "47.",
        "47.",
        "5 7/8 = 47/8, numerator is 47."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A classroom raised $350 for charity. They bought 25 gift packages for $12 each. How much money remains?",
        "$50",
        ["$40", "$60", "$70"],
        "25 × 12 = $300. Remaining = $350 - $300 = $50.",
        "$50.",
        "$50.",
        "$350 - $300 = $50."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 0.75 × 10³.",
        750, ["750"],
        "0.75 × 1,000 = 750.",
        "750.",
        "750.",
        "0.75 × 1,000 = 750."
    ))

    return questions
'''

with open('scripts/builders/grade_5.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated scripts/builders/grade_5.py successfully!")
