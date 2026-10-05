# Unit 2C Task 7 — Example solution

Print a right-angled triangle using a symbol read from the user (`*` or `0`, etc.).

```python
# Example solution: right-angled triangle (any symbol)
rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to print (e.g. * or 0): ")

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(symbol, end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-7) · [Back to lab tasks](../../docs/lab-tasks.md)
