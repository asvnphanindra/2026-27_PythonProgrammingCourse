# Unit 4B Task 3 — Example solution

Demonstrate try-except-else-finally blocks.

```python
# Example solution: try-except-else-finally
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Result:", result)
finally:
    print("Program finished.")
```

[Back to hint](../../docs/hints.md#unit-4b-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
