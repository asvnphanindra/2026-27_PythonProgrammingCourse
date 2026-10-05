# Unit 2C Task 6 — Example solution

Print Pascal's triangle for n rows.

```python
# Example solution: Pascal's triangle
n = int(input("Enter number of rows: "))

for row in range(n):
    value = 1
    for col in range(row + 1):
        print(value, end=" ")
        value = value * (row - col) // (col + 1)
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-6) · [Back to lab tasks](../../docs/lab-tasks.md)
