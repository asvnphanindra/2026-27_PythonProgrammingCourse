# Unit 2C Task 10 — Example solution

Print a diamond pattern of stars.

```python
# Example solution: diamond pattern of stars
n = int(input("Enter number of rows (half diamond): "))

# Upper half (including middle)
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(i):
        print("*", end=" ")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(i):
        print("*", end=" ")
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-10) · [Back to lab tasks](../../docs/lab-tasks.md)
