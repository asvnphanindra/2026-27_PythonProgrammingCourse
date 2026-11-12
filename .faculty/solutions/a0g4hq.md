# Unit 3D Task 8 — Example solution

Student details displayed using `**kwargs`.

```python
# Example solution: student details with **kwargs
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(name="Anu", maths=85, science=90)
```

[Back to hint](../../docs/hints.md#unit-3d-task-8) · [Back to lab tasks](../../docs/lab-tasks/README.md)
