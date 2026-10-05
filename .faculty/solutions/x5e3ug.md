# Unit 2C Task 5 — Example solution

Print a number right-angled triangle pattern.

```python
# Example solution: number right-angled triangle
rows = 6

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(column_loop_var, end=" ")
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
