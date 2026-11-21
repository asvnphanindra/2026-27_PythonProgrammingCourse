# Unit IV: Dictionaries, Exception Handling and File Handling — Hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Hints index](README.md) · [Lab tasks for this unit](../lab-tasks/unit4-dictionaries-and-exception-handling.md)

Jump to a task:

**Unit 4A:** [Task 1](#unit-4a-task-1) · [Task 2](#unit-4a-task-2) · [Task 3](#unit-4a-task-3) · [Task 4](#unit-4a-task-4) · [Task 5](#unit-4a-task-5) · [Task 6](#unit-4a-task-6) · [Task 7](#unit-4a-task-7) · [Task 8](#unit-4a-task-8) · [Task 9](#unit-4a-task-9) · [Task 10](#unit-4a-task-10)

**Unit 4B:** [Task 1](#unit-4b-task-1) · [Task 2](#unit-4b-task-2) · [Task 3](#unit-4b-task-3) · [Task 4](#unit-4b-task-4) · [Task 5](#unit-4b-task-5) · [Task 6](#unit-4b-task-6) · [Task 7](#unit-4b-task-7)

**Unit 4C:** [Task 1](#unit-4c-task-1) · [Task 2](#unit-4c-task-2) · [Task 3](#unit-4c-task-3) · [Task 4](#unit-4c-task-4) · [Task 5](#unit-4c-task-5)

---

<a id="unit-4a-task-1"></a>

## Unit 4A Task 1: Create a student dictionary, update age, and add city

Creates a dictionary, reads values by key, and updates or adds entries.

**What is a dictionary?**
- A collection of **key–value** pairs written with `{ }`
- Keys are usually unique; look up a value with `dict[key]`
- Useful for labelled data (name → value)

### Analyse the problem: Identify Input, Process and Output

**Input**
- Sample keys and values (for example student details)

**Process**
- Create a dictionary with `{ key: value, ... }`
- Access a value with `d[key]` or `d.get(key)`
- Update an existing key with assignment; add a new key the same way

**Output**
- Dictionary before and after updates, plus selected values

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
dict_data = {
    "name": ____,  # e.g. "Anu"
    "age": ____,  # e.g. 20
    "course": ____,  # e.g. "Python"
}
print("Student:", ____)
print("Name:", dict_data[____])

dict_data[____] = ____  # update age, e.g. 21
dict_data[____] = ____  # add a new key, e.g. "city": "Guntur"
print("Updated:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `name="Anu"`, `age=20`, then set `age=21`, add `city="Guntur"` |
| **Example output** | `Student: {'name': 'Anu', 'age': 20, 'course': 'Python'}`<br>`Name: Anu`<br>`Updated: {'name': 'Anu', 'age': 21, 'course': 'Python', 'city': 'Guntur'}` |

<a href="../../.faculty/solutions/l1r5sb.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-2"></a>

## Unit 4A Task 2: Use keys, values, items, get, update and pop

Demonstrates `keys`, `values`, `items`, `get`, `update`, and `pop`.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sample dictionary

**Process**
- `keys()` — all keys
- `values()` — all values
- `items()` — key–value pairs
- `get(key)` — value or `None` if missing (no error)
- `update({...})` — merge/overwrite entries
- `pop(key)` — remove a key and return its value

**Output**
- Results of each method

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
dict_data = {"a": 1, "b": 2, "c": 3}
print("Keys:", ____)  # dict_data.keys()
print("Values:", ____)
print("Items:", ____)
print("get b:", dict_data.____("b"))
print("get z:", dict_data.____("z"))  # missing key

dict_data.____({"b": 20, "d": 4})  # update
print("After update:", ____)

removed = dict_data.____("a")  # pop
print("Removed:", ____)
print("After pop:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `dict_data = {"a": 1, "b": 2, "c": 3}` |
| **Example output** | `Keys: dict_keys(['a', 'b', 'c'])`<br>`get b: 2`<br>`get z: None`<br>`After update:` includes `b: 20` and `d: 4`<br>`Removed: 1` |

<a href="../../.faculty/solutions/m2s6tc.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-3"></a>

## Unit 4A Task 3: Count word frequency in a sentence

Counts how many times each word appears in a sentence.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sentence (string)

**Process**
- Split the sentence into words (`split()`)
- For each word, increase its count in a dictionary
- Use `dict_data.get(word, 0) + 1` or check membership

**Output**
- Dictionary of word → count

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
sentence = ____  # e.g. "to be or not to be"
words = sentence.____()  # split into words
dict_data = {}

for word in words:
    dict_data[word] = dict_data.____(word, 0) + 1

print("Frequency:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `"to be or not to be"` |
| **Example output** | `Frequency: {'to': 2, 'be': 2, 'or': 1, 'not': 1}` |

<a href="../../.faculty/solutions/n3t7ud.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-4"></a>

## Unit 4A Task 4: Nested student dictionary (name and marks)

Creates a dictionary whose values are dictionaries, then accesses nested values.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Nested structure (for example students → details)

**Process**
- Outer key selects an inner dictionary
- Access with `outer[key1][key2]`

**Output**
- Selected nested values and/or the full structure

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
dict_data = {
    "S1": {"name": ____, "marks": ____},  # e.g. "Ram", 85
    "S2": {"name": ____, "marks": ____},  # e.g. "Sita", 90
}
print("All:", ____)
print("S1 name:", dict_data[____][____])
print("S2 marks:", dict_data[____][____])
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `S1: Ram/85`, `S2: Sita/90` |
| **Example output** | `S1 name: Ram`<br>`S2 marks: 90` |

<a href="../../.faculty/solutions/o4u8ve.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-5"></a>

## Unit 4A Task 5: Print keys, values and items with loops

Loops over keys, values, and items.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A sample dictionary

**Process**
- `for key in d:` — keys
- `for value in d.values():` — values
- `for key, value in d.items():` — pairs

**Output**
- Printed keys, values, and pairs

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
dict_data = {"maths": 80, "science": 75, "english": 90}

print("Keys:")
for key in ____:
    print(key)

print("Values:")
for value in dict_data.____():
    print(value)

print("Items:")
for key, value in dict_data.____():
    print(key, "→", value)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `dict_data = {"maths": 80, "science": 75, "english": 90}` |
| **Example output** | prints each key, each value, then each `key → value` pair |

<a href="../../.faculty/solutions/p5v9wf.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-6"></a>

## Unit 4A Task 6: Squares and even numbers with list comprehension

Builds lists of squares and even numbers using list comprehension.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A range or list of numbers (for example 1 to 10)

**Process**
- Squares: `[x * x for x in ...]`
- Evens: `[x for x in ... if x % 2 == 0]`

**Output**
- List of squares and list of even numbers

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = range(____, ____)  # e.g. 1 to 10 inclusive → range(1, 11)

list_squares = [____ for x in list_data]
list_evens = [____ for x in list_data if ____]

print("Squares:", ____)
print("Evens:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | numbers 1 through 10 |
| **Example output** | `Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`<br>`Evens: [2, 4, 6, 8, 10]` |

<a href="../../.faculty/solutions/q6w0xg.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-7"></a>

## Unit 4A Task 7: Number-to-square dictionary comprehension

Builds a dictionary using a comprehension (for example number → square).

### Analyse the problem: Identify Input, Process and Output

**Input**
- A range or list of numbers

**Process**
- Form: `{key_expr: value_expr for item in sequence}`
- Example: `{x: x * x for x in range(1, 6)}`

**Output**
- The resulting dictionary

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
dict_data = {____: ____ for x in range(1, 6)}
print("Squares dict:", ____)

# optional: only even keys
dict_even_squares = {____: ____ for x in range(1, 11) if ____}
print("Even squares:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `range(1, 6)` for squares |
| **Example output** | `Squares dict: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}` |

<a href="../../.faculty/solutions/r7x1yh.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-8"></a>

## Unit 4A Task 8: Merge two dictionaries with update()

Combines two dictionaries into one using the `update()` method.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two dictionaries

**Process**
- Make a copy of the first dictionary (so the original is not changed)
- Call `update()` with the second dictionary
- Keys already present are overwritten by values from the second dictionary

**Output**
- The merged dictionary

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
dict_data = ____  # e.g. {"a": 1, "b": 2}
dict_extra = ____  # e.g. {"b": 3, "c": 4}

dict_merged = dict_data.____()  # copy
dict_merged.____(dict_extra)  # update
print("Merged:", ____)
```

> **Hint:** `update()` changes the dictionary in place. Copy first if you need to keep `dict_data` unchanged. If both have the same key, the value from `dict_extra` is kept.

### Example

| Item | Details |
|------|---------|
| **Example input** | `dict_data = {"a": 1, "b": 2}`, `dict_extra = {"b": 3, "c": 4}` |
| **Example output** | `Merged: {'a': 1, 'b': 3, 'c': 4}` |

<a href="../../.faculty/solutions/s8y2zi.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-9"></a>

## Unit 4A Task 9: Student name, marks and grade record

Stores name, marks, and grade in a dictionary and displays them.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Student name and marks (grade may be computed or given)

**Process**
- Store fields in a dictionary
- Optionally compute grade from marks with `if` / `elif`
- Print each field

**Output**
- Student record (name, marks, grade)

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
name = ____  # e.g. "Krishna"
marks = ____  # e.g. 86

if marks >= 90:
    grade = ____
elif marks >= 80:
    grade = ____
elif marks >= 70:
    grade = ____
else:
    grade = ____

dict_data = {"name": ____, "marks": ____, "grade": ____}
print("Record:", ____)
for key, value in dict_data.____():
    print(f"{key}: {value}")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | name `Krishna`, marks `86` |
| **Example output** | `name: Krishna`<br>`marks: 86`<br>`grade: B` (if 80–89 → B) |

<a href="../../.faculty/solutions/t9z3aj.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4a-task-10"></a>

## Unit 4A Task 10: Sort student dictionaries by marks

Sorts a list of dictionaries by a chosen key.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A list of dictionaries (for example students with `name` and `marks`)

**Process**
- Use `sorted(list_data, key=lambda d: d["marks"])` (or another key)
- `reverse=True` for descending order if needed

**Output**
- Sorted list of dictionaries

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = [
    {"name": "Anu", "marks": 75},
    {"name": "Ravi", "marks": 90},
    {"name": "Sita", "marks": 82},
]

list_by_marks = sorted(list_data, key=lambda d: d[____])
print("By marks ascending:", ____)

list_by_marks_desc = sorted(list_data, key=lambda d: d[____], reverse=____)
print("By marks descending:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | Anu 75, Ravi 90, Sita 82 |
| **Example output** | ascending: Anu, Sita, Ravi · descending: Ravi, Sita, Anu |

<a href="../../.faculty/solutions/u1b5ck.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-1"></a>

## Unit 4B Task 1: Catch ZeroDivisionError when dividing by zero

Catches `ZeroDivisionError` with `try` / `except` when dividing 10 by 0.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values that may cause an error (for example dividing by zero, or an invalid index)

**Process**
- Put risky code inside `try`
- Catch the error with `except ExceptionType`
- Print a clear message instead of letting the program stop

**Output**
- Either the normal result, or a handled error message

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
try:
    a = ____  # e.g. 10
    b = ____  # e.g. 0
    result = a / b
    print("Result:", ____)
except ____:  # ZeroDivisionError
    print("Cannot divide by zero.")
```

> **Hint:** Code after a successful `try` still runs only if no exception occurred. The `except` block runs only when that error happens.

### Example

| Item | Details |
|------|---------|
| **Example input** | `a = 10`, `b = 0` |
| **Example output** | `Cannot divide by zero.` |

<a href="../../.faculty/solutions/v2c6dl.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-2"></a>

## Unit 4B Task 2: Handle ValueError and IndexError for a list index

Reads a list index from the user and handles `ValueError` and `IndexError` with separate `except` blocks.

### Analyse the problem: Identify Input, Process and Output

**Input**
- User values or sample data that can raise different exceptions

**Process**
- Use one `try` block
- Add multiple `except` clauses (for example `ValueError`, `IndexError`, `ZeroDivisionError`)
- Print a message specific to each error type

**Output**
- A message matching which exception occurred

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
list_data = [10, 20, 30]
try:
    index = int(____)  # e.g. input("Enter index: ")
    value = list_data[____]
    print("Value:", ____)
except ____:  # ValueError — non-integer input
    print("Please enter a valid integer index.")
except ____:  # IndexError — index out of range
    print("Index is out of range.")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | index `5` (list has only 3 items) |
| **Example output** | `Index is out of range.` |

<a href="../../.faculty/solutions/w3d7em.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-3"></a>

## Unit 4B Task 3: Convert text to int, print square with else/finally

Converts entered text to an integer and prints its square using `try` / `except` / `else` / `finally` (focus: `else` and `finally`, not division).

### Analyse the problem: Identify Input, Process and Output

**Input**
- Text that should represent an integer (for example `5` or `abc`)

**Process**
- `try`: convert with `int()`
- `except ValueError`: handle non-integer text
- `else`: runs only when conversion succeeded — print the square
- `finally`: always runs (closing message)

**Output**
- Square of the number, or an error message, plus a final message that always appears

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
try:
    text = ____  # e.g. input("Enter a number: ")
    number = int(____)
except ____:  # ValueError
    print("That is not a valid integer.")
else:
    print("Square:", ____)  # e.g. number * number
finally:
    print(____)  # e.g. "Program finished."
```

> **Hint:** `else` is for the success path. `finally` runs whether the code succeeded or failed. Division with `ZeroDivisionError` is covered in Task 4.

### Example

| Item | Details |
|------|---------|
| **Example input** | `5` |
| **Example output** | `Square: 25`<br>`Program finished.` |
| **Example input** | `abc` |
| **Example output** | `That is not a valid integer.`<br>`Program finished.` |

<a href="../../.faculty/solutions/x4e8fn.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-4"></a>

## Unit 4B Task 4: Read numerator/denominator with ZeroDivisionError and ValueError

Reads numerator and denominator from the user and handles invalid conversion and division by zero.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Numerator and denominator from the user (as text)

**Process**
- Convert inputs with `int()` or `float()` (may raise `ValueError`)
- Divide the numbers (may raise `ZeroDivisionError`)
- Catch each exception separately

**Output**
- Quotient, or a specific error message

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
try:
    num = ____(input("Enter numerator: "))  # int or float
    den = ____(input("Enter denominator: "))
    print("Quotient:", num / ____)
except ____:
    print("Denominator cannot be zero.")
except ____:
    print("Please enter valid numbers.")
```

### Example

| Item | Details |
|------|---------|
| **Example input** | numerator `12`, denominator `abc` |
| **Example output** | `Please enter valid numbers.` |

<a href="../../.faculty/solutions/y5f9go.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-5"></a>

## Unit 4B Task 5: Raise ValueError if age is negative

Uses `raise ValueError` when the entered age is negative.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A value that must satisfy a rule (for example age must be positive)

**Process**
- Check the rule with `if`
- Use `raise ValueError("message")` (or another exception) when the rule fails
- Catch the raised exception with `try` / `except` and print the message

**Output**
- Confirmation if valid, or the raised error message if invalid

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
try:
    age = int(____)
    if age < ____:  # e.g. 0
        raise ____("Age cannot be negative.")
    print("Valid age:", ____)
except ____ as err:
    print("Error:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | age `-3` |
| **Example output** | `Error: Age cannot be negative.` |

<a href="../../.faculty/solutions/z6g0hp.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-6"></a>

## Unit 4B Task 6: Raise InvalidSpeedError for invalid vehicle speed

Raises a custom `InvalidSpeedError` when vehicle speed is outside 0–120 km/h.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A vehicle speed in km/h (must be between 0 and 120)

**Process**
- Define `class MyError(Exception): pass` (choose a clear name, for example `InvalidSpeedError`)
- Raise your custom exception when the value is invalid
- Catch that custom type in `except`

**Output**
- Success message, or the custom exception message

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class ____(Exception):  # e.g. InvalidSpeedError
    pass

try:
    speed = int(____)  # e.g. input("Enter speed (km/h): ")
    if speed < 0 or speed > ____:  # e.g. 120
        raise ____("Speed must be between 0 and 120.")
    print("Speed accepted:", ____)
except ____ as err:
    print("Custom error:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | speed `150` |
| **Example output** | `Custom error: Speed must be between 0 and 120.` |

<a href="../../.faculty/solutions/a7h1iq.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4b-task-7"></a>

## Unit 4B Task 7: Validate marks 0–100 with InvalidMarksError and Pass/Fail

Validates student marks (0–100) with `InvalidMarksError`, prints Pass/Fail (≥40), and uses `finally`.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Student marks entered as text (must be a number between 0 and 100)

**Process**
- Define a custom exception class (for example `InvalidMarksError`)
- Convert input with `int()` (may raise `ValueError`)
- If marks are outside 0–100, `raise` the custom exception
- If marks are valid: print Pass when marks ≥ 40, otherwise Fail
- Catch `ValueError` and the custom exception separately (specific exceptions)
- Use `finally` for a message that always runs

**Output**
- Pass / Fail, or an error message; then the `finally` message

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class ____(Exception):  # e.g. InvalidMarksError
    pass

try:
    marks = int(input(____))  # e.g. "Enter student marks: "
    if marks < ____ or marks > ____:
        raise ____("Marks must be between 0 and 100")
    if marks >= ____:  # e.g. 40
        print("Result: Pass")
    else:
        print("Result: Fail")
except ____:
    print("Error: Please enter numbers only.")
except ____ as e:
    print("Invalid Input:", ____)
finally:
    print(____)  # e.g. "Marks processing completed."
```

> **Hint:** Catch `ValueError` for non-numeric input and your custom exception for out-of-range marks. `finally` runs whether the result was Pass, Fail, or an error.

### Example

| Input | Expected output |
|-------|-----------------|
| `75` | `Result: Pass`<br>`Marks processing completed.` |
| `25` | `Result: Fail`<br>`Marks processing completed.` |
| `abc` | `Error: Please enter numbers only.`<br>`Marks processing completed.` |
| `120` | `Invalid Input: Marks must be between 0 and 100`<br>`Marks processing completed.` |
| `-5` | `Invalid Input: Marks must be between 0 and 100`<br>`Marks processing completed.` |

> **Note:** The `finally` block always prints `Marks processing completed.` after the result or error message.

<a href="../../.faculty/solutions/b8i2jr.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4c-task-1"></a>

## Unit 4C Task 1: Read and display sample.txt

Opens `sample.txt`, reads its content, and displays it.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A text file name (for example `sample.txt`) that already exists

**Process**
- Open the file with `open(filename, "r")` (prefer `with open(...)`)
- Read content with `read()` (or read line by line)
- Close is automatic when using `with`

**Output**
- The full file content printed to the screen

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
filename = ____  # e.g. "sample.txt"
with open(filename, ____) as file:  # "r"
    content = file.____()
print(____)
```

> **Hint:** Create a small `sample.txt` in the same folder before running, or ask the user for the file name.

### Example

| Item | Details |
|------|---------|
| **Example file** | `sample.txt` containing `Hello Python` |
| **Example output** | `Hello Python` |

<a href="../../.faculty/solutions/c9j3ks.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4c-task-2"></a>

## Unit 4C Task 2: Write a line of text to output.txt

Writes a line of text into `output.txt` (creates the file if it does not exist).

### Analyse the problem: Identify Input, Process and Output

**Input**
- File name and the text to write (from the program or from the user)

**Process**
- Open with mode `"w"` (overwrite) or `"a"` (append)
- Use `write()` or `writelines()`
- Prefer `with open(...)` so the file closes safely

**Output**
- Confirmation message; the file on disk contains the written text

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
filename = ____  # e.g. "output.txt"
text = ____  # e.g. "Learning file handling in Python."
with open(filename, ____) as file:  # "w"
    file.____(text)
print("Data written to", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | write `Learning file handling in Python.` to `output.txt` |
| **Example output** | `Data written to output.txt` (and the file holds that line) |

<a href="../../.faculty/solutions/d0k4lt.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4c-task-3"></a>

## Unit 4C Task 3: Count lines, words and characters in a file

Reads a text file and reports how many lines, words, and characters it has.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A text file name

**Process**
- Read all lines (or the full text)
- Lines: number of lines (for example `len(readlines())`)
- Words: split the text on whitespace and count
- Characters: `len(text)` (decide whether to include spaces/newlines and stay consistent)

**Output**
- Counts for lines, words, and characters

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
filename = ____
with open(filename, "r") as file:
    text = file.____()

line_count = len(text.____("\n"))  # or use readlines()
word_count = len(text.____())
char_count = len(____)

print("Lines:", ____)
print("Words:", ____)
print("Characters:", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example file** | two lines: `Hello world` and `Python files` |
| **Example output** | Lines `2`, Words `4`, Characters includes letters and spaces/newlines |

<a href="../../.faculty/solutions/e1l5mu.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4c-task-4"></a>

## Unit 4C Task 4: Copy sample.txt into copy.txt

Copies everything from `sample.txt` into `copy.txt`.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Source file name and destination file name

**Process**
- Open source in `"r"` and destination in `"w"`
- Read from source and write to destination
- You may use nested `with` statements

**Output**
- Destination file contains the same text; print a success message

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
source = ____  # e.g. "sample.txt"
destination = ____  # e.g. "copy.txt"
with open(source, "r") as src:
    content = src.____()
with open(destination, ____) as dest:  # "w"
    dest.____(content)
print("Copied from", source, "to", ____)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | source `sample.txt`, destination `copy.txt` |
| **Example output** | `Copied from sample.txt to copy.txt` |

<a href="../../.faculty/solutions/f2m6nv.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---

<a id="unit-4c-task-5"></a>

## Unit 4C Task 5: Replace a word in a text file (e.g. Python → Java)

Finds a word in a text file and replaces it with another word, then saves the result.

### Analyse the problem: Identify Input, Process and Output

**Input**
- File name, the word to find, and the replacement word

**Process**
- Read the full file content
- Use `str.replace(old, new)` (or replace only the first occurrence if required)
- Write the updated text back (same file or a new file — state which you chose)

**Output**
- Confirmation; opening the file shows the replaced text

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
filename = ____
old_word = ____  # e.g. "Python"
new_word = ____  # e.g. "Java"

with open(filename, "r") as file:
    content = file.____()

updated = content.____(old_word, new_word)

with open(filename, ____) as file:  # "w" to overwrite
    file.____(updated)

print("Replaced", old_word, "with", ____)
```

> **Hint:** `replace` changes every occurrence. Test with a small file first so you do not overwrite important data by mistake.

### Example

| Item | Details |
|------|---------|
| **Example input** | file has `I love Python`, replace `Python` → `Java` |
| **Example output** | file becomes `I love Java` |

<a href="../../.faculty/solutions/g3n7ow.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit4-dictionaries-and-exception-handling.md).

---
