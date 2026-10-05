# Unit 2B Task 9 — Example solution

Count the digits of a number using a `while` loop.

```python
# Example solution: count digits using a while loop
number = int(input("Enter a number: "))

original_number = number
digit_count = 0

if number == 0:
    digit_count = 1
else:
    while number > 0:
        digit_count = digit_count + 1
        number = number // 10

print(f"Number of digits in {original_number} is {digit_count}")
```

[Back to hint](../../docs/hints.md#unit-2b-task-9) · [Back to lab tasks](../../docs/lab-tasks.md)
