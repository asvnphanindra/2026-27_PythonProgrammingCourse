# Unit 2C Task 6 — Example solution

Print Pascal's triangle for n rows.

```python
# Example solution: Pascal's triangle
n = int(input("Enter number of rows: "))

for row_var in range(n):
    value = 1
    for col_var in range(row_var + 1):
        print(value, end=" ")
        value = value * (row_var - col_var) // (col_var + 1)
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-6) · [Back to lab tasks](../../docs/lab-tasks.md)
