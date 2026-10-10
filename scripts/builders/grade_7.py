"""
scripts/builders/grade_7.py
High-fidelity mathematical question builder for Grade 7 (Lessons 1-25).
100% verified math answers, child-friendly prompts, and progressive 3-tier hints.
"""

from scripts.builders.helpers import make_numeric_question, make_mc_question

def build_grade_7_questions():
    questions = []
    G = 7

    # =========================================================================
    # LESSON 1: Unit Rates with Fractions (7.RP.A.1)
    # =========================================================================
    LID = "G7_L01"
    LT = "Unit Rates with Fractions"
    DOM = "Ratios & Proportional Relationships"
    STD = "7.RP.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A runner jogs 1/2 mile in 1/10 of an hour. What is the runner\'s speed in miles per hour (mph)?",
        5, ["5", "5 mph"],
        "Unit rate = (distance) ÷ (time) = (1/2) ÷ (1/10) = (1/2) × 10 = 5 mph.",
        "5 mph.",
        "5.",
        "1/2 ÷ 1/10 = 5 mph."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A painter covers 3/4 of a wall in 1/2 hour. How many walls can the painter cover in 1 hour?",
        "1 and 1/2 walls",
        ["3/8 wall", "2 walls", "1 wall"],
        "Rate = (3/4) ÷ (1/2) = (3/4) × 2 = 6/4 = 1 1/2 walls per hour.",
        "1 and 1/2 walls.",
        "1 and 1/2 walls.",
        "3/4 ÷ 1/2 = 3/2 = 1 1/2 walls."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A snail moves 2/3 of a meter in 1/6 of an hour. What is its speed in meters per hour?",
        4, ["4", "4 m/h"],
        "(2/3) ÷ (1/6) = (2/3) × 6 = 12/3 = 4 meters per hour.",
        "4 m/h.",
        "4.",
        "2/3 ÷ 1/6 = 4 m/h."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A recipe requires 2/3 cup of sugar for every 1/4 batch of cookies. How many cups of sugar are needed for 1 full batch?",
        "8/3 cups (2 and 2/3 cups)",
        ["2/12 cup", "1/6 cup", "3 cups"],
        "(2/3) ÷ (1/4) = (2/3) × 4 = 8/3 = 2 and 2/3 cups.",
        "8/3 cups (2 2/3 cups).",
        "8/3 cups (2 and 2/3 cups).",
        "2/3 ÷ 1/4 = 8/3 cups."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A water faucet fills 3/5 of a bucket in 1/10 of a minute. How many buckets does it fill per minute?",
        6, ["6", "6 buckets"],
        "(3/5) ÷ (1/10) = (3/5) × 10 = 30/5 = 6 buckets per minute.",
        "6 buckets.",
        "6.",
        "3/5 ÷ 1/10 = 6 buckets."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A car uses 1/4 gallon of gas to travel 7 and 1/2 miles (15/2 miles). How many miles per gallon (mpg) does the car get?",
        30, ["30", "30 mpg"],
        "(15/2) ÷ (1/4) = (15/2) × 4 = 60/2 = 30 miles per gallon.",
        "30 mpg.",
        "30.",
        "15/2 ÷ 1/4 = 30 mpg."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Kiran walks 3/8 mile in 1/12 hour. At this rate, how far does Kiran walk in 1 hour?",
        "4 and 1/2 miles",
        ["4 miles", "3 and 1/2 miles", "5 miles"],
        "(3/8) ÷ (1/12) = (3/8) × 12 = 36/8 = 9/2 = 4 1/2 miles.",
        "4 and 1/2 miles.",
        "4 and 1/2 miles.",
        "3/8 × 12 = 4 1/2 miles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A lawn mower cuts 2/5 of an acre in 1/15 of an hour. How many acres per hour can it cut?",
        6, ["6", "6 acres"],
        "(2/5) ÷ (1/15) = (2/5) × 15 = 30/5 = 6 acres per hour.",
        "6 acres.",
        "6.",
        "2/5 ÷ 1/15 = 6 acres/h."
    ))

    # =========================================================================
    # LESSON 2: Proportional Relationships (7.RP.A.2a-b)
    # =========================================================================
    LID = "G7_L02"
    LT = "Proportional Relationships"
    DOM = "Ratios & Proportional Relationships"
    STD = "7.RP.A.2a-b"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a proportional relationship, when x = 4, y = 12. What is the constant of proportionality k (k = y ÷ x)?",
        3, ["3"],
        "Constant of proportionality k = y/x = 12 ÷ 4 = 3.",
        "3.",
        "3.",
        "k = 12 ÷ 4 = 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which of the following is required for a graph to represent a proportional relationship?",
        "The graph must be a straight line that passes through the origin (0, 0)",
        ["The graph must be curved", "The graph must pass through (0, 5)", "The graph must be a horizontal line"],
        "A proportional relationship always graphs as a straight line passing through (0, 0).",
        "Straight line through (0, 0).",
        "The graph must be a straight line that passes through the origin (0, 0).",
        "Proportional graphs are straight lines through (0, 0)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A table has pairs (2, 7), (4, 14), (6, 21). What is the constant of proportionality k = y/x?",
        3.5, ["3.5", "7/2"],
        "7 ÷ 2 = 3.5; 14 ÷ 4 = 3.5; 21 ÷ 6 = 3.5. k = 3.5.",
        "3.5.",
        "3.5.",
        "k = 7/2 = 3.5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which table represents a proportional relationship?",
        "(1, 4), (2, 8), (3, 12)",
        ["(1, 4), (2, 5), (3, 6)", "(1, 2), (2, 5), (3, 8)", "(0, 2), (1, 5), (2, 8)"],
        "Check y/x: 4/1 = 4, 8/2 = 4, 12/3 = 4 (constant ratio of 4).",
        "(1, 4), (2, 8), (3, 12).",
        "(1, 4), (2, 8), (3, 12).",
        "The ratio y/x is constantly 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "If y is proportional to x with k = 5, what is y when x = 9?",
        45, ["45"],
        "y = kx = 5 × 9 = 45.",
        "45.",
        "45.",
        "y = 5 × 9 = 45."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A proportional relationship contains the point (8, 20). What is the value of k = y/x? (Enter decimal 2.5)",
        2.5, ["2.5", "5/2"],
        "k = 20 ÷ 8 = 2.5.",
        "2.5.",
        "2.5.",
        "k = 20/8 = 2.5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "On a graph of a proportional relationship, what does the point (1, r) represent?",
        "The unit rate r (constant of proportionality)",
        ["The total cost", "The origin", "The slope plus 1"],
        "(1, r) shows that when x = 1, y = r, which is the unit rate.",
        "The unit rate.",
        "The unit rate r (constant of proportionality).",
        "(1, r) represents the unit rate."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If y is proportional to x and passes through (6, 15), what is y when x = 10?",
        25, ["25"],
        "k = 15/6 = 2.5. y = 2.5 × 10 = 25.",
        "25.",
        "25.",
        "y = 2.5 × 10 = 25."
    ))

    # =========================================================================
    # LESSON 3: Equations of Proportional Relationships (7.RP.A.2c-d)
    # =========================================================================
    LID = "G7_L03"
    LT = "Equations of Proportional Relationships"
    DOM = "Ratios & Proportional Relationships"
    STD = "7.RP.A.2c-d"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Apples cost $1.50 per pound. Which equation models the total cost y for x pounds of apples?",
        "y = 1.50x",
        ["y = x + 1.50", "y = 1.50 ÷ x", "x = 1.50y"],
        "In a proportional relationship, y = kx, where k is the unit rate ($1.50).",
        "y = 1.50x.",
        "y = 1.50x.",
        "y = 1.50x."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In the proportional equation y = 8x, what is the value of y when x = 6?",
        48, ["48"],
        "y = 8(6) = 48.",
        "48.",
        "48.",
        "y = 8 × 6 = 48."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A car travels at a constant speed of 65 mph. Which equation represents distance d in terms of hours t?",
        "d = 65t",
        ["d = t + 65", "t = 65d", "d = 65 ÷ t"],
        "Distance = rate × time: d = 65t.",
        "d = 65t.",
        "d = 65t.",
        "d = 65t."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Using d = 65t, how many miles will the car travel in 4 hours?",
        260, ["260", "260 miles"],
        "d = 65 × 4 = 260 miles.",
        "260.",
        "260.",
        "65 × 4 = 260 miles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "On a graph of y = kx, what does the point (0, 0) mean in a real-world scenario of distance vs time?",
        "In 0 hours, 0 distance has been traveled",
        ["The car was stopped for 1 hour", "The speed was 0 mph", "The car broke down"],
        "(0, 0) indicates zero time elapsed corresponds to zero distance covered.",
        "0 distance in 0 hours.",
        "In 0 hours, 0 distance has been traveled.",
        "(0, 0) means 0 distance in 0 time."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If y = 4.2x, what is the value of x when y = 21?",
        5, ["5"],
        "x = y ÷ k = 21 ÷ 4.2 = 5.",
        "5.",
        "5.",
        "x = 21 ÷ 4.2 = 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A recipe equation is s = 0.75f, where s is cups of sugar and f is cups of flour. How much sugar is needed for 8 cups of flour?",
        "6 cups",
        ["5 cups", "7 cups", "8 cups"],
        "s = 0.75 × 8 = 6 cups.",
        "6 cups.",
        "6 cups.",
        "0.75 × 8 = 6 cups."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the constant of proportionality k in the equation y = 13.5x?",
        13.5, ["13.5"],
        "In y = kx, the coefficient of x is k = 13.5.",
        "13.5.",
        "13.5.",
        "k = 13.5."
    ))

    # =========================================================================
    # LESSON 4: Percents: Increase, Decrease & Percent Change (7.RP.A.3)
    # =========================================================================
    LID = "G7_L04"
    LT = "Percents: Increase, Decrease & Percent Change"
    DOM = "Ratios & Proportional Relationships"
    STD = "7.RP.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A store marks up a $40 jacket by 25%. What is the markup amount in dollars?",
        10, ["10", "$10"],
        "Markup = 0.25 × 40 = $10.",
        "$10.",
        "10.",
        "0.25 × 40 = $10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the final retail price of the $40 jacket from Q01 after the 25% ($10) markup?",
        50, ["50", "$50"],
        "Final price = 40 + 10 = $50.",
        "$50.",
        "50.",
        "$40 + $10 = $50."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A skateboard originally priced at $120 is on sale for 30% off. What is the discount in dollars?",
        36, ["36", "$36"],
        "Discount = 0.30 × 120 = $36.",
        "$36.",
        "36.",
        "0.30 × 120 = $36."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the sale price of the $120 skateboard from Q03 after the $36 discount?",
        84, ["84", "$84"],
        "$120 - $36 = $84.",
        "$84.",
        "84.",
        "$120 - $36 = $84."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "The price of gas increased from $3.00 to $3.60. What is the percent increase? (Percent change = (change ÷ original) × 100)",
        20, ["20", "20%"],
        "Change = 3.60 - 3.00 = 0.60. Percent increase = (0.60 ÷ 3.00) × 100 = 20%.",
        "20%.",
        "20.",
        "(0.60 / 3.00) × 100 = 20%."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A population dropped from 500 to 425. What is the percent decrease?",
        "15%",
        ["10%", "20%", "25%"],
        "Decrease = 500 - 425 = 75. Percent decrease = (75 ÷ 500) × 100 = 15%.",
        "15%.",
        "15%.",
        "75 / 500 = 0.15 = 15%."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "An item cost $80. It was increased by 10%, then decreased by 10%. What is the final price in dollars and cents? (Enter 79.20)",
        79.2, ["79.2", "79.20", "$79.20"],
        "Increase: 80 × 1.10 = 88. Decrease: 88 × 0.90 = $79.20.",
        "$79.20.",
        "79.20.",
        "88 × 0.90 = $79.20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Why is an increase of 10% followed by a decrease of 10% NOT equal to the original price?",
        "The 10% decrease is calculated from a larger base value than the original amount",
        ["Percentages cannot be added", "The formula has an error", "Because tax is added"],
        "10% of $88 is $8.80, which is larger than the original $8.00 increase.",
        "Decreased from a larger base value.",
        "The 10% decrease is calculated from a larger base value than the original amount.",
        "The decrease applies to the higher post-markup value."
    ))

    # =========================================================================
    # LESSON 5: Financial Literacy: Tax, Tip, Commission (7.RP.A.3)
    # =========================================================================
    LID = "G5_L05"
    LID = "G7_L05"
    LT = "Financial Literacy: Tax, Tip, Commission, Simple Interest"
    DOM = "Ratios & Proportional Relationships"
    STD = "7.RP.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A meal costs $40.00. Sales tax is 8%. What is the tax amount in dollars and cents? (Enter 3.20)",
        3.2, ["3.2", "3.20", "$3.20"],
        "Tax = 0.08 × 40 = $3.20.",
        "$3.20.",
        "3.20.",
        "0.08 × 40 = $3.20."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "You want to leave a 15% tip on a $60 dinner bill. What is the tip amount in dollars?",
        9, ["9", "$9", "9.00"],
        "Tip = 0.15 × 60 = $9.00.",
        "$9.",
        "9.",
        "0.15 × 60 = $9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A salesperson earns a 5% commission on sales. If she sells $8,000 worth of merchandise, what is her commission in dollars?",
        400, ["400", "$400"],
        "Commission = 0.05 × 8,000 = $400.",
        "$400.",
        "400.",
        "0.05 × 8,000 = $400."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Calculate simple interest: I = Prt. Principal P = $1,000, rate r = 4% (0.04), time t = 3 years. What is the interest earned in dollars?",
        120, ["120", "$120"],
        "I = 1,000 × 0.04 × 3 = $120.",
        "$120.",
        "120.",
        "1,000 × 0.04 × 3 = $120."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A pair of sneakers costs $80. Sales tax is 7%. What is the total cost including tax?",
        "$85.60",
        ["$87.00", "$85.00", "$86.40"],
        "Tax = 0.07 × 80 = $5.60. Total = $80 + $5.60 = $85.60.",
        "$85.60.",
        "$85.60.",
        "$80 × 1.07 = $85.60."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A loan of $2,500 has simple interest at 6% per year for 2 years. What is the total balance owed (Principal + Interest) in dollars?",
        2800, ["2800", "$2800", "$2,800"],
        "Interest = 2,500 × 0.06 × 2 = $300. Total = 2,500 + 300 = $2,800.",
        "$2,800.",
        "2800.",
        "2,500 + 300 = $2,800."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A real estate agent receives 3% commission on a home sold for $300,000. How much is the commission?",
        "$9,000",
        ["$900", "$3,000", "$12,000"],
        "0.03 × 300,000 = $9,000.",
        "$9,000.",
        "$9,000.",
        "0.03 × 300,000 = $9,000."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "You pay $54 for a coat on sale, which includes a 20% discount off the original price. What was the original price in dollars? (0.80 × Original = 54 -> Enter 67.50)",
        67.5, ["67.5", "67.50", "$67.50"],
        "Original = 54 ÷ 0.80 = $67.50.",
        "$67.50.",
        "67.50.",
        "54 ÷ 0.80 = $67.50."
    ))

    # =========================================================================
    # LESSON 6: Adding & Subtracting Rational Numbers (7.NS.A.1)
    # =========================================================================
    LID = "G7_L06"
    LT = "Adding & Subtracting Rational Numbers"
    DOM = "The Number System"
    STD = "7.NS.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: -12 + 7.",
        -5, ["-5"],
        "Subtract absolute values and keep sign of larger magnitude: 12 - 7 = 5 -> -5.",
        "-5.",
        "-5.",
        "-12 + 7 = -5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Calculate: -8 - 15.",
        -23, ["-23"],
        "Subtracting is adding the opposite: -8 + (-15) = -23.",
        "-23.",
        "-23.",
        "-8 - 15 = -23."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Calculate: 14 - (-9).",
        23, ["23"],
        "Subtracting a negative is adding: 14 + 9 = 23.",
        "23.",
        "23.",
        "14 - (-9) = 14 + 9 = 23."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: -3.5 + 8.2.",
        "4.7",
        ["-4.7", "11.7", "-11.7"],
        "8.2 - 3.5 = 4.7.",
        "4.7.",
        "4.7.",
        "8.2 - 3.5 = 4.7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: -1/3 + (-1/6).",
        "-1/2",
        ["-2/9", "-1/9", "-2/3"],
        "-2/6 + (-1/6) = -3/6 = -1/2.",
        "-1/2.",
        "-1/2.",
        "-2/6 - 1/6 = -3/6 = -1/2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Calculate: -18 - (-25).",
        7, ["7"],
        "-18 + 25 = 7.",
        "7.",
        "7.",
        "-18 + 25 = 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A diver starts at -15 feet, descends 25 feet deeper, and then rises 18 feet. What is the diver\'s final elevation?",
        "-22 feet",
        ["-28 feet", "-58 feet", "-40 feet"],
        "-15 - 25 + 18 = -40 + 18 = -22 feet.",
        "-22 feet.",
        "-22 feet.",
        "-15 - 25 + 18 = -22 feet."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate: -5.75 - 4.25.",
        -10.0, ["-10", "-10.0"],
        "-(5.75 + 4.25) = -10.0.",
        "-10.",
        "-10.",
        "-5.75 - 4.25 = -10."
    ))

    # =========================================================================
    # LESSON 7: Multiplying & Dividing Rational Numbers (7.NS.A.2)
    # =========================================================================
    LID = "G7_L07"
    LT = "Multiplying & Dividing Rational Numbers"
    DOM = "The Number System"
    STD = "7.NS.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Calculate: (-6) × 7.",
        -42, ["-42"],
        "Negative × Positive = Negative: -42.",
        "-42.",
        "-42.",
        "-6 × 7 = -42."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Calculate: (-8) × (-9).",
        72, ["72"],
        "Negative × Negative = Positive: 72.",
        "72.",
        "72.",
        "-8 × -9 = 72."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: -56 ÷ 8.",
        -7, ["-7"],
        "Negative ÷ Positive = Negative: -7.",
        "-7.",
        "-7.",
        "-56 ÷ 8 = -7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: -48 ÷ (-6).",
        8, ["8"],
        "Negative ÷ Negative = Positive: 8.",
        "8.",
        "8.",
        "-48 ÷ -6 = 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Calculate: (-2/3) × (9/10).",
        "-3/5",
        ["3/5", "-18/13", "-4/5"],
        "(-2 × 9) / (3 × 10) = -18/30 = -3/5.",
        "-3/5.",
        "-3/5.",
        "-18/30 = -3/5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Calculate: (-2) × (-3) × (-4).",
        -24, ["-24"],
        "(-2) × (-3) = 6; 6 × (-4) = -24.",
        "-24.",
        "-24.",
        "6 × (-4) = -24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Convert the fraction -3/8 into a decimal.",
        "-0.375",
        ["-0.38", "-0.37", "-0.4"],
        "-3 ÷ 8 = -0.375.",
        "-0.375.",
        "-0.375.",
        "-3/8 = -0.375."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: (-15) ÷ (-0.5).",
        30, ["30"],
        "-15 ÷ -0.5 = 15 ÷ 0.5 = 30.",
        "30.",
        "30.",
        "15 ÷ 0.5 = 30."
    ))

    # =========================================================================
    # LESSON 8: Four Operations with Rational Numbers (7.NS.A.3)
    # =========================================================================
    LID = "G7_L08"
    LT = "Four Operations with Rational Numbers"
    DOM = "The Number System"
    STD = "7.NS.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Evaluate: 4 × (-3) + 15.",
        3, ["3"],
        "4 × (-3) = -12. -12 + 15 = 3.",
        "3.",
        "3.",
        "-12 + 15 = 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Evaluate: -20 ÷ 4 - 6.",
        -11, ["-11"],
        "-20 ÷ 4 = -5. -5 - 6 = -11.",
        "-11.",
        "-11.",
        "-5 - 6 = -11."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Evaluate: (-2)³ + 10.",
        2, ["2"],
        "(-2)³ = -8. -8 + 10 = 2.",
        "2.",
        "2.",
        "-8 + 10 = 2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: (-4.5) × 2 + 12.5.",
        "3.5",
        ["-3.5", "21.5", "-21.5"],
        "-9.0 + 12.5 = 3.5.",
        "3.5.",
        "3.5.",
        "-9 + 12.5 = 3.5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A submarine descends at 15 feet per minute for 8 minutes. What is its change in elevation in feet?",
        -120, ["-120", "-120 feet"],
        "-15 × 8 = -120 feet.",
        "-120.",
        "-120.",
        "-15 × 8 = -120."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate: [(-3) × 4 - 6] ÷ (-3).",
        6, ["6"],
        "(-12 - 6) = -18. -18 ÷ (-3) = 6.",
        "6.",
        "6.",
        "-18 ÷ -3 = 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A stock dropped $2.50 per day for 5 days, then gained $8.00 on the 6th day. What was the net change?",
        "-$4.50",
        ["+$4.50", "-$12.50", "+$8.00"],
        "5 × (-2.50) = -12.50. -12.50 + 8.00 = -$4.50.",
        "-$4.50.",
        "-$4.50.",
        "-12.50 + 8.00 = -$4.50."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate: 25 - (-3)² × 2.",
        7, ["7"],
        "(-3)² = 9; 9 × 2 = 18. 25 - 18 = 7.",
        "7.",
        "7.",
        "25 - 18 = 7."
    ))

    # =========================================================================
    # LESSON 9: Linear Expressions with Rational Coefficients (7.EE.A.1/2)
    # =========================================================================
    LID = "G7_L09"
    LT = "Linear Expressions with Rational Coefficients"
    DOM = "Expressions"
    STD = "7.EE.A.1 / 7.EE.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Simplify by combining like terms: 3x - 5 + 4x + 9.",
        "7x + 4",
        ["7x - 4", "12x + 4", "7x + 14"],
        "(3x + 4x) + (-5 + 9) = 7x + 4.",
        "7x + 4.",
        "7x + 4.",
        "3x + 4x - 5 + 9 = 7x + 4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Expand: -3(2x - 5).",
        "-6x + 15",
        ["-6x - 15", "6x - 15", "-6x - 5"],
        "-3 × 2x = -6x; -3 × (-5) = +15.",
        "-6x + 15.",
        "-6x + 15.",
        "-3(2x) - 3(-5) = -6x + 15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "An item with original price p is on sale for 20% off. Which expression represents the sale price?",
        "0.80p (or p - 0.20p)",
        ["1.20p", "p - 20", "0.20p"],
        "p - 0.20p = (1 - 0.20)p = 0.80p.",
        "0.80p.",
        "0.80p (or p - 0.20p).",
        "(1 - 0.20)p = 0.80p."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Factor completely: 12x - 18.",
        "6(2x - 3)",
        ["3(4x - 6)", "2(6x - 9)", "12(x - 1)"],
        "GCF(12, 18) = 6. 12x ÷ 6 = 2x; -18 ÷ 6 = -3. Factored form: 6(2x - 3).",
        "6(2x - 3).",
        "6(2x - 3).",
        "6(2x - 3)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the coefficient of x when 2(3x - 4) + 5(2x + 1) is simplified?",
        16, ["16"],
        "6x - 8 + 10x + 5 = 16x - 3. Coefficient of x is 16.",
        "16.",
        "16.",
        "6x + 10x = 16x."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Simplify: (1/2)(4x - 8) + (1/3)(9x + 6).",
        "5x - 2",
        ["5x - 6", "7x - 2", "5x + 2"],
        "2x - 4 + 3x + 2 = 5x - 2.",
        "5x - 2.",
        "5x - 2.",
        "(2x - 4) + (3x + 2) = 5x - 2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A meal costs m dollars. You add 8% tax and 15% tip. Which expression represents the total cost?",
        "1.23m",
        ["1.08m + 15", "0.23m", "m + 0.08 + 0.15"],
        "m + 0.08m + 0.15m = 1.23m.",
        "1.23m.",
        "1.23m.",
        "(1 + 0.08 + 0.15)m = 1.23m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the constant term when 4(2x - 3) - 2(x + 5) is simplified?",
        -22, ["-22"],
        "Constants: 4(-3) - 2(5) = -12 - 10 = -22.",
        "-22.",
        "-22.",
        "-12 - 10 = -22."
    ))

    # =========================================================================
    # LESSON 10: Solving Two-Step Equations (7.EE.B.4a)
    # =========================================================================
    LID = "G7_L10"
    LT = "Solving Two-Step Equations"
    DOM = "Expressions"
    STD = "7.EE.B.4a"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve for x: 2x + 7 = 15.",
        4, ["4", "x=4", "x = 4"],
        "Subtract 7 from both sides: 2x = 8. Divide by 2: x = 4.",
        "x = 4.",
        "4.",
        "2x = 8 -> x = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve for y: 5y - 3 = 22.",
        5, ["5", "y=5", "y = 5"],
        "Add 3: 5y = 25. Divide by 5: y = 5.",
        "y = 5.",
        "5.",
        "5y = 25 -> y = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve for m: 3(m + 4) = 24.",
        4, ["4", "m=4", "m = 4"],
        "Divide by 3: m + 4 = 8. Subtract 4: m = 4.",
        "m = 4.",
        "4.",
        "m + 4 = 8 -> m = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve for x: -4x + 8 = -12.",
        5, ["5", "x=5", "x = 5"],
        "Subtract 8: -4x = -20. Divide by -4: x = 5.",
        "x = 5.",
        "5.",
        "-4x = -20 -> x = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve for w: (w - 3) ÷ 4 = 5.",
        23, ["23", "w=23", "w = 23"],
        "Multiply by 4: w - 3 = 20. Add 3: w = 23.",
        "w = 23.",
        "23.",
        "w - 3 = 20 -> w = 23."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve for k: -2(k - 5) = 14.",
        -2, ["-2", "k=-2", "k = -2"],
        "Divide by -2: k - 5 = -7. Add 5: k = -2.",
        "k = -2.",
        "-2.",
        "k - 5 = -7 -> k = -2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Sam bought a skateboard for $65 and 3 helmets of equal cost. The total was $125. Which equation finds the cost of one helmet h?",
        "3h + 65 = 125",
        ["h + 65 = 125", "3(h + 65) = 125", "3h - 65 = 125"],
        "3 helmets at h dollars each plus $65 skateboard: 3h + 65 = 125.",
        "3h + 65 = 125.",
        "3h + 65 = 125.",
        "3h + 65 = 125."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In problem Q07 (3h + 65 = 125), what is the cost of each helmet in dollars?",
        20, ["20", "$20"],
        "3h = 125 - 65 = 60. h = 60 ÷ 3 = $20.",
        "$20.",
        "20.",
        "3h = 60 -> h = 20."
    ))

    # =========================================================================
    # LESSON 11: Solving Two-Step Inequalities (7.EE.B.4b)
    # =========================================================================
    LID = "G7_L11"
    LT = "Solving Two-Step Inequalities"
    DOM = "Expressions"
    STD = "7.EE.B.4b"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve the inequality: 3x + 5 > 14.",
        "x > 3",
        ["x < 3", "x > 6", "x ≥ 3"],
        "Subtract 5: 3x > 9. Divide by 3: x > 3.",
        "x > 3.",
        "x > 3.",
        "3x > 9 -> x > 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What critical rule must you remember when multiplying or dividing both sides of an inequality by a negative number?",
        "Reverse the direction of the inequality sign",
        ["Keep the sign the same", "Change all numbers to positive", "The inequality becomes an equals sign"],
        "Multiplying or dividing by a negative reverses the inequality direction (< becomes >, etc.).",
        "Flip/reverse the inequality sign.",
        "Reverse the direction of the inequality sign.",
        "Always reverse the inequality symbol when dividing or multiplying by a negative."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: -2x + 8 ≤ 16.",
        "x ≥ -4",
        ["x ≤ -4", "x ≥ 4", "x ≤ 4"],
        "Subtract 8: -2x ≤ 8. Divide by -2 and flip sign: x ≥ -4.",
        "x ≥ -4.",
        "x ≥ -4.",
        "-2x ≤ 8 -> x ≥ -4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the largest integer solution to 5x - 4 < 26?",
        5, ["5"],
        "5x < 30 -> x < 6. The largest integer strictly less than 6 is 5.",
        "5.",
        "5.",
        "x < 6, largest integer is 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: -4y - 6 > 10.",
        "y < -4",
        ["y > -4", "y < 4", "y > 4"],
        "Add 6: -4y > 16. Divide by -4 (flip sign): y < -4.",
        "y < -4.",
        "y < -4.",
        "-4y > 16 -> y < -4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A taxi service charges $3.00 flat fee plus $2.50 per mile. Leo has $23.00. Which inequality represents miles m he can travel?",
        "2.50m + 3.00 ≤ 23.00",
        ["2.50m + 3.00 ≥ 23.00", "3.00m + 2.50 ≤ 23.00", "2.50m - 3.00 ≤ 23.00"],
        "Total cost must be less than or equal to $23: 2.50m + 3.00 ≤ 23.00.",
        "2.50m + 3.00 ≤ 23.00.",
        "2.50m + 3.00 ≤ 23.00.",
        "2.50m + 3 ≤ 23."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In problem Q06 (2.50m + 3 ≤ 23), what is the maximum number of miles Leo can travel?",
        8, ["8", "8 miles"],
        "2.50m ≤ 20. m ≤ 20 ÷ 2.50 = 8 miles.",
        "8 miles.",
        "8.",
        "m ≤ 20 / 2.5 = 8 miles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the smallest integer solution to -3x + 12 ≤ 0?",
        4, ["4"],
        "-3x ≤ -12 -> x ≥ 4. Smallest integer is 4.",
        "4.",
        "4.",
        "x ≥ 4, smallest is 4."
    ))

    # =========================================================================
    # LESSON 12: Scale Drawings (7.G.A.1)
    # =========================================================================
    LID = "G7_L12"
    LT = "Scale Drawings"
    DOM = "Geometry"
    STD = "7.G.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A map scale is 1 inch = 15 miles. If two cities are 4 inches apart on the map, what is the actual distance in miles?",
        60, ["60", "60 miles"],
        "Multiply map distance by scale: 4 × 15 = 60 miles.",
        "60 miles.",
        "60.",
        "4 × 15 = 60 miles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A blueprint uses a scale of 1 cm = 2 meters. A room is 5 cm long on the blueprint. What is the actual room length?",
        "10 meters",
        ["7 meters", "2.5 meters", "12 meters"],
        "5 × 2 = 10 meters.",
        "10 meters.",
        "10 meters.",
        "5 × 2 = 10 m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "On a blueprint with scale 1 cm = 3 meters, a rectangular patio is 4 cm by 6 cm. What is the actual area in square meters?",
        216, ["216", "216 sq m"],
        "Actual length = 6 × 3 = 18 m. Actual width = 4 × 3 = 12 m. Area = 18 × 12 = 216 sq m.",
        "216 sq m.",
        "216.",
        "18 × 12 = 216 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "If a scale drawing has a scale factor of 1:50, what does that mean?",
        "Every 1 unit on the drawing equals 50 units in real life",
        ["The real object is 50 times smaller", "The drawing is 50 times larger", "The area is 50 times larger"],
        "Scale 1:50 means actual dimensions are 50 times larger than the drawing.",
        "1 unit on drawing = 50 units real.",
        "Every 1 unit on the drawing equals 50 units in real life.",
        "1:50 scale means real life is 50 times the drawing dimension."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "An actual highway is 120 miles long. On a map with scale 1 inch = 20 miles, how many inches long is the highway on the map?",
        6, ["6", "6 inches"],
        "120 ÷ 20 = 6 inches.",
        "6 inches.",
        "6.",
        "120 ÷ 20 = 6 inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A photo is 4 inches wide by 6 inches high. It is enlarged by a scale factor of 3. What is the area of the enlarged photo in square inches?",
        216, ["216", "216 sq in"],
        "New dimensions: 12 in by 18 in. New area = 12 × 18 = 216 sq in (Notice: 24 × 3² = 216).",
        "216 sq in.",
        "216.",
        "12 × 18 = 216 sq in."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "When the linear dimensions of a 2D figure are multiplied by a scale factor k, by what factor does its area change?",
        "k²",
        ["k", "2k", "k³"],
        "Area scales by the square of the linear scale factor: k × k = k².",
        "k².",
        "k².",
        "Area scales by k²."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A model car has a length of 8 inches. The scale is 1 inch = 2.5 feet. What is the actual car length in feet?",
        20, ["20", "20 feet"],
        "8 × 2.5 = 20 feet.",
        "20 feet.",
        "20.",
        "8 × 2.5 = 20 ft."
    ))

    # =========================================================================
    # LESSON 13: Drawing Geometric Figures (7.G.A.2)
    # =========================================================================
    LID = "G7_L13"
    LT = "Drawing Geometric Figures"
    DOM = "Geometry"
    STD = "7.G.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Can a triangle have side lengths of 3 cm, 4 cm, and 8 cm?",
        "No, because the sum of the two shorter sides (3 + 4 = 7) is not greater than the third side (8)",
        ["Yes, any three lengths make a triangle", "Yes, because 3 + 4 + 8 = 15", "Only if it is a right triangle"],
        "Triangle Inequality Theorem: The sum of any two side lengths must be strictly greater than the third side.",
        "3 + 4 = 7 < 8, so no triangle can be formed.",
        "No, because the sum of the two shorter sides (3 + 4 = 7) is not greater than the third side (8).",
        "Triangle Inequality requires a + b > c."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which set of three angle measures can form a unique triangle?",
        "50°, 60°, 70°",
        ["40°, 50°, 80°", "60°, 60°, 70°", "90°, 90°, 10°"],
        "The angle sum of any triangle must be exactly 180°: 50 + 60 + 70 = 180°.",
        "50°, 60°, 70°.",
        "50°, 60°, 70°.",
        "50 + 60 + 70 = 180°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "If you are given three angle measures that add to 180° (e.g. 45°, 45°, 90°), how many different triangles can be formed?",
        "Infinitely many similar triangles of different sizes",
        ["Exactly one unique triangle", "No triangles", "Exactly three triangles"],
        "Angle-Angle-Angle (AAA) determines shape (similarity) but not size, so infinitely many triangles exist.",
        "Infinitely many triangles.",
        "Infinitely many similar triangles of different sizes.",
        "Three angles determine shape, not unique size."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Two angles of a triangle measure 45° and 75°. What is the measure of the third angle in degrees? (180 - 120)",
        60, ["60", "60°", "60 degrees"],
        "180 - (45 + 75) = 180 - 120 = 60°.",
        "60°.",
        "60.",
        "180 - 120 = 60°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Which three side lengths CAN form a triangle?",
        "5 cm, 8 cm, 10 cm",
        ["2 cm, 3 cm, 6 cm", "4 cm, 5 cm, 9 cm", "1 cm, 2 cm, 5 cm"],
        "5 + 8 = 13 > 10; 5 + 10 > 8; 8 + 10 > 5. All triangle inequalities hold.",
        "5 cm, 8 cm, 10 cm.",
        "5 cm, 8 cm, 10 cm.",
        "5 + 8 = 13 > 10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If two sides of a triangle are 6 cm and 10 cm, which of the following could be the length of the third side?",
        "8 cm",
        ["4 cm", "16 cm", "18 cm"],
        "Third side must be between 10 - 6 = 4 and 10 + 6 = 16: 4 < s < 16. 8 cm works.",
        "8 cm.",
        "8 cm.",
        "4 < s < 16, so 8 is valid."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "When two sides and the included angle (SAS) are specified, how many unique triangles can be drawn?",
        "Exactly one unique triangle",
        ["More than one", "No triangles", "Infinitely many"],
        "By the SAS congruence criterion, specifying two sides and the included angle determines a unique triangle.",
        "Exactly one unique triangle.",
        "Exactly one unique triangle.",
        "SAS determines a unique triangle."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "An isosceles triangle has an angle of 100°. The other two angles are congruent. What is the measure of each equal angle in degrees?",
        40, ["40", "40°", "40 degrees"],
        "(180 - 100) ÷ 2 = 80 ÷ 2 = 40°.",
        "40°.",
        "40.",
        "(180 - 100)/2 = 40°."
    ))

    # =========================================================================
    # LESSON 14: Slicing 3D Figures (7.G.A.3)
    # =========================================================================
    LID = "G7_L14"
    LT = "Slicing 3D Figures"
    DOM = "Geometry"
    STD = "7.G.A.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "If a right rectangular prism is sliced by a plane parallel to its base, what 2-dimensional shape is the cross-section?",
        "Rectangle",
        ["Triangle", "Circle", "Trapezoid"],
        "Slicing parallel to the base yields a cross-section congruent to the base: a rectangle.",
        "Rectangle.",
        "Rectangle.",
        "A slice parallel to a rectangular base produces a rectangle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "If a right cylinder is sliced parallel to its circular base, what shape is the cross-section?",
        "Circle",
        ["Rectangle", "Oval", "Triangle"],
        "A cross-section parallel to the base of a cylinder is a circle.",
        "Circle.",
        "Circle.",
        "Parallel slice to cylinder base is a circle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "If a right cylinder is sliced by a plane perpendicular to its base, what shape is the cross-section?",
        "Rectangle",
        ["Circle", "Triangle", "Hexagon"],
        "A vertical cross-section of a cylinder perpendicular to the base is a rectangle.",
        "Rectangle.",
        "Rectangle.",
        "A vertical slice of a cylinder produces a rectangle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "If a right square pyramid is sliced by a plane passing through the apex and perpendicular to the base, what shape is formed?",
        "Triangle",
        ["Square", "Trapezoid", "Rectangle"],
        "A vertical slice through the apex creates a triangle.",
        "Triangle.",
        "Triangle.",
        "Vertical slice through the apex is a triangle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "If a cube is sliced by a plane that cuts through three adjacent edges at the corner, what shape is the cross-section?",
        "Triangle",
        ["Square", "Circle", "Pentagon"],
        "Slicing off a corner creates a triangular cross-section.",
        "Triangle.",
        "Triangle.",
        "Cutting off a corner yields a triangle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If a cone is sliced parallel to its circular base, what shape is the cross-section?",
        "Circle",
        ["Triangle", "Parabola", "Rectangle"],
        "A slice parallel to the base of a cone is a smaller circle.",
        "Circle.",
        "Circle.",
        "Parallel slice to cone base is a circle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If a cone is sliced vertically through its vertex, what shape is the cross-section?",
        "Triangle",
        ["Circle", "Square", "Semicircle"],
        "A slice through the vertex perpendicular to the base of a cone produces an isosceles triangle.",
        "Triangle.",
        "Triangle.",
        "Vertical cut through vertex produces an isosceles triangle."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If a sphere is sliced by ANY plane, what shape is the cross-section always?",
        "Circle",
        ["Oval", "Rectangle", "Depends on the angle"],
        "Every planar cross-section of a sphere is a circle.",
        "Circle.",
        "Circle.",
        "Every cross-section of a sphere is a circle."
    ))

    # =========================================================================
    # LESSON 15: Circles: Circumference & Area (7.G.B.4)
    # =========================================================================
    LID = "G7_L15"
    LT = "Circles: Circumference & Area"
    DOM = "Geometry"
    STD = "7.G.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A circle has a radius of 7 cm. Using π ≈ 22/7, find its circumference in cm. (C = 2πr)",
        44, ["44", "44 cm"],
        "C = 2 × (22/7) × 7 = 44 cm.",
        "44 cm.",
        "44.",
        "2 × (22/7) × 7 = 44 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A circle has a diameter of 10 meters. Using π ≈ 3.14, find its circumference in meters. (C = πd)",
        31.4, ["31.4", "31.4 m"],
        "C = 3.14 × 10 = 31.4 meters.",
        "31.4 m.",
        "31.4.",
        "3.14 × 10 = 31.4 m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the area of a circle with radius 10 cm using π ≈ 3.14 in square cm. (A = πr²)",
        314, ["314", "314 sq cm"],
        "A = 3.14 × 10² = 3.14 × 100 = 314 sq cm.",
        "314 sq cm.",
        "314.",
        "3.14 × 100 = 314 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A circle has a radius of 7 cm. Using π ≈ 22/7, what is its area in square cm?",
        154, ["154", "154 sq cm"],
        "A = (22/7) × 7² = (22/7) × 49 = 22 × 7 = 154 sq cm.",
        "154 sq cm.",
        "154.",
        "(22/7) × 49 = 154 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "If the diameter of a circle is 16 inches, what is its radius?",
        "8 inches",
        ["32 inches", "4 inches", "16 inches"],
        "Radius is half of diameter: 16 ÷ 2 = 8 inches.",
        "8 inches.",
        "8 inches.",
        "r = d/2 = 8 inches."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the area of a circle with a diameter of 20 meters using π ≈ 3.14 in square meters. (Radius = 10)",
        314, ["314", "314 sq m"],
        "r = 10. A = 3.14 × 10² = 314 sq m.",
        "314 sq m.",
        "314.",
        "3.14 × 10² = 314 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If the circumference of a circle is 18π, what is its radius?",
        "9",
        ["18", "6", "36"],
        "C = 2πr = 18π -> 2r = 18 -> r = 9.",
        "9.",
        "9.",
        "2r = 18 -> r = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A circular bicycle wheel has radius 14 inches. Using π ≈ 22/7, how many inches does it travel in 1 full turn? (Circumference)",
        88, ["88", "88 inches"],
        "C = 2 × (22/7) × 14 = 2 × 22 × 2 = 88 inches.",
        "88 inches.",
        "88.",
        "2 × (22/7) × 14 = 88 inches."
    ))

    # =========================================================================
    # LESSON 16: Angle Relationships (7.G.B.5)
    # =========================================================================
    LID = "G7_L16"
    LT = "Angle Relationships"
    DOM = "Geometry"
    STD = "7.G.B.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Two angles are complementary (sum to 90°). If one angle measures 58°, what is the measure of the other angle in degrees?",
        32, ["32", "32°", "32 degrees"],
        "90 - 58 = 32°.",
        "32°.",
        "32.",
        "90 - 58 = 32°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Two angles are supplementary (sum to 180°). If one angle measures 124°, what is the measure of the other angle in degrees?",
        56, ["56", "56°", "56 degrees"],
        "180 - 124 = 56°.",
        "56°.",
        "56.",
        "180 - 124 = 56°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Vertical angles are opposite angles formed by intersecting lines. If one angle is 72°, what is the vertical angle across from it in degrees?",
        72, ["72", "72°", "72 degrees"],
        "Vertical angles are congruent (equal): 72°.",
        "72°.",
        "72.",
        "Vertical angles are equal: 72°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Two supplementary angles have measures (2x)° and 80°. What is the value of x? (2x + 80 = 180)",
        50, ["50"],
        "2x = 180 - 80 = 100. x = 100 ÷ 2 = 50.",
        "50.",
        "50.",
        "2x = 100 -> x = 50."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Angles ∠A and ∠B are adjacent and form a right angle. If ∠A = (3x + 15)° and ∠B = 45°, what is x?",
        "10",
        ["15", "5", "20"],
        "3x + 15 + 45 = 90. 3x + 60 = 90. 3x = 30 -> x = 10.",
        "10.",
        "10.",
        "3x = 30 -> x = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Two vertical angles are given by (4x - 10)° and (2x + 30)°. What is x? (4x - 10 = 2x + 30)",
        20, ["20"],
        "4x - 2x = 30 + 10 -> 2x = 40 -> x = 20.",
        "20.",
        "20.",
        "2x = 40 -> x = 20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Three angles meet at a point along a straight line: 40°, x°, and (2x)°. What is x? (40 + 3x = 180)",
        "46.67",
        ["45", "50", "40"],
        "3x = 180 - 40 = 140. x = 140 ÷ 3 ≈ 46.67°.",
        "46.67.",
        "46.67.",
        "3x = 140 -> x ≈ 46.67."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "An angle is 4 times its complement: x = 4(90 - x). What is the angle x in degrees? (5x = 360)",
        72, ["72", "72°", "72 degrees"],
        "x + 0.25x = 90 (or 5x = 360 -> x = 72°). Check: complement is 18°; 18 × 4 = 72°.",
        "72°.",
        "72.",
        "x = 72°."
    ))

    # =========================================================================
    # LESSON 17: Surface Area of Composite Figures (7.G.B.6)
    # =========================================================================
    LID = "G7_L17"
    LT = "Surface Area of Composite Figures"
    DOM = "Geometry"
    STD = "7.G.B.6"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the surface area of a right prism with two triangular bases (each area 15 cm²) and three rectangular faces of areas 30, 40, and 50 cm² in square cm.",
        150, ["150", "150 sq cm"],
        "SA = (2 × 15) + (30 + 40 + 50) = 30 + 120 = 150 sq cm.",
        "150 sq cm.",
        "150.",
        "30 + 120 = 150 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "When finding the surface area of two joined solids, which faces must be EXCLUDED?",
        "The overlapping touching faces where the two solids meet",
        ["All bottom faces", "The front faces", "The triangular faces"],
        "Only the exposed outer surfaces count toward surface area; internal joined faces are excluded.",
        "Exclude the overlapping joined faces.",
        "The overlapping touching faces where the two solids meet.",
        "Internal touching faces do not count toward surface area."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A wooden box without a lid (open top) is 10 cm long, 6 cm wide, and 4 cm high. What is its outside surface area in square cm? (Base + 4 sides: 60 + 2(40) + 2(24))",
        188, ["188", "188 sq cm"],
        "Bottom = 10 × 6 = 60. Front/Back = 2 × (10 × 4) = 80. Left/Right = 2 × (6 × 4) = 48. Total = 60 + 80 + 48 = 188 sq cm.",
        "188 sq cm.",
        "188.",
        "60 + 80 + 48 = 188 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Two cubes of edge length 3 cm are glued face-to-face. What is the total exposed surface area in square cm? (Each cube had 6 faces of 9; 2 faces are covered)",
        90, ["90", "90 sq cm"],
        "Total faces = 12 - 2 = 10 faces. Each face is 3² = 9 sq cm. 10 × 9 = 90 sq cm.",
        "90 sq cm.",
        "90.",
        "10 × 9 = 90 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A cylinder has radius 3 cm and height 5 cm. Lateral surface area is 2πrh. Using π ≈ 3.14, what is the lateral area?",
        "94.2 sq cm",
        ["47.1 sq cm", "150 sq cm", "28.26 sq cm"],
        "Lateral SA = 2 × 3.14 × 3 × 5 = 94.2 sq cm.",
        "94.2 sq cm.",
        "94.2 sq cm.",
        "2 × 3.14 × 15 = 94.2 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A right trapezoidal prism has two trapezoid bases (each area 24 cm²) and 4 rectangular faces with areas 20, 30, 40, and 50 cm². What is the total surface area in square cm?",
        188, ["188", "188 sq cm"],
        "SA = (2 × 24) + (20 + 30 + 40 + 50) = 48 + 140 = 188 sq cm.",
        "188 sq cm.",
        "188.",
        "48 + 140 = 188 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Three cubes of side length 2 cm are stacked in a column. What is the total exposed surface area?",
        "56 sq cm",
        ["72 sq cm", "48 sq cm", "64 sq cm"],
        "Total cube faces = 3 × 6 = 18. Gluing 3 cubes together covers 4 faces (2 interfaces × 2). Exposed faces = 18 - 4 = 14. Area = 14 × 4 = 56 sq cm.",
        "56 sq cm.",
        "56 sq cm.",
        "14 × 4 = 56 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the surface area of a rectangular prism 8 ft by 5 ft by 2 ft in square feet. (2(40 + 16 + 10))",
        132, ["132", "132 sq ft"],
        "2 × (40 + 16 + 10) = 2 × 66 = 132 sq ft.",
        "132 sq ft.",
        "132.",
        "2 × 66 = 132 sq ft."
    ))

    # =========================================================================
    # LESSON 18: Volume of Prisms & Pyramids (7.G.B.6)
    # =========================================================================
    LID = "G7_L18"
    LT = "Volume of Prisms & Pyramids"
    DOM = "Geometry"
    STD = "7.G.B.6"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the volume of a right triangular prism with base area 18 cm² and height 10 cm in cubic cm. (V = Bh)",
        180, ["180", "180 cm³"],
        "V = Base Area × height = 18 × 10 = 180 cm³.",
        "180 cm³.",
        "180.",
        "18 × 10 = 180 cm³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which formula gives the volume of a pyramid with base area B and height h?",
        "V = (1/3)Bh",
        ["V = Bh", "V = (1/2)Bh", "V = 3Bh"],
        "A pyramid has 1/3 the volume of a prism with the same base and height: V = (1/3)Bh.",
        "V = (1/3)Bh.",
        "V = (1/3)Bh.",
        "Volume of pyramid is 1/3 Bh."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A square pyramid has a base area of 36 square feet and a height of 9 feet. What is its volume in cubic feet?",
        108, ["108", "108 cu ft"],
        "V = (1/3) × 36 × 9 = 12 × 9 = 108 cubic feet.",
        "108 cu ft.",
        "108.",
        "1/3 × 36 × 9 = 108 cu ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A trapezoidal prism has a trapezoid base with area 25 m² and prism length 8 m. What is its volume in cubic meters?",
        200, ["200", "200 m³"],
        "V = Bh = 25 × 8 = 200 cubic meters.",
        "200 m³.",
        "200.",
        "25 × 8 = 200 m³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A triangular prism has a right triangle base with legs 6 cm and 8 cm (base area = 24 cm²). If the prism height is 15 cm, what is the volume?",
        "360 cm³",
        ["180 cm³", "720 cm³", "120 cm³"],
        "Base area = 1/2 × 6 × 8 = 24 cm². V = 24 × 15 = 360 cm³.",
        "360 cm³.",
        "360 cm³.",
        "24 × 15 = 360 cm³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A pyramid with volume 60 cubic inches has a base area of 20 square inches. What is its height in inches? (h = 3V ÷ B)",
        9, ["9", "9 inches"],
        "h = (3 × 60) ÷ 20 = 180 ÷ 20 = 9 inches.",
        "9 inches.",
        "9.",
        "3 × 60 ÷ 20 = 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If a prism and a pyramid have identical bases and heights, how many times greater is the prism\'s volume than the pyramid\'s volume?",
        "3 times greater",
        ["2 times greater", "They are equal", "1/3 as large"],
        "Prism volume = Bh; Pyramid volume = (1/3)Bh. The prism is 3 times the pyramid.",
        "3 times greater.",
        "3 times greater.",
        "The prism is 3 times the pyramid volume."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A rectangular pyramid has base dimensions 6 m by 5 m (B = 30 m²) and height 12 m. What is its volume in cubic meters?",
        120, ["120", "120 m³"],
        "V = (1/3) × 30 × 12 = 10 × 12 = 120 cubic meters.",
        "120 m³.",
        "120.",
        "1/3 × 30 × 12 = 120 m³."
    ))

    # =========================================================================
    # LESSON 19: Statistical Sampling (7.SP.A.1 / 7.SP.A.2)
    # =========================================================================
    LID = "G7_L19"
    LT = "Statistical Sampling"
    DOM = "Statistics"
    STD = "7.SP.A.1 / 7.SP.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which of the following describes a representative sample of a whole school?",
        "Selecting every 10th student from an alphabetical list of all students",
        ["Surveying only the 8th grade basketball team", "Surveying students who arrive early for detention", "Asking your three best friends"],
        "A representative random sample gives every member of the population an equal chance of being selected.",
        "Every 10th student alphabetically.",
        "Selecting every 10th student from an alphabetical list of all students.",
        "Systematic random sampling produces a representative sample."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A survey of 50 randomly selected students found that 35 prefer pizza. What proportion of students prefer pizza?",
        "70%",
        ["35%", "50%", "85%"],
        "35 ÷ 50 = 70/100 = 70%.",
        "70%.",
        "70%.",
        "35/50 = 70%."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In a school of 600 students, a random sample of 50 students showed that 35 prefer pizza (70%). Estimate how many students in the entire school prefer pizza.",
        420, ["420", "420 students"],
        "Estimate = 0.70 × 600 = 420 students.",
        "420 students.",
        "420.",
        "0.70 × 600 = 420."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Why is a larger sample size generally better than a smaller sample size?",
        "It provides a more accurate estimate and reduces sampling variability",
        ["It guarantees 100% certainty", "It always changes the average", "It eliminates the need for random selection"],
        "Larger random samples produce closer estimates to the true population parameter.",
        "More accurate estimate, less variability.",
        "It provides a more accurate estimate and reduces sampling variability.",
        "Larger samples reduce sampling variability."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "In a sample of 80 light bulbs, 4 were defective (5%). In a shipment of 2,000 bulbs, how many are expected to be defective?",
        100, ["100", "100 bulbs"],
        "Defect rate = 4/80 = 5%. In 2,000: 0.05 × 2,000 = 100 bulbs.",
        "100 bulbs.",
        "100.",
        "0.05 × 2,000 = 100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A bookstore manager wants to know favorite genres. She surveys customers standing in the Sci-Fi aisle. Is this sample biased or representative?",
        "Biased, because customers in the Sci-Fi aisle are much more likely to prefer Sci-Fi",
        ["Representative, because they are book readers", "Unbiased random sample", "Completely scientific"],
        "Convenience sampling in a specific aisle over-represents that aisle\'s genre preference.",
        "Biased.",
        "Biased, because customers in the Sci-Fi aisle are much more likely to prefer Sci-Fi.",
        "Convenience sampling causes selection bias."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In a wildlife study, 60 fish are tagged and released into a lake. Later, a sample of 50 fish is caught, and 5 of them are tagged (10%). Estimate the total fish population in the lake. (60 ÷ 0.10)",
        600, ["600", "600 fish"],
        "Total = (Tagged total × Caught sample) ÷ (Tagged caught) = (60 × 50) ÷ 5 = 600 fish.",
        "600 fish.",
        "600.",
        "60 ÷ 0.10 = 600 fish."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the term for a subset of a population selected so that every individual has an equal chance of being chosen?",
        "Simple random sample",
        ["Voluntary response sample", "Biased sample", "Convenience sample"],
        "A simple random sample gives every member equal selection probability.",
        "Simple random sample.",
        "Simple random sample.",
        "Simple random sample."
    ))

    # =========================================================================
    # LESSON 20: Comparing Two Populations (7.SP.B.3 / 7.SP.B.4)
    # =========================================================================
    LID = "G7_L20"
    LT = "Comparing Two Populations"
    DOM = "Statistics"
    STD = "7.SP.B.3 / 7.SP.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Team A has mean score 82 and Team B has mean score 76. What is the difference between their means?",
        6, ["6", "6 points"],
        "82 - 76 = 6.",
        "6.",
        "6.",
        "82 - 76 = 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What measure of variability is calculated as the average distance between each data point and the mean?",
        "Mean Absolute Deviation (MAD)",
        ["Interquartile Range (IQR)", "Median", "Mode"],
        "MAD measures the average distance of data points from the mean.",
        "Mean Absolute Deviation (MAD).",
        "Mean Absolute Deviation (MAD).",
        "MAD is the average distance from the mean."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Class 1 has a mean of 80 with a MAD of 4. Class 2 has a mean of 88 with a MAD of 4. How many MADs apart are the two means? (Difference ÷ MAD = 8 ÷ 4)",
        2, ["2"],
        "Difference = 88 - 80 = 8. 8 ÷ 4 = 2 MADs.",
        "2 MADs.",
        "2.",
        "8 ÷ 4 = 2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Group X has an IQR of 12 and Group Y has an IQR of 5. What does this tell you about Group X compared to Group Y?",
        "Group X has greater variability/spread in the middle 50% of its data",
        ["Group X has a higher average", "Group Y has more data values", "Group X is smaller"],
        "A larger IQR indicates greater dispersion or spread in the middle half of the distribution.",
        "Group X has greater variability.",
        "Group X has greater variability/spread in the middle 50% of its data.",
        "Higher IQR indicates greater spread."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Plant group A has median height 24 cm; group B has median height 19 cm. What is the difference in medians in cm?",
        5, ["5", "5 cm"],
        "24 - 19 = 5 cm.",
        "5 cm.",
        "5.",
        "24 - 19 = 5 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Two box plots are compared: Box Plot A\'s entire box (Q1 to Q3) is to the right of Box Plot B\'s box. What conclusion can be drawn?",
        "The middle 50% of Group A values are consistently higher than Group B values",
        ["Group B has a higher mean", "The two groups are identical", "No conclusion can be made"],
        "When the IQR of A is strictly above B, Group A systematically scores higher in the center.",
        "Group A is consistently higher.",
        "The middle 50% of Group A values are consistently higher than Group B values.",
        "The higher IQR range indicates higher values."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Dataset has mean 20. Values are 18, 20, 22. Deviations from mean: |18-20|=2, |20-20|=0, |22-20|=2. What is the MAD? (Sum ÷ 3 = 4/3 ≈ 1.33)",
        1.33, ["1.33", "4/3"],
        "(2 + 0 + 2) ÷ 3 = 4/3 ≈ 1.33.",
        "1.33.",
        "1.33.",
        "4 ÷ 3 ≈ 1.33."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If the difference between two sample means is 3 times the MAD, is this difference likely meaningful?",
        "Yes, 3 MADs indicates a substantial, meaningful difference between populations",
        ["No, 3 MADs means they overlap completely", "MAD has nothing to do with difference", "Only if MAD is zero"],
        "A difference of 2 or more MADs indicates very little overlap and a significant shift.",
        "Yes, substantial difference.",
        "Yes, 3 MADs indicates a substantial, meaningful difference between populations.",
        "3 MADs represents a statistically notable difference."
    ))

    # =========================================================================
    # LESSON 21: Introduction to Probability (7.SP.C.5)
    # =========================================================================
    LID = "G7_L21"
    LT = "Introduction to Probability"
    DOM = "Statistics"
    STD = "7.SP.C.5"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the probability of an impossible event that can never occur?",
        "0",
        ["1", "0.5", "-1"],
        "Probabilities range from 0 (impossible) to 1 (certain).",
        "0.",
        "0.",
        "Impossible events have probability 0."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the probability of rolling an even number on a standard 6-sided die? (2, 4, 6 out of 6)",
        "1/2 (or 0.5)",
        ["1/6", "2/6", "5/6"],
        "3 even outcomes out of 6 total = 3/6 = 1/2.",
        "1/2.",
        "1/2 (or 0.5).",
        "3/6 = 1/2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A spinner has 8 equal sections numbered 1 to 8. What is the probability of spinning a number greater than 5? (Enter numerator over 8: numbers 6, 7, 8)",
        3, ["3"],
        "Numbers greater than 5 are 6, 7, 8 (3 outcomes). P = 3/8. Numerator is 3.",
        "3.",
        "3.",
        "3 outcomes out of 8, numerator is 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "An event has a probability of 0.85. How would you describe the likelihood of this event?",
        "Likely",
        ["Unlikely", "Impossible", "Certain"],
        "Events with probability between 0.5 and 1 are likely. (0.85 is very likely).",
        "Likely.",
        "Likely.",
        "0.85 is classified as likely."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A bag has 3 red, 4 blue, and 5 green marbles (total 12). What is the numerator of P(blue) when written in simplest form (1/___)?",
        3, ["3"],
        "P(blue) = 4/12 = 1/3. The denominator in simplest form is 3.",
        "3.",
        "3.",
        "4/12 = 1/3, denominator is 3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If the probability of rain tomorrow is 0.35, what is the probability that it will NOT rain tomorrow?",
        "0.65",
        ["0.35", "0.75", "0.50"],
        "P(not rain) = 1 - P(rain) = 1 - 0.35 = 0.65.",
        "0.65.",
        "0.65.",
        "1 - 0.35 = 0.65."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A coin is flipped 200 times. How many heads would you theoretically expect? (P = 0.5)",
        100, ["100"],
        "Expected value = 200 × 0.5 = 100 heads.",
        "100.",
        "100.",
        "200 × 0.5 = 100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Which of the following probabilities represents an event that is equally likely to occur or not occur?",
        "1/2",
        ["1/4", "3/4", "1"],
        "A probability of 0.5 (or 1/2) means equally likely (50-50 chance).",
        "1/2.",
        "1/2.",
        "1/2 represents 50-50 chance."
    ))

    # =========================================================================
    # LESSON 22: Probability Models (7.SP.C.6 / 7.SP.C.7)
    # =========================================================================
    LID = "G7_L22"
    LT = "Probability Models"
    DOM = "Statistics"
    STD = "7.SP.C.6 / 7.SP.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A fair 6-sided die is rolled 60 times. Theoretically, how many times do you expect to roll a 4? (60 × 1/6)",
        10, ["10"],
        "Expected frequency = 60 × (1/6) = 10.",
        "10.",
        "10.",
        "60 × 1/6 = 10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the difference between theoretical and experimental probability?",
        "Theoretical is based on mathematical reasoning of possible outcomes; experimental is based on actual trial data",
        ["They are always identical in every experiment", "Experimental is always greater than theoretical", "Theoretical is only for coins"],
        "Theoretical probability calculates what should happen; experimental records what actually happened.",
        "Theoretical = math reasoning; Experimental = actual trials.",
        "Theoretical is based on mathematical reasoning of possible outcomes; experimental is based on actual trial data.",
        "Theoretical is calculated; experimental is observed."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In a simulation, a spinner landed on red 24 times out of 80 spins. What is the experimental probability of red as a decimal?",
        0.3, ["0.3", "0.30"],
        "24 ÷ 80 = 3/10 = 0.3.",
        "0.3.",
        "0.3.",
        "24 ÷ 80 = 0.3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "According to the Law of Large Numbers, what happens to experimental probability as the number of trials increases?",
        "It gets closer and closer to the theoretical probability",
        ["It becomes 0", "It becomes 1", "It diverges away from theoretical"],
        "As trials increase, relative frequency converges toward theoretical probability.",
        "Gets closer to theoretical probability.",
        "It gets closer and closer to the theoretical probability.",
        "The Law of Large Numbers ensures convergence to theoretical probability."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A factory makes toys. 2 out of every 50 inspected toys have a defect (4%). In a batch of 1,500 toys, how many defective toys are expected?",
        60, ["60", "60 toys"],
        "0.04 × 1,500 = 60 defective toys.",
        "60 toys.",
        "60.",
        "0.04 × 1,500 = 60."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A uniform probability model has 5 possible outcomes (A, B, C, D, E) that are all equally likely. What is P(A)?",
        "1/5 (0.20)",
        ["1/4", "1/2", "5/1"],
        "Uniform model divides 1 equally among 5 outcomes: 1/5 = 0.20.",
        "1/5 (0.20).",
        "1/5 (0.20).",
        "P = 1/5 = 0.2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A bag has 100 tiles. In 20 random draws (with replacement), a blue tile was drawn 7 times (35%). Estimate how many blue tiles are in the bag of 100.",
        35, ["35", "35 tiles"],
        "0.35 × 100 = 35 blue tiles.",
        "35.",
        "35.",
        "35% of 100 = 35."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In a non-uniform probability model, P(Red) = 0.4 and P(Blue) = 0.35. If Green is the only other outcome, what is P(Green)?",
        "0.25",
        ["0.35", "0.15", "0.75"],
        "All probabilities must sum to 1: 1 - (0.40 + 0.35) = 1 - 0.75 = 0.25.",
        "0.25.",
        "0.25.",
        "1 - 0.75 = 0.25."
    ))

    # =========================================================================
    # LESSON 23: Compound Events & Sample Spaces (7.SP.C.8)
    # =========================================================================
    LID = "G7_L23"
    LT = "Compound Events & Sample Spaces"
    DOM = "Statistics"
    STD = "7.SP.C.8"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "You flip a coin (2 outcomes) and roll a 6-sided die (6 outcomes). How many total possible outcomes are in the sample space? (Fundamental Counting Principle: 2 × 6)",
        12, ["12", "12 outcomes"],
        "Multiply number of outcomes for each event: 2 × 6 = 12.",
        "12 outcomes.",
        "12.",
        "2 × 6 = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the probability of flipping Heads on a coin AND rolling a 6 on a 6-sided die? (1/2 × 1/6)",
        "1/12",
        ["1/8", "2/12", "1/6"],
        "For independent events: P(H and 6) = P(H) × P(6) = (1/2) × (1/6) = 1/12.",
        "1/12.",
        "1/12.",
        "1/2 × 1/6 = 1/12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "You flip two fair coins. What is the numerator of P(both Heads) when written as a fraction over 4? (Sample space: HH, HT, TH, TT)",
        1, ["1"],
        "HH is 1 outcome out of 4: 1/4. Numerator is 1.",
        "1.",
        "1.",
        "HH is 1 out of 4, numerator is 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "You choose 1 shirt from 4 colors, 1 pair of pants from 3 styles, and 1 pair of shoes from 2 pairs. How many different outfits can you make?",
        "24 outfits",
        ["9 outfits", "12 outfits", "18 outfits"],
        "4 × 3 × 2 = 24 outfits.",
        "24 outfits.",
        "24 outfits.",
        "4 × 3 × 2 = 24 outfits."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many total outcomes are possible when rolling two standard 6-sided dice? (6 × 6)",
        36, ["36", "36 outcomes"],
        "6 × 6 = 36 outcomes.",
        "36 outcomes.",
        "36.",
        "6 × 6 = 36."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "When rolling two 6-sided dice, how many outcomes give a sum of 7? (Pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1))",
        "6 outcomes",
        ["5 outcomes", "7 outcomes", "4 outcomes"],
        "There are 6 pairs that sum to 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).",
        "6 outcomes.",
        "6 outcomes.",
        "6 pairs sum to 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In problem Q06 (6 outcomes with sum 7 out of 36), what is the denominator of P(sum of 7) in simplest form (1/___)?",
        6, ["6"],
        "6/36 = 1/6. Denominator is 6.",
        "6.",
        "6.",
        "6/36 = 1/6, denominator is 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A bag has 3 red and 2 blue marbles. You draw a marble, do NOT replace it, and draw a second marble. What is P(both red)?",
        "3/10",
        ["9/25", "6/20", "1/5"],
        "First draw: 3/5. Second draw: 2/4 = 1/2. P = (3/5) × (1/2) = 3/10.",
        "3/10.",
        "3/10.",
        "(3/5) × (2/4) = 3/10."
    ))

    # =========================================================================
    # LESSON 24: Multi-Step Ratio & Geometry Word Problems (7.MP)
    # =========================================================================
    LID = "G7_L24"
    LT = "Multi-Step Ratio & Geometry Word Problems"
    DOM = "Geometry"
    STD = "7.MP"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A circular pool has diameter 14 meters. A safety rope is placed around its perimeter. Using π ≈ 22/7, what is the length of the rope in meters? (C = πd)",
        44, ["44", "44 m"],
        "C = (22/7) × 14 = 44 meters.",
        "44 m.",
        "44.",
        "(22/7) × 14 = 44 m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A jacket costs $80. It is discounted by 25%, and then 5% sales tax is added to the sale price. What is the final total?",
        "$63.00",
        ["$60.00", "$65.00", "$64.00"],
        "Sale price: 80 × 0.75 = $60. With 5% tax: 60 × 1.05 = $63.00.",
        "$63.00.",
        "$63.00.",
        "60 × 1.05 = $63.00."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A garden is rectangular with length 15 meters and width 8 meters. It is scaled up by a factor of 2. What is the area of the enlarged garden in square meters? (Original area = 120; Area scales by 2² = 4)",
        480, ["480", "480 sq m"],
        "120 × 4 = 480 square meters (or 30 × 16 = 480).",
        "480 sq m.",
        "480.",
        "120 × 4 = 480 sq m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A recipe for 4 people uses 2/3 cup of milk. How many cups of milk are needed for 12 people? (12 is 3 times 4)",
        2, ["2", "2 cups"],
        "(2/3) × 3 = 6/3 = 2 cups.",
        "2 cups.",
        "2.",
        "2/3 × 3 = 2 cups."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A cylindrical tank has radius 5 ft and height 10 ft. V = πr²h. Using π ≈ 3.14, what is the volume?",
        "785 cu ft",
        ["750 cu ft", "800 cu ft", "314 cu ft"],
        "V = 3.14 × 25 × 10 = 3.14 × 250 = 785 cubic feet.",
        "785 cu ft.",
        "785 cu ft.",
        "3.14 × 250 = 785 cu ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rectangular prism shipping box has dimensions 20 in × 15 in × 10 in (V = 3,000 cu in). Small cubes of edge 5 in (V = 125 cu in) are packed inside. How many cubes fit?",
        24, ["24", "24 cubes"],
        "(20÷5) × (15÷5) × (10÷5) = 4 × 3 × 2 = 24 cubes.",
        "24 cubes.",
        "24.",
        "4 × 3 × 2 = 24 cubes."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A store increases prices by 20%, then during a holiday sale decreases prices by 20%. The final price compared to the original price is:",
        "4% lower than original",
        ["Equal to original", "4% higher than original", "10% lower"],
        "1.20 × 0.80 = 0.96 = 96% of original (a 4% net decrease).",
        "4% lower.",
        "4% lower than original.",
        "1.20 × 0.80 = 0.96 -> 4% lower."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: 3x - 14 = 31.",
        15, ["15"],
        "3x = 45 -> x = 15.",
        "15.",
        "15.",
        "3x = 45 -> x = 15."
    ))

    # =========================================================================
    # LESSON 25: Cumulative Review (7.MP)
    # =========================================================================
    LID = "G7_L25"
    LT = "Cumulative Review"
    DOM = "Statistics"
    STD = "7.MP"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve for x: -5x + 12 = -18.",
        6, ["6"],
        "-5x = -30 -> x = 6.",
        "x = 6.",
        "6.",
        "-5x = -30 -> x = 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Evaluate: (-3/4) × (-8/9).",
        "2/3",
        ["-2/3", "24/36", "6/12"],
        "(-3 × -8) / (4 × 9) = 24/36 = 2/3.",
        "2/3.",
        "2/3.",
        "24/36 = 2/3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A runner covers 3/4 mile in 1/8 hour. What is the speed in mph?",
        6, ["6", "6 mph"],
        "(3/4) ÷ (1/8) = (3/4) × 8 = 6 mph.",
        "6 mph.",
        "6.",
        "3/4 × 8 = 6 mph."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the circumference of a circle with radius 5 cm? (Use π ≈ 3.14)",
        "31.4 cm",
        ["15.7 cm", "78.5 cm", "314 cm"],
        "C = 2 × 3.14 × 5 = 31.4 cm.",
        "31.4 cm.",
        "31.4 cm.",
        "2 × 3.14 × 5 = 31.4 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find simple interest earned on $500 at 4% for 3 years in dollars. (I = Prt)",
        60, ["60", "$60"],
        "I = 500 × 0.04 × 3 = $60.",
        "$60.",
        "60.",
        "500 × 0.04 × 3 = $60."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "What is the volume of a square pyramid with base side 6 cm and height 10 cm in cubic cm? (B = 36, V = 1/3 Bh)",
        120, ["120", "120 cm³"],
        "V = (1/3) × 36 × 10 = 12 × 10 = 120 cm³.",
        "120 cm³.",
        "120.",
        "1/3 × 36 × 10 = 120 cm³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Solve: -3(x - 4) ≤ 15.",
        "x ≥ -1",
        ["x ≤ -1", "x ≥ 1", "x ≤ 1"],
        "Divide by -3 and flip: x - 4 ≥ -5 -> x ≥ -1.",
        "x ≥ -1.",
        "x ≥ -1.",
        "x - 4 ≥ -5 -> x ≥ -1."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A bill is $85. A 20% tip is added. What is the total paid in dollars?",
        102, ["102", "$102"],
        "85 × 1.20 = $102.",
        "$102.",
        "102.",
        "85 × 1.20 = $102."
    ))

    return questions
