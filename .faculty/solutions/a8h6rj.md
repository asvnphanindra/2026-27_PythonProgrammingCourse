# Unit 2C Task 8 — Example solution

Print a diamond pattern of stars.

```python
# Example solution: diamond pattern of stars
rows = 3

# Upper half (including middle)
for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        print("*", end=" ")
    print()

# Lower half
for row_loop_var in range(rows - 1, 0, -1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        print("*", end=" ")
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
