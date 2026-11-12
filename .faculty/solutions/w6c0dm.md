# Unit 3D Task 3 — Example solution

Marks total and average using a function with parameters and return values.

```python
# Example solution: marks total and average (function)
def total_and_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average

m1, m2, m3 = 80, 70, 90
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:", average)
```

[Back to hint](../../docs/hints.md#unit-3d-task-3) · [Back to lab tasks](../../docs/lab-tasks/README.md)
