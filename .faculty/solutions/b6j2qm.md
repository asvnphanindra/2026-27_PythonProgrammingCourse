# Unit 2B Task 7 — Example solution

Fibonacci series up to N terms using a `for` loop.

```python
# Example solution: Fibonacci series up to N terms using a for loop
n = int(input("Enter how many terms: "))

first = 0
second = 1

for count in range(n):
    print(f"Term {count + 1} of {n} is {first}")
    next_term = first + second
    first = second
    second = next_term
```
