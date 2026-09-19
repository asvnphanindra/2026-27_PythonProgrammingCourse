# Lab task hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Jump to a task: [Unit 1 Task 4](#unit-1-task-4) · [Task 5](#unit-1-task-5) · [Task 6](#unit-1-task-6) · [Task 7](#unit-1-task-7) · [Task 8](#unit-1-task-8)

> **Note for students:** Always focus on the **units** of the input data when you ask the user for values. Your `input()` message must be clear so the user knows exactly what to enter.
>
> **Good:** `Enter principal amount in rupees: `  
> **Unclear:** `Enter principal: `
>
> State the unit in the prompt (for example: Celsius, rupees, percent, years). This avoids mistakes and makes your program easier to use and test.

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
