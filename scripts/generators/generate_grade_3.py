"""
scripts/generators/generate_grade_3.py
Script to generate the complete Grade 3 curriculum questions builder.
"""
import os

code = '''"""
scripts/builders/grade_3.py
High-fidelity mathematical question builder for Grade 3 (Lessons 1-25).
100% verified math answers, child-friendly prompts, and progressive 3-tier hints.
"""

from scripts.builders.helpers import make_numeric_question, make_mc_question

def build_grade_3_questions():
    questions = []
    G = 3

    # =========================================================================
    # LESSON 1: Understanding Multiplication (3.OA.A.1)
    # =========================================================================
    LID = "G3_L01"
    LT = "Understanding Multiplication"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Maya has 4 baskets. She places 5 apples in each basket. How many apples does Maya have in total?",
        20, ["20", "20 apples"],
        "Multiplication represents equal groups of items. Total = (number of groups) × (items in each group).",
        "Add 5 four times: 5 + 5 + 5 + 5, or calculate 4 × 5.",
        "4 × 5 = 20 apples.",
        "Maya has 4 groups of 5 apples. 4 × 5 = 20 apples."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which repeated addition sentence represents 3 × 6?",
        "6 + 6 + 6 = 18",
        ["3 + 6 = 9", "3 + 3 + 3 = 9", "6 + 3 + 6 = 15"],
        "3 × 6 means 3 groups of 6.",
        "Write 6 added together 3 times.",
        "6 + 6 + 6 = 18.",
        "3 × 6 means 3 groups with 6 in each group: 6 + 6 + 6 = 18."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A dog has 4 legs. If there are 6 dogs playing in the dog park, how many total legs are there?",
        24, ["24", "24 legs"],
        "Multiply the number of items per group by the total number of groups.",
        "There are 6 dogs, and each dog has 4 legs. Multiply 6 × 4.",
        "6 × 4 = 24 legs.",
        "6 dogs with 4 legs each: 6 × 4 = 24 legs."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "An array has 3 rows of stars with 5 stars in each row. Which multiplication equation models this array?",
        "3 × 5 = 15",
        ["3 + 5 = 8", "5 - 3 = 2", "3 × 3 = 9"],
        "An array arranges objects into equal rows and columns. Total = (rows) × (columns).",
        "There are 3 rows and 5 columns.",
        "3 rows × 5 columns = 15 stars in total.",
        "An array with 3 rows of 5 stars has 3 × 5 = 15 stars."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Leo planted seeds in an egg carton with 2 rows and 6 columns. How many total seeds did Leo plant?",
        12, ["12", "12 seeds"],
        "To find the total in a grid, multiply the number of rows by the number of columns.",
        "Calculate 2 rows × 6 columns.",
        "2 × 6 = 12 seeds.",
        "2 rows × 6 columns = 12 total seeds."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Sofia bakes 7 trays of cookies. Each tray holds 4 cookies. How many cookies did Sofia bake in total?",
        28, ["28", "28 cookies"],
        "Total items = (number of trays) × (cookies per tray).",
        "Multiply 7 by 4.",
        "7 × 4 = 28 cookies.",
        "7 trays × 4 cookies per tray = 28 cookies."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which story problem represents the equation 5 × 8 = 40?",
        "Liam bought 5 packs of markers with 8 markers in each pack.",
        ["Liam had 5 markers and found 8 more.", "Liam had 40 markers and gave 8 to a friend.", "Liam shared 5 markers equally among 8 friends."],
        "Multiplication represents combining equal groups.",
        "Look for the situation with 5 equal groups of 8 items.",
        "5 packs of 8 markers means 5 × 8 = 40 markers.",
        "5 packs with 8 markers each is 5 equal groups of 8: 5 × 8 = 40."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A classroom has 8 tables. Each table has 3 chairs. How many chairs are in the classroom altogether?",
        24, ["24", "24 chairs"],
        "Multiply the number of groups by the size of each group.",
        "Multiply 8 tables by 3 chairs per table.",
        "8 × 3 = 24 chairs.",
        "8 tables × 3 chairs = 24 chairs."
    ))

    # =========================================================================
    # LESSON 2: Multiplication on a Number Line (3.OA.A.3)
    # =========================================================================
    LID = "G3_L02"
    LT = "Multiplication on a Number Line"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A frog starts at 0 and takes 4 jumps of size 3 on a number line. At what number does the frog land?",
        12, ["12"],
        "Jumping on a number line models multiplication: (number of jumps) × (jump size).",
        "Calculate 4 × 3.",
        "0 + 3 + 3 + 3 + 3 = 12.",
        "4 jumps of 3 = 4 × 3 = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A grasshopper takes 5 jumps of size 2 on a number line. Which equation models these jumps?",
        "5 × 2 = 10",
        ["5 + 2 = 7", "2 × 2 = 4", "5 × 5 = 25"],
        "The number of jumps is the first factor; the jump size is the second factor.",
        "5 jumps of 2 units each equals 5 × 2.",
        "5 jumps of 2 lands on 10, so 5 × 2 = 10.",
        "5 jumps of size 2 is represented by 5 × 2 = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rabbit jumps from 0 to 18 on a number line by making equal jumps of 6. How many jumps did the rabbit make?",
        3, ["3", "3 jumps"],
        "Divide the ending number by the size of each jump: (Total distance) ÷ (jump size) = (number of jumps).",
        "Calculate 18 ÷ 6.",
        "6, 12, 18 is 3 jumps.",
        "18 ÷ 6 = 3 jumps of size 6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Kiran makes 6 jumps of size 4 on a number line. What is Kiran\\'s landing point?",
        24, ["24"],
        "Landing point = (jumps) × (jump size).",
        "Multiply 6 by 4.",
        "6 × 4 = 24.",
        "6 jumps of 4 units = 6 × 4 = 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "On a number line, if you start at 0 and make 7 jumps of 5, what number do you reach?",
        "35",
        ["30", "40", "12"],
        "Skip count by 5 seven times: 5, 10, 15, 20, 25, 30, 35.",
        "7 × 5 = 35.",
        "7 jumps of 5 = 35.",
        "7 jumps of 5 is 7 × 5 = 35."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A cricket makes 8 jumps of size 4 on a number line starting at 0. Where is the cricket now?",
        32, ["32"],
        "Multiply the number of jumps by the distance per jump.",
        "8 jumps of 4 = 8 × 4.",
        "8 × 4 = 32.",
        "8 × 4 = 32 on the number line."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which number line jump pattern shows 9 × 3 = 27?",
        "9 jumps of size 3 starting at 0",
        ["3 jumps of size 9 starting at 10", "9 jumps of size 2 starting at 0", "27 jumps of size 1 starting at 3"],
        "The first number is the number of jumps, and the second is the jump length.",
        "9 jumps of 3 units equals 27.",
        "9 jumps of 3 starting at 0 models 9 × 3 = 27.",
        "9 jumps of size 3 equals 27."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If you make jumps of size 7 starting at 0 and reach 42, how many jumps did you make?",
        6, ["6", "6 jumps"],
        "To find the number of jumps: (final number) ÷ (jump size).",
        "Calculate 42 ÷ 7.",
        "42 ÷ 7 = 6.",
        "42 ÷ 7 = 6 jumps."
    ))

    # =========================================================================
    # LESSON 3: Commutative & Associative Properties (3.OA.B.5)
    # =========================================================================
    LID = "G3_L03"
    LT = "Commutative & Associative Properties"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.B.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "According to the Commutative Property of Multiplication, if 4 × 7 = 28, then 7 × 4 = ?",
        28, ["28"],
        "The Commutative Property states that changing the order of factors does not change the product: a × b = b × a.",
        "4 × 7 has the same product as 7 × 4.",
        "7 × 4 = 28.",
        "By the Commutative Property, 7 × 4 = 4 × 7 = 28."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which equation illustrates the Commutative Property of Multiplication?",
        "3 × 8 = 8 × 3",
        ["3 + 8 = 8 + 3", "(2 × 3) × 4 = 2 × (3 × 4)", "3 × 1 = 3"],
        "The Commutative Property of Multiplication switches the order of factors in multiplication.",
        "Look for multiplication where the numbers swap places across the equals sign.",
        "3 × 8 = 8 × 3 is the Commutative Property of Multiplication.",
        "3 × 8 = 8 × 3 demonstrates the Commutative Property."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Use the Associative Property: (2 × 3) × 5 = 2 × (3 × 5). What is the product?",
        30, ["30"],
        "The Associative Property states that grouping factors differently does not change the product: (a × b) × c = a × (b × c).",
        "Calculate inside first: 2 × 3 = 6, then 6 × 5 = 30; or 3 × 5 = 15, then 2 × 15 = 30.",
        "Both equal 30.",
        "(2 × 3) × 5 = 6 × 5 = 30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What number makes this equation true: (4 × 2) × 3 = 4 × (? × 3)?",
        "2",
        ["3", "4", "6"],
        "The Associative Property regroups the exact same factors: (a × b) × c = a × (b × c).",
        "Compare the factors: 4, 2, and 3 are in both expressions.",
        "The missing factor inside the parentheses is 2.",
        "By the Associative Property, the missing factor is 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Calculate (5 × 2) × 7 using mental math by grouping 5 × 2 first. What is the result?",
        70, ["70"],
        "Multiply (5 × 2) first to get an easy multiple of 10.",
        "5 × 2 = 10. Now multiply 10 × 7.",
        "10 × 7 = 70.",
        "(5 × 2) × 7 = 10 × 7 = 70."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If 9 × 6 = 54, find the missing number in: 6 × ___ = 54.",
        9, ["9"],
        "Commutative property: a × b = b × a.",
        "Since 9 × 6 = 54, then 6 × 9 = 54.",
        "The missing number is 9.",
        "By the Commutative Property, 6 × 9 = 54."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following is equal to 4 × (2 × 5)?",
        "(4 × 2) × 5",
        ["(4 + 2) + 5", "4 × 2 + 5", "(4 × 5) + 2"],
        "The Associative Property allows changing parentheses grouping in multiplication.",
        "4 × (2 × 5) = (4 × 2) × 5.",
        "(4 × 2) × 5 = 8 × 5 = 40, which matches 4 × 10 = 40.",
        "By the Associative Property, 4 × (2 × 5) = (4 × 2) × 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate (3 × 3) × 4. What is the value?",
        36, ["36"],
        "Evaluate inside parentheses first, then multiply by the remaining factor.",
        "3 × 3 = 9, then multiply 9 × 4.",
        "9 × 4 = 36.",
        "(3 × 3) × 4 = 9 × 4 = 36."
    ))

    # =========================================================================
    # LESSON 4: Understanding Division (3.OA.A.2)
    # =========================================================================
    LID = "G3_L04"
    LT = "Understanding Division"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A teacher shares 15 crayons equally among 3 students. How many crayons does each student receive?",
        5, ["5", "5 crayons"],
        "Division is equal sharing: (total items) ÷ (number of groups) = (items per group).",
        "Calculate 15 ÷ 3.",
        "15 ÷ 3 = 5 crayons.",
        "15 crayons divided among 3 students: 15 ÷ 3 = 5 crayons."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "There are 18 cookies. Mom puts 3 cookies into each bag. How many bags does she fill?",
        "6 bags",
        ["5 bags", "7 bags", "9 bags"],
        "Division by grouping: (total items) ÷ (items in each group) = (number of groups).",
        "Divide 18 by 3.",
        "18 ÷ 3 = 6 bags.",
        "18 ÷ 3 = 6 bags."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Marcus has 24 stickers. He puts an equal number on each of 4 pages. How many stickers are on each page?",
        6, ["6", "6 stickers"],
        "Divide total stickers by the number of pages.",
        "Calculate 24 ÷ 4.",
        "24 ÷ 4 = 6 stickers.",
        "24 stickers ÷ 4 pages = 6 stickers per page."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which division equation represents sharing 20 marbles equally among 5 friends?",
        "20 ÷ 5 = 4",
        ["20 - 5 = 15", "5 × 4 = 20", "20 ÷ 4 = 5"],
        "Total items is the dividend (first number), groups is the divisor (second number).",
        "20 shared among 5 friends is written as 20 ÷ 5.",
        "20 ÷ 5 = 4.",
        "20 ÷ 5 = 4 represents 20 marbles shared among 5 friends."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 28 ÷ 7.",
        4, ["4"],
        "Think of multiplication: What number times 7 equals 28?",
        "7 × 4 = 28, so 28 ÷ 7 = 4.",
        "28 ÷ 7 = 4.",
        "28 ÷ 7 = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A baker packs 36 muffins into boxes of 6. How many boxes of muffins does the baker make?",
        6, ["6", "6 boxes"],
        "Divide total muffins by muffins per box.",
        "Calculate 36 ÷ 6.",
        "36 ÷ 6 = 6 boxes.",
        "36 ÷ 6 = 6 boxes."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If you have 35 tennis balls and put 5 balls into each can, which equation tells you the number of cans?",
        "35 ÷ 5 = 7",
        ["35 - 5 = 30", "35 + 5 = 40", "5 × 7 = 35"],
        "Find how many equal groups of 5 are in 35.",
        "35 divided by 5 equals 7.",
        "35 ÷ 5 = 7 cans.",
        "35 ÷ 5 = 7 is the correct division equation."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "There are 40 students going on a field trip. If 4 students ride in each van, how many vans are needed?",
        10, ["10", "10 vans"],
        "Divide the total number of students by the number per van.",
        "40 ÷ 4 = 10.",
        "10 vans are needed.",
        "40 ÷ 4 = 10 vans."
    ))

    # =========================================================================
    # LESSON 5: Multiplication & Division Relationships (3.OA.B.6)
    # =========================================================================
    LID = "G3_L05"
    LT = "Multiplication & Division Relationships"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.B.6"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the missing number in the fact family: 6 × ___ = 42.",
        7, ["7"],
        "Multiplication and division are inverse operations. If 6 × ? = 42, then 42 ÷ 6 = ?.",
        "Calculate 42 ÷ 6.",
        "42 ÷ 6 = 7.",
        "6 × 7 = 42, so the missing number is 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which equation belongs to the same fact family as 4 × 8 = 32?",
        "32 ÷ 8 = 4",
        ["4 + 8 = 12", "32 - 8 = 24", "4 × 4 = 16"],
        "A fact family consists of related facts using the same three numbers (4, 8, 32).",
        "The related division equations are 32 ÷ 8 = 4 and 32 ÷ 4 = 8.",
        "32 ÷ 8 = 4 belongs to this fact family.",
        "32 ÷ 8 = 4 is an inverse relationship in the fact family."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the missing value: ___ ÷ 5 = 9?",
        45, ["45"],
        "To find the dividend, multiply the divisor by the quotient: ? = 5 × 9.",
        "Calculate 5 × 9.",
        "5 × 9 = 45.",
        "45 ÷ 5 = 9, so the missing value is 45."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Find the unknown factor: 8 × ___ = 64.",
        8, ["8"],
        "Divide 64 by 8 to find the unknown factor.",
        "64 ÷ 8 = 8.",
        "8 × 8 = 64.",
        "8 × 8 = 64."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "If you know that 7 × 9 = 63, what is 63 ÷ 7?",
        "9",
        ["7", "8", "10"],
        "Multiplication and division undo each other.",
        "Since 7 × 9 = 63, 63 ÷ 7 must be 9.",
        "63 ÷ 7 = 9.",
        "63 ÷ 7 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the value of k in: 54 ÷ k = 6.",
        9, ["9"],
        "Think: 6 × k = 54. What number times 6 gives 54?",
        "54 ÷ 6 = 9.",
        "k = 9.",
        "54 ÷ 9 = 6, so k = 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which number sentence can help you solve 48 ÷ 6 = ___?",
        "6 × ___ = 48",
        ["6 + ___ = 48", "48 - 6 = ___", "48 × 6 = ___"],
        "Division can be solved as an unknown-factor multiplication problem.",
        "48 ÷ 6 = ? means 6 × ? = 48.",
        "6 × 8 = 48, so 48 ÷ 6 = 8.",
        "6 × ___ = 48 is the corresponding multiplication sentence."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve for n: n × 7 = 56.",
        8, ["8"],
        "Divide 56 by 7 to find n.",
        "56 ÷ 7 = 8.",
        "n = 8.",
        "8 × 7 = 56, so n = 8."
    ))

    # =========================================================================
    # LESSON 6: Facts for 2s, 5s, and 10s (3.OA.C.7)
    # =========================================================================
    LID = "G3_L06"
    LT = "Facts for 2s, 5s, and 10s"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: 7 × 2.",
        14, ["14"],
        "Multiplying by 2 means doubling the number.",
        "7 + 7 = 14.",
        "7 × 2 = 14.",
        "7 × 2 = 14."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which product is equal to 9 × 5?",
        "45",
        ["40", "50", "35"],
        "Multiples of 5 always end in 0 or 5.",
        "Count by 5 nine times: 5, 10, 15, 20, 25, 30, 35, 40, 45.",
        "9 × 5 = 45.",
        "9 × 5 = 45."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 8 × 10.",
        80, ["80"],
        "Multiplying a whole number by 10 appends a 0 to the ones place.",
        "8 with a 0 at the end is 80.",
        "8 × 10 = 80.",
        "8 × 10 = 80."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is 50 ÷ 5?",
        "10",
        ["5", "15", "25"],
        "Think: 5 times what number equals 50?",
        "5 × 10 = 50.",
        "50 ÷ 5 = 10.",
        "50 ÷ 5 = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 18 ÷ 2.",
        9, ["9"],
        "Dividing by 2 is cutting in half.",
        "Half of 18 is 9.",
        "18 ÷ 2 = 9.",
        "18 ÷ 2 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Calculate: 6 × 5.",
        30, ["30"],
        "Skip count by 5 six times.",
        "5, 10, 15, 20, 25, 30.",
        "6 × 5 = 30.",
        "6 × 5 = 30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is 70 ÷ 10?",
        "7",
        ["10", "6", "8"],
        "Dividing by 10 removes a zero from the ones place.",
        "70 ÷ 10 = 7.",
        "70 ÷ 10 = 7.",
        "70 ÷ 10 = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 12 × 5.",
        60, ["60"],
        "Break 12 into (10 + 2): (10 × 5) + (2 × 5).",
        "50 + 10 = 60.",
        "12 × 5 = 60.",
        "12 × 5 = 60."
    ))

    # =========================================================================
    # LESSON 7: Facts for 3s, 4s, and 6s (3.OA.C.7)
    # =========================================================================
    LID = "G3_L07"
    LT = "Facts for 3s, 4s, and 6s"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: 6 × 3.",
        18, ["18"],
        "Count by 3 six times or count by 6 three times.",
        "6 + 6 + 6 = 18.",
        "6 × 3 = 18.",
        "6 × 3 = 18."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is 7 × 4?",
        "28",
        ["24", "32", "21"],
        "To multiply by 4, double the number twice.",
        "Double 7 is 14; double 14 is 28.",
        "7 × 4 = 28.",
        "7 × 4 = 28."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 9 × 4.",
        36, ["36"],
        "Multiply 9 by 4: double 9 is 18, double 18 is 36.",
        "9 × 4 = 36.",
        "9 × 4 = 36.",
        "9 × 4 = 36."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is 24 ÷ 6?",
        "4",
        ["3", "6", "8"],
        "Think: 6 × ? = 24.",
        "6 × 4 = 24.",
        "24 ÷ 6 = 4.",
        "24 ÷ 6 = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 36 ÷ 4.",
        9, ["9"],
        "Think: 4 times what equals 36?",
        "4 × 9 = 36.",
        "36 ÷ 4 = 9.",
        "36 ÷ 4 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Calculate: 8 × 6.",
        48, ["48"],
        "Use 8 × 5 = 40, then add one more 8.",
        "40 + 8 = 48.",
        "8 × 6 = 48.",
        "8 × 6 = 48."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is 27 ÷ 3?",
        "9",
        ["8", "7", "6"],
        "Think: 3 × ? = 27.",
        "3 × 9 = 27.",
        "27 ÷ 3 = 9.",
        "27 ÷ 3 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 7 × 6.",
        42, ["42"],
        "Use 7 × 5 = 35 and add 7.",
        "35 + 7 = 42.",
        "7 × 6 = 42.",
        "7 × 6 = 42."
    ))

    # =========================================================================
    # LESSON 8: Facts for 7s, 8s, and 9s (3.OA.C.7)
    # =========================================================================
    LID = "G3_L08"
    LT = "Facts for 7s, 8s, and 9s"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: 7 × 7.",
        49, ["49"],
        "7 squared equals 49.",
        "7 groups of 7 = 49.",
        "7 × 7 = 49.",
        "7 × 7 = 49."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is 8 × 7?",
        "56",
        ["54", "58", "64"],
        "Remember the sequence: 5, 6, 7, 8 -> 56 = 7 × 8.",
        "7 × 8 = 56.",
        "8 × 7 = 56.",
        "8 × 7 = 56."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Calculate: 9 × 8.",
        72, ["72"],
        "For 9 facts, the digits add up to 9: 7 + 2 = 9.",
        "10 × 8 = 80, subtract 8 = 72.",
        "9 × 8 = 72.",
        "9 × 8 = 72."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is 63 ÷ 7?",
        "9",
        ["7", "8", "6"],
        "Think: 7 × ? = 63.",
        "7 × 9 = 63.",
        "63 ÷ 7 = 9.",
        "63 ÷ 7 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 81 ÷ 9.",
        9, ["9"],
        "9 × 9 = 81.",
        "81 divided by 9 equals 9.",
        "81 ÷ 9 = 9.",
        "81 ÷ 9 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Calculate: 9 × 9.",
        81, ["81"],
        "9 squared equals 81.",
        "10 × 9 = 90, subtract 9 = 81.",
        "9 × 9 = 81.",
        "9 × 9 = 81."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is 64 ÷ 8?",
        "8",
        ["7", "9", "6"],
        "8 × 8 = 64.",
        "64 ÷ 8 = 8.",
        "64 ÷ 8 = 8.",
        "64 ÷ 8 = 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 8 × 8.",
        64, ["64"],
        "8 squared equals 64.",
        "8 × 8 = 64.",
        "8 × 8 = 64.",
        "8 × 8 = 64."
    ))

    # =========================================================================
    # LESSON 9: Two-Step Word Problems (3.OA.D.8)
    # =========================================================================
    LID = "G3_L09"
    LT = "Two-Step Word Problems"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.D.8"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Chloe bought 3 packs of gum with 5 pieces in each pack. She chewed 4 pieces. How many pieces of gum are left?",
        11, ["11", "11 pieces"],
        "Two-step problem: First multiply to find the total, then subtract the chewed pieces.",
        "Step 1: 3 × 5 = 15 pieces. Step 2: 15 - 4.",
        "15 - 4 = 11 pieces.",
        "Total gum = 3 × 5 = 15. Remaining = 15 - 4 = 11 pieces."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Maya has 4 boxes with 6 crayons each. Her teacher gives her 8 more crayons. How many crayons does Maya have now?",
        "32 crayons",
        ["24 crayons", "28 crayons", "36 crayons"],
        "First find crayons in boxes (4 × 6), then add the extra crayons (+ 8).",
        "4 × 6 = 24. 24 + 8 = 32.",
        "32 crayons in total.",
        "4 × 6 = 24 crayons in boxes. 24 + 8 = 32 crayons altogether."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A bakery baked 50 muffins. They sold 26 muffins in the morning and 14 muffins in the afternoon. How many muffins are left?",
        10, ["10", "10 muffins"],
        "Find the total muffins sold by adding morning and afternoon sales, then subtract from 50.",
        "26 + 14 = 40 sold. 50 - 40 = ?",
        "50 - 40 = 10 muffins.",
        "Total sold = 26 + 14 = 40. Remaining = 50 - 40 = 10 muffins."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Jake had $40. He bought 3 books that cost $7 each. How much money does Jake have left?",
        "$19",
        ["$21", "$17", "$23"],
        "First multiply 3 books by $7 to get total cost. Then subtract cost from $40.",
        "3 × 7 = $21. $40 - $21 = $19.",
        "Jake has $19 left.",
        "Cost of books = 3 × $7 = $21. Remaining money = $40 - $21 = $19."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Emma has 2 bags with 8 apples in each bag. She shares all of her apples equally among 4 friends. How many apples does each friend get?",
        4, ["4", "4 apples"],
        "Step 1: Total apples = 2 × 8. Step 2: Divide total by 4 friends.",
        "2 × 8 = 16 apples. 16 ÷ 4 = ?",
        "16 ÷ 4 = 4 apples.",
        "Total apples = 2 × 8 = 16. Apples per friend = 16 ÷ 4 = 4 apples."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A grocer puts 5 boxes of apples on display with 6 apples in each box. If 3 apples are damaged and removed, how many apples are left?",
        27, ["27", "27 apples"],
        "Find total apples first (5 × 6), then subtract the 3 damaged apples.",
        "5 × 6 = 30. 30 - 3 = 27.",
        "27 apples.",
        "5 × 6 = 30 apples. 30 - 3 = 27 good apples."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Noah collected 18 shells. His brother collected 14 shells. They put all of their shells equally into 4 jars. How many shells are in each jar?",
        "8 shells",
        ["7 shells", "6 shells", "9 shells"],
        "First add all shells (18 + 14 = 32), then divide by 4 jars.",
        "18 + 14 = 32 shells. 32 ÷ 4 = 8 shells.",
        "8 shells per jar.",
        "Total shells = 18 + 14 = 32. Per jar = 32 ÷ 4 = 8 shells."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "4 baskets have 8 oranges each. If 12 oranges are squeezed to make fresh juice, how many oranges remain?",
        20, ["20", "20 oranges"],
        "Calculate total oranges: 4 × 8 = 32. Subtract oranges used: 32 - 12.",
        "32 - 12 = 20 oranges.",
        "20 oranges.",
        "Total oranges = 4 × 8 = 32. Remaining = 32 - 12 = 20 oranges."
    ))

    # =========================================================================
    # LESSON 10: Identifying Arithmetic Patterns (3.OA.D.9)
    # =========================================================================
    LID = "G3_L10"
    LT = "Identifying Arithmetic Patterns"
    DOM = "Operations & Algebraic Thinking"
    STD = "3.OA.D.9"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the next number in the arithmetic pattern: 4, 8, 12, 16, ___?",
        20, ["20"],
        "Find the rule: subtract consecutive terms to find the step size.",
        "8 - 4 = 4; the pattern adds 4 each time. 16 + 4 = ?",
        "16 + 4 = 20.",
        "The pattern increases by 4 each term. 16 + 4 = 20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "When you multiply any whole number by an even number, what kind of product do you always get?",
        "An even number",
        ["An odd number", "A prime number", "Zero"],
        "Even numbers have 2 as a factor. Any multiple of an even number also has 2 as a factor.",
        "Try examples: 3 × 2 = 6 (even), 5 × 4 = 20 (even).",
        "The product is always even.",
        "Multiplying any number by an even number always produces an even number."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In the addition pattern, adding two odd numbers always gives an even number. What is the sum of 5 + 7?",
        12, ["12"],
        "Odd + Odd = Even.",
        "5 + 7 = 12.",
        "12 is an even number.",
        "5 + 7 = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the rule for the pattern: 6, 12, 18, 24, 30?",
        "Add 6",
        ["Add 4", "Multiply by 2", "Subtract 6"],
        "Check the difference between consecutive numbers: 12 - 6 = 6, 18 - 12 = 6.",
        "The rule adds 6 each time.",
        "The rule is 'Add 6'.",
        "Each term is 6 greater than the previous term, so the rule is Add 6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the next number in the pattern of multiples of 9: 9, 18, 27, 36, ___?",
        45, ["45"],
        "Add 9 to the last number: 36 + 9.",
        "36 + 9 = 45.",
        "45.",
        "Multiples of 9 increase by 9. 36 + 9 = 45."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "What is the next number in this decreasing pattern: 100, 90, 80, 70, ___?",
        60, ["60"],
        "Each step subtracts 10.",
        "70 - 10 = 60.",
        "60.",
        "The rule is subtract 10. 70 - 10 = 60."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following numbers belongs to the pattern of multiples of 4?",
        "28",
        ["25", "30", "35"],
        "Multiples of 4 are divisible by 4 with no remainder.",
        "28 ÷ 4 = 7 with no remainder.",
        "28 is a multiple of 4.",
        "28 = 4 × 7, so it belongs to the pattern of multiples of 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the missing number in the pattern: 3, 7, 11, ___, 19?",
        15, ["15"],
        "Find the difference: 7 - 3 = 4, 11 - 7 = 4. The pattern adds 4.",
        "11 + 4 = 15. Check: 15 + 4 = 19.",
        "15 is the missing number.",
        "Adding 4 to 11 gives 15, and 15 + 4 = 19."
    ))

    # =========================================================================
    # LESSON 11: Rounding Whole Numbers (3.NBT.A.1)
    # =========================================================================
    LID = "G3_L11"
    LT = "Rounding Whole Numbers"
    DOM = "Number & Operations in Base Ten"
    STD = "3.NBT.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Round 47 to the nearest 10.",
        50, ["50"],
        "Look at the ones digit. If it is 5 or greater, round up.",
        "The ones digit is 7, which is 5 or greater. Round 47 up to 50.",
        "50.",
        "47 is between 40 and 50, closer to 50. 47 rounds to 50."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Round 83 to the nearest 10.",
        "80",
        ["90", "85", "70"],
        "Look at the ones digit. If it is less than 5, round down.",
        "The ones digit is 3 (less than 5). Round down to 80.",
        "80.",
        "83 is closer to 80 than 90. 83 rounds to 80."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Round 364 to the nearest 100.",
        400, ["400"],
        "To round to the nearest hundred, look at the tens digit. If it is 5 or greater, round up.",
        "The tens digit is 6 (5 or greater). Round up to 400.",
        "400.",
        "364 is between 300 and 400, closer to 400. 364 rounds to 400."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Round 249 to the nearest 100.",
        "200",
        ["300", "250", "240"],
        "Look at the tens digit. The tens digit is 4.",
        "Since 4 is less than 5, round down to 200.",
        "200.",
        "249 is closer to 200 than 300 (just 1 away from 250). Rounds to 200."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Round 528 to the nearest 10.",
        530, ["530"],
        "To round to nearest ten, look at the ones digit. The ones digit is 8.",
        "Since 8 >= 5, round up: 520 becomes 530.",
        "530.",
        "528 rounds to 530 to the nearest ten."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Round 750 to the nearest 100.",
        800, ["800"],
        "When the tens digit is 5, round up to the next hundred.",
        "750 is halfway; by standard rounding rule, round up to 800.",
        "800.",
        "750 rounds up to 800."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following numbers rounds to 70 when rounded to the nearest 10?",
        "68",
        ["64", "76", "75"],
        "Numbers from 65 to 74 round to 70.",
        "68 is between 65 and 74.",
        "68 rounds to 70.",
        "68 rounds up to 70 because the ones digit 8 is >= 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Round 685 to the nearest 10.",
        690, ["690"],
        "Look at the ones digit: it is 5. Round up to the next ten.",
        "680 rounds up to 690.",
        "690.",
        "685 rounds up to 690."
    ))

    # =========================================================================
    # LESSON 12: Addition & Subtraction within 1000 (3.NBT.A.2)
    # =========================================================================
    LID = "G3_L12"
    LT = "Addition & Subtraction within 1000"
    DOM = "Number & Operations in Base Ten"
    STD = "3.NBT.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 345 + 228.",
        573, ["573"],
        "Add place by place starting from ones, regrouping when a sum is 10 or greater.",
        "5 + 8 = 13 (write 3, carry 1). 1 + 4 + 2 = 7. 3 + 2 = 5.",
        "573.",
        "345 + 228 = 573."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 512 - 187.",
        "325",
        ["335", "425", "315"],
        "Subtract place by place, regrouping across tens and hundreds when needed.",
        "Regroup 12 - 7 = 5. Regroup 10 - 8 = 2. 4 - 1 = 3.",
        "325.",
        "512 - 187 = 325."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 624 + 189.",
        813, ["813"],
        "Add ones: 4 + 9 = 13 (carry 1). Add tens: 1 + 2 + 8 = 11 (carry 1). Add hundreds: 1 + 6 + 1 = 8.",
        "813.",
        "813.",
        "624 + 189 = 813."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 700 - 342.",
        "358",
        ["368", "458", "348"],
        "Subtract across zeros by regrouping 700 as 6 hundreds, 9 tens, and 10 ones.",
        "10 - 2 = 8. 9 - 4 = 5. 6 - 3 = 3.",
        "358.",
        "700 - 342 = 358."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 456 + 378.",
        834, ["834"],
        "Add: 6 + 8 = 14 (carry 1). 1 + 5 + 7 = 13 (carry 1). 1 + 4 + 3 = 8.",
        "834.",
        "834.",
        "456 + 378 = 834."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 831 - 465.",
        366, ["366"],
        "Regroup ones: 11 - 5 = 6. Regroup tens: 12 - 6 = 6. Hundreds: 7 - 4 = 3.",
        "366.",
        "366.",
        "831 - 465 = 366."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is 408 + 295?",
        "703",
        ["693", "713", "603"],
        "Add 8 + 5 = 13 (carry 1). 1 + 0 + 9 = 10 (carry 1). 1 + 4 + 2 = 7.",
        "703.",
        "703.",
        "408 + 295 = 703."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 902 - 548.",
        354, ["354"],
        "Regroup across zero: 12 - 8 = 4, 9 - 4 = 5, 8 - 5 = 3.",
        "354.",
        "354.",
        "902 - 548 = 354."
    ))

    # =========================================================================
    # LESSON 13: Multiplying by Multiples of 10 (3.NBT.A.3)
    # =========================================================================
    LID = "G3_L13"
    LT = "Multiplying by Multiples of 10"
    DOM = "Number & Operations in Base Ten"
    STD = "3.NBT.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: 4 × 30.",
        120, ["120"],
        "Multiply the single digits first, then append a zero: 4 × 3 tens = 12 tens.",
        "4 × 3 = 12, so 4 × 30 = 120.",
        "120.",
        "4 × 30 = 120."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is 6 × 50?",
        "300",
        ["350", "250", "30"],
        "6 × 5 = 30. Append a zero for multiplying by 50.",
        "30 tens = 300.",
        "300.",
        "6 × 50 = 300."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 8 × 40.",
        320, ["320"],
        "8 × 4 = 32 tens.",
        "32 with a zero is 320.",
        "320.",
        "8 × 40 = 320."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Calculate: 7 × 90.",
        "630",
        ["640", "720", "63"],
        "7 × 9 = 63. Multiply by 10 to get 630.",
        "63 × 10 = 630.",
        "630.",
        "7 × 90 = 630."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 5 × 80.",
        400, ["400"],
        "5 × 8 = 40. Append a zero to make 400.",
        "40 tens = 400.",
        "400.",
        "5 × 80 = 400."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 9 × 60.",
        540, ["540"],
        "9 × 6 = 54. 54 tens = 540.",
        "540.",
        "540.",
        "9 × 60 = 540."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A school bought 3 boxes of folders with 40 folders in each box. How many folders did the school buy in total?",
        "120 folders",
        ["140 folders", "100 folders", "70 folders"],
        "Multiply number of boxes by folders per box: 3 × 40.",
        "3 × 4 = 12 tens = 120 folders.",
        "120 folders.",
        "3 × 40 = 120 folders."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 6 × 70.",
        420, ["420"],
        "6 × 7 = 42. Append zero to get 420.",
        "420.",
        "420.",
        "6 × 70 = 420."
    ))

    # =========================================================================
    # LESSON 14: Fractions as Parts of a Whole (3.NF.A.1)
    # =========================================================================
    LID = "G3_L14"
    LT = "Fractions as Parts of a Whole"
    DOM = "Number & Operations --- Fractions"
    STD = "3.NF.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the denominator of the fraction 3/8?",
        8, ["8"],
        "In a fraction a/b, the denominator is the bottom number, representing the total number of equal parts.",
        "In 3/8, 3 is the numerator and 8 is the denominator.",
        "8 is the denominator.",
        "In the fraction 3/8, the bottom number (denominator) is 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A pizza is divided into 4 equal slices. Liam eats 1 slice. What fraction of the pizza did Liam eat?",
        "1/4",
        ["1/2", "3/4", "4/1"],
        "A unit fraction 1/b represents 1 part out of b equal parts.",
        "Liam ate 1 slice out of 4 equal slices.",
        "1/4 of the pizza.",
        "1 slice out of 4 equal parts is 1/4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the numerator of the fraction 5/6?",
        5, ["5"],
        "The numerator is the top number of a fraction, representing the count of shaded or selected parts.",
        "In 5/6, 5 is on top.",
        "5.",
        "In 5/6, the numerator is 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A strip is divided into 6 equal parts. 5 of the parts are shaded blue. What fraction is shaded blue?",
        "5/6",
        ["1/6", "5/5", "6/5"],
        "Fraction = (shaded parts) / (total equal parts).",
        "5 shaded parts out of 6 total equal parts = 5/6.",
        "5/6.",
        "5 parts out of 6 equal parts is written as 5/6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A chocolate bar has 8 equal pieces. Maria eats 3 pieces. How many pieces are left?",
        5, ["5", "5 pieces"],
        "Subtract the eaten pieces from total pieces: 8 - 3.",
        "8 - 3 = 5 pieces.",
        "5 pieces remain (5/8 of the bar).",
        "8 - 3 = 5 pieces left."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which fraction represents 1 whole partitioned into 3 equal parts?",
        "3/3",
        ["1/3", "2/3", "3/1"],
        "When all parts are included, the numerator equals the denominator: b/b = 1.",
        "3 parts out of 3 equal parts = 3/3 = 1 whole.",
        "3/3.",
        "3/3 represents 1 whole partitioned into 3 equal parts."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What unit fraction represents one part of a rectangle split into 5 equal parts?",
        "1/5",
        ["5/1", "2/5", "1/4"],
        "A unit fraction always has a numerator of 1: 1/b.",
        "One part out of 5 equal parts is 1/5.",
        "1/5.",
        "Each equal part of 5 is 1/5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A garden is partitioned into 8 equal sections. Tomatoes are planted in 7 sections. How many sections do NOT have tomatoes?",
        1, ["1", "1 section"],
        "Subtract sections with tomatoes from total sections: 8 - 7.",
        "8 - 7 = 1 section.",
        "1 section (which is 1/8 of the garden).",
        "8 - 7 = 1 section."
    ))

    # =========================================================================
    # LESSON 15: Fractions on a Number Line (3.NF.A.2)
    # =========================================================================
    LID = "G3_L15"
    LT = "Fractions on a Number Line"
    DOM = "Number & Operations --- Fractions"
    STD = "3.NF.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which fraction is located exactly halfway between 0 and 1 on a number line?",
        "1/2",
        ["1/4", "3/4", "1/3"],
        "Halfway divides 0 to 1 into 2 equal segments.",
        "The midpoint of 0 and 1 is 1/2.",
        "1/2.",
        "1/2 is halfway between 0 and 1."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "If the distance from 0 to 1 on a number line is divided into 4 equal segments, how many fourths represent the whole number 1?",
        4, ["4", "4/4"],
        "Each segment is 1/4. The point 1 is at 4/4.",
        "4 segments of 1/4 make 1.",
        "4.",
        "4 fourths (4/4) equal 1 whole."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "If a number line from 0 to 1 is divided into 6 equal parts, what fraction is at the 3rd tick mark after 0?",
        "3/6",
        ["1/6", "2/6", "4/6"],
        "Each mark represents 1/6. The 3rd mark is 3/6.",
        "3 jumps of 1/6 = 3/6.",
        "3/6.",
        "The 3rd mark is at 3/6 (which is equivalent to 1/2)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "How many equal intervals of size 1/8 are needed to reach 5/8 starting from 0?",
        5, ["5", "5 jumps"],
        "Starting at 0, each jump of 1/8 advances by 1/8. 5 jumps reach 5/8.",
        "5 jumps of 1/8 = 5/8.",
        "5.",
        "5 intervals of 1/8 reach 5/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "On a number line from 0 to 1 partitioned into thirds, what fraction is located at 1?",
        "3/3",
        ["1/3", "2/3", "4/3"],
        "The whole number 1 partitioned into thirds is 3/3.",
        "3/3 = 1.",
        "3/3.",
        "3/3 is at the number 1 on the number line."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A point is plotted on a number line divided into eighths. It is 6 steps to the right of 0. What is the numerator of this fraction?",
        6, ["6"],
        "6 steps on a number line partitioned into eighths represents 6/8.",
        "The numerator is 6.",
        "6.",
        "The point is at 6/8, so its numerator is 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which fraction is closer to 1 on a number line: 1/4 or 3/4?",
        "3/4",
        ["1/4", "They are the same distance", "Neither"],
        "Compare distance to 1: 1 - 3/4 = 1/4, while 1 - 1/4 = 3/4.",
        "3/4 is only 1/4 away from 1.",
        "3/4 is closer to 1.",
        "3/4 is closer to 1 than 1/4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If a number line from 0 to 1 is divided into 5 equal parts, what is the denominator of each interval?",
        5, ["5"],
        "When 0 to 1 is partitioned into 5 equal segments, each segment is 1/5.",
        "The denominator is 5.",
        "5.",
        "The denominator is 5."
    ))

    # =========================================================================
    # LESSON 16: Equivalent Fractions (3.NF.A.3a-c)
    # =========================================================================
    LID = "G3_L16"
    LT = "Equivalent Fractions"
    DOM = "Number & Operations --- Fractions"
    STD = "3.NF.A.3a-c"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the missing numerator to make the fractions equivalent: 1/2 = ___/4.",
        2, ["2"],
        "Multiply the numerator and denominator by the same number (2).",
        "1 × 2 = 2, and 2 × 2 = 4.",
        "2.",
        "1/2 = 2/4 because multiplying numerator and denominator by 2 gives 2/4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which fraction is equivalent to 1/3?",
        "2/6",
        ["2/3", "3/6", "1/6"],
        "Multiply both numerator and denominator of 1/3 by 2.",
        "1 × 2 = 2, and 3 × 2 = 6, so 2/6.",
        "2/6 is equivalent to 1/3.",
        "1/3 = 2/6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Complete the equivalent fraction: 2/3 = ___/6.",
        4, ["4"],
        "The denominator was multiplied by 2 (3 × 2 = 6). Multiply numerator by 2.",
        "2 × 2 = 4.",
        "4.",
        "2/3 = 4/6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which whole number is equivalent to the fraction 8/2?",
        "4",
        ["2", "6", "8"],
        "A fraction represents division: 8/2 = 8 ÷ 2.",
        "8 ÷ 2 = 4.",
        "4.",
        "8/2 = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Complete the equivalent fraction: 3/4 = ___/8.",
        6, ["6"],
        "Multiply numerator and denominator of 3/4 by 2.",
        "3 × 2 = 6.",
        "6.",
        "3/4 = 6/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which fraction is equivalent to 4/8?",
        "1/2",
        ["1/4", "3/4", "2/3"],
        "Divide numerator and denominator by 4: (4÷4)/(8÷4) = 1/2.",
        "4/8 simplifies to 1/2.",
        "1/2.",
        "4/8 = 1/2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Find the missing denominator: 2/5 = 4/___.",
        10, ["10"],
        "The numerator was multiplied by 2 (2 × 2 = 4). Multiply denominator by 2.",
        "5 × 2 = 10.",
        "10.",
        "2/5 = 4/10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What fraction represents the whole number 5?",
        "5/1",
        ["1/5", "5/5", "10/5"],
        "Any whole number n can be written as n/1.",
        "5 wholes = 5/1.",
        "5/1.",
        "5 = 5/1."
    ))

    # =========================================================================
    # LESSON 17: Comparing Fractions (3.NF.A.3d)
    # =========================================================================
    LID = "G3_L17"
    LT = "Comparing Fractions"
    DOM = "Number & Operations --- Fractions"
    STD = "3.NF.A.3d"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which comparison between 3/4 and 1/4 is correct?",
        "3/4 > 1/4",
        ["3/4 < 1/4", "3/4 = 1/4", "1/4 > 3/4"],
        "When denominators are the same, compare numerators. The fraction with the larger numerator is greater.",
        "3 > 1, so 3/4 > 1/4.",
        "3/4 > 1/4.",
        "3/4 is greater than 1/4 because 3 parts is more than 1 part of the same size."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Compare 2/5 and 4/5. Which symbol belongs in the blank: 2/5 ___ 4/5?",
        "<",
        [">", "=", "+"],
        "Same denominator: compare 2 and 4. 2 is less than 4.",
        "2/5 < 4/5.",
        "<.",
        "2/5 < 4/5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Which fraction is greater: 1/3 or 1/6?",
        "1/3",
        ["1/6", "They are equal", "Cannot be determined"],
        "When numerators are the same (both 1), smaller denominators mean larger pieces.",
        "Thirds are larger than sixths, so 1/3 > 1/6.",
        "1/3 is greater.",
        "1/3 > 1/6 because cutting a whole into 3 parts makes bigger pieces than cutting into 6 parts."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Compare 3/8 and 5/8. Which statement is true?",
        "5/8 is greater than 3/8",
        ["3/8 is greater than 5/8", "3/8 is equal to 5/8", "5/8 is less than 3/8"],
        "5 eighths is more than 3 eighths.",
        "5/8 > 3/8.",
        "5/8 is greater.",
        "5/8 > 3/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Which fraction is smaller: 1/2 or 1/8?",
        "1/8",
        ["1/2", "They are equal", "Neither"],
        "Same numerator (1): the fraction with the larger denominator has smaller parts.",
        "Eighths are much smaller than halves, so 1/8 is smaller.",
        "1/8.",
        "1/8 is smaller than 1/2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which fraction is the largest among: 1/8, 3/8, 5/8, 7/8?",
        "7/8",
        ["1/8", "3/8", "5/8"],
        "All fractions have denominator 8. Compare numerators: 7 is largest.",
        "7/8 has the most eighths.",
        "7/8 is largest.",
        "7/8 is the largest fraction."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which comparison is correct?",
        "2/3 > 2/6",
        ["2/3 < 2/6", "2/3 = 2/6", "2/6 > 2/3"],
        "Same numerator (2): thirds are larger than sixths.",
        "2 thirds is greater than 2 sixths.",
        "2/3 > 2/6.",
        "2/3 > 2/6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Compare 5/6 and 3/6. Which is greater?",
        "5/6",
        ["3/6", "They are equal", "Cannot tell"],
        "Same denominator 6: 5 is greater than 3.",
        "5/6 > 3/6.",
        "5/6.",
        "5/6 is greater than 3/6."
    ))

    # =========================================================================
    # LESSON 18: Telling Time & Elapsed Time (3.MD.A.1)
    # =========================================================================
    LID = "G3_L18"
    LT = "Telling Time & Elapsed Time"
    DOM = "Measurement & Data"
    STD = "3.MD.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A soccer practice starts at 3:15 PM and ends at 3:50 PM. How many minutes did practice last?",
        35, ["35", "35 minutes"],
        "Subtract starting minutes from ending minutes within the same hour.",
        "50 - 15 = 35 minutes.",
        "35 minutes.",
        "3:50 - 3:15 = 35 minutes."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What time is 45 minutes after 3:15?",
        "4:00",
        ["3:50", "4:15", "3:45"],
        "Add minutes: 15 + 45 = 60 minutes. 60 minutes makes 1 whole hour.",
        "3:00 + 1 hour = 4:00.",
        "4:00.",
        "3:15 + 45 minutes = 4:00."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Maya starts reading at 4:20 PM and reads for 30 minutes. At what time does she finish? (Enter minute portion: e.g. 50 for 4:50)",
        50, ["50", "4:50"],
        "Add elapsed minutes to the start minute: 20 + 30.",
        "20 + 30 = 50, so the time is 4:50.",
        "50.",
        "4:20 + 30 minutes = 4:50 PM."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "If a cartoon starts at 8:05 AM and lasts 25 minutes, what time does it end?",
        "8:30 AM",
        ["8:25 AM", "8:35 AM", "8:40 AM"],
        "Add 25 minutes to 8:05: 5 + 25 = 30.",
        "The cartoon ends at 8:30 AM.",
        "8:30 AM.",
        "8:05 + 25 minutes = 8:30 AM."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A bus departs at 10:10 AM and arrives at 10:45 AM. How long was the bus ride in minutes?",
        35, ["35", "35 minutes"],
        "Subtract departure minutes from arrival minutes: 45 - 10.",
        "45 - 10 = 35 minutes.",
        "35 minutes.",
        "10:45 - 10:10 = 35 minutes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "How many minutes are in 1 whole hour?",
        60, ["60", "60 minutes"],
        "1 hour = 60 minutes.",
        "60 minutes.",
        "60.",
        "There are 60 minutes in 1 hour."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which time represents 'quarter past 7'?",
        "7:15",
        ["7:30", "7:45", "6:45"],
        "A quarter of an hour is 15 minutes. Quarter past 7 means 15 minutes after 7:00.",
        "7:15.",
        "7:15.",
        "Quarter past 7 is 7:15."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If gym class begins at 1:25 PM and ends at 2:10 PM, how many minutes long was gym class?",
        45, ["45", "45 minutes"],
        "Count from 1:25 to 2:00 (35 min), then add 10 min to 2:10.",
        "35 + 10 = 45 minutes.",
        "45 minutes.",
        "From 1:25 to 2:10 is 45 minutes."
    ))

    # =========================================================================
    # LESSON 19: Measuring Liquid Volume & Mass (3.MD.A.2)
    # =========================================================================
    LID = "G3_L19"
    LT = "Measuring Liquid Volume & Mass"
    DOM = "Measurement & Data"
    STD = "3.MD.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A pitcher holds 3 liters of water. Carlos pours in 4 more liters. How many liters of water are in the pitcher now?",
        7, ["7", "7 liters"],
        "Add the volumes: 3 + 4.",
        "3 + 4 = 7 liters.",
        "7 liters.",
        "3 + 4 = 7 liters."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which metric unit is most appropriate to measure the mass of a paperclip?",
        "Grams",
        ["Kilograms", "Liters", "Meters"],
        "Small, light objects are measured in grams. Heavy objects are measured in kilograms.",
        "A paperclip has a mass of about 1 gram.",
        "Grams.",
        "A paperclip is very light, so grams is the appropriate unit."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "An apple has a mass of 150 grams. An orange has a mass of 200 grams. What is their total combined mass in grams?",
        350, ["350", "350 grams"],
        "Add the masses: 150 + 200.",
        "150 + 200 = 350 grams.",
        "350 grams.",
        "150 + 200 = 350 grams."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which unit is best to measure the volume of water in a bathtub?",
        "Liters",
        ["Grams", "Kilograms", "Millimeters"],
        "Large liquid capacities are measured in liters.",
        "A bathtub holds around 150 liters of water.",
        "Liters.",
        "Liters is the standard unit for large liquid volumes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A bucket holds 18 liters of water. If 7 liters are poured out, how many liters remain?",
        11, ["11", "11 liters"],
        "Subtract the poured water from the total: 18 - 7.",
        "18 - 7 = 11 liters.",
        "11 liters.",
        "18 - 7 = 11 liters."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A package has a mass of 4 kilograms. What is the total mass of 5 identical packages in kilograms?",
        20, ["20", "20 kg", "20 kilograms"],
        "Multiply mass per package by the number of packages: 4 × 5.",
        "4 × 5 = 20 kilograms.",
        "20 kilograms.",
        "4 × 5 = 20 kilograms."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "1 kilogram is equal to how many grams?",
        "1,000 grams",
        ["100 grams", "10 grams", "10,000 grams"],
        "The prefix 'kilo-' means one thousand.",
        "1 kg = 1,000 g.",
        "1,000 grams.",
        "1 kilogram = 1,000 grams."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A bottle holds 500 milliliters of juice. If you drink 200 milliliters, how many milliliters are left?",
        300, ["300", "300 mL"],
        "Subtract consumed amount from total: 500 - 200.",
        "500 - 200 = 300 milliliters.",
        "300 milliliters.",
        "500 - 200 = 300 mL."
    ))

    # =========================================================================
    # LESSON 20: Picture Graphs & Bar Graphs (3.MD.B.3)
    # =========================================================================
    LID = "G3_L20"
    LT = "Picture Graphs & Bar Graphs"
    DOM = "Measurement & Data"
    STD = "3.MD.B.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a picture graph, each star symbol represents 4 books read. How many books do 5 star symbols represent?",
        20, ["20", "20 books"],
        "Multiply the number of symbols by the key value: 5 × 4.",
        "5 × 4 = 20 books.",
        "20 books.",
        "5 stars × 4 books per star = 20 books."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "On a bar graph, 14 students chose Apples and 9 chose Bananas. How many more students chose Apples than Bananas?",
        "5 students",
        ["4 students", "6 students", "23 students"],
        "To find 'how many more', subtract the smaller value from the larger value.",
        "14 - 9 = 5 students.",
        "5 students.",
        "14 - 9 = 5 students."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In a pictograph where 1 smiley face = 3 students, Leo counts 6 smiley faces for soccer. How many students chose soccer?",
        18, ["18", "18 students"],
        "Multiply symbols by key scale: 6 × 3.",
        "6 × 3 = 18 students.",
        "18 students.",
        "6 × 3 = 18 students."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "If each circle symbol represents 5 points, how many circles are needed to represent 35 points?",
        "7 circles",
        ["5 circles", "6 circles", "8 circles"],
        "Divide total points by points per circle: 35 ÷ 5.",
        "35 ÷ 5 = 7 circles.",
        "7 circles.",
        "35 ÷ 5 = 7 circles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "On a favorite pet graph, 12 students voted for dogs, 15 for cats, and 8 for birds. How many total students were surveyed?",
        35, ["35", "35 students"],
        "Add the votes together: 12 + 15 + 8.",
        "12 + 15 = 27; 27 + 8 = 35 students.",
        "35 students.",
        "12 + 15 + 8 = 35 students."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "On a scaled bar graph where the scale goes by 10s, Bar A reaches 80. How many units does Bar A show?",
        80, ["80"],
        "Read the top of the bar across to the vertical axis.",
        "The bar aligns with 80.",
        "80.",
        "Bar A shows 80 units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What does the key in a picture graph tell you?",
        "What each symbol represents",
        ["The title of the graph", "The total number of rows", "The color of the bars"],
        "The key explains the scale or value of one picture symbol.",
        "For example, 'Key: 1 star = 2 students'.",
        "The key tells what each symbol represents.",
        "The key defines the numerical value represented by each picture symbol."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Bar X has a value of 25 and Bar Y has a value of 18. What is the difference between Bar X and Bar Y?",
        7, ["7"],
        "Subtract Bar Y from Bar X: 25 - 18.",
        "25 - 18 = 7.",
        "7.",
        "25 - 18 = 7."
    ))

    # =========================================================================
    # LESSON 21: Measurement Data on Line Plots (3.MD.B.4)
    # =========================================================================
    LID = "G3_L21"
    LT = "Measurement Data on Line Plots"
    DOM = "Measurement & Data"
    STD = "3.MD.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "On a standard ruler, how many quarter-inches (1/4 in) are in 1 whole inch?",
        4, ["4"],
        "1 inch divided into fourths has 4 parts: 4/4 = 1.",
        "There are 4 quarter-inches in 1 inch.",
        "4.",
        "4 quarters equal 1 whole inch."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "On a line plot showing lengths of ribbons, what does each 'X' mark represent?",
        "One ribbon measured",
        ["The total length", "The ruler length", "One inch"],
        "Each mark (X or dot) on a line plot represents one individual data observation.",
        "Each X represents one ribbon that was measured.",
        "One ribbon measured.",
        "Each X represents one data point (one ribbon measured)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A pencil measures 5 inches and another measures 3 inches. What is the difference in their lengths in inches?",
        2, ["2", "2 inches"],
        "Subtract lengths: 5 - 3 = 2 inches.",
        "5 - 3 = 2.",
        "2 inches.",
        "5 - 3 = 2 inches."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "On a line plot, there are three X marks at 2 inches and two X marks at 3 inches. How many total items were measured?",
        "5 items",
        ["6 items", "3 items", "2 items"],
        "Count the total number of X marks on the plot.",
        "3 + 2 = 5 X marks.",
        "5 items.",
        "3 + 2 = 5 items were measured."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many half-inches (1/2 in) are there in 3 whole inches?",
        6, ["6"],
        "Each whole inch has 2 halves. For 3 inches: 3 × 2 = 6.",
        "3 × 2 = 6 half-inches.",
        "6.",
        "3 × 2 = 6 half-inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If four pieces of string each measure 1/2 inch, what is their combined length in inches?",
        2, ["2", "2 inches"],
        "Add: 1/2 + 1/2 + 1/2 + 1/2 = 4/2 = 2 whole inches.",
        "4 × (1/2) = 2.",
        "2 inches.",
        "4 × 1/2 = 2 inches."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A line plot shows measurements in halves of an inch. Which measurement could appear on this line plot?",
        "2 and 1/2 inches",
        ["2 and 1/3 inches", "2 and 1/5 inches", "2 and 1/7 inches"],
        "A line plot marked in halves has values like 0, 1/2, 1, 1 1/2, 2, 2 1/2, etc.",
        "2 and 1/2 is a half-inch measurement.",
        "2 and 1/2 inches.",
        "2 and 1/2 inches is partitioned in halves."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "On a line plot, there are 5 X marks above 6 inches. How many measured items had a length of 6 inches?",
        5, ["5", "5 items"],
        "The number of X marks above a tick mark shows the frequency for that measurement.",
        "5 X marks means 5 items.",
        "5 items.",
        "5 items measured 6 inches."
    ))

    # =========================================================================
    # LESSON 22: Understanding Area & Unit Squares (3.MD.C.5 / 3.MD.C.6)
    # =========================================================================
    LID = "G3_L22"
    LT = "Understanding Area & Unit Squares"
    DOM = "Measurement & Data"
    STD = "3.MD.C.5 / 3.MD.C.6"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A rectangle is tiled completely by 4 rows of 6 unit squares with no gaps or overlaps. What is the area in square units?",
        24, ["24", "24 square units"],
        "Area is found by counting unit squares or multiplying rows by columns: rows × columns.",
        "4 rows × 6 squares per row = 24 square units.",
        "24 square units.",
        "4 × 6 = 24 square units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the area of a square that is 5 unit squares long and 5 unit squares wide?",
        "25 square units",
        ["20 square units", "10 square units", "30 square units"],
        "Area of a square = side × side.",
        "5 × 5 = 25 square units.",
        "25 square units.",
        "5 × 5 = 25 square units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A figure is made of 18 unit squares tiled together. What is the area of the figure in square units?",
        18, ["18", "18 square units"],
        "Area is measured by the total number of unit squares covering the figure.",
        "18 unit squares = area of 18 square units.",
        "18 square units.",
        "The area is 18 square units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What unit is used to measure area?",
        "Square units",
        ["Linear units", "Cubic units", "Liters"],
        "Area measures 2-dimensional surface coverage, so it is measured in square units (e.g., square centimeters, square feet).",
        "Square units.",
        "Square units.",
        "Area is measured in square units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A grid has 3 rows of unit squares with 7 squares in each row. What is its total area in square units?",
        21, ["21", "21 square units"],
        "Multiply rows by columns: 3 × 7.",
        "3 × 7 = 21 square units.",
        "21 square units.",
        "3 × 7 = 21 square units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rectangle has an area of 16 square units and a width of 4 units. What is its length?",
        4, ["4", "4 units"],
        "Area = length × width. Length = Area ÷ width.",
        "16 ÷ 4 = 4 units.",
        "4 units.",
        "16 ÷ 4 = 4 units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What does area measure?",
        "The amount of surface a plane figure covers",
        ["The distance around the outside of a shape", "The weight of a shape", "The height of a shape"],
        "Perimeter is the distance around; Area is the surface covered inside.",
        "Area measures surface coverage.",
        "The amount of surface a figure covers.",
        "Area is the amount of surface covered by a 2D shape."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A mosaic rug is covered with 5 rows of 8 unit square tiles. What is the area of the rug in square tiles?",
        40, ["40", "40 tiles"],
        "Multiply rows by tiles per row: 5 × 8.",
        "5 × 8 = 40 square tiles.",
        "40.",
        "5 × 8 = 40 square units."
    ))

    # =========================================================================
    # LESSON 23: Area of Rectangles & Decomposing (3.MD.C.7)
    # =========================================================================
    LID = "G3_L23"
    LT = "Area of Rectangles & Decomposing"
    DOM = "Measurement & Data"
    STD = "3.MD.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the area of a rectangle with a length of 9 cm and a width of 4 cm in square centimeters.",
        36, ["36", "36 sq cm"],
        "Area of a rectangle = length × width.",
        "9 × 4 = 36 square centimeters.",
        "36.",
        "9 × 4 = 36 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which formula gives the area of a rectangle?",
        "Area = length × width",
        ["Area = length + width", "Area = 2 × length + 2 × width", "Area = length ÷ width"],
        "Area is found by multiplying the two side dimensions together.",
        "Area = length × width.",
        "Area = length × width.",
        "The area formula is Area = length × width."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rectangle has an area of 48 square inches. If its length is 8 inches, what is its width in inches?",
        6, ["6", "6 inches"],
        "Width = Area ÷ length.",
        "48 ÷ 8 = 6 inches.",
        "6 inches.",
        "48 ÷ 8 = 6 inches."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "By decomposing, 7 × 8 can be broken into (7 × 5) + (7 × 3). What is 35 + 21?",
        "56",
        ["54", "58", "60"],
        "Use the distributive property: 7 × 8 = 7 × (5 + 3) = 35 + 21.",
        "35 + 21 = 56.",
        "56.",
        "35 + 21 = 56."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the area of a rectangular garden that is 6 meters wide and 10 meters long in square meters.",
        60, ["60", "60 sq m"],
        "Area = length × width.",
        "10 × 6 = 60 square meters.",
        "60 square meters.",
        "10 × 6 = 60 sq m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "An L-shaped room is decomposed into two rectangles: one is 4 m by 5 m (area 20) and the other is 3 m by 2 m (area 6). What is the total area of the room in square meters?",
        26, ["26", "26 sq m"],
        "Add the areas of the two decomposed rectangular parts: 20 + 6.",
        "20 + 6 = 26 square meters.",
        "26 square meters.",
        "20 + 6 = 26 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the area of a square with a side length of 9 inches?",
        "81 square inches",
        ["72 square inches", "36 square inches", "90 square inches"],
        "Area of square = side × side: 9 × 9.",
        "9 × 9 = 81 square inches.",
        "81 square inches.",
        "9 × 9 = 81 square inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A wall is 8 feet high and 12 feet long. What is the area of the wall in square feet?",
        96, ["96", "96 sq ft"],
        "Area = height × length: 8 × 12.",
        "8 × 12 = 96 square feet.",
        "96.",
        "8 × 12 = 96 sq ft."
    ))

    # =========================================================================
    # LESSON 24: Perimeter & Area Relationships (3.MD.D.8)
    # =========================================================================
    LID = "G3_L24"
    LT = "Perimeter & Area Relationships"
    DOM = "Measurement & Data"
    STD = "3.MD.D.8"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the perimeter of a rectangle with length 7 cm and width 4 cm in centimeters.",
        22, ["22", "22 cm"],
        "Perimeter is the distance around: Perimeter = 2 × (length + width).",
        "7 + 4 = 11. 11 × 2 = 22 cm.",
        "22 cm.",
        "Perimeter = 7 + 4 + 7 + 4 = 22 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the perimeter of a square with side length 6 inches?",
        "24 inches",
        ["36 inches", "12 inches", "18 inches"],
        "A square has 4 equal sides: Perimeter = 4 × side.",
        "4 × 6 = 24 inches.",
        "24 inches.",
        "4 × 6 = 24 inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A triangle has side lengths of 5 cm, 7 cm, and 9 cm. What is its perimeter in centimeters?",
        21, ["21", "21 cm"],
        "Add all three side lengths together.",
        "5 + 7 + 9 = 21 cm.",
        "21 cm.",
        "5 + 7 + 9 = 21 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A rectangle has a perimeter of 20 cm and a length of 6 cm. What is its width in centimeters?",
        "4 cm",
        ["5 cm", "6 cm", "8 cm"],
        "Perimeter = 2 × (length + width) = 20. So length + width = 10.",
        "6 + width = 10 -> width = 4 cm.",
        "4 cm.",
        "20 - (6 + 6) = 8. 8 ÷ 2 = 4 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A regular pentagon has 5 equal sides. If each side measures 4 cm, what is its perimeter in centimeters?",
        20, ["20", "20 cm"],
        "Multiply the number of sides by the side length: 5 × 4.",
        "5 × 4 = 20 cm.",
        "20 cm.",
        "5 × 4 = 20 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rectangle has side lengths 3 units and 4 units. What is its perimeter in units?",
        14, ["14", "14 units"],
        "Perimeter = 2 × (3 + 4) = 2 × 7 = 14 units.",
        "3 + 4 + 3 + 4 = 14.",
        "14 units.",
        "Perimeter = 3 + 4 + 3 + 4 = 14."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What does perimeter measure?",
        "The total distance around the outside edge of a shape",
        ["The surface area inside a shape", "The volume inside a box", "The number of angles"],
        "Perimeter is a 1-dimensional measurement of boundary length.",
        "Distance around the outside.",
        "Total distance around the outside edge.",
        "Perimeter is the total boundary distance around a 2D shape."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the perimeter of a regular hexagon (6 equal sides) where each side is 5 inches.",
        30, ["30", "30 inches"],
        "A regular hexagon has 6 equal sides: Perimeter = 6 × side length.",
        "6 × 5 = 30 inches.",
        "30 inches.",
        "6 × 5 = 30 inches."
    ))

    # =========================================================================
    # LESSON 25: Shape Classes & Financial Literacy (3.G.A.1 / 3.G.A.2 / 3.MD.D.8)
    # =========================================================================
    LID = "G3_L25"
    LT = "Shape Classes & Financial Literacy"
    DOM = "Geometry & Financial Literacy"
    STD = "3.G.A.1 / 3.G.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "How many sides does any quadrilateral have?",
        4, ["4", "4 sides"],
        "The prefix 'quad-' means four. All quadrilaterals have 4 sides and 4 angles.",
        "A quadrilateral has 4 sides.",
        "4 sides.",
        "A quadrilateral has 4 sides."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which shape is always classified as a quadrilateral?",
        "Rectangle",
        ["Triangle", "Pentagon", "Hexagon"],
        "A rectangle has 4 sides, so it is a quadrilateral.",
        "Rectangles have 4 straight sides.",
        "Rectangle.",
        "A rectangle is a 4-sided polygon, which is a quadrilateral."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Leo has 3 quarters (25¢ each), 2 dimes (10¢ each), and 1 nickel (5¢). How many total cents does Leo have?",
        100, ["100", "100 cents", "$1.00", "$1"],
        "Add: (3 × 25) + (2 × 10) + 5.",
        "75 + 20 + 5 = 100 cents ($1.00).",
        "100 cents.",
        "75¢ + 20¢ + 5¢ = 100¢ ($1.00)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A rectangle is partitioned into 4 equal shares. What fraction of the area is each share?",
        "1/4",
        ["1/2", "3/4", "4/1"],
        "When an area is divided into 4 equal shares, each share represents 1/4 of the total area.",
        "Each part is 1/4.",
        "1/4.",
        "Each equal part of 4 is 1/4 of the area."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Maya buys a book for $6. She pays with a $10 bill. How many dollars in change should Maya receive?",
        4, ["4", "$4"],
        "Subtract item cost from money paid: $10 - $6.",
        "10 - 6 = 4.",
        "$4.",
        "$10 - $6 = $4 in change."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which quadrilateral has 4 equal sides and 4 right angles?",
        "Square",
        ["Rhombus", "Trapezoid", "Parallelogram"],
        "A square has all 4 sides equal AND 4 right (90°) angles.",
        "A square satisfies both properties.",
        "Square.",
        "A square has 4 congruent sides and 4 right angles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A square is cut diagonally into 2 equal triangles. What fraction of the square\\'s area is each triangle?",
        "1/2",
        ["1/4", "2/1", "1/3"],
        "Cutting into 2 equal shares gives 1/2 for each share.",
        "Each triangle is 1/2 of the square.",
        "1/2.",
        "Each triangle is 1/2 of the square."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A student has one $5 bill and two $1 bills. What is the total dollar amount?",
        7, ["7", "$7"],
        "Add dollar values: 5 + 1 + 1.",
        "5 + 2 = $7.",
        "$7.",
        "$5 + $2 = $7."
    ))

    return questions
'''

with open('scripts/builders/grade_3.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated scripts/builders/grade_3.py successfully!")
