# Unit III: Lists, Tuples, Sets and Functions — Hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Hints index](README.md) · [Lab tasks for this unit](../lab-tasks/unit3-lists-tuples-sets-and-functions.md)

Jump to a task:

**Unit 3A:** [Task 1](#unit-3a-task-1) · [Task 2](#unit-3a-task-2) · [Task 3](#unit-3a-task-3) · [Task 4](#unit-3a-task-4) · [Task 5](#unit-3a-task-5)

**Unit 3B:** [Task 1](#unit-3b-task-1) · [Task 2](#unit-3b-task-2) · [Task 3](#unit-3b-task-3) · [Task 4](#unit-3b-task-4)

**Unit 3C:** [Task 1](#unit-3c-task-1) · [Task 2](#unit-3c-task-2) · [Task 3](#unit-3c-task-3)

**Unit 3D:** [Task 1](#unit-3d-task-1) · [Task 2](#unit-3d-task-2) · [Task 3](#unit-3d-task-3) · [Task 4](#unit-3d-task-4) · [Task 4a](#unit-3d-task-4a) · [Task 5](#unit-3d-task-5) · [Task 6](#unit-3d-task-6) · [Task 7](#unit-3d-task-7) · [Task 8](#unit-3d-task-8) · [Task 9](#unit-3d-task-9) · [Task 10 (Optional)](#unit-3d-task-10) · [Task 11 (Optional)](#unit-3d-task-11) · [Task 12](#unit-3d-task-12) · [Task 13](#unit-3d-task-13) · [Task 14](#unit-3d-task-14) · [Task 15](#unit-3d-task-15)

---

<a id="unit-3a-task-1"></a>

## Unit 3A Task 1: Create, traverse and display a list

Creates a list, visits each element with a loop, and displays the list.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sample list (fixed in code or read from the user)

**Process**
- Create the list
- Traverse with `for item in list_data`
- Print each item; also print the whole list

**Output**
- Each element on its own line (or labelled), and the full list

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = ____  # e.g. [10, 20, 30, 40]

print("List:", ____)

print("Elements one by one:")
for ____ in ____:  # each item in list_data
    print(____)
```

> **Hint:** `for item in list_data:` visits every value without needing indexes.

### Example

| Item | Details |
|------|---------|
| **Example input** | `list_data = [10, 20, 30, 40]` |
| **Example output** | `List: [10, 20, 30, 40]`<br>`Elements one by one:`<br>`10`<br>`20`<br>`30`<br>`40` |

<a href="../../.faculty/solutions/i2u6vy.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3a-task-2"></a>

## Unit 3A Task 2: List operations

Demonstrates `insert`, `append`, `remove`, `sort`, and `reverse` on a list.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A starting list (fixed in code or read from the user)

**Process**
- Call each required method and print the list after useful steps
- `append(x)` adds at the end; `insert(i, x)` places `x` at index `i`
- `remove(x)` removes the first matching value
- `sort()` sorts in place; `reverse()` reverses in place

**Output**
- The list after each operation (or after the set of operations)

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = ____  # e.g. [3, 1, 4, 1, 5]
print("Original:", ____)

list_data.____(9)  # append 9 at the end
print("After append:", ____)

list_data.____(0, 7)  # insert 7 at index 0
print("After insert:", ____)

list_data.____(1)  # remove first matching 1
print("After remove:", ____)

list_data.____()  # sort ascending
print("After sort:", ____)

list_data.____()  # reverse the list
print("After reverse:", ____)
```

> **Hint:** These methods change the list in place (they do not return a new list).

### Example

| Item | Details |
|------|---------|
| **Example input** | `list_data = [3, 1, 4, 1, 5]` |
| **Example output** | `Original: [3, 1, 4, 1, 5]`<br>`After append: [3, 1, 4, 1, 5, 9]`<br>`After insert: [7, 3, 1, 4, 1, 5, 9]`<br>`After remove: [7, 3, 4, 1, 5, 9]`<br>`After sort: [1, 3, 4, 5, 7, 9]`<br>`After reverse: [9, 7, 5, 4, 3, 1]` |

<a href="../../.faculty/solutions/j3v7wz.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3a-task-3"></a>

## Unit 3A Task 3: Largest and smallest in a list

Finds the largest and smallest values in a list of numbers.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A list of numbers (example: `[12, 5, 28, 9, 17]`)

**Process**
- Use `max(list_data)` and `min(list_data)` (or find them with a loop)

**Output**
- The list, the largest value, and the smallest value

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = ____  # e.g. [12, 5, 28, 9, 17]

largest = ____  # max of list_data
smallest = ____  # min of list_data

print("List:", ____)
print("Largest:", ____)
print("Smallest:", ____)
```

> **Hint:** Built-in `max()` / `min()` work directly on a list of numbers.

### Example

| Item | Details |
|------|---------|
| **Example input** | `list_data = [12, 5, 28, 9, 17]` |
| **Example output** | `List: [12, 5, 28, 9, 17]`<br>`Largest: 28`<br>`Smallest: 5` |

<a href="../../.faculty/solutions/k4w8xa.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3a-task-4"></a>

## Unit 3A Task 4: Remove duplicates from a list

Builds a new list that keeps each value only once (order preserved).

### Analyse the problem: Identify Input, Process and Output

**Input**
- A list that may contain repeated values

**Process**
- Start an empty result list
- For each item: if it is not already in the result, append it
- (Do this with list membership — save the set-based way for Unit 3C Task 3)

**Output**
- Original list and list without duplicates

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = ____  # e.g. [1, 2, 2, 3, 1, 4, 3]
unique = ____  # empty list []

for ____ in ____:  # each item in list_data
    if ____:  # item not already in unique
        unique.____(____)  # append item

print("Original:", ____)
print("Without duplicates:", ____)
```

> **Hint:** `if item not in unique:` skips values you have already kept.

### Example

| Item | Details |
|------|---------|
| **Example input** | `list_data = [1, 2, 2, 3, 1, 4, 3]` |
| **Example output** | `Original: [1, 2, 2, 3, 1, 4, 3]`<br>`Without duplicates: [1, 2, 3, 4]` |

<a href="../../.faculty/solutions/l5x9yb.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3a-task-5"></a>

## Unit 3A Task 5: Matrix operations with nested lists

Stores matrices as nested lists and performs addition (and shows the result).

**What is a nested-list matrix?**
- A matrix is a grid of numbers in rows and columns
- In Python, each **row** is a list; the whole matrix is a list of those row lists
- Example 2×2: `[[1, 2], [3, 4]]` means row 0 is `1 2`, row 1 is `3 4`

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two matrices of the same size (fixed in code or read from the user)

**Process**
- Create an empty result matrix (or build row by row)
- For each row index `i` and column index `j`, add corresponding elements: `a[i][j] + b[i][j]`

**Output**
- Both input matrices and the sum matrix

### Sample input and output messages

**Program structure** (fill in the blanks — matrix addition):

```python
matrix_a = ____  # e.g. [[1, 2], [3, 4]]
matrix_b = ____  # e.g. [[5, 6], [7, 8]]

rows = ____  # len(matrix_a)
cols = ____  # len(matrix_a[0])

result = []
for ____ in ____:  # i in range(rows)
    row = []
    for ____ in ____:  # j in range(cols)
        row.append(____)  # matrix_a[i][j] + matrix_b[i][j]
    result.append(____)

print("Matrix A:", ____)
print("Matrix B:", ____)
print("Sum:", ____)
```

> **Hint:** Outer loop walks rows; inner loop walks columns. Both matrices must have the same shape for addition.

### Example

| Item | Details |
|------|---------|
| **Example input** | `matrix_a = [[1, 2], [3, 4]]`, `matrix_b = [[5, 6], [7, 8]]` |
| **Example output** | `Matrix A: [[1, 2], [3, 4]]`<br>`Matrix B: [[5, 6], [7, 8]]`<br>`Sum: [[6, 8], [10, 12]]` |

<a href="../../.faculty/solutions/m6y0zc.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3b-task-1"></a>

## Unit 3B Task 1: Create and access a tuple

Creates a tuple and accesses elements by index (including the last item).

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sample tuple (fixed in code or read from the user)

**Process**
- Create the tuple with parentheses
- Access with positive and negative indexes; use `len()` for length

**Output**
- The tuple, first item, last item, and length

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
tuple_data = ____  # e.g. ("red", "green", "blue")

print("Tuple:", ____)
print("First:", ____)  # index 0
print("Last:", ____)  # index -1
print("Length:", ____)  # len(tuple_data)
```

> **Hint:** A single-item tuple needs a trailing comma: `(5,)`. Plain `(5)` is just an int in parentheses.

### Example

| Item | Details |
|------|---------|
| **Example input** | `tuple_data = ("red", "green", "blue")` |
| **Example output** | `Tuple: ('red', 'green', 'blue')`<br>`First: red`<br>`Last: blue`<br>`Length: 3` |

<a href="../../.faculty/solutions/n7z1ad.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3b-task-2"></a>

## Unit 3B Task 2: Tuple operations

Demonstrates concatenation (`+`), slicing, and unpacking.

### Analyse the problem: Identify Input, Process and Output

**Input**
- One or two sample tuples

**Process**
- Concatenate with `+`
- Slice with `[start:stop]`
- Unpack into separate variables (number of variables must match length)

**Output**
- Joined tuple, a slice, and the unpacked values

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
tuple_data = ____  # e.g. (1, 2, 3)
tuple_extra = ____  # e.g. (4, 5)

joined = ____  # concatenate with +
print("Joined:", ____)

print("Slice first two:", ____)  # tuple_data[:2]

a, b, c = ____  # unpack tuple_data
print("Unpacked:", ____, ____, ____)
```

> **Hint:** Unpacking `a, b, c = (1, 2, 3)` assigns `a=1`, `b=2`, `c=3` in one step.

### Example

| Item | Details |
|------|---------|
| **Example input** | `tuple_data = (1, 2, 3)`, `tuple_extra = (4, 5)` |
| **Example output** | `Joined: (1, 2, 3, 4, 5)`<br>`Slice first two: (1, 2)`<br>`Unpacked: 1 2 3` |

<a href="../../.faculty/solutions/o8a2be.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3b-task-3"></a>

## Unit 3B Task 3: Swap using tuple unpacking

Swaps two variables with packing and unpacking (no temporary third variable).

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two values (example: `10` and `20`)

**Process**
- Assign `first, second = second, first`

**Output**
- Values before and after the swap

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
first_number = ____  # e.g. 10
second_number = ____  # e.g. 20

print("Before:", ____, ____)

____, ____ = ____, ____  # swap with unpacking

print("After:", ____, ____)
```

> **Hint:** The right-hand side builds a temporary tuple; the left-hand side unpacks it into the two names.

### Example

| Item | Details |
|------|---------|
| **Example input** | `first_number = 10`, `second_number = 20` |
| **Example output** | `Before: 10 20`<br>`After: 20 10` |

<a href="../../.faculty/solutions/p9b3cf.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3b-task-4"></a>

## Unit 3B Task 4: Maximum and minimum in a tuple

Finds the largest and smallest values in a tuple of numbers.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A tuple of numbers

**Process**
- Use `max(tuple_data)` and `min(tuple_data)`

**Output**
- The tuple, maximum, and minimum

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
tuple_data = ____  # e.g. (12, 5, 28, 9, 17)

largest = ____  # max(tuple_data)
smallest = ____  # min(tuple_data)

print("Tuple:", ____)
print("Maximum:", ____)
print("Minimum:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `tuple_data = (12, 5, 28, 9, 17)` |
| **Example output** | `Tuple: (12, 5, 28, 9, 17)`<br>`Maximum: 28`<br>`Minimum: 5` |

<a href="../../.faculty/solutions/q0c4dg.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3c-task-1"></a>

## Unit 3C Task 1: Set creation and basic operations

Creates sets and shows union, intersection, and difference.

**What is a set?**
- An unordered collection of **unique** items written with `{ }`
- Duplicates are stored only once
- Useful for membership tests and combining collections

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two sample sets

**Process**
- Union: all items from both (`|` or `.union()`)
- Intersection: items in both (`&` or `.intersection()`)
- Difference: items in the first but not the second (`-` or `.difference()`)

**Output**
- Both sets and the three operation results

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
set_a = ____  # e.g. {1, 2, 3, 4}
set_b = ____  # e.g. {3, 4, 5, 6}

print("Set A:", ____)
print("Set B:", ____)
print("Union:", ____)  # set_a | set_b
print("Intersection:", ____)  # set_a & set_b
print("Difference (A - B):", ____)  # set_a - set_b
```

> **Hint:** Sets print in no fixed order. Compare results by the items present, not by print order.

### Example

| Item | Details |
|------|---------|
| **Example input** | `set_a = {1, 2, 3, 4}`, `set_b = {3, 4, 5, 6}` |
| **Example output** (items may print in any order) | `Union: {1, 2, 3, 4, 5, 6}`<br>`Intersection: {3, 4}`<br>`Difference (A - B): {1, 2}` |

<a href="../../.faculty/solutions/r1d5eh.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3c-task-2"></a>

## Unit 3C Task 2: Set membership and methods

Tests membership with `in` / `not in`, and uses `add`, `remove`, and `discard`.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sample set and a few values to test or change

**Process**
- Check membership with `in` / `not in`
- `add(x)` inserts `x` if missing
- `remove(x)` deletes `x` (error if missing)
- `discard(x)` deletes `x` if present (no error if missing)

**Output**
- Membership results and the set after each change

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
set_data = ____  # e.g. {10, 20, 30}
print("Set:", ____)

print("20 in set?", ____)  # 20 in set_data
print("40 not in set?", ____)  # 40 not in set_data

set_data.____(40)  # add 40
print("After add:", ____)

set_data.____(10)  # remove 10
print("After remove:", ____)

set_data.____(99)  # discard 99 (safe even if missing)
print("After discard:", ____)
```

> **Hint:** Prefer `discard` when the value might not be present; use `remove` when you expect it to exist.

### Example

| Item | Details |
|------|---------|
| **Example input** | `set_data = {10, 20, 30}` |
| **Example output** (set order may vary) | `20 in set? True`<br>`40 not in set? True`<br>`After add: {10, 20, 30, 40}`<br>`After remove: {20, 30, 40}`<br>`After discard: {20, 30, 40}` |

<a href="../../.faculty/solutions/s2e6fi.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3c-task-3"></a>

## Unit 3C Task 3: Remove duplicates using sets

Converts a list to a set (unique values), then back to a list if needed.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A list with possible duplicates

**Process**
- `set(list_data)` drops duplicates
- Convert back with `list(...)` if you need a list again
- Note: set conversion does **not** guarantee original order

**Output**
- Original list and the unique collection

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = ____  # e.g. [1, 2, 2, 3, 1, 4, 3]

unique_set = ____  # set(list_data)
unique_list = ____  # list(unique_set)

print("Original:", ____)
print("Unique set:", ____)
print("Unique list:", ____)
```

> **Think about it:** Compare with Unit 3A Task 4. The loop version can keep first-seen order; `set(...)` is shorter but order is not guaranteed.

### Example

| Item | Details |
|------|---------|
| **Example input** | `list_data = [1, 2, 2, 3, 1, 4, 3]` |
| **Example output** | `Original: [1, 2, 2, 3, 1, 4, 3]`<br>`Unique set: {1, 2, 3, 4}` (order may vary)<br>`Unique list:` same items as the set |

<a href="../../.faculty/solutions/t3f7gj.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-1"></a>

## Unit 3D Task 1: Rectangle area and perimeter (function)

Defines a function that takes length and breadth, and returns area and perimeter.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Length and breadth of a rectangle

**Process**
- Define a function with two parameters
- Area = length × breadth
- Perimeter = 2 × (length + breadth)
- Return both values (for example as a tuple)

**Output**
- Area and perimeter

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def rectangle_area_perimeter(____, ____):  # length, breadth
    area = ____
    perimeter = ____
    return ____, ____

length = ____  # e.g. 5
breadth = ____  # e.g. 3
area, perimeter = ____(length, breadth)
print("Area:", ____)
print("Perimeter:", ____)
```

> **Hint:** A function can return more than one value: `return a, b`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `length = 5`, `breadth = 3` |
| **Example output** | `Area: 15`<br>`Perimeter: 16` |

<a href="../../.faculty/solutions/u4a8bk.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-2"></a>

## Unit 3D Task 2: Celsius to Fahrenheit (function)

Defines a function that converts Celsius to Fahrenheit and returns the result.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Temperature in Celsius

**Process**
- Formula: Fahrenheit = (Celsius × 9/5) + 32
- Put the formula inside a function and `return` the result

**Output**
- Temperature in Fahrenheit

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def celsius_to_fahrenheit(____):  # celsius
    fahrenheit = ____
    return ____

celsius = ____  # e.g. 37
fahrenheit = ____(celsius)
print("Fahrenheit:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `celsius = 37` |
| **Example output** | `Fahrenheit: 98.6` |

<a href="../../.faculty/solutions/v5b9cl.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-3"></a>

## Unit 3D Task 3: Marks total and average (function)

Defines a function that takes three subject marks and returns total and average.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Marks of three subjects

**Process**
- Total = sum of the three marks
- Average = total / 3
- Return both values

**Output**
- Total and average

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def total_and_average(____, ____, ____):  # mark1, mark2, mark3
    total = ____
    average = ____
    return ____, ____

m1, m2, m3 = ____, ____, ____  # e.g. 80, 70, 90
total, average = ____(m1, m2, m3)
print("Total:", ____)
print("Average:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `80`, `70`, `90` |
| **Example output** | `Total: 240`<br>`Average: 80.0` |

<a href="../../.faculty/solutions/w6c0dm.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-4"></a>

## Unit 3D Task 4: Simple interest with default arguments

Defines a function with a default rate and calls it with and without an explicit rate.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Principal, time, and optionally rate

**Process**
- Simple interest = (principal × time × rate) / 100
- Give `rate` a default value of `5` in the function definition
- Call once without rate (uses default) and once with an explicit rate

**Output**
- Simple interest for each call

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def simple_interest(principal, time, rate=____):  # default rate 5
    return ____  # (principal * time * rate) / 100

print("SI (default rate):", ____(1000, 2))  # uses rate=5
print("SI (rate=8):", ____(1000, 2, ____))  # explicit rate
```

> **Hint:** Parameters with defaults must come after parameters without defaults.

### Example

| Item | Details |
|------|---------|
| **Example input** | principal `1000`, time `2`; calls with default rate and with rate `8` |
| **Example output** | `SI (default rate): 100.0`<br>`SI (rate=8): 160.0` |

<a href="../../.faculty/solutions/x7d1en.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-4a"></a>

## Unit 3D Task 4a: Keyword vs positional arguments (`divide`)

Defines `divide(a, b)` and calls it with keyword arguments and with positional arguments to compare the results.

**What are keyword arguments?**
- You pass values by **parameter name**, for example `divide(b=10, a=20)`
- Order does not matter when names are used
- Positional arguments follow definition order: `divide(10, 20)` means `a=10`, `b=20`

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two numbers used as `a` and `b`

**Process**
- Define `divide(a, b)` that returns `a / b`
- Call with keyword arguments: `divide(b=10, a=20)` → `20 / 10`
- Call with positional arguments: `divide(10, 20)` → `10 / 20`
- Print both results

**Output**
- `2.0` for the keyword call; `0.5` for the positional call

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
# Example: function defined using two parameters
def divide(____, ____):  # a, b are 2 parameters
    return ____

result = divide(____=10, ____=20)  # with keyword arguments
print(result)  # Output: 2.0

result = divide(____, ____)  # positional arguments
print(result)  # Output: 0.5
```

> **Hint:** With keywords, `a` and `b` are matched by name even if the order is swapped.

### Example

| Item | Details |
|------|---------|
| **Example input** | `divide(b=10, a=20)` and `divide(10, 20)` |
| **Example output** | `2.0`<br>`0.5` |

<a href="../../.faculty/solutions/k0q4ra.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-5"></a>

## Unit 3D Task 5: Sum using *args

Defines a function with `*args` that returns the sum of any number of values.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Any number of numeric values passed to the function

**Process**
- `*args` collects positional arguments into a tuple
- Sum the values in `args` and return the result

**Output**
- The sum

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def sum_values(____):  # *args
    total = ____
    for value in ____:
        total = ____
    return ____

print(sum_values(1, 2, 3))
print(sum_values(10, 20, 30, 40))
```

> **Hint:** You may also use `return sum(args)`.

### Example

| Item | Details |
|------|---------|
| **Example input** | `sum_values(1, 2, 3)` and `sum_values(10, 20, 30, 40)` |
| **Example output** | `6`<br>`100` |

<a href="../../.faculty/solutions/b1h5ir.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-6"></a>

## Unit 3D Task 6: print_details with **kwargs

Defines `print_details(**kwargs)` and prints each key–value pair.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Keyword arguments such as name, age, city

**Process**
- `**kwargs` collects keyword arguments into a dictionary
- Loop over `kwargs.items()` and print each pair

**Output**
- Each key and its value

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def print_details(____):  # **kwargs
    for key, value in ____.items():
        print(f"{key}: {value}")

print_details(name="____", age=____, city="____")  # Krishna, 26, Guntur
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `print_details(name="Krishna", age=26, city="Guntur")` |
| **Example output** | `name: Krishna`<br>`age: 26`<br>`city: Guntur` |

<a href="../../.faculty/solutions/y8e2fo.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-7"></a>

## Unit 3D Task 7: shopping_cart with **products

Defines `shopping_cart(**products)`, prints each item with price in ₹, and shows the total.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Product names and prices as keyword arguments

**Process**
- Start `total` at 0
- For each item and price in `products.items()`, print and add to total
- Print the total

**Output**
- Each item with ₹ price, then total

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def shopping_cart(____):  # **products
    total = ____
    print("Items Purchased:")
    for item, price in ____.items():
        print(f"{item}: ₹{price}")
        total = ____
    print(f"Total: ₹{total}")

# multiple keyword arguments
shopping_cart(apple=____, orange=____, mango=____)  # 15, 12, 10
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `shopping_cart(apple=15, orange=12, mango=10)` |
| **Example output** | `Items Purchased:`<br>`apple: ₹15`<br>`orange: ₹12`<br>`mango: ₹10`<br>`Total: ₹37` |

<a href="../../.faculty/solutions/z9f3gp.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-8"></a>

## Unit 3D Task 8: Student details with **kwargs

Defines a function using `**kwargs` to display a student's name and subject marks.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Keyword arguments for name and subject marks

**Process**
- Accept details with `**kwargs`
- Print each key and value (name and marks)

**Output**
- Student details

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def student_details(____):  # **kwargs
    for key, value in ____.items():
        print(f"{key}: {value}")

student_details(name="____", maths=____, science=____)  # e.g. Anu, 85, 90
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `student_details(name="Anu", maths=85, science=90)` |
| **Example output** | `name: Anu`<br>`maths: 85`<br>`science: 90` |

<a href="../../.faculty/solutions/a0g4hq.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-9"></a>

## Unit 3D Task 9: Local does not change global

Shows that a local variable with the same name does not change the global variable.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A global variable (for example `x`)

**Process**
- Inside a function, assign to a variable with the same name (this creates a **local** variable)
- Do not use `global`
- Print the value inside the function and again outside

**Output**
- Local value inside the function; global value unchanged outside

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
x = ____  # e.g. 10

def demo():
    x = ____  # local assignment, e.g. 20
    print("Inside function, x =", ____)

demo()
print("Outside function, x =", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | global `x = 10`; local `x = 20` inside the function |
| **Example output** | `Inside function, x = 20`<br>`Outside function, x = 10` |

<a href="../../.faculty/solutions/d3j7kt.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-10"></a>

## Unit 3D Task 10 (Optional): Global counter increment

Increments a global counter inside a function using the `global` keyword.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A global counter starting at a known value

**Process**
- Declare `global counter` inside the function before changing it
- Increment the counter
- Call the function and print the counter before and after

**Output**
- Counter values showing the update

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
counter = ____  # e.g. 0

def increment():
    ____ counter  # global keyword
    counter = ____
    print("Inside function, counter =", ____)

print("Before:", ____)
increment()
print("After:", ____)
```

> **Hint:** Without `global`, assigning to `counter` inside the function would create a local variable (or cause an error if you read then write).

### Example

| Item | Details |
|------|---------|
| **Example input** | `counter = 0`, then call `increment()` once |
| **Example output** | `Before: 0`<br>`Inside function, counter = 1`<br>`After: 1` |

<a href="../../.faculty/solutions/e4k8lu.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-11"></a>

## Unit 3D Task 11 (Optional): Bank balance global vs local

Uses a global `balance` with a deposit function (`global`), and another function with a local `balance` that does not update the account.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Starting global balance and a deposit amount

**Process**
- `deposit`: use `global balance` and add the amount
- `show_local_balance`: assign a local `balance` (no `global`) so the account is unchanged
- Print the global balance after each call

**Output**
- Balance after deposit; balance still the same after the local-only function

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
balance = ____  # e.g. 1000

def deposit(amount):
    ____ balance
    balance = ____
    print("After deposit, balance =", ____)

def show_local_balance():
    balance = ____  # local only, e.g. 0
    print("Inside local function, balance =", ____)

print("Start:", ____)
deposit(____)  # e.g. 500
print("Account balance:", ____)
show_local_balance()
print("Account balance still:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | start `1000`, deposit `500`, local `balance = 0` |
| **Example output** | `Start: 1000`<br>`After deposit, balance = 1500`<br>`Account balance: 1500`<br>`Inside local function, balance = 0`<br>`Account balance still: 1500` |

<a href="../../.faculty/solutions/f5l9mv.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-12"></a>

## Unit 3D Task 12: Factorial using recursion

Finds the factorial of a number with a recursive function.

**What is factorial?**
- `n!` means multiply all whole numbers from `n` down to `1`
- Example: `5! = 5 × 4 × 3 × 2 × 1 = 120`
- Also: `0! = 1` and `1! = 1`

**What is recursion?**
- A function that calls itself
- Needs a **base case** to stop
- Needs a **recursive case** that moves toward the base case
- For factorial: `n! = n × (n - 1)!`

### Analyse the problem: Identify Input, Process and Output

**Input**
- A non-negative integer `n`

**Process**
- Base case: `0! = 1` and `1! = 1`
- Recursive case: `n! = n × (n - 1)!`

**Output**
- Factorial of `n`

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def factorial(n):
    if n == ____ or n == ____:  # base case
        return ____
    return n * ____(____)  # recursive call

number = ____  # e.g. 5
print("Factorial:", ____(number))
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `number = 5` |
| **Example output** | `Factorial: 120` |

<a href="../../.faculty/solutions/g6m0nw.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-13"></a>

## Unit 3D Task 13: Fibonacci series using recursion

Generates Fibonacci terms using a recursive function for the nth term.

**What is the Fibonacci series?**
- Each term is the **sum of the previous two** terms
- Start with: `0, 1`
- Next terms: `0+1=1`, `1+1=2`, `1+2=3`, `2+3=5`, …
- First 7 terms: `0 1 1 2 3 5 8`

**Recursive rule**
- `fib(0) = 0`
- `fib(1) = 1`
- `fib(k) = fib(k-1) + fib(k-2)`

### Analyse the problem: Identify Input, Process and Output

**Input**
- Number of terms `n`

**Process**
- Recursive definition: `fib(0) = 0`, `fib(1) = 1`, `fib(k) = fib(k-1) + fib(k-2)`
- Loop from `0` to `n-1` and print `fib(i)` for each term

**Output**
- First `n` Fibonacci numbers

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def fib(k):
    if k == ____:
        return ____
    if k == ____:
        return ____
    return ____(____) + ____(____)

n = ____  # e.g. 7
for i in range(____):
    print(____(i), end=" ")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `n = 7` |
| **Example output** | `0 1 1 2 3 5 8` |

<a href="../../.faculty/solutions/h7n1ox.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-14"></a>

## Unit 3D Task 14: GCD using recursion

Finds the GCD of two numbers with the Euclidean algorithm (recursive).

**What is GCD?**
- GCD = Greatest Common Divisor = largest number that divides both numbers exactly
- Example: GCD of 48 and 18 is **6** (because `48 = 6×8` and `18 = 6×3`)

**Euclidean algorithm with remainder**
1. Divide `a` by `b` and take remainder: `r = a % b`
2. Replace: `a ← b`, `b ← r`
3. Repeat until `b` becomes `0`
4. Then GCD is `a`

Example: `gcd(48, 18)`

| Step | a | b | a % b |
|------|---|---|-------|
| 1 | 48 | 18 | 12 |
| 2 | 18 | 12 | 6 |
| 3 | 12 | 6 | 0 |
| 4 | 6 | 0 | stop → GCD = 6 |

Recursive form: `gcd(a, b) = a` if `b == 0`, else `gcd(b, a % b)`.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two integers `a` and `b`

**Process**
- Base case: if `b == 0`, GCD is `a`
- Recursive case: `gcd(a, b) = gcd(b, a % b)`

**Output**
- GCD of the two numbers

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
def gcd(a, b):
    if b == ____:
        return ____
    return ____(____, ____)  # gcd(b, a % b)

x, y = ____, ____  # e.g. 48, 18
print("GCD:", ____(x, y))
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `48`, `18` |
| **Example output** | `GCD: 6` |

<a href="../../.faculty/solutions/i8o2py.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---

<a id="unit-3d-task-15"></a>

## Unit 3D Task 15: Lambda with map, filter, and reduce

Uses lambda functions with `map()`, `filter()`, and `reduce()`.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sample list of numbers

**Process**
- `map`: apply a lambda to every item (for example square each value)
- `filter`: keep items that match a lambda condition (for example even numbers)
- `reduce`: combine items with a lambda (for example sum); import from `functools`

**Output**
- Results of map, filter, and reduce

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
from functools import reduce

numbers = ____  # e.g. [1, 2, 3, 4, 5]

squares = list(map(lambda x: ____, numbers))
evens = list(filter(lambda x: ____, numbers))
total = reduce(lambda a, b: ____, numbers)

print("Squares:", ____)
print("Evens:", ____)
print("Sum:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `numbers = [1, 2, 3, 4, 5]` |
| **Example output** | `Squares: [1, 4, 9, 16, 25]`<br>`Evens: [2, 4]`<br>`Sum: 15` |

<a href="../../.faculty/solutions/j9p3qz.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit3-lists-tuples-sets-and-functions.md).

---
