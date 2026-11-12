# Unit 3D Task 6 — Example solution

`print_details(**kwargs)` printing each key–value pair.

```python
# Example solution: print_details with **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krishna", age=26, city="Guntur")
```

[Back to hint](../../docs/hints.md#unit-3d-task-6) · [Back to lab tasks](../../docs/lab-tasks/README.md)
