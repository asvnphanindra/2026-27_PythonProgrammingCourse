# Unit 4B Task 7 — Example solution

Validate student marks 0–100 with InvalidMarksError, print Pass/Fail (≥40), and use finally.

```python
# Example solution: robust input validation for student marks
class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
except ValueError:
    print("Error: Please enter numbers only.")
except InvalidMarksError as e:
    print("Invalid Input:", e)
finally:
    print("Marks processing completed.")
```

**Sample checks**

| Input | Expected output |
|-------|-----------------|
| `75` | `Result: Pass` then `Marks processing completed.` |
| `25` | `Result: Fail` then `Marks processing completed.` |
| `abc` | `Error: Please enter numbers only.` then `Marks processing completed.` |
| `120` | `Invalid Input: Marks must be between 0 and 100` then `Marks processing completed.` |
| `-5` | `Invalid Input: Marks must be between 0 and 100` then `Marks processing completed.` |

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4b-task-7) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
