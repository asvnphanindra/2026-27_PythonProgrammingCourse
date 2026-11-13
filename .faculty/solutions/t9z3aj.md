# Unit 4A Task 9 — Example solution

Student records (name, marks, grade) using a dictionary.

```python
# Example solution: student records dictionary
name = "Krishna"
marks = 86

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

student = {"name": name, "marks": marks, "grade": grade}
print("Record:", student)
for key, value in student.items():
    print(f"{key}: {value}")
```

[Back to hint](../../docs/hints.md#unit-4a-task-9) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
