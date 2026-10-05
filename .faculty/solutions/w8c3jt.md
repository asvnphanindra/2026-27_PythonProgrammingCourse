# Unit 2B Task 3 — Example solution

Sum and average of N numbers using a `for` loop.

```python
# Example solution: sum and average of N numbers using a for loop
total_input_numbers = int(input("Enter how many numbers: "))

total_sum = 0

for count in range(total_input_numbers):
    number = float(input("Enter a number: "))
    total_sum = total_sum + number

average = total_sum / total_input_numbers

print(f"Sum of {total_input_numbers} numbers is {total_sum}")
print(f"Average of {total_input_numbers} numbers (sum {total_sum}) is {average}")
```

[Back to hint](../../docs/hints.md#unit-2b-task-3) · [Back to lab tasks](../../docs/lab-tasks.md)
