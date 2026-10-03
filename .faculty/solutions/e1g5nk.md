# Unit 2B Task 11 — Example solution

Check whether a 3-digit number is an Armstrong number using a `while` loop.
Assume the number has 3 digits (power = 3).

```python
# Example solution: 3-digit Armstrong number check using a while loop
number = int(input("Enter a 3-digit number: "))

original_number = number
armstrong_sum = 0

while number > 0:
    digit = number % 10
    armstrong_sum = armstrong_sum + digit ** 3
    number = number // 10

if armstrong_sum == original_number:
    print(
        f"{original_number} is an Armstrong number "
        f"(sum of cubes of digits is {armstrong_sum})"
    )
else:
    print(
        f"{original_number} is not an Armstrong number "
        f"(sum of cubes of digits is {armstrong_sum})"
    )
```

> **Think about it:** This program assumes the number has **3 digits** (power `3`). How would you generalize this code so it works for a number with **any** number of digits, not only 3-digit numbers?
