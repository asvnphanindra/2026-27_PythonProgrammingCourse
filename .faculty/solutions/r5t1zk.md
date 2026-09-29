# Unit 2B Task 6 — Example solution

Prime numbers between 1 and N using `for` loops.

```python
# Example solution: prime numbers from 1 to N using for loops
n = int(input("Enter the value of N: "))

for number in range(2, n + 1):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number between 1 and {n}")
```
