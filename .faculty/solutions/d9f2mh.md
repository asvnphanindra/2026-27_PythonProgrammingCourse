# Unit 2B Task 10 — Example solution

Reverse a number using a `while` loop.

```python
# Example solution: reverse a number using a while loop
number = int(input("Enter a number: "))

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(f"Reverse of {original_number} is {reversed_number}")
```
