# Unit 4A Task 10 — Example solution

Sort a list of dictionaries based on a key.

```python
# Example solution: sort list of dictionaries
students = [
    {"name": "Anu", "marks": 75},
    {"name": "Ravi", "marks": 90},
    {"name": "Sita", "marks": 82},
]

by_marks = sorted(students, key=lambda d: d["marks"])
print("By marks ascending:", by_marks)

by_marks_desc = sorted(students, key=lambda d: d["marks"], reverse=True)
print("By marks descending:", by_marks_desc)
```

[Back to hint](../../docs/hints.md#unit-4a-task-10) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
