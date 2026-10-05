# Unit 2C Task 11 — Example solution

Print a right-angled triangle pattern of zeros.

```python
# Example solution: right-angled triangle of zeros
rows = 3

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(0, end=" ")
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
