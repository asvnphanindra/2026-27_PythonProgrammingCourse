# Unit 3D Task 13 — Example solution

Fibonacci series using a recursive term function.

```python
# Example solution: Fibonacci series using recursion
def fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

n = 7
for i in range(n):
    print(fib(i), end=" ")
```

[Back to hint](../../docs/hints.md#unit-3d-task-13) · [Back to lab tasks](../../docs/lab-tasks.md)
