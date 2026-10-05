# Unit 2A Task 8 — Example solution

Check whether a number is prime or not (input between 1 and 100).
Uses an `if-elif-else` ladder only — no `for` loop.

```python
# Example solution: prime check with if-elif ladder (1 to 100)
number = int(input("Enter a number between 1 and 100: "))

if number < 1 or number > 100:
    print(f"{number} is not between 1 and 100")
elif number == 1:
    print(f"{number} is not a prime number")
elif number == 2 or number == 3 or number == 5 or number == 7:
    print(f"{number} is a prime number")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")
```

> **Think about it:** This program assumes the input is between `1` and `100` (and the checks use only `2`, `3`, `5`, and `7`). How would you generalize this code so it works for **any** positive number, not only values between `1` and `100`?

[Back to hint](../../docs/hints.md#unit-2a-task-8) · [Back to lab tasks](../../docs/lab-tasks.md)
