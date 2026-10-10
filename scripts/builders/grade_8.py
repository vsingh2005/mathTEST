"""
scripts/builders/grade_8.py
High-fidelity mathematical question builder for Grade 8 (Lessons 1-25).
100% verified math answers, child-friendly prompts, and progressive 3-tier hints.
"""

from scripts.builders.helpers import make_numeric_question, make_mc_question

def build_grade_8_questions():
    questions = []
    G = 8

    # =========================================================================
    # LESSON 1: Translations, Reflections & Rotations (8.G.A.1)
    # =========================================================================
    LID = "G8_L01"
    LT = "Translations, Reflections & Rotations"
    DOM = "Rigid Transformations & Congruence"
    STD = "8.G.A.1"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A point at (3, 5) is translated 4 units right and 2 units down. What are its new coordinates?",
        "(7, 3)",
        ["(7, 7)", "(-1, 3)", "(1, 7)"],
        "Translate right means add to x (3 + 4 = 7); down means subtract from y (5 - 2 = 3).",
        "(7, 3).",
        "(7, 3).",
        "(3+4, 5-2) = (7, 3)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which properties are preserved under rigid transformations (translations, reflections, and rotations)?",
        "Both side lengths and angle measures are preserved",
        ["Only side lengths are preserved", "Only angle measures are preserved", "Neither lengths nor angles are preserved"],
        "Rigid motions preserve both distances (lengths) and angle measures, maintaining congruent shapes.",
        "Both side lengths and angle measures.",
        "Both side lengths and angle measures are preserved.",
        "Rigid transformations preserve size and shape."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "The point (-2, 4) is reflected across the x-axis. What is its new y-coordinate?",
        -4, ["-4"],
        "Reflecting across the x-axis keeps the x-coordinate the same and negates y: (x, -y).",
        "-4.",
        "-4.",
        "4 becomes -4."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "The point (3, -5) is reflected across the y-axis. What are its new coordinates?",
        "(-3, -5)",
        ["(-3, 5)", "(3, 5)", "(5, -3)"],
        "Reflecting across the y-axis negates the x-coordinate while y stays the same: (-x, y).",
        "(-3, -5).",
        "(-3, -5).",
        "(-3, -5)."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A point (2, 4) is rotated 90 degrees counterclockwise about the origin. What are its new coordinates?",
        "(-4, 2)",
        ["(4, -2)", "(-2, -4)", "(4, 2)"],
        "A 90° counterclockwise rotation maps (x, y) to (-y, x). Here, (2, 4) becomes (-4, 2).",
        "(-4, 2).",
        "(-4, 2).",
        "(x, y) -> (-y, x) -> (-4, 2)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A triangle vertex is at (1, 6). After a 180-degree rotation about the origin, what is the new x-coordinate?",
        -1, ["-1"],
        "A 180° rotation about the origin maps (x, y) to (-x, -y). New x is -1.",
        "-1.",
        "-1.",
        "x becomes -1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A line segment of length 8 cm is rotated 90 degrees clockwise and then translated 5 units up. What is the length of the resulting segment?",
        "8 cm",
        ["13 cm", "3 cm", "16 cm"],
        "Rotations and translations are rigid motions and preserve segment length.",
        "8 cm.",
        "8 cm.",
        "Rigid transformations preserve length: 8 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Point A(-3, 2) is translated by (x + 5, y - 7). What is the sum of the new x and y coordinates?",
        -3, ["-3"],
        "New coordinates: x = -3 + 5 = 2; y = 2 - 7 = -5. Sum = 2 + (-5) = -3.",
        "-3.",
        "-3.",
        "2 + (-5) = -3."
    ))

    # =========================================================================
    # LESSON 2: Sequences of Transformations (8.G.A.2)
    # =========================================================================
    LID = "G8_L02"
    LT = "Sequences of Transformations"
    DOM = "Rigid Transformations & Congruence"
    STD = "8.G.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Two 2-dimensional figures are congruent if and only if:",
        "One figure can be mapped onto the other through a sequence of rigid transformations",
        ["They have the same color", "They have the same orientation", "One is twice as large as the other"],
        "Congruence means identical size and shape, obtainable via translations, reflections, or rotations.",
        "Can be mapped via rigid motions.",
        "One figure can be mapped onto the other through a sequence of rigid transformations.",
        "Rigid transformations demonstrate congruence."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Point (1, 2) is reflected across the y-axis, then translated 3 units right. What is the final x-coordinate?",
        2, ["2"],
        "Reflection across y-axis gives x = -1. Then translate 3 units right: -1 + 3 = 2.",
        "2.",
        "2.",
        "-1 + 3 = 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Triangle ABC has angle measures 40°, 60°, and 80°. After a sequence of reflections and rotations to form Triangle A'B'C', what is the measure of angle A' in degrees?",
        40, ["40", "40 degrees", "40°"],
        "Rigid transformations preserve all angle measures.",
        "40°.",
        "40.",
        "Angle measure is preserved: 40°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Point (4, -1) is rotated 180 degrees about the origin, then translated up 5 units. What is the final y-coordinate?",
        6, ["6"],
        "180° rotation negates coordinates: (4, -1) -> (-4, 1). Translate up 5: y = 1 + 5 = 6.",
        "6.",
        "6.",
        "1 + 5 = 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Which sequence of transformations can map a shape onto a mirror image that is shifted across the grid?",
        "A reflection followed by a translation",
        ["Two translations", "A dilation", "A stretch"],
        "A reflection flips the orientation (mirror image), and a translation shifts the position.",
        "Reflection then translation.",
        "A reflection followed by a translation.",
        "Reflection flips orientation; translation moves it."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Triangle 1 has side lengths 5, 12, and 13. If Triangle 2 is congruent to Triangle 1, what is the perimeter of Triangle 2?",
        30, ["30"],
        "Congruent triangles have identical side lengths: Perimeter = 5 + 12 + 13 = 30.",
        "30.",
        "30.",
        "5 + 12 + 13 = 30."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Can a sequence of rigid transformations change the area of a polygon?",
        "No, rigid transformations preserve both area and perimeter",
        ["Yes, rotations change the area", "Yes, reflections double the area", "Yes, translations decrease the area"],
        "Rigid motions preserve all distances, angles, and areas.",
        "No, area is preserved.",
        "No, rigid transformations preserve both area and perimeter.",
        "Rigid transformations preserve area."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Point (2, 3) is reflected across the x-axis, then reflected across the y-axis. This two-step sequence is equivalent to a single rotation about the origin of how many degrees?",
        180, ["180", "180 degrees", "180°"],
        "(x, y) -> (x, -y) -> (-x, -y). This is identical to a 180° rotation about the origin.",
        "180°.",
        "180.",
        "Successive reflections across perpendicular axes equal 180° rotation."
    ))

    # =========================================================================
    # LESSON 3: Angle Relationships & Parallel Lines (8.G.A.5)
    # =========================================================================
    LID = "G8_L03"
    LT = "Angle Relationships & Parallel Lines"
    DOM = "Rigid Transformations & Congruence"
    STD = "8.G.A.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "What is the sum of the interior angle measures of any triangle in degrees?",
        180, ["180", "180 degrees", "180°"],
        "The interior angles of any triangle always sum to 180°.",
        "180°.",
        "180.",
        "Sum of triangle interior angles is 180°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In triangle ABC, angle A = 55° and angle B = 65°. What is the measure of angle C in degrees?",
        60, ["60", "60 degrees", "60°"],
        "Angle C = 180 - (55 + 65) = 180 - 120 = 60°.",
        "60°.",
        "60.",
        "180 - 120 = 60°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Two parallel lines are cut by a transversal. If one alternate interior angle measures 72°, what is the measure of the other alternate interior angle in degrees?",
        72, ["72", "72 degrees", "72°"],
        "When parallel lines are intersected by a transversal, alternate interior angles are congruent (equal).",
        "72°.",
        "72.",
        "Alternate interior angles are equal: 72°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Two parallel lines are cut by a transversal. If an interior angle measures 110°, what is the measure of its consecutive (same-side) interior angle in degrees?",
        70, ["70", "70 degrees", "70°"],
        "Consecutive (same-side) interior angles are supplementary (sum to 180°): 180 - 110 = 70°.",
        "70°.",
        "70.",
        "180 - 110 = 70°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "The exterior angle of a triangle is always equal to:",
        "The sum of the two remote interior angles",
        ["The adjacent interior angle", "180 degrees minus the perimeter", "Twice the smallest angle"],
        "The Exterior Angle Theorem states that an exterior angle equals the sum of the two opposite remote interior angles.",
        "Sum of two remote interior angles.",
        "The sum of the two remote interior angles.",
        "Exterior angle = sum of remote interior angles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "In triangle XYZ, two remote interior angles measure 48° and 76°. What is the measure of the exterior angle at the third vertex in degrees?",
        124, ["124", "124 degrees", "124°"],
        "Exterior angle = 48° + 76° = 124°.",
        "124°.",
        "124.",
        "48 + 76 = 124°."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If two lines are cut by a transversal and their corresponding angles are both 85°, what must be true?",
        "The two lines are parallel",
        ["The two lines are perpendicular", "The transversal is horizontal", "The lines intersect at a right angle"],
        "Equal corresponding angles prove that the two lines are parallel.",
        "The lines are parallel.",
        "The two lines are parallel.",
        "Equal corresponding angles guarantee parallel lines."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "The angles of a triangle are (2x)°, (3x)°, and (5x)°. Find the value of x.",
        18, ["18"],
        "2x + 3x + 5x = 10x = 180°. x = 180 ÷ 10 = 18.",
        "18.",
        "18.",
        "10x = 180 -> x = 18."
    ))

    # =========================================================================
    # LESSON 4: Dilations & Scale Factor (8.G.A.3 / 8.G.A.4)
    # =========================================================================
    LID = "G8_L04"
    LT = "Dilations & Scale Factor"
    DOM = "Dilations, Similarity & Introducing Slope"
    STD = "8.G.A.3 / 8.G.A.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Point (3, 4) is dilated by a scale factor of 3 centered at the origin. What is the new y-coordinate?",
        12, ["12"],
        "Multiply coordinates by scale factor: new y = 4 × 3 = 12.",
        "12.",
        "12.",
        "4 × 3 = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A dilation with a scale factor of k = 0.5 results in:",
        "A reduction (smaller figure)",
        ["An enlargement (larger figure)", "A congruent figure", "A reflection"],
        "A scale factor between 0 and 1 produces a reduction.",
        "A reduction.",
        "A reduction (smaller figure).",
        "k < 1 produces a reduction."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A rectangle with width 6 cm and length 10 cm is dilated by a scale factor of 2.5. What is the new length in cm?",
        25, ["25", "25 cm"],
        "New length = 10 × 2.5 = 25 cm.",
        "25 cm.",
        "25.",
        "10 × 2.5 = 25 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Under a dilation centered at the origin with scale factor k = 2, what is the algebraic rule for any point (x, y)?",
        "(2x, 2y)",
        ["(x + 2, y + 2)", "(x / 2, y / 2)", "(2x, y)"],
        "A dilation multiplies each coordinate by scale factor k: (kx, ky) -> (2x, 2y).",
        "(2x, 2y).",
        "(2x, 2y).",
        "Rule is (kx, ky) = (2x, 2y)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A segment of length 15 is dilated by scale factor k = 2/3. What is the new length?",
        10, ["10"],
        "New length = 15 × (2/3) = 30/3 = 10.",
        "10.",
        "10.",
        "15 × 2/3 = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A triangle has an area of 12 square inches. If it is dilated by a scale factor of 3, what is the area of the dilated triangle in square inches?",
        108, ["108", "108 sq in"],
        "Area scales by k²: New Area = 12 × 3² = 12 × 9 = 108 square inches.",
        "108 sq in.",
        "108.",
        "12 × 3² = 108 sq in."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What happens to angle measures when a polygon is dilated by a scale factor of 4?",
        "Angle measures remain exactly the same",
        ["Angle measures are multiplied by 4", "Angle measures are divided by 4", "Angle measures sum to 720 degrees"],
        "Dilations preserve angle measures; shapes remain similar.",
        "Angles stay the same.",
        "Angle measures remain exactly the same.",
        "Dilations preserve angles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Point A(8, 12) is dilated to A'(2, 3) centered at the origin. What is the scale factor k? (Enter as a fraction or decimal: e.g. 0.25 or 1/4)",
        0.25, ["0.25", "1/4"],
        "Scale factor k = 2/8 = 3/12 = 1/4 = 0.25.",
        "0.25 or 1/4.",
        "0.25.",
        "2/8 = 1/4 = 0.25."
    ))

    # =========================================================================
    # LESSON 5: Similar Figures (8.G.A.4)
    # =========================================================================
    LID = "G8_L05"
    LT = "Similar Figures"
    DOM = "Dilations, Similarity & Introducing Slope"
    STD = "8.G.A.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Two geometric figures are similar if and only if:",
        "Corresponding angles are equal and corresponding side lengths are proportional",
        ["They have identical perimeters", "They have the same orientation", "All side lengths are equal to 1"],
        "Similarity requires equal corresponding angles and proportional side lengths.",
        "Equal angles, proportional sides.",
        "Corresponding angles are equal and corresponding side lengths are proportional.",
        "Definition of geometric similarity."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Triangle ABC is similar to Triangle DEF. Side AB = 4 and side DE = 12. If side BC = 5, what is the length of side EF?",
        15, ["15"],
        "Scale factor = 12 ÷ 4 = 3. Side EF = 5 × 3 = 15.",
        "15.",
        "15.",
        "5 × (12/4) = 15."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A 6-foot-tall person casts a 4-foot shadow. At the same time, a nearby tree casts an 18-foot shadow. How tall is the tree in feet?",
        27, ["27", "27 ft", "27 feet"],
        "Set up proportion: 6 / 4 = h / 18 -> 4h = 108 -> h = 27 feet.",
        "27 ft.",
        "27.",
        "6/4 × 18 = 27 ft."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Triangle 1 has angles 50° and 60°. Triangle 2 has angles 50° and 70°. Are the two triangles similar?",
        "Yes, by the Angle-Angle (AA) similarity criterion",
        ["No, because 60 is not equal to 70", "Only if their sides are equal", "Cannot be determined"],
        "In Triangle 1, the third angle is 180 - 110 = 70°. Both have angles 50°, 60°, and 70°, so AA criterion holds.",
        "Yes, by AA similarity.",
        "Yes, by the Angle-Angle (AA) similarity criterion.",
        "Both triangles have angles 50°, 60°, and 70°."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Rectangle A is 4 cm by 8 cm. Rectangle B is similar to A and has a shorter side of 10 cm. What is the longer side of Rectangle B in cm?",
        20, ["20", "20 cm"],
        "Scale factor = 10 ÷ 4 = 2.5. Longer side = 8 × 2.5 = 20 cm.",
        "20 cm.",
        "20.",
        "8 × 2.5 = 20 cm."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Two similar polygons have side ratio 1:4. If the perimeter of the smaller polygon is 18 cm, what is the perimeter of the larger polygon in cm?",
        72, ["72", "72 cm"],
        "Perimeter scales linearly with scale factor: 18 × 4 = 72 cm.",
        "72 cm.",
        "72.",
        "18 × 4 = 72 cm."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If the ratio of side lengths of two similar figures is 2:5, what is the ratio of their areas?",
        "4:25",
        ["2:5", "4:10", "8:125"],
        "Area ratio is the square of the side length ratio: 2² : 5² = 4:25.",
        "4:25.",
        "4:25.",
        "2²:5² = 4:25."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Two similar triangles have side ratio 3:5. If the area of the smaller triangle is 27 sq cm, what is the area of the larger triangle in sq cm?",
        75, ["75", "75 sq cm"],
        "Area ratio = (5/3)² = 25/9. Larger area = 27 × (25/9) = 3 × 25 = 75 sq cm.",
        "75 sq cm.",
        "75.",
        "27 × 25/9 = 75 sq cm."
    ))

    # =========================================================================
    # LESSON 6: Introducing Slope via Similar Triangles (8.EE.B.6)
    # =========================================================================
    LID = "G8_L06"
    LT = "Introducing Slope via Similar Triangles"
    DOM = "Dilations, Similarity & Introducing Slope"
    STD = "8.EE.B.6"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Why is the slope between any two points on a straight line constant?",
        "Slope triangles along the line are similar, so the ratio of vertical change to horizontal change is constant",
        ["The line is always horizontal", "The line always passes through (0, 0)", "Straight lines have no slope"],
        "Right triangles formed along a straight line are similar, making rise/run identical everywhere.",
        "Slope triangles are similar.",
        "Slope triangles along the line are similar, so the ratio of vertical change to horizontal change is constant.",
        "Similar triangles establish constant slope."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A slope triangle on a line has a vertical rise of 6 and a horizontal run of 2. What is the slope of the line?",
        3, ["3"],
        "Slope = rise ÷ run = 6 ÷ 2 = 3.",
        "3.",
        "3.",
        "6 ÷ 2 = 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "On the same line with slope 3, another slope triangle has a horizontal run of 5. What must its vertical rise be?",
        15, ["15"],
        "Rise = slope × run = 3 × 5 = 15.",
        "15.",
        "15.",
        "3 × 5 = 15."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "What is the standard formula for finding the slope m between two points (x1, y1) and (x2, y2)?",
        "m = (y2 - y1) / (x2 - x1)",
        ["m = (x2 - x1) / (y2 - y1)", "m = (y2 + y1) / (x2 + x1)", "m = (x2)(y2) - (x1)(y1)"],
        "Slope is the ratio of vertical change (delta y) to horizontal change (delta x).",
        "m = (y2 - y1) / (x2 - x1).",
        "m = (y2 - y1) / (x2 - x1).",
        "Rise over run formula."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Find the slope of the line passing through points (1, 2) and (4, 11).",
        3, ["3"],
        "m = (11 - 2) ÷ (4 - 1) = 9 ÷ 3 = 3.",
        "3.",
        "3.",
        "(11 - 2)/(4 - 1) = 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the slope of the line passing through points (2, 5) and (6, 13).",
        2, ["2"],
        "m = (13 - 5) ÷ (6 - 2) = 8 ÷ 4 = 2.",
        "2.",
        "2.",
        "(13 - 5)/(6 - 2) = 2."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Slope triangle A has rise/run = 4/6, and slope triangle B has rise/run = 6/9. Do they lie on the same straight line?",
        "Yes, because 4/6 simplifies to 2/3 and 6/9 simplifies to 2/3",
        ["No, because 4 and 6 are different numbers", "Only if both triangles have hypotenuse 10", "Cannot be determined"],
        "Both simplify to 2/3, confirming a constant rate of change.",
        "Yes, both equal 2/3.",
        "Yes, because 4/6 simplifies to 2/3 and 6/9 simplifies to 2/3.",
        "Both equal 2/3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A line has slope 4 and passes through (1, 3). If a point on this line has x = 4, what is its y-coordinate?",
        15, ["15"],
        "y - 3 = 4(4 - 1) = 12 -> y = 15.",
        "15.",
        "15.",
        "3 + 4(3) = 15."
    ))

    # =========================================================================
    # LESSON 7: Slope & Proportional Relationships (8.EE.B.5)
    # =========================================================================
    LID = "G8_L07"
    LT = "Slope & Proportional Relationships"
    DOM = "Linear Relationships & Proportional Relationships"
    STD = "8.EE.B.5"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a proportional relationship y = kx, if y = 20 when x = 4, what is the unit rate (slope k)?",
        5, ["5"],
        "k = y ÷ x = 20 ÷ 4 = 5.",
        "5.",
        "5.",
        "20 ÷ 4 = 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "The graph of any proportional relationship must always:",
        "Be a straight line that passes through the origin (0, 0)",
        ["Be a curved line passing through (1, 1)", "Have a negative slope", "Pass through the point (0, 10)"],
        "Proportional graphs are straight lines passing through (0, 0).",
        "Pass through (0, 0).",
        "Be a straight line that passes through the origin (0, 0).",
        "Direct proportionality passes through the origin."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Car A travels according to d = 65t (miles in t hours), and Car B travels according to d = 55t. Which car is faster?",
        "Car A, because its speed (slope) 65 mph is greater than 55 mph",
        ["Car B, because 55 is smaller", "Both cars travel at identical speeds", "Cannot be determined without travel time"],
        "The slope represents unit rate of speed: 65 > 55.",
        "Car A is faster (65 mph).",
        "Car A, because its speed (slope) 65 mph is greater than 55 mph.",
        "Higher slope equals higher speed."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A runner travels distance d = 8t (miles in t hours). How far does the runner travel in 3.5 hours in miles?",
        28, ["28", "28 miles"],
        "d = 8 × 3.5 = 28 miles.",
        "28 miles.",
        "28.",
        "8 × 3.5 = 28 miles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A graph of juice bottles sold passes through (0, 0) and (5, 15), where x is bottles and y is cost in dollars. What is the unit price per bottle in dollars?",
        3, ["3", "$3"],
        "Unit price = 15 ÷ 5 = $3 per bottle.",
        "$3.",
        "3.",
        "15 ÷ 5 = $3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Company X charges $12 per hour (y = 12x). Company Y charges $45 for 3 hours. What is the difference in their hourly rates in dollars?",
        3, ["3", "$3"],
        "Company Y hourly rate = 45 ÷ 3 = $15. Difference = 15 - 12 = $3 per hour.",
        "$3.",
        "3.",
        "15 - 12 = $3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What does the slope of a distance-versus-time graph represent physically?",
        "Speed (rate of motion)",
        ["Total distance", "Acceleration", "Starting position"],
        "Rise (distance) divided by run (time) is speed (velocity).",
        "Speed.",
        "Speed (rate of motion).",
        "Distance ÷ time = speed."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If y varies directly with x, and y = 42 when x = 6, what is the value of y when x = 9?",
        63, ["63"],
        "k = 42 ÷ 6 = 7. For x = 9: y = 7 × 9 = 63.",
        "63.",
        "63.",
        "7 × 9 = 63."
    ))

    # =========================================================================
    # LESSON 8: Slope-Intercept Form y = mx + b (8.EE.B.6 / 8.F.A.3)
    # =========================================================================
    LID = "G8_L08"
    LT = "Slope-Intercept Form y = mx + b"
    DOM = "Linear Relationships"
    STD = "8.EE.B.6 / 8.F.A.3"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In the linear equation y = 4x + 7, what is the y-intercept b?",
        7, ["7"],
        "In y = mx + b, b is the constant term: 7.",
        "7.",
        "7.",
        "b = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In the linear equation y = -3x + 10, what is the slope m?",
        -3, ["-3"],
        "In y = mx + b, m is the coefficient of x: -3.",
        "-3.",
        "-3.",
        "m = -3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "What does the y-intercept b represent on the graph of a line?",
        "The coordinates (0, b) where the line crosses the y-axis",
        ["The steepness of the line", "The point where the line crosses the x-axis", "The length of the line"],
        "The y-intercept is the output value when x = 0, where the line crosses the vertical axis.",
        "(0, b) on the y-axis.",
        "The coordinates (0, b) where the line crosses the y-axis.",
        "y-intercept is where line meets y-axis."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A line has equation y = 2x - 5. What is the value of y when x = 6?",
        7, ["7"],
        "y = 2(6) - 5 = 12 - 5 = 7.",
        "7.",
        "7.",
        "2(6) - 5 = 7."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Which equation represents a line with slope -1/2 and y-intercept 3?",
        "y = -1/2 x + 3",
        ["y = 3x - 1/2", "y = -2x + 3", "y = 1/2 x - 3"],
        "Substitute m = -1/2 and b = 3 into y = mx + b.",
        "y = -1/2 x + 3.",
        "y = -1/2 x + 3.",
        "y = -1/2 x + 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the y-intercept b of a line that has slope 3 and passes through the point (2, 11).",
        5, ["5"],
        "11 = 3(2) + b -> 11 = 6 + b -> b = 5.",
        "5.",
        "5.",
        "11 - 6 = 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A line passes through points (0, 4) and (2, 10). What is its equation in slope-intercept form?",
        "y = 3x + 4",
        ["y = 4x + 3", "y = 2x + 4", "y = 3x + 10"],
        "b = 4 (from (0, 4)). Slope m = (10 - 4)/(2 - 0) = 6/2 = 3. Equation: y = 3x + 4.",
        "y = 3x + 4.",
        "y = 3x + 4.",
        "m = 3, b = 4 -> y = 3x + 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A gym membership costs a $25 sign-up fee plus $15 per month (y = 15x + 25). What is the total cost for 6 months in dollars?",
        115, ["115", "$115"],
        "y = 15(6) + 25 = 90 + 25 = $115.",
        "$115.",
        "115.",
        "15 × 6 + 25 = $115."
    ))

    # =========================================================================
    # LESSON 9: Interpreting Linear Models (8.F.B.4)
    # =========================================================================
    LID = "G8_L09"
    LT = "Interpreting Linear Models"
    DOM = "Linear Relationships & Constructing"
    STD = "8.F.B.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In the taxi fare model C = 3.50m + 5.00, where m is miles traveled, what does the constant 5.00 represent?",
        "The initial base fee charged before driving any miles",
        ["The cost per mile driven", "The total distance of the trip", "The driver's hourly wage"],
        "The constant term represents the starting value (y-intercept) when m = 0.",
        "Base fee.",
        "The initial base fee charged before driving any miles.",
        "Base fee at 0 miles."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In the water tank model W = 200 - 15d (gallons remaining after d days), how many gallons of water are lost each day?",
        15, ["15", "15 gallons"],
        "The rate of change is -15 gallons per day, meaning 15 gallons are lost daily.",
        "15 gallons.",
        "15.",
        "15 gallons per day."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A candle is 12 inches tall and burns at 1.5 inches per hour: h = 12 - 1.5t. How many hours until the candle burns down completely (h = 0)?",
        8, ["8", "8 hours"],
        "0 = 12 - 1.5t -> 1.5t = 12 -> t = 12 ÷ 1.5 = 8 hours.",
        "8 hours.",
        "8.",
        "12 ÷ 1.5 = 8 hours."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In a savings model S = 50w + 100, where w is weeks, what does the slope 50 represent?",
        "The amount saved each week",
        ["The initial amount deposited", "The total number of weeks", "The interest rate"],
        "The slope 50 represents the rate of change: $50 added per week.",
        "Amount saved each week.",
        "The amount saved each week.",
        "Weekly savings rate."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A plumber charges C = 45h + 60. How much does a 4-hour service call cost in dollars?",
        240, ["240", "$240"],
        "C = 45(4) + 60 = 180 + 60 = $240.",
        "$240.",
        "240.",
        "45 × 4 + 60 = $240."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A tank has 500 liters of fuel and drains at 25 liters per minute. After how many minutes will 100 liters remain?",
        16, ["16", "16 minutes"],
        "500 - 25m = 100 -> 25m = 400 -> m = 400 ÷ 25 = 16 minutes.",
        "16 minutes.",
        "16.",
        "(500 - 100) ÷ 25 = 16."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "If the rate of change is zero in a linear model y = mx + b, what does the graph look like?",
        "A horizontal flat line",
        ["A vertical line", "A line increasing at 45 degrees", "A parabolic curve"],
        "When slope m = 0, y = b for all x, which graphs as a horizontal line.",
        "Horizontal line.",
        "A horizontal flat line.",
        "Slope of zero is horizontal."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A truck rental costs $20 base fee plus $0.50 per mile. If John paid $65 total, how many miles did he drive?",
        90, ["90", "90 miles"],
        "20 + 0.50m = 65 -> 0.50m = 45 -> m = 45 ÷ 0.50 = 90 miles.",
        "90 miles.",
        "90.",
        "45 ÷ 0.50 = 90 miles."
    ))

    # =========================================================================
    # LESSON 10: Solving Linear Equations in One Variable (8.EE.C.7)
    # =========================================================================
    LID = "G8_L10"
    LT = "Solving Linear Equations in One Variable"
    DOM = "Linear Equations & Linear Systems"
    STD = "8.EE.C.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve for x: 3x + 7 = 22.",
        5, ["5"],
        "Subtract 7: 3x = 15. Divide by 3: x = 5.",
        "5.",
        "5.",
        "3x = 15 -> x = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve for x: 5x - 8 = 2x + 13.",
        7, ["7"],
        "Subtract 2x: 3x - 8 = 13. Add 8: 3x = 21. Divide by 3: x = 7.",
        "7.",
        "7.",
        "3x = 21 -> x = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve for x: 2(3x - 4) = 28.",
        6, ["6"],
        "Expand: 6x - 8 = 28. Add 8: 6x = 36. Divide by 6: x = 6.",
        "6.",
        "6.",
        "6x = 36 -> x = 6."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "How many solutions does the equation 4x + 6 = 4x + 6 have?",
        "Infinitely many solutions",
        ["Exactly one solution", "No solution", "Exactly two solutions"],
        "Both sides are identical for all real values of x, so there are infinitely many solutions.",
        "Infinitely many solutions.",
        "Infinitely many solutions.",
        "Identity equation has infinitely many solutions."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "How many solutions does the equation 2x + 5 = 2x + 9 have?",
        "No solution",
        ["One solution", "Infinitely many solutions", "x = 0"],
        "Subtracting 2x gives 5 = 9, which is impossible (contradiction).",
        "No solution.",
        "No solution.",
        "5 = 9 has no solution."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve for x: 4(x + 2) - 3 = 2(x + 7) + 1.",
        5, ["5"],
        "Left: 4x + 8 - 3 = 4x + 5. Right: 2x + 14 + 1 = 2x + 15. 4x + 5 = 2x + 15 -> 2x = 10 -> x = 5.",
        "5.",
        "5.",
        "2x = 10 -> x = 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which of the following equations has NO solution?",
        "3x + 4 = 3x - 2",
        ["3x + 4 = 2x + 4", "3x + 4 = 3x + 4", "3x = 12"],
        "3x + 4 = 3x - 2 simplifies to 4 = -2, which is false.",
        "3x + 4 = 3x - 2.",
        "3x + 4 = 3x - 2.",
        "4 = -2 has no solution."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve for x: (x / 3) + 5 = 9.",
        12, ["12"],
        "x / 3 = 9 - 5 = 4 -> x = 4 × 3 = 12.",
        "12.",
        "12.",
        "x = 4 × 3 = 12."
    ))

    # =========================================================================
    # LESSON 11: Systems of Equations: Graphing (8.EE.C.8a / 8.EE.C.8c)
    # =========================================================================
    LID = "G8_L11"
    LT = "Systems of Equations: Graphing"
    DOM = "Linear Equations & Linear Systems"
    STD = "8.EE.C.8a / 8.EE.C.8c"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "On a graph, the solution to a system of two linear equations is represented by:",
        "The point of intersection of the two lines",
        ["The x-intercept of the first line", "The y-intercept of the second line", "The midpoint of both lines"],
        "The point where both lines intersect satisfies both equations simultaneously.",
        "Intersection point.",
        "The point of intersection of the two lines.",
        "Intersection point solves both equations."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "If two lines on a graph are parallel and never intersect, how many solutions does the system have?",
        "No solution",
        ["Exactly one solution", "Infinitely many solutions", "Two solutions"],
        "Parallel lines have no common points, so there is no solution.",
        "No solution.",
        "No solution.",
        "Parallel lines have no solution."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "If two equations represent the exact same line, how many solutions does the system have?",
        "Infinitely many solutions",
        ["No solution", "Exactly one solution", "Four solutions"],
        "Every point on the coincident line is a solution.",
        "Infinitely many solutions.",
        "Infinitely many solutions.",
        "Coincident lines have infinitely many solutions."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "The lines y = 2x + 1 and y = -x + 7 intersect at a point. What is the x-coordinate of the intersection?",
        2, ["2"],
        "2x + 1 = -x + 7 -> 3x = 6 -> x = 2.",
        "2.",
        "2.",
        "3x = 6 -> x = 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "For the system in Q04 (y = 2x + 1 and y = -x + 7 at x = 2), what is the y-coordinate of the intersection?",
        5, ["5"],
        "Substitute x = 2: y = 2(2) + 1 = 5.",
        "5.",
        "5.",
        "2(2) + 1 = 5."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Does the ordered pair (3, 4) satisfy both equations: y = x + 1 and y = 2x - 2?",
        "Yes, because 4 = 3 + 1 and 4 = 2(3) - 2",
        ["No, it only satisfies y = x + 1", "No, it only satisfies y = 2x - 2", "No, it satisfies neither"],
        "Testing (3, 4): 4 = 3 + 1 (true) and 4 = 6 - 2 = 4 (true).",
        "Yes, it satisfies both.",
        "Yes, because 4 = 3 + 1 and 4 = 2(3) - 2.",
        "(3, 4) satisfies both equations."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "The lines y = x + 4 and y = 3x intersect. What is the x-coordinate of the intersection?",
        2, ["2"],
        "3x = x + 4 -> 2x = 4 -> x = 2.",
        "2.",
        "2.",
        "2x = 4 -> x = 2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "For lines y = 4x - 5 and y = 2x + 3, what is the value of y at their intersection?",
        11, ["11"],
        "4x - 5 = 2x + 3 -> 2x = 8 -> x = 4. Then y = 4(4) - 5 = 16 - 5 = 11.",
        "11.",
        "11.",
        "x = 4 -> y = 11."
    ))

    # =========================================================================
    # LESSON 12: Systems of Equations: Substitution & Elimination (8.EE.C.8b / 8.EE.C.8c)
    # =========================================================================
    LID = "G8_L12"
    LT = "Systems of Equations: Substitution & Elimination"
    DOM = "Linear Equations & Linear Systems"
    STD = "8.EE.C.8b / 8.EE.C.8c"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Solve using substitution: y = 2x and x + y = 12. What is the value of x?",
        4, ["4"],
        "Substitute y = 2x into x + y = 12: x + 2x = 12 -> 3x = 12 -> x = 4.",
        "4.",
        "4.",
        "3x = 12 -> x = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In Q01, where x = 4 and y = 2x, what is the value of y?",
        8, ["8"],
        "y = 2(4) = 8.",
        "8.",
        "8.",
        "y = 2 × 4 = 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve by elimination: x + y = 10 and x - y = 4. What is the value of x?",
        7, ["7"],
        "Add equations: 2x = 14 -> x = 7.",
        "7.",
        "7.",
        "2x = 14 -> x = 7."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In Q03, where x = 7 and x + y = 10, what is the value of y?",
        3, ["3"],
        "y = 10 - 7 = 3.",
        "3.",
        "3.",
        "10 - 7 = 3."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Solve the system: 2x + y = 13 and y = x + 1. What is the value of x?",
        4, ["4"],
        "2x + (x + 1) = 13 -> 3x + 1 = 13 -> 3x = 12 -> x = 4.",
        "4.",
        "4.",
        "3x = 12 -> x = 4."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A theater sells adult tickets for $10 and child tickets for $6. A family buys 8 tickets for $64. How many adult tickets were bought?",
        4, ["4"],
        "Let a = adult, c = child. a + c = 8, 10a + 6c = 64. 10a + 6(8 - a) = 64 -> 4a + 48 = 64 -> 4a = 16 -> a = 4.",
        "4.",
        "4.",
        "4 adult tickets."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In Q06, how many child tickets were bought?",
        4, ["4"],
        "Child tickets c = 8 - 4 = 4.",
        "4.",
        "4.",
        "8 - 4 = 4 child tickets."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Solve by elimination: 3x + 2y = 16 and 3x - 2y = 8. What is the value of x?",
        4, ["4"],
        "Add the two equations: 6x = 24 -> x = 4.",
        "4.",
        "4.",
        "6x = 24 -> x = 4."
    ))

    # =========================================================================
    # LESSON 13: Understanding Functions (8.F.A.1 / 8.F.A.2 / 8.F.A.3)
    # =========================================================================
    LID = "G8_L13"
    LT = "Understanding Functions"
    DOM = "Functions & Volume"
    STD = "8.F.A.1 / 8.F.A.2 / 8.F.A.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A relation is a function if and only if:",
        "Each input value has exactly one output value",
        ["All outputs are distinct numbers", "The graph is always a vertical line", "Every output has two inputs"],
        "A function assigns exactly one output to each input in its domain.",
        "Each input has one output.",
        "Each input value has exactly one output value.",
        "Function definition: one output per input."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Which of the following sets of ordered pairs represents a function?",
        "{(1, 2), (2, 4), (3, 6), (4, 8)}",
        ["{(1, 2), (1, 3), (2, 4), (3, 5)}", "{(2, 5), (2, 7), (2, 9), (2, 11)}", "{(3, 1), (3, 2), (4, 5), (4, 6)}"],
        "In {(1, 2), (2, 4), (3, 6), (4, 8)}, every x-value is unique.",
        "{(1, 2), (2, 4), (3, 6), (4, 8)}.",
        "{(1, 2), (2, 4), (3, 6), (4, 8)}.",
        "Every input maps to a unique output."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Does the relation {(2, 5), (3, 7), (2, 9)} represent a function?",
        "No, because the input 2 has two different outputs (5 and 9)",
        ["Yes, because all outputs are odd numbers", "Yes, because it has three pairs", "Cannot be determined"],
        "An input value cannot map to multiple distinct outputs in a function.",
        "No, input 2 repeats with different outputs.",
        "No, because the input 2 has two different outputs (5 and 9).",
        "Input 2 has two outputs: not a function."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following equations represents a NON-linear function?",
        "y = x² + 3",
        ["y = 2x - 5", "y = -4x + 1", "y = x / 2"],
        "Linear functions have exponent 1 for x; x² is quadratic (non-linear).",
        "y = x² + 3.",
        "y = x² + 3.",
        "x² is non-linear."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "For the function f(x) = 3x - 4, what is the output value when input x = 5?",
        11, ["11"],
        "f(5) = 3(5) - 4 = 15 - 4 = 11.",
        "11.",
        "11.",
        "3(5) - 4 = 11."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Function A has rate of change 4 (y = 4x + 1). Function B passes through (0, 2) and (2, 12) (slope = 5). What is the difference between their rates of change?",
        1, ["1"],
        "Slope of B = (12 - 2) ÷ (2 - 0) = 10 ÷ 2 = 5. Difference = 5 - 4 = 1.",
        "1.",
        "1.",
        "5 - 4 = 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Can a vertical line on a coordinate grid represent a function?",
        "No, because it fails the vertical line test by having infinitely many outputs for a single input",
        ["Yes, because it is straight", "Yes, if it crosses the x-axis", "Only if it passes through the origin"],
        "A vertical line has one x-value mapped to multiple y-values, violating the function rule.",
        "No, fails vertical line test.",
        "No, because it fails the vertical line test by having infinitely many outputs for a single input.",
        "Vertical line is not a function."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "For the linear function y = -2x + 15, what is the input x that gives an output y = 7?",
        4, ["4"],
        "7 = -2x + 15 -> 2x = 8 -> x = 4.",
        "4.",
        "4.",
        "2x = 8 -> x = 4."
    ))

    # =========================================================================
    # LESSON 14: Qualitative Graphs & Functional Relationships (8.F.B.5)
    # =========================================================================
    LID = "G8_L14"
    LT = "Qualitative Graphs & Functional Relationships"
    DOM = "Functions & Volume"
    STD = "8.F.B.5"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A car accelerates from a stop, drives at a constant speed, then slows down to a stop at a red light. What does its speed-time graph look like?",
        "A line rising from zero, a flat horizontal section, and a line falling back to zero",
        ["A straight line going constantly upward", "A circle", "A line going down then staying at zero"],
        "Accelerating means increasing speed, constant speed means horizontal flat line, slowing means decreasing speed.",
        "Rises, stays flat, then falls.",
        "A line rising from zero, a flat horizontal section, and a line falling back to zero.",
        "Qualitative graph shows rise, plateau, fall."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "If a distance-time graph has a horizontal flat section, what is the object doing during that time interval?",
        "Remaining stationary (stopped)",
        ["Moving at maximum speed", "Accelerating rapidly", "Moving backwards"],
        "A horizontal distance-time graph means distance does not change over time, so the object is stopped.",
        "Stationary (stopped).",
        "Remaining stationary (stopped).",
        "Flat line on distance-time means stationary."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Water is poured into a cylindrical container at a constant flow rate. What does the graph of water height versus time look like?",
        "A straight line increasing at a constant rate",
        ["A curve getting steeper", "A curve flattening out", "A horizontal line"],
        "Because the cylinder has uniform width, water height increases at a constant linear rate.",
        "Straight line increasing constantly.",
        "A straight line increasing at a constant rate.",
        "Uniform container gives constant linear growth."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A roller coaster climbs slowly up a hill, then plunges rapidly down. How does the graph of speed versus time describe the plunge?",
        "A steep upward line showing rapid acceleration",
        ["A flat line", "A line going down to zero", "A horizontal wave"],
        "Going down the steep drop causes speed to increase dramatically (steep positive slope).",
        "Steep upward line.",
        "A steep upward line showing rapid acceleration.",
        "Plunge causes speed to increase steeply."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A runner runs 3 miles in 30 minutes, rests for 10 minutes, and walks 1 mile in 20 minutes. What was the total duration of the trip in minutes?",
        60, ["60", "60 minutes"],
        "Total time = 30 + 10 + 20 = 60 minutes.",
        "60 minutes.",
        "60.",
        "30 + 10 + 20 = 60 min."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A vase shaped like a sphere (widest at the middle) is filled with water at a steady rate. How does the rate of height increase behave?",
        "Increases quickly at first, slows down through the middle, then speeds up near the top",
        ["Increases at a steady constant rate throughout", "Decreases steadily throughout", "Stays at zero"],
        "As the cross-sectional area widens in the middle, height rises more slowly.",
        "Fast, slows in middle, fast near top.",
        "Increases quickly at first, slows down through the middle, then speeds up near the top.",
        "Cross-section affects fill rate."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which section of a distance-from-home versus time graph indicates that a traveler is returning towards home?",
        "A section where the line has a negative slope (slopes downward)",
        ["A section where the slope is positive", "A horizontal section", "The highest peak"],
        "Decreasing distance from home creates a downward slope.",
        "Negative downward slope.",
        "A section where the line has a negative slope (slopes downward).",
        "Negative slope means returning home."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A cyclist rides at 12 mph for 2 hours, rests for 1 hour, then rides at 10 mph for 1 hour. What is the total distance traveled in miles?",
        34, ["34", "34 miles"],
        "Leg 1: 12 × 2 = 24 miles. Rest: 0 miles. Leg 2: 10 × 1 = 10 miles. Total = 24 + 10 = 34 miles.",
        "34 miles.",
        "34.",
        "24 + 10 = 34 miles."
    ))

    # =========================================================================
    # LESSON 15: Volume of Cylinders, Cones & Spheres (8.G.C.9)
    # =========================================================================
    LID = "G8_L15"
    LT = "Volume of Cylinders, Cones & Spheres"
    DOM = "Functions & Volume"
    STD = "8.G.C.9"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the volume of a cylinder with radius 3 cm and height 10 cm in terms of π. Enter the coefficient of π. (V = π × r² × h)",
        90, ["90"],
        "V = π × 3² × 10 = π × 9 × 10 = 90π. Coefficient is 90.",
        "90.",
        "90.",
        "3² × 10 = 90."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "How does the volume of a cone compare to the volume of a cylinder with the same base radius and height?",
        "The cone has exactly 1/3 the volume of the cylinder",
        ["The cone has 1/2 the volume", "The cone has equal volume", "The cone has 2/3 the volume"],
        "Volume of cone = 1/3 π r² h, which is exactly one-third the cylinder volume π r² h.",
        "1/3 the volume.",
        "The cone has exactly 1/3 the volume of the cylinder.",
        "Cone volume is 1/3 of cylinder."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the volume of a cone with radius 6 cm and height 7 cm in terms of π. Enter the coefficient of π. (V = 1/3 × π × r² × h)",
        84, ["84"],
        "V = (1/3) × π × 6² × 7 = (1/3) × π × 36 × 7 = 12 × 7 × π = 84π.",
        "84.",
        "84.",
        "1/3 × 36 × 7 = 84."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Find the volume of a sphere with radius 3 cm in terms of π. Enter the coefficient of π. (V = 4/3 × π × r³)",
        36, ["36"],
        "V = (4/3) × π × 3³ = (4/3) × π × 27 = 4 × 9 × π = 36π.",
        "36.",
        "36.",
        "4/3 × 27 = 36."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A cylinder has diameter 8 meters (radius 4 m) and height 5 meters. What is its volume in cubic meters using π ≈ 3.14?",
        251.2, ["251.2", "251.2 cu m"],
        "V = 3.14 × 4² × 5 = 3.14 × 16 × 5 = 3.14 × 80 = 251.2 cubic meters.",
        "251.2 cubic meters.",
        "251.2.",
        "3.14 × 16 × 5 = 251.2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A cone has volume 48π cubic inches and height 9 inches. What is the value of its radius squared (r²)? (48π = 1/3 × π × r² × 9)",
        16, ["16"],
        "48π = 3π × r² -> r² = 48 ÷ 3 = 16.",
        "16.",
        "16.",
        "48 ÷ 3 = 16."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "A sphere has radius 6 cm. What is its volume in terms of π? Enter the coefficient of π. (V = 4/3 × π × r³)",
        288, ["288"],
        "V = (4/3) × π × 6³ = (4/3) × π × 216 = 4 × 72 × π = 288π.",
        "288.",
        "288.",
        "4/3 × 216 = 288."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If the radius of a cylinder is doubled while its height remains the same, by what factor does its volume increase?",
        "Factor of 4",
        ["Factor of 2", "Factor of 8", "Factor of 6"],
        "Volume is proportional to r²: (2r)² = 4r², so volume multiplies by 4.",
        "Factor of 4.",
        "Factor of 4.",
        "Radius squared quadruples volume."
    ))

    # =========================================================================
    # LESSON 16: Patterns of Association in Scatter Plots (8.SP.A.1)
    # =========================================================================
    LID = "G8_L16"
    LT = "Patterns of Association in Scatter Plots"
    DOM = "Associations in Data & Scatter Plots"
    STD = "8.SP.A.1"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "When data points on a scatter plot generally trend upward from left to right, this indicates:",
        "A positive association",
        ["A negative association", "No association", "A constant horizontal relationship"],
        "As x increases, y tends to increase, showing a positive association.",
        "Positive association.",
        "A positive association.",
        "Upward trend indicates positive association."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "If higher values of variable x correspond to lower values of variable y, this indicates:",
        "A negative association",
        ["A positive association", "No association", "A non-linear cluster"],
        "As x increases, y decreases, creating a downward trend (negative association).",
        "Negative association.",
        "A negative association.",
        "Downward trend is negative association."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A scatter plot compares students' shoe sizes to their scores on a math test. What type of association would you expect?",
        "No association",
        ["Strong positive linear association", "Strong negative linear association", "Quadratic association"],
        "Shoe size has no meaningful mathematical relationship to math performance.",
        "No association.",
        "No association.",
        "Shoe size and test score are unrelated."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "A data point that lies unusually far away from the overall pattern formed by the rest of the data is called:",
        "An outlier",
        ["A cluster", "A line of best fit", "The origin"],
        "An outlier is an observation distinctly separated from the main body of data.",
        "An outlier.",
        "An outlier.",
        "Distant point is an outlier."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "When points on a scatter plot follow a curved path rather than a straight line, the relationship is classified as:",
        "Non-linear association",
        ["Positive linear association", "Negative linear association", "Zero association"],
        "Curved patterns represent non-linear relationships.",
        "Non-linear association.",
        "Non-linear association.",
        "Curved data indicates non-linear association."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "In a study of study hours versus test scores, all students who studied 0 hours scored between 40-55, except one student who scored 98. That point is:",
        "An outlier",
        ["A cluster", "A negative trend", "A data error that invalidates the study"],
        "It deviates significantly from the typical trend of the group.",
        "An outlier.",
        "An outlier.",
        "Isolated high score is an outlier."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which pair of real-world variables would most likely show a negative linear association?",
        "Outdoor temperature and home heating bill costs",
        ["Height and weight of growing children", "Hours spent studying and exam grade", "Number of siblings and test scores"],
        "As outdoor temperature increases, home heating expenses decrease.",
        "Outdoor temperature and heating costs.",
        "Outdoor temperature and home heating bill costs.",
        "Warmer weather reduces heating costs."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "In a scatter plot of 25 data points, 23 points cluster closely along a line, while 2 points lie far away from the cluster. How many outliers are there?",
        2, ["2"],
        "The 2 points separated from the primary cluster are outliers.",
        "2.",
        "2.",
        "2 outliers."
    ))

    # =========================================================================
    # LESSON 17: Predictions & Lines of Best Fit (8.SP.A.2 / 8.SP.A.3)
    # =========================================================================
    LID = "G8_L17"
    LT = "Predictions & Lines of Best Fit"
    DOM = "Associations in Data & Lines of Best Fit"
    STD = "8.SP.A.2 / 8.SP.A.3"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A line of best fit (trend line) on a scatter plot should:",
        "Pass as close as possible to all data points, balancing points above and below the line",
        ["Connect every single data point like a dot-to-dot", "Always pass through (0, 0)", "Pass only through the lowest and highest points"],
        "A trend line models the overall central trend of bivariate data.",
        "Balances points above and below.",
        "Pass as close as possible to all data points, balancing points above and below the line.",
        "Best fit line minimizes overall distance to points."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "A line of best fit for test scores is y = 8x + 40, where x is hours studied. Predict the score for a student who studies 5 hours.",
        80, ["80"],
        "y = 8(5) + 40 = 40 + 40 = 80.",
        "80.",
        "80.",
        "8(5) + 40 = 80."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A trend line for plant growth is y = 0.5x + 3 (height in inches after x days). What is the predicted height after 14 days in inches?",
        10, ["10", "10 inches"],
        "y = 0.5(14) + 3 = 7 + 3 = 10 inches.",
        "10 inches.",
        "10.",
        "0.5(14) + 3 = 10."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "In the linear model y = 2.5x + 10, where y is total cost for x carnival rides, what does the slope 2.5 represent?",
        "The cost per ride",
        ["The entry admission fee", "The total number of rides", "The maximum budget"],
        "The slope represents the rate of change ($2.50 per ride).",
        "Cost per ride.",
        "The cost per ride.",
        "Slope indicates cost per ride."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A laptop battery discharge is modeled by y = -3x + 90 (battery percentage after x hours). How many hours until the battery reaches 0%?",
        30, ["30", "30 hours"],
        "0 = -3x + 90 -> 3x = 90 -> x = 30 hours.",
        "30 hours.",
        "30.",
        "90 ÷ 3 = 30."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "A trend line is y = 1.2x + 15. If a student scored 75, how many hours x did the student study?",
        50, ["50"],
        "75 = 1.2x + 15 -> 1.2x = 60 -> x = 60 ÷ 1.2 = 50.",
        "50.",
        "50.",
        "60 ÷ 1.2 = 50."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Using a line of best fit to predict values far outside the observed range of data is called:",
        "Extrapolation (which is less reliable than interpolation)",
        ["Interpolation", "Correlation", "Transformation"],
        "Extrapolation predicts beyond measured data, carrying greater uncertainty.",
        "Extrapolation.",
        "Extrapolation (which is less reliable than interpolation).",
        "Predicting outside data range is extrapolation."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "The line of best fit is y = 15x + 50. What is the predicted value of y when x = 8?",
        170, ["170"],
        "y = 15(8) + 50 = 120 + 50 = 170.",
        "170.",
        "170.",
        "15 × 8 + 50 = 170."
    ))

    # =========================================================================
    # LESSON 18: Two-Way Frequency Tables (8.SP.A.4)
    # =========================================================================
    LID = "G8_L18"
    LT = "Two-Way Frequency Tables"
    DOM = "Associations in Data"
    STD = "8.SP.A.4"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A survey of 100 students asks about sports. 45 boys play sports and 25 girls play sports. How many total students play sports?",
        70, ["70"],
        "Total students playing sports = 45 + 25 = 70.",
        "70.",
        "70.",
        "45 + 25 = 70."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In the survey from Q01 (100 students total, 70 play sports), how many students do NOT play sports?",
        30, ["30"],
        "100 - 70 = 30 students.",
        "30.",
        "30.",
        "100 - 70 = 30."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "In a group of 80 people, 48 own a dog. What percentage of the group owns a dog?",
        60, ["60", "60%"],
        "Relative frequency = 48 ÷ 80 = 0.60 = 60%.",
        "60%.",
        "60.",
        "48/80 = 60%."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "How is a relative frequency calculated in a two-way table?",
        "Divide the cell frequency by the row total, column total, or grand total",
        ["Multiply all numbers in the row", "Subtract the smallest count from the largest", "Take the square root of the cell count"],
        "Relative frequency is the fraction or percentage of the total represented by a count.",
        "Divide frequency by total.",
        "Divide the cell frequency by the row total, column total, or grand total.",
        "Ratio of count to total."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Out of 50 boys surveyed, 35 prefer action movies. What percentage of boys prefer action movies?",
        70, ["70", "70%"],
        "Conditional relative frequency = 35 ÷ 50 = 70%.",
        "70%.",
        "70.",
        "35/50 = 70%."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "What type of data does a two-way table display?",
        "Bivariate categorical data (two categorical variables)",
        ["Continuous numerical data", "Only 3-dimensional data", "Time series coordinates"],
        "Two-way tables summarize relationships between two categorical variables.",
        "Bivariate categorical data.",
        "Bivariate categorical data (two categorical variables).",
        "Categorical bivariate data."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "In a school survey, the 7th-grade row total is 40 and the 8th-grade row total is 60. What is the grand total of students surveyed?",
        100, ["100"],
        "Grand total = 40 + 60 = 100 students.",
        "100.",
        "100.",
        "40 + 60 = 100."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "If 80% of students who play an instrument also participate in drama, compared to only 20% of non-musicians, this indicates:",
        "An association between playing an instrument and participating in drama",
        ["No association", "That drama causes students to play instruments", "That the data is invalid"],
        "A substantial difference in conditional relative frequencies indicates an association between the two variables.",
        "Evidence of an association.",
        "An association between playing an instrument and participating in drama.",
        "Difference in relative frequencies shows association."
    ))

    # =========================================================================
    # LESSON 19: Properties of Integer Exponents (8.EE.A.1)
    # =========================================================================
    LID = "G8_L19"
    LT = "Properties of Integer Exponents"
    DOM = "Exponents & Scientific Notation"
    STD = "8.EE.A.1"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Evaluate: 2³ × 2⁴. (Product of powers rule: 2^(3+4) = 2⁷).",
        128, ["128"],
        "2⁷ = 128.",
        "128.",
        "128.",
        "2⁷ = 128."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Simplify the power of a power: (x⁵)³.",
        "x¹⁵",
        ["x⁸", "x²", "3x⁵"],
        "Power of a power rule: multiply exponents (5 × 3 = 15): x¹⁵.",
        "x¹⁵.",
        "x¹⁵.",
        "(x⁵)³ = x¹⁵."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Evaluate: 5⁰. Any non-zero base raised to power 0 equals:",
        1, ["1"],
        "Any non-zero number raised to the zero power equals 1.",
        "1.",
        "1.",
        "5⁰ = 1."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which expression is equivalent to 3⁻⁴?",
        "1 / 3⁴ (or 1/81)",
        ["-3⁴", "-12", "3 / 4"],
        "Negative exponent rule: a⁻ⁿ = 1 / aⁿ. Thus 3⁻⁴ = 1 / 3⁴ = 1/81.",
        "1 / 3⁴.",
        "1 / 3⁴ (or 1/81).",
        "Negative exponent moves base to denominator."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Simplify and evaluate: 4⁶ ÷ 4⁴.",
        16, ["16"],
        "Quotient rule: 4^(6 - 4) = 4² = 16.",
        "16.",
        "16.",
        "4² = 16."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate: (2⁻³)⁻².",
        64, ["64"],
        "Multiply exponents: (-3) × (-2) = 6. 2⁶ = 64.",
        "64.",
        "64.",
        "2⁶ = 64."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Simplify: (2a³b⁴)³.",
        "8a⁹b¹²",
        ["6a⁹b¹²", "8a⁶b⁷", "2a⁹b¹²"],
        "Apply power to each factor: 2³ × a^(3×3) × b^(4×3) = 8a⁹b¹².",
        "8a⁹b¹².",
        "8a⁹b¹².",
        "2³ a⁹ b¹² = 8a⁹b¹²."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Evaluate: (3⁴ × 3⁻²) ÷ 3¹.",
        3, ["3"],
        "Add and subtract exponents: 3^(4 + (-2) - 1) = 3¹ = 3.",
        "3.",
        "3.",
        "3¹ = 3."
    ))

    # =========================================================================
    # LESSON 20: Scientific Notation & Orders of Magnitude (8.EE.A.3 / 8.EE.A.4)
    # =========================================================================
    LID = "G8_L20"
    LT = "Scientific Notation & Orders of Magnitude"
    DOM = "Exponents & Scientific Notation"
    STD = "8.EE.A.3 / 8.EE.A.4"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Write 450,000 in scientific notation.",
        "4.5 × 10⁵",
        ["45 × 10⁴", "4.5 × 10⁶", "0.45 × 10⁶"],
        "Move decimal point 5 places left to obtain a coefficient between 1 and 10: 4.5 × 10⁵.",
        "4.5 × 10⁵.",
        "4.5 × 10⁵.",
        "4.5 × 10⁵."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Write 0.00032 in scientific notation.",
        "3.2 × 10⁻⁴",
        ["3.2 × 10⁴", "32 × 10⁻⁵", "0.32 × 10⁻³"],
        "Move decimal 4 places right: 3.2 × 10⁻⁴.",
        "3.2 × 10⁻⁴.",
        "3.2 × 10⁻⁴.",
        "3.2 × 10⁻⁴."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "How many times larger is 6 × 10⁸ than 2 × 10⁵?",
        3000, ["3000"],
        "(6 × 10⁸) ÷ (2 × 10⁵) = (6/2) × 10^(8 - 5) = 3 × 10³ = 3000.",
        "3000.",
        "3000.",
        "3 × 10³ = 3000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Compute: (2 × 10⁴) × (3 × 10⁵).",
        "6 × 10⁹",
        ["6 × 10²⁰", "5 × 10⁹", "6 × 10⁴⁵"],
        "Multiply coefficients (2 × 3 = 6) and add exponents (4 + 5 = 9): 6 × 10⁹.",
        "6 × 10⁹.",
        "6 × 10⁹.",
        "(2×3) × 10^(4+5) = 6 × 10⁹."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "The distance to a star is 4 × 10¹³ meters. A space probe travels 2 × 10¹⁰ meters per year. How many years will it take to reach the star?",
        2000, ["2000", "2000 years"],
        "(4 × 10¹³) ÷ (2 × 10¹⁰) = 2 × 10³ = 2000 years.",
        "2000 years.",
        "2000.",
        "2 × 10³ = 2000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Compute: (8 × 10⁷) ÷ (4 × 10²).",
        "2 × 10⁵",
        ["2 × 10⁹", "4 × 10⁵", "2 × 10³"],
        "(8 ÷ 4) × 10^(7 - 2) = 2 × 10⁵.",
        "2 × 10⁵.",
        "2 × 10⁵.",
        "2 × 10⁵."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Add: (3 × 10⁴) + (5 × 10³).",
        "3.5 × 10⁴",
        ["8 × 10⁷", "8 × 10⁴", "15 × 10¹²"],
        "Convert to matching powers: 30,000 + 5,000 = 35,000 = 3.5 × 10⁴.",
        "3.5 × 10⁴.",
        "3.5 × 10⁴.",
        "30,000 + 5,000 = 3.5 × 10⁴."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Convert 7.8 × 10⁻³ to standard decimal form.",
        0.0078, ["0.0078"],
        "Move decimal 3 places left: 0.0078.",
        "0.0078.",
        "0.0078.",
        "0.0078."
    ))

    # =========================================================================
    # LESSON 21: Square & Cube Roots (8.EE.A.2)
    # =========================================================================
    LID = "G8_L21"
    LT = "Square & Cube Roots"
    DOM = "Pythagorean Theorem & Irrational Numbers"
    STD = "8.EE.A.2"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Evaluate the square root: √81.",
        9, ["9"],
        "9 × 9 = 81, so √81 = 9.",
        "9.",
        "9.",
        "√81 = 9."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Evaluate the cube root: ∛64 (the cube root of 64).",
        4, ["4"],
        "4 × 4 × 4 = 64, so ∛64 = 4.",
        "4.",
        "4.",
        "4³ = 64."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Solve for x (where x > 0): x² = 144.",
        12, ["12"],
        "x = √144 = 12.",
        "12.",
        "12.",
        "12² = 144."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Solve for y: y³ = 125.",
        5, ["5"],
        "y = ∛125 = 5.",
        "5.",
        "5.",
        "5³ = 125."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "Between which two consecutive whole numbers does √50 lie?",
        "Between 7 and 8",
        ["Between 6 and 7", "Between 8 and 9", "Between 24 and 26"],
        "7² = 49 and 8² = 64. Since 49 < 50 < 64, √50 lies between 7 and 8.",
        "Between 7 and 8.",
        "Between 7 and 8.",
        "7² = 49 < 50 < 64 = 8²."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Solve for x: x³ = 1000.",
        10, ["10"],
        "10 × 10 × 10 = 1000, so x = 10.",
        "10.",
        "10.",
        "10³ = 1000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Evaluate: √0.25.",
        "0.5",
        ["0.05", "5", "0.025"],
        "0.5 × 0.5 = 0.25, so √0.25 = 0.5.",
        "0.5.",
        "0.5.",
        "0.5² = 0.25."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "What is the area of a square garden whose side length is √49 meters in square meters?",
        49, ["49", "49 sq m"],
        "Area = (side)² = (√49)² = 49 square meters.",
        "49 sq m.",
        "49.",
        "(√49)² = 49."
    ))

    # =========================================================================
    # LESSON 22: The Pythagorean Theorem (8.G.B.7)
    # =========================================================================
    LID = "G8_L22"
    LT = "The Pythagorean Theorem"
    DOM = "Pythagorean Theorem & Irrational Numbers"
    STD = "8.G.B.7"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "In a right triangle, the legs are a = 3 and b = 4. What is the length of the hypotenuse c? (a² + b² = c²)",
        5, ["5"],
        "c² = 3² + 4² = 9 + 16 = 25 -> c = √25 = 5.",
        "5.",
        "5.",
        "√(9 + 16) = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "In a right triangle, legs are a = 6 and b = 8. What is the hypotenuse c?",
        10, ["10"],
        "c² = 6² + 8² = 36 + 64 = 100 -> c = √100 = 10.",
        "10.",
        "10.",
        "√(36 + 64) = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A right triangle has hypotenuse c = 13 and one leg a = 5. What is the length of leg b?",
        12, ["12"],
        "b² = 13² - 5² = 169 - 25 = 144 -> b = √144 = 12.",
        "12.",
        "12.",
        "√(169 - 25) = 12."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Do side lengths 9, 12, and 15 form a right triangle?",
        "Yes, because 9² + 12² = 81 + 144 = 225 = 15²",
        ["No, because 9 + 12 is greater than 15", "Only if the triangle is equilateral", "No, because 15 is odd"],
        "By the converse of the Pythagorean theorem, 9² + 12² = 15² proves it is a right triangle.",
        "Yes, 81 + 144 = 225.",
        "Yes, because 9² + 12² = 81 + 144 = 225 = 15².",
        "9² + 12² = 15²."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A 10-foot ladder leans against a vertical wall. The base is 6 feet from the wall. How high up the wall does the ladder reach in feet?",
        8, ["8", "8 ft", "8 feet"],
        "h² = 10² - 6² = 100 - 36 = 64 -> h = √64 = 8 feet.",
        "8 ft.",
        "8.",
        "√(100 - 36) = 8 ft."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "In a right triangle, legs are 8 and 15. What is the length of the hypotenuse?",
        17, ["17"],
        "c² = 8² + 15² = 64 + 225 = 289 -> c = √289 = 17.",
        "17.",
        "17.",
        "√(64 + 225) = 17."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Which set of side lengths does NOT form a right triangle?",
        "5, 10, 15",
        ["3, 4, 5", "5, 12, 13", "7, 24, 25"],
        "5² + 10² = 25 + 100 = 125 ≠ 15² (225).",
        "5, 10, 15.",
        "5, 10, 15.",
        "5² + 10² ≠ 15²."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "A TV screen has width 16 inches and height 12 inches. What is the diagonal screen size in inches?",
        20, ["20", "20 inches"],
        "d² = 16² + 12² = 256 + 144 = 400 -> d = √400 = 20 inches.",
        "20 inches.",
        "20.",
        "√(256 + 144) = 20."
    ))

    # =========================================================================
    # LESSON 23: Distance in the Coordinate Plane (8.G.B.8)
    # =========================================================================
    LID = "G8_L23"
    LT = "Distance in the Coordinate Plane"
    DOM = "Pythagorean Theorem & Irrational Numbers"
    STD = "8.G.B.8"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Find the distance between (0, 0) and (3, 4) in the coordinate plane.",
        5, ["5", "5 units"],
        "d = √(3² + 4²) = √(9 + 16) = √25 = 5 units.",
        "5 units.",
        "5.",
        "√(9 + 16) = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Find the distance between (1, 2) and (7, 10).",
        10, ["10", "10 units"],
        "dx = 7 - 1 = 6; dy = 10 - 2 = 8. d = √(6² + 8²) = √(36 + 64) = √100 = 10 units.",
        "10 units.",
        "10.",
        "√(36 + 64) = 10."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Find the distance between (-2, 3) and (3, 15).",
        13, ["13", "13 units"],
        "dx = 3 - (-2) = 5; dy = 15 - 3 = 12. d = √(5² + 12²) = √(25 + 144) = √169 = 13 units.",
        "13 units.",
        "13.",
        "√(25 + 144) = 13."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "The coordinate distance formula d = √((x2 - x1)² + (y2 - y1)²) is a direct application of which theorem?",
        "The Pythagorean Theorem",
        ["The Fundamental Theorem of Algebra", "The Quadratic Formula", "Euler's Formula"],
        "The horizontal and vertical differences form the legs of a right triangle whose hypotenuse is the distance.",
        "Pythagorean Theorem.",
        "The Pythagorean Theorem.",
        "Distance formula comes from Pythagorean Theorem."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What is the length of the line segment connecting (2, 5) and (6, 8)?",
        5, ["5", "5 units"],
        "dx = 6 - 2 = 4; dy = 8 - 5 = 3. d = √(4² + 3²) = √25 = 5 units.",
        "5 units.",
        "5.",
        "√(16 + 9) = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Find the distance between (-4, -1) and (4, 14).",
        17, ["17", "17 units"],
        "dx = 4 - (-4) = 8; dy = 14 - (-1) = 15. d = √(8² + 15²) = √(64 + 225) = √289 = 17 units.",
        "17 units.",
        "17.",
        "√(64 + 225) = 17."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "What is the horizontal distance between (-3, 4) and (5, 4)?",
        8, ["8", "8 units"],
        "Same y-coordinate: distance = |5 - (-3)| = 8 units.",
        "8 units.",
        "8.",
        "|5 - (-3)| = 8."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Find the perimeter of a right triangle with vertices at (0, 0), (9, 0), and (0, 12).",
        36, ["36", "36 units"],
        "Leg 1 = 9; Leg 2 = 12. Hypotenuse = √(9² + 12²) = 15. Perimeter = 9 + 12 + 15 = 36 units.",
        "36 units.",
        "36.",
        "9 + 12 + 15 = 36."
    ))

    # =========================================================================
    # LESSON 24: Rational & Irrational Numbers (8.NS.A.1 / 8.NS.A.2)
    # =========================================================================
    LID = "G8_L24"
    LT = "Rational & Irrational Numbers"
    DOM = "Pythagorean Theorem & Irrational Numbers"
    STD = "8.NS.A.1 / 8.NS.A.2"

    questions.append(make_mc_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "Which of the following is an irrational number?",
        "√2",
        ["3/4", "0.25", "√16"],
        "√2 has a non-terminating, non-repeating decimal expansion and cannot be written as a fraction of integers.",
        "√2.",
        "√2.",
        "√2 is irrational."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Can the repeating decimal 0.333... be written as a fraction of two integers?",
        "Yes, it equals 1/3, which is a rational number",
        ["No, because it repeats infinitely", "No, all decimals are irrational", "Only if rounded to 0.33"],
        "Every repeating decimal can be written as a fraction a/b, so it is rational.",
        "Yes, equals 1/3 (rational).",
        "Yes, it equals 1/3, which is a rational number.",
        "0.333... = 1/3."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "Convert the repeating decimal 0.777... into a simplified fraction.",
        "7/9",
        ["7/10", "7/99", "3/4"],
        "Let x = 0.777... -> 10x = 7.777... -> 9x = 7 -> x = 7/9.",
        "7/9.",
        "7/9.",
        "0.777... = 7/9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which statement is true for ALL rational numbers?",
        "They can be expressed as a ratio of two integers a/b where b ≠ 0",
        ["They must be positive whole numbers", "Their decimal expansion never repeats", "They cannot be graphed on a number line"],
        "Definition of rational numbers is the quotient of two integers.",
        "Ratio of two integers a/b.",
        "They can be expressed as a ratio of two integers a/b where b ≠ 0.",
        "Rational = ratio of integers."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "What integer is √75 closest to?",
        9, ["9"],
        "8² = 64 and 9² = 81. 75 is closer to 81 (|81 - 75| = 6) than 64 (|75 - 64| = 11). Closest integer is 9.",
        "9.",
        "9.",
        "√75 is closest to 9."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Convert the repeating decimal 0.454545... into a simplified fraction.",
        "5/11",
        ["45/100", "9/20", "4/9"],
        "100x - x = 99x = 45 -> x = 45/99 = 5/11.",
        "5/11.",
        "5/11.",
        "45/99 = 5/11."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "Is √100 a rational or irrational number?",
        "Rational, because √100 = 10, which is an integer",
        ["Irrational, because it is under a square root", "Neither rational nor irrational", "Imaginary"],
        "100 is a perfect square: √100 = 10 = 10/1, which is rational.",
        "Rational (equals 10).",
        "Rational, because √100 = 10, which is an integer.",
        "√100 = 10 is rational."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Between which two consecutive whole numbers does √20 lie? Enter the smaller whole number.",
        4, ["4"],
        "4² = 16 and 5² = 25. Since 16 < 20 < 25, √20 lies between 4 and 5. Smaller whole number is 4.",
        "4.",
        "4.",
        "4² = 16 < 20 < 25 = 5²."
    ))

    # =========================================================================
    # LESSON 25: Cumulative Real-World Applications (8.MP.1--8.MP.8)
    # =========================================================================
    LID = "G8_L25"
    LT = "Cumulative Real-World Applications"
    DOM = "Capstone"
    STD = "8.MP.1--8.MP.8"

    questions.append(make_numeric_question(
        f"{LID}_Q01", G, LID, LT, DOM, STD, 1,
        "A cone-shaped paper cup has radius 3 cm and height 10 cm. Find its volume in cubic cm using π ≈ 3.14. (V = 1/3 × π × r² × h)",
        94.2, ["94.2", "94.2 cu cm"],
        "V = (1/3) × 3.14 × 3² × 10 = (1/3) × 3.14 × 9 × 10 = 3 × 3.14 × 10 = 94.2 cubic cm.",
        "94.2 cu cm.",
        "94.2.",
        "3 × 3.14 × 10 = 94.2."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q02", G, LID, LT, DOM, STD, 1,
        "Solve for x: 5(2x - 3) = 35.",
        5, ["5"],
        "2x - 3 = 35 ÷ 5 = 7 -> 2x = 10 -> x = 5.",
        "5.",
        "5.",
        "2x = 10 -> x = 5."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q03", G, LID, LT, DOM, STD, 2,
        "A park walking path goes 30 meters East, then 40 meters North. What is the straight-line distance back to the start in meters?",
        50, ["50", "50 m", "50 meters"],
        "d = √(30² + 40²) = √(900 + 1600) = √2500 = 50 meters.",
        "50 meters.",
        "50.",
        "√(900 + 1600) = 50 m."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q04", G, LID, LT, DOM, STD, 2,
        "Which of the following equations has NO solution?",
        "2x + 7 = 2x - 5",
        ["2x + 7 = 3x - 5", "2x + 7 = 2x + 7", "4x = 20"],
        "Subtracting 2x gives 7 = -5 (false statement, contradiction).",
        "2x + 7 = 2x - 5.",
        "2x + 7 = 2x - 5.",
        "7 = -5 has no solution."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q05", G, LID, LT, DOM, STD, 2,
        "A mobile phone plan charges $30 per month plus $0.10 per text message. If the monthly bill is $42, how many text messages were sent?",
        120, ["120"],
        "30 + 0.10t = 42 -> 0.10t = 12 -> t = 12 ÷ 0.10 = 120 messages.",
        "120.",
        "120.",
        "12 ÷ 0.10 = 120."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q06", G, LID, LT, DOM, STD, 3,
        "Evaluate: (3 × 10⁵) × (2 × 10³). Enter your answer as a standard whole number.",
        600000000, ["600000000", "600,000,000"],
        "(3 × 2) × 10^(5 + 3) = 6 × 10⁸ = 600,000,000.",
        "600,000,000.",
        "600000000.",
        "6 × 10⁸ = 600000000."
    ))
    questions.append(make_mc_question(
        f"{LID}_Q07", G, LID, LT, DOM, STD, 3,
        "The point (4, -3) is reflected across the x-axis, then rotated 180 degrees about the origin. What are its final coordinates?",
        "(-4, -3)",
        ["(4, 3)", "(-4, 3)", "(3, -4)"],
        "Reflect across x-axis: (4, -3) -> (4, 3). Rotate 180°: (4, 3) -> (-4, -3).",
        "(-4, -3).",
        "(-4, -3).",
        "(4, -3) -> (4, 3) -> (-4, -3)."
    ))
    questions.append(make_numeric_question(
        f"{LID}_Q08", G, LID, LT, DOM, STD, 3,
        "Two lines y = 3x - 1 and y = x + 7 intersect at a point. What is the x-coordinate of their intersection?",
        4, ["4"],
        "3x - 1 = x + 7 -> 2x = 8 -> x = 4.",
        "4.",
        "4.",
        "2x = 8 -> x = 4."
    ))

    return questions
