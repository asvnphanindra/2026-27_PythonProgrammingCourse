# Unit 2B Task 11 — Example solution

Check whether a number is an Armstrong number using a `while` loop.

```python
# Example solution: Armstrong number check using a while loop
number = int(input("Enter a number: "))

original_number = number
digit_count = 0
temp = number

if temp == 0:
    digit_count = 1
else:
    while temp > 0:
        digit_count = digit_count + 1
        temp = temp // 10

armstrong_sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    armstrong_sum = armstrong_sum + digit ** digit_count
    temp = temp // 10

if armstrong_sum == original_number:
    print(
        f"{original_number} is an Armstrong number "
        f"(sum of digits to power {digit_count} is {armstrong_sum})"
    )
else:
    print(
        f"{original_number} is not an Armstrong number "
        f"(sum of digits to power {digit_count} is {armstrong_sum})"
    )
```
