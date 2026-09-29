# Unit 2B Task 4 — Example solution

Largest number in a series of N numbers using a `for` loop.

```python
# Example solution: largest in a series of N numbers using a for loop
total_input_numbers = int(input("Enter how many numbers: "))

largest = float(input("Enter a number: "))

for count in range(total_input_numbers - 1):
    number = float(input("Enter a number: "))
    if number > largest:
        largest = number

print(f"Largest among {total_input_numbers} numbers is {largest}")
```
