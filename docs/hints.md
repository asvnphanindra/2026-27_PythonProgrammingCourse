# Lab task hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Lab tasks](lab-tasks.md).

> **Important:** In the **Process** section and in sample code, hints show only the **structure** (for example `if` / `else` shape). They do **not** give the full logic.  
> Look for placeholders such as `<condition>` or comments like `# TODO: add your logic here` and write your own code in those places. Use the **Example** values to check whether your logic is correct.

Jump to a task:

**Unit 1:** [Task 1](#unit-1-task-1) · [Task 2](#unit-1-task-2) · [Task 3](#unit-1-task-3) · [Task 4](#unit-1-task-4) · [Task 5](#unit-1-task-5) · [Task 6](#unit-1-task-6) · [Task 7](#unit-1-task-7) · [Task 8](#unit-1-task-8) · [Task 9](#unit-1-task-9) · [Task 10](#unit-1-task-10) · [Task 11](#unit-1-task-11) · [Task 12](#unit-1-task-12) · [Task 13](#unit-1-task-13) · [Task 14](#unit-1-task-14) · [Task 15](#unit-1-task-15)

**Unit 2A:** [Task 1](#unit-2a-task-1) · [Task 2](#unit-2a-task-2) · [Task 3](#unit-2a-task-3) · [Task 7 Approach 1](#unit-2a-task-7-approach-1) · [Task 7 Approach 2](#unit-2a-task-7-approach-2) · [Task 7 Approach 3](#unit-2a-task-7-approach-3)

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation** | `sum_of_numbers = 10 + 20 = 30` |
| **Example output** | `sum_of_numbers = 30` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | `square_of_number = 5 ** 2 = 25` |
| **Example output** | `square_of_number = 25` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = float(input("Enter a number: "))
```

**Output messages** (use with `print()`):

```python
print(f"Square of the number is {square_of_number}")
```

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `length_in_cm = 10`, `breadth_in_cm = 5` |
| **Example calculation** | `area_in_square_cm = 10 * 5 = 50`<br>`perimeter_in_cm = 2 * (10 + 5) = 30` |
| **Example output** | `area_in_square_cm = 50`, `perimeter_in_cm = 30` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `temperature_in_celsius = 25` |
| **Example calculation** | `(25 * 9 / 5) + 32 = 77` |
| **Example output** | `temperature_in_fahrenheit = 77` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation (Approach 2)** | `number1 = 10 + 20 = 30`<br>`number2 = 30 - 20 = 10`<br>`number1 = 30 - 10 = 20` |
| **Example output** | `number1 = 20`, `number2 = 10` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `principal_amount_in_rupees = 10000`, `rate_of_interest_in_percent = 5`, `time_in_years = 2` |
| **Example calculation** | `(10000 * 5 * 2) / 100 = 1000` |
| **Example output** | `simple_interest_in_rupees = 1000` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `principal_amount_in_rupees = 10000`, `rate_of_interest_in_percent = 5`, `time_in_years = 2` |
| **Example calculation** | `10000 * (1.05) ** 2 = 11025`<br>`11025 - 10000 = 1025` |
| **Example output** | `total_amount_in_rupees = 11025`, `compound_interest_in_rupees = 1025` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 10` |
| **Example calculation** | `10 * (10 + 1) / 2 = 55` |
| **Example output** | `sum_of_natural_numbers = 55` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of n: "))
```

**Output messages** (use with `print()`):

```python
print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers}")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-9"></a>

## Unit 1 Task 9: Arithmetic operators

Performs arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`) on two numbers and displays the results.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 3` |
| **Example calculation** | `10 + 3 = 13`<br>`10 - 3 = 7`<br>`10 * 3 = 30`<br>`10 / 3 = 3.333...`<br>`10 // 3 = 3`<br>`10 % 3 = 1`<br>`10 ** 3 = 1000` |
| **Example output** | `13`, `7`, `30`, `3.333...`, `3`, `1`, `1000` |

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

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-10"></a>

## Unit 1 Task 10: Relational operators

Compares two numbers using relational operators and prints the Boolean results.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation** | `10 == 20 → False`<br>`10 != 20 → True`<br>`10 > 20 → False`<br>`10 < 20 → True`<br>`10 >= 20 → False`<br>`10 <= 20 → True` |
| **Example output** | `False`, `True`, `False`, `True`, `False`, `True` |

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

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-11"></a>

## Unit 1 Task 11: Logical operators

Demonstrates logical operators `and`, `or`, and `not` using Boolean conditions.

### Example

| Item | Details |
|------|---------|
| **Example input** | `number1 = 10`, `number2 = 20` |
| **Example calculation** | `(10 > 5) and (20 > 15) → True`<br>`(10 > 50) or (20 > 15) → True`<br>`not (10 > 50) → True` |
| **Example output** | `True`, `True`, `True` |

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

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-12"></a>

## Unit 1 Task 12: Identity operators

Demonstrates identity operators `is` and `is not` (whether two names refer to the same object), with both `True` and `False` cases for each operator.

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

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-13"></a>

## Unit 1 Task 13: Membership operators

Demonstrates membership operators `in` and `not in` with the basic Python data types that support membership checks: **string**, **list**, **tuple**, **set**, and **dictionary**.

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

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-14"></a>

## Unit 1 Task 14: Operator precedence and associativity

Shows how operator precedence and associativity decide the order of evaluation in an expression.

### Example

| Item | Details |
|------|---------|
| **Example expressions** | `2 + 3 * 4`<br>`2 ** 3 ** 2`<br>`10 - 4 - 2` |
| **Example calculation** | `2 + 3 * 4 = 2 + 12 = 14` (`*` before `+`)<br>`2 ** 3 ** 2 = 2 ** 9 = 512` (`**` is right-associative)<br>`10 - 4 - 2 = 6 - 2 = 4` (`-` is left-associative) |
| **Example output** | `14`, `512`, `4` |

### Sample input and output messages

This task is usually demonstrated with fixed expressions in code.

```python
print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")
print(f"10 - 4 - 2 = {10 - 4 - 2}")
```

> **Note:** Higher-precedence operators are evaluated first. For the same precedence, associativity decides the order (`**` is right-to-left; most others are left-to-right).

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-1-task-15"></a>

## Unit 1 Task 15: Type conversion (int, float, string)

Demonstrates converting values between `int`, `float`, and `str` using the variable names `str_num`, `float_num`, and `int_num`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `str_num = "25"` |
| **Example calculation** | `int_num = int("25") → 25`<br>`float_num = float("25") → 25.0`<br>`str_num = str(25) → "25"` |
| **Example output** | `int_num = 25`, `float_num = 25.0`, `str_num = "25"` |

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `angle1_in_degrees = 60`, `angle2_in_degrees = 60`, `angle3_in_degrees = 60` |
| **Example calculation** | All angles > 0 → True<br>`60 + 60 + 60 = 180` → True<br>So the triangle is valid |
| **Example output** | The triangle is valid |

**Another example (invalid):** `angle1_in_degrees = 90`, `angle2_in_degrees = 90`, `angle3_in_degrees = 90` → sum = 270 ≠ 180 → The triangle is not valid

### Sample input and output messages

**Input messages** (use with `input()`):

```python
angle1_in_degrees = float(input("Enter first angle in degrees: "))
angle2_in_degrees = float(input("Enter second angle in degrees: "))
angle3_in_degrees = float(input("Enter third angle in degrees: "))
```

**Program structure** (fill in the blanks — do not copy a finished condition):

```python
if <condition>:  # TODO: add your logic here to check if the triangle is valid
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is valid")
else:
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is not valid")
```

> **Note on units:** Ask for angles in **degrees** in the `input()` message.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `age_in_years = 20` |
| **Example calculation** | `20 >= 18` → True → Eligible to vote |
| **Example output** | Eligible to vote |

**Another example:** `age_in_years = 16` → `16 >= 18` → False → Not eligible to vote

### Sample input and output messages

**Input messages** (use with `input()`):

```python
age_in_years = int(input("Enter age in years: "))
```

**Program structure** (fill in the blanks — do not copy a finished condition):

```python
if <condition>:  # TODO: add your logic here to check voting eligibility
    print(f"Age {age_in_years} years: Eligible to vote")
else:
    print(f"Age {age_in_years} years: Not eligible to vote")
```

> **Note on units:** Ask for age in **years** in the `input()` message.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 15` |
| **Example calculation** | `15 > 0` → True → Positive |
| **Example output** | The number is positive |

**Other examples:** `number = -7` → The number is negative; `number = 0` → The number is zero

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = float(input("Enter a number: "))
```

**Program structure** (fill in the blanks — do not copy finished conditions):

```python
if <condition_1>:  # TODO: add your logic for a positive number
    print(f"The number {number} is positive")
elif <condition_2>:  # TODO: add your logic for a negative number
    print(f"The number {number} is negative")
else:
    # TODO: handle the remaining case (zero)
    print(f"The number {number} is zero")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-1"></a>

## Unit 2A Task 7: Leap year — Approach 1 (nested if-else)

Checks whether a year is a leap year using nested `if-else`. Write the conditions yourself; only the nesting structure is shown.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Use nested `if-else`. Fill in each condition using the leap-year rules from class notes. |
| **Output** | Message stating whether the year is a leap year or not |

### Example

| Item | Details |
|------|---------|
| **Example input** | `year = 2000` |
| **Example calculation** | `2000 % 400 == 0` → True → Leap year |
| **Example output** | `2000 is a leap year` |

**Other examples:** `1900` → Not a leap year; `2024` → Leap year; `2023` → Not a leap year

### Sample input and output messages

**Input messages** (use with `input()`):

```python
year = int(input("Enter a year: "))
```

**Program structure** (fill in the blanks — nested if-else):

```python
if <condition_1>:  # TODO: add your logic here
    print(f"{year} is a leap year")
else:
    if <condition_2>:  # TODO: add your logic here
        print(f"{year} is not a leap year")
    else:
        if <condition_3>:  # TODO: add your logic here
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-2"></a>

## Unit 2A Task 7: Leap year — Approach 2 (if-elif-else ladder)

Checks whether a year is a leap year using an `if-elif-else` ladder. Write each condition yourself.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Use `if` / `elif` / `else`. Fill in each condition using the leap-year rules from class notes. |
| **Output** | Message stating whether the year is a leap year or not |

### Example

| Item | Details |
|------|---------|
| **Example input** | `year = 1900` |
| **Example calculation** | `1900 % 400 != 0`<br>`1900 % 100 == 0` → Not a leap year |
| **Example output** | `1900 is not a leap year` |

**Other examples:** `2000` → Leap year; `2024` → Leap year; `2023` → Not a leap year

### Sample input and output messages

**Input messages** (use with `input()`):

```python
year = int(input("Enter a year: "))
```

**Program structure** (fill in the blanks — if-elif-else ladder):

```python
if <condition_1>:  # TODO: add your logic here
    print(f"{year} is a leap year")
elif <condition_2>:  # TODO: add your logic here
    print(f"{year} is not a leap year")
elif <condition_3>:  # TODO: add your logic here
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-3"></a>

## Unit 2A Task 7: Leap year — Approach 3 (single if condition)

Checks whether a year is a leap year using one combined condition with `or` / `and`. Write that condition yourself.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Use a single `if-else`. Fill in one combined condition using the leap-year rules from class notes. |
| **Output** | Message stating whether the year is a leap year or not |

### Example

| Item | Details |
|------|---------|
| **Example input** | `year = 2024` |
| **Example calculation** | `2024 % 400 != 0`<br>`2024 % 4 == 0` and `2024 % 100 != 0` → True → Leap year |
| **Example output** | `2024 is a leap year` |

**Other examples:** `2000` → Leap year; `1900` → Not a leap year; `2023` → Not a leap year

### Sample input and output messages

**Input messages** (use with `input()`):

```python
year = int(input("Enter a year: "))
```

**Program structure** (fill in the blanks — single if condition):

```python
if <condition>:  # TODO: add your combined leap-year logic here (use and / or as needed)
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Print `1`, then `2`, then `3`, then `4`, then `5` |
| **Example output** | `Number = 1 (from 1 to 5)`<br>`Number = 2 (from 1 to 5)`<br>`Number = 3 (from 1 to 5)`<br>`Number = 4 (from 1 to 5)`<br>`Number = 5 (from 1 to 5)` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of N: "))
```

**Program structure** (fill in the blanks — for loop):

```python
for <variable> in <sequence>:  # TODO: use range(...) to generate numbers from 1 to n
    print(f"Number = {<variable>} (from 1 to {n})")  # TODO: print the current number and N
```

> **Hint:** The sequence of numbers from 1 to N can be generated using the `range` function.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Counter goes `1 → 2 → 3 → 4 → 5`, printing each value |
| **Example output** | `Number = 1 (from 1 to 5)`<br>`Number = 2 (from 1 to 5)`<br>`Number = 3 (from 1 to 5)`<br>`Number = 4 (from 1 to 5)`<br>`Number = 5 (from 1 to 5)` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of N: "))
```

**Program structure** (fill in the blanks — while loop):

```python
<counter> = 1  # TODO: start from 1

while <condition>:  # TODO: continue while counter is within 1 to n
    print(f"Number = {<counter>} (from 1 to {n})")  # TODO: print the current number and N
    <counter> = <update>  # TODO: move to the next number
```

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | `5 × 1 = 5`<br>`5 × 2 = 10`<br>…<br>`5 × 10 = 50` |
| **Example output** | `5 x 1 = 5`<br>`5 x 2 = 10`<br>`5 x 3 = 15`<br>`5 x 4 = 20`<br>`5 x 5 = 25`<br>`5 x 6 = 30`<br>`5 x 7 = 35`<br>`5 x 8 = 40`<br>`5 x 9 = 45`<br>`5 x 10 = 50` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — for loop):

```python
for <variable> in <sequence>:  # TODO: use range(...) for multipliers (e.g. 1 to 10)
    <product> = <expression>  # TODO: multiply number by the current multiplier
    print(f"{number} x {<variable>} = {<product>}")
```

> **Hint:** The sequence of multipliers can be generated using the `range` function.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | Counter goes `1 → 2 → … → 10`, printing `5 x counter = product` each time |
| **Example output** | `5 x 1 = 5`<br>`5 x 2 = 10`<br>`5 x 3 = 15`<br>`5 x 4 = 20`<br>`5 x 5 = 25`<br>`5 x 6 = 30`<br>`5 x 7 = 35`<br>`5 x 8 = 40`<br>`5 x 9 = 45`<br>`5 x 10 = 50` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
<counter> = 1  # TODO: start from 1

while <condition>:  # TODO: continue while counter is within 1 to 10
    <product> = <expression>  # TODO: multiply number by the current counter
    print(f"{number} x {<counter>} = {<product>}")
    <counter> = <update>  # TODO: move to the next multiplier
```

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `total_input_numbers = 3`<br>numbers: `10`, `20`, `30` |
| **Example calculation** | `total_sum = 10 + 20 + 30 = 60`<br>`average = 60 / 3 = 20` |
| **Example output** | `Sum of 3 numbers is 60`<br>`Average of 3 numbers (sum 60) is 20` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
total_input_numbers = int(input("Enter how many numbers: "))
```

**Program structure** (fill in the blanks — for loop):

```python
total_sum = 0  # start with zero

for <variable> in <sequence>:  # TODO: use range(...) to repeat total_input_numbers times
    <number> = float(input("Enter a number: "))  # TODO: read each number
    total_sum = <update_sum>  # TODO: add the number to total_sum

average = <expression>  # TODO: divide total_sum by total_input_numbers

print(f"Sum of {total_input_numbers} numbers is {total_sum}")
print(f"Average of {total_input_numbers} numbers (sum {total_sum}) is {average}")
```

> **Hint:** The loop can run `total_input_numbers` times using the `range` function.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `total_input_numbers = 4`<br>numbers: `10`, `25`, `7`, `18` |
| **Example calculation** | Start with `largest = 10`<br>Compare `25` → update to `25`<br>Compare `7` → keep `25`<br>Compare `18` → keep `25` |
| **Example output** | `Largest among 4 numbers is 25` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
total_input_numbers = int(input("Enter how many numbers: "))
```

**Program structure** (fill in the blanks — for loop):

```python
largest = float(input("Enter a number: "))  # start with the first number

for <variable> in <sequence>:  # TODO: use range(...) for the remaining numbers
    <number> = float(input("Enter a number: "))  # TODO: read the next number
    if <condition>:  # TODO: check whether number is greater than largest
        largest = <number>  # TODO: update largest

print(f"Largest among {total_input_numbers} numbers is {largest}")
```

> **Hint:** After storing the first number in `largest`, the loop only needs to run for the remaining `total_input_numbers - 1` values.

<a href="../.faculty/solutions/h2v6ys.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-5"></a>

## Unit 2B Task 5: Factorial of a number (for loop)

Finds the factorial of a number using a `for` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Set `factorial` to `1` at the start
- Use a `for` loop to multiply by each integer from `1` to the given number
- After the loop, `factorial` holds the result

**Output**
- Show the factorial of the number

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example calculation** | `1 × 2 × 3 × 4 × 5 = 120` |
| **Example output** | `Factorial of 5 is 120` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — for loop):

```python
factorial = 1  # start with 1

for <variable> in <sequence>:  # TODO: use range(...) for values from 1 to number
    factorial = <update>  # TODO: multiply factorial by the current value

print(f"Factorial of {number} is {factorial}")
```

> **Hint:** The numbers to multiply can be generated with `range` from `1` to `number` (inclusive).

<a href="../.faculty/solutions/m9q4bd.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-6"></a>

## Unit 2B Task 6: Prime numbers from 1 to N (for loop)

Prints all prime numbers between 1 and N using `for` loops.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number `n` from the user

**Process**
- Take each candidate number from `2` to `n` (1 is not a prime number)
- For each candidate, check whether it has any divisor other than `1` and itself
- If it has no such divisor, it is prime

**Output**
- Show each prime number between 1 and `n`

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 10` |
| **Example calculation** | Check `2`, `3`, `4`, …, `10`<br>Primes: `2`, `3`, `5`, `7` |
| **Example output** | `2 is a prime number between 1 and 10`<br>`3 is a prime number between 1 and 10`<br>`5 is a prime number between 1 and 10`<br>`7 is a prime number between 1 and 10` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter the value of N: "))
```

**Program structure** (fill in the blanks — for loop):

```python
for <number> in <sequence>:  # TODO: use range(...) for candidates from 2 to n
    is_prime = True  # assume prime until a divisor is found

    for <divisor> in <inner_sequence>:  # TODO: try possible divisors (e.g. from 2 up to number - 1)
        if <condition>:  # TODO: check whether number is divisible by divisor
            is_prime = False
            break

    if is_prime:
        print(f"{<number>} is a prime number between 1 and {n}")
```

> **Hint:** A prime number is greater than `1` and has no divisors other than `1` and itself. Use nested `for` loops: one for each candidate, one to test divisors.

<a href="../.faculty/solutions/r5t1zk.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-7"></a>

## Unit 2B Task 7: Fibonacci series up to N terms (for loop)

Prints the Fibonacci series for the first N terms using a `for` loop.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 7` |
| **Example calculation** | `0`, `1`, `0+1=1`, `1+1=2`, `1+2=3`, `2+3=5`, `3+5=8` |
| **Example output** | `Term 1 of 7 is 0`<br>`Term 2 of 7 is 1`<br>`Term 3 of 7 is 1`<br>`Term 4 of 7 is 2`<br>`Term 5 of 7 is 3`<br>`Term 6 of 7 is 5`<br>`Term 7 of 7 is 8` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter how many terms: "))
```

**Program structure** (fill in the blanks — for loop):

```python
first = 0
second = 1

for <variable> in <sequence>:  # TODO: use range(...) to repeat n times
    print(f"Term {<term_number>} of {n} is {first}")
    <next_term> = <expression>  # TODO: add first and second
    first = second
    second = <next_term>
```

> **Hint:** Keep two variables for the current pair. After printing `first`, move the pair forward: `first` becomes the old `second`, and `second` becomes their sum.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 123` |
| **Example calculation** | Last digit `3` → sum `3`, number becomes `12`<br>Last digit `2` → sum `5`, number becomes `1`<br>Last digit `1` → sum `6`, number becomes `0` |
| **Example output** | `Sum of digits of 123 is 6` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number  # keep a copy for the output message
digit_sum = 0

while <condition>:  # TODO: continue while number still has digits
    <digit> = <expression>  # TODO: get the last digit with % 10
    digit_sum = <update>  # TODO: add the digit to digit_sum
    number = <update>  # TODO: remove the last digit with // 10

print(f"Sum of digits of {original_number} is {digit_sum}")
```

> **Hint:** Peel digits with arithmetic only: `% 10` for the last digit and `// 10` to shorten the number. Avoid string methods for this task.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 1234` |
| **Example calculation** | `1234 → 123 → 12 → 1 → 0` (four steps) |
| **Example output** | `Number of digits in 1234 is 4` |

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
    while <condition>:  # TODO: continue while number still has digits
        digit_count = <update>  # TODO: increase the count by 1
        number = <update>  # TODO: remove the last digit with // 10

print(f"Number of digits in {original_number} is {digit_count}")
```

> **Hint:** Each `// 10` shortens the number by one digit. Count how many times you can do that until the number becomes `0`.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 1234` |
| **Example calculation** | `0 → 4 → 43 → 432 → 4321` |
| **Example output** | `Reverse of 1234 is 4321` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number
reversed_number = 0

while <condition>:  # TODO: continue while number still has digits
    <digit> = <expression>  # TODO: get the last digit with % 10
    reversed_number = <update>  # TODO: build reverse as reversed_number * 10 + digit
    number = <update>  # TODO: remove the last digit with // 10

print(f"Reverse of {original_number} is {reversed_number}")
```

> **Hint:** Build the reverse from right to left: each new digit becomes the new ones place of `reversed_number`.

<a href="../.faculty/solutions/d9f2mh.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-11"></a>

## Unit 2B Task 11: Armstrong number (while loop)

Checks whether a number is an Armstrong number using a `while` loop.

An Armstrong number equals the sum of its digits each raised to the power of the digit count (example: `153 = 1³ + 5³ + 3³`).

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 153` |
| **Example calculation** | Digits = `3`<br>`1³ + 5³ + 3³ = 1 + 125 + 27 = 153` |
| **Example output** | `153 is an Armstrong number (sum of digits to power 3 is 153)` |

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
# TODO: count digits of temp into digit_count

# Step 2: sum each digit raised to digit_count
armstrong_sum = 0
temp = number
while <condition>:  # TODO: peel digits from temp
    <digit> = <expression>  # TODO: last digit with % 10
    armstrong_sum = <update>  # TODO: add digit ** digit_count
    temp = <update>  # TODO: remove last digit with // 10

if <condition>:  # TODO: compare armstrong_sum with original_number
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

> **Hint:** You usually need two while-loop passes: one to count digits (the power), one to build the powered digit sum. Use `%` and `//` only — no strings.

<a href="../.faculty/solutions/e1g5nk.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2b-task-12"></a>

## Unit 2B Task 12: Palindrome number (while loop)

Checks whether a number is a palindrome using a `while` loop.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Read a number from the user

**Process**
- Keep a copy of the original number
- Reverse the number (same idea as Task 10)
- If the reversed value equals the original, it is a palindrome

**Output**
- Say whether the number is a palindrome, and show the reversed value

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 121` |
| **Example calculation** | Reverse of `121` is `121` → equal → palindrome |
| **Example output** | `121 is a palindrome (reversed value is 121)` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
number = int(input("Enter a number: "))
```

**Program structure** (fill in the blanks — while loop):

```python
original_number = number
reversed_number = 0

while <condition>:  # TODO: reverse digits into reversed_number (see Task 10)
    <digit> = <expression>
    reversed_number = <update>
    number = <update>

if <condition>:  # TODO: compare reversed_number with original_number
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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 8` |
| **Example calculation** | Print `1`–`4`, then break at `5` (do not print `6`–`8`) |
| **Example output** | `for loop number = 1 (up to 8)` … `for loop number = 4 (up to 8)`<br>`Breaking for loop at number 5 (N was 8)` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print until N, stop early at 5): "))
```

**Program structure** (fill in the blanks — for loop):

```python
for <variable> in <sequence>:  # TODO: range from 1 to n
    if <condition>:  # TODO: stop when the number is 5
        print(f"Breaking for loop at number {<variable>} (N was {n})")
        break
    print(f"for loop number = {<variable>} (up to {n})")
```

> **Hint:** `break` exits the loop immediately. Code after `break` inside that loop body does not run for later values.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 8` |
| **Example calculation** | Print `1`–`4`, then break at `5` |
| **Example output** | `while loop number = 1 (up to 8)` … `while loop number = 4 (up to 8)`<br>`Breaking while loop at number 5 (N was 8)` |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print until N, stop early at 5): "))
```

**Program structure** (fill in the blanks — while loop):

```python
<counter> = 1

while <condition>:  # TODO: continue while counter <= n
    if <stop_condition>:  # TODO: stop when counter is 5
        print(f"Breaking while loop at number {<counter>} (N was {n})")
        break
    print(f"while loop number = {<counter>} (up to {n})")
    <counter> = <update>
```

> **Hint:** Same idea as the for-loop version: `break` ends the while loop right away.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Print odds `1`, `3`, `5`; skip evens `2`, `4` |
| **Example output** | `for loop odd number = 1 (up to 5)`<br>`Skipping even number 2 with continue (N is 5)` … |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print 1 to N, skip even numbers): "))
```

**Program structure** (fill in the blanks — for loop):

```python
for <variable> in <sequence>:  # TODO: range from 1 to n
    if <condition>:  # TODO: detect an even number
        print(f"Skipping even number {<variable>} with continue (N is {n})")
        continue
    print(f"for loop odd number = {<variable>} (up to {n})")
```

> **Hint:** `continue` jumps to the next iteration. The print for odd numbers is skipped for that even value.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 5` |
| **Example calculation** | Same as Approach 1, using a while loop |
| **Example output** | `while loop odd number = 1 (up to 5)` … |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (print 1 to N, skip even numbers): "))
```

**Program structure** (fill in the blanks — while loop):

```python
<counter> = 1

while <condition>:  # TODO: counter <= n
    if <even_condition>:  # TODO: even check
        print(f"Skipping even number {<counter>} with continue (N is {n})")
        <counter> = <update>  # TODO: important before continue
        continue
    print(f"while loop odd number = {<counter>} (up to {n})")
    <counter> = <update>
```

> **Hint:** In a while loop, update the counter **before** `continue`, or the loop may never move past that even value.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 6` |
| **Example calculation** | `3` and `6` use `pass`; other values print normally |
| **Example output** | `for loop number = 1 (up to 6)` … `Used pass for multiple of 3: 3 (N is 6)` … |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (use pass for multiples of 3): "))
```

**Program structure** (fill in the blanks — for loop):

```python
for <variable> in <sequence>:  # TODO: range from 1 to n
    if <condition>:  # TODO: multiple of 3
        pass  # placeholder: do nothing here yet
        print(f"Used pass for multiple of 3: {<variable>} (N is {n})")
    else:
        print(f"for loop number = {<variable>} (up to {n})")
```

> **Hint:** `pass` is a no-op. It keeps the `if` block valid when you are not ready to write real logic yet.

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

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 6` |
| **Example calculation** | Same behaviour as the for-loop version |
| **Example output** | `while loop number = 1 (up to 6)` … `Used pass for multiple of 3: 3 (N is 6)` … |

### Sample input and output messages

**Input messages** (use with `input()`):

```python
n = int(input("Enter N (use pass for multiples of 3): "))
```

**Program structure** (fill in the blanks — while loop):

```python
<counter> = 1

while <condition>:  # TODO: counter <= n
    if <condition>:  # TODO: multiple of 3
        pass
        print(f"Used pass for multiple of 3: {<counter>} (N is {n})")
    else:
        print(f"while loop number = {<counter>} (up to {n})")
    <counter> = <update>
```

> **Hint:** `pass` does not skip the rest of the loop by itself — unlike `continue`. Here it only fills an empty branch.

<a href="../.faculty/solutions/i4n9su.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](lab-tasks.md).
