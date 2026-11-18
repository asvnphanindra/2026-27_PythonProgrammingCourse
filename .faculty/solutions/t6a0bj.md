# Unit 5C Task 3 — Example solution

Create a custom package with multiple modules.

**Package layout:**

```text
mypackage/
  __init__.py
  greetings.py
  calc.py
```

**`mypackage/greetings.py`:**

```python
def hello(name):
    return f"Hello, {name}"
```

**`mypackage/calc.py`:**

```python
def add(a, b):
    return a + b
```

**`mypackage/__init__.py`:** (can be empty)

**Main file** `Unit-5C_Task-3_Custom_Package.py`:

```python
# Example solution: custom package with multiple modules
from mypackage.greetings import hello
from mypackage.calc import add

print(hello("Anu"))
print("Sum:", add(2, 3))
```

[Back to hint](../../docs/hints.md#unit-5c-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
