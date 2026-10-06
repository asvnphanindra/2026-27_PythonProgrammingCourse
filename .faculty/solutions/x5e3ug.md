# Unit 2C Task 12 — Example solution

Print a centered pyramid pattern of numbers.

```python
# Example solution: centered number pyramid
rows = 5

for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var in range(1, 2 * row_loop_var):
        print(column_loop_var, end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-12) · [Back to lab tasks](../../docs/lab-tasks.md)
