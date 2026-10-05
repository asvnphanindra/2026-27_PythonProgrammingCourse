# Unit 2C Task 5 — Example solution

Print a square grid of stars (5x5, then generalized with user input).

```python
# Example solution: star grid (generalized)
rows = int(input("Enter grid size (rows and columns): "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        print("*", end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-5) · [Back to lab tasks](../../docs/lab-tasks.md)
