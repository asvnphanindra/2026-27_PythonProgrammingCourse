# Unit 2C Task 8 — Example solution

Print an inverted right-angled triangle of stars.

```python
# Example solution: inverted right-angled triangle of stars
rows = int(input("Enter number of rows: "))

for row_loop_var in range(rows, 0, -1):
    for column_loop_var in range(1, row_loop_var + 1):
        print("*", end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-8) · [Back to lab tasks](../../docs/lab-tasks.md)
