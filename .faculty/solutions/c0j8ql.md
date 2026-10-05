# Unit 2C Task 10 — Example solution

Print a diamond pattern of stars.

```python
# Example solution: diamond pattern of stars
n = int(input("Enter number of rows (half diamond): "))

# Upper half (including middle)
for row_var in range(1, n + 1):
    for col_var in range(n - row_var):
        print(" ", end=" ")
    for col_var in range(row_var):
        print("*", end=" ")
    print()

# Lower half
for row_var in range(n - 1, 0, -1):
    for col_var in range(n - row_var):
        print(" ", end=" ")
    for col_var in range(row_var):
        print("*", end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-10) · [Back to lab tasks](../../docs/lab-tasks.md)
