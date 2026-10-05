# Unit 2C Task 8 — Example solution

Print a right-angled triangle of stars.

```python
# Example solution: right-angled triangle of stars
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-8) · [Back to lab tasks](../../docs/lab-tasks.md)
