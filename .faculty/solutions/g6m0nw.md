# Unit 3D Task 13 — Example solution

Factorial using recursion.

```python
# Example solution: factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
print("Factorial:", factorial(number))
```

[Back to hint](../../docs/hints.md#unit-3d-task-13) · [Back to lab tasks](../../docs/lab-tasks.md)
