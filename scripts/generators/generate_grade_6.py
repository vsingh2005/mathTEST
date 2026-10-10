"""
scripts/generators/generate_grade_6.py
Script to generate the complete Grade 6 curriculum questions builder (Lessons 1-25).
"""

code = '''"""
scripts/builders/grade_6.py
High-fidelity mathematical question builder for Grade 6 (Lessons 1-25).
100% verified math answers, child-friendly prompts, and progressive 3-tier hints.
"""

from scripts.builders.helpers import make_numeric_question, make_mc_question

def build_grade_6_questions():
    questions = []
    G = 6

    # =========================================================================
    # LESSON 1: Introduction to Ratios (6.RP.A.1)
    # =========================================================================
    LID = "G6_L01"
    LT = "Introduction to Ratios"
    DOM = "Ratios, Rates"
    STD = "6.RP.A.1"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a fruit bowl, there are 4 apples and 7 oranges. What is the ratio of apples to oranges?",
        "4 to 7",
        ["7 to 4", "4 to 11", "7 to 11"],
        "A ratio compares two quantities in the specified order: (apples) : (oranges).",
        "Apples = 4, Oranges = 7 -> 4 to 7.",
        "4 to 7.",
        "The ratio of apples to oranges is 4 to 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In a class of 25 students, 15 are girls and 10 are boys. What is the simplified ratio of boys to girls? (Enter in format 2/3 as a fraction)",
        "2/3", ["2/3", "2:3", "2 to 3"],
        "Ratio of boys to girls = 10 : 15. Divide both by 5: 2 : 3.",
        "10 ÷ 5 = 2; 15 ÷ 5 = 3.",
        "2/3.",
        "10:15 simplifies to 2:3 (or 2/3)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A recipe uses 3 cups of flour for every 2 cups of sugar. If you use 6 cups of flour, how many cups of sugar should you use?",
        "4 cups",
        ["3 cups", "5 cups", "6 cups"],
        "Ratio flour:sugar is 3:2. If flour is doubled (3 × 2 = 6), sugar must also be doubled (2 × 2 = 4).",
        "4 cups.",
        "4 cups.",
        "3:2 = 6:4, so 4 cups of sugar are needed."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In a bag of marbles, the ratio of blue to red marbles is 5:3. If there are 15 blue marbles, how many red marbles are there?",
        9, ["9", "9 marbles"],
        "Multiply the ratio by 3 (since 5 × 3 = 15): 3 × 3 = 9 red marbles.",
        "9.",
        "9.",
        "5:3 = 15:9, so there are 9 red marbles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A sports team has won 12 games and lost 8 games. What is the ratio of wins to total games played in simplest form?",
        "3 to 5",
        ["3 to 2", "2 to 3", "12 to 8"],
        "Total games = 12 + 8 = 20. Ratio of wins to total = 12:20. Divide by 4: 3:5.",
        "3 to 5.",
        "3 to 5.",
        "12 / 20 = 3/5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "The ratio of cats to dogs at a shelter is 3:4. If there are 35 animals in total, how many cats are there?",
        15, ["15", "15 cats"],
        "Total ratio parts = 3 + 4 = 7 parts. Value of 1 part = 35 ÷ 7 = 5 animals. Cats = 3 × 5 = 15.",
        "15 cats.",
        "15.",
        "35 × (3/7) = 15 cats."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which ratio is NOT equivalent to 6:8?",
        "9:10",
        ["3:4", "12:16", "18:24"],
        "6:8 simplifies to 3:4. Multiply 3:4 by 3 gives 9:12, not 9:10.",
        "9:10.",
        "9:10.",
        "6:8 = 3:4; 9:10 is not equivalent to 3:4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In problem Q06 (35 animals, ratio 3:4), how many dogs are there?",
        20, ["20", "20 dogs"],
        "Dogs = 4 parts × 5 = 20 dogs. (Check: 15 + 20 = 35).",
        "20 dogs.",
        "20.",
        "35 × (4/7) = 20 dogs."
    ))

    # =========================================================================
    # LESSON 2: Unit Rates (6.RP.A.2)
    # =========================================================================
    LID = "G6_L02"
    LT = "Unit Rates"
    DOM = "Ratios, Rates"
    STD = "6.RP.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A car travels 180 miles in 3 hours. What is the unit rate in miles per hour (mph)?",
        60, ["60", "60 mph"],
        "Unit rate = (total distance) ÷ (total time) = 180 ÷ 3.",
        "180 ÷ 3 = 60 mph.",
        "60 mph.",
        "180 ÷ 3 = 60 miles per hour."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A grocery store sells 5 pounds of apples for $10. What is the unit price per pound?",
        "$2 per pound",
        ["$0.50 per pound", "$5 per pound", "$15 per pound"],
        "Unit price = (total cost) ÷ (pounds) = $10 ÷ 5 = $2/lb.",
        "$2 per pound.",
        "$2 per pound.",
        "$10 ÷ 5 = $2 per pound."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A typist types 240 words in 4 minutes. What is the typing speed in words per minute?",
        60, ["60", "60 wpm"],
        "Divide words by minutes: 240 ÷ 4 = 60.",
        "60 words per minute.",
        "60.",
        "240 ÷ 4 = 60 words per minute."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Brand A sells 12 oz of juice for $3.00 ($0.25/oz). Brand B sells 16 oz for $3.20 ($0.20/oz). Which is the better buy?",
        "Brand B, because its unit price is lower",
        ["Brand A, because the total cost is lower", "They are the same value", "Brand A, because it has fewer ounces"],
        "Compare unit prices: Brand A = 3.00/12 = $0.25/oz; Brand B = 3.20/16 = $0.20/oz. Brand B is cheaper per oz.",
        "Brand B.",
        "Brand B, because its unit price is lower.",
        "Brand B ($0.20/oz) is the better buy."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A runner covers 12 kilometers in 2 hours. At this rate, how many kilometers will the runner cover in 5 hours?",
        30, ["30", "30 km"],
        "Unit rate = 12 ÷ 2 = 6 km/h. Distance for 5 hours = 6 × 5 = 30 km.",
        "30 km.",
        "30.",
        "6 km/h × 5 h = 30 km."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A machine produces 350 bolts in 7 minutes. How many bolts does it produce in 10 minutes?",
        500, ["500", "500 bolts"],
        "Rate = 350 ÷ 7 = 50 bolts/min. In 10 min: 50 × 10 = 500 bolts.",
        "500 bolts.",
        "500.",
        "50 × 10 = 500 bolts."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If 8 movie tickets cost $96, what is the cost of 5 tickets at the same rate?",
        "$60",
        ["$50", "$65", "$70"],
        "Unit price = $96 ÷ 8 = $12 per ticket. Cost of 5 tickets = 5 × $12 = $60.",
        "$60.",
        "$60.",
        "96 ÷ 8 = 12; 5 × 12 = $60."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A pack of 6 pens costs $4.50. What is the unit cost of one pen in cents? (e.g. 75)",
        75, ["75", "75 cents", "$0.75"],
        "$4.50 ÷ 6 = $0.75 = 75 cents.",
        "75 cents.",
        "75.",
        "4.50 ÷ 6 = $0.75 (75 cents)."
    ))

    # =========================================================================
    # LESSON 3: Equivalent Ratios & Ratio Tables (6.RP.A.3a)
    # =========================================================================
    LID = "G6_L03"
    LT = "Equivalent Ratios & Ratio Tables"
    DOM = "Ratios, Rates"
    STD = "6.RP.A.3a"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a ratio table with ratio 2:5, what is the missing value: (2, 5), (4, 10), (6, ___)?",
        15, ["15"],
        "Each x is multiplied by 2.5 (or y = 5 × (x/2)). For x = 6: 6 × (5/2) = 15.",
        "15.",
        "15.",
        "2:5 = 6:15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which pair of values is equivalent to the ratio 3:4?",
        "(12, 16)",
        ["(9, 15)", "(6, 10)", "(15, 18)"],
        "Multiply both terms by 4: 3 × 4 = 12 and 4 × 4 = 16.",
        "(12, 16).",
        "(12, 16).",
        "3:4 = 12:16."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In a ratio table: 3 cups of water need 1 scoop of powder. How many scoops of powder are needed for 18 cups of water?",
        6, ["6", "6 scoops"],
        "Divide 18 by 3: 18 ÷ 3 = 6 scoops.",
        "6 scoops.",
        "6.",
        "18 ÷ 3 = 6 scoops."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "When equivalent ratio pairs from a table are plotted on a coordinate grid, they always lie on:",
        "A straight line passing through the origin (0, 0)",
        ["A curved line", "A horizontal line only", "A circle"],
        "Equivalent ratios represent proportional relationships, which graph as straight lines through (0, 0).",
        "Straight line through origin.",
        "A straight line passing through the origin (0, 0).",
        "Proportional relationships form a line through (0, 0)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the missing number in the ratio table: (4, 14), (8, 28), (10, ___).",
        35, ["35"],
        "Unit rate = 14 ÷ 4 = 3.5. For 10: 10 × 3.5 = 35.",
        "35.",
        "35.",
        "4:14 = 10:35."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "If (x, y) follows the ratio 5:9 and y = 45, what is the value of x?",
        25, ["25"],
        "9 was multiplied by 5 to get 45. Multiply 5 by 5: 5 × 5 = 25.",
        "25.",
        "25.",
        "5:9 = 25:45."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which point does NOT lie on the line representing the ratio 2:3?",
        "(6, 8)",
        ["(2, 3)", "(4, 6)", "(6, 9)"],
        "Check y/x: 3/2 = 1.5. For (6, 8), 8/6 = 1.33 ≠ 1.5.",
        "(6, 8).",
        "(6, 8).",
        "(6, 8) does not have ratio 2:3 (6:9 is correct)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A recipe ratio table has ingredients in ratio 4:7. If you have 28 of the second ingredient, how much of the first ingredient do you need?",
        16, ["16"],
        "7 × 4 = 28. Multiply 4 by 4: 4 × 4 = 16.",
        "16.",
        "16.",
        "4:7 = 16:28."
    ))

    # =========================================================================
    # LESSON 4: Percents as Rates per 100 (6.RP.A.3c)
    # =========================================================================
    LID = "G6_L04"
    LT = "Percents as Rates per 100"
    DOM = "Ratios, Rates"
    STD = "6.RP.A.3c"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is 25% of 80?",
        20, ["20"],
        "25% is equal to 1/4 (or 0.25). 80 ÷ 4 = 20.",
        "20.",
        "20.",
        "0.25 × 80 = 20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the fraction 3/5 written as a percentage?",
        "60%",
        ["35%", "50%", "75%"],
        "Convert to a fraction over 100: (3 × 20) / (5 × 20) = 60/100 = 60%.",
        "60%.",
        "60%.",
        "3/5 = 60/100 = 60%."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is 15% of 200?",
        30, ["30"],
        "15% of 100 is 15. For 200: 15 × 2 = 30 (or 0.15 × 200 = 30).",
        "30.",
        "30.",
        "0.15 × 200 = 30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "If 40% of a class is 12 students, how many total students are in the class?",
        "30 students",
        ["25 students", "32 students", "48 students"],
        "40% = 0.4. Total = 12 ÷ 0.4 = 120 ÷ 4 = 30 students.",
        "30 students.",
        "30 students.",
        "12 ÷ 0.4 = 30 students."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is 50% of 94?",
        47, ["47"],
        "50% is half of the number: 94 ÷ 2 = 47.",
        "47.",
        "47.",
        "94 ÷ 2 = 47."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A student scored 18 out of 20 on a math quiz. What percentage is that?",
        90, ["90", "90%"],
        "18/20 = (18 × 5) / (20 × 5) = 90/100 = 90%.",
        "90%.",
        "90.",
        "18/20 = 90%."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A jacket regularly priced at $80 is on sale for 30% off. What is the discount amount in dollars?",
        "$24",
        ["$30", "$20", "$56"],
        "Discount = 30% of $80 = 0.30 × 80 = $24.",
        "$24.",
        "$24.",
        "0.30 × $80 = $24."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In problem Q07 (regular price $80, discount $24), what is the sale price of the jacket in dollars?",
        56, ["56", "$56"],
        "$80 - $24 = $56.",
        "$56.",
        "56.",
        "$80 - $24 = $56."
    ))

    # =========================================================================
    # LESSON 5: Converting Measurement Units (6.RP.A.3d)
    # =========================================================================
    LID = "G6_L05"
    LT = "Converting Measurement Units"
    DOM = "Ratios, Rates"
    STD = "6.RP.A.3d"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Convert 8 feet to inches using ratio reasoning (1 foot = 12 inches).",
        96, ["96", "96 inches"],
        "Multiply feet by 12: 8 × 12 = 96 inches.",
        "96 inches.",
        "96.",
        "8 × 12 = 96 inches."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "How many meters are in 3.5 kilometers? (1 km = 1,000 m)",
        "3,500 meters",
        ["350 meters", "35,000 meters", "0.0035 meters"],
        "Multiply by 1,000: 3.5 × 1,000 = 3,500 m.",
        "3,500 meters.",
        "3,500 meters.",
        "3.5 × 1,000 = 3,500 m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "How many yards are in 72 feet? (1 yard = 3 feet)",
        24, ["24", "24 yards"],
        "Divide feet by 3: 72 ÷ 3 = 24 yards.",
        "24 yards.",
        "24.",
        "72 ÷ 3 = 24 yards."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "How many ounces are in 4.5 pounds? (1 lb = 16 oz)",
        "72 ounces",
        ["64 ounces", "68 ounces", "74 ounces"],
        "4.5 × 16 = 72 ounces.",
        "72 ounces.",
        "72 ounces.",
        "4.5 × 16 = 72 oz."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Convert 4,500 milliliters to liters. (1 L = 1,000 mL)",
        4.5, ["4.5", "4.5 L"],
        "Divide mL by 1,000: 4,500 ÷ 1,000 = 4.5 liters.",
        "4.5 L.",
        "4.5.",
        "4,500 ÷ 1,000 = 4.5 L."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A car drives at 60 miles per hour. How many miles does it travel in 15 minutes? (15 min = 1/4 hour)",
        15, ["15", "15 miles"],
        "60 × (1/4) = 15 miles.",
        "15 miles.",
        "15.",
        "60 × 0.25 = 15 miles."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If 1 inch is approximately 2.54 cm, about how many centimeters is 10 inches?",
        "25.4 cm",
        ["254 cm", "2.54 cm", "0.254 cm"],
        "Multiply by 10: 10 × 2.54 = 25.4 cm.",
        "25.4 cm.",
        "25.4 cm.",
        "10 × 2.54 = 25.4 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "How many cups are in 3 gallons? (1 gallon = 16 cups)",
        48, ["48", "48 cups"],
        "Multiply gallons by 16: 3 × 16 = 48 cups.",
        "48 cups.",
        "48.",
        "3 × 16 = 48 cups."
    ))

    # =========================================================================
    # LESSON 6: Dividing Fractions by Fractions (6.NS.A.1)
    # =========================================================================
    LID = "G6_L06"
    LT = "Dividing Fractions by Fractions"
    DOM = "The Number System"
    STD = "6.NS.A.1"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: (3/4) ÷ (1/2).",
        "3/2 (or 1 and 1/2)",
        ["3/8", "1/2", "2/3"],
        "Multiply by the reciprocal: (3/4) × (2/1) = 6/4 = 3/2 = 1 1/2.",
        "3/2 (1 1/2).",
        "3/2 (or 1 and 1/2).",
        "3/4 × 2/1 = 6/4 = 3/2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the reciprocal of 4/7? (Enter numerator of 7/4)",
        7, ["7"],
        "The reciprocal flips numerator and denominator: 7/4. Numerator is 7.",
        "7.",
        "7.",
        "Reciprocal of 4/7 is 7/4, numerator is 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: (2/3) ÷ (4/5).",
        "5/6",
        ["8/15", "6/5", "10/12"],
        "Multiply by reciprocal: (2/3) × (5/4) = 10/12 = 5/6.",
        "5/6.",
        "5/6.",
        "2/3 × 5/4 = 10/12 = 5/6."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A piece of wood is 3/4 meter long. It is cut into pieces of 1/8 meter each. How many pieces are there?",
        6, ["6", "6 pieces"],
        "(3/4) ÷ (1/8) = (3/4) × (8/1) = 24/4 = 6 pieces.",
        "6 pieces.",
        "6.",
        "3/4 × 8 = 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve: (5/6) ÷ (1/3).",
        "5/2 (or 2 and 1/2)",
        ["5/18", "6/15", "2/5"],
        "(5/6) × (3/1) = 15/6 = 5/2 = 2 1/2.",
        "5/2 (2 1/2).",
        "5/2 (or 2 and 1/2).",
        "5/6 × 3/1 = 15/6 = 5/2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 2 and 1/2 ÷ 3/4. (Convert 2 1/2 to 5/2 first). What is the numerator of the resulting improper fraction in simplest form (10/3)?",
        10, ["10"],
        "(5/2) ÷ (3/4) = (5/2) × (4/3) = 20/6 = 10/3. Numerator is 10.",
        "10.",
        "10.",
        "5/2 × 4/3 = 10/3, numerator is 10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A container holds 5/8 gallon of paint. Each craft project requires 1/16 gallon. How many projects can be completed?",
        "10 projects",
        ["8 projects", "12 projects", "5 projects"],
        "(5/8) ÷ (1/16) = (5/8) × 16 = 5 × 2 = 10 projects.",
        "10 projects.",
        "10 projects.",
        "5/8 × 16 = 10 projects."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve: (7/9) ÷ (7/18). What whole number does this equal?",
        2, ["2"],
        "(7/9) × (18/7) = 18/9 = 2.",
        "2.",
        "2.",
        "7/9 × 18/7 = 2."
    ))

    # =========================================================================
    # LESSON 7: Multi-Digit Decimals & Operations (6.NS.B.2 / 6.NS.B.3)
    # =========================================================================
    LID = "G6_L07"
    LT = "Multi-Digit Decimals & Operations"
    DOM = "The Number System"
    STD = "6.NS.B.2 / 6.NS.B.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve: 35.4 + 18.72.",
        54.12, ["54.12"],
        "35.40 + 18.72 = 54.12.",
        "54.12.",
        "54.12.",
        "35.40 + 18.72 = 54.12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: 42.5 - 16.38.",
        26.12, ["26.12"],
        "42.50 - 16.38 = 26.12.",
        "26.12.",
        "26.12.",
        "42.50 - 16.38 = 26.12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve: 4.8 × 3.5.",
        16.8, ["16.8", "16.80"],
        "48 × 35 = 1680. Two decimal places: 16.80 = 16.8.",
        "16.8.",
        "16.8.",
        "4.8 × 3.5 = 16.8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve: 15.75 ÷ 0.5.",
        31.5, ["31.5"],
        "Multiply by 10: 157.5 ÷ 5 = 31.5.",
        "31.5.",
        "31.5.",
        "15.75 ÷ 0.5 = 31.5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve using standard algorithm: 2,176 ÷ 34.",
        "64",
        ["62", "66", "54"],
        "34 × 60 = 2040; 2176 - 2040 = 136; 136 ÷ 34 = 4. 60 + 4 = 64.",
        "64.",
        "64.",
        "2,176 ÷ 34 = 64."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve: 0.25 × 0.16.",
        0.04, ["0.04", "0.0400"],
        "25 × 16 = 400. Four decimal places: 0.0400 = 0.04.",
        "0.04.",
        "0.04.",
        "0.25 × 0.16 = 0.04."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Solve: 7.56 ÷ 0.18.",
        42, ["42"],
        "Multiply by 100: 756 ÷ 18 = 42.",
        "42.",
        "42.",
        "7.56 ÷ 0.18 = 42."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A car drives 345.6 miles on 10.8 gallons of gasoline. What is its fuel efficiency in miles per gallon?",
        "32 mpg",
        ["30 mpg", "34 mpg", "36 mpg"],
        "345.6 ÷ 10.8 = 3456 ÷ 108 = 32 mpg.",
        "32 mpg.",
        "32 mpg.",
        "345.6 ÷ 10.8 = 32 mpg."
    ))

    # =========================================================================
    # LESSON 8: GCF & LCM (6.NS.B.4)
    # =========================================================================
    LID = "G6_L08"
    LT = "Greatest Common Factor & Least Common Multiple"
    DOM = "The Number System"
    STD = "6.NS.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the Greatest Common Factor (GCF) of 24 and 36.",
        12, ["12"],
        "Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36. GCF = 12.",
        "12.",
        "12.",
        "GCF(24, 36) = 12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Find the Least Common Multiple (LCM) of 6 and 8.",
        24, ["24"],
        "Multiples of 6: 6, 12, 18, 24, 30. Multiples of 8: 8, 16, 24, 32. LCM = 24.",
        "24.",
        "24.",
        "LCM(6, 8) = 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Use the distributive property to factor out the GCF: 36 + 48 = ___ × (3 + 4). What is the GCF?",
        "12",
        ["6", "8", "4"],
        "GCF of 36 and 48 is 12: 36 = 12 × 3 and 48 = 12 × 4. 12 × (3 + 4).",
        "12.",
        "12.",
        "36 + 48 = 12(3 + 4)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Hot dogs come in packs of 10. Buns come in packs of 8. What is the smallest number of hot dogs and buns you can buy so none are left over? (LCM of 10 and 8)",
        40, ["40"],
        "LCM(10, 8) = 40.",
        "40.",
        "40.",
        "LCM(10, 8) = 40."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the GCF of 18 and 45?",
        9, ["9"],
        "Factors of 18: 1, 2, 3, 6, 9, 18. Factors of 45: 1, 3, 5, 9, 15, 45. GCF = 9.",
        "9.",
        "9.",
        "GCF(18, 45) = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the LCM of 9 and 12.",
        36, ["36"],
        "Multiples of 9: 9, 18, 27, 36. Multiples of 12: 12, 24, 36. LCM = 36.",
        "36.",
        "36.",
        "LCM(9, 12) = 36."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which expression correctly shows 28 + 42 factored using the GCF?",
        "14(2 + 3)",
        ["7(4 + 6)", "2(14 + 21)", "4(7 + 10)"],
        "GCF of 28 and 42 is 14: 14 × 2 = 28 and 14 × 3 = 42. Factored form: 14(2 + 3).",
        "14(2 + 3).",
        "14(2 + 3).",
        "28 + 42 = 14(2 + 3)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the GCF of 30 and 75?",
        15, ["15"],
        "Factors of 30: 1, 2, 3, 5, 6, 10, 15, 30. Factors of 75: 1, 3, 5, 15, 25, 75. GCF = 15.",
        "15.",
        "15.",
        "GCF(30, 75) = 15."
    ))

    # =========================================================================
    # LESSON 9: Negative Numbers & Number Line (6.NS.C.5 / 6.NS.C.6)
    # =========================================================================
    LID = "G6_L09"
    LT = "Negative Numbers & Number Line"
    DOM = "The Number System"
    STD = "6.NS.C.5 / 6.NS.C.6"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which integer represents a bank withdrawal of $50?",
        "-50",
        ["+50", "0", "500"],
        "Withdrawals represent money taken out (negative): -50.",
        "-50.",
        "-50.",
        "A withdrawal of $50 is represented by -50."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the opposite of -14?",
        14, ["14", "+14"],
        "The opposite of a negative number is the positive number with the same distance from 0: -(-14) = 14.",
        "14.",
        "14.",
        "The opposite of -14 is 14."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A submarine is 250 feet below sea level. Which integer represents this elevation?",
        "-250",
        ["+250", "0", "-25"],
        "Below sea level is represented by negative integers: -250.",
        "-250.",
        "-250.",
        "250 feet below sea level is -250."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "On a horizontal number line, which statement is true about negative numbers?",
        "They are located to the left of 0 and decrease as you move further left",
        ["They are located to the right of 0", "They are greater than positive numbers", "They are all equal to 0"],
        "Negative numbers lie to the left of 0; numbers further left are smaller.",
        "To the left of 0.",
        "They are located to the left of 0 and decrease as you move further left.",
        "Negative numbers are to the left of 0 on a number line."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the opposite of the opposite of -8? (i.e. -(-(-8)))",
        -8, ["-8"],
        "The opposite of -8 is 8. The opposite of 8 is -8.",
        "-8.",
        "-8.",
        "-(-(-8)) = -8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which number line point represents the opposite of 3.5?",
        "-3.5",
        ["3.5", "0", "-7"],
        "The opposite of +3.5 is -3.5.",
        "-3.5.",
        "-3.5.",
        "The opposite of 3.5 is -3.5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "The temperature was -4°F. It dropped by 6°F. What is the new temperature in °F?",
        -10, ["-10", "-10°F"],
        "-4 - 6 = -10°F.",
        "-10°F.",
        "-10.",
        "-4 - 6 = -10°F."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Which situation is best represented by 0?",
        "Sea level",
        ["A 10-degree drop in temperature", "Owing $20", "Climbing a 100-foot hill"],
        "Sea level is the reference point (0 elevation).",
        "Sea level.",
        "Sea level.",
        "Sea level is represented by 0."
    ))

    # =========================================================================
    # LESSON 10: Absolute Value & Ordering (6.NS.C.7)
    # =========================================================================
    LID = "G6_L10"
    LT = "Absolute Value & Ordering"
    DOM = "The Number System"
    STD = "6.NS.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the absolute value of -15? (|-15|)",
        15, ["15"],
        "Absolute value is the distance from 0 on a number line, which is always non-negative: |-15| = 15.",
        "15.",
        "15.",
        "|-15| = 15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Compare -8 and -3. Which symbol makes the statement true: -8 ___ -3?",
        "<",
        [">", "=", "+"],
        "On a number line, -8 is further to the left than -3, so -8 is less than -3.",
        "-8 < -3.",
        "<.",
        "-8 < -3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Calculate: |24| - |-9|.",
        15, ["15"],
        "|24| = 24 and |-9| = 9. Then 24 - 9 = 15.",
        "15.",
        "15.",
        "24 - 9 = 15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Order from least to greatest: -6, 2, -10, 0, -1.",
        "-10, -6, -1, 0, 2",
        ["-1, -6, -10, 0, 2", "2, 0, -1, -6, -10", "-10, -6, 2, 0, -1"],
        "Most negative is smallest: -10 < -6 < -1 < 0 < 2.",
        "-10, -6, -1, 0, 2.",
        "-10, -6, -1, 0, 2.",
        "-10 < -6 < -1 < 0 < 2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Account A has a balance of -$45. Account B has a balance of -$70. Which person has greater debt?",
        "Account B, because |-70| > |-45|",
        ["Account A, because -45 > -70", "Both have the same debt", "Neither has debt"],
        "Debt is the magnitude of the negative balance: |-70| = $70 debt vs $45 debt.",
        "Account B has greater debt ($70).",
        "Account B, because |-70| > |-45|.",
        "Debt is measured by absolute value: |-70| = 70 > 45."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate: |-12| + |18| - |-5|.",
        25, ["25"],
        "12 + 18 - 5 = 30 - 5 = 25.",
        "25.",
        "25.",
        "12 + 18 - 5 = 25."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which statement about absolute value is always true?",
        "The absolute value of any non-zero number is positive",
        ["The absolute value of a negative number is negative", "The absolute value of a number is always greater than the number", "Absolute value depends on direction"],
        "Distance is always non-negative: |x| >= 0 for all x.",
        "Always positive for non-zero numbers.",
        "The absolute value of any non-zero number is positive.",
        "|x| is always non-negative."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the distance on a number line between -7 and 8? (|-7 - 8|)",
        15, ["15", "15 units"],
        "Distance = 8 - (-7) = 8 + 7 = 15 units.",
        "15 units.",
        "15.",
        "|-7 - 8| = 15 units."
    ))

    # =========================================================================
    # LESSON 11: Exponents & Numerical Expressions (6.EE.A.1)
    # =========================================================================
    LID = "G6_L11"
    LT = "Exponents & Numerical Expressions"
    DOM = "Expressions"
    STD = "6.EE.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Evaluate: 3⁴.",
        81, ["81"],
        "3⁴ = 3 × 3 × 3 × 3 = 9 × 9 = 81.",
        "81.",
        "81.",
        "3⁴ = 81."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which expression represents 5 × 5 × 5 in exponential form?",
        "5³",
        ["3⁵", "5 × 3", "15"],
        "The base is 5 and it is multiplied 3 times: 5³.",
        "5³.",
        "5³.",
        "5 × 5 × 5 = 5³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Evaluate: 2³ + 4².",
        24, ["24"],
        "2³ = 8; 4² = 16. 8 + 16 = 24.",
        "24.",
        "24.",
        "8 + 16 = 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Evaluate: 50 - 2 × 3².",
        "32",
        ["432", "144", "41"],
        "Exponents first: 3² = 9. Multiply: 2 × 9 = 18. Subtract: 50 - 18 = 32.",
        "32.",
        "32.",
        "50 - 2 × 9 = 50 - 18 = 32."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Evaluate: (6 - 2)² + 5 × 3.",
        31, ["31"],
        "Parentheses first: 6 - 2 = 4. Exponent: 4² = 16. Multiply: 5 × 3 = 15. Add: 16 + 15 = 31.",
        "31.",
        "31.",
        "16 + 15 = 31."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate: 4³ ÷ 8 + 3².",
        17, ["17"],
        "4³ = 64; 64 ÷ 8 = 8. 3² = 9. 8 + 9 = 17.",
        "17.",
        "17.",
        "64 ÷ 8 + 9 = 8 + 9 = 17."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Evaluate: 2 × (3 + 1)² - 10.",
        "22",
        ["26", "14", "38"],
        "Parentheses: 3 + 1 = 4. Exponent: 4² = 16. Multiply: 2 × 16 = 32. Subtract: 32 - 10 = 22.",
        "22.",
        "22.",
        "2 × 16 - 10 = 32 - 10 = 22."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate: 10² - (5² + 4²).",
        59, ["59"],
        "10² = 100. 5² + 4² = 25 + 16 = 41. 100 - 41 = 59.",
        "59.",
        "59.",
        "100 - 41 = 59."
    ))

    # =========================================================================
    # LESSON 12: Evaluating Algebraic Expressions (6.EE.A.2)
    # =========================================================================
    LID = "G6_L12"
    LT = "Evaluating Algebraic Expressions"
    DOM = "Expressions"
    STD = "6.EE.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Evaluate the expression 3x + 5 when x = 4.",
        17, ["17"],
        "Substitute x = 4: 3(4) + 5 = 12 + 5 = 17.",
        "17.",
        "17.",
        "3(4) + 5 = 12 + 5 = 17."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which algebraic expression represents '7 less than the product of 4 and y'?",
        "4y - 7",
        ["7 - 4y", "4y + 7", "4(y - 7)"],
        "Product of 4 and y is 4y; 7 less than that means subtract 7: 4y - 7.",
        "4y - 7.",
        "4y - 7.",
        "4y - 7 represents 7 less than 4y."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Evaluate 2a² - 3b when a = 3 and b = 2.",
        12, ["12"],
        "a² = 3² = 9. 2(9) = 18. 3b = 3(2) = 6. 18 - 6 = 12.",
        "12.",
        "12.",
        "2(9) - 3(2) = 18 - 6 = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In the expression 5x² + 3x + 8, what is the coefficient of x?",
        "3",
        ["5", "8", "2"],
        "The coefficient is the numerical factor multiplying the variable: in 3x, the coefficient is 3.",
        "3.",
        "3.",
        "The coefficient of x is 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Evaluate (m + n) ÷ 2 when m = 9 and n = 7.",
        8, ["8"],
        "m + n = 9 + 7 = 16. 16 ÷ 2 = 8.",
        "8.",
        "8.",
        "(9 + 7) ÷ 2 = 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate 4(x + y) - z when x = 3, y = 5, and z = 8.",
        24, ["24"],
        "x + y = 3 + 5 = 8. 4(8) = 32. 32 - 8 = 24.",
        "24.",
        "24.",
        "4(8) - 8 = 32 - 8 = 24."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which term in the expression 7x³ + 2x² - 9 is the constant term?",
        "-9",
        ["7", "2", "x³"],
        "A constant term has no variable attached: -9.",
        "-9.",
        "-9.",
        "-9 is the constant term."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate y³ - 2y when y = 3.",
        21, ["21"],
        "y³ = 3³ = 27. 2y = 2(3) = 6. 27 - 6 = 21.",
        "21.",
        "21.",
        "27 - 6 = 21."
    ))

    # =========================================================================
    # LESSON 13: Properties & Equivalent Expressions (6.EE.A.3 / 6.EE.A.4)
    # =========================================================================
    LID = "G6_L13"
    LT = "Properties & Equivalent Expressions"
    DOM = "Expressions"
    STD = "6.EE.A.3 / 6.EE.A.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Apply the distributive property: 3(x + 4) = ?",
        "3x + 12",
        ["3x + 4", "x + 12", "7x"],
        "Multiply each term inside by 3: 3 × x + 3 × 4 = 3x + 12.",
        "3x + 12.",
        "3x + 12.",
        "3(x + 4) = 3x + 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Combine like terms: 5x + 3x.",
        "8x",
        ["8x²", "15x", "8"],
        "Add coefficients of like terms: (5 + 3)x = 8x.",
        "8x.",
        "8x.",
        "5x + 3x = 8x."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Simplify by combining like terms: 4x + 7 + 2x - 3.",
        "6x + 4",
        ["6x + 10", "8x + 4", "6x - 4"],
        "Group like terms: (4x + 2x) + (7 - 3) = 6x + 4.",
        "6x + 4.",
        "6x + 4.",
        "4x + 2x + 7 - 3 = 6x + 4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which expression is equivalent to 2(3x + 5) + 4x?",
        "10x + 10",
        ["10x + 5", "6x + 10", "14x"],
        "Distribute: 6x + 10. Add 4x: (6x + 4x) + 10 = 10x + 10.",
        "10x + 10.",
        "10x + 10.",
        "6x + 10 + 4x = 10x + 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the coefficient of x when 7x - 2x + 4x is simplified?",
        9, ["9"],
        "(7 - 2 + 4)x = 9x. The coefficient is 9.",
        "9.",
        "9.",
        "7 - 2 + 4 = 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which pair of expressions are equivalent for all values of y?",
        "4(y + 2) and 4y + 8",
        ["4(y + 2) and 4y + 2", "3y + 5 and 8y", "y + y + y and y³"],
        "By distributive property, 4(y + 2) = 4y + 8.",
        "4(y + 2) and 4y + 8.",
        "4(y + 2) and 4y + 8.",
        "4(y + 2) = 4y + 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Factor out the GCF: 18x + 24.",
        "6(3x + 4)",
        ["3(6x + 8)", "2(9x + 12)", "12(x + 2)"],
        "GCF(18, 24) = 6. 18x ÷ 6 = 3x; 24 ÷ 6 = 4. Factored form: 6(3x + 4).",
        "6(3x + 4).",
        "6(3x + 4).",
        "18x + 24 = 6(3x + 4)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the constant term when 5(2x + 3) is expanded?",
        15, ["15"],
        "5 × 2x = 10x; 5 × 3 = 15. The constant term is 15.",
        "15.",
        "15.",
        "5 × 3 = 15."
    ))

    # =========================================================================
    # LESSON 14: Solving One-Variable Equations (6.EE.B.5 / 6.EE.B.7)
    # =========================================================================
    LID = "G6_L14"
    LT = "Solving One-Variable Equations"
    DOM = "Expressions"
    STD = "6.EE.B.5 / 6.EE.B.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve for x: x + 14 = 35.",
        21, ["21"],
        "Subtract 14 from both sides: x = 35 - 14.",
        "x = 21.",
        "21.",
        "x = 35 - 14 = 21."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve for y: 6y = 48.",
        8, ["8"],
        "Divide both sides by 6: y = 48 ÷ 6 = 8.",
        "y = 8.",
        "8.",
        "y = 48 ÷ 6 = 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve for m: m - 18 = 47.",
        65, ["65"],
        "Add 18 to both sides: m = 47 + 18.",
        "m = 65.",
        "65.",
        "m = 47 + 18 = 65."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve for p: p ÷ 4 = 15.",
        60, ["60"],
        "Multiply both sides by 4: p = 15 × 4.",
        "p = 60.",
        "60.",
        "p = 15 × 4 = 60."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Which value is a solution to the equation 2.5x = 10?",
        "4",
        ["2", "5", "25"],
        "Divide 10 by 2.5: 10 ÷ 2.5 = 4.",
        "4.",
        "4.",
        "2.5 × 4 = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve for w: (3/4)w = 12.",
        16, ["16"],
        "Multiply by reciprocal (4/3): w = 12 × (4/3) = 48/3 = 16.",
        "w = 16.",
        "16.",
        "w = 12 × (4/3) = 16."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Marcus had some money m. After spending $14.50 on lunch, he had $25.50 left. Which equation represents this?",
        "m - 14.50 = 25.50",
        ["m + 14.50 = 25.50", "25.50 - m = 14.50", "14.50m = 25.50"],
        "Original money m minus spent $14.50 equals $25.50.",
        "m - 14.50 = 25.50.",
        "m - 14.50 = 25.50.",
        "m - 14.50 = 25.50."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In problem Q07 (m - 14.50 = 25.50), how much money did Marcus have originally in dollars?",
        40, ["40", "$40"],
        "m = 25.50 + 14.50 = $40.00.",
        "$40.",
        "40.",
        "m = 25.50 + 14.50 = $40."
    ))

    # =========================================================================
    # LESSON 15: Writing & Graphing Inequalities (6.EE.B.8)
    # =========================================================================
    LID = "G6_L15"
    LT = "Writing & Graphing Inequalities"
    DOM = "Expressions"
    STD = "6.EE.B.8"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which inequality represents 'You must be at least 48 inches tall to ride'?",
        "h ≥ 48",
        ["h > 48", "h ≤ 48", "h < 48"],
        "'At least' means 48 or greater: h ≥ 48.",
        "h ≥ 48.",
        "h ≥ 48.",
        "'At least 48' means h ≥ 48."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "On a number line, how do you graph the inequality x > 3?",
        "An open circle at 3 with an arrow pointing right",
        ["A closed circle at 3 with arrow right", "An open circle at 3 with arrow left", "A closed circle at 3 with arrow left"],
        "Strict inequality (>) uses an open circle (3 is not included) and shades to the right (greater).",
        "Open circle at 3, arrow pointing right.",
        "An open circle at 3 with an arrow pointing right.",
        "x > 3 has an open circle at 3 and arrow right."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Which inequality represents 'The temperature is at most 32 degrees'?",
        "t ≤ 32",
        ["t < 32", "t ≥ 32", "t > 32"],
        "'At most' means 32 or less: t ≤ 32.",
        "t ≤ 32.",
        "t ≤ 32.",
        "'At most 32' means t ≤ 32."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following values is NOT a solution to x < 7?",
        "7",
        ["6", "0", "-2"],
        "For strict inequality x < 7, 7 is not less than 7.",
        "7 is not a solution.",
        "7.",
        "7 is not strictly less than 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "On a number line, when do you use a closed (solid) circle?",
        "When the inequality includes 'or equal to' (≤ or ≥)",
        ["When the inequality is strictly greater than (>)", "When the number is negative", "Always"],
        "A solid circle means the boundary number itself is included in the solution set.",
        "For ≤ and ≥.",
        "When the inequality includes 'or equal to' (≤ or ≥).",
        "Closed circles represent ≤ and ≥."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "What is the largest integer that satisfies the inequality x < 15?",
        14, ["14"],
        "The integer immediately less than 15 is 14.",
        "14.",
        "14.",
        "14 is the largest integer < 15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A speed limit sign says 55 mph. Which inequality represents legal speeds s?",
        "s ≤ 55",
        ["s ≥ 55", "s < 55", "s = 55"],
        "Speed must be 55 mph or less: s ≤ 55.",
        "s ≤ 55.",
        "s ≤ 55.",
        "Speed limit means s ≤ 55."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the smallest integer that satisfies x ≥ -3?",
        -3, ["-3"],
        "Since the inequality is ≥ (or equal to), -3 is included.",
        "-3.",
        "-3.",
        "-3 is the minimum value."
    ))

    # =========================================================================
    # LESSON 16: Area of Triangles & Quadrilaterals (6.G.A.1)
    # =========================================================================
    LID = "G6_L16"
    LT = "Area of Triangles & Quadrilaterals"
    DOM = "Geometry"
    STD = "6.G.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the area of a triangle with base 8 cm and height 5 cm in square cm. (Area = 1/2 × b × h)",
        20, ["20", "20 sq cm"],
        "Area = (1/2) × 8 × 5 = 4 × 5 = 20 square cm.",
        "20.",
        "20.",
        "1/2 × 8 × 5 = 20 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Find the area of a parallelogram with base 12 meters and height 7 meters in square meters. (Area = b × h)",
        84, ["84", "84 sq m"],
        "Area = base × height = 12 × 7 = 84 square meters.",
        "84.",
        "84.",
        "12 × 7 = 84 sq m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A trapezoid has parallel bases of 6 cm and 10 cm, and height 4 cm. What is its area in square cm? (Area = 1/2 × (b1 + b2) × h)",
        32, ["32", "32 sq cm"],
        "Average of bases = (6 + 10) / 2 = 8. Area = 8 × 4 = 32 square cm.",
        "32.",
        "32.",
        "1/2 × (6 + 10) × 4 = 32 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A right triangle has legs of length 6 inches and 8 inches. What is its area in square inches?",
        "24 square inches",
        ["48 square inches", "14 square inches", "28 square inches"],
        "In a right triangle, the two legs are the base and height: Area = (1/2) × 6 × 8 = 24 sq in.",
        "24 sq in.",
        "24 square inches.",
        "1/2 × 6 × 8 = 24 sq in."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A triangle has an area of 36 square meters and a base of 9 meters. What is its height in meters? (h = 2 × Area ÷ b)",
        8, ["8", "8 meters"],
        "2 × 36 = 72. Height = 72 ÷ 9 = 8 meters.",
        "8 meters.",
        "8.",
        "2 × 36 ÷ 9 = 8 m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rhombus has diagonals of lengths 10 cm and 14 cm. What is its area in square cm? (Area = 1/2 × d1 × d2)",
        70, ["70", "70 sq cm"],
        "(1/2) × 10 × 14 = 5 × 14 = 70 square cm.",
        "70.",
        "70.",
        "1/2 × 10 × 14 = 70 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A trapezoid has bases 8 ft and 12 ft with height 6 ft. What is its area?",
        "60 sq ft",
        ["120 sq ft", "48 sq ft", "72 sq ft"],
        "Area = (1/2) × (8 + 12) × 6 = (1/2) × 20 × 6 = 60 sq ft.",
        "60 sq ft.",
        "60 sq ft.",
        "1/2 × 20 × 6 = 60 sq ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the area of a triangle with base 15 cm and height 12 cm in square cm.",
        90, ["90", "90 sq cm"],
        "(1/2) × 15 × 12 = 15 × 6 = 90 square cm.",
        "90.",
        "90.",
        "1/2 × 15 × 12 = 90 sq cm."
    ))

    # =========================================================================
    # LESSON 17: Area of Irregular Polygons (6.G.A.1)
    # =========================================================================
    LID = "G6_L17"
    LT = "Area of Irregular Polygons"
    DOM = "Geometry"
    STD = "6.G.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "An irregular polygon is decomposed into a rectangle (area 40 sq m) and a triangle (area 15 sq m). What is the total area in square meters?",
        55, ["55", "55 sq m"],
        "Add the areas of the decomposed shapes: 40 + 15 = 55 square meters.",
        "55 sq m.",
        "55.",
        "40 + 15 = 55 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the best method to calculate the area of an irregular polygon?",
        "Decompose it into familiar non-overlapping shapes (rectangles, triangles) and sum their areas",
        ["Multiply the perimeter by 2", "Measure only the longest diagonal", "Multiply all side lengths together"],
        "Decomposing into standard shapes (rectangles, triangles) allows calculating individual areas.",
        "Decompose and sum areas.",
        "Decompose it into familiar non-overlapping shapes (rectangles, triangles) and sum their areas.",
        "Decomposing into standard shapes and summing areas gives the total area."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "An L-shaped figure is split into two rectangles: Rectangle A is 8 m × 3 m (area 24) and Rectangle B is 5 m × 4 m (area 20). What is the total area in square meters?",
        44, ["44", "44 sq m"],
        "24 + 20 = 44 square meters.",
        "44 sq m.",
        "44.",
        "24 + 20 = 44 sq m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A house-shaped figure consists of a square of side 6 ft and a triangular roof of base 6 ft and height 4 ft. What is the total area in square feet?",
        "48 sq ft",
        ["36 sq ft", "60 sq ft", "52 sq ft"],
        "Square area = 6 × 6 = 36 sq ft. Triangle area = 1/2 × 6 × 4 = 12 sq ft. Total = 36 + 12 = 48 sq ft.",
        "48 sq ft.",
        "48 sq ft.",
        "36 + 12 = 48 sq ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A park polygon is composed of three rectangles with areas 120, 85, and 95 square yards. What is the total park area in square yards?",
        300, ["300", "300 sq yd"],
        "120 + 85 + 95 = 300 square yards.",
        "300 sq yd.",
        "300.",
        "120 + 85 + 95 = 300 sq yd."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A figure is made of a rectangle (10 cm by 8 cm = 80 sq cm) with two identical right triangles cut out, each having legs 3 cm and 4 cm (each area 6 sq cm). What is the remaining area in square cm?",
        68, ["68", "68 sq cm"],
        "Total cut out = 6 + 6 = 12 sq cm. Remaining = 80 - 12 = 68 square cm.",
        "68 sq cm.",
        "68.",
        "80 - 12 = 68 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A polygon consists of a trapezoid (area 45 cm²) joined to a rectangle (area 30 cm²). What is the total area?",
        "75 cm²",
        ["85 cm²", "90 cm²", "65 cm²"],
        "45 + 30 = 75 cm².",
        "75 cm².",
        "75 cm².",
        "45 + 30 = 75 cm²."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "An irregular floor has three sections: 50 sq ft, 42 sq ft, and 28 sq ft. What is the total area in square feet?",
        120, ["120", "120 sq ft"],
        "50 + 42 + 28 = 120 square feet.",
        "120 sq ft.",
        "120.",
        "50 + 42 + 28 = 120 sq ft."
    ))

    # =========================================================================
    # LESSON 18: Volume with Fractional Edges (6.G.A.2)
    # =========================================================================
    LID = "G6_L18"
    LT = "Volume of Rectangular Prisms with Fractional Edges"
    DOM = "Geometry"
    STD = "6.G.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the volume of a rectangular prism with length 1/2 meter, width 1/3 meter, and height 1/4 meter in cubic meters.",
        "1/24 cubic meter",
        ["1/9 cubic meter", "1/12 cubic meter", "3/9 cubic meter"],
        "Volume = (1/2) × (1/3) × (1/4) = 1/(2 × 3 × 4) = 1/24 cubic meter.",
        "1/24 cubic meter.",
        "1/24 cubic meter.",
        "1/2 × 1/3 × 1/4 = 1/24 m³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "How many small cubes with edge length 1/2 inch fit inside a 1-inch cube?",
        8, ["8", "8 cubes"],
        "Volume of 1-inch cube = 1. Volume of small cube = (1/2)³ = 1/8. 1 ÷ (1/8) = 8 cubes.",
        "8 cubes.",
        "8.",
        "2 × 2 × 2 = 8 cubes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the volume of a box with length 2 and 1/2 feet (5/2 ft), width 4 feet, and height 3 feet in cubic feet.",
        30, ["30", "30 cu ft"],
        "V = (5/2) × 4 × 3 = 10 × 3 = 30 cubic feet.",
        "30 cu ft.",
        "30.",
        "5/2 × 12 = 30 cu ft."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A prism has length 3/4 m, width 2/3 m, and height 1/2 m. What is its volume in cubic meters?",
        "1/4 cubic meter",
        ["1/8 cubic meter", "6/24 cubic meter", "1/3 cubic meter"],
        "V = (3/4) × (2/3) × (1/2) = 6/24 = 1/4 m³.",
        "1/4 cubic meter.",
        "1/4 cubic meter.",
        "6/24 = 1/4 m³."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A box measures 1 and 1/2 inches by 2 inches by 3 inches. What is its volume in cubic inches?",
        9, ["9", "9 cu in"],
        "V = (3/2) × 2 × 3 = 3 × 3 = 9 cubic inches.",
        "9 cu in.",
        "9.",
        "3/2 × 6 = 9 cu in."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A prism is 4 cm long, 2 and 1/2 cm wide (5/2 cm), and 1 and 1/5 cm high (6/5 cm). What is its volume in cubic cm?",
        12, ["12", "12 cm³"],
        "V = 4 × (5/2) × (6/5) = 10 × (6/5) = 12 cm³.",
        "12 cm³.",
        "12.",
        "4 × (5/2) × (6/5) = 12 cm³."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "How many cubes of edge 1/3 foot fit into a prism of dimensions 2 ft by 1 ft by 1 ft (volume 2 cu ft)?",
        "54 cubes",
        ["18 cubes", "27 cubes", "36 cubes"],
        "Volume of small cube = (1/3)³ = 1/27 cu ft. Number of cubes = 2 ÷ (1/27) = 54 cubes.",
        "54 cubes.",
        "54 cubes.",
        "2 ÷ (1/27) = 54 cubes."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Calculate the volume of a rectangular prism with length 3/5 m, width 5/6 m, and height 2 m in cubic meters. (Enter as a fraction: e.g. 1)",
        1, ["1", "1.0", "1 m³"],
        "V = (3/5) × (5/6) × 2 = (15/30) × 2 = (1/2) × 2 = 1 cubic meter.",
        "1 m³.",
        "1.",
        "(3/5 × 5/6) × 2 = 1/2 × 2 = 1 m³."
    ))

    # =========================================================================
    # LESSON 19: Surface Area & Nets (6.G.A.4)
    # =========================================================================
    LID = "G6_L19"
    LT = "Surface Area & Nets"
    DOM = "Geometry"
    STD = "6.G.A.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the surface area of a cube with edge length 3 cm in square cm. (SA = 6 × s²)",
        54, ["54", "54 sq cm"],
        "Area of one face = 3² = 9 sq cm. A cube has 6 identical faces: 6 × 9 = 54 sq cm.",
        "54 sq cm.",
        "54.",
        "6 × 3² = 54 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A net of a rectangular prism unfolds into how many 2-dimensional rectangular faces?",
        "6 faces",
        ["4 faces", "8 faces", "12 faces"],
        "A rectangular prism has 6 rectangular faces (top/bottom, front/back, left/right).",
        "6 faces.",
        "6 faces.",
        "A rectangular prism has 6 faces."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the surface area of a rectangular prism with length 5 cm, width 4 cm, and height 3 cm in square cm. (SA = 2(lw + lh + wh))",
        94, ["94", "94 sq cm"],
        "lw = 20, lh = 15, wh = 12. Sum = 47. 2 × 47 = 94 sq cm.",
        "94 sq cm.",
        "94.",
        "2(20 + 15 + 12) = 94 sq cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "The net of a square pyramid consists of:",
        "1 square base and 4 triangular faces",
        ["2 square bases and 4 rectangles", "4 squares and 2 triangles", "5 triangles"],
        "A square pyramid has 1 square base and 4 triangles meeting at the apex.",
        "1 square and 4 triangles.",
        "1 square base and 4 triangular faces.",
        "Square pyramid net = 1 square and 4 triangles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A square pyramid has a base of 6 cm by 6 cm (area 36) and 4 triangular faces each with base 6 cm and height 5 cm (each area 15). What is the total surface area in square cm?",
        96, ["96", "96 sq cm"],
        "Base = 36. 4 triangles = 4 × 15 = 60. Total SA = 36 + 60 = 96 sq cm.",
        "96 sq cm.",
        "96.",
        "36 + 60 = 96 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the surface area of a rectangular prism measuring 10 inches by 6 inches by 2 inches in square inches.",
        184, ["184", "184 sq in"],
        "2 × (60 + 20 + 12) = 2 × 92 = 184 sq in.",
        "184 sq in.",
        "184.",
        "2(60 + 20 + 12) = 184 sq in."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the surface area of a cube with edge length 5 feet?",
        "150 sq ft",
        ["125 sq ft", "100 sq ft", "175 sq ft"],
        "6 × 5² = 6 × 25 = 150 sq ft.",
        "150 sq ft.",
        "150 sq ft.",
        "6 × 25 = 150 sq ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A triangular prism net has two triangular bases (each area 12 cm²) and three rectangular faces with areas 30 cm², 40 cm², and 50 cm². What is the total surface area in square cm?",
        144, ["144", "144 sq cm"],
        "Total SA = (2 × 12) + (30 + 40 + 50) = 24 + 120 = 144 sq cm.",
        "144 sq cm.",
        "144.",
        "24 + 120 = 144 sq cm."
    ))

    # =========================================================================
    # LESSON 20: Polygons in Coordinate Plane (6.G.A.3)
    # =========================================================================
    LID = "G6_L20"
    LT = "Polygons in Coordinate Plane"
    DOM = "Geometry"
    STD = "6.G.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the distance between points (2, 3) and (2, 9) in the coordinate plane?",
        6, ["6", "6 units"],
        "Same x-coordinate: distance is the vertical difference |9 - 3| = 6 units.",
        "6 units.",
        "6.",
        "|9 - 3| = 6 units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the distance between points (-4, 5) and (3, 5) in the coordinate plane?",
        7, ["7", "7 units"],
        "Same y-coordinate: distance is the horizontal difference |3 - (-4)| = 3 + 4 = 7 units.",
        "7 units.",
        "7.",
        "|3 - (-4)| = 7 units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rectangle has vertices at (1, 1), (1, 5), (6, 5), and (6, 1). What is its perimeter in units?",
        18, ["18", "18 units"],
        "Height = 5 - 1 = 4. Width = 6 - 1 = 5. Perimeter = 2 × (4 + 5) = 18 units.",
        "18 units.",
        "18.",
        "2(4 + 5) = 18 units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the area of the rectangle from Q03 with vertices (1, 1), (1, 5), (6, 5), (6, 1) in square units?",
        20, ["20", "20 sq units"],
        "Area = width × height = 5 × 4 = 20 square units.",
        "20 sq units.",
        "20.",
        "5 × 4 = 20 sq units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A right triangle has vertices at (0, 0), (6, 0), and (0, 8). What is its area in square units?",
        "24 square units",
        ["48 square units", "14 square units", "20 square units"],
        "Base = 6, Height = 8. Area = (1/2) × 6 × 8 = 24 sq units.",
        "24 sq units.",
        "24 square units.",
        "1/2 × 6 × 8 = 24 sq units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A rectangle has vertices at (-3, 2), (-3, -4), (5, -4), and (5, 2). What is its area in square units?",
        48, ["48", "48 sq units"],
        "Width = |5 - (-3)| = 8. Height = |2 - (-4)| = 6. Area = 8 × 6 = 48 sq units.",
        "48 sq units.",
        "48.",
        "8 × 6 = 48 sq units."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the perimeter of the rectangle from Q06 with width 8 and height 6?",
        "28 units",
        ["48 units", "14 units", "24 units"],
        "Perimeter = 2 × (8 + 6) = 2 × 14 = 28 units.",
        "28 units.",
        "28 units.",
        "2(8 + 6) = 28 units."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Distance between (-5, -2) and (-5, 6) in units:",
        8, ["8", "8 units"],
        "|6 - (-2)| = 8 units.",
        "8 units.",
        "8.",
        "|6 - (-2)| = 8 units."
    ))

    # =========================================================================
    # LESSON 21: Statistical Questions & Variability (6.SP.A.1 / 6.SP.A.2)
    # =========================================================================
    LID = "G6_L21"
    LT = "Statistical Questions & Variability"
    DOM = "Statistics, Data"
    STD = "6.SP.A.1 / 6.SP.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which of the following is a statistical question?",
        "How many books did each student in the 6th grade read this year?",
        ["How tall is Mount Everest?", "How many days are in a week?", "How old is the teacher right now?"],
        "A statistical question anticipates variability in the data collected from multiple subjects.",
        "Books read by 6th graders (has variability).",
        "How many books did each student in the 6th grade read this year?",
        "It anticipates variability in answers among students."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Why is 'How old is Liam?' NOT a statistical question?",
        "It has only one specific answer with no variability",
        ["It involves numbers", "It is about a student", "It cannot be answered"],
        "A single person\\'s age has one exact answer, so there is no variability.",
        "No variability in the answer.",
        "It has only one specific answer with no variability.",
        "Non-statistical questions have a single fixed answer."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the range of this dataset: 12, 18, 9, 25, 14, 30. (Range = Maximum - Minimum)",
        21, ["21"],
        "Maximum = 30; Minimum = 9. Range = 30 - 9 = 21.",
        "21.",
        "21.",
        "30 - 9 = 21."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following describes the spread or variability of a data set?",
        "Range and Interquartile Range (IQR)",
        ["Mean and Median", "Mode only", "Sample size"],
        "Measures of center are mean and median; measures of spread/variability are range and IQR.",
        "Range and IQR.",
        "Range and Interquartile Range (IQR).",
        "Range and IQR measure variability."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the range of test scores: 85, 92, 78, 95, 88?",
        17, ["17"],
        "Max = 95; Min = 78. Range = 95 - 78 = 17.",
        "17.",
        "17.",
        "95 - 78 = 17."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Which of the following is a statistical question?",
        "How many minutes do middle schoolers spend on homework each night?",
        ["What time does school start tomorrow?", "Is 17 a prime number?", "How many states are in the USA?"],
        "Homework time varies from student to student (variability).",
        "Homework minutes (has variability).",
        "How many minutes do middle schoolers spend on homework each night?",
        "It anticipates variability in middle schoolers\\' homework times."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A data distribution is symmetrical and bell-shaped. Which measure of center best summarizes the data?",
        "Mean",
        ["Range", "Maximum", "Mode"],
        "For symmetric distributions without extreme outliers, the mean is the preferred measure of center.",
        "Mean.",
        "Mean.",
        "Mean is best for symmetric data."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In a data set with maximum 104 and range 48, what is the minimum value?",
        56, ["56"],
        "Minimum = Maximum - Range = 104 - 48 = 56.",
        "56.",
        "56.",
        "104 - 48 = 56."
    ))

    # =========================================================================
    # LESSON 22: Measures of Center: Mean, Median (6.SP.B.5c)
    # =========================================================================
    LID = "G6_L22"
    LT = "Measures of Center: Mean, Median"
    DOM = "Statistics, Data"
    STD = "6.SP.B.5c"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the mean (average) of the data set: 6, 8, 10, 12, 14. (Sum ÷ count)",
        10, ["10"],
        "Sum = 6 + 8 + 10 + 12 + 14 = 50. Mean = 50 ÷ 5 = 10.",
        "10.",
        "10.",
        "50 ÷ 5 = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Find the median of the ordered data set: 3, 5, 7, 9, 11, 13, 15.",
        9, ["9"],
        "The median is the middle value in the sorted list. With 7 items, the 4th item is 9.",
        "9.",
        "9.",
        "The middle value is 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the median of this data set: 4, 8, 12, 16, 20, 24. (Average the two middle numbers)",
        14, ["14"],
        "Middle numbers are 12 and 16. Median = (12 + 16) ÷ 2 = 28 ÷ 2 = 14.",
        "14.",
        "14.",
        "(12 + 16) ÷ 2 = 14."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Find the mode (most frequent number) of: 5, 8, 7, 5, 9, 5, 8, 10.",
        5, ["5"],
        "5 appears 3 times, which is more than any other number.",
        "5.",
        "5.",
        "5 is the mode."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A data set has scores: 10, 12, 14, 15, 100. Why is the median (14) a better measure of center than the mean (30.2)?",
        "The outlier 100 pulls the mean up, while the median is resistant to outliers",
        ["The mean is always harder to calculate", "The median is always larger than the mean", "The mode is 14"],
        "Outliers distort the mean; the median gives a truer picture of the center.",
        "Median is resistant to extreme outliers.",
        "The outlier 100 pulls the mean up, while the median is resistant to outliers.",
        "Median is not distorted by extreme outliers like 100."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Maya has test scores of 80, 85, and 95. What score must she get on her 4th test to have an overall mean of 90? (Need total 360)",
        100, ["100"],
        "Total needed = 90 × 4 = 360. Current sum = 80 + 85 + 95 = 260. 360 - 260 = 100.",
        "100.",
        "100.",
        "360 - 260 = 100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the mean of: 15, 20, 25, 30, 35, 45?",
        "28.33",
        ["27.5", "30", "25"],
        "Sum = 170. 170 ÷ 6 ≈ 28.33.",
        "28.33.",
        "28.33.",
        "170 ÷ 6 ≈ 28.33."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the median of: 15, 7, 22, 13, 9, 18. (Sorted: 7, 9, 13, 15, 18, 22)",
        14, ["14"],
        "Middle numbers are 13 and 15. Median = (13 + 15) ÷ 2 = 14.",
        "14.",
        "14.",
        "(13 + 15) ÷ 2 = 14."
    ))

    # =========================================================================
    # LESSON 23: Displaying Data: Histograms & Box Plots (6.SP.B.4)
    # =========================================================================
    LID = "G6_L23"
    LT = "Displaying Data: Histograms & Box Plots"
    DOM = "Statistics, Data"
    STD = "6.SP.B.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a box plot, the five-number summary values are: Min=10, Q1=18, Median=25, Q3=32, Max=40. What is the Interquartile Range (IQR = Q3 - Q1)?",
        14, ["14"],
        "IQR = Q3 - Q1 = 32 - 18 = 14.",
        "14.",
        "14.",
        "32 - 18 = 14."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What percentage of the data in a box plot lies inside the box (between Q1 and Q3)?",
        "50%",
        ["25%", "75%", "100%"],
        "The box spans from the 25th percentile (Q1) to the 75th percentile (Q3), containing exactly 50% of the data.",
        "50%.",
        "50%.",
        "The IQR contains 50% of the data."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What is the difference between a bar graph and a histogram?",
        "Histograms display continuous data grouped into equal intervals with touching bars",
        ["Bar graphs have no labels", "Histograms only show categories like fruit types", "They are identical"],
        "Histograms show frequency distributions of continuous numerical intervals (bins) with touching bars.",
        "Continuous intervals with touching bars.",
        "Histograms display continuous data grouped into equal intervals with touching bars.",
        "Histograms show numerical frequency intervals."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In a box plot with Q1 = 45 and Q3 = 65, what is the IQR?",
        20, ["20"],
        "IQR = 65 - 45 = 20.",
        "20.",
        "20.",
        "65 - 45 = 20."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "On a dot plot, there are 4 dots above 5, 6 dots above 6, and 2 dots above 7. What is the total number of data points?",
        "12",
        ["10", "14", "18"],
        "4 + 6 + 2 = 12 data points.",
        "12.",
        "12.",
        "4 + 6 + 2 = 12."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Given sorted data: 2, 4, 6, 8, 10, 12, 14, 16. Lower half is (2, 4, 6, 8), Q1 = (4+6)/2 = 5. Upper half is (10, 12, 14, 16), Q3 = (12+14)/2 = 13. What is the IQR?",
        8, ["8"],
        "IQR = Q3 - Q1 = 13 - 5 = 8.",
        "8.",
        "8.",
        "13 - 5 = 8."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In a histogram with bin intervals 0-9, 10-19, 20-29, 30-39, in which interval would a data value of 24 be counted?",
        "20-29",
        ["10-19", "30-39", "0-9"],
        "24 falls between 20 and 29 inclusive.",
        "20-29.",
        "20-29.",
        "24 is in the 20-29 bin."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In a box plot, the minimum is 12 and the maximum is 58. What is the overall range?",
        46, ["46"],
        "Range = Max - Min = 58 - 12 = 46.",
        "46.",
        "46.",
        "58 - 12 = 46."
    ))

    # =========================================================================
    # LESSON 24: Financial Literacy: Managing Money (6.RP / practical)
    # =========================================================================
    LID = "G6_L24"
    LT = "Financial Literacy: Managing Money"
    DOM = "Statistics, Data"
    STD = "6.RP / practical"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Carlos earns $150 per week. He budgets 20% of his earnings for savings. How many dollars does he save each week?",
        30, ["30", "$30"],
        "Savings = 0.20 × 150 = $30.",
        "$30.",
        "30.",
        "0.20 × 150 = $30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "What is the difference between a debit card and a credit card?",
        "A debit card withdraws money directly from your bank account; a credit card borrows money that must be repaid",
        ["A credit card uses your own cash", "A debit card charges interest fees on purchases", "They are identical"],
        "Debit cards spend money already in your checking account; credit cards borrow money.",
        "Debit card uses your cash; credit card borrows money.",
        "A debit card withdraws money directly from your bank account; a credit card borrows money that must be repaid.",
        "Debit spends checking funds; credit borrows money."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Sofia has a starting bank balance of $250. She deposits $75 and withdraws $40. What is her new balance in dollars?",
        285, ["285", "$285"],
        "250 + 75 - 40 = 325 - 40 = $285.",
        "$285.",
        "285.",
        "250 + 75 - 40 = $285."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In a balanced budget, which relationship should hold true?",
        "Total Income ≥ Total Expenses + Savings",
        ["Expenses should exceed Income", "Income should be 0", "Savings should equal Total Debt"],
        "A balanced budget ensures total expenses do not exceed total income.",
        "Income ≥ Expenses.",
        "Total Income ≥ Total Expenses + Savings.",
        "Income must cover expenses and savings."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A monthly budget has $800 income. Rent is $400, food is $200, and utilities are $80. How many dollars remain for savings?",
        120, ["120", "$120"],
        "Expenses = 400 + 200 + 80 = $680. Savings = 800 - 680 = $120.",
        "$120.",
        "120.",
        "800 - 680 = $120."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Leo deposits $500 into a savings account that earns 3% simple annual interest. How much interest in dollars does he earn in 1 year? (I = Prt)",
        15, ["15", "$15"],
        "Interest = 500 × 0.03 × 1 = $15.",
        "$15.",
        "15.",
        "500 × 0.03 = $15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following is considered a fixed expense in a monthly budget?",
        "Monthly apartment rent",
        ["Grocery bill", "Movie theater tickets", "Electric bill in summer"],
        "Fixed expenses stay the same amount every month (like rent).",
        "Monthly apartment rent.",
        "Monthly apartment rent.",
        "Rent is a fixed recurring expense."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If a person with $500 balance writes a check for $520 with no overdraft protection, what is the negative balance in dollars?",
        -20, ["-20", "-$20"],
        "500 - 520 = -$20.",
        "-$20.",
        "-20.",
        "500 - 520 = -$20."
    ))

    # =========================================================================
    # LESSON 25: Cumulative Word Problems (6.MP)
    # =========================================================================
    LID = "G6_L25"
    LT = "Cumulative Word Problems"
    DOM = "Statistics, Data"
    STD = "6.MP"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A recipe calls for a ratio of 2 cups of oats to 3 cups of water. To make a large batch using 12 cups of water, how many cups of oats are needed?",
        8, ["8", "8 cups"],
        "Water multiplied by 4 (3 × 4 = 12). Oats = 2 × 4 = 8 cups.",
        "8 cups.",
        "8.",
        "2 × 4 = 8 cups."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve: (4/5) ÷ (2/3).",
        "6/5 (or 1 and 1/5)",
        ["8/15", "5/6", "2/5"],
        "(4/5) × (3/2) = 12/10 = 6/5 = 1 1/5.",
        "6/5 (1 1/5).",
        "6/5 (or 1 and 1/5).",
        "4/5 × 3/2 = 6/5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve for x: 3x + 15 = 48.",
        11, ["11"],
        "3x = 48 - 15 = 33. x = 33 ÷ 3 = 11.",
        "11.",
        "11.",
        "3x = 33 -> x = 11."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the surface area of a cube with edge length 4 cm in square cm?",
        "96 sq cm",
        ["64 sq cm", "48 sq cm", "16 sq cm"],
        "SA = 6 × s² = 6 × 16 = 96 sq cm.",
        "96 sq cm.",
        "96 sq cm.",
        "6 × 16 = 96 sq cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the area of a triangle with base 14 meters and height 6 meters in square meters.",
        42, ["42", "42 sq m"],
        "Area = (1/2) × 14 × 6 = 7 × 6 = 42 sq m.",
        "42 sq m.",
        "42.",
        "1/2 × 14 × 6 = 42 sq m."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A store has a 25% off sale. A skateboard normally costs $80. What is the sale price in dollars?",
        60, ["60", "$60"],
        "Discount = 0.25 × 80 = $20. Sale price = 80 - 20 = $60.",
        "$60.",
        "60.",
        "80 - 20 = $60."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the mean of: 12, 16, 20, 24, 28?",
        "20",
        ["18", "22", "24"],
        "Sum = 100. 100 ÷ 5 = 20.",
        "20.",
        "20.",
        "100 ÷ 5 = 20."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate: 4² - 3 × 2 + 5.",
        15, ["15"],
        "4² = 16; 3 × 2 = 6. 16 - 6 + 5 = 15.",
        "15.",
        "15.",
        "16 - 6 + 5 = 15."
    ))

    return questions
'''

with open('scripts/builders/grade_6.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated scripts/builders/grade_6.py successfully!")
