"""Generate faculty example Full lab observations (one file per Full task)."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent / "observations"


def tc(rows: list[tuple[str, str, str, str]]) -> str:
    lines = [
        "| # | Input | Expected output | Actual output | Type |",
        "|---|-------|-----------------|---------------|------|",
    ]
    for i, (inp, exp, act, typ) in enumerate(rows, 1):
        lines.append(f"| {i} | {inp} | {exp} | {act} | {typ} |")
    return "\n".join(lines)


def flowchart_linear(steps: list[str]) -> str:
    """Simple top-to-bottom Mermaid flowchart."""
    nodes = []
    edges = []
    for i, label in enumerate(steps):
        shape = f'["{label}"]' if i not in (0, len(steps) - 1) else f'(["{label}"])'
        if i == 0 or i == len(steps) - 1:
            nodes.append(f"    N{i}{shape}")
        else:
            # parallelogram-ish via stadium for I/O, rectangle for process
            if label.lower().startswith("read") or label.lower().startswith("print") or label.lower().startswith("display"):
                nodes.append(f'    N{i}[/"{label}"/]')
            else:
                nodes.append(f'    N{i}["{label}"]')
        if i > 0:
            edges.append(f"    N{i-1} --> N{i}")
    return "```mermaid\nflowchart TD\n" + "\n".join(nodes + edges) + "\n```"


def flowchart_decision(
    start_io: list[str],
    condition: str,
    yes_path: list[str],
    no_path: list[str],
    end: str = "Stop",
) -> str:
    nodes = ['    S(["Start"])']
    edges = []
    prev = "S"
    for i, label in enumerate(start_io):
        nid = f"A{i}"
        nodes.append(f'    {nid}[/"{label}"/]')
        edges.append(f"    {prev} --> {nid}")
        prev = nid
    nodes.append(f'    D{{"{condition}"}}')
    edges.append(f"    {prev} --> D")
    for i, label in enumerate(yes_path):
        nid = f"Y{i}"
        nodes.append(f'    {nid}[/"{label}"/]' if label.lower().startswith("print") or label.lower().startswith("display") else f'    {nid}["{label}"]')
        if i == 0:
            edges.append(f'    D -->|Yes| {nid}')
        else:
            edges.append(f"    Y{i-1} --> {nid}")
    for i, label in enumerate(no_path):
        nid = f"N{i}"
        nodes.append(f'    {nid}[/"{label}"/]' if label.lower().startswith("print") or label.lower().startswith("display") else f'    {nid}["{label}"]')
        if i == 0:
            edges.append(f'    D -->|No| {nid}')
        else:
            edges.append(f"    N{i-1} --> {nid}")
    nodes.append(f'    E(["{end}"])')
    if yes_path:
        edges.append(f"    Y{len(yes_path)-1} --> E")
    else:
        edges.append("    D -->|Yes| E")
    if no_path:
        edges.append(f"    N{len(no_path)-1} --> E")
    else:
        edges.append("    D -->|No| E")
    return "```mermaid\nflowchart TD\n" + "\n".join(nodes + edges) + "\n```"


def doc(
    title: str,
    task: str,
    aim: str,
    algorithm: list[str],
    flowchart: str,
    pseudocode: str,
    program: str,
    filename: str,
    test_cases: str,
    hint_anchor: str,
) -> str:
    algo = "\n".join(f"{i}. {step}" for i, step in enumerate(algorithm, 1))
    return f"""# {title} — Example full observation

Faculty reference for a complete **Full** lab observation (Task, Aim, Algorithm, Flowchart, Pseudocode, Python program, Saved file location, Test cases). Students prepare their own write-up before lab.

## Right-hand page

### Task

{task}

### Aim

{aim}

### Algorithm

{algo}

### Python program

```python
{program.strip()}
```

### Saved file location

`{filename}` (repository root)

## Left-hand page

### Flowchart

{flowchart}

### Pseudocode

```
{pseudocode.strip()}
```

### Test cases

At least **5** cases; at least **2** tricky (edge / boundary / unusual). Actual output shown as when the program is correct.

{test_cases}

[Back to hint](../../docs/hints.md#{hint_anchor}) · [Back to lab tasks](../../docs/lab-tasks/README.md)
"""


# (index_label, cryptic_file, markdown_body)
OBSERVATIONS: list[tuple[str, str, str]] = []


def add(index_label: str, cryptic: str, body: str) -> None:
    OBSERVATIONS.append((index_label, cryptic, body))


# ── Unit 1 ──────────────────────────────────────────────────────────────────

add(
    "Unit 1 Task 1 — Sum of two numbers",
    "u1t1sum.md",
    doc(
        "Unit 1 Task 1",
        "Write a python program to read two numbers and display their sum.",
        "To read two numbers from the user and display their sum.",
        [
            "Start",
            "Read number1 and number2",
            "Compute sum_of_numbers = number1 + number2",
            "Display sum_of_numbers",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read number1, number2",
                "sum = number1 + number2",
                "Print sum",
                "Stop",
            ]
        ),
        """
BEGIN
    READ number1, number2
    sum_of_numbers ← number1 + number2
    PRINT sum_of_numbers
END
""",
        """
# Example: sum of two numbers
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
sum_of_numbers = number1 + number2
print(f"Sum of the two numbers is {sum_of_numbers}")
""",
        "Unit-1_Task-1_Sum_of_Two_Numbers.py",
        tc(
            [
                ("10, 20", "Sum of the two numbers is 30.0", "Sum of the two numbers is 30.0", "Normal"),
                ("-5, 8", "Sum of the two numbers is 3.0", "Sum of the two numbers is 3.0", "Normal"),
                ("2.5, 3.5", "Sum of the two numbers is 6.0", "Sum of the two numbers is 6.0", "Normal"),
                ("0, 0", "Sum of the two numbers is 0.0", "Sum of the two numbers is 0.0", "Tricky"),
                ("-10, -20", "Sum of the two numbers is -30.0", "Sum of the two numbers is -30.0", "Tricky"),
            ]
        ),
        "unit-1-task-1",
    ),
)

add(
    "Unit 1 Task 2 — Square of a number",
    "u1t2sqr.md",
    doc(
        "Unit 1 Task 2",
        "Write a python program to display the square of a number.",
        "To read a number and display its square.",
        [
            "Start",
            "Read number",
            "Compute square_of_number = number ** 2",
            "Display square_of_number",
            "Stop",
        ],
        flowchart_linear(
            ["Start", "Read number", "square = number ** 2", "Print square", "Stop"]
        ),
        """
BEGIN
    READ number
    square_of_number ← number ** 2
    PRINT square_of_number
END
""",
        """
# Example: square of a number
number = float(input("Enter a number: "))
square_of_number = number ** 2
print(f"Square of the number is {square_of_number}")
""",
        "Unit-1_Task-2_Square_of_a_Number.py",
        tc(
            [
                ("5", "Square of the number is 25.0", "Square of the number is 25.0", "Normal"),
                ("0", "Square of the number is 0.0", "Square of the number is 0.0", "Normal"),
                ("1.5", "Square of the number is 2.25", "Square of the number is 2.25", "Normal"),
                ("-4", "Square of the number is 16.0", "Square of the number is 16.0", "Tricky"),
                ("0.1", "Square of the number is 0.01", "Square of the number is 0.01", "Tricky"),
            ]
        ),
        "unit-1-task-2",
    ),
)

add(
    "Unit 1 Task 3 — Rectangle area and perimeter",
    "u1t3rec.md",
    doc(
        "Unit 1 Task 3",
        "Write a python program to calculate area and perimeter of a rectangle.",
        "To calculate the area and perimeter of a rectangle from length and breadth.",
        [
            "Start",
            "Read length_in_cm and breadth_in_cm",
            "Compute area_in_square_cm = length_in_cm * breadth_in_cm",
            "Compute perimeter_in_cm = 2 * (length_in_cm + breadth_in_cm)",
            "Display area and perimeter",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read length, breadth",
                "area = length * breadth",
                "perimeter = 2*(length+breadth)",
                "Print area, perimeter",
                "Stop",
            ]
        ),
        """
BEGIN
    READ length_in_cm, breadth_in_cm
    area_in_square_cm ← length_in_cm * breadth_in_cm
    perimeter_in_cm ← 2 * (length_in_cm + breadth_in_cm)
    PRINT area_in_square_cm, perimeter_in_cm
END
""",
        """
# Example: rectangle area and perimeter
length_in_cm = float(input("Enter length in cm: "))
breadth_in_cm = float(input("Enter breadth in cm: "))
area_in_square_cm = length_in_cm * breadth_in_cm
perimeter_in_cm = 2 * (length_in_cm + breadth_in_cm)
print(f"Area of the rectangle is {area_in_square_cm} square cm")
print(f"Perimeter of the rectangle is {perimeter_in_cm} cm")
""",
        "Unit-1_Task-3_Rectangle_Area_Perimeter.py",
        tc(
            [
                ("10, 5", "Area 50.0 sq cm; Perimeter 30.0 cm", "Area 50.0 sq cm; Perimeter 30.0 cm", "Normal"),
                ("7, 7", "Area 49.0 sq cm; Perimeter 28.0 cm", "Area 49.0 sq cm; Perimeter 28.0 cm", "Normal"),
                ("2.5, 4", "Area 10.0 sq cm; Perimeter 13.0 cm", "Area 10.0 sq cm; Perimeter 13.0 cm", "Normal"),
                ("1, 100", "Area 100.0 sq cm; Perimeter 202.0 cm", "Area 100.0 sq cm; Perimeter 202.0 cm", "Tricky"),
                ("0.5, 0.5", "Area 0.25 sq cm; Perimeter 2.0 cm", "Area 0.25 sq cm; Perimeter 2.0 cm", "Tricky"),
            ]
        ),
        "unit-1-task-3",
    ),
)

add(
    "Unit 1 Task 4 — Celsius to Fahrenheit",
    "u1t4c2f.md",
    doc(
        "Unit 1 Task 4",
        "Write a python program to convert temperature from Celsius to Fahrenheit.",
        "To convert a temperature from Celsius to Fahrenheit using the standard formula.",
        [
            "Start",
            "Read temperature_in_celsius",
            "Compute temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32",
            "Display temperature_in_fahrenheit",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read Celsius",
                "F = (C * 9/5) + 32",
                "Print Fahrenheit",
                "Stop",
            ]
        ),
        """
BEGIN
    READ temperature_in_celsius
    temperature_in_fahrenheit ← (temperature_in_celsius * 9 / 5) + 32
    PRINT temperature_in_fahrenheit
END
""",
        """
# Example: Celsius to Fahrenheit
temperature_in_celsius = float(input("Enter temperature in Celsius: "))
temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit is {temperature_in_fahrenheit}")
""",
        "Unit-1_Task-4_Celsius_to_Fahrenheit.py",
        tc(
            [
                ("25", "Temperature in Fahrenheit is 77.0", "Temperature in Fahrenheit is 77.0", "Normal"),
                ("0", "Temperature in Fahrenheit is 32.0", "Temperature in Fahrenheit is 32.0", "Normal"),
                ("100", "Temperature in Fahrenheit is 212.0", "Temperature in Fahrenheit is 212.0", "Normal"),
                ("-40", "Temperature in Fahrenheit is -40.0", "Temperature in Fahrenheit is -40.0", "Tricky"),
                ("37", "Temperature in Fahrenheit is 98.6", "Temperature in Fahrenheit is 98.6", "Tricky"),
            ]
        ),
        "unit-1-task-4",
    ),
)

add(
    "Unit 1 Task 5 — Swap two numbers",
    "u1t5swp.md",
    doc(
        "Unit 1 Task 5",
        "Write a python program to swap two numbers without using a third variable.",
        "To exchange the values of two numbers without using a third variable (arithmetic approach).",
        [
            "Start",
            "Read number1 and number2",
            "Set number1 = number1 + number2",
            "Set number2 = number1 - number2",
            "Set number1 = number1 - number2",
            "Display number1 and number2",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read number1, number2",
                "number1 = number1 + number2",
                "number2 = number1 - number2",
                "number1 = number1 - number2",
                "Print swapped values",
                "Stop",
            ]
        ),
        """
BEGIN
    READ number1, number2
    number1 ← number1 + number2
    number2 ← number1 - number2
    number1 ← number1 - number2
    PRINT number1, number2
END
""",
        """
# Example: swap two numbers without a third variable
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print(f"After swapping, first number is {number1} and second number is {number2}")
""",
        "Unit-1_Task-5_Swap_Two_Numbers.py",
        tc(
            [
                ("10, 20", "first 20.0, second 10.0", "first 20.0, second 10.0", "Normal"),
                ("5, 5", "first 5.0, second 5.0", "first 5.0, second 5.0", "Normal"),
                ("-3, 7", "first 7.0, second -3.0", "first 7.0, second -3.0", "Normal"),
                ("0, 15", "first 15.0, second 0.0", "first 15.0, second 0.0", "Tricky"),
                ("-8, -2", "first -2.0, second -8.0", "first -2.0, second -8.0", "Tricky"),
            ]
        ),
        "unit-1-task-5",
    ),
)

add(
    "Unit 1 Task 6 — Simple interest",
    "u1t6si.md",
    doc(
        "Unit 1 Task 6",
        "Write a python program to calculate simple interest.",
        "To calculate simple interest from principal, rate, and time.",
        [
            "Start",
            "Read principal_amount_in_rupees, rate_of_interest_in_percent, time_in_years",
            "Compute simple_interest_in_rupees = (P * R * T) / 100",
            "Display simple_interest_in_rupees",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read P, R, T",
                "SI = (P * R * T) / 100",
                "Print SI",
                "Stop",
            ]
        ),
        """
BEGIN
    READ principal_amount_in_rupees, rate_of_interest_in_percent, time_in_years
    simple_interest_in_rupees ← (principal_amount_in_rupees * rate_of_interest_in_percent * time_in_years) / 100
    PRINT simple_interest_in_rupees
END
""",
        """
# Example: simple interest
principal_amount_in_rupees = float(input("Enter principal amount in rupees: "))
rate_of_interest_in_percent = float(input("Enter rate of interest in percent: "))
time_in_years = float(input("Enter time in years: "))
simple_interest_in_rupees = (
    principal_amount_in_rupees * rate_of_interest_in_percent * time_in_years
) / 100
print(f"Simple interest is {simple_interest_in_rupees} rupees")
""",
        "Unit-1_Task-6_Simple_Interest.py",
        tc(
            [
                ("10000, 5, 2", "Simple interest is 1000.0 rupees", "Simple interest is 1000.0 rupees", "Normal"),
                ("5000, 10, 1", "Simple interest is 500.0 rupees", "Simple interest is 500.0 rupees", "Normal"),
                ("2000, 7.5, 3", "Simple interest is 450.0 rupees", "Simple interest is 450.0 rupees", "Normal"),
                ("1000, 0, 5", "Simple interest is 0.0 rupees", "Simple interest is 0.0 rupees", "Tricky"),
                ("10000, 5, 0.5", "Simple interest is 250.0 rupees", "Simple interest is 250.0 rupees", "Tricky"),
            ]
        ),
        "unit-1-task-6",
    ),
)

add(
    "Unit 1 Task 7 — Compound interest",
    "u1t7ci.md",
    doc(
        "Unit 1 Task 7",
        "Write a python program to calculate compound interest.",
        "To calculate compound interest and total amount from principal, rate, and time.",
        [
            "Start",
            "Read principal_amount_in_rupees, rate_of_interest_in_percent, time_in_years",
            "Compute total_amount_in_rupees = P * (1 + R/100) ** T",
            "Compute compound_interest_in_rupees = total_amount_in_rupees - P",
            "Display total amount and compound interest",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read P, R, T",
                "A = P * (1 + R/100) ** T",
                "CI = A - P",
                "Print A, CI",
                "Stop",
            ]
        ),
        """
BEGIN
    READ principal_amount_in_rupees, rate_of_interest_in_percent, time_in_years
    total_amount_in_rupees ← principal_amount_in_rupees * (1 + rate_of_interest_in_percent / 100) ** time_in_years
    compound_interest_in_rupees ← total_amount_in_rupees - principal_amount_in_rupees
    PRINT total_amount_in_rupees, compound_interest_in_rupees
END
""",
        """
# Example: compound interest
principal_amount_in_rupees = float(input("Enter principal amount in rupees: "))
rate_of_interest_in_percent = float(input("Enter rate of interest in percent: "))
time_in_years = float(input("Enter time in years: "))
total_amount_in_rupees = principal_amount_in_rupees * (
    1 + rate_of_interest_in_percent / 100
) ** time_in_years
compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees
print(f"Total amount is {total_amount_in_rupees} rupees")
print(f"Compound interest is {compound_interest_in_rupees} rupees")
""",
        "Unit-1_Task-7_Compound_Interest.py",
        tc(
            [
                ("10000, 5, 2", "Total 11025.0; CI 1025.0", "Total 11025.0; CI 1025.0", "Normal"),
                ("1000, 10, 1", "Total 1100.0; CI 100.0", "Total 1100.0; CI 100.0", "Normal"),
                ("5000, 8, 3", "Total ≈ 6298.56; CI ≈ 1298.56", "Total ≈ 6298.56; CI ≈ 1298.56", "Normal"),
                ("10000, 0, 5", "Total 10000.0; CI 0.0", "Total 10000.0; CI 0.0", "Tricky"),
                ("1000, 10, 0", "Total 1000.0; CI 0.0", "Total 1000.0; CI 0.0", "Tricky"),
            ]
        ),
        "unit-1-task-7",
    ),
)

add(
    "Unit 1 Task 8 — Sum of first N natural numbers",
    "u1t8nat.md",
    doc(
        "Unit 1 Task 8",
        "Write a python program to find the sum of first N natural numbers using a formula.",
        "To find the sum of the first N natural numbers using the formula N*(N+1)/2.",
        [
            "Start",
            "Read n",
            "Compute sum_of_natural_numbers = n * (n + 1) / 2",
            "Display sum_of_natural_numbers",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read n",
                "sum = n * (n + 1) / 2",
                "Print sum",
                "Stop",
            ]
        ),
        """
BEGIN
    READ n
    sum_of_natural_numbers ← n * (n + 1) / 2
    PRINT sum_of_natural_numbers
END
""",
        """
# Example: sum of first N natural numbers (formula)
n = int(input("Enter the value of n: "))
sum_of_natural_numbers = n * (n + 1) / 2
print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers}")
""",
        "Unit-1_Task-8_Sum_of_N_Natural_Numbers.py",
        tc(
            [
                ("10", "Sum of first 10 natural numbers is 55.0", "Sum of first 10 natural numbers is 55.0", "Normal"),
                ("1", "Sum of first 1 natural numbers is 1.0", "Sum of first 1 natural numbers is 1.0", "Normal"),
                ("100", "Sum of first 100 natural numbers is 5050.0", "Sum of first 100 natural numbers is 5050.0", "Normal"),
                ("0", "Sum of first 0 natural numbers is 0.0", "Sum of first 0 natural numbers is 0.0", "Tricky"),
                ("2", "Sum of first 2 natural numbers is 3.0", "Sum of first 2 natural numbers is 3.0", "Tricky"),
            ]
        ),
        "unit-1-task-8",
    ),
)

# ── Unit 2A ─────────────────────────────────────────────────────────────────

add(
    "Unit 2A Task 1 — Valid triangle",
    "u2a1tri.md",
    doc(
        "Unit 2A Task 1",
        "Write a python program to check whether a triangle is valid given its three angles.",
        "To check whether three given angles form a valid triangle (all positive and sum to 180°).",
        [
            "Start",
            "Read angle1, angle2, angle3",
            "If all angles > 0 and angle1 + angle2 + angle3 == 180, then print valid; else print not valid",
            "Stop",
        ],
        flowchart_decision(
            ["Read angle1, angle2, angle3"],
            "all > 0 and sum == 180?",
            ["Print valid triangle"],
            ["Print not valid"],
        ),
        """
BEGIN
    READ angle1, angle2, angle3
    IF angle1 > 0 AND angle2 > 0 AND angle3 > 0 AND angle1 + angle2 + angle3 = 180 THEN
        PRINT "valid"
    ELSE
        PRINT "not valid"
    ENDIF
END
""",
        """
# Example solution: valid triangle from three angles
angle1_in_degrees = float(input("Enter first angle in degrees: "))
angle2_in_degrees = float(input("Enter second angle in degrees: "))
angle3_in_degrees = float(input("Enter third angle in degrees: "))

if (
    angle1_in_degrees > 0
    and angle2_in_degrees > 0
    and angle3_in_degrees > 0
    and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180
):
    print(
        f"The triangle with angles {angle1_in_degrees}, "
        f"{angle2_in_degrees}, and {angle3_in_degrees} is valid"
    )
else:
    print(
        f"The triangle with angles {angle1_in_degrees}, "
        f"{angle2_in_degrees}, and {angle3_in_degrees} is not valid"
    )
""",
        "Unit-2A_Task-1_Valid_Triangle_Angles.py",
        tc(
            [
                ("60, 60, 60", "valid", "valid", "Normal"),
                ("90, 45, 45", "valid", "valid", "Normal"),
                ("100, 40, 40", "valid", "valid", "Normal"),
                ("90, 90, 90", "not valid (sum 270)", "not valid", "Tricky"),
                ("0, 90, 90", "not valid (zero angle)", "not valid", "Tricky"),
            ]
        ),
        "unit-2a-task-1",
    ),
)

add(
    "Unit 2A Task 3 — Positive, negative, or zero",
    "u2a3pnz.md",
    doc(
        "Unit 2A Task 3",
        "Write a python program to check whether a number is positive, negative, or zero.",
        "To classify a given number as positive, negative, or zero using if-elif-else.",
        [
            "Start",
            "Read number",
            "If number > 0 print positive; else if number < 0 print negative; else print zero",
            "Stop",
        ],
        flowchart_decision(
            ["Read number"],
            "number > 0?",
            ["Print positive"],
            ["Check if number < 0; print negative or zero"],
        ),
        """
BEGIN
    READ number
    IF number > 0 THEN
        PRINT "positive"
    ELSE IF number < 0 THEN
        PRINT "negative"
    ELSE
        PRINT "zero"
    ENDIF
END
""",
        """
# Example solution: positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive")
elif number < 0:
    print(f"The number {number} is negative")
else:
    print(f"The number {number} is zero")
""",
        "Unit-2A_Task-3_Positive_Negative_Zero.py",
        tc(
            [
                ("5", "positive", "positive", "Normal"),
                ("-3", "negative", "negative", "Normal"),
                ("12.5", "positive", "positive", "Normal"),
                ("0", "zero", "zero", "Tricky"),
                ("-0.001", "negative", "negative", "Tricky"),
            ]
        ),
        "unit-2a-task-3",
    ),
)

add(
    "Unit 2A Task 4 — Student grade (elif ladder)",
    "u2a4grd.md",
    doc(
        "Unit 2A Task 4",
        "Write a python program to print the grade of a student using an elif ladder "
        "(Marks >= 90 → Grade A; >= 80 and < 90 → Grade B; >= 70 and < 80 → Grade C; < 70 → Grade D).",
        "To assign a grade from marks using an if-elif-else ladder.",
        [
            "Start",
            "Read marks",
            "If marks >= 90 → Grade A; else if marks >= 80 → Grade B; else if marks >= 70 → Grade C; else Grade D",
            "Display the grade",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read marks",
                "Choose grade with elif ladder",
                "Print grade",
                "Stop",
            ]
        ),
        """
BEGIN
    READ marks
    IF marks >= 90 THEN
        grade ← "A"
    ELSE IF marks >= 80 THEN
        grade ← "B"
    ELSE IF marks >= 70 THEN
        grade ← "C"
    ELSE
        grade ← "D"
    ENDIF
    PRINT grade
END
""",
        """
# Example solution: student grade using elif ladder
marks = float(input("Enter marks: "))

if marks >= 90:
    print(f"Marks {marks}: Grade A")
elif marks >= 80:
    print(f"Marks {marks}: Grade B")
elif marks >= 70:
    print(f"Marks {marks}: Grade C")
else:
    print(f"Marks {marks}: Grade D")
""",
        "Unit-2A_Task-4_Student_Grade_Elif_Ladder.py",
        tc(
            [
                ("95", "Grade A", "Grade A", "Normal"),
                ("85", "Grade B", "Grade B", "Normal"),
                ("75", "Grade C", "Grade C", "Normal"),
                ("90", "Grade A (boundary)", "Grade A", "Tricky"),
                ("69.9", "Grade D (just below 70)", "Grade D", "Tricky"),
            ]
        ),
        "unit-2a-task-4",
    ),
)

add(
    "Unit 2A Task 5 — Largest of three (nested if)",
    "u2a5max.md",
    doc(
        "Unit 2A Task 5",
        "Write a python program to find the largest of three numbers using nested if.",
        "To find the largest among three numbers using nested if statements.",
        [
            "Start",
            "Read x, y, z",
            "If x >= y: if x >= z then largest = x else largest = z; else if y >= z then largest = y else largest = z",
            "Display largest",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read x, y, z",
                "Compare with nested if",
                "Print largest",
                "Stop",
            ]
        ),
        """
BEGIN
    READ x, y, z
    IF x >= y THEN
        IF x >= z THEN
            largest ← x
        ELSE
            largest ← z
        ENDIF
    ELSE
        IF y >= z THEN
            largest ← y
        ELSE
            largest ← z
        ENDIF
    ENDIF
    PRINT largest
END
""",
        """
# Example solution: largest of three numbers using nested if
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y:
    if x >= z:
        largest = x
    else:
        largest = z
else:
    if y >= z:
        largest = y
    else:
        largest = z

print(f"Largest = {largest} (among {x}, {y}, {z})")
""",
        "Unit-2A_Task-5_Largest_of_Three_Nested_If.py",
        tc(
            [
                ("3, 7, 5", "Largest = 7", "Largest = 7", "Normal"),
                ("10, 2, 8", "Largest = 10", "Largest = 10", "Normal"),
                ("1, 4, 9", "Largest = 9", "Largest = 9", "Normal"),
                ("5, 5, 5", "Largest = 5 (all equal)", "Largest = 5", "Tricky"),
                ("-1, -5, -3", "Largest = -1", "Largest = -1", "Tricky"),
            ]
        ),
        "unit-2a-task-5",
    ),
)

# ── Unit 2B ─────────────────────────────────────────────────────────────────

add(
    "Unit 2B Task 3 — Sum and average of N numbers",
    "u2b3avg.md",
    doc(
        "Unit 2B Task 3",
        "Write a python program to find the sum and average of N numbers using for loop.",
        "To read N numbers, compute their sum and average using a for loop.",
        [
            "Start",
            "Read total_input_numbers (N)",
            "Initialize total_sum = 0",
            "For count from 0 to N-1: read number; total_sum = total_sum + number",
            "Compute average = total_sum / N",
            "Display sum and average",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read N",
                "total_sum = 0",
                "Loop N times: read number, add to sum",
                "average = sum / N",
                "Print sum, average",
                "Stop",
            ]
        ),
        """
BEGIN
    READ N
    total_sum ← 0
    FOR count ← 1 TO N DO
        READ number
        total_sum ← total_sum + number
    ENDFOR
    average ← total_sum / N
    PRINT total_sum, average
END
""",
        """
# Example solution: sum and average of N numbers using a for loop
total_input_numbers = int(input("Enter how many numbers: "))

total_sum = 0

for count in range(total_input_numbers):
    number = float(input("Enter a number: "))
    total_sum = total_sum + number

average = total_sum / total_input_numbers

print(f"Sum of {total_input_numbers} numbers is {total_sum}")
print(f"Average of {total_input_numbers} numbers (sum {total_sum}) is {average}")
""",
        "Unit-2B_Task-3_Sum_and_Average_of_N_Numbers_For_Loop.py",
        tc(
            [
                ("N=3; 10, 20, 30", "Sum 60.0; Avg 20.0", "Sum 60.0; Avg 20.0", "Normal"),
                ("N=2; 5, 15", "Sum 20.0; Avg 10.0", "Sum 20.0; Avg 10.0", "Normal"),
                ("N=4; 1, 2, 3, 4", "Sum 10.0; Avg 2.5", "Sum 10.0; Avg 2.5", "Normal"),
                ("N=1; 7", "Sum 7.0; Avg 7.0", "Sum 7.0; Avg 7.0", "Tricky"),
                ("N=3; -5, 0, 5", "Sum 0.0; Avg 0.0", "Sum 0.0; Avg 0.0", "Tricky"),
            ]
        ),
        "unit-2b-task-3",
    ),
)

add(
    "Unit 2B Task 7 — Fibonacci series up to N terms",
    "u2b7fib.md",
    doc(
        "Unit 2B Task 7",
        "Write a python program to print Fibonacci series up to N terms using for loop.",
        "To print the first N terms of the Fibonacci series using a for loop.",
        [
            "Start",
            "Read n",
            "Initialize first = 0, second = 1",
            "For count from 0 to n-1: print first; next_term = first + second; first = second; second = next_term",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read n",
                "first=0, second=1",
                "Loop n times: print first, update pair",
                "Stop",
            ]
        ),
        """
BEGIN
    READ n
    first ← 0
    second ← 1
    FOR count ← 1 TO n DO
        PRINT first
        next_term ← first + second
        first ← second
        second ← next_term
    ENDFOR
END
""",
        """
# Example solution: Fibonacci series up to N terms using a for loop
n = int(input("Enter how many terms: "))

first = 0
second = 1

for count in range(n):
    print(f"Fibonacci series term {count + 1} of {n} terms = {first}")
    next_term = first + second
    first = second
    second = next_term
""",
        "Unit-2B_Task-7_Fibonacci_Series_N_Terms_For_Loop.py",
        tc(
            [
                ("5", "0 1 1 2 3", "0 1 1 2 3", "Normal"),
                ("7", "0 1 1 2 3 5 8", "0 1 1 2 3 5 8", "Normal"),
                ("3", "0 1 1", "0 1 1", "Normal"),
                ("1", "0", "0", "Tricky"),
                ("2", "0 1", "0 1", "Tricky"),
            ]
        ),
        "unit-2b-task-7",
    ),
)

add(
    "Unit 2B Task 8 — Sum of digits",
    "u2b8dig.md",
    doc(
        "Unit 2B Task 8",
        "Write a python program to find the sum of digits of a number using while loop.",
        "To find the sum of digits of a positive integer using a while loop.",
        [
            "Start",
            "Read number; save original_number; digit_sum = 0",
            "While number > 0: digit = number % 10; digit_sum += digit; number //= 10",
            "Display digit_sum",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read number",
                "digit_sum = 0",
                "While number > 0: add last digit, number //= 10",
                "Print digit_sum",
                "Stop",
            ]
        ),
        """
BEGIN
    READ number
    original ← number
    digit_sum ← 0
    WHILE number > 0 DO
        digit ← number MOD 10
        digit_sum ← digit_sum + digit
        number ← number DIV 10
    ENDWHILE
    PRINT digit_sum
END
""",
        """
# Example solution: sum of digits using a while loop
number = int(input("Enter a number: "))

original_number = number
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum = digit_sum + digit
    number = number // 10

print(f"Sum of digits of {original_number} is {digit_sum}")
""",
        "Unit-2B_Task-8_Sum_of_Digits_While_Loop.py",
        tc(
            [
                ("123", "Sum of digits of 123 is 6", "Sum of digits of 123 is 6", "Normal"),
                ("999", "Sum of digits of 999 is 27", "Sum of digits of 999 is 27", "Normal"),
                ("1001", "Sum of digits of 1001 is 2", "Sum of digits of 1001 is 2", "Normal"),
                ("0", "Sum of digits of 0 is 0 (loop never runs)", "Sum of digits of 0 is 0", "Tricky"),
                ("7", "Sum of digits of 7 is 7", "Sum of digits of 7 is 7", "Tricky"),
            ]
        ),
        "unit-2b-task-8",
    ),
)

add(
    "Unit 2B Task 11 — Armstrong number (3 digits)",
    "u2b11arm.md",
    doc(
        "Unit 2B Task 11",
        "Write a python program to check whether a number is an Armstrong number using while loop "
        "(assume the number has 3 digits).",
        "To check whether a 3-digit number is an Armstrong number (sum of cubes of digits equals the number).",
        [
            "Start",
            "Read number; save original; armstrong_sum = 0",
            "While number > 0: extract digit; armstrong_sum += digit ** 3; number //= 10",
            "If armstrong_sum == original print Armstrong; else print not Armstrong",
            "Stop",
        ],
        flowchart_decision(
            ["Read 3-digit number", "Compute sum of cubes of digits"],
            "sum of cubes == original?",
            ["Print is Armstrong"],
            ["Print is not Armstrong"],
        ),
        """
BEGIN
    READ number
    original ← number
    armstrong_sum ← 0
    WHILE number > 0 DO
        digit ← number MOD 10
        armstrong_sum ← armstrong_sum + digit ** 3
        number ← number DIV 10
    ENDWHILE
    IF armstrong_sum = original THEN
        PRINT "Armstrong"
    ELSE
        PRINT "not Armstrong"
    ENDIF
END
""",
        """
# Example solution: 3-digit Armstrong number check using a while loop
number = int(input("Enter a 3-digit number: "))

original_number = number
armstrong_sum = 0

while number > 0:
    digit = number % 10
    armstrong_sum = armstrong_sum + digit ** 3
    number = number // 10

if armstrong_sum == original_number:
    print(
        f"{original_number} is an Armstrong number "
        f"(sum of cubes of digits is {armstrong_sum})"
    )
else:
    print(
        f"{original_number} is not an Armstrong number "
        f"(sum of cubes of digits is {armstrong_sum})"
    )
""",
        "Unit-2B_Task-11_Armstrong_Number_While_Loop.py",
        tc(
            [
                ("153", "is Armstrong (1^3+5^3+3^3=153)", "is Armstrong", "Normal"),
                ("370", "is Armstrong", "is Armstrong", "Normal"),
                ("371", "is Armstrong", "is Armstrong", "Normal"),
                ("100", "not Armstrong (1)", "not Armstrong", "Tricky"),
                ("999", "not Armstrong (3*729=2187)", "not Armstrong", "Tricky"),
            ]
        ),
        "unit-2b-task-11",
    ),
)

# ── Unit 2C ─────────────────────────────────────────────────────────────────

add(
    "Unit 2C Task 4 — 3x3 numbers (while-for)",
    "u2c4wfr.md",
    doc(
        "Unit 2C Task 4",
        "Write a python program to print numbers in a 3x3 grid using while-for nested loop.",
        "To print numbers 1 to 9 in a 3×3 grid using an outer while loop and an inner for loop.",
        [
            "Start",
            "Initialize num = 1, row_loop_var = 1",
            "While row_loop_var <= 3: for each column 1..3 print num and increment; print newline; increment row",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "num=1, row=1",
                "While row <= 3",
                "For col 1..3: print num, num++",
                "Newline; row++",
                "Stop",
            ]
        ),
        """
BEGIN
    num ← 1
    row ← 1
    WHILE row ≤ 3 DO
        FOR col ← 1 TO 3 DO
            PRINT num
            num ← num + 1
        ENDFOR
        PRINT newline
        row ← row + 1
    ENDWHILE
END
""",
        """
# Example solution: 3x3 grid of numbers (while-for)
num = 1
row_loop_var = 1

while row_loop_var <= 3:
    for column_loop_var in range(1, 4):
        print(num, end=" ")
        num = num + 1
    print()
    row_loop_var = row_loop_var + 1
""",
        "Unit-2C_Task-4_Three_by_Three_Numbers_While_For.py",
        tc(
            [
                ("(no input)", "1 2 3 / 4 5 6 / 7 8 9", "1 2 3 / 4 5 6 / 7 8 9", "Normal"),
                ("Check row count", "exactly 3 lines", "exactly 3 lines", "Normal"),
                ("Check last value", "last printed value is 9", "9", "Normal"),
                ("Spacing", "spaces between numbers on a row", "space-separated", "Tricky"),
                ("First cell", "first printed value is 1", "1", "Tricky"),
            ]
        ),
        "unit-2c-task-4",
    ),
)

add(
    "Unit 2C Task 5 — Star grid (user input)",
    "u2c5stg.md",
    doc(
        "Unit 2C Task 5",
        "Write a python program to print a 5x5 grid of stars (*); generalize so the grid size is based on user input.",
        "To print an N×N grid of stars where N is read from the user (example: 5×5).",
        [
            "Start",
            "Read rows",
            "For each row 1..rows: for each column 1..rows print '* '; print newline",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read rows",
                "For r = 1 to rows",
                "For c = 1 to rows: print *",
                "Newline",
                "Stop",
            ]
        ),
        """
BEGIN
    READ rows
    FOR r ← 1 TO rows DO
        FOR c ← 1 TO rows DO
            PRINT "* "
        ENDFOR
        PRINT newline
    ENDFOR
END
""",
        """
# Example solution: star grid (generalized)
rows = int(input("Enter grid size (rows and columns): "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        print("*", end=" ")
    print()
""",
        "Unit-2C_Task-5_Star_Grid_User_Input.py",
        tc(
            [
                ("5", "5×5 full star grid", "5 rows of 5 stars", "Normal"),
                ("3", "3×3 full star grid", "3 rows of 3 stars", "Normal"),
                ("4", "4×4 full star grid", "4 rows of 4 stars", "Normal"),
                ("1", "single *", "*", "Tricky"),
                ("2", "* * / * *", "2×2 grid", "Tricky"),
            ]
        ),
        "unit-2c-task-5",
    ),
)

add(
    "Unit 2C Task 6 — Hollow star grid (user input)",
    "u2c6hlw.md",
    doc(
        "Unit 2C Task 6",
        "Write a python program to print a 5x5 hollow grid of stars (*); generalize so the grid size is based on user input.",
        "To print an N×N hollow star grid (border only) where N is read from the user.",
        [
            "Start",
            "Read rows",
            "For each row and column: if on border print '*', else print space",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read rows",
                "For each cell",
                "If border: print *; else space",
                "Stop",
            ]
        ),
        """
BEGIN
    READ rows
    FOR r ← 1 TO rows DO
        FOR c ← 1 TO rows DO
            IF r = 1 OR r = rows OR c = 1 OR c = rows THEN
                PRINT "* "
            ELSE
                PRINT "  "
            ENDIF
        ENDFOR
        PRINT newline
    ENDFOR
END
""",
        """
# Example solution: hollow star grid (generalized)
rows = int(input("Enter grid size (rows and columns): "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        if (
            row_loop_var == 1
            or row_loop_var == rows
            or column_loop_var == 1
            or column_loop_var == rows
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
""",
        "Unit-2C_Task-6_Hollow_Star_Grid_User_Input.py",
        tc(
            [
                ("5", "hollow 5×5 (border stars, hollow inside)", "hollow 5×5", "Normal"),
                ("4", "hollow 4×4", "hollow 4×4", "Normal"),
                ("3", "hollow 3×3 (only center empty)", "hollow 3×3", "Normal"),
                ("1", "single * (all cells are border)", "*", "Tricky"),
                ("2", "2×2 all stars (no interior)", "* * / * *", "Tricky"),
            ]
        ),
        "unit-2c-task-6",
    ),
)

add(
    "Unit 2C Task 13 — Pascal's triangle",
    "u2c13pas.md",
    doc(
        "Unit 2C Task 13",
        "Write a python program to print Pascal's triangle.",
        "To print Pascal's triangle for a given number of rows (centered), computing each value from the previous.",
        [
            "Start",
            "Read rows",
            "For each row: print leading spaces; initialize value = 1; for each column print value and update value",
            "Stop",
        ],
        flowchart_linear(
            [
                "Start",
                "Read rows",
                "For each row: spaces then values",
                "Update value with binomial recurrence",
                "Stop",
            ]
        ),
        """
BEGIN
    READ rows
    FOR r ← 1 TO rows DO
        PRINT (rows - r) spaces
        value ← 1
        FOR c ← 1 TO r DO
            PRINT value
            value ← value * (r - c) / c
        ENDFOR
        PRINT newline
    ENDFOR
END
""",
        """
# Example solution: Pascal's triangle
rows = int(input("Enter number of rows: "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end="")
    value = 1
    for column_loop_var in range(1, row_loop_var + 1):
        print(value, end=" ")
        value = value * (row_loop_var - column_loop_var) // column_loop_var
    print()
""",
        "Unit-2C_Task-13_Pascals_Triangle.py",
        tc(
            [
                ("5", "1 / 1 1 / 1 2 1 / 1 3 3 1 / 1 4 6 4 1", "Pascal rows 1..5", "Normal"),
                ("3", "1 / 1 1 / 1 2 1", "Pascal rows 1..3", "Normal"),
                ("4", "… / 1 3 3 1", "includes 1 3 3 1", "Normal"),
                ("1", "1", "1", "Tricky"),
                ("2", "1 / 1 1", "1 then 1 1", "Tricky"),
            ]
        ),
        "unit-2c-task-13",
    ),
)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# Faculty full-observation index",
        "",
        "Not linked from student docs. Example **Full** lab observations (all required sections).",
        "Map task → cryptic file.",
        "",
        "| Task | File |",
        "|------|------|",
    ]
    for label, cryptic, body in OBSERVATIONS:
        path = OUT / cryptic
        path.write_text(body, encoding="utf-8")
        index_lines.append(f"| {label} | `{cryptic}` |")
    (OUT / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(OBSERVATIONS)} observation files + INDEX.md to {OUT}")


if __name__ == "__main__":
    main()
