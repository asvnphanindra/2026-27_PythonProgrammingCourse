# Unit 2B Task 7 — Example solution

Fibonacci series up to N terms using a `for` loop.

```python
# Example solution: Fibonacci series up to N terms using a for loop
n = int(input("Enter how many terms: "))

first = 0
second = 1

for count in range(n):
    print(f"Fibonacci series term {count + 1} of {n} terms = {first}")
    next_term = first + second
    first = second
    second = next_term
```

[Back to hint](../../docs/hints.md#unit-2b-task-7) · [Back to lab tasks](../../docs/lab-tasks.md)
