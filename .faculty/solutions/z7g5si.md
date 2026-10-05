# Unit 2C Task 7 — Example solution

Print Floyd's triangle.

```python
# Example solution: Floyd's triangle
n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()
```

[Back to hint](../../docs/hints.md#unit-2c-task-7) · [Back to lab tasks](../../docs/lab-tasks.md)
