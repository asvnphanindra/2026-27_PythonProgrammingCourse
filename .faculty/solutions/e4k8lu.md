# Unit 3D Task 10 (Optional) — Example solution

Global counter incremented with the `global` keyword.

```python
# Example solution: global counter increment
counter = 0

def increment():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)

print("Before:", counter)
increment()
print("After:", counter)
```

[Back to hint](../../docs/hints.md#unit-3d-task-10) · [Back to lab tasks](../../docs/lab-tasks/README.md)
