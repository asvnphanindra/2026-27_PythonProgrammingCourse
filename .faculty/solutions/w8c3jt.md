# Unit 2B Task 3 — Example solution

Sum and average of N numbers using a `for` loop.

```python
total_input_numbers = int(input("Enter how many numbers: "))

total_sum = 0

for count in range(total_input_numbers):
    number = float(input("Enter a number: "))
    total_sum = total_sum + number

average = total_sum / total_input_numbers

print(f"Sum = {total_sum}")
print(f"Average = {average}")
```
