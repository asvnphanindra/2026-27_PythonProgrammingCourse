# Lab task hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Lab tasks](lab-tasks.md).

> **Important:** In the **Process** section and in sample code, hints show only the **structure** (for example `if` / `else` shape). They do **not** give the full logic.  
> Look for blanks such as `____` and fill in your own code. A short comment next to each blank tells you what to write there. Use the **Example** values to check whether your logic is correct.

Jump to a task:

**Unit 1:** [Task 1](#unit-1-task-1) · [Task 2](#unit-1-task-2) · [Task 3](#unit-1-task-3) · [Task 4](#unit-1-task-4) · [Task 5](#unit-1-task-5) · [Task 6](#unit-1-task-6) · [Task 7](#unit-1-task-7) · [Task 8](#unit-1-task-8) · [Task 9](#unit-1-task-9) · [Task 10](#unit-1-task-10) · [Task 11](#unit-1-task-11) · [Task 12](#unit-1-task-12) · [Task 13](#unit-1-task-13) · [Task 14](#unit-1-task-14) · [Task 15](#unit-1-task-15)

**Unit 2A:** [Task 1](#unit-2a-task-1) · [Task 2](#unit-2a-task-2) · [Task 3](#unit-2a-task-3) · [Task 5](#unit-2a-task-5) · [Task 7 Approach 1](#unit-2a-task-7-approach-1) · [Task 7 Approach 2](#unit-2a-task-7-approach-2) · [Task 7 Approach 3](#unit-2a-task-7-approach-3) · [Task 8](#unit-2a-task-8)

**Unit 2B:** [Task 1 Approach 1](#unit-2b-task-1-approach-1) · [Task 1 Approach 2](#unit-2b-task-1-approach-2) · [Task 2 Approach 1](#unit-2b-task-2-approach-1) · [Task 2 Approach 2](#unit-2b-task-2-approach-2) · [Task 3](#unit-2b-task-3) · [Task 4](#unit-2b-task-4) · [Task 5](#unit-2b-task-5) · [Task 6](#unit-2b-task-6) · [Task 7](#unit-2b-task-7) · [Task 8](#unit-2b-task-8) · [Task 9](#unit-2b-task-9) · [Task 10](#unit-2b-task-10) · [Task 11](#unit-2b-task-11) · [Task 12](#unit-2b-task-12) · [Task 13 Approach 1](#unit-2b-task-13-approach-1) · [Task 13 Approach 2](#unit-2b-task-13-approach-2) · [Task 14 Approach 1](#unit-2b-task-14-approach-1) · [Task 14 Approach 2](#unit-2b-task-14-approach-2) · [Task 15 Approach 1](#unit-2b-task-15-approach-1) · [Task 15 Approach 2](#unit-2b-task-15-approach-2)

---

<a id="unit-1-task-1"></a>

## Unit 1 Task 1: Sum of two numbers

Reads two numbers from the user and displays their sum.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `number1`, `number2` |
| **Process** | `sum_of_numbers = number1 + number2` |
| **Output** | `sum_of_numbers` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
```

**Output messages** (use with `print()`):

```python
print(f"Sum of the two numbers is {sum_of_numbers}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation** | `sum_of_numbers = 10 + 20 = 30` |
| **Example output** | `sum_of_numbers = 30` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-2"></a>

## Unit 1 Task 2: Square of a number

Reads a number and displays its square.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `number` |
| **Process** | `square_of_number = number ** 2` |
| **Output** | `square_of_number` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = float(input("Enter a number: "))
```

**Output messages** (use with `print()`):

```python
print(f"Square of the number is {square_of_number}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | `square_of_number = 5 ** 2 = 25` |
| **Example output** | `square_of_number = 25` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-3"></a>

## Unit 1 Task 3: Area and perimeter of a rectangle

Calculates the area and perimeter of a rectangle from its length and breadth.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `length_in_cm`, `breadth_in_cm` |
| **Process** | `area_in_square_cm = length_in_cm * breadth_in_cm`<br>`perimeter_in_cm = 2 * (length_in_cm + breadth_in_cm)` |
| **Output** | `area_in_square_cm`, `perimeter_in_cm` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
length_in_cm = float(input("Enter length in cm: "))
breadth_in_cm = float(input("Enter breadth in cm: "))
```

**Output messages** (use with `print()`):

```python
print(f"Area of the rectangle is {area_in_square_cm} square cm")
print(f"Perimeter of the rectangle is {perimeter_in_cm} cm")
```

> **Note on units:** State the unit clearly in your `input()` message. This example uses **cm** for length/breadth, **cm** for perimeter, and **square cm** for area. You may choose any other appropriate unit (m, mm, inches, and so on), but keep input and output units consistent.

### Example

| Item | Details |
|------|---------|
| **Example input** | `length_in_cm = 10`, `breadth_in_cm = 5` |
| **Example calculation** | `area_in_square_cm = 10 * 5 = 50`<br>`perimeter_in_cm = 2 * (10 + 5) = 30` |
| **Example output** | `area_in_square_cm = 50`, `perimeter_in_cm = 30` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-4"></a>

## Unit 1 Task 4: Celsius to Fahrenheit

Converts a Celsius temperature to Fahrenheit using the standard conversion formula.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `temperature_in_celsius` |
| **Process** | `temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32` |
| **Output** | `temperature_in_fahrenheit` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
temperature_in_celsius = float(input("Enter temperature in Celsius: "))
```

**Output messages** (use with `print()`):

```python
print(f"Temperature in Fahrenheit is {temperature_in_fahrenheit}")
```

> **Note on units:** Make the unit clear in your `input()` prompt. Output should also show Fahrenheit clearly in `print()`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `temperature_in_celsius = 25` |
| **Example calculation** | `(25 * 9 / 5) + 32 = 77` |
| **Example output** | `temperature_in_fahrenheit = 77` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-5"></a>

## Unit 1 Task 5: Swap two numbers

Exchanges the values of two variables. Approach 1 is the Python way; Approach 2 swaps using only arithmetic, without a third variable.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `number1`, `number2` |
| **Process (Approach 1)** | `number1, number2 = number2, number1` |
| **Process (Approach 2)** | `number1 = number1 + number2`<br>`number2 = number1 - number2`<br>`number1 = number1 - number2` |
| **Output** | `number1`, `number2` (after swap) |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
```

**Output messages** (use with `print()`):

```python
print(f"After swapping, first number is {number1} and second number is {number2}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation (Approach 2)** | `number1 = 10 + 20 = 30`<br>`number2 = 30 - 20 = 10`<br>`number1 = 30 - 10 = 20` |
| **Example output** | `number1 = 20`, `number2 = 10` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-6"></a>

## Unit 1 Task 6: Simple interest

Finds interest earned on a fixed principal over time. Interest is calculated only on the original amount.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `principal_amount_in_rupees`, `rate_of_interest_in_percent`, `time_in_years` |
| **Process** | `simple_interest_in_rupees = (principal_amount_in_rupees * rate_of_interest_in_percent * time_in_years) / 100` |
| **Output** | `simple_interest_in_rupees` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
principal_amount_in_rupees = float(input("Enter principal amount in rupees: "))
rate_of_interest_in_percent = float(input("Enter rate of interest in percent: "))
time_in_years = float(input("Enter time in years: "))
```

**Output messages** (use with `print()`):

```python
print(f"Simple interest is {simple_interest_in_rupees} rupees")
```

> **Note on units:** State each unit in your `input()` message.
>
> **Good:** `Enter principal amount in rupees: `  
> **Unclear:** `Enter principal: `
>
> Use clear units such as rupees, percent, and years so the user knows exactly what to enter.

### Example

| Item | Details |
|------|---------|
| **Example input** | `principal_amount_in_rupees = 10000`, `rate_of_interest_in_percent = 5`, `time_in_years = 2` |
| **Example calculation** | `(10000 * 5 * 2) / 100 = 1000` |
| **Example output** | `simple_interest_in_rupees = 1000` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-7"></a>

## Unit 1 Task 7: Compound interest

Finds interest where each year’s interest is added to the principal. Next year’s interest is calculated on this new total.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `principal_amount_in_rupees`, `rate_of_interest_in_percent`, `time_in_years` |
| **Process** | `total_amount_in_rupees = principal_amount_in_rupees * (1 + rate_of_interest_in_percent / 100) ** time_in_years`<br>`compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees` |
| **Output** | `compound_interest_in_rupees` (optionally `total_amount_in_rupees`) |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
principal_amount_in_rupees = float(input("Enter principal amount in rupees: "))
rate_of_interest_in_percent = float(input("Enter rate of interest in percent: "))
time_in_years = float(input("Enter time in years: "))
```

**Output messages** (use with `print()`):

```python
print(f"Total amount is {total_amount_in_rupees} rupees")
print(f"Compound interest is {compound_interest_in_rupees} rupees")
```

> **Note on units:** State each unit in your `input()` message (rupees, percent, years). Keep the output unit consistent (rupees) in `print()`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `principal_amount_in_rupees = 10000`, `rate_of_interest_in_percent = 5`, `time_in_years = 2` |
| **Example calculation** | `10000 * (1.05) ** 2 = 11025`<br>`11025 - 10000 = 1025` |
| **Example output** | `total_amount_in_rupees = 11025`, `compound_interest_in_rupees = 1025` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-8"></a>

## Unit 1 Task 8: Sum of first N natural numbers

Adds the first `n` natural numbers using a formula, so a loop is not needed.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `n` `# n matches the formula` |
| **Process** | `sum_of_natural_numbers = n * (n + 1) / 2`<br>`# Formula: sum_of_natural_numbers = n * (n + 1) / 2` |
| **Output** | `sum_of_natural_numbers` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of n: "))
```

**Output messages** (use with `print()`):

```python
print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 10` |
| **Example calculation** | `10 * (10 + 1) / 2 = 55` |
| **Example output** | `sum_of_natural_numbers = 55` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-9"></a>

## Unit 1 Task 9: Arithmetic operators

Performs arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`) on two numbers and displays the results.

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
```

**Output messages** (use with `print()`):

```python
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponent: {exponent}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 3` |
| **Example calculation** | `10 + 3 = 13`<br>`10 - 3 = 7`<br>`10 * 3 = 30`<br>`10 / 3 = 3.333...`<br>`10 // 3 = 3`<br>`10 % 3 = 1`<br>`10 ** 3 = 1000` |
| **Example output** | `13`, `7`, `30`, `3.333...`, `3`, `1`, `1000` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-10"></a>

## Unit 1 Task 10: Relational operators

Compares two numbers using relational operators and prints the Boolean results.

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
```

**Output messages** (use with `print()`):

```python
print(f"{number1} == {number2} is {number1 == number2}")
print(f"{number1} != {number2} is {number1 != number2}")
print(f"{number1} > {number2} is {number1 > number2}")
print(f"{number1} < {number2} is {number1 < number2}")
print(f"{number1} >= {number2} is {number1 >= number2}")
print(f"{number1} <= {number2} is {number1 <= number2}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation** | `10 == 20 → False`<br>`10 != 20 → True`<br>`10 > 20 → False`<br>`10 < 20 → True`<br>`10 >= 20 → False`<br>`10 <= 20 → True` |
| **Example output** | `False`, `True`, `False`, `True`, `False`, `True` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-11"></a>

## Unit 1 Task 11: Logical operators

Demonstrates logical operators `and`, `or`, and `not` using Boolean conditions.

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
```

**Output messages** (use with `print()`):

```python
print(f"({number1} > 5) and ({number2} > 15) is {(number1 > 5) and (number2 > 15)}")
print(f"({number1} > 50) or ({number2} > 15) is {(number1 > 50) or (number2 > 15)}")
print(f"not ({number1} > 50) is {not (number1 > 50)}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation** | `(10 > 5) and (20 > 15) → True`<br>`(10 > 50) or (20 > 15) → True`<br>`not (10 > 50) → True` |
| **Example output** | `True`, `True`, `True` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-12"></a>

## Unit 1 Task 12: Identity operators

Demonstrates identity operators `is` and `is not` (whether two names refer to the same object), with both `True` and `False` cases for each operator.

### Sample input and output messages

This task is usually demonstrated with variables in code (lists need not come from `input()`).

```python
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(f"list_a is list_b: {list_a is list_b}")          # True
print(f"list_a is list_c: {list_a is list_c}")          # False
print(f"list_a is not list_c: {list_a is not list_c}")  # True
print(f"list_a is not list_b: {list_a is not list_b}")  # False
```

> **Note:** `==` checks value equality. `is` checks whether both names refer to the **same object** in memory.

### Example

| Operator | Case | Example | Result |
|----------|------|---------|--------|
| `is` | True | `list_a is list_b` (same object) | `True` |
| `is` | False | `list_a is list_c` (different objects) | `False` |
| `is not` | True | `list_a is not list_c` (different objects) | `True` |
| `is not` | False | `list_a is not list_b` (same object) | `False` |

Where:

```python
list_a = [1, 2, 3]
list_b = list_a      # same object as list_a
list_c = [1, 2, 3]   # same values, but a different object
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-13"></a>

## Unit 1 Task 13: Membership operators

Demonstrates membership operators `in` and `not in` with the basic Python data types that support membership checks: **string**, **list**, **tuple**, **set**, and **dictionary**.

### Sample input and output messages

This task is usually demonstrated with fixed examples covering each data type.

```python
# string
text = "python"
print(f"'th' in '{text}' is {'th' in text}")
print(f"'xyz' not in '{text}' is {'xyz' not in text}")

# list (int, float, bool, str values)
number_list = [10, 20, 30]
float_list = [1.5, 2.5, 3.5]
bool_list = [True, False]
string_list = ["hi", "bye"]
print(f"10 in {number_list} is {10 in number_list}")
print(f"3.5 in {float_list} is {3.5 in float_list}")
print(f"True in {bool_list} is {True in bool_list}")
print(f"'hi' in {string_list} is {'hi' in string_list}")

# tuple
number_tuple = (1, 2, 3)
print(f"2 in {number_tuple} is {2 in number_tuple}")

# set
number_set = {1, 5, 9}
print(f"5 in {number_set} is {5 in number_set}")

# dictionary (membership checks keys)
student = {"name": "Ada", "age": 20}
print(f"'name' in {student} is {'name' in student}")
print(f"'Ada' not in {student} is {'Ada' not in student}")
```

> **Note:** Use `in` / `not in` with containers such as `str`, `list`, `tuple`, `set`, and `dict`. You can search for basic values (`int`, `float`, `bool`, `str`) **inside** these containers. For a dictionary, `in` checks the **keys**, not the values.
>
> `int`, `float`, and `bool` themselves are not containers, so expressions like `2 in 10` are invalid.

### Example

| Data type | Example | Result |
|-----------|---------|--------|
| **string (`str`)** | `"th" in "python"` | `True` |
| **string (`str`)** | `"xyz" not in "python"` | `True` |
| **list** | `10 in [10, 20, 30]` | `True` |
| **list** | `3.5 in [1.5, 2.5, 3.5]` | `True` |
| **list** | `True in [True, False]` | `True` |
| **tuple** | `2 in (1, 2, 3)` | `True` |
| **set** | `5 in {1, 5, 9}` | `True` |
| **dictionary (`dict`)** | `"name" in {"name": "Ada", "age": 20}` | `True` (checks **keys**) |
| **dictionary (`dict`)** | `"Ada" not in {"name": "Ada", "age": 20}` | `True` (values are not checked by default) |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-14"></a>

## Unit 1 Task 14: Operator precedence and associativity

Shows how operator precedence and associativity decide the order of evaluation in an expression.

### Sample input and output messages

This task is usually demonstrated with fixed expressions in code.

```python
print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")
print(f"10 - 4 - 2 = {10 - 4 - 2}")
```

> **Note:** Higher-precedence operators are evaluated first. For the same precedence, associativity decides the order (`**` is right-to-left; most others are left-to-right).

### Example

| Item | Details |
|------|---------|
| **Example expressions** | `2 + 3 * 4`<br>`2 ** 3 ** 2`<br>`10 - 4 - 2` |
| **Example calculation** | `2 + 3 * 4 = 2 + 12 = 14` (`*` before `+`)<br>`2 ** 3 ** 2 = 2 ** 9 = 512` (`**` is right-associative)<br>`10 - 4 - 2 = 6 - 2 = 4` (`-` is left-associative) |
| **Example output** | `14`, `512`, `4` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-15"></a>

## Unit 1 Task 15: Type conversion (int, float, string)

Demonstrates converting values between `int`, `float`, and `str` using the variable names `str_num`, `float_num`, and `int_num`.

### Sample input and output messages

**Input messages** (use with `input()`):

```python
str_num = input("Enter a numeric value as text: ")
```

**Output messages** (use with `print()`):

```python
int_num = int(str_num)
float_num = float(str_num)
str_num = str(int_num)

print(f"Integer value: {int_num}, type: {type(int_num)}")
print(f"Float value: {float_num}, type: {type(float_num)}")
print(f"String value: {str_num}, type: {type(str_num)}")
```

> **Note:** `input()` always returns a string. Convert with `int()` or `float()` before doing arithmetic.
>
> Refer to the **class notes** and try executing the examples discussed in the class to strengthen your understanding of type conversion.

### Example

| Item | Details |
|------|---------|
| **Example input** | `str_num = "25"` |
| **Example calculation** | `int_num = int("25") → 25`<br>`float_num = float("25") → 25.0`<br>`str_num = str(25) → "25"` |
| **Example output** | `int_num = 25`, `float_num = 25.0`, `str_num = "25"` |

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-1"></a>

## Unit 2A Task 1: Valid triangle (three angles)

Checks whether a triangle is valid when its three angles are given. Think about the rules a valid triangle must satisfy (use class notes and the example below).

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `angle1_in_degrees`, `angle2_in_degrees`, `angle3_in_degrees` |
| **Process** | Use an `if-else` structure. Write your own condition to decide whether the triangle is valid. |
| **Output** | Message stating whether the triangle is valid or not |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
angle1_in_degrees = float(input("Enter first angle in degrees: "))
angle2_in_degrees = float(input("Enter second angle in degrees: "))
angle3_in_degrees = float(input("Enter third angle in degrees: "))
```

**Program structure** (fill in the blanks — do not copy a finished condition):

```python
if ____:  # check whether the triangle is valid
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is valid")
else:
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is not valid")
```

> **Note on units:** Ask for angles in **degrees** in the `input()` message.

### Example

| Item | Details |
|------|---------|
| **Example input** | `angle1_in_degrees = 60`, `angle2_in_degrees = 60`, `angle3_in_degrees = 60` |
| **Example calculation** | All angles > 0 → True<br>`60 + 60 + 60 = 180` → True<br>So the triangle is valid |
| **Example output** | The triangle is valid |

**Another example (invalid):** `angle1_in_degrees = 90`, `angle2_in_degrees = 90`, `angle3_in_degrees = 90` → sum = 270 ≠ 180 → The triangle is not valid
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-2"></a>

## Unit 2A Task 2: Voting eligibility

Checks whether a person is eligible to vote using if-else. Decide the eligibility rule from the problem statement and class notes.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `age_in_years` |
| **Process** | Use an `if-else` structure. Write your own condition to decide eligibility. |
| **Output** | Message stating whether the person is eligible to vote or not |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
age_in_years = int(input("Enter age in years: "))
```

**Program structure** (fill in the blanks — do not copy a finished condition):

```python
if ____:  # check voting eligibility (use age_in_years)
    print(f"Age {age_in_years} years: Eligible to vote")
else:
    print(f"Age {age_in_years} years: Not eligible to vote")
```

> **Note on units:** Ask for age in **years** in the `input()` message.

### Example

| Item | Details |
|------|---------|
| **Example input** | `age_in_years = 20` |
| **Example calculation** | `20 >= 18` → True → Eligible to vote |
| **Example output** | Eligible to vote |

**Another example:** `age_in_years = 16` → `16 >= 18` → False → Not eligible to vote
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-3"></a>

## Unit 2A Task 3: Positive, negative, or zero

Checks whether a given number is positive, negative, or zero.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `number` |
| **Process** | Use an `if-elif-else` structure. Write your own conditions for positive, negative, and zero. |
| **Output** | Message stating whether the number is positive, negative, or zero |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = float(input("Enter a number: "))
```

**Program structure** (fill in the blanks — do not copy finished conditions):

```python
if ____:  # positive number?
    print(f"The number {number} is positive")
elif ____:  # negative number?
    print(f"The number {number} is negative")
else:
    print(f"The number {number} is zero")  # remaining case
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 15` |
| **Example calculation** | `15 > 0` → True → Positive |
| **Example output** | The number is positive |

**Other examples:** `number = -7` → The number is negative; `number = 0` → The number is zero
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-5"></a>

## Unit 2A Task 5: Largest of three numbers (nested if)

Finds the largest of three numbers using nested `if`. Only one inner block runs — the side that won the outer compare.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | three numbers `x`, `y`, `z` |
| **Process** | **Outer if:** compare `x` and `y` (`x >= y`).<br>**Outer else:** when `x < y`.<br>**Inner under if:** compare `x` with `z` → `largest = x` or `z`.<br>**Inner under else:** compare `y` with `z` → `largest = y` or `z`.<br>Store that winner in `largest`, then print it. |
| **Output** | `Largest = … (among x, y, z)` |

**Process columns** (nested structure):

| If `x >= y` | Else (`x < y`) |
|-------------|----------------|
| Compare `x` with `z` (`x >= z`). | Compare `y` with `z` (`y >= z`). |
| True → `largest = x`. | True → `largest = y`. |
| False → `largest = z`. | False → `largest = z`. |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
```

**Program structure** (fill in the blanks — nested if):

```python
if ____:  # outer: compare x with y
    if ____:  # inner under if: compare x with z
        largest = ____  # x wins
    else:
        largest = ____  # z wins on this side
else:
    if ____:  # inner under else: compare y with z
        largest = ____  # y wins
    else:
        largest = ____  # z wins on this side

print(f"Largest = {largest} (among {x}, {y}, {z})")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `x = 10`, `y = 25`, `z = 7` |
| **Example calculation** | `10 >= 25` → False → outer else → `25 >= 7` → True → `largest = 25` |
| **Example output** | `Largest = 25 (among 10, 25, 7)` |

**Another example:** `x = 9`, `y = 9`, `z = 4` → `9 >= 9` → True → `9 >= 4` → True → `Largest = 9 (among 9, 9, 4)`
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-1"></a>

## Unit 2A Task 7: Leap year — Approach 1 (nested if-else)

Checks whether a year is a leap year using nested `if-else`. Write the conditions yourself; only the nesting structure is shown.

**What is a leap year?**
- A normal year has `365` days
- A leap year has `366` days (February has one extra day)
- Leap years follow simple calendar rules using divisible checks (`%`)

**How to check if a year is a leap year?**
- If the year is divisible by `400` → it **is** a leap year (example: `2000`)
- Else if the year is divisible by `100` → it is **not** a leap year (example: `1900`)
- Else if the year is divisible by `4` → it **is** a leap year (example: `2024`)
- Else → it is **not** a leap year (example: `2023`)

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Use nested `if-else`. Fill in each condition using the leap-year rules from class notes. |
| **Output** | Message stating whether the year is a leap year or not |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
year = int(input("Enter a year: "))
```

**Program structure** (fill in the blanks — nested if-else):

```python
if ____:  # outer leap-year check
    print(f"{year} is a leap year")
else:
    if ____:  # nested check
        print(f"{year} is not a leap year")
    else:
        if ____:  # innermost check
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `year = 2000` |
| **Example calculation** | `2000 % 400 == 0` → True → Leap year |
| **Example output** | `2000 is a leap year` |

**Other examples:** `1900` → Not a leap year; `2024` → Leap year; `2023` → Not a leap year
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-2"></a>

## Unit 2A Task 7: Leap year — Approach 2 (if-elif-else ladder)

Checks whether a year is a leap year using an `if-elif-else` ladder. Write each condition yourself.

**What is a leap year?**
- A normal year has `365` days
- A leap year has `366` days (February has one extra day)
- Leap years follow simple calendar rules using divisible checks (`%`)

**How to check if a year is a leap year?**
- If the year is divisible by `400` → it **is** a leap year (example: `2000`)
- Else if the year is divisible by `100` → it is **not** a leap year (example: `1900`)
- Else if the year is divisible by `4` → it **is** a leap year (example: `2024`)
- Else → it is **not** a leap year (example: `2023`)

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Use `if` / `elif` / `else`. Fill in each condition using the leap-year rules from class notes. |
| **Output** | Message stating whether the year is a leap year or not |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
year = int(input("Enter a year: "))
```

**Program structure** (fill in the blanks — if-elif-else ladder):

```python
if ____:  # first leap-year condition
    print(f"{year} is a leap year")
elif ____:  # second condition
    print(f"{year} is not a leap year")
elif ____:  # third condition
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `year = 1900` |
| **Example calculation** | `1900 % 400 != 0`<br>`1900 % 100 == 0` → Not a leap year |
| **Example output** | `1900 is not a leap year` |

**Other examples:** `2000` → Leap year; `2024` → Leap year; `2023` → Not a leap year
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-3"></a>

## Unit 2A Task 7: Leap year — Approach 3 (single if condition)

Checks whether a year is a leap year using one combined condition with `or` / `and`. Write that condition yourself.

**What is a leap year?**
- A normal year has `365` days
- A leap year has `366` days (February has one extra day)
- Leap years follow simple calendar rules using divisible checks (`%`)

**How to check if a year is a leap year?**
- If the year is divisible by `400` → it **is** a leap year (example: `2000`)
- Else if the year is divisible by `100` → it is **not** a leap year (example: `1900`)
- Else if the year is divisible by `4` → it **is** a leap year (example: `2024`)
- Else → it is **not** a leap year (example: `2023`)

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Use a single `if-else`. Fill in one combined condition using the leap-year rules from class notes. |
| **Output** | Message stating whether the year is a leap year or not |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
year = int(input("Enter a year: "))
```

**Program structure** (fill in the blanks — single if condition):

```python
if ____:  # one combined leap-year condition (use and / or)
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `year = 2024` |
| **Example calculation** | `2024 % 400 != 0`<br>`2024 % 4 == 0` and `2024 % 100 != 0` → True → Leap year |
| **Example output** | `2024 is a leap year` |

**Other examples:** `2000` → Leap year; `1900` → Not a leap year; `2023` → Not a leap year
Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-8"></a>

## Unit 2A Task 8: Prime number check (1 to 100)

Checks whether a given number is prime or not. The input number must be between `1` and `100`.

**What is a prime number?**
- A prime number is a whole number greater than `1`
- It can be divided evenly only by `1` and by itself
- It has no other positive divisors
- Examples: `2`, `3`, `5`, `7`, `11`, `97`
- Not prime: `1` (too small), `4` (divisible by `2`), `9` (divisible by `3`), `100` (divisible by `2`, `4`, `5`, …)

**How to check a number between 1 and 100 (using if-elif only)?**
- First check that the number is from `1` to `100` (inclusive)
- If it is outside that range, print a message
- If the number is `1`, it is **not** prime
- If the number is `2`, `3`, `5`, or `7`, it **is** prime
- Else if the number is divisible by `2`, `3`, `5`, or `7`, it is **not** prime
- Else it **is** prime
- Why only `2`, `3`, `5`, `7`? For numbers up to `100`, these are enough to catch non-primes (no loop needed)

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user (must be between `1` and `100`)

**Process**
- Use an `if-elif-else` ladder
- Check the range, then the prime rules above
- Print the message directly in each branch (do not use a `for` loop)

**Output**
- Show whether the number is prime or not (include the number in the message)
- Or show that the number is outside the allowed range

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number between 1 and 100: "))
```

**Program structure** (fill in the blanks — if-elif-else ladder):

```python
if ____:  # number is outside 1 to 100?
    print(f"{number} is not between 1 and 100")
elif ____:  # 1 is not prime
    print(f"{number} is not a prime number")
elif ____:  # number is 2, 3, 5, or 7?
    print(f"{number} is a prime number")
elif ____:  # divisible by 2, 3, 5, or 7?
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")
```

> **Hint:** Keep it as a simple `if` / `elif` / `else` ladder. Print the message in each branch. Do not use a `for` loop or an `is_prime` flag.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 17` |
| **Example calculation** | `17` is between `1` and `100`<br>Not `1`, not `2/3/5/7`<br>Not divisible by `2`, `3`, `5`, or `7` → prime |
| **Example output** | `17 is a prime number` |

**Other examples:** `1` → not prime; `4` → not prime; `7` → prime; `97` → prime; `120` → not between 1 and 100

<a href="../.faculty/solutions/j5p8wv.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-1-approach-1"></a>

## Unit 2B Task 1: Print numbers from 1 to N — Approach 1 (for loop)

Prints all integers from 1 to N using a `for` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n` from the user

**Process**
- Make a list of numbers from 1 to `n` using the `range` function
- Use a `for` loop to take each number from that list
- Print each number

**Output**
- Show all numbers from 1 to `n`, one on each line

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of N: "))
```

**Program structure** (fill in the blanks — for loop):

```python
for ____ in ____:  # loop variable; use range(...) from 1 to n
    print(f"{____}")  # print the current number
```

> **Hint:** The sequence of numbers from 1 to N can be generated using the `range` function.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Print `1`, then `2`, then `3`, then `4`, then `5` |
| **Example output** | `1`<br>`2`<br>`3`<br>`4`<br>`5` |

<a href="../.faculty/solutions/k7m2xq.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-1-approach-2"></a>

## Unit 2B Task 1: Print numbers from 1 to N — Approach 2 (while loop)

Prints all integers from 1 to N using a `while` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n` from the user

**Process**
- Start a counter with value `1`
- Repeat these steps using a `while` loop while the counter is less than or equal to `n`:
  - Print the counter
  - Add `1` to the counter

**Output**
- Show all numbers from 1 to `n`, one on each line

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of N: "))
```

**Program structure** (fill in the blanks — while loop):

```python
____ = 1  # start a counter from 1

while ____:  # continue while the counter is within 1 to n
    print(f"{____}")  # print the current number
    ____ = ____  # move to the next number
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Counter goes `1 → 2 → 3 → 4 → 5`, printing each value |
| **Example output** | `1`<br>`2`<br>`3`<br>`4`<br>`5` |

<a href="../.faculty/solutions/k7m2xq.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-2-approach-1"></a>

## Unit 2B Task 2: Multiplication table — Approach 1 (for loop)

Prints the multiplication table of a given number using a `for` loop (usually from 1 to 10).

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user (the number for the table)

**Process**
- Make a list of multipliers from 1 to 10 using the `range` function
- Use a `for` loop to take each multiplier from that list
- Multiply the given number by the multiplier
- Print the result in the form: `number x multiplier = product`

**Output**
- Show the multiplication table of the given number from 1 to 10

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — for loop):

```python
for ____ in ____:  # multiplier; use range(...) for 1 to 10
    ____ = ____  # multiply number by the current multiplier
    print(f"{number} x {____} = {____}")  # show number, multiplier, and product
```

> **Hint:** The sequence of multipliers can be generated using the `range` function.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | `5 × 1 = 5`<br>`5 × 2 = 10`<br>…<br>`5 × 10 = 50` |
| **Example output** | `5 x 1 = 5`<br>`5 x 2 = 10`<br>`5 x 3 = 15`<br>`5 x 4 = 20`<br>`5 x 5 = 25`<br>`5 x 6 = 30`<br>`5 x 7 = 35`<br>`5 x 8 = 40`<br>`5 x 9 = 45`<br>`5 x 10 = 50` |

<a href="../.faculty/solutions/p4n9rw.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-2-approach-2"></a>

## Unit 2B Task 2: Multiplication table — Approach 2 (while loop)

Prints the multiplication table of a given number using a `while` loop (usually from 1 to 10).

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user (the number for the table)

**Process**
- Start a counter with value `1`
- Repeat these steps using a `while` loop while the counter is less than or equal to `10`:
  - Multiply the given number by the counter
  - Print the result in the form: `number x counter = product`
  - Add `1` to the counter

**Output**
- Show the multiplication table of the given number from 1 to 10

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
____ = 1  # start multiplier from 1

while ____:  # continue while multiplier is within 1 to 10
    ____ = ____  # multiply number by the current multiplier
    print(f"{number} x {____} = {____}")  # show number, multiplier, and product
    ____ = ____  # move to the next multiplier
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | Counter goes `1 → 2 → … → 10`, printing `5 x counter = product` each time |
| **Example output** | `5 x 1 = 5`<br>`5 x 2 = 10`<br>`5 x 3 = 15`<br>`5 x 4 = 20`<br>`5 x 5 = 25`<br>`5 x 6 = 30`<br>`5 x 7 = 35`<br>`5 x 8 = 40`<br>`5 x 9 = 45`<br>`5 x 10 = 50` |

<a href="../.faculty/solutions/p4n9rw.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-3"></a>

## Unit 2B Task 3: Sum and average of N numbers (for loop)

Finds the sum and average of several numbers entered by the user using a `for` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read how many numbers to take (`total_input_numbers`)
- Read `total_input_numbers` numbers from the user, one by one

**Process**
- Set `total_sum` to `0` at the start
- Use a `for` loop that runs `total_input_numbers` times (you can use the `range` function)
- Inside the loop:
  - Read one number
  - Add that number to `total_sum`
- After the loop, find the average: `average = total_sum / total_input_numbers`

**Output**
- Show the sum of the numbers
- Show the average of the numbers

### Sample input and output messages

**Input messages** (use with `input()`):

```python
total_input_numbers = int(input("Enter how many numbers: "))
```

**Program structure** (fill in the blanks — for loop):

```python
total_sum = 0  # start with zero

for ____ in ____:  # repeat total_input_numbers times (use range)
    ____ = float(input("Enter a number: "))  # read each number
    total_sum = ____  # add the number to total_sum

average = ____  # divide total_sum by total_input_numbers

print(f"Sum of {total_input_numbers} numbers is {total_sum}")
print(f"Average of {total_input_numbers} numbers (sum {total_sum}) is {average}")
```

> **Hint:** The loop can run `total_input_numbers` times using the `range` function.

### Example

| Item | Details |
|------|---------|
| **Example input** | `total_input_numbers = 3`<br>numbers: `10`, `20`, `30` |
| **Example calculation** | `total_sum = 10 + 20 + 30 = 60`<br>`average = 60 / 3 = 20` |
| **Example output** | `Sum of 3 numbers is 60`<br>`Average of 3 numbers (sum 60) is 20` |

<a href="../.faculty/solutions/w8c3jt.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-4"></a>

## Unit 2B Task 4: Largest in a series of N numbers (for loop)

Finds the largest number among several numbers entered by the user using a `for` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read how many numbers to take (`total_input_numbers`)
- Read `total_input_numbers` numbers from the user, one by one

**Process**
- Read the first number and store it in `largest`
- Use a `for` loop for the remaining numbers (`total_input_numbers - 1` times)
- Inside the loop:
  - Read the next number
  - If it is greater than `largest`, update `largest`

**Output**
- Show the largest number

### Sample input and output messages

**Input messages** (use with `input()`):

```python
total_input_numbers = int(input("Enter how many numbers: "))
```

**Program structure** (fill in the blanks — for loop):

```python
largest = float(input("Enter a number: "))  # start with the first number

for ____ in ____:  # remaining numbers only (total_input_numbers - 1 times)
    ____ = float(input("Enter a number: "))  # read the next number
    if ____:  # is this number greater than largest?
        largest = ____  # update largest

print(f"Largest among {total_input_numbers} numbers is {largest}")
```

> **Hint:** After storing the first number in `largest`, the loop only needs to run for the remaining `total_input_numbers - 1` values.

### Example

| Item | Details |
|------|---------|
| **Example input** | `total_input_numbers = 4`<br>numbers: `10`, `25`, `7`, `18` |
| **Example calculation** | Start with `largest = 10`<br>Compare `25` → update to `25`<br>Compare `7` → keep `25`<br>Compare `18` → keep `25` |
| **Example output** | `Largest among 4 numbers is 25` |

<a href="../.faculty/solutions/h2v6ys.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-5"></a>

## Unit 2B Task 5: Factorial of a number (for loop)

Finds the factorial of a number using a `for` loop.

**What is a factorial?**
- The factorial of a whole number `n` is written as `n!`
- It means: multiply all whole numbers from `1` up to `n`
- Example: `5! = 1 × 2 × 3 × 4 × 5 = 120`
- Special case: `0! = 1` (by definition)

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Set `factorial` to `1` at the start
- Use a `for` loop to multiply by each integer from `1` to the given number
- After the loop, `factorial` holds the result

**Output**
- Show the factorial of the number

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — for loop):

```python
factorial = 1  # start with 1

for ____ in ____:  # values from 1 to number (use range)
    factorial = ____  # multiply factorial by the current value

print(f"Factorial of {number} is {factorial}")
```

> **Hint:** The numbers to multiply can be generated with `range` from `1` to `number` (inclusive).

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | `1 × 2 × 3 × 4 × 5 = 120` |
| **Example output** | `Factorial of 5 is 120` |

<a href="../.faculty/solutions/m9q4bd.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-6"></a>

## Unit 2B Task 6: Prime numbers from 1 to N (for loop)

Prints all prime numbers between 1 and N using `for` loops.

**What is a prime number?**
- A prime number is a whole number greater than `1`
- It can be divided evenly only by `1` and by itself
- It has no other positive divisors
- Examples: `2`, `3`, `5`, `7`, `11`
- Not prime: `1` (too small), `4` (divisible by `2`), `9` (divisible by `3`)

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n` from the user

**Process**
- Take each candidate number from `2` to `n` (1 is not a prime number)
- For each candidate, check whether it has any divisor other than `1` and itself
- If it has no such divisor, it is prime

**Output**
- Show each prime number between 1 and `n`

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of N: "))
```

**Program structure** (fill in the blanks — for loop):

```python
for ____ in ____:  # each candidate from 2 to n
    is_prime = True  # assume prime until a divisor is found

    for ____ in ____:  # try possible divisors (e.g. 2 to number - 1)
        if ____:  # is number divisible by this divisor?
            is_prime = False
            break

    if is_prime:
        print(f"{____} is a prime number between 1 and {n}")  # print the prime candidate
```

> **Hint:** A prime number is greater than `1` and has no divisors other than `1` and itself. Use nested `for` loops: one for each candidate, one to test divisors.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 10` |
| **Example calculation** | Check `2`, `3`, `4`, …, `10`<br>Primes: `2`, `3`, `5`, `7` |
| **Example output** | `2 is a prime number between 1 and 10`<br>`3 is a prime number between 1 and 10`<br>`5 is a prime number between 1 and 10`<br>`7 is a prime number between 1 and 10` |

<a href="../.faculty/solutions/r5t1zk.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-7"></a>

## Unit 2B Task 7: Fibonacci series up to N terms (for loop)

Prints the Fibonacci series for the first N terms using a `for` loop.

**What is the Fibonacci series?**
- It is a list of numbers that follows a simple rule
- Start with the first two numbers: `0` and `1`
- Each next number is the sum of the two numbers before it
- So: `0`, `1`, then `0 + 1 = 1`, then `1 + 1 = 2`, then `1 + 2 = 3`, and so on
- Example (first 7 terms): `0`, `1`, `1`, `2`, `3`, `5`, `8`

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read how many terms to print (`n`)

**Process**
- Start with the first two Fibonacci values: `0` and `1`
- Use a `for` loop that runs `n` times
- In each iteration:
  - Print the current first value
  - Compute the next term as the sum of the two current values
  - Shift the pair forward for the next iteration

**Output**
- Show the first `n` Fibonacci terms

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter how many terms: "))
```

**Program structure** (fill in the blanks — for loop):

```python
first = 0
second = 1

for ____ in ____:  # repeat n times (use range)
    print(f"Fibonacci series term {____} of {n} terms = {first}")  # term number (1 to n)
    ____ = ____  # next term = first + second
    first = second
    second = ____  # store the next term
```

> **Hint:** Keep two variables for the current pair. After printing `first`, move the pair forward: `first` becomes the old `second`, and `second` becomes their sum.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 7` |
| **Example calculation** | `0`, `1`, `0+1=1`, `1+1=2`, `1+2=3`, `2+3=5`, `3+5=8` |
| **Example output** | `Fibonacci series term 1 of 7 terms = 0`<br>`Fibonacci series term 2 of 7 terms = 1`<br>`Fibonacci series term 3 of 7 terms = 1`<br>`Fibonacci series term 4 of 7 terms = 2`<br>`Fibonacci series term 5 of 7 terms = 3`<br>`Fibonacci series term 6 of 7 terms = 5`<br>`Fibonacci series term 7 of 7 terms = 8` |

<a href="../.faculty/solutions/b6j2qm.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-8"></a>

## Unit 2B Task 8: Sum of digits (while loop)

Finds the sum of digits of a number using a `while` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Keep a copy of the original number (for the final message)
- Set `digit_sum` to `0`
- While the number is greater than `0`:
  - Take the last digit using `% 10`
  - Add that digit to `digit_sum`
  - Remove the last digit using `// 10`
- Do **not** convert the number to a string to get digits

**Output**
- Show the sum of the digits

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number  # keep a copy for the output message
digit_sum = 0

while ____:  # continue while number still has digits
    ____ = ____  # get the last digit with % 10
    digit_sum = ____  # add the digit to digit_sum
    number = ____  # remove the last digit with // 10

print(f"Sum of digits of {original_number} is {digit_sum}")
```

> **Hint:** Peel digits with arithmetic only: `% 10` for the last digit and `// 10` to shorten the number. Avoid string methods for this task.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 123` |
| **Example calculation** | Last digit `3` → sum `3`, number becomes `12`<br>Last digit `2` → sum `5`, number becomes `1`<br>Last digit `1` → sum `6`, number becomes `0` |
| **Example output** | `Sum of digits of 123 is 6` |

<a href="../.faculty/solutions/v3n8wp.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-9"></a>

## Unit 2B Task 9: Count digits (while loop)

Counts how many digits a number has using a `while` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Keep a copy of the original number (for the final message)
- Set `digit_count` to `0`
- Special case: if the number is `0`, it has `1` digit
- Otherwise, while the number is greater than `0`:
  - Add `1` to `digit_count`
  - Remove the last digit using `// 10`
- Do **not** convert the number to a string to count digits

**Output**
- Show how many digits the number has

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number
digit_count = 0

if number == 0:
    digit_count = 1
else:
    while ____:  # continue while number still has digits
        digit_count = ____  # increase the count by 1
        number = ____  # remove the last digit with // 10

print(f"Number of digits in {original_number} is {digit_count}")
```

> **Hint:** Each `// 10` shortens the number by one digit. Count how many times you can do that until the number becomes `0`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 1234` |
| **Example calculation** | `1234 → 123 → 12 → 1 → 0` (four steps) |
| **Example output** | `Number of digits in 1234 is 4` |

<a href="../.faculty/solutions/c4x7la.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-10"></a>

## Unit 2B Task 10: Reverse a number (while loop)

Reverses the digits of a number using a `while` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Keep a copy of the original number
- Set `reversed_number` to `0`
- While the number is greater than `0`:
  - Take the last digit using `% 10`
  - Attach it to `reversed_number` (multiply current reverse by `10`, then add the digit)
  - Remove the last digit using `// 10`
- Do **not** reverse with string slicing

**Output**
- Show the reversed number

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number
reversed_number = 0

while ____:  # continue while number still has digits
    ____ = ____  # get the last digit with % 10
    reversed_number = ____  # build reverse: reversed_number * 10 + digit
    number = ____  # remove the last digit with // 10

print(f"Reverse of {original_number} is {reversed_number}")
```

> **Hint:** Build the reverse from right to left: each new digit becomes the new ones place of `reversed_number`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 1234` |
| **Example calculation** | `0 → 4 → 43 → 432 → 4321` |
| **Example output** | `Reverse of 1234 is 4321` |

<a href="../.faculty/solutions/d9f2mh.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-11"></a>

## Unit 2B Task 11: Armstrong number (while loop)

Checks whether a number is an Armstrong number using a `while` loop.

**What is an Armstrong number?**
- Take each digit of the number
- Raise each digit to the power of how many digits the number has
- Add those powered values together
- If that sum equals the original number, it is an Armstrong number
- Example: `153` has `3` digits, so check `1³ + 5³ + 3³ = 1 + 125 + 27 = 153` → Armstrong
- Another example: `9474` has `4` digits, so each digit is raised to the power `4`

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Keep a copy of the original number
- Count the digits (same idea as Task 9) → store as `digit_count`
- Set `armstrong_sum` to `0`
- Peel each digit again with `% 10` / `// 10`
- Add `digit ** digit_count` to `armstrong_sum`
- Compare `armstrong_sum` with the original number

**Output**
- Say whether the number is an Armstrong number, and show the computed sum

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number

# Step 1: count digits into digit_count (see Task 9 idea)
digit_count = 0
temp = number
____  # write a while loop here to count digits of temp

# Step 2: sum each digit raised to digit_count
armstrong_sum = 0
temp = number
while ____:  # peel digits from temp
    ____ = ____  # last digit with % 10
    armstrong_sum = ____  # add digit ** digit_count
    temp = ____  # remove last digit with // 10

if ____:  # compare armstrong_sum with original_number
    print(
        f"{original_number} is an Armstrong number "
        f"(sum of digits to power {digit_count} is {armstrong_sum})"
    )
else:
    print(
        f"{original_number} is not an Armstrong number "
        f"(sum of digits to power {digit_count} is {armstrong_sum})"
    )
```

> **Hint:**
> - First, use a `while` loop only to **count how many digits** the number has. That count becomes the power (for `153`, the power is `3`).
> - Then, use another `while` loop to **take each digit**, raise it to that power, and **add** the results.
> - You need two loops because you must know the digit count **before** you start raising digits to that power.
> - Use `% 10` and `// 10` only — do not use strings.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 153` |
| **Example calculation** | Digits = `3`<br>`1³ + 5³ + 3³ = 1 + 125 + 27 = 153` |
| **Example output** | `153 is an Armstrong number (sum of digits to power 3 is 153)` |

<a href="../.faculty/solutions/e1g5nk.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-12"></a>

## Unit 2B Task 12: Palindrome number (while loop)

Checks whether a number is a palindrome using a `while` loop.

**What is a palindrome number?**
- A palindrome reads the same from left to right and from right to left
- For a number, reverse its digits and compare with the original
- If both are the same, the number is a palindrome
- Example: `121` → reverse is `121` → palindrome
- Example: `123` → reverse is `321` → not a palindrome

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Keep a copy of the original number
- Reverse the number (same idea as Task 10)
- If the reversed value equals the original, it is a palindrome

**Output**
- Say whether the number is a palindrome, and show the reversed value

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number
reversed_number = 0

while ____:  # reverse digits into reversed_number (see Task 10)
    ____ = ____  # last digit with % 10
    reversed_number = ____  # build reverse: reversed_number * 10 + digit
    number = ____  # remove last digit with // 10

if ____:  # compare reversed_number with original_number
    print(
        f"{original_number} is a palindrome "
        f"(reversed value is {reversed_number})"
    )
else:
    print(
        f"{original_number} is not a palindrome "
        f"(reversed value is {reversed_number})"
    )
```

> **Hint:** A palindrome number reads the same forwards and backwards. Reverse with `%` / `//`, then compare.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 121` |
| **Example calculation** | Reverse of `121` is `121` → equal → palindrome |
| **Example output** | `121 is a palindrome (reversed value is 121)` |

<a href="../.faculty/solutions/f8h3pj.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-13-approach-1"></a>

## Unit 2B Task 13: Break statement — Approach 1 (for loop)

Demonstrates `break` to leave a `for` loop early.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n` (upper limit)

**Process**
- Loop from `1` to `n`
- When the current number becomes `5`, print a break message and stop the loop with `break`
- Otherwise print the current number

**Output**
- Numbers printed before breaking, plus a message that shows where the loop stopped

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print until N, stop early at 5): "))
```

**Program structure** (fill in the blanks — for loop):

```python
for ____ in ____:  # numbers from 1 to n (use range)
    if ____:  # stop when the number is 5
        print(f"Breaking for loop at number {____} (N was {n})")  # current number
        break
    print(f"for loop number = {____} (up to {n})")  # current number
```

> **Hint:** `break` exits the loop immediately. Code after `break` inside that loop body does not run for later values.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 8` |
| **Example calculation** | Print `1`–`4`, then break at `5` (do not print `6`–`8`) |
| **Example output** | `for loop number = 1 (up to 8)` … `for loop number = 4 (up to 8)`<br>`Breaking for loop at number 5 (N was 8)` |

<a href="../.faculty/solutions/g2k6qs.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-13-approach-2"></a>

## Unit 2B Task 13: Break statement — Approach 2 (while loop)

Demonstrates `break` to leave a `while` loop early.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n` (upper limit)

**Process**
- Start a counter at `1`
- While the counter is less than or equal to `n`:
  - If the counter is `5`, print a break message and `break`
  - Otherwise print the counter and add `1`

**Output**
- Numbers printed before breaking, plus a message that shows where the loop stopped

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print until N, stop early at 5): "))
```

**Program structure** (fill in the blanks — while loop):

```python
____ = 1  # start a counter from 1

while ____:  # continue while counter <= n
    if ____:  # stop when counter is 5
        print(f"Breaking while loop at number {____} (N was {n})")  # current counter
        break
    print(f"while loop number = {____} (up to {n})")  # current counter
    ____ = ____  # move to the next number
```

> **Hint:** Same idea as the for-loop version: `break` ends the while loop right away.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 8` |
| **Example calculation** | Print `1`–`4`, then break at `5` |
| **Example output** | `while loop number = 1 (up to 8)` … `while loop number = 4 (up to 8)`<br>`Breaking while loop at number 5 (N was 8)` |

<a href="../.faculty/solutions/g2k6qs.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-14-approach-1"></a>

## Unit 2B Task 14: Continue statement — Approach 1 (for loop)

Demonstrates `continue` to skip the rest of one `for` loop iteration.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n`

**Process**
- Loop from `1` to `n`
- If the number is even, print a skip message and `continue`
- Otherwise print the odd number

**Output**
- Odd numbers from `1` to `n`, plus skip messages for even values

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print 1 to N, skip even numbers): "))
```

**Program structure** (fill in the blanks — for loop):

```python
for ____ in ____:  # numbers from 1 to n (use range)
    if ____:  # is the number even?
        print(f"Skipping even number {____} with continue (N is {n})")  # current number
        continue
    print(f"for loop odd number = {____} (up to {n})")  # current number
```

> **Hint:** `continue` jumps to the next iteration. The print for odd numbers is skipped for that even value.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Print odds `1`, `3`, `5`; skip evens `2`, `4` |
| **Example output** | `for loop odd number = 1 (up to 5)`<br>`Skipping even number 2 with continue (N is 5)` … |

<a href="../.faculty/solutions/h7m1rt.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-14-approach-2"></a>

## Unit 2B Task 14: Continue statement — Approach 2 (while loop)

Demonstrates `continue` to skip the rest of one `while` loop iteration.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n`

**Process**
- Start a counter at `1`
- While the counter is less than or equal to `n`:
  - If even: print skip message, increase the counter, then `continue`
  - If odd: print the number, then increase the counter

**Output**
- Odd numbers from `1` to `n`, plus skip messages for even values

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print 1 to N, skip even numbers): "))
```

**Program structure** (fill in the blanks — while loop):

```python
____ = 1  # start a counter from 1

while ____:  # continue while counter <= n
    if ____:  # is the counter even?
        print(f"Skipping even number {____} with continue (N is {n})")  # current counter
        ____ = ____  # increase counter before continue
        continue
    print(f"while loop odd number = {____} (up to {n})")  # current counter
    ____ = ____  # move to the next number
```

> **Hint:** In a while loop, update the counter **before** `continue`, or the loop may never move past that even value.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Same as Approach 1, using a while loop |
| **Example output** | `while loop odd number = 1 (up to 5)` … |

<a href="../.faculty/solutions/h7m1rt.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-15-approach-1"></a>

## Unit 2B Task 15: Pass statement — Approach 1 (for loop)

Demonstrates `pass` as a placeholder inside a `for` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n`

**Process**
- Loop from `1` to `n`
- If the number is a multiple of `3`, use `pass` (no special logic yet) and print that `pass` was used
- Otherwise print the number normally

**Output**
- A message for multiples of `3` showing `pass`, and normal messages for other numbers

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (use pass for multiples of 3): "))
```

**Program structure** (fill in the blanks — for loop):

```python
for ____ in ____:  # numbers from 1 to n (use range)
    if ____:  # is it a multiple of 3?
        pass  # do nothing here yet
        print(f"Used pass for multiple of 3: {____} (N is {n})")  # current number
    else:
        print(f"for loop number = {____} (up to {n})")  # current number
```

> **Hint:** `pass` is a no-op. It keeps the `if` block valid when you are not ready to write real logic yet.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 6` |
| **Example calculation** | `3` and `6` use `pass`; other values print normally |
| **Example output** | `for loop number = 1 (up to 6)` … `Used pass for multiple of 3: 3 (N is 6)` … |

<a href="../.faculty/solutions/i4n9su.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-15-approach-2"></a>

## Unit 2B Task 15: Pass statement — Approach 2 (while loop)

Demonstrates `pass` as a placeholder inside a `while` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n`

**Process**
- Same idea as Approach 1, using a while loop and a counter

**Output**
- A message for multiples of `3` showing `pass`, and normal messages for other numbers

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (use pass for multiples of 3): "))
```

**Program structure** (fill in the blanks — while loop):

```python
____ = 1  # start a counter from 1

while ____:  # continue while counter <= n
    if ____:  # is it a multiple of 3?
        pass  # do nothing here yet
        print(f"Used pass for multiple of 3: {____} (N is {n})")  # current counter
    else:
        print(f"while loop number = {____} (up to {n})")  # current counter
    ____ = ____  # move to the next number
```

> **Hint:** `pass` does not skip the rest of the loop by itself — unlike `continue`. Here it only fills an empty branch.

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 6` |
| **Example calculation** | Same behaviour as the for-loop version |
| **Example output** | `while loop number = 1 (up to 6)` … `Used pass for multiple of 3: 3 (N is 6)` … |

<a href="../.faculty/solutions/i4n9su.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).
