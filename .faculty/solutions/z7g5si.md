# Unit 2C Task 14 — Example solution

Print Floyd's triangle.

```python
# Example solution: Floyd's triangle
rows = int(input("Enter number of rows: "))
num = 1

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(num, end=" ")
        num = num + 1
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
