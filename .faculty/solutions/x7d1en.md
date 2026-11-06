# Unit 3D Task 4 — Example solution

Simple interest with a default rate argument.

```python
# Example solution: simple interest with default arguments
def simple_interest(principal, time, rate=5):
    return (principal * time * rate) / 100

print("SI (default rate):", simple_interest(1000, 2))
print("SI (rate=8):", simple_interest(1000, 2, 8))
```

[Back to hint](../../docs/hints.md#unit-3d-task-4) · [Back to lab tasks](../../docs/lab-tasks.md)
