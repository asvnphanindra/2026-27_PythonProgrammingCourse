# Unit 4B Task 4 — Example solution

Handle ZeroDivisionError and ValueError.

```python
# Example solution: ZeroDivisionError and ValueError
try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))
    print("Quotient:", num / den)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Please enter valid numbers.")
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4b-task-4) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
