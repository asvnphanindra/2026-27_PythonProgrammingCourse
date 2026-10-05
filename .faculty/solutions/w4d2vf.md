# Unit 2C Task 4 — Example solution

Print numbers 1 to 9 in a 3x3 grid using while-for nested loops.

```python
# Example solution: 3x3 grid of numbers (while-for)
num = 1
row_var = 1

while row_var <= 3:
    for col_var in range(3):
        print(num, end=" ")
        num = num + 1
    print()
    row_var = row_var + 1
```

[Back to hint](../../docs/hints.md#unit-2c-task-4) · [Back to lab tasks](../../docs/lab-tasks.md)
