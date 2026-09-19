# Lab task hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Lab tasks](lab-tasks.md).

Jump to a task: [Unit 1 Task 3](#unit-1-task-3) · [Task 4](#unit-1-task-4) · [Task 5](#unit-1-task-5) · [Task 6](#unit-1-task-6) · [Task 7](#unit-1-task-7) · [Task 8](#unit-1-task-8)

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
