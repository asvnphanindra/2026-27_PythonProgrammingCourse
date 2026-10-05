# Unit 2C Task 14 — Example solution

Print a hollow square pattern of stars.

```python
# Example solution: hollow square of stars
rows = 5

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        if (
            column_loop_var == 1
            or column_loop_var == rows
            or row_loop_var == 1
            or row_loop_var == rows
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
