# Unit 3D Task 5 — Example solution

Sum of any number of values using `*args`.

```python
# Example solution: sum using *args
def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total

print(sum_values(1, 2, 3))
print(sum_values(10, 20, 30, 40))
```

[Back to hint](../../docs/hints.md#unit-3d-task-5) · [Back to lab tasks](../../docs/lab-tasks/README.md)
