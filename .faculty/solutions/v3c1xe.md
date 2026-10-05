# Unit 2C Task 3 — Example solution

Print numbers 1 to 9 in a 3x3 grid using for-for nested loops.

```python
# Example solution: 3x3 grid of numbers (for-for)
num = 1
rows = 3

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        print(num, end=" ")
        num = num + 1
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-3) · [Back to lab tasks](../../docs/lab-tasks.md)
