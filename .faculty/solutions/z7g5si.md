# Unit 2C Task 7 — Example solution

Print Floyd's triangle.

```python
# Example solution: Floyd's triangle
rows = 4
print_val = 1

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(print_val, end=" ")
        print_val = print_val + 1
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
