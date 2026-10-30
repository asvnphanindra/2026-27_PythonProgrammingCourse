# Unit 3A Task 5 — Example solution

Matrix addition using nested lists.

```python
# Example solution: matrix addition with nested lists
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

rows = len(matrix_a)
cols = len(matrix_a[0])

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("Sum:", result)
```

[Back to hint](../../docs/hints.md#unit-3a-task-5) · [Back to lab tasks](../../docs/lab-tasks.md)
