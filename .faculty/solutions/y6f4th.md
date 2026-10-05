# Unit 2C Task 12 — Example solution

Print Pascal's triangle for n rows.

```python
# Example solution: Pascal's triangle
rows = int(input("Enter number of rows: "))

for row_loop_var in range(1, rows + 1):
    value = 1
    for column_loop_var in range(1, row_loop_var + 1):
        print(value, end=" ")
        value = value * (row_loop_var - column_loop_var) // column_loop_var
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
