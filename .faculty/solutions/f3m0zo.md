# Unit 2C Task 13 — Example solution

Print a centered pyramid pattern of stars.

```python
# Example solution: centered pyramid of stars
rows = 3

for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        print("*", end=" ")
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
