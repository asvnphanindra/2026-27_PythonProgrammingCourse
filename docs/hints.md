# Lab task hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Lab tasks](lab-tasks.md).

Jump to a task:

**Unit 1:** [Task 1](#unit-1-task-1) · [Task 2](#unit-1-task-2) · [Task 3](#unit-1-task-3) · [Task 4](#unit-1-task-4) · [Task 5](#unit-1-task-5) · [Task 6](#unit-1-task-6) · [Task 7](#unit-1-task-7) · [Task 8](#unit-1-task-8) · [Task 9](#unit-1-task-9) · [Task 10](#unit-1-task-10) · [Task 11](#unit-1-task-11) · [Task 12](#unit-1-task-12) · [Task 13](#unit-1-task-13) · [Task 14](#unit-1-task-14) · [Task 15](#unit-1-task-15)

**Unit 2A:** [Task 1](#unit-2a-task-1) · [Task 2](#unit-2a-task-2) · [Task 3](#unit-2a-task-3) · [Task 7 Approach 1](#unit-2a-task-7-approach-1) · [Task 7 Approach 2](#unit-2a-task-7-approach-2) · [Task 7 Approach 3](#unit-2a-task-7-approach-3)

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

Checks whether a triangle is valid when its three angles are given. A triangle is valid if each angle is greater than 0 and the sum of the three angles is 180 degrees.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `angle1_in_degrees`, `angle2_in_degrees`, `angle3_in_degrees` |
| **Process** | Check `angle1_in_degrees > 0 and angle2_in_degrees > 0 and angle3_in_degrees > 0` and `angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180` |
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

**Output messages** (use with `print()`):

```python
if (
    angle1_in_degrees > 0
    and angle2_in_degrees > 0
    and angle3_in_degrees > 0
    and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180
):
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is valid")
else:
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is not valid")
```

> **Note on units:** Ask for angles in **degrees** in the `input()` message.

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-2"></a>

## Unit 2A Task 2: Voting eligibility

Checks whether a person is eligible to vote using if-else. A person is eligible if age is 18 years or more.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `age_in_years` |
| **Process** | If `age_in_years >= 18`, eligible; otherwise not eligible |
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

**Output messages** (use with `print()`):

```python
if age_in_years >= 18:
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
| **Process** | If `number > 0` → positive; elif `number < 0` → negative; else → zero |
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

**Output messages** (use with `print()`):

```python
if number > 0:
    print(f"The number {number} is positive")
elif number < 0:
    print(f"The number {number} is negative")
else:
    print(f"The number {number} is zero")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-1"></a>

## Unit 2A Task 7: Leap year — Approach 1 (nested if-else)

Checks whether a year is a leap year using nested `if-else`.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | Nested checks: divisible by 400 → leap; else if divisible by 100 → not leap; else if divisible by 4 → leap; else → not leap |
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

**Output messages** (use with `print()`):

```python
if year % 400 == 0:
    print(f"{year} is a leap year")
else:
    if year % 100 == 0:
        print(f"{year} is not a leap year")
    else:
        if year % 4 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-2"></a>

## Unit 2A Task 7: Leap year — Approach 2 (if-elif-else ladder)

Checks whether a year is a leap year using an `if-elif-else` ladder.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | `if year % 400 == 0` → leap; `elif year % 100 == 0` → not leap; `elif year % 4 == 0` → leap; `else` → not leap |
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

**Output messages** (use with `print()`):

```python
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

Back to [Lab tasks](lab-tasks.md).

---

<a id="unit-2a-task-7-approach-3"></a>

## Unit 2A Task 7: Leap year — Approach 3 (single if condition)

Checks whether a year is a leap year using one combined condition with `or` / `and`.

### Analyse the problem: Identify Input, Process and Output

| Item | Details |
|------|---------|
| **Input** | `year` |
| **Process** | If `year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)` → leap; else → not leap |
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

**Output messages** (use with `print()`):

```python
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

Back to [Lab tasks](lab-tasks.md).
