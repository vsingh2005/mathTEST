"""
scripts/generators/generate_grade_4.py
Script to generate the complete Grade 4 curriculum questions builder (Lessons 1-25).
"""

code = '''"""
scripts/builders/grade_4.py
High-fidelity mathematical question builder for Grade 4 (Lessons 1-25).
100% verified math answers, child-friendly prompts, and progressive 3-tier hints.
"""

from scripts.builders.helpers import make_numeric_question, make_mc_question

def build_grade_4_questions():
    questions = []
    G = 4

    # =========================================================================
    # LESSON 1: Comparison Word Problems (4.OA.A.1 / 4.OA.A.2)
    # =========================================================================
    LID = "G4_L01"
    LT = "Comparison Word Problems"
    DOM = "Operations & Algebraic Thinking"
    STD = "4.OA.A.1 / 4.OA.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Leo has 6 books. Maya has 4 times as many books as Leo. How many books does Maya have?",
        24, ["24", "24 books"],
        "Multiplicative comparison means one quantity is a multiple of another: Maya = 4 × Leo.",
        "Multiply Leo\\'s 6 books by 4.",
        "6 × 4 = 24 books.",
        "Maya has 4 × 6 = 24 books."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which statement represents the equation 35 = 5 × 7?",
        "35 is 5 times as many as 7",
        ["35 is 5 more than 7", "35 is 7 less than 5", "5 is 35 times as many as 7"],
        "Multiplication compares two quantities: a = b × c means a is b times as many as c.",
        "35 = 5 × 7 means 35 is 5 times as many as 7 (or 7 times as many as 5).",
        "35 is 5 times as many as 7.",
        "35 = 5 × 7 expresses that 35 is 5 times as many as 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A red ribbon is 45 cm long. It is 5 times as long as a blue ribbon. How long is the blue ribbon in cm?",
        9, ["9", "9 cm"],
        "To find the smaller quantity, divide the larger quantity by the comparison factor: 45 ÷ 5.",
        "Calculate 45 ÷ 5.",
        "45 ÷ 5 = 9 cm.",
        "Blue ribbon = 45 ÷ 5 = 9 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Sam scored 8 points in a video game. Rachel scored 3 times as many points as Sam. How many points did Rachel score?",
        "24 points",
        ["11 points", "21 points", "28 points"],
        "Multiply Sam\\'s score by 3: 8 × 3.",
        "8 × 3 = 24.",
        "24 points.",
        "Rachel scored 8 × 3 = 24 points."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A giraffe is 18 feet tall. A baby goat is 3 feet tall. How many times taller is the giraffe than the baby goat?",
        6, ["6", "6 times"],
        "Divide the height of the giraffe by the height of the goat: 18 ÷ 3.",
        "18 ÷ 3 = 6.",
        "6 times taller.",
        "18 ÷ 3 = 6 times taller."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "At the shelter, there are 28 cats. There are 4 times as many cats as dogs. How many dogs are at the shelter?",
        7, ["7", "7 dogs"],
        "Divide the number of cats by 4: 28 ÷ 4.",
        "28 ÷ 4 = 7 dogs.",
        "7 dogs.",
        "28 ÷ 4 = 7 dogs."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "An adult elephant weighs 6,000 pounds. A young elephant weighs 2,000 pounds. Which equation represents this comparison?",
        "6,000 = 3 × 2,000",
        ["6,000 = 4,000 + 2,000", "2,000 = 3 × 6,000", "6,000 ÷ 2 = 3,000"],
        "Divide to find the factor: 6,000 ÷ 2,000 = 3.",
        "The adult weighs 3 times as much: 6,000 = 3 × 2,000.",
        "6,000 = 3 × 2,000.",
        "6,000 = 3 × 2,000 models the multiplicative comparison."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Kiran saved $7. His older brother saved 8 times as much money. How much money did Kiran\\'s brother save in dollars?",
        56, ["56", "$56"],
        "Multiply Kiran\\'s savings by 8: 7 × 8.",
        "7 × 8 = 56.",
        "$56.",
        "7 × 8 = $56."
    ))

    # =========================================================================
    # LESSON 2: Multi-Step Word Problems (4.OA.A.3)
    # =========================================================================
    LID = "G4_L02"
    LT = "Multi-Step Word Problems"
    DOM = "Operations & Algebraic Thinking"
    STD = "4.OA.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A toy store has 5 boxes with 12 cars in each box. They sell 15 cars. How many cars are left?",
        45, ["45", "45 cars"],
        "Find total cars first (5 × 12), then subtract the sold cars (60 - 15).",
        "5 × 12 = 60 cars. 60 - 15 = ?",
        "60 - 15 = 45 cars.",
        "Total = 5 × 12 = 60. Left = 60 - 15 = 45 cars."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A farmer packs 85 apples into bags of 6. How many full bags of apples can the farmer make?",
        "14 bags",
        ["13 bags", "15 bags", "12 bags"],
        "Divide 85 by 6 to find whole quotient (full bags).",
        "85 ÷ 6 = 14 with a remainder of 1.",
        "14 full bags.",
        "85 ÷ 6 = 14 with remainder 1. The farmer makes 14 full bags."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In problem Q02 with 85 apples packed into bags of 6, how many apples are left over?",
        1, ["1", "1 apple"],
        "The leftover amount is the remainder of 85 ÷ 6.",
        "14 × 6 = 84. 85 - 84 = 1.",
        "1 apple left over.",
        "85 - 84 = 1 apple left over."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A school bus holds 40 students. There are 130 students going on a trip. How many buses are needed so every student has a seat?",
        "4 buses",
        ["3 buses", "5 buses", "3 buses and 10 students walking"],
        "When transporting people, any remainder requires an extra whole bus.",
        "130 ÷ 40 = 3 with remainder 10. 3 buses hold 120 students; 10 more students need a 4th bus.",
        "4 buses.",
        "130 ÷ 40 = 3 R10, so 4 buses are needed."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Ella has $100. She buys 4 shirts for $18 each. How much money does Ella have left in dollars?",
        28, ["28", "$28"],
        "Multiply shirt price by 4 (4 × 18), then subtract from $100.",
        "4 × 18 = 72. 100 - 72 = ?",
        "100 - 72 = $28.",
        "Cost = 4 × 18 = $72. Left = 100 - 72 = $28."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A baker makes 6 batches of 24 cookies. He gives 40 cookies to a party and packs the rest into bags of 8. How many bags does he pack?",
        13, ["13", "13 bags"],
        "Step 1: Total cookies = 6 × 24 = 144. Step 2: Remaining = 144 - 40 = 104. Step 3: Bags = 104 ÷ 8.",
        "104 ÷ 8 = 13.",
        "13 bags.",
        "Total = 144. Remaining = 104. Bags = 104 ÷ 8 = 13 bags."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Marcus earned $45 mowing lawns and $35 washing cars. He spent $20 on a game. Which expression shows his remaining money?",
        "(45 + 35) - 20",
        ["45 + (35 - 20) + 45", "45 × 35 - 20", "(45 - 20) + 35 × 2"],
        "First add total earnings (45 + 35), then subtract amount spent (- 20).",
        "(45 + 35) - 20 = 80 - 20 = 60.",
        "(45 + 35) - 20.",
        "(45 + 35) - 20 correctly represents the steps."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "3 teachers each order 15 notebooks. The principal adds 20 more notebooks to the order. How many notebooks were ordered altogether?",
        65, ["65", "65 notebooks"],
        "Calculate teachers\\' notebooks: 3 × 15 = 45. Add principal\\'s: 45 + 20.",
        "45 + 20 = 65.",
        "65 notebooks.",
        "3 × 15 = 45. 45 + 20 = 65 notebooks."
    ))

    # =========================================================================
    # LESSON 3: Factors & Multiples (4.OA.B.4)
    # =========================================================================
    LID = "G3_L03"
    LID = "G4_L03"
    LT = "Factors & Multiples"
    DOM = "Operations & Algebraic Thinking"
    STD = "4.OA.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "How many total factors does the number 12 have? (List: 1, 2, 3, 4, 6, 12)",
        6, ["6"],
        "Find all pairs of numbers that multiply to give 12: 1×12, 2×6, 3×4.",
        "The factors of 12 are 1, 2, 3, 4, 6, 12. Count them.",
        "There are 6 factors.",
        "12 has 6 factors: 1, 2, 3, 4, 6, 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which of the following numbers is a prime number?",
        "13",
        ["12", "15", "21"],
        "A prime number has exactly two distinct factors: 1 and itself.",
        "13 has only factors 1 and 13. (12, 15, and 21 have more factors).",
        "13 is prime.",
        "13 is prime because its only factors are 1 and 13."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the greatest factor of 24 that is less than 24?",
        12, ["12"],
        "List factors of 24: 1, 2, 3, 4, 6, 8, 12, 24.",
        "The largest factor before 24 is 12 (since 2 × 12 = 24).",
        "12.",
        "12 is the largest proper factor of 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following is a composite number?",
        "18",
        ["7", "11", "17"],
        "A composite number has more than two factors.",
        "18 has factors 1, 2, 3, 6, 9, 18, so it is composite.",
        "18 is composite.",
        "18 has more than two factors, so it is composite."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the smallest non-zero multiple of 7?",
        7, ["7"],
        "Multiples of 7 are 7 × 1, 7 × 2, 7 × 3...",
        "7 × 1 = 7.",
        "7.",
        "7 is the smallest non-zero multiple of 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Is 49 prime or composite?",
        "Composite, because 7 × 7 = 49",
        ["Prime, because it is an odd number", "Prime, because it has only 2 factors", "Neither prime nor composite"],
        "Check divisibility: 49 is divisible by 7 (7 × 7 = 49).",
        "Its factors are 1, 7, and 49 (3 factors).",
        "Composite, because 7 × 7 = 49.",
        "49 is composite because 7 × 7 = 49."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which list contains all the factors of 16?",
        "1, 2, 4, 8, 16",
        ["1, 4, 16", "2, 4, 8, 16", "1, 2, 3, 4, 8, 16"],
        "Pairs: 1 × 16 = 16, 2 × 8 = 16, 4 × 4 = 16.",
        "All factors: 1, 2, 4, 8, 16.",
        "1, 2, 4, 8, 16.",
        "The factors of 16 are 1, 2, 4, 8, 16."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the 5th multiple of 8?",
        40, ["40"],
        "Multiply 8 by 5: 8 × 5.",
        "8 × 5 = 40.",
        "40.",
        "8 × 5 = 40."
    ))

    # =========================================================================
    # LESSON 4: Generating Patterns (4.OA.C.5)
    # =========================================================================
    LID = "G4_L04"
    LT = "Generating Patterns"
    DOM = "Operations & Algebraic Thinking"
    STD = "4.OA.C.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A pattern starts at 2 and follows the rule 'Add 5'. What is the 4th term? (Terms: 2, 7, 12, ___)",
        17, ["17"],
        "Add 5 to each term: 2 + 5 = 7; 7 + 5 = 12; 12 + 5 = ?",
        "12 + 5 = 17.",
        "17.",
        "2, 7, 12, 17. The 4th term is 17."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Look at the pattern: 3, 6, 12, 24, 48. What is the rule?",
        "Multiply by 2",
        ["Add 3", "Multiply by 3", "Add 6"],
        "Compare each term to the next: 3 × 2 = 6, 6 × 2 = 12, 12 × 2 = 24.",
        "The rule is multiply by 2.",
        "Multiply by 2.",
        "Each term is doubled, so the rule is multiply by 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A pattern starts at 64 and follows the rule 'Divide by 2'. What is the next number: 64, 32, 16, ___?",
        8, ["8"],
        "Divide 16 by 2.",
        "16 ÷ 2 = 8.",
        "8.",
        "16 ÷ 2 = 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In a pattern with rule 'Add 4' starting at 1 (1, 5, 9, 13, 17...), what do you notice about all the numbers?",
        "All the numbers are odd",
        ["All the numbers are even", "All the numbers are multiples of 4", "The numbers alternate even and odd"],
        "Starting with an odd number and adding an even number (4) always produces an odd number.",
        "Odd + Even = Odd. Every number is odd.",
        "All numbers are odd.",
        "Starting at 1 and repeatedly adding 4 always results in an odd number."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the missing number in the pattern: 5, 11, ___, 23, 29?",
        17, ["17"],
        "Find the step: 11 - 5 = 6. The rule is Add 6.",
        "11 + 6 = 17. Check: 17 + 6 = 23.",
        "17.",
        "11 + 6 = 17."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A sequence starts at 1 and multiplies by 3: 1, 3, 9, 27, ___. What is the 5th term?",
        81, ["81"],
        "Multiply 27 by 3.",
        "27 × 3 = 81.",
        "81.",
        "27 × 3 = 81."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A shape pattern repeats: Circle, Square, Triangle, Circle, Square, Triangle... What is the 10th shape?",
        "Circle",
        ["Square", "Triangle", "Star"],
        "The pattern repeats every 3 shapes: 1=Circle, 2=Square, 3=Triangle.",
        "10 ÷ 3 has a remainder of 1. Remainder 1 corresponds to Circle.",
        "Circle.",
        "10 ÷ 3 = 3 R1. The 1st shape in the cycle is Circle."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A number pattern follows: 100, 92, 84, 76, ___. What is the next number?",
        68, ["68"],
        "Find difference: 100 - 92 = 8. The rule is subtract 8.",
        "76 - 8 = 68.",
        "68.",
        "76 - 8 = 68."
    ))

    # =========================================================================
    # LESSON 5: Equations & Unknowns (4.OA.A.3)
    # =========================================================================
    LID = "G4_L05"
    LT = "Equations & Unknowns"
    DOM = "Operations & Algebraic Thinking"
    STD = "4.OA.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the value of n in the equation: n + 15 = 42.",
        27, ["27"],
        "Subtract 15 from both sides: n = 42 - 15.",
        "42 - 15 = 27.",
        "n = 27.",
        "n = 42 - 15 = 27."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve for x: 7 × x = 56.",
        "8",
        ["6", "7", "9"],
        "Divide both sides by 7: x = 56 ÷ 7.",
        "56 ÷ 7 = 8.",
        "x = 8.",
        "x = 56 ÷ 7 = 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the unknown value: y - 28 = 35.",
        63, ["63"],
        "Add 28 to both sides: y = 35 + 28.",
        "35 + 28 = 63.",
        "y = 63.",
        "y = 35 + 28 = 63."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve for m: m ÷ 6 = 9.",
        "54",
        ["48", "36", "63"],
        "Multiply both sides by 6: m = 9 × 6.",
        "9 × 6 = 54.",
        "m = 54.",
        "m = 9 × 6 = 54."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the value of p in: 3 × p + 4 = 25.",
        7, ["7"],
        "Step 1: Subtract 4 from 25: 3p = 21. Step 2: Divide by 3: p = 21 ÷ 3.",
        "21 ÷ 3 = 7.",
        "p = 7.",
        "3p = 21 -> p = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve for w: 4 × w - 8 = 24.",
        8, ["8"],
        "Add 8 to 24: 4w = 32. Divide by 4: w = 32 ÷ 4.",
        "32 ÷ 4 = 8.",
        "w = 8.",
        "4w = 32 -> w = 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which equation represents: 'A number k multiplied by 5, then added to 10, equals 45'?",
        "5k + 10 = 45",
        ["5 + k + 10 = 45", "k ÷ 5 + 10 = 45", "5k - 10 = 45"],
        "Translate words to algebra: k multiplied by 5 is 5k; add 10 is + 10; equals 45 is = 45.",
        "5k + 10 = 45.",
        "5k + 10 = 45.",
        "5k + 10 = 45 matches the sentence."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the value of k in: 5k + 10 = 45.",
        7, ["7"],
        "5k = 45 - 10 = 35. k = 35 ÷ 5.",
        "35 ÷ 5 = 7.",
        "k = 7.",
        "5k = 35 -> k = 7."
    ))

    # =========================================================================
    # LESSON 6: Place Value Structure (4.NBT.A.1 / 4.NBT.A.2)
    # =========================================================================
    LID = "G4_L06"
    LT = "Place Value Structure"
    DOM = "Place Value & Multi-Digit Arithmetic"
    STD = "4.NBT.A.1 / 4.NBT.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In the number 45,720, what is the value of the digit 5?",
        5000, ["5000", "5,000"],
        "The 5 is in the thousands place: 5 × 1,000 = 5,000.",
        "5 thousands = 5,000.",
        "5,000.",
        "The digit 5 is in the thousands place, with a value of 5,000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "How many times greater is the value of the 7 in 70,000 than the 7 in 7,000?",
        "10 times greater",
        ["100 times greater", "2 times greater", "1,000 times greater"],
        "In base ten, each place to the left is 10 times the value of the place to its right.",
        "Ten-thousands is 10 times thousands: 70,000 ÷ 7,000 = 10.",
        "10 times greater.",
        "70,000 is 10 times 7,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Write in standard form: 60,000 + 4,000 + 300 + 20 + 5.",
        64325, ["64325", "64,325"],
        "Combine the values in each place: 6 ten-thousands, 4 thousands, 3 hundreds, 2 tens, 5 ones.",
        "64,325.",
        "64,325.",
        "60,000 + 4,000 + 300 + 20 + 5 = 64,325."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which represents 308,045 in word form?",
        "Three hundred eight thousand, forty-five",
        ["Three hundred eighty thousand, forty-five", "Thirty-eight thousand, forty-five", "Three hundred eight thousand, four hundred five"],
        "Read by periods: 308 thousands (three hundred eight thousand), and 045 (forty-five).",
        "Three hundred eight thousand, forty-five.",
        "Three hundred eight thousand, forty-five.",
        "308,045 is three hundred eight thousand, forty-five."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the value of the digit 9 in 920,415?",
        900000, ["900000", "900,000"],
        "The 9 is in the hundred-thousands place: 9 × 100,000.",
        "900,000.",
        "900,000.",
        "The value is 900,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "How many tens are in 1,000?",
        100, ["100"],
        "Divide 1,000 by 10.",
        "1,000 ÷ 10 = 100.",
        "100 tens.",
        "1,000 ÷ 10 = 100 tens."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In the number 66,240, compare the 6 in the ten-thousands place to the 6 in the thousands place.",
        "The first 6 has 10 times the value of the second 6",
        ["The first 6 has the same value as the second 6", "The second 6 has 10 times the value of the first 6", "The first 6 has 100 times the value of the second 6"],
        "Ten-thousands (60,000) is 10 times thousands (6,000).",
        "60,000 ÷ 6,000 = 10.",
        "10 times the value.",
        "60,000 is 10 times 6,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the standard form of four hundred twelve thousand, six?",
        412006, ["412006", "412,006"],
        "412 thousands and 6 ones (with 0 hundreds and 0 tens).",
        "412,006.",
        "412,006.",
        "412,006."
    ))

    # =========================================================================
    # LESSON 7: Rounding & Comparing Numbers (4.NBT.A.2 / 4.NBT.A.3)
    # =========================================================================
    LID = "G4_L07"
    LT = "Rounding & Comparing Numbers"
    DOM = "Place Value & Multi-Digit Arithmetic"
    STD = "4.NBT.A.2 / 4.NBT.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Round 54,321 to the nearest thousand.",
        54000, ["54000", "54,000"],
        "Look at the hundreds digit (3). Since 3 < 5, round down to 54,000.",
        "54,000.",
        "54,000.",
        "54,321 rounds to 54,000 to the nearest thousand."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Compare 74,520 and 74,250. Which symbol belongs in 74,520 ___ 74,250?",
        ">",
        ["<", "=", "+"],
        "Compare place by place from left to right: ten-thousands are equal (7), thousands equal (4), hundreds: 5 > 2.",
        "74,520 > 74,250.",
        ">.",
        "74,520 > 74,250 because 5 hundreds is greater than 2 hundreds."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Round 368,490 to the nearest ten-thousand.",
        370000, ["370000", "370,000"],
        "Look at the thousands digit (8). Since 8 >= 5, round up: 360,000 becomes 370,000.",
        "370,000.",
        "370,000.",
        "368,490 rounds to 370,000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following numbers rounds to 500,000 when rounded to the nearest hundred-thousand?",
        "482,900",
        ["439,000", "562,000", "410,000"],
        "Look at the ten-thousands digit: in 482,900, the ten-thousands digit is 8 (>= 5), so it rounds up to 500,000.",
        "482,900 rounds to 500,000.",
        "482,900.",
        "482,900 rounds to 500,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Round 89,650 to the nearest hundred.",
        89700, ["89700", "89,700"],
        "Look at the tens digit (5). Since 5 >= 5, round up: 89,600 becomes 89,700.",
        "89,700.",
        "89,700.",
        "89,650 rounds to 89,700."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Round 499,800 to the nearest thousand.",
        500000, ["500000", "500,000"],
        "Hundreds digit is 8 (>= 5). Round 499 thousands up to 500 thousands.",
        "500,000.",
        "500,000.",
        "499,800 rounds up to 500,000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Order from least to greatest: 104,200; 140,020; 104,020.",
        "104,020 < 104,200 < 140,020",
        ["140,020 < 104,200 < 104,020", "104,200 < 104,020 < 140,020", "104,020 < 140,020 < 104,200"],
        "Compare: 104,020 has 0 hundreds, 104,200 has 2 hundreds, 140,020 has 4 ten-thousands.",
        "104,020 < 104,200 < 140,020.",
        "104,020 < 104,200 < 140,020.",
        "The correct order from least to greatest is 104,020 < 104,200 < 140,020."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Round 745,219 to the nearest hundred-thousand.",
        700000, ["700000", "700,000"],
        "The ten-thousands digit is 4 (< 5). Round down to 700,000.",
        "700,000.",
        "700,000.",
        "745,219 rounds to 700,000."
    ))

    # =========================================================================
    # LESSON 8: Multi-Digit Addition & Subtraction (4.NBT.B.4)
    # =========================================================================
    LID = "G4_L08"
    LT = "Multi-Digit Addition & Subtraction"
    DOM = "Place Value & Multi-Digit Arithmetic"
    STD = "4.NBT.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 42,518 + 23,461.",
        65979, ["65979", "65,979"],
        "Add place by place: 8+1=9, 1+6=7, 5+4=9, 2+3=5, 4+2=6.",
        "65,979.",
        "65,979.",
        "42,518 + 23,461 = 65,979."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 58,400 - 24,150.",
        "34,250",
        ["34,350", "34,150", "35,250"],
        "Subtract with regrouping: 0 - 0 = 0; regroup 10 - 5 = 5; 3 - 1 = 2; 8 - 4 = 4; 5 - 2 = 3.",
        "34,250.",
        "34,250.",
        "58,400 - 24,150 = 34,250."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 84,675 + 17,548.",
        102223, ["102223", "102,223"],
        "Add with regrouping across multiple places.",
        "84,675 + 17,548 = 102,223.",
        "102,223.",
        "84,675 + 17,548 = 102,223."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 100,000 - 45,678.",
        "54,322",
        ["54,422", "55,322", "64,322"],
        "Subtract across zeros: 10 - 8 = 2; 9 - 7 = 2; 9 - 6 = 3; 9 - 5 = 4; 9 - 4 = 5.",
        "54,322.",
        "54,322.",
        "100,000 - 45,678 = 54,322."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 63,412 - 28,655.",
        34757, ["34757", "34,757"],
        "Regroup ones, tens, and hundreds.",
        "63,412 - 28,655 = 34,757.",
        "34,757.",
        "63,412 - 28,655 = 34,757."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A stadium has 45,680 seats. 38,945 tickets were sold. How many seats are empty?",
        6735, ["6735", "6,735"],
        "Subtract tickets sold from total seats: 45,680 - 38,945.",
        "45,680 - 38,945 = 6,735.",
        "6,735 seats.",
        "45,680 - 38,945 = 6,735."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "City A has 215,400 residents. City B has 189,750 residents. How many more residents live in City A than City B?",
        "25,650",
        ["26,650", "25,750", "35,650"],
        "Subtract: 215,400 - 189,750.",
        "215,400 - 189,750 = 25,650.",
        "25,650.",
        "215,400 - 189,750 = 25,650 residents."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Add: 348,291 + 156,849.",
        505140, ["505140", "505,140"],
        "348,291 + 156,849 = 505,140.",
        "505,140.",
        "505,140.",
        "348,291 + 156,849 = 505,140."
    ))

    # =========================================================================
    # LESSON 9: Multi-Digit Multiplication (4.NBT.B.5)
    # =========================================================================
    LID = "G4_L09"
    LT = "Multi-Digit Multiplication"
    DOM = "Place Value & Multi-Digit Arithmetic"
    STD = "4.NBT.B.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 324 × 3.",
        972, ["972"],
        "Multiply each place: (300 × 3) + (20 × 3) + (4 × 3) = 900 + 60 + 12.",
        "900 + 60 + 12 = 972.",
        "972.",
        "324 × 3 = 972."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 45 × 12.",
        "540",
        ["520", "560", "450"],
        "Use partial products: (45 × 10) + (45 × 2) = 450 + 90.",
        "450 + 90 = 540.",
        "540.",
        "45 × 12 = 540."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Calculate: 1,425 × 4.",
        5700, ["5700", "5,700"],
        "Multiply: (1000 × 4) + (400 × 4) + (25 × 4) = 4000 + 1600 + 100.",
        "4000 + 1600 + 100 = 5,700.",
        "5,700.",
        "1,425 × 4 = 5,700."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Calculate: 28 × 34.",
        "952",
        ["922", "982", "852"],
        "Multiply partial products: 28 × 30 = 840; 28 × 4 = 112; 840 + 112 = 952.",
        "952.",
        "952.",
        "28 × 34 = 952."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 2,306 × 5.",
        11530, ["11530", "11,530"],
        "Multiply: 2000 × 5 = 10,000; 300 × 5 = 1,500; 6 × 5 = 30. Total = 11,530.",
        "11,530.",
        "11,530.",
        "2,306 × 5 = 11,530."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 63 × 47.",
        2961, ["2961", "2,961"],
        "Multiply: 63 × 40 = 2520; 63 × 7 = 441; 2520 + 441 = 2961.",
        "2,961.",
        "2,961.",
        "63 × 47 = 2,961."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A theater has 36 rows of seats with 28 seats in each row. How many seats are in the theater?",
        "1,008 seats",
        ["1,018 seats", "998 seats", "980 seats"],
        "Multiply rows by seats per row: 36 × 28.",
        "36 × 28 = 1,008.",
        "1,008 seats.",
        "36 × 28 = 1,008 seats."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 3,842 × 6.",
        23052, ["23052", "23,052"],
        "Multiply 3,842 by 6.",
        "3,842 × 6 = 23,052.",
        "23,052.",
        "3,842 × 6 = 23,052."
    ))

    # =========================================================================
    # LESSON 10: Multi-Digit Division (4.NBT.B.6)
    # =========================================================================
    LID = "G4_L10"
    LT = "Multi-Digit Division"
    DOM = "Place Value & Multi-Digit Arithmetic"
    STD = "4.NBT.B.6"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 1,284 ÷ 3.",
        428, ["428"],
        "Divide place by place: 12 hundreds ÷ 3 = 4 hundreds; 8 tens ÷ 3 = 2 tens R2; 24 ones ÷ 3 = 8 ones.",
        "428.",
        "428.",
        "1,284 ÷ 3 = 428."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 835 ÷ 5.",
        167, ["167"],
        "Divide: 8 hundreds ÷ 5 = 1 hundred R3; 33 tens ÷ 5 = 6 tens R3; 35 ones ÷ 5 = 7 ones.",
        "167.",
        "167.",
        "835 ÷ 5 = 167."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A box holds 6 donuts. How many full boxes can be filled with 130 donuts?",
        21, ["21", "21 boxes"],
        "Divide 130 by 6 to find the whole quotient.",
        "130 ÷ 6 = 21 with a remainder of 4.",
        "21 full boxes.",
        "130 ÷ 6 = 21 R4. 21 full boxes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In problem Q03 with 130 donuts packed 6 per box, how many donuts are left over?",
        4, ["4", "4 donuts"],
        "The leftover donuts equal the remainder: 130 - (21 × 6) = 130 - 126.",
        "4 donuts.",
        "4 donuts left over.",
        "Remainder is 4 donuts."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: 2,456 ÷ 4.",
        "614",
        ["612", "616", "624"],
        "24 hundreds ÷ 4 = 6 hundreds; 5 tens ÷ 4 = 1 ten R1; 16 ones ÷ 4 = 4 ones.",
        "614.",
        "614.",
        "2,456 ÷ 4 = 614."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 3,745 ÷ 7.",
        535, ["535"],
        "37 ÷ 7 = 5 R2; 24 ÷ 7 = 3 R3; 35 ÷ 7 = 5.",
        "535.",
        "535.",
        "3,745 ÷ 7 = 535."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the quotient and remainder of 427 ÷ 8?",
        "53 R3",
        ["53 R5", "52 R7", "54 R1"],
        "42 ÷ 8 = 5 R2; 27 ÷ 8 = 3 R3. Check: 53 × 8 = 424; 424 + 3 = 427.",
        "53 R3.",
        "53 R3.",
        "427 ÷ 8 = 53 with remainder 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 5,616 ÷ 9.",
        624, ["624"],
        "56 ÷ 9 = 6 R2; 21 ÷ 9 = 2 R3; 36 ÷ 9 = 4.",
        "624.",
        "624.",
        "5,616 ÷ 9 = 624."
    ))

    # =========================================================================
    # LESSON 11: Equivalent Fractions (4.NF.A.1)
    # =========================================================================
    LID = "G4_L11"
    LT = "Equivalent Fractions"
    DOM = "Fractions & Decimals"
    STD = "4.NF.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the missing numerator: 3/4 = ___/12.",
        9, ["9"],
        "Multiply numerator and denominator by 3 (since 4 × 3 = 12).",
        "3 × 3 = 9.",
        "9.",
        "3/4 = 9/12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which fraction is equivalent to 2/5?",
        "6/15",
        ["4/15", "5/10", "6/10"],
        "Multiply numerator and denominator of 2/5 by 3: (2×3)/(5×3) = 6/15.",
        "6/15 is equivalent.",
        "6/15.",
        "2/5 = 6/15."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Complete: 5/6 = 25/___.",
        30, ["30"],
        "The numerator was multiplied by 5 (5 × 5 = 25). Multiply denominator by 5: 6 × 5.",
        "6 × 5 = 30.",
        "30.",
        "5/6 = 25/30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Simplify the fraction 8/12 to simplest form.",
        "2/3",
        ["4/6", "3/4", "1/2"],
        "Divide both numerator and denominator by their greatest common factor, 4: (8÷4)/(12÷4).",
        "2/3.",
        "2/3.",
        "8/12 = 2/3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the missing numerator: 4/7 = ___/28.",
        16, ["16"],
        "7 × 4 = 28. Multiply numerator by 4: 4 × 4 = 16.",
        "16.",
        "16.",
        "4/7 = 16/28."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which pair of fractions are NOT equivalent?",
        "3/5 and 6/12",
        ["1/2 and 4/8", "2/3 and 8/12", "3/4 and 9/12"],
        "Check cross products or simplest forms: 3/5 = 0.6 while 6/12 = 1/2 = 0.5. They are not equal.",
        "3/5 and 6/12 are not equivalent.",
        "3/5 and 6/12.",
        "3/5 is not equal to 6/12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the simplest form numerator of 15/20?",
        3, ["3"],
        "Divide 15 and 20 by 5: 15 ÷ 5 = 3 and 20 ÷ 5 = 4.",
        "The simplified fraction is 3/4. The numerator is 3.",
        "3.",
        "15/20 = 3/4, numerator is 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the missing denominator: 7/8 = 21/___.",
        24, ["24"],
        "7 × 3 = 21. Multiply 8 by 3: 8 × 3 = 24.",
        "24.",
        "24.",
        "7/8 = 21/24."
    ))

    # =========================================================================
    # LESSON 12: Comparing Fractions (4.NF.A.2)
    # =========================================================================
    LID = "G4_L12"
    LT = "Comparing Fractions"
    DOM = "Fractions & Decimals"
    STD = "4.NF.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Compare 3/4 and 5/8. Which symbol belongs in 3/4 ___ 5/8?",
        ">",
        ["<", "=", "+"],
        "Find a common denominator: 3/4 = 6/8. Compare 6/8 and 5/8: 6 > 5.",
        "3/4 > 5/8.",
        ">.",
        "3/4 = 6/8 > 5/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Compare 2/3 and 4/5 by cross-multiplying: (2 × 5) ___ (3 × 4). Which is greater?",
        "4/5 is greater",
        ["2/3 is greater", "They are equal", "Cannot tell"],
        "Cross-multiply: 2 × 5 = 10; 3 × 4 = 12. Since 10 < 12, 2/3 < 4/5.",
        "4/5 is greater.",
        "4/5 is greater.",
        "4/5 = 12/15 > 2/3 = 10/15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Use benchmark 1/2 to compare: 3/8 and 5/6. Which statement is correct?",
        "3/8 < 1/2 and 5/6 > 1/2, so 3/8 < 5/6",
        ["Both are greater than 1/2", "Both are less than 1/2", "3/8 > 5/6"],
        "Half of 8 is 4 (so 3/8 < 1/2); half of 6 is 3 (so 5/6 > 1/2).",
        "3/8 < 5/6.",
        "3/8 < 1/2 and 5/6 > 1/2, so 3/8 < 5/6.",
        "Comparing to benchmark 1/2 shows 3/8 < 5/6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which fraction is greater: 5/12 or 7/12?",
        "7/12",
        ["5/12", "They are equal", "Neither"],
        "Same denominator 12: compare numerators. 7 > 5.",
        "7/12.",
        "7/12.",
        "7/12 is greater than 5/12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Compare 3/5 and 6/10. Which statement is true?",
        "3/5 = 6/10",
        ["3/5 > 6/10", "3/5 < 6/10", "They cannot be compared"],
        "Multiply numerator and denominator of 3/5 by 2: (3×2)/(5×2) = 6/10.",
        "3/5 = 6/10.",
        "3/5 = 6/10.",
        "3/5 and 6/10 are equivalent fractions."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which of the following is the greatest fraction: 1/3, 2/5, 5/8, 1/2?",
        "5/8",
        ["1/3", "2/5", "1/2"],
        "Convert to decimals or benchmark: 1/3 ≈ 0.33, 2/5 = 0.40, 1/2 = 0.50, 5/8 = 0.625.",
        "5/8 is the greatest.",
        "5/8.",
        "5/8 is greatest (0.625)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Compare 7/10 and 3/4. Common denominator is 20. Which fraction is larger?",
        "3/4 is larger",
        ["7/10 is larger", "They are equal", "Cannot determine"],
        "7/10 = 14/20; 3/4 = 15/20. 15/20 > 14/20.",
        "3/4 is larger.",
        "3/4 is larger.",
        "3/4 = 15/20 > 7/10 = 14/20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Which symbol makes this comparison true: 4/9 ___ 5/12?",
        ">",
        ["<", "=", "+"],
        "Cross-multiply: 4 × 12 = 48; 9 × 5 = 45. Since 48 > 45, 4/9 > 5/12.",
        ">.",
        ">.",
        "4/9 > 5/12."
    ))

    # =========================================================================
    # LESSON 13: Adding & Subtracting Fractions (4.NF.B.3a-b)
    # =========================================================================
    LID = "G4_L13"
    LT = "Adding & Subtracting Fractions"
    DOM = "Fractions & Decimals"
    STD = "4.NF.B.3a-b"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 3/8 + 2/8.",
        "5/8",
        ["5/16", "1/8", "6/8"],
        "When denominators are the same, add the numerators and keep the denominator: (3+2)/8.",
        "5/8.",
        "5/8.",
        "3/8 + 2/8 = 5/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 7/10 - 4/10.",
        "3/10",
        ["3/0", "11/10", "3/20"],
        "Subtract numerators: (7 - 4)/10.",
        "3/10.",
        "3/10.",
        "7/10 - 4/10 = 3/10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 1 and 2/5 + 2 and 1/5.",
        "3 and 3/5",
        ["3 and 3/10", "4 and 3/5", "3 and 1/5"],
        "Add whole numbers (1 + 2 = 3) and add fractions (2/5 + 1/5 = 3/5).",
        "3 and 3/5.",
        "3 and 3/5.",
        "1 2/5 + 2 1/5 = 3 3/5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 4 and 5/6 - 2 and 1/6.",
        "2 and 4/6",
        ["2 and 6/6", "2 and 3/6", "1 and 4/6"],
        "Subtract whole numbers (4 - 2 = 2) and subtract fractions (5/6 - 1/6 = 4/6).",
        "2 and 4/6.",
        "2 and 4/6 (or 2 and 2/3).",
        "4 5/6 - 2 1/6 = 2 4/6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the numerator of the sum: 4/9 + 3/9?",
        7, ["7"],
        "Add the numerators: 4 + 3 = 7. Denominator remains 9.",
        "7.",
        "7.",
        "4/9 + 3/9 = 7/9, numerator is 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve by regrouping: 3 and 1/4 - 1 and 3/4.",
        "1 and 2/4",
        ["1 and 3/4", "2 and 2/4", "1 and 1/4"],
        "Regroup 3 and 1/4 as 2 and 5/4. Then: (2 - 1) + (5/4 - 3/4) = 1 and 2/4.",
        "1 and 2/4 (or 1 and 1/2).",
        "1 and 2/4.",
        "3 1/4 - 1 3/4 = 2 5/4 - 1 3/4 = 1 2/4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is 5/8 + 7/8 written as a mixed number?",
        "1 and 4/8",
        ["1 and 2/8", "12/16", "2 and 1/8"],
        "5/8 + 7/8 = 12/8. Convert to mixed number: 12 ÷ 8 = 1 with 4 left over -> 1 and 4/8.",
        "1 and 4/8 (or 1 and 1/2).",
        "1 and 4/8.",
        "12/8 = 1 4/8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the numerator of: 11/12 - 5/12?",
        6, ["6"],
        "11 - 5 = 6. (Result is 6/12).",
        "6.",
        "6.",
        "11/12 - 5/12 = 6/12, numerator is 6."
    ))

    # =========================================================================
    # LESSON 14: Decomposing Fractions & Word Problems (4.NF.B.3c-d)
    # =========================================================================
    LID = "G4_L14"
    LT = "Decomposing Fractions & Word Problems"
    DOM = "Fractions & Decimals"
    STD = "4.NF.B.3c-d"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which expression decomposes 5/8 into a sum of unit fractions?",
        "1/8 + 1/8 + 1/8 + 1/8 + 1/8",
        ["5/1 + 5/1 + 5/1", "1/5 + 1/5 + 1/5 + 1/5 + 1/5", "2/8 + 4/8"],
        "Unit fractions have a numerator of 1: 1/8.",
        "Five copies of 1/8 added together.",
        "1/8 + 1/8 + 1/8 + 1/8 + 1/8.",
        "5/8 = 1/8 + 1/8 + 1/8 + 1/8 + 1/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which of the following shows another valid way to decompose 5/8?",
        "2/8 + 3/8",
        ["2/8 + 4/8", "1/8 + 5/8", "3/8 + 3/8"],
        "Find fractions with denominator 8 whose numerators sum to 5: 2 + 3 = 5.",
        "2/8 + 3/8 = 5/8.",
        "2/8 + 3/8.",
        "2/8 + 3/8 = 5/8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Maya walked 3/10 mile to the store and 4/10 mile to the library. How far did she walk in total?",
        "7/10 mile",
        ["7/20 mile", "1/10 mile", "1 mile"],
        "Add distances: 3/10 + 4/10 = 7/10.",
        "7/10 mile.",
        "7/10 mile.",
        "3/10 + 4/10 = 7/10 mile."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A recipe uses 2 and 3/4 cups of flour. Carlos has already added 1 and 1/4 cups. How much more flour is needed?",
        "1 and 2/4 cups",
        ["1 and 1/4 cups", "2 cups", "1 and 3/4 cups"],
        "Subtract: 2 3/4 - 1 1/4 = 1 2/4 cups.",
        "1 and 2/4 cups (or 1 1/2 cups).",
        "1 and 2/4 cups.",
        "2 3/4 - 1 1/4 = 1 2/4 cups."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many eighths must be added to 3/8 to make 1 whole (8/8)?",
        5, ["5"],
        "8/8 - 3/8 = 5/8, so 5 eighths are needed.",
        "5.",
        "5 eighths.",
        "3/8 + 5/8 = 8/8 = 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A pitcher had 7/8 quart of juice. The kids drank 4/8 quart. How much juice remains in the pitcher?",
        "3/8 quart",
        ["2/8 quart", "4/8 quart", "11/8 quart"],
        "Subtract: 7/8 - 4/8 = 3/8.",
        "3/8 quart.",
        "3/8 quart.",
        "7/8 - 4/8 = 3/8 quart."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which expression is NOT equal to 6/10?",
        "3/10 + 4/10",
        ["1/10 + 5/10", "2/10 + 4/10", "3/10 + 3/10"],
        "3/10 + 4/10 = 7/10 (which is not 6/10).",
        "3/10 + 4/10.",
        "3/10 + 4/10.",
        "3/10 + 4/10 = 7/10, not 6/10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Kiran ate 2/6 of a pizza and Sam ate 3/6 of the pizza. What is the numerator of the fraction of pizza eaten?",
        5, ["5"],
        "2/6 + 3/6 = 5/6. The numerator is 5.",
        "5.",
        "5.",
        "2/6 + 3/6 = 5/6, numerator is 5."
    ))

    # =========================================================================
    # LESSON 15: Multiplying Fractions by Whole Numbers (4.NF.B.4)
    # =========================================================================
    LID = "G4_L15"
    LT = "Multiplying Fractions by Whole Numbers"
    DOM = "Fractions & Decimals"
    STD = "4.NF.B.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: 3 × (2/5).",
        "6/5",
        ["5/5", "6/15", "5/8"],
        "Multiply the whole number by the numerator: (3 × 2)/5.",
        "6/5.",
        "6/5.",
        "3 × 2/5 = 6/5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the numerator of 4 × (3/7)?",
        12, ["12"],
        "Multiply 4 by 3 = 12. Result is 12/7.",
        "12.",
        "12.",
        "4 × 3/7 = 12/7, numerator is 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Each person gets 3/4 cup of soup. How much soup is needed for 5 people?",
        "15/4 cups",
        ["8/4 cups", "15/20 cups", "3/20 cups"],
        "Multiply 5 by 3/4: (5 × 3)/4 = 15/4 cups.",
        "15/4 cups (or 3 and 3/4 cups).",
        "15/4 cups.",
        "5 × 3/4 = 15/4 cups."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which product is equal to 6 × (1/3)?",
        "2",
        ["3", "6/18", "1"],
        "6 × (1/3) = 6/3 = 2 whole.",
        "6/3 = 2.",
        "2.",
        "6 × 1/3 = 6/3 = 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Calculate: 8 × (1/4). What whole number does this equal?",
        2, ["2"],
        "8 × 1/4 = 8/4 = 2.",
        "2.",
        "2.",
        "8 × 1/4 = 8/4 = 2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A runner jogs 2/3 of a mile every day for 4 days. How many total miles did the runner jog?",
        "8/3 miles",
        ["6/3 miles", "8/12 miles", "2 miles"],
        "Multiply 4 by 2/3: (4 × 2)/3 = 8/3 miles.",
        "8/3 miles (or 2 and 2/3 miles).",
        "8/3 miles.",
        "4 × 2/3 = 8/3 miles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Write 15/4 as a mixed number.",
        "3 and 3/4",
        ["3 and 1/4", "4 and 3/4", "2 and 3/4"],
        "Divide 15 by 4: 15 ÷ 4 = 3 with remainder 3 -> 3 and 3/4.",
        "3 and 3/4.",
        "3 and 3/4.",
        "15/4 = 3 3/4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate: 10 × (3/5). What whole number does this equal?",
        6, ["6"],
        "10 × 3/5 = 30/5 = 6.",
        "6.",
        "6.",
        "10 × 3/5 = 30/5 = 6."
    ))

    # =========================================================================
    # LESSON 16: Decimal Fractions (4.NF.C.5)
    # =========================================================================
    LID = "G4_L16"
    LT = "Decimal Fractions"
    DOM = "Fractions & Decimals"
    STD = "4.NF.C.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Express 3/10 as an equivalent fraction with denominator 100: 3/10 = ___/100.",
        30, ["30"],
        "Multiply numerator and denominator by 10: 3 × 10 = 30.",
        "30.",
        "30.",
        "3/10 = 30/100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 4/10 + 25/100.",
        "65/100",
        ["29/100", "29/110", "65/10"],
        "Convert 4/10 to 40/100. Then add: 40/100 + 25/100 = 65/100.",
        "65/100.",
        "65/100.",
        "4/10 + 25/100 = 40/100 + 25/100 = 65/100."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the numerator of: 7/10 + 18/100 when written as a fraction over 100?",
        88, ["88"],
        "7/10 = 70/100. 70 + 18 = 88.",
        "88.",
        "88.",
        "7/10 + 18/100 = 70/100 + 18/100 = 88/100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 50/100 + 3/10.",
        "80/100",
        ["53/100", "53/110", "8/10"],
        "3/10 = 30/100. 50/100 + 30/100 = 80/100.",
        "80/100 (which also equals 8/10).",
        "80/100.",
        "50/100 + 30/100 = 80/100."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the missing numerator: 9/10 = ___/100.",
        90, ["90"],
        "Multiply 9 by 10: 90.",
        "90.",
        "90.",
        "9/10 = 90/100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 6/10 + 40/100.",
        "100/100 (1 whole)",
        ["46/100", "46/110", "16/10"],
        "6/10 = 60/100. 60/100 + 40/100 = 100/100 = 1.",
        "100/100 (1 whole).",
        "100/100 (1 whole).",
        "60/100 + 40/100 = 100/100 = 1."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Calculate the numerator: 2/10 + 73/100 = ___/100.",
        93, ["93"],
        "2/10 = 20/100. 20 + 73 = 93.",
        "93.",
        "93.",
        "20/100 + 73/100 = 93/100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Which fraction is equivalent to 80/100?",
        "8/10",
        ["8/100", "80/10", "8/1"],
        "Divide numerator and denominator by 10: (80÷10)/(100÷10) = 8/10.",
        "8/10.",
        "8/10.",
        "80/100 = 8/10."
    ))

    # =========================================================================
    # LESSON 17: Decimal Notation & Comparison (4.NF.C.6 / 4.NF.C.7)
    # =========================================================================
    LID = "G4_L17"
    LT = "Decimal Notation & Comparison"
    DOM = "Fractions & Decimals"
    STD = "4.NF.C.6 / 4.NF.C.7"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the fraction 7/10 written as a decimal?",
        "0.7",
        ["0.07", "7.0", "0.70"],
        "Tenths have one digit after the decimal point: 7/10 = 0.7.",
        "0.7.",
        "0.7.",
        "7/10 = 0.7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the fraction 25/100 written as a decimal?",
        "0.25",
        ["2.5", "0.025", "0.205"],
        "Hundredths have two digits after the decimal point: 25/100 = 0.25.",
        "0.25.",
        "0.25.",
        "25/100 = 0.25."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Compare 0.6 and 0.45. Which symbol belongs in 0.6 ___ 0.45?",
        ">",
        ["<", "=", "+"],
        "Line up decimals: 0.60 vs 0.45. 60 hundredths is greater than 45 hundredths.",
        "0.6 > 0.45.",
        ">.",
        "0.6 = 0.60 > 0.45."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following is equivalent to 0.5?",
        "0.50",
        ["0.05", "5.0", "0.005"],
        "Trailing zeros after the last digit in a decimal do not change its value: 5 tenths = 50 hundredths.",
        "0.50.",
        "0.50.",
        "0.5 = 0.50."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is 3/100 written as a decimal?",
        "0.03",
        ["0.3", "0.30", "3.0"],
        "3 hundredths has a 0 in the tenths place and 3 in the hundredths place: 0.03.",
        "0.03.",
        "0.03.",
        "3/100 = 0.03."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Order from least to greatest: 0.32, 0.4, 0.08.",
        "0.08 < 0.32 < 0.4",
        ["0.4 < 0.32 < 0.08", "0.08 < 0.4 < 0.32", "0.32 < 0.08 < 0.4"],
        "Rewrite as hundredths: 0.08, 0.32, 0.40. Compare: 8 < 32 < 40.",
        "0.08 < 0.32 < 0.4.",
        "0.08 < 0.32 < 0.4.",
        "0.08 < 0.32 < 0.40."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Compare 0.72 and 0.8. Which statement is true?",
        "0.8 is greater than 0.72",
        ["0.72 is greater than 0.8", "They are equal", "0.72 is 10 times 0.8"],
        "Compare tenths: 8 tenths is greater than 7 tenths (0.80 > 0.72).",
        "0.8 > 0.72.",
        "0.8 is greater than 0.72.",
        "0.80 > 0.72."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "How many hundredths are in 0.8?",
        80, ["80"],
        "0.8 = 8 tenths = 80 hundredths.",
        "80.",
        "80.",
        "0.8 = 80 hundredths."
    ))

    # =========================================================================
    # LESSON 18: Measurement Size Relationships (4.MD.A.1)
    # =========================================================================
    LID = "G4_L18"
    LT = "Measurement Size Relationships"
    DOM = "Measurement & Data"
    STD = "4.MD.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "1 kilometer equals how many meters?",
        1000, ["1000", "1,000"],
        "The prefix 'kilo-' means 1,000. 1 km = 1,000 m.",
        "1,000.",
        "1,000 meters.",
        "1 km = 1,000 m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "How many centimeters are in 4 meters? (1 meter = 100 cm)",
        400, ["400", "400 cm"],
        "Multiply meters by 100: 4 × 100.",
        "400 cm.",
        "400.",
        "4 × 100 = 400 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "How many ounces are in 3 pounds? (1 pound = 16 ounces)",
        48, ["48", "48 oz"],
        "Multiply pounds by 16: 3 × 16.",
        "3 × 16 = 48 ounces.",
        "48.",
        "3 × 16 = 48 ounces."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "How many minutes are in 5 hours? (1 hour = 60 minutes)",
        "300 minutes",
        ["240 minutes", "360 minutes", "500 minutes"],
        "Multiply hours by 60: 5 × 60.",
        "5 × 60 = 300 minutes.",
        "300 minutes.",
        "5 × 60 = 300 minutes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many milliliters are in 6 liters? (1 liter = 1,000 mL)",
        6000, ["6000", "6,000"],
        "Multiply liters by 1,000: 6 × 1,000.",
        "6,000 mL.",
        "6,000.",
        "6 × 1,000 = 6,000 mL."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "How many feet are in 7 yards? (1 yard = 3 feet)",
        21, ["21", "21 feet"],
        "Multiply yards by 3: 7 × 3.",
        "7 × 3 = 21 feet.",
        "21.",
        "7 × 3 = 21 feet."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "How many seconds are in 4 minutes? (1 minute = 60 seconds)",
        "240 seconds",
        ["200 seconds", "260 seconds", "300 seconds"],
        "Multiply minutes by 60: 4 × 60.",
        "4 × 60 = 240 seconds.",
        "240 seconds.",
        "4 × 60 = 240 seconds."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "How many grams are in 8 kilograms? (1 kg = 1,000 g)",
        8000, ["8000", "8,000"],
        "Multiply kilograms by 1,000: 8 × 1,000.",
        "8,000 grams.",
        "8,000.",
        "8 × 1,000 = 8,000 g."
    ))

    # =========================================================================
    # LESSON 19: Measurement Word Problems (4.MD.A.2)
    # =========================================================================
    LID = "G4_L19"
    LT = "Measurement Word Problems"
    DOM = "Measurement & Data"
    STD = "4.MD.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Liam has a board that is 2 meters long. He cuts off 75 cm. How many centimeters of the board are left? (2 m = 200 cm)",
        125, ["125", "125 cm"],
        "Convert 2 m to 200 cm. Then subtract: 200 - 75.",
        "200 - 75 = 125 cm.",
        "125 cm.",
        "200 cm - 75 cm = 125 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A movie starts at 6:45 PM and lasts 1 hour and 30 minutes. What time does the movie end?",
        "8:15 PM",
        ["8:00 PM", "8:30 PM", "7:45 PM"],
        "Add 1 hour to 6:45 -> 7:45 PM. Add 30 minutes to 7:45 -> 8:15 PM.",
        "8:15 PM.",
        "8:15 PM.",
        "6:45 + 1 hr 30 min = 8:15 PM."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A baker had 5 kg of flour. She used 1,800 grams for bread. How many grams of flour does she have left? (5 kg = 5,000 g)",
        3200, ["3200", "3,200", "3200 g"],
        "Convert 5 kg = 5,000 g. Subtract: 5,000 - 1,800.",
        "5,000 - 1,800 = 3,200 g.",
        "3,200 g.",
        "5,000 - 1,800 = 3,200 grams."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Sofia bought a notebook for $3.75 and a pen for $1.50. She paid with a $10 bill. How much change did she receive?",
        "$4.75",
        ["$5.25", "$4.25", "$5.75"],
        "Total spent = $3.75 + $1.50 = $5.25. Change = $10.00 - $5.25 = $4.75.",
        "$4.75.",
        "$4.75.",
        "$10.00 - $5.25 = $4.75."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A bottle holds 2 liters of soda. Carlos pours out 650 mL. How many milliliters remain in the bottle? (2 L = 2,000 mL)",
        1350, ["1350", "1,350", "1350 mL"],
        "2,000 mL - 650 mL = 1,350 mL.",
        "1,350 mL.",
        "1,350.",
        "2,000 - 650 = 1,350 mL."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A runner jogs 3 km on Monday and 2,400 meters on Tuesday. What is the total distance jogged in meters? (3 km = 3,000 m)",
        5400, ["5400", "5,400", "5400 m"],
        "3,000 m + 2,400 m = 5,400 m.",
        "5,400 m.",
        "5,400.",
        "3,000 + 2,400 = 5,400 meters."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A bag of potatoes weighs 4 pounds. How many ounces does it weigh? (1 lb = 16 oz)",
        "64 ounces",
        ["48 ounces", "60 ounces", "72 ounces"],
        "Multiply pounds by 16: 4 × 16 = 64 ounces.",
        "64 ounces.",
        "64 ounces.",
        "4 × 16 = 64 ounces."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A football practice lasts 2 hours and 15 minutes. How many total minutes is that? (2 hours = 120 minutes)",
        135, ["135", "135 minutes"],
        "120 minutes + 15 minutes = 135 minutes.",
        "135 minutes.",
        "135.",
        "120 + 15 = 135 minutes."
    ))

    # =========================================================================
    # LESSON 20: Area & Perimeter of Rectangles (4.MD.A.3)
    # =========================================================================
    LID = "G4_L20"
    LT = "Area & Perimeter of Rectangles"
    DOM = "Measurement & Data"
    STD = "4.MD.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the perimeter of a rectangle with length 14 meters and width 8 meters in meters.",
        44, ["44", "44 m"],
        "Perimeter = 2 × (length + width) = 2 × (14 + 8) = 2 × 22.",
        "44 meters.",
        "44.",
        "2 × (14 + 8) = 44 m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Find the area of a rectangle with length 12 feet and width 7 feet.",
        "84 square feet",
        ["38 square feet", "72 square feet", "96 square feet"],
        "Area = length × width = 12 × 7 = 84 sq ft.",
        "84 sq ft.",
        "84 square feet.",
        "12 × 7 = 84 sq ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rectangular rug has an area of 96 square feet. Its length is 12 feet. What is its width in feet?",
        8, ["8", "8 feet"],
        "Width = Area ÷ length = 96 ÷ 12.",
        "96 ÷ 12 = 8 feet.",
        "8.",
        "96 ÷ 12 = 8 feet."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A square garden has a perimeter of 36 meters. What is the area of the garden?",
        "81 square meters",
        ["36 square meters", "72 square meters", "64 square meters"],
        "Step 1: Side = 36 ÷ 4 = 9 m. Step 2: Area = side × side = 9 × 9 = 81 sq m.",
        "81 sq m.",
        "81 square meters.",
        "Side = 36/4 = 9. Area = 9 × 9 = 81 sq m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A rectangle has a perimeter of 40 cm. If its length is 14 cm, what is its width in cm?",
        6, ["6", "6 cm"],
        "Perimeter = 2 × (length + width) = 40. Length + width = 20. Width = 20 - 14 = 6.",
        "6 cm.",
        "6.",
        "20 - 14 = 6 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rectangular backyard is 25 meters long and 16 meters wide. What is its area in square meters?",
        400, ["400", "400 sq m"],
        "Area = 25 × 16. (25 × 4 × 4 = 100 × 4 = 400).",
        "400 sq m.",
        "400.",
        "25 × 16 = 400 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which rectangle has a perimeter of 24 units and an area of 32 square units?",
        "Length 8 units, Width 4 units",
        ["Length 6 units, Width 6 units", "Length 10 units, Width 2 units", "Length 7 units, Width 5 units"],
        "Check: P = 2 × (8 + 4) = 24. Area = 8 × 4 = 32.",
        "8 by 4.",
        "Length 8 units, Width 4 units.",
        "8 × 4 = 32 and 2(8 + 4) = 24."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the perimeter of a rectangle that has an area of 45 square cm and a width of 5 cm?",
        28, ["28", "28 cm"],
        "Length = 45 ÷ 5 = 9 cm. Perimeter = 2 × (9 + 5) = 2 × 14 = 28 cm.",
        "28 cm.",
        "28.",
        "Length = 9. P = 2(9 + 5) = 28 cm."
    ))

    # =========================================================================
    # LESSON 21: Line Plots with Fractions (4.MD.B.4)
    # =========================================================================
    LID = "G4_L21"
    LT = "Line Plots with Fractions"
    DOM = "Measurement & Data"
    STD = "4.MD.B.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A line plot displays insect lengths in inches: four insects measure 3/8 inch and two measure 5/8 inch. How many insects were measured in total?",
        "6 insects",
        ["4 insects", "2 insects", "8 insects"],
        "Add the number of data points (X marks): 4 + 2 = 6.",
        "6 insects.",
        "6 insects.",
        "4 + 2 = 6 insects."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the difference between the longest insect (5/8 in) and shortest insect (3/8 in)?",
        "2/8 inch",
        ["1/8 inch", "8/8 inch", "2/16 inch"],
        "Subtract lengths: 5/8 - 3/8 = 2/8 inch.",
        "2/8 inch (or 1/4 inch).",
        "2/8 inch.",
        "5/8 - 3/8 = 2/8 inch."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the total combined length of 4 ribbons that each measure 1/4 inch? (in whole inches)",
        1, ["1", "1 inch"],
        "4 × (1/4) = 4/4 = 1 whole inch.",
        "1 inch.",
        "1.",
        "4 × 1/4 = 1 inch."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "On a line plot, there are measurements of 1/8, 1/4, 3/8, 1/2. Which measurement is equivalent to 2/8?",
        "1/4",
        ["1/8", "3/8", "1/2"],
        "Simplify 2/8: divide numerator and denominator by 2 -> 1/4.",
        "1/4.",
        "1/4.",
        "2/8 = 1/4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "If there are three ribbons of length 1/2 inch, what is the numerator of their combined length when written as an improper fraction over 2?",
        3, ["3"],
        "3 × 1/2 = 3/2. The numerator is 3.",
        "3.",
        "3.",
        "3 × 1/2 = 3/2, numerator is 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A line plot shows plant heights: 1/8, 2/8, 3/8, 4/8, 5/8, 6/8. What is the range between 6/8 and 1/8?",
        "5/8 inch",
        ["7/8 inch", "4/8 inch", "1/8 inch"],
        "Range = maximum - minimum: 6/8 - 1/8 = 5/8 inch.",
        "5/8 inch.",
        "5/8 inch.",
        "6/8 - 1/8 = 5/8 inch."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Two nails measure 3/4 inch and 1/2 inch. What is their combined length in inches? (Enter numerator when written over 4: e.g. 5 for 5/4)",
        5, ["5"],
        "Convert 1/2 to 2/4. Add: 3/4 + 2/4 = 5/4.",
        "5/4, so numerator is 5.",
        "5.",
        "3/4 + 2/4 = 5/4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If five pencil leads each measure 1/8 inch, what is their total length?",
        "5/8 inch",
        ["5/40 inch", "1/8 inch", "1 inch"],
        "5 × (1/8) = 5/8 inch.",
        "5/8 inch.",
        "5/8 inch.",
        "5 × 1/8 = 5/8 inch."
    ))

    # =========================================================================
    # LESSON 22: Understanding Angle Measurement (4.MD.C.5)
    # =========================================================================
    LID = "G4_L22"
    LT = "Understanding Angle Measurement"
    DOM = "Measurement & Data"
    STD = "4.MD.C.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "How many degrees are in one full complete circle rotation?",
        360, ["360", "360 degrees", "360°"],
        "A full turn around a circle is 360 degrees.",
        "360°.",
        "360 degrees.",
        "A full rotation is 360 degrees."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "How many degrees are in a right angle (one quarter of a circle turn)?",
        90, ["90", "90 degrees", "90°"],
        "A right angle is 1/4 of 360°: 360 ÷ 4 = 90°.",
        "90°.",
        "90 degrees.",
        "A right angle measures 90°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "An angle that measures less than 90° is called what type of angle?",
        "Acute angle",
        ["Obtuse angle", "Right angle", "Straight angle"],
        "Acute angles are greater than 0° and less than 90°.",
        "Acute angle.",
        "Acute angle.",
        "An angle less than 90° is acute."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "An angle that measures greater than 90° and less than 180° is called what?",
        "Obtuse angle",
        ["Acute angle", "Right angle", "Reflex angle"],
        "Obtuse angles are between 90° and 180°.",
        "Obtuse angle.",
        "Obtuse angle.",
        "An angle between 90° and 180° is obtuse."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many degrees are in a straight angle (a straight line)?",
        180, ["180", "180 degrees", "180°"],
        "A straight angle is half of a full turn: 360 ÷ 2 = 180°.",
        "180°.",
        "180 degrees.",
        "A straight angle measures 180°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "An angle turns through 1/6 of a circle. How many degrees does it measure? (360 ÷ 6)",
        60, ["60", "60 degrees", "60°"],
        "Calculate 360 ÷ 6 = 60°.",
        "60°.",
        "60 degrees.",
        "360 ÷ 6 = 60°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "An angle turns through 3/4 of a circle. How many degrees is that?",
        "270°",
        ["180°", "90°", "300°"],
        "3 × 90° = 270° (or 3/4 × 360° = 270°).",
        "270°.",
        "270°.",
        "3/4 × 360° = 270°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If an angle turns through 1/12 of a circle (like one hour on a clock face), how many degrees does it turn?",
        30, ["30", "30 degrees", "30°"],
        "360 ÷ 12 = 30°.",
        "30°.",
        "30.",
        "360 ÷ 12 = 30°."
    ))

    # =========================================================================
    # LESSON 23: Measuring & Adding Angles (4.MD.C.6 / 4.MD.C.7)
    # =========================================================================
    LID = "G4_L23"
    LT = "Measuring & Adding Angles"
    DOM = "Measurement & Data"
    STD = "4.MD.C.6 / 4.MD.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Two adjacent angles form a right angle (90°). If one angle measures 35°, what is the measure of the other angle in degrees?",
        55, ["55", "55°", "55 degrees"],
        "Complementary angles sum to 90°: 90 - 35 = 55°.",
        "90 - 35 = 55°.",
        "55°.",
        "90° - 35° = 55°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Two adjacent angles form a straight line (180°). If one angle is 110°, what is the other angle in degrees?",
        70, ["70", "70°", "70 degrees"],
        "Supplementary angles sum to 180°: 180 - 110 = 70°.",
        "180 - 110 = 70°.",
        "70°.",
        "180° - 110° = 70°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "An angle is decomposed into two smaller angles measuring 42° and 38°. What is the total angle measure in degrees?",
        80, ["80", "80°", "80 degrees"],
        "Angle addition postulate: Add the parts together: 42 + 38 = 80°.",
        "80°.",
        "80°.",
        "42° + 38° = 80°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A 125° angle is split into two angles. One angle is 50°. What is the unknown angle?",
        "75°",
        ["65°", "85°", "175°"],
        "Subtract known angle from total: 125 - 50 = 75°.",
        "75°.",
        "75°.",
        "125° - 50° = 75°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Three angles meet at a point to form a straight line (180°). Two of the angles are 50° and 65°. What is the third angle in degrees?",
        65, ["65", "65°", "65 degrees"],
        "50 + 65 = 115°. 180 - 115 = 65°.",
        "65°.",
        "65°.",
        "180 - (50 + 65) = 65°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "What tool is used to measure and sketch angles in degrees?",
        "Protractor",
        ["Compass", "Ruler", "Thermometer"],
        "A protractor has degree markings from 0° to 180° for measuring angles.",
        "Protractor.",
        "Protractor.",
        "A protractor measures angles in degrees."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A right angle is split into 3 equal angles. How many degrees does each angle measure?",
        30, ["30", "30°", "30 degrees"],
        "90 ÷ 3 = 30°.",
        "30°.",
        "30°.",
        "90° ÷ 3 = 30°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Two angles form a straight angle. One angle measures 135°. What is the measure of the second angle in degrees?",
        45, ["45", "45°", "45 degrees"],
        "180 - 135 = 45°.",
        "45°.",
        "45°.",
        "180° - 135° = 45°."
    ))

    # =========================================================================
    # LESSON 24: Lines, Angles & Shape Symmetry (4.G.A.1 / 4.G.A.3)
    # =========================================================================
    LID = "G4_L24"
    LT = "Lines, Angles & Shape Symmetry"
    DOM = "Geometry & Financial Literacy"
    STD = "4.G.A.1 / 4.G.A.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Lines that never intersect and stay the exact same distance apart are called what?",
        "Parallel lines",
        ["Perpendicular lines", "Intersecting lines", "Rays"],
        "Parallel lines run side-by-side forever without touching.",
        "Parallel lines.",
        "Parallel lines.",
        "Parallel lines never intersect."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Lines that intersect at a 90° right angle are called what?",
        "Perpendicular lines",
        ["Parallel lines", "Collinear lines", "Curved lines"],
        "Perpendicular lines form square 90° corners.",
        "Perpendicular lines.",
        "Perpendicular lines.",
        "Perpendicular lines meet at right angles (90°)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "How many lines of symmetry does a square have?",
        4, ["4", "4 lines"],
        "A square can be folded symmetrically along 2 diagonals and 2 midlines: 4 lines of symmetry.",
        "4 lines of symmetry.",
        "4.",
        "A square has 4 lines of symmetry."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A geometric figure that starts at an endpoint and goes on forever in one direction is called a:",
        "Ray",
        ["Line segment", "Line", "Point"],
        "A ray has 1 endpoint and extends infinitely in 1 direction.",
        "Ray.",
        "Ray.",
        "A ray has one endpoint and extends infinitely in one direction."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many lines of symmetry does a non-square rectangle have?",
        2, ["2", "2 lines"],
        "A rectangle has 2 lines of symmetry (horizontal and vertical through centers of opposite sides).",
        "2 lines.",
        "2.",
        "A rectangle has 2 lines of symmetry."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which triangle has all three sides of equal length?",
        "Equilateral triangle",
        ["Isosceles triangle", "Scalene triangle", "Right triangle"],
        "Equilateral triangles have 3 equal sides and 3 equal 60° angles.",
        "Equilateral triangle.",
        "Equilateral triangle.",
        "An equilateral triangle has all 3 sides equal."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A triangle with one 90° angle is called a:",
        "Right triangle",
        ["Acute triangle", "Obtuse triangle", "Equilateral triangle"],
        "A right triangle has exactly one right angle.",
        "Right triangle.",
        "Right triangle.",
        "A triangle with a 90° angle is a right triangle."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "How many lines of symmetry does an equilateral triangle have?",
        3, ["3", "3 lines"],
        "An equilateral triangle has 3 lines of symmetry (one through each vertex).",
        "3.",
        "3.",
        "An equilateral triangle has 3 lines of symmetry."
    ))

    # =========================================================================
    # LESSON 25: Classifying Shapes & Financial Literacy (4.G.A.2)
    # =========================================================================
    LID = "G4_L25"
    LT = "Classifying Shapes & Financial Literacy"
    DOM = "Geometry & Financial Literacy"
    STD = "4.G.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which quadrilateral has exactly one pair of parallel sides?",
        "Trapezoid",
        ["Parallelogram", "Rectangle", "Rhombus"],
        "By the standard definition, a trapezoid has exactly one pair of parallel opposite sides.",
        "Trapezoid.",
        "Trapezoid.",
        "A trapezoid has one pair of parallel sides."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which quadrilateral has 4 equal sides but not necessarily 90° angles?",
        "Rhombus",
        ["Rectangle", "Trapezoid", "Kite"],
        "A rhombus is an equilateral parallelogram.",
        "Rhombus.",
        "Rhombus.",
        "A rhombus has 4 equal sides."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A book costs $15.00. Sales tax is $1.20. What is the total cost in dollars and cents? (Enter 16.20)",
        16.2, ["16.2", "16.20", "$16.20"],
        "Add price and tax: $15.00 + $1.20 = $16.20.",
        "$16.20.",
        "16.20.",
        "$15.00 + $1.20 = $16.20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A video game originally costs $40. It is on sale with a $15 discount. What is the sale price?",
        "$25",
        ["$35", "$20", "$30"],
        "Subtract discount from original price: $40 - $15 = $25.",
        "$25.",
        "$25.",
        "$40 - $15 = $25."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Leo pays for a $13.50 lunch with a $20 bill. How many dollars in change does he receive? (Enter 6.50)",
        6.5, ["6.5", "6.50", "$6.50"],
        "Subtract: $20.00 - $13.50 = $6.50.",
        "$6.50.",
        "6.50.",
        "$20.00 - $13.50 = $6.50."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which shape is always both a rectangle and a rhombus?",
        "Square",
        ["Parallelogram", "Trapezoid", "Pentagon"],
        "A square has 4 right angles (rectangle) AND 4 equal sides (rhombus).",
        "Square.",
        "Square.",
        "A square is both a rectangle and a rhombus."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Maya saves $5 every week. How many dollars will she save after 12 weeks?",
        60, ["60", "$60"],
        "Multiply savings per week by number of weeks: 5 × 12 = 60.",
        "$60.",
        "60.",
        "5 × 12 = $60."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Which term describes money you earn from a job or allowance?",
        "Income",
        ["Expense", "Tax", "Debt"],
        "Income is money received or earned.",
        "Income.",
        "Income.",
        "Money earned is income."
    ))

    return questions
'''

with open('scripts/builders/grade_4.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated scripts/builders/grade_4.py successfully!")
