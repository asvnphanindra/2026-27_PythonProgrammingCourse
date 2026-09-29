# Unit 2B Task 8 — Example solution

Sum of digits of a number using a `while` loop.

```python
# Example solution: sum of digits using a while loop
number = int(input("Enter a number: "))

original_number = number
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum = digit_sum + digit
    number = number // 10

print(f"Sum of digits of {original_number} is {digit_sum}")
```
