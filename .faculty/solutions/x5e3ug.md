# Unit 2C Task 5 — Example solution

Print a pyramid of numbers from 1 to 10.

```python
# Example solution: pyramid pattern of numbers from 1 to 10
num = 1
rows = 4

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        if num <= 10:
            print(num, end=" ")
            num = num + 1
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-5) · [Back to lab tasks](../../docs/lab-tasks.md)
