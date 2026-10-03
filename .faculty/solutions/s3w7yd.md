# Unit 2C Task 7 — Example solution

Prime numbers between 1 and N using nested `for` loops and divisor count.

```python
# Example solution: primes from 1 to N using divisor count
n = int(input("Enter the value of N: "))

for number in range(1, n + 1):
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        print(f"{number} is a prime number between 1 and {n}")
```
