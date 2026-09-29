# Unit 2B Task 2 — Example solution

Multiplication table of a number (1 to 10). Both approaches below.

## Approach 1: for loop

```python
# Example solution: multiplication table using a for loop
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
```

## Approach 2: while loop

```python
# Example solution: multiplication table using a while loop
number = int(input("Enter a number: "))

multiplier = 1
while multiplier <= 10:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier = multiplier + 1
```
