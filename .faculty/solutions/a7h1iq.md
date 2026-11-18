# Unit 4B Task 6 — Example solution

Create and raise a custom exception.

```python
# Example solution: custom exception
class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Marks accepted:", marks)
except InvalidMarksError as err:
    print("Custom error:", err)
except ValueError:
    print("Please enter a valid integer.")
```

[Back to hint](../../docs/hints.md#unit-4b-task-6) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
