"""
scripts/update_curriculum_metadata.py
Synchronizes lesson metadata across curriculum.json and grade_*.json
in both shared/data/ and website/shared/data/.
Ensures accurate titles, CCSS standards, and rich descriptions.
"""
import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

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

DESCRIPTIONS = {
    # Grade 4
    "G4_L03": "Find all factor pairs for a whole number in the range 1-100; determine whether a number is a multiple or prime/composite.",
    "G4_L04": "Generate a number or shape pattern that follows a given rule, and identify apparent features of the pattern.",
    "G4_L05": "Solve multi-step word problems with whole numbers using equations with a variable standing for the unknown quantity.",
    "G4_L14": "Decompose a fraction into a sum of fractions with the same denominator in more than one way, and solve addition/subtraction word problems.",
    "G4_L24": "Draw and identify points, lines, line segments, rays, angles, perpendicular and parallel lines, and recognize lines of symmetry.",
    "G4_L25": "Classify two-dimensional figures based on parallel or perpendicular lines and angle types, and apply math to practical situations.",
    
    # Grade 5
    "G5_L12": "Apply and extend previous understandings of multiplication to multiply a fraction or whole number by a fraction.",

    # Grade 6
    "G6_L01": "Understand the concept of a ratio and use ratio language to describe a relationship between two quantities.",
    "G6_L02": "Understand unit rate a/b associated with a ratio a:b and solve real-world unit rate problems.",
    "G6_L03": "Find equivalent ratios using ratio tables, tape diagrams, and double number line diagrams.",
    "G6_L04": "Find a percent of a quantity as a rate per 100 and solve problems involving parts, wholes, and percents.",
    "G6_L05": "Use ratio reasoning to convert measurement units across customary and metric systems.",
    "G6_L06": "Interpret and compute quotients of fractions, and solve word problems involving division of fractions by fractions.",
    "G6_L07": "Fluently divide multi-digit numbers using standard algorithms, and perform operations on decimals.",
    "G6_L08": "Find greatest common factors up to 100 and least common multiples up to 12 using prime factorization.",
    "G6_L09": "Understand positive and negative integers to describe real-world quantities, and graph on number lines.",
    "G6_L10": "Interpret absolute value as magnitude and distance from zero, and distinguish comparison from absolute value.",
    "G6_L11": "Write and evaluate numerical expressions involving whole-number exponents.",
    "G6_L12": "Evaluate algebraic expressions at specific values of their variables using the order of operations.",
    "G6_L13": "Apply properties of operations such as the distributive property to generate equivalent expressions.",
    "G6_L14": "Solve one-variable linear equations using inverse operations and check solutions for reasonableness.",
    "G6_L15": "Write inequalities of the form x > c or x < c to represent constraints, and graph solutions on number lines.",
    "G6_L16": "Calculate the area of right triangles, acute/obtuse triangles, and special quadrilaterals.",
    "G6_L17": "Calculate area of irregular polygons by decomposing into triangles and rectangles.",
    "G6_L18": "Find volume of rectangular prisms with fractional edge lengths using unit cube packing and V = lwh.",
    "G6_L19": "Construct two-dimensional nets and calculate total surface area of prisms and pyramids.",
    "G6_L20": "Plot polygons in the coordinate plane given coordinates and determine perimeter and side lengths.",
    "G6_L21": "Recognize statistical questions and describe data distributions by center, spread, and overall shape.",
    "G6_L22": "Calculate and interpret measures of center including mean and median in real-world contexts.",
    "G6_L23": "Display numerical data in plots on a number line, including dot plots, histograms, and box plots.",
    "G6_L24": "Apply rates, ratios, and percentages to personal finance, budgeting, and unit price calculations.",
    "G6_L25": "Solve multi-step cumulative review word problems synthesizing all Grade 6 mathematical standards.",

    # Grade 7
    "G7_L01": "Compute unit rates associated with ratios of fractions, including quantities measured in like or different units.",
    "G7_L02": "Decide whether two quantities are in a proportional relationship by testing equivalent ratios in tables and graphs.",
    "G7_L03": "Identify the constant of proportionality in tables, graphs, equations, and diagrams, and write equations y = kx.",
    "G7_L04": "Use proportional relationships to solve multi-step ratio and percent problems involving markups and discounts.",
    "G7_L05": "Solve multi-step consumer math problems including sales tax, gratuity, commissions, fees, and simple interest.",
    "G7_L06": "Apply and extend addition and subtraction to rational numbers; model on a horizontal or vertical number line.",
    "G7_L07": "Multiply and divide signed rational numbers; understand rules for signs and convert fractions to decimals.",
    "G7_L08": "Solve real-world problems involving all four arithmetic operations with rational numbers and complex fractions.",
    "G7_L09": "Apply properties of operations as strategies to add, subtract, factor, and expand linear expressions.",
    "G7_L10": "Solve word problems leading to equations of the form px + q = r and p(x + q) = r with fluency.",
    "G7_L11": "Solve two-step inequalities and graph the solution set on a number line, interpreting context.",
    "G7_L12": "Solve problems involving scale drawings of geometric figures, including computing actual dimensions from scales.",
    "G7_L13": "Draw geometric shapes with given conditions, focusing on constructing triangles from three measures of angles or sides.",
    "G7_L14": "Describe the two-dimensional cross-sections that result from slicing three-dimensional figures.",
    "G7_L15": "Understand formulas for area and circumference of a circle and use them to solve mathematical problems.",
    "G7_L16": "Use facts about supplementary, complementary, vertical, and adjacent angles to solve for unknown angles.",
    "G7_L17": "Calculate area and surface area of two- and three-dimensional composite objects composed of polygons and prisms.",
    "G7_L18": "Find volume of right prisms with polygonal bases and solve practical capacity and packing problems.",
    "G7_L19": "Understand that random sampling produces representative samples to support valid inferences about a population.",
    "G7_L20": "Use measures of center and measures of variability for numerical data to draw informal comparative inferences.",
    "G7_L21": "Understand that the probability of a chance event is a number between 0 and 1 indicating likelihood.",
    "G7_L22": "Develop a probability model and use it to find probabilities of events, comparing model to observed frequencies.",
    "G7_L23": "Find probabilities of compound events using organized lists, tables, tree diagrams, and simulation.",
    "G7_L24": "Synthesize ratios, proportional reasoning, and geometry to solve complex multi-step real-world problems.",
    "G7_L25": "Review all Grade 7 Common Core domains in a comprehensive mathematical capstone challenge.",

    # Grade 8
    "G8_L07": "Graph proportional relationships, interpreting the unit rate as the slope of the graph, and compare different relationships.",
    "G8_L16": "Construct and interpret scatter plots for bivariate measurement data to investigate patterns of association.",
    "G8_L17": "Know that straight lines are widely used to model relationships; use the equation of a linear model to solve problems."
}

def update_all():
    curriculum_lessons = []

    for grade in range(3, 9):
        print(f"Processing Grade {grade}...")
        builder_fn = BUILDERS[grade]
        questions = builder_fn()

        # Build lesson mapping from questions
        lesson_meta = {}
        for q in questions:
            lid = q['lessonId']
            if lid not in lesson_meta:
                lesson_meta[lid] = {
                    'title': q['lessonTitle'],
                    'domain': q['domain'],
                    'standard': q['standard']
                }

        # Load existing lessons to preserve unit names and numbers
        existing_path = os.path.join(BASE_DIR, "shared", "data", f"grade_{grade}.json")
        with open(existing_path, 'r', encoding='utf-8') as f:
            grade_data = json.load(f)

        updated_lessons = []
        for l in grade_data['lessons']:
            lid = l['lessonId']
            meta = lesson_meta.get(lid, {})

            # Clean and update
            new_title = meta.get('title', l['title'])
            new_standard = meta.get('standard', l['standard'])
            new_domain = meta.get('domain', l.get('domain', ''))

            # Description fallback
            new_desc = DESCRIPTIONS.get(lid, l.get('description', ''))
            if not new_desc or len(new_desc) < 15:
                new_desc = f"Master {new_title.lower()} aligned with standard {new_standard}."

            lesson_obj = {
                "lessonNumber": l['lessonNumber'],
                "lessonId": lid,
                "grade": grade,
                "domain": new_domain,
                "unit": l.get('unit', f"Unit {l['lessonNumber']}"),
                "title": new_title,
                "description": new_desc,
                "standard": new_standard,
                "questionCount": 8
            }
            updated_lessons.append(lesson_obj)
            curriculum_lessons.append(lesson_obj)

        grade_payload = {
            "grade": grade,
            "lessonCount": 25,
            "questionCount": 200,
            "lessons": updated_lessons,
            "questions": questions
        }

        # Save to shared/data/ and website/shared/data/
        for base in ["shared/data", "website/shared/data"]:
            out_file = os.path.join(BASE_DIR, base, f"grade_{grade}.json")
            with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(grade_payload, f, indent=2, ensure_ascii=False)
            print(f"  Saved {out_file}")

    # Now write curriculum.json
    curr_payload = {
        "grades": [3, 4, 5, 6, 7, 8],
        "totalLessons": len(curriculum_lessons),
        "lessons": curriculum_lessons
    }

    for base in ["shared/data", "website/shared/data"]:
        out_curr = os.path.join(BASE_DIR, base, "curriculum.json")
        with open(out_curr, 'w', encoding='utf-8') as f:
            json.dump(curr_payload, f, indent=2, ensure_ascii=False)
        print(f"Saved {out_curr}")

if __name__ == '__main__':
    update_all()
    print("\nCurriculum metadata update completed successfully!")
