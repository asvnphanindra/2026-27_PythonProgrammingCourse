# Unit 3D Task 9 — Example solution

Local variable does not change the global variable with the same name.

```python
# Example solution: local does not change global
x = 10

def demo():
    x = 20  # local assignment
    print("Inside function, x =", x)

demo()
print("Outside function, x =", x)
```

[Back to hint](../../docs/hints.md#unit-3d-task-9) · [Back to lab tasks](../../docs/lab-tasks/README.md)
