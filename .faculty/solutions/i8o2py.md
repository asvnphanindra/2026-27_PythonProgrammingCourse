# Unit 3D Task 14 — Example solution

GCD of two numbers using recursion (Euclidean algorithm).

```python
# Example solution: GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

x, y = 48, 18
print("GCD:", gcd(x, y))
```

[Back to hint](../../docs/hints.md#unit-3d-task-14) · [Back to lab tasks](../../docs/lab-tasks/README.md)
