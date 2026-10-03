# Unit 2B Task 6 — Example solution

Check whether a number is prime or not using a `for` loop and divisor count.
Assume the input is between 1 and 100 for this task.

```python
# Example solution: prime check using divisor count (for loop)
number = int(input("Enter a number between 1 and 100: "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print(f"{number} is a prime number (divisor count = {count})")
else:
    print(f"{number} is not a prime number (divisor count = {count})")
```

> **Think about it:** This program assumes the input is between `1` and `100`. How would you generalize this code so it works for **any** positive number, not only values between `1` and `100`?
