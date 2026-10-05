# Unit 2C Task 12 — Example solution

Print a pyramid of numbers from 1 to 10.

```python
# Example solution: pyramid pattern of numbers from 1 to 10
num = 1
rows = 4

for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var in range(1, row_loop_var + 1):
        if num <= 10:
            print(num, end=" ")
            num = num + 1
    print()
```

[Back to lab tasks](../../docs/lab-tasks.md)
