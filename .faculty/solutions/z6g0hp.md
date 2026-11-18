# Unit 4B Task 5 — Example solution

Demonstrate raising exceptions using raise.

```python
# Example solution: raise an exception
try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Valid age:", age)
except ValueError as err:
    print("Error:", err)
```

[Back to hint](../../docs/hints.md#unit-4b-task-5) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
