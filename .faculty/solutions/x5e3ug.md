# Unit 2C Task 5 — Example solution

Print a pyramid of numbers from 1 to 10.

```python
# Example solution: pyramid pattern of numbers from 1 to 10
num = 1
rows = 4

for row_var in range(1, rows + 1):
    for col_var in range(rows - row_var):
        print(" ", end=" ")
    for col_var in range(row_var):
        if num <= 10:
            print(num, end=" ")
            num = num + 1
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-5) · [Back to lab tasks](../../docs/lab-tasks.md)
