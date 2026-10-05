# Unit 2C Task 4 — Example solution

Print numbers 1 to 9 in a 3x3 grid using while-for nested loops.

```python
# Example solution: 3x3 grid of numbers (while-for)
num = 1
row_loop_var = 1

while row_loop_var <= 3:
    for column_loop_var in range(1, 4):
        print(num, end=" ")
        num = num + 1
    print()
    row_loop_var = row_loop_var + 1
```

[Back to hint](../../docs/hints.md#unit-2c-task-4) · [Back to lab tasks](../../docs/lab-tasks.md)
