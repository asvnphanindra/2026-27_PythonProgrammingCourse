# Unit 2C Task 9 — Example solution

Print an inverted right-angled triangle of stars.

```python
# Example solution: inverted right-angled triangle of stars
n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-9) · [Back to lab tasks](../../docs/lab-tasks.md)
